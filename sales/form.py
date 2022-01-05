from django import forms

CHART_CHOICES = (
    ('#1', 'Bar char'),
    ('#2', 'Pie char'),
    ('#3', 'Line char'),
)

class SaleSearchForm(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    char_type = forms.ChoiceField(choices=CHART_CHOICES)