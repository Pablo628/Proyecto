from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .form import *
from .models import *

# Create your views here.
# views de Liquidacion
def index(request):
#     #return HttpResponse("Esta es la vista de Liquidacion Conductores")
    return render(request, "Liquidacion/index.html")
class LiquidacionList(ListView):
    model=Liquidacion
    template_name='Liquidacion/liquidacion_list.html'
class LiquidacionCreate(CreateView):
    model=Liquidacion
    form_class=LiquidacionForm
    template_name='Liquidacion/liquidacion_form.html'
    success_url=reverse_lazy('Liquidacion_listar')
class LiquidacionUpdate(UpdateView):
    model=Liquidacion
    form_class=LiquidacionForm
    template_name='Liquidacion/liquidacion_form.html'
    success_url=reverse_lazy('Liquidacion_listar')
class LiquidacionDelete(DeleteView):
    model=Liquidacion
    template_name='Liquidacion/liquidacion_delete.html'
    success_url=reverse_lazy('Liquidacion_listar')
# def Liquidacion_view(request):
#     if request.method=='POST':
#         form=LiquidacionForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('Liquidacion_listar')
#     else:
#         form=LiquidacionForm()
#     return render(request, "Liquidacion/liquidacion_form.html", {'form':form})

# def Liquidacion_list(request):
#     liquidacion=Liquidacion.objects.all().order_by('id')
#     contexto={'liquidaciones':liquidacion}
#     return render(request, 'Liquidacion/liquidacion_list.html', contexto)

# def Liquidacion_edit(request,id_liquidacion):
#     liquidacion=Liquidacion.objects.get(id=id_liquidacion)
#     if request.method=='GET':
#             form=LiquidacionForm(instance=liquidacion)
#     else:
#         form=LiquidacionForm(request.POST, instance=liquidacion)
#         if form.is_valid():
#             form.save()
#         return redirect ('Liquidacion_listar')
#     return render(request, 'Liquidacion/liquidacion_form.html', {'form':form})

# def Liquidacion_delete(request,id_liquidacion):
#     liquidacion=Liquidacion.objects.get(id=id_liquidacion)
#     if request.method=='POST':
#         liquidacion.delete()
#         return redirect ('Liquidacion_listar')
#     return render(request, 'Liquidacion/liquidacion_delete.html', {'liquidacion':liquidacion})

# Views de estado
def Estado_view(request):
    if request.method=='POST':
        form=EstadoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Estado_crear')
    else:
        form=EstadoForm()
    return render(request, "EstadoL/estadol_form.html", {'form':form})


def Estado_edit(request,id_estadol):
    estadol=EstadoL.objects.get(id=id_estadol)
    if request.method=='GET':
            form=EstadoForm(instance=estadol)
    else:
        form=LiquidacionForm(request.POST, instance=estadol)
        if form.is_valid():
            form.save()
        return redirect ('Estado_listar')
    return render(request, 'EstadoL/estadol_form.html', {'form':form})

def Estado_delete(request,id_estadol):
    estadol=EstadoL.objects.get(id=id_estadol)
    if request.method=='POST':
        estadol.delete()
        return redirect ('Estado_listar')
    return render(request, 'EstadoL/estadol_delete.html', {'estado':estadol})
