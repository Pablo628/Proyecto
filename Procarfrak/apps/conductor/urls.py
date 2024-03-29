from django.urls import re_path, path
from apps.conductor.views import *
from apps.conductor.reportes import *


urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^listar', ConductorList.as_view(), name='Conductor_listar'),
    re_path(r'^nuevo$', ConductorCreate.as_view(), name='Conductor_crear'),
    re_path(r'^editar/(?P<pk>\d+)/$', ConductorUpdate.as_view(), name='Conductor_editar'),
    re_path(r'^eliminar/(?P<pk>\d+)/$', ConductorDelete.as_view(), name='Conductor_eliminar'),
    path(r'conductor/listado', reporte_conductores, name='reporte_conductores'),  # Agrega la URL del informe de conductores

]