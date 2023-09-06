from django import forms
from apps.vehiculo.models import *

class VehiculoForm(forms.ModelForm):
    class Meta:
        model=Vehiculo

        fields = [
            'placa',
            'marca',
            'modelo',
            'estado_vehiculo',
        ]
        labels={
            'placa':'Placa del vehículo',
            'marca':'Marca del vehículo',
            'modelo': 'Modelo del vehículo',
            'estado_vehiculo': 'Estado del vehículo',
        }
        widgets={
            'placa': forms.TextInput(attrs={'class':'form-control'}),
            'marca': forms.TextInput(attrs={'class':'form-control'}),
            'modelo': forms.TextInput(attrs={'class':'form-control'}),
            'estado_vehiculo': forms.Select(attrs={'class':'form-control'}),
        }

class EstadoForm(forms.ModelForm):
    class Meta:
        model=EstadoV
        fields = [
            'descripcion',
        ]
        labels={
            'descripcion':'Descripcion',
        }
        widgets={
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
        }