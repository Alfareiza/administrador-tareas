from django.urls import path

from webdev.tareas import views

app_name = 'tareas'

urlpatterns = [
    path('', views.home, name='home')
]
