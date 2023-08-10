from django import forms
from LiquidacionConductor.models import Conductor,EstadoC
class ConductorForm(forms.ModelForm):
    class Meta:
        model= Conductor
        fields = [
            'name',
            'lastname',
            'birthdate',
            'estadoC',
            'vehiculo',
        ]
        labels = {
            'name': 'Nombre',
            'lastname': 'Apellido',
            'birthdate': 'Fecha de nacimiento',
            'estadoC': 'Estado conductor',
            'vehiculo': 'Vehiculo',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'lastname': forms.TextInput(attrs={'class':'form-control'}),
            'birthdate': forms.TextInput(attrs={'class':'form-control'}),
            'estadoC': forms.Select(attrs={'class':'form-control'}),
            'vehiculo': forms.Select(attrs={'class':'form-control'}),
        }