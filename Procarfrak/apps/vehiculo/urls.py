from  django.urls import re_path, include
from apps.vehiculo.views import *

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^editar/(?P<pk>\d+)/$', VehiculoEdit.as_view(), name='vehiculo_editar'),
    re_path(r'^eliminar/(?P<pk>\d+)/$', VehiculoDelete.as_view(), name='vehiculo_eliminar'),
    re_path(r'^nuevo$', VehiculoCreate.as_view(), name='vehiculo_crear'),
    re_path(r'^listar$', VehiculoList.as_view(), name='vehiculo_listar'),

    # urls de estado
    re_path(r'^nuevo_estado$', Estado_view, name='Estado_crear'),
    re_path(r'^editar_estado/(?P<id_estado>\d+)/$', Estado_edit, name='Estado_editar'),
    re_path(r'^eliminar_estado/(?P<id_estado>\d+)/$', Estado_delete, name='Estado_eliminar'),

]
