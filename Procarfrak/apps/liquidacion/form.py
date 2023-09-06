from django import forms
from apps.liquidacion.models import *

class LiquidacionForm(forms.ModelForm):
    class Meta:
        model = Liquidacion
        fields = [
            'description',
            'date',
            'amount',
            'estadoL',
        ]
        labels = {
            'description': 'Descripción',
            'date': 'Fecha',
            'amount': 'Cantidad',
            'estadoL': 'Estado Liquidación',
        }
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'estadoL': forms.Select(attrs={'class': 'form-control'}),
        }

class EstadoForm(forms.ModelForm):
    class Meta:
        model=EstadoL
        fields = [
            'descripcion',
        ]
        labels={
            'descripcion':'Descripcion',
        }
        widgets={
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
        }