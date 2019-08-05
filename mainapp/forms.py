from django import forms
from .models import ContractUs

class ContractUsForm(forms.ModelForm):
    class Meta:
        model = ContractUs
        fields = '__all__'