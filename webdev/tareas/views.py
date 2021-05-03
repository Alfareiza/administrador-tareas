from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from webdev.tareas.forms import TareaNuevaForm, TareaForm
from webdev.tareas.models import Tarea


def home(request):
    if request.method == 'POST':
        form = TareaNuevaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tareas:home'))
        else:
            tareas_pendientes = Tarea.objects.filter(realizada=False).all()
            tareas_realizadas = Tarea.objects.filter(realizada=True).all()
            return render(request, 'tareas/home.html', {'form': form,
                                                        'tareas_pendientes': tareas_pendientes,
                                                        'tareas_realizadas': tareas_realizadas},
                          status=400)

    tareas_pendientes = Tarea.objects.filter(realizada=False).all()
    tareas_realizadas = Tarea.objects.filter(realizada=True).all()
    return render(request, 'tareas/home.html',
                  {'tareas_pendientes': tareas_pendientes,
                   'tareas_realizadas': tareas_realizadas})


def detalle(request, tarea_id):
    if request.method == 'POST':
        tarea = Tarea.objects.get(id=tarea_id)
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect(reverse('tareas:home'))


def eliminar(request, tarea_id):
    if request.method == 'POST':
        Tarea.objects.get(id=tarea_id).delete()
    return HttpResponseRedirect(reverse('tareas:home'))
