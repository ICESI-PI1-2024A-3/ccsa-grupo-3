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



    def test_codigo_programa_inexistente(self):
        response = self.client.get(
            '/eliminarPrograma/123234E/')

        self.assertEqual(response.status_code, 302)




    def test_editing_director_view(self):
            url = reverse('editing_director')
            response = self.client.post(url, {'txtCodigo': self.director.cedula, 'nombre': 'Nuevo Nombre',
                                              'apellido': 'Nuevo Apellido', 'email': 'nuevo@example.com',
                                              'telefono': '987654321', 'ciudad': self.ciudad.nombre})
            self.assertEqual(response.status_code, 302)  # Check for redirect



    def test_edicion_programa_view(self):
                url = reverse('edicion_programa')
                response = self.client.post(url, {'txtCodigo': self.programa.codigo, 'facultad': self.facultad.nombre,
                                                  'tipoPrograma': self.tipo_programa.nombre})
                self.assertEqual(response.status_code, 302)  # Check for redirect