from django import forms

class SurveyForm(forms.Form):
    total_value = forms.IntegerField(widget=forms.HiddenInput())
