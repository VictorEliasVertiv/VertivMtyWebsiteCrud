from django.shortcuts import render, redirect
from .models import Empleado
from .forms import EmpleadoForm

# Create your views here.

def empleado_lista(request):
    empleado = Empleado.objects.all()
    context = {
        'empleado': empleado,
    }
    return render(request, 'empleado/lista.html', context)


def crear_empleado(request):
    form = EmpleadoForm()

    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleados-lista')

    context = {
        'form': form,
    }
    return render(request, 'empleado/crear.html', context)


def editar_empleado(request, pk):
    empleado = Empleado.objects.get(id=pk)
    form = EmpleadoForm(instance=empleado)

    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('empleados-lista')

    context = {
        'empleado': empleado,
        'form': form,
    }
    return render(request, 'empleado/editar.html', context)


def eliminar_empleado(request, pk):
    empleado = Empleado.objects.get(id=pk)

    if request.method == 'POST':
        empleado.delete()
        return redirect('empleados-lista')

    context = {
        'empleado': empleado,
    }
    return render(request, 'empleado/eliminar.html',context)