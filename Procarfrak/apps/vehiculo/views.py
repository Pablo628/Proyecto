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


# Eliminar registro
class VehiculoDelete(DeleteView):
    model=Vehiculo
    template_name='vehiculo/vehiculo_delete.html'
    success_url= reverse_lazy('vehiculo_listar')

# # Create your views here.
def index(request):
    return HttpResponse("Esta es la vista de vehiculo")

# Views de estado
def Estado_view(request):
    if request.method=='POST':
        form=EstadoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Estado_crear')
    else:
        form=EstadoForm()
    return render(request, "EstadoV/estadov_form.html", {'form':form})


def Estado_edit(request,id_estadov):
    estadov=EstadoV.objects.get(id=id_estadov)
    if request.method=='GET':
            form=EstadoForm(instance=estadov)
    else:
        form=VehiculoForm(request.POST, instance=estadov)
        if form.is_valid():
            form.save()
        return redirect ('Estado_listar')
    return render(request, 'EstadoV/estadov_form.html', {'form':form})

def Estado_delete(request,id_estadov):
    estadov=EstadoV.objects.get(id=id_estadov)
    if request.method=='POST':
        estadov.delete()
        return redirect ('Estado_listar')
    return render(request, 'EstadoV/estadov_delete.html', {'estado':estadov})