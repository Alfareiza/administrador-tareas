from django.forms import ModelForm

from webdev.tareas.models import Tarea


class TareaNuevaForm(ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre']
