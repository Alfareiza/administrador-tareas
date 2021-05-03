from django.forms import ModelForm

from webdev.tareas.models import Tarea


class TareaNuevaForm(ModelForm):
    """
    Este formulario va a tratar la entrada de tareas, solamente capturando su nombre.
    """

    class Meta:
        model = Tarea
        fields = ['nombre']


class TareaForm(ModelForm):
    """
    Este formulario va a tratar todos los campos de la tarea existente.
    """

    class Meta:
        model = Tarea
        fields = ['nombre', 'realizada']
