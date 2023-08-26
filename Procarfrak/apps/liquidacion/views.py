from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.liquidacion.form import *
from apps.liquidacion.models import EstadoL, Liquidacion

# Create your views here.

# views de Liquidacion
def index(request):
    return HttpResponse("Esta es la vista de Liquidacion Conductores")
    # return render(request, "Liquidacion/index.html")

class LiquidacionList(ListView):
    model=Liquidacion
    template_name='liquidacion/liquidacion_list.html'
    paginate_by=2

class LiquidacionCreate(CreateView):
    model=Liquidacion
    form_class=LiquidacionForm
    template_name='liquidacion/liquidacion_form.html'
    success_url=reverse_lazy('Liquidacion_listar')

class LiquidacionUpdate(UpdateView):
    model=Liquidacion
    form_class=LiquidacionForm
    template_name='liquidacion/liquidacion_form.html'
    success_url=reverse_lazy('Liquidacion_listar')

class LiquidacionDelete(DeleteView):
    model=Liquidacion
    template_name='liquidacion/liquidacion_delete.html'
    success_url=reverse_lazy('Liquidacion_listar')


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