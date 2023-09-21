from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from apps.conductor.form import ConductorForm
from apps.conductor.models import Conductor

# Create your views here.
def index(request):
    return render(request, 'conductor/index.html')


class ConductorList(ListView):
    model=Conductor
    template_name='conductor/conductor_list.html'
    paginate_by=2

class ConductorCreate(CreateView):
    model=Conductor
    form_class = ConductorForm
    template_name='conductor/conductor_form.html'
    success_url=reverse_lazy('Conductor_listar')
    
    def form_valid(self, form):
        # Obtén el valor seleccionado del estado desde el formulario
        estado = form.cleaned_data['estadoC']
        # Asigna el valor del estado al objeto conductor antes de guardarlo
        form.instance.estadoC = estado
        return super().form_valid(form)



class ConductorUpdate(UpdateView):
    model=Conductor
    form_class=ConductorForm
    template_name='conductor/conductor_form.html'
    success_url=reverse_lazy('Conductor_listar')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = self.get_object()  # Esto asegura que el objeto se pasa a la plantilla
        return context
    def form_valid(self, form):
        # Obtén el valor seleccionado del estado desde el formulario
        estado = form.cleaned_data['estadoC']
        # Asigna el valor del estado al objeto conductor antes de guardarlo
        form.instance.estadoC = estado
        return super().form_valid(form)

class ConductorDelete(DeleteView):
    model=Conductor
    template_name='conductor/conductor_delete.html'
    succes_url=reverse_lazy('Conductor_listar')
