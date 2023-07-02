from django.urls import re_path
from .views import *


urlpatterns = [
    re_path(r'^nuevo$', RegistroUsuario.as_view(), name='Registro'),
]