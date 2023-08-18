from django.shortcuts import render
from django.http import HttpResponse
from apps.vehiculo.models import Vehiculo
from apps.vehiculo.form import VehiculoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
#Pagina inicial
# def index(request):
#     return render(request, "vehiculo/index.html")

class VehiculoList(ListView):
    model=Vehiculo
    template_name='vehiculo/vehiculo_list.html'


#crear registro
class VehiculoCreate(CreateView):
    model=Vehiculo
    form_class= VehiculoForm
    template_name='vehiculo/vehiculo_form.html'
    success_url= reverse_lazy('vehiculo_listar')

#Editar registro
class VehiculoEdit(UpdateView):
    model=Vehiculo
    form_class= VehiculoForm
    template_name='vehiculo/vehiculo_form.html'
    success_url= reverse_lazy('vehiculo_listar')

# Eliminar registro
class VehiculoDelete(DeleteView):
    model=Vehiculo
    template_name='vehiculo/vehiculo_delete.html'
    success_url= reverse_lazy('vehiculo_listar')

# # Create your views here.
def index(request):
    return HttpResponse("Esta es la vista de vehiculo")