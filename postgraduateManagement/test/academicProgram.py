import unittest
from django.test import TestCase, Client
from django.urls import reverse
from postgraduateManagement.views import viewProgramPosgraduates, eliminarPrograma, editingDirector, edicionPrograma
from postgraduateManagement.models import Departamento, Usuario, Periodo

from django.test import TestCase
from django.urls import reverse
from postgraduateManagement.models import *
from django.contrib.auth.models import User


class MiVistaTest(TestCase):
    def setUp(self):

        self.ciudad = Ciudad.objects.create(
            id=52,
            nombre="Prueba"
        )

        self.facultad = Facultad.objects.create(
            id=1,
            nombre="Facultad de Prueba"
        )

        self.tipo_programa = TipoPrograma.objects.create(
            id=1,
            nombre="Tipo de Programa de Prueba"
        )

        self.director = Director.objects.create(
            cedula="1234567890",
            nombre="Nombre de Prueba",
            apellido="Apellido de Prueba",
            email="correo@prueba.com",
            telefono="1234567890",
            url_foto="http://url_de_prueba.com",
            ciudad=self.ciudad

        )

        self.programa = Programa.objects.create(
            codigo="123234E",
            nombre="Programa de Prueba",
            descripcion="descripcion",
            facultad=self.facultad,
            tipo_de_programa=self.tipo_programa,
            director=self.director
        )

    def test_vista_programa_posgraduados(self):
        response = self.client.get(
            '/subjects/verProgramacion/123234E/')

        self.assertEqual(response.status_code, 200)

    def test_codigo_programa_inexistente(self):
        response = self.client.get(
            '/subjects/eliminarPrograma/123234E/')

        self.assertEqual(response.status_code, 302)

    def test3(self):
        response = self.client.get(
            '/subjects/editarDirector/1234567890/')

        self.assertEqual(response.status_code, 200)

        def test_editing_director_post(self):
            # Datos a enviar en el POST
            data = {
                'txtCodigo': '1234567890',
                'nombre': 'Nuevo Nombre',
                'apellido': 'Nuevo Apellido',
                'email': 'nuevo@example.com',
                'telefono': '987654321',
                'ciudad': 'Test Ciudad'
            }

            response = self.client.post(
                reverse('/subjects/editing_director'), data)
            # Verifica si la redirección es exitosa
            self.assertEqual(response.status_code, 302)

            # Verifica si los datos del director se han actualizado correctamente en la base de datos
            director_actualizado = Director.objects.get(cedula='1234567890')
            self.assertEqual(director_actualizado.nombre, 'Nuevo Nombre')
            self.assertEqual(director_actualizado.apellido, 'Nuevo Apellido')
            self.assertEqual(director_actualizado.email, 'nuevo@example.com')
            self.assertEqual(director_actualizado.telefono, '987654321')
