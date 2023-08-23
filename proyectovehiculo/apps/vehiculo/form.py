from django import forms
from apps.vehiculo.models import Vehiculo

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