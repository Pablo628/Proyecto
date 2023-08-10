from django.urls import path, re_path, include
from .views import index, conductor_view, conductor_list, conductor_edit, conductor_delete

app_name="Liquidacion_Conductor"

def conductor_user():
    return conductor_user

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^conductor/nuevo$', conductor_view, name='conductor_crear'),
    re_path(r'^conductor/listar$', conductor_list, name='conductor_listar'),
    re_path(r'^conductor/editar/(?P<id_conductor>\d+)/$', conductor_edit, name='conductor_edit'),
    re_path(r'^conductor/eliminar/(?P<id_conductor>\d+)/$', conductor_delete, name='conductor_eliminar'),


]