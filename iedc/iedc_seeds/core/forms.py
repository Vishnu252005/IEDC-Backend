from django import forms
from .models import Registrant  # Replace with your actual model

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registrant  # Replace with your model name
        fields = ['name', 'email', 'phone', 'college', 'event']  # Replace with your actual fields

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'college': forms.TextInput(attrs={'class': 'form-control'}),
            'event': forms.TextInput(attrs={'class': 'form-control'}),
        }
