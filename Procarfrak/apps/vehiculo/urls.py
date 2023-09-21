from  django.urls import re_path, path
from apps.vehiculo.views import *
from apps.vehiculo.reportes import *


urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^editar/(?P<pk>\d+)/$', VehiculoEdit.as_view(), name='vehiculo_editar'),
    re_path(r'^eliminar/(?P<pk>\d+)/$', VehiculoDelete.as_view(), name='vehiculo_eliminar'),
    re_path(r'^nuevo$', VehiculoCreate.as_view(), name='vehiculo_crear'),
    re_path(r'^listar$', VehiculoList.as_view(), name='vehiculo_listar'),
    path('vehiculo/listado', reporte_vehiculos, name='reporte_vehiculos'),
]
