from django.db import models
from apps.conductor.models import Conductor

# Create your models here.
class Liquidacion(models.Model):
    description = models.TextField(max_length=20)
    date = models.DateField()
    amount = models.FloatField()
    estadoL = models.CharField(max_length=10, choices=(("al día", "Al día"), ("pendiente", "Pendiente")), null=True, blank=True)
    conductor = models.ForeignKey(Conductor, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return ' {} '.format(self.description)