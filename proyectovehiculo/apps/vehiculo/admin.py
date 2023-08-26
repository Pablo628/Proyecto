from django.contrib import admin
from apps.vehiculo.models import Vehiculo, Estado_Vehiculo
# from apps.mascota.apps import Vacuna

# Register your models here.
admin.site.register(Vehiculo)
admin.site.register(Estado_Vehiculo)

