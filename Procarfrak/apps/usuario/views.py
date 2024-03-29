from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.usuario.forms import *
from django.contrib.auth import login, logout, authenticate


# Create your views here.

class RegistroUsuario(CreateView):
    model=User
    template_name='usuario/registrar.html'
    form_class=RegistroForm
    success_url=reverse_lazy('Liquidacion_listar')