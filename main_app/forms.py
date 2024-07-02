from django import forms

# справа как передаются во вью слева как выглядят на фронте
PARAM_TYPE_CHOICES = (
    ("std", "std"),
    ("var", "var"),
    ("snr_r", "snr_r"),
    ("snr_c", "snr_c"),
)


class ApproxDemoForm(forms.Form):
    param_type = forms.ChoiceField(choices=PARAM_TYPE_CHOICES)
    var_value = forms.DecimalField(max_digits=10, decimal_places=2)
    show_pnxi = forms.BooleanField(required=False)
    show_pyxim1 = forms.BooleanField(required=False)
    show_pyxip1 = forms.BooleanField(required=False)
    show_pyxi = forms.BooleanField(required=False)
    show_hists = forms.BooleanField(required=False)
    show_px1 = forms.DecimalField(max_digits=10, decimal_places=2)
    num_points = forms.IntegerField()


class AnotherDemoForm(forms.Form):
    another_param = forms.CharField(max_length=100)
    another_value = forms.IntegerField()