import os

import numpy as np
from django.conf import settings
from scipy.stats import norm
from scipy.special import erf
from typing import Literal
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')


def approx_demo(
        paramtype: Literal["std", "var", "snr_r", "snr_c"],
        varvalue: float,
        show_pnxi: bool,
        show_pyxim1: bool,
        show_pyxip1: bool,
        show_pyxi: bool,
        show_hists: bool,
        px1: float,
        num_points: int,
        filename="output_approx.png"
) -> str:
    max_xi = 4
    matplotlib.use('Agg')
    # define formats
    landscape = (930, 350)
    portrait = (640, 480)

    # select format
    output_format = portrait

    # Create an invisible figure.
    fig, ax = plt.subplots(figsize=(output_format[0] / 100, output_format[1] / 100))
    plt.ioff()

    # define style
    plt.rc('lines', linewidth=2)
    plt.rc('axes', titlesize=8, titleweight='bold', labelsize=8)
    plt.rc('font', family='Helvetica')

    p = varvalue
    if paramtype == "std":
        sigma = abs(p)
    elif paramtype == "var":
        sigma = abs(np.sqrt(p))
    elif paramtype == "snr_r":
        sigma = np.sqrt(10 ** (-p / 10))
    elif paramtype == "snr_c":
        sigma = np.sqrt(10 ** (-p / 10) / 2)

    if sigma < np.finfo(float).eps:
        sigma = np.finfo(float).eps

    px1 = np.clip(px1, 0, 1)

    num_points = max(1, round(num_points))

    x = np.linspace(-1, 1, 2001) * abs(max_xi)
    pn = pdf(x, sigma)
    pym1 = pdf(x + 1, sigma)
    pyp1 = pdf(x - 1, sigma)
    py = (1 - px1) * pym1 + px1 * pyp1

    Xrv = 2 * (np.random.rand(num_points) < px1) - 1
    Nrv = sigma * np.random.randn(num_points)
    Yrv = Xrv + Nrv
    Y_xp1 = Yrv[Xrv > 0]
    Y_xm1 = Yrv[Xrv < 0]

    delta_x = 0.166667
    x_bins = np.arange(-max_xi, max_xi + delta_x, delta_x)

    ber = np.mean(Xrv * Yrv < 0)
    ber_ex = Q(1 / sigma)

    if show_pnxi and show_hists:
        counts, centers = np.histogram(Nrv, bins=x_bins)
        freqs = counts / sum(counts) / delta_x
        ax.bar(centers[:-1], freqs, width=delta_x, color=[0.3, 0.3, 0.3], label='_nolegend_')

    if show_pyxim1 and show_hists:
        counts, centers = np.histogram(Y_xm1, bins=x_bins - delta_x / 3)
        freqs = counts / sum(counts) / delta_x
        ax.bar(centers[:-1], freqs, width=delta_x * 0.8, color=[0.75, 0, 0], label='_nolegend_')

    if show_pyxip1 and show_hists:
        counts, centers = np.histogram(Y_xp1, bins=x_bins + delta_x / 3)
        freqs = counts / sum(counts) / delta_x
        ax.bar(centers[:-1], freqs, width=delta_x * 0.8, color=[0, 0.45, 0], label='_nolegend_')

    if show_pyxi and show_hists:
        counts, centers = np.histogram(Yrv, bins=x_bins)
        freqs = counts / sum(counts) / delta_x
        ax.bar(centers[:-1], freqs, width=delta_x * 0.8, color=[0, 0, 0.75], label='_nolegend_')

    legend_entries = []

    if show_pnxi:
        ax.plot(x, pn, color=[0.5, 0.5, 0.5], linewidth=5, label='p_n(ξ)')

    if show_pyxim1:
        ax.plot(x, pym1, color=[1, 0, 0], linewidth=5, label='p_y(ξ|X=-1)')

    if show_pyxip1:
        ax.plot(x, pyp1, color=[0, 0.7, 0], linewidth=5, label='p_y(ξ|X=+1)')

    if show_pyxi:
        ax.plot(x, py, color=[0, 0, 1], linewidth=5, label='p_y(ξ)')

    ax.set_xlim([-max_xi, max_xi])

    snr_r = 10 * np.log10(1 / (sigma ** 2))
    snr_c = 10 * np.log10(1 / (2 * sigma ** 2))

    if paramtype == "std":
        title1 = f'σ = {sigma:.2f}'
    elif paramtype == "var":
        title1 = f'σ² = {sigma ** 2:.2f}'
    elif paramtype == "snr_r":
        title1 = f'SNR (real-val.) = {snr_r:.2f} dB'
    elif paramtype == "snr_c":
        title1 = f'SNR (complex-val.) = {snr_c:.2f} dB'

    ax.set_title(f'{title1}, BER = {ber} (simulated), BER = {ber_ex} (exact)')
    ax.set_xlabel('ξ')
    ax.legend()
    ax.grid(True)

    # Create an image file. This png image is displayed on the webpage. Its size must be 640x480.
    image_name = 'output_approx1.png'
    image_path = os.path.join(settings.MEDIA_ROOT, image_name)
    # output_path = f'media/{filename}'
    plt.savefig(image_path)
    plt.close(fig)
    return os.path.join(settings.MEDIA_URL, image_name)


def pdf(x: np.ndarray, sigma: float) -> np.ndarray:
    return 1 / (np.sqrt(2 * np.pi) * sigma) * np.exp(-1 / (2 * sigma ** 2) * x ** 2)


def Q(x: float) -> float:
    return 0.5 * (1 - erf(x / np.sqrt(2)))
