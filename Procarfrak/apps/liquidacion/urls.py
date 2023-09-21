from django.urls import re_path
from apps.liquidacion.views import *

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^listar', LiquidacionList.as_view(), name='Liquidacion_listar'),
    re_path(r'^nuevo$', LiquidacionCreate.as_view(), name='Liquidacion_crear'),
    re_path(r'^editar/(?P<pk>\d+)/$', LiquidacionUpdate.as_view(), name='Liquidacion_editar'),
    re_path(r'^eliminar/(?P<pk>\d+)/$', LiquidacionDelete.as_view(), name='Liquidacion_eliminar'),
]