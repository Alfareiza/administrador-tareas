import pytest
from django.urls import reverse
from django.test import TestCase

_test_case = TestCase()

assert_contains = _test_case.assertContains
assert_not_contains = _test_case.assertNotContains


@pytest.fixture
def respuesta(client, db):
    resp = client.get(reverse('tareas:home'))
    return resp


def test_status_code(respuesta):
    assert respuesta.status_code == 200


def test_formulario_presente(respuesta):
    assert_contains(respuesta, '<form')


def test_button_guardar_presente(respuesta):
    assert_contains(respuesta, '<button type="submit')
