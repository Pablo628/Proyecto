from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.liquidacion.form import *
from apps.liquidacion.models import  Liquidacion

# Create your views here.
def index(request):
    return HttpResponse("Esta es la vista de Liquidacion Conductores")
    # return render(request, "Liquidacion/index.html")

class LiquidacionList(ListView):
    model=Liquidacion
    template_name='liquidacion/liquidacion_list.html'
    paginate_by=2

class LiquidacionCreate(CreateView):
    model = Liquidacion
    form_class = LiquidacionForm
    template_name = 'liquidacion/liquidacion_form.html'
    success_url = reverse_lazy('Liquidacion_listar')

    def form_valid(self, form):
        # Obtén el valor seleccionado del estado desde el formulario
        estado = form.cleaned_data['estadoL']
        # Asigna el valor del estado al objeto Liquidacion antes de guardarlo
        form.instance.estadoL = estado
        return super().form_valid(form)

class LiquidacionUpdate(UpdateView):
    model = Liquidacion
    form_class = LiquidacionForm
    template_name = 'liquidacion/liquidacion_form.html'
    success_url = reverse_lazy('Liquidacion_listar')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = self.get_object()  # Esto asegura que el objeto se pasa a la plantilla
        return context
    def form_valid(self, form):
        # Obtén el valor seleccionado del estado desde el formulario
        estado = form.cleaned_data['estadoL']
        # Asigna el valor del estado al objeto Liquidacion antes de guardarlo
        form.instance.estadoL = estado
        return super().form_valid(form)



class LiquidacionDelete(DeleteView):
    model = Liquidacion
    template_name = 'liquidacion/liquidacion_delete.html'  # Utiliza la nueva plantilla
    success_url = reverse_lazy('Liquidacion_listar')


