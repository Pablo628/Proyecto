from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(EstadoV)
admin.site.register(Vehiculo)
admin.site.register(EstadoC)
admin.site.register(Conductor)
admin.site.register(EstadoL)
admin.site.register(Liquidacion)