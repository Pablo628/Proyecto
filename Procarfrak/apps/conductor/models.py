from django.db import models
from apps.vehiculo.models import Vehiculo

# Create your models here.
class Conductor(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birthdate = models.DateField()
    estadoC = models.CharField(max_length=10, choices=(("activo", "Activo"), ("inactivo", "Inactivo")), null=True, blank=True)
    vehiculo = models.ForeignKey(Vehiculo, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return ' {} '.format(self.name)

