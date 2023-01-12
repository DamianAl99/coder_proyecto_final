from django import forms

class SchedulesForm(forms.Form):
    cliente = forms.CharField(max_length=50)
    services = forms.CharField(max_length=50)