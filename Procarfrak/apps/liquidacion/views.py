from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.liquidacion.form import *
from apps.liquidacion.models import  Liquidacion
from django.db.models import Sum
from django.utils import timezone


# Create your views here.
def index(request):
    return HttpResponse("Esta es la vista de Liquidacion Conductores")
    # return render(request, "Liquidacion/index.html")

class LiquidacionList(ListView):
    model = Liquidacion
    template_name = 'liquidacion/liquidacion_list.html'
    paginate_by = 2
    
    def get_queryset(self):
        # Obtén el queryset de liquidaciones
        queryset = super().get_queryset()

        # Calcula el total general de todas las liquidaciones
        total_general = queryset.aggregate(Sum('amount'))['amount__sum'] or 0.0

        # Crea un diccionario para almacenar los totales por conductor
        totales_por_conductor = {}

        # Recorre las liquidaciones y calcula el total por conductor
        for liquidacion in queryset:
            conductor_id = liquidacion.conductor.id
            if conductor_id not in totales_por_conductor:
                totales_por_conductor[conductor_id] = 0.0
            totales_por_conductor[conductor_id] += liquidacion.amount

        # Agrega los totales generales y por conductor al contexto
        self.total_general = total_general
        self.totales_por_conductor = totales_por_conductor

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_general'] = self.total_general
        context['totales_por_conductor'] = self.totales_por_conductor
        return context

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

from django.http import JsonResponse

def cambiar_estado_liquidacion(request, liquidacion_id):
    if request.method == 'POST':
        nuevo_estado = request.POST.get('estadoL')
        liquidacion = Liquidacion.objects.get(pk=liquidacion_id)
        liquidacion.estadoL = nuevo_estado
        liquidacion.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})