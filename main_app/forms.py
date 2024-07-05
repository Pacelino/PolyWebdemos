from django import forms

# слева как передаются во вью. справа как выглядят на фронте
PARAM_TYPE_CHOICES = (
    ("std", "std"),
    ("var", "var"),
    ("snr_r", "snr_r"),
    ("snr_c", "snr_c"),
)

CABLE_TYPE_CHOICES = (
    (0, "CAD55"),
    (1, "CAT5"),
    (2, "T05u"),
    (3, "T05b"),
    (4, "T05h")
)


class ApproxDemoForm(forms.Form):
    param_type = forms.ChoiceField(choices=PARAM_TYPE_CHOICES)
    var_value = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.TextInput)
    show_pnxi = forms.BooleanField(required=False)
    show_pyxim1 = forms.BooleanField(required=False)
    show_pyxip1 = forms.BooleanField(required=False)
    show_pyxi = forms.BooleanField(required=False)
    show_hists = forms.BooleanField(required=False)
    show_px1 = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.TextInput)
    num_points = forms.IntegerField(widget=forms.TextInput)


class CapacityDistance_G9701Form(forms.Form):
    idx = forms.ChoiceField(label="Cable", choices=CABLE_TYPE_CHOICES)
    delta_f = forms.ChoiceField(label="Step", choices=((43125, "4.3125 kHZ",), (86250, "8.625 kHZ")))
    checkADSL1 = forms.BooleanField(label="ADSL 1.1MHz", required=False)
    checkADSL2 = forms.BooleanField(label="ADSL+ 2.2 MHz", required=False)
    checkVDSL1 = forms.BooleanField(label="VDSL2 17.6 MHz", required=False)
    checkVDSL2 = forms.BooleanField(label="VDSL2 30 MHz", required=False)
    distance_start = forms.DecimalField(label="Start", max_digits=5, decimal_places=2, min_value=0, widget=forms.TextInput)
    distance_stop = forms.DecimalField(label="Stop", max_digits=5, decimal_places=2,  max_value=6.0, widget=forms.TextInput)


