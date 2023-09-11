from django import forms
from apps.vehiculo.models import *

class VehiculoForm(forms.ModelForm):
    # Define las opciones de estado como una lista de tuplas
    ESTADO_CHOICES = (
        ("activo", "Activo"),
        ("inactivo", "Inactivo"),
    )

    # Cambia el campo 'estadoL' a un ChoiceField con las opciones definidas arriba
    estadoV = forms.ChoiceField(choices=ESTADO_CHOICES, label="Estado Vehiculo")

    class Meta:
        model=Vehiculo

        fields = [
            'placa',
            'marca',
            'modelo',
        ]
        labels={
            'placa':'Placa del vehículo',
            'marca':'Marca del vehículo',
            'modelo': 'Modelo del vehículo',
        }
        widgets={
            'placa': forms.TextInput(attrs={'class':'form-control'}),
            'marca': forms.TextInput(attrs={'class':'form-control'}),
            'modelo': forms.TextInput(attrs={'class':'form-control'}),
        }

