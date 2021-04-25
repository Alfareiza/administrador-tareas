from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from webdev.tareas.forms import TareaNuevaForm
from webdev.tareas.models import Tarea


def home(request):
    if request.method == 'POST':
        form = TareaNuevaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tareas:home'))
        else:
            tareas_pendientes = Tarea.objects.filter(realizada=False).all()
            return render(request, 'tareas/home.html', {'form': form, 'tareas_pendientes': tareas_pendientes},
                          status=400)

    tareas_pendientes = Tarea.objects.filter(realizada=False).all()
    return render(request, 'tareas/home.html', {'tareas_pendientes': tareas_pendientes})
