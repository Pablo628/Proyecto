from django.db import models


class Estado_Vehiculo(models.Model):
    descripcion=models.TextField(max_length=100)
    def __str__(self):
        return '{}'.format(self.descripcion)


# Create your models here.
class Vehiculo(models.Model):
    placa=models.CharField(max_length=20)
    marca=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50)
    estado_vehiculo=models.ForeignKey(Estado_Vehiculo, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.placa)
