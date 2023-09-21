from django.db import models




# Create your models here.
class Vehiculo(models.Model):
    placa=models.CharField(max_length=20)
    marca=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50)
    estadoV = models.CharField(max_length=10, choices=(("activo", "Activo"), ("inactivo", "Inactivo")), null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.placa)
