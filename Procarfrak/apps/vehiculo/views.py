from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.vehiculo.models import *
from apps.vehiculo.form import *
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
    
    def form_valid(self, form):
        # Obtén el valor seleccionado del estado desde el formulario
        estado = form.cleaned_data['estadoV']
        # Asigna el valor del estado al objeto Liquidacion antes de guardarlo
        form.instance.estadoV = estado
        return super().form_valid(form)


#Editar registro
class VehiculoEdit(UpdateView):
    model=Vehiculo
    form_class= VehiculoForm
    template_name='vehiculo/vehiculo_form.html'
    success_url= reverse_lazy('vehiculo_listar')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = self.get_object()  # Esto asegura que el objeto se pasa a la plantilla
        return context
    def form_valid(self, form):
        # Obtén el valor seleccionado del estado desde el formulario
        estado = form.cleaned_data['estadoV']
        # Asigna el valor del estado al objeto Liquidacion antes de guardarlo
        form.instance.estadoV = estado
        return super().form_valid(form)



# Eliminar registro
class VehiculoDelete(DeleteView):
    model=Vehiculo
    template_name='vehiculo/vehiculo_delete.html'
    success_url= reverse_lazy('vehiculo_listar')

# # Create your views here.
def index(request):
    return HttpResponse("Esta es la vista de vehiculo")

