from django import forms

class SurveyForm(forms.Form):
    total_value = forms.IntegerField(widget=forms.HiddenInput())

class VoiceFileForm(forms.Form):
    voiceFile = forms.FileField()