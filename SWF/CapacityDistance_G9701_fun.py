import os

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import math

from django.conf import settings


def get_cable_parameterG9071(F: np.ndarray, idx: int) -> tuple[np.ndarray, np.ndarray, str]:
    """
    Placeholder function for get_cable_parameterG9071.
    Replace with actual implementation.

    Args:
        F (np.ndarray): Array of frequencies.
        idx (int): Index of the cable.

    Returns:
        tuple[np.ndarray, np.ndarray, str]: Tuple containing the impedance (Zs), admittance (Yp), and name of the cable.
    """
    Zs = np.ones_like(F) * 0.05  # Example values
    Yp = np.ones_like(F) * 0.02  # Example values
    Name = "Example Cable"
    return Zs, Yp, Name


def CapacityDistance_fun(
        idx: int,
        delta_f: float,
        checkADSL1: bool,
        checkADSL2: bool,
        checkVDSL1: bool,
        checkVDSL2: bool,
        distance_start: float,
        distance_stop: float,
        TX_Power_all_db=24,
        filename="output_CapacityDistance_fun.png",
) -> str:
    """
    Calculates and plots the capacity of a cable as a function of distance.

    Args:
        idx (int): Index of the cable.
        delta_f (float): Frequency step size.
        checkADSL1 (int): Flag for ADSL 1.1 MHz.
        checkADSL2 (int): Flag for ADSL+ 2.2 MHz.
        checkVDSL1 (int): Flag for VDSL2 17.6 MHz.
        checkVDSL2 (int): Flag for VDSL2 30 MHz.
        distance_start (float): Starting distance in kilometers.
        distance_stop (float): Ending distance in kilometers.
        TX_Power_all_db (float): Total transmit power in dBm.
        filename (str): Name of the output file.
    """
    matplotlib.use('Agg')
    # define formats
    landscape = (930, 350)
    portrait = (640, 480)

    # select format
    output_format = portrait

    # Create an invisible figure.
    plt.figure(figsize=(output_format[0 ] /100, output_format[1 ] /100), dpi=100)

    # define style
    plt.rc('lines', linewidth=2)
    plt.rcParams['lines.linewidth'] = 2
    plt.rcParams['lines.linestyle'] = '-'

    Bandwidths = []
    Legend = []
    if checkADSL1:
        Bandwidths.append(1.1e6)
        Legend.append('ADSL 1.1 MHz')
    if checkADSL2:
        Bandwidths.append(2.2e6)
        Legend.append('ADSL+ 2.2 MHz')
    if checkVDSL1:
        Bandwidths.append(17.6e6)
        Legend.append('VDSL2 17.6 MHz')
    if checkVDSL2:
        Bandwidths.append(30e6)
        Legend.append('VDSL2 30MHz')

    Distances = np.linspace(distance_start, distance_stop, 100)

    # Parameter
    Annex_Freq_Offset = 138e3
    KilometerPerMiles = 1.609344
    ThermalNoisePerCarrier = -174 + 10 * np.log10(delta_f)  # in dB
    MaxSNR_dB = 45.15  # in dB
    c0 = 299792458  # exact

    K = len(Distances)
    M = len(Bandwidths)
    for m in range(M):
        Bandwidth = Bandwidths[m]
        TX_Power = 10 * np.log10(((10 ** (TX_Power_all_db / 10)) / Bandwidth) * delta_f)

        Capacity_array = np.zeros(K)
        for k in range(K):
            distance = Distances[k]

            # Calculate frequencies
            freq = np.arange(Annex_Freq_Offset, Annex_Freq_Offset + Bandwidth, delta_f)

            # get cable parameters
            F = freq
            Zs, Yp, Name = get_cable_parameterG9071(F, idx)
            Zs = Zs * 1000
            Yp = Yp * 1000

            # Telegraphen equation
            Gamma = np.sqrt(Zs * Yp)
            alpha = np.real(Gamma)

            Amplitude = 1 / 2 * np.exp(-1 * distance * alpha)
            H_dB = 20 * np.log10(Amplitude)
            SNR_dB = TX_Power + H_dB - ThermalNoisePerCarrier
            SNR_dB[SNR_dB > MaxSNR_dB] = MaxSNR_dB
            SNR_lin = 10 ** (SNR_dB / 10)
            Capacity = np.log2(1 + SNR_lin)
            Capacity_Mbitps = np.sum(Capacity * delta_f) / 1e6
            Capacity_array[k] = Capacity_Mbitps

        # plot
        plt.plot(Distances, Capacity_array, label=Legend[m])

    plt.xlabel('Distance [km]')
    plt.ylabel('Capacity [Mbit/s]')
    plt.legend()
    plt.legend(frameon=False)
    plt.grid(True)

    # Create an image file. This png image is displayed on the webpage. Its size
    # must be 640x480.
    image_path = os.path.join(settings.MEDIA_ROOT, filename)
    plt.savefig(image_path, format='png', bbox_inches='tight', dpi=100)
    plt.close()
    return os.path.join(settings.MEDIA_URL, filename)

#
# if __name__ == '__main__':
#     # Test data
#     idx = 5
#     delta_f = 43125
#     checkADSL1 = 1
#     checkADSL2 = 1
#     checkVDSL1 = 1
#     checkVDSL2 = 1
#     distance_start = 1.25
#     distance_stop = 5
#     TX_Power_all_db = 24
#     filename = "test.png"
#
#     CapacityDistance_fun(
#         idx,
#         delta_f,
#         checkADSL1,
#         checkADSL2,
#         checkVDSL1,
#         checkVDSL2,
#         distance_start,
#         distance_stop,
#         TX_Power_all_db,
#         filename,
#     )