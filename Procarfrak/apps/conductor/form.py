from django import forms
from apps.conductor.models import *
class ConductorForm(forms.ModelForm):
    class Meta:
        model= Conductor
        fields = [
            'name',
            'lastname',
            'birthdate',
            'estadoC',
        ]
        labels = {
            'name': 'Nombre',
            'lastname': 'Apellido',
            'birthdate': 'Fecha de nacimiento',
            'estadoC': 'Estado Conductor',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'lastname': forms.TextInput(attrs={'class':'form-control'}),
            'birthdate': forms.SelectDateWidget(attrs={'class':'form-control'}),
            'estadoC': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }