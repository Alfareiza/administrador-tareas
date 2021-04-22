from django.db import models


# Create your models here.
class Tarea(models.Model):
    nombre = models.CharField(max_length=128, )
    realizada = models.BooleanField(default=False)
