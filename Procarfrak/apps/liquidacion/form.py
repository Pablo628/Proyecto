from django import forms
from apps.liquidacion.models import Liquidacion


class LiquidacionForm(forms.ModelForm):
    ESTADO_CHOICES = (
        ("al día", "Al día"),
        ("pendiente", "Pendiente"),
    )

    estadoL = forms.ChoiceField(choices=ESTADO_CHOICES, label="Estado Liquidación")

    class Meta:
        model = Liquidacion
        fields = [
            'description',
            'date',
            'amount',
            'conductor',
        ]
        labels = {
            'description': 'Descripción',
            'date': 'Fecha',
            'amount': 'Cantidad',
            'conductor': 'Conductor',
        }
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type':'date'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'conductor': forms.Select(attrs={'class':'form-control'}),
        }

