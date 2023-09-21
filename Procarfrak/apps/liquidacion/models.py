from django.db import models
from apps.conductor.models import Conductor
from django.db.models import Sum

# Create your models here.
class Liquidacion(models.Model):
    description = models.TextField(max_length=20)
    date = models.DateField()
    amount = models.FloatField()
    estadoL = models.CharField(max_length=10, choices=(("al día", "Al día"), ("pendiente", "Pendiente")), null=True, blank=True)
    conductor = models.ForeignKey(Conductor, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return ' {} '.format(self.description)

    @classmethod
    def total_por_auto(cls, conductor_id):
        return cls.objects.filter(conductor_id=conductor_id).aggregate(Sum('amount'))['amount__sum'] or 0.0

    @classmethod
    def total_general(cls):
        return cls.objects.aggregate(Sum('amount'))['amount__sum'] or 0.0
