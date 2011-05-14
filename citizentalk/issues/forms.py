
from django import forms
from issues.models import Issue

class CreateForm(forms.Form):
    title = forms.CharField(required=True)
    description = forms.CharField(widget=forms.Textarea)
    tags = forms.CharField()
    latitude = forms.DecimalField(widget=forms.HiddenInput)
    longitude = forms.DecimalField(widget=forms.HiddenInput)

    def clean(self):
        cleaned_data = self.cleaned_data
        tags = cleaned_data.get("tags")

        if u':' in tags:
            raise forms.ValidationError("Colons are not allowed in the "
                                    "tags field")
