from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'^$', index, name='index'),
    # re_path(r'^listar$', Liquidacion_list, name='Liquidacion_listar'),
    re_path(r'^listar$', LiquidacionList.as_view(), name='Liquidacion_listar'),
    # re_path(r'^nuevo$', Liquidacion_view, name='Liquidacion_crear'),
    re_path(r'^nuevo$', LiquidacionCreate.as_view(), name='Liquidacion_crear'),
    # re_path(r'^editar/(?P<id_liquidacion>\d+)/$', Liquidacion_edit, name='Liquidacion_editar'),
    re_path(r'^editar/(?P<pk>\d+)/$', LiquidacionUpdate.as_view(), name='Liquidacion_editar'),
    # re_path(r'^eliminar/(?P<id_liquidacion>\d+)/$', Liquidacion_delete, name='Liquidacion_eliminar'),
    re_path(r'^eliminar/(?P<pk>\d+)/$', LiquidacionDelete.as_view(), name='Liquidacion_eliminar'),

    # urls de estado
    re_path(r'^nuevo_estado$', Estado_view, name='Estado_crear'),
    re_path(r'^editar_estado/(?P<id_estado>\d+)/$', Estado_edit, name='Estado_editar'),
    re_path(r'^eliminar_estado/(?P<id_estado>\d+)/$', Estado_delete, name='Estado_eliminar'),
]
