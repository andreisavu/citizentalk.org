
from django import forms
from issues.models import Issue

class CreateForm(forms.Form):
    title = forms.CharField(required=True)
    description = forms.CharField(widget=forms.Textarea)
    latitude = forms.DecimalField(widget=forms.HiddenInput)
    longitude = forms.DecimalField(widget=forms.HiddenInput)

