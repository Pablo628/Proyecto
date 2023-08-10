from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from usuario.forms import RegistroForm


# Create your views here.
class RegistroUsuario(CreateView):
    model = User
    template_name = 'Usuario/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('conductor_listar')

