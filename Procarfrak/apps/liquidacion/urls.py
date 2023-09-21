from django.urls import re_path
from apps.liquidacion.views import *
from django.urls import path
from apps.liquidacion.reportes import *

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^listar', LiquidacionList.as_view(), name='Liquidacion_listar'),
    re_path(r'^nuevo$', LiquidacionCreate.as_view(), name='Liquidacion_crear'),
    re_path(r'^editar/(?P<pk>\d+)/$', LiquidacionUpdate.as_view(), name='Liquidacion_editar'),
    re_path(r'^eliminar/(?P<pk>\d+)/$', LiquidacionDelete.as_view(), name='Liquidacion_eliminar'),
    path('cambiar_estado_liquidacion/<int:liquidacion_id>/', cambiar_estado_liquidacion, name='cambiar_estado_liquidacion'),
    path(r'liquidacion/listado', reporte_liquidaciones, name='reporte_liquidaciones'),
]
