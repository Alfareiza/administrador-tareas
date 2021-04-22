import pytest
from django.test import Client
from django.urls import reverse
from webdev.tareas.models import Tarea


@pytest.fixture
def respuesta(client, db):
    resp = client.post(reverse('tareas:home'), data={'nombre': 'Tarea'})
    return resp


def test_tarea_existe_en_bd(respuesta):
    assert Tarea.objects.exists()


@pytest.fixture
def respuesta_dato_invalido(client, db):
    resp = client.post(reverse('tareas:home'), data={'nombre': ''})
    return resp


def test_tarea_no_existe_en_bd(respuesta_dato_invalido):
    assert not Tarea.objects.exists()
