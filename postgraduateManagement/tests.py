from django.test import TestCase

# Create your tests here.


import unittest
from django.urls import reverse
from django.test import TestCase
from .models import Curso, Departamento, Materia, Usuario, Periodo
from postgraduateManagement.Views.CourseViews import *


class TestViews(TestCase):

    def setUp(self):
        # Crear un departamento de prueba
        self.departamento_prueba = Departamento.objects.create(
            codigo="DEP001",
            nombre="Departamento de Prueba"
        )

        # Crear un usuario de prueba
        self.usuario_prueba = Usuario.objects.create(
            id=1,
            nombre="Nombre de Prueba",
            apellido="Apellido de Prueba"
        )

        # Crear un periodo de prueba
        self.periodo_prueba = Periodo.objects.create(
            semestre="2023-01",
            fecha_inicio="2023-01-01",
            fecha_fin="2023-05-31"
        )

        # Crear una materia de prueba asociada al departamento de prueba
        self.materia_prueba = Materia.objects.create(
            codigo="MAT001",
            nombre="Materia de Prueba",
            creditos=3,
            departamento=self.departamento_prueba
        )

        # Crear un curso de prueba relacionado con la materia de prueba, usuario de prueba y periodo de prueba
        self.curso = Curso.objects.create(
            nrc="12345",
            grupo="Grupo de Prueba",
            cupo=30,
            materia=self.materia_prueba,
            usuario=self.usuario_prueba,
            periodo=self.periodo_prueba
        )

    def test_course_view(self):
        response = self.client.get(
            '/subjectmanagment/MateriaCodigo/') 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'postgraduateManagement/../curso_list.html')

    def test_course_delete_view(self):
        response = self.client.post(reverse('course_delete', kwargs={'pk': self.curso.pk}))
        self.assertEqual(response.status_code, 302)

    def test_course_update_view(self):
        response = self.client.post(reverse('course_update', kwargs={'codigo_materia': 'MAT001', 'pk': self.curso.pk}),
                                    {
                                        'grupo': 'Nuevo Grupo',
                                        'cupo': 40,
                                        'usuario': self.usuario_prueba.pk,
                                        'periodo': self.periodo_prueba.semestre
                                    })
        self.assertEqual(response.status_code, 200)

    def test_course_create_view(self):
        response = self.client.post(reverse('course_create'), {
            'materia': self.materia_prueba.pk,
            'nrc': '54321',
            'grupo': 'Nuevo Grupo',
            'cupo': 20,
            'usuario': self.usuario_prueba.pk,
            'periodo': self.periodo_prueba.semestre
        })
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
