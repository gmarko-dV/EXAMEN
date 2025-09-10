from django.shortcuts import render, redirect
from .models import Paciente
from .forms import PacienteForm

def paciente(request):
    pacientes = Paciente.objects.all()
    return render(request, 'listado_pac.html', {'paciente': pacientes})

def create_pac(request):
    if request.method == 'GET':
        return render(request, 'create_paciente.html', {
            'form': PacienteForm()
        })
    else:
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paciente')
        return render(request, 'create_paciente.html', {
            'form': form,
            'error': 'Ingrese Datos Válidos'
        })