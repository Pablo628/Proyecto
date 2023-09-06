from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from apps.conductor.form import ConductorForm
from apps.conductor.models import Conductor,EstadoC

# Create your views here.
def index(request):
    return render(request, 'conductor/index.html')

def conductor_view(request):
    estados=EstadoC.objects.all()
    context={
        'estadoC':estados
    }
    if request.method =='POST':
        form = ConductorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conductor_listar')
    else:
        form=ConductorForm()
    return render (request, 'conductor/conductor_form.html', {'form':form})

def conductor_list(request):
    conductor=Conductor.objects.all().order_by('id')
    contexto={'conductores':conductor}
    return render(request, 'conductor/conductor_list.html', contexto)

def conductor_edit(request, id_conductor):
    conductor=Conductor.objects.get(id=id_conductor)
    if request.method=='GET':
        form=ConductorForm(instance=conductor)
    else:
        form=ConductorForm(request.POST, instance=conductor)
        if form.is_valid():
            form.save()
        return redirect('conductor_listar')
    return render(request, 'conductor/conductor_form.html', {'form':form})



def conductor_delete(request, id_conductor):
    conductor=Conductor.objects.get(id=id_conductor)
    print(id_conductor)
    if request.method=='POST':
        conductor.delete()
        return redirect('conductor_listar')
    return render(request, 'conductor/conductor_delete.html', {'conductor':conductor})
