from django import forms

class EmployeesForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.FloatField()
    ci = forms.IntegerField(required=False)