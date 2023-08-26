from django.db import models

# Create your models here.
class EstadoL(models.Model):
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return ' {} '.format(self.descripcion)
    

class Liquidacion(models.Model):
    description = models.TextField(max_length=100)
    date = models.DateField()
    amount = models.FloatField()
    estadoL = models.ForeignKey(EstadoL, null=True, blank=True, on_delete=models.CASCADE)
    # conductor = models.ForeignKey(Conductor, null=True, blank=True, on_delete=models.CASCADE)
    # administrador = models.ForeignKey(Administrador, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return ' {} '.format(self.description)