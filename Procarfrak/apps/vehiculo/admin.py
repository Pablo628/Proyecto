from django.contrib import admin
from apps.vehiculo.models import Vehiculo, EstadoV
# from apps.mascota.apps import Vacuna

# Register your models here.
admin.site.register(EstadoV)
admin.site.register(Vehiculo)

