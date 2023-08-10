from django.urls import include, re_path
from usuario.views import RegistroUsuario

urlpatterns = [
    re_path(r'^nuevo', RegistroUsuario.as_view(), name='Registrar'),
]