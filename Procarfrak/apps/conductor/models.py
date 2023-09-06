from django.db import models

#-------------------------------------------------------------
#Datos Conductor
class EstadoC(models.Model):
    descripcion = models.TextField(max_length=100)
    
    def __str__(self):
        return '{}'.format(self.descripcion)

class Conductor(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birthdate = models.DateField()
    estadoC = models.BooleanField(default=False)
    def __str__(self):
        return ' {} '.format(self.name)

