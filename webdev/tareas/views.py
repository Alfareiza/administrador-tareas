from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from webdev.tareas.forms import TareaNuevaForm


def home(request):
    if request.method == 'POST':
        form = TareaNuevaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'tareas/home.html', {'form': form}, status=400)

    return render(request, 'tareas/home.html')
