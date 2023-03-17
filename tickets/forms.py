from django import forms
from .models import Pnr

class PnrForm(forms.ModelForm):
    class Meta:
        model = Pnr
        fields = ['code']