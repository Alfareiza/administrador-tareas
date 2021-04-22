import pytest
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertContains


@pytest.fixture
def respuesta(client):
    resp = client.get(reverse('tareas:home'))
    return resp


def test_status_code(respuesta):
    assert respuesta.status_code == 200


def test_formulario_presente(respuesta):
    assertContains(respuesta, '<form')


def test_button_guardar_presente(respuesta):
    assertContains(respuesta, '<button type="submit')
