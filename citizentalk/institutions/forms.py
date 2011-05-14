from django.forms import ModelForm
from models import Institution

class InstitutionForm(ModelForm):
    class Meta:
        model = Institution
