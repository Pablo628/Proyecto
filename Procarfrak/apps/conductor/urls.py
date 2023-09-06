from django.urls import re_path
from apps.conductor.views import index, conductor_view, conductor_list, conductor_edit, conductor_delete

# app_name="Liquidacion_Conductor"

# def conductor_user():
#     return conductor_user

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^nuevo$', conductor_view, name='conductor_crear'),
    re_path(r'^listar', conductor_list, name='conductor_listar'),
    re_path(r'^editar/(?P<id_conductor>\d+)/$', conductor_edit, name='conductor_edit'),
    re_path(r'^eliminar/(?P<id_conductor>\d+)/$', conductor_delete, name='conductor_eliminar'),


]