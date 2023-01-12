from django import forms

class ServicesForm(forms.Form):
    name = forms.CharField(max_length=50)
    duration = forms.CharField(max_length=15)
    description= forms.CharField(max_length=150)