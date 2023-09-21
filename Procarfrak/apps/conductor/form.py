from django import forms
from apps.conductor.models import *

class ConductorForm(forms.ModelForm):
    # Define las opciones de estado como una lista de tuplas
    ESTADO_CHOICES = (
        ("activo", "Activo"),
        ("inactivo", "Inactivo"),
    )

    # Cambia el campo 'estadoL' a un ChoiceField con las opciones definidas arriba
    estadoC = forms.ChoiceField(choices=ESTADO_CHOICES, label="Estado Conductor")


    class Meta:
        model= Conductor
        fields = [
            'name',
            'lastname',
            'birthdate',
            'vehiculo',
        ]
        labels = {
            'name': 'Nombre',
            'lastname': 'Apellido',
            'birthdate': 'Fecha de nacimiento',
            'vehiculo': 'Vehiculo',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'lastname': forms.TextInput(attrs={'class':'form-control'}),
            'birthdate': forms.DateInput(attrs={'type':'date'}),
            'vehiculo': forms.Select(attrs={'class':'form-control'}),
        }