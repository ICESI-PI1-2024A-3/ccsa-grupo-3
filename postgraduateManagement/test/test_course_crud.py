# Create your tests here.
import unittest

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpRequest
from django.test import TestCase
from django.urls import reverse
from postgraduateManagement.views.views_course import *
from postgraduateManagement.models import Departamento, Usuario, Periodo, Programa, Director, Facultad, TipoPrograma, \
    Ciudad


class TestViews(TestCase):

    def setUp(self):
        # Crear un departamento de prueba
        self.departamento_prueba = Departamento.objects.create(
            codigo="DEP001",
            nombre="Depar"
        )

        # Crear un usuario de prueba
        self.usuario_prueba = Usuario.objects.create(
            id=1,
            nombre="Nombre de Prueba",
            apellido="Apellido de Prueba",
        )

        self.user = User.objects.create_superuser(username='testuser', password='12345')
        self.client.force_login(self.user)

        # Crear un periodo de prueba
        self.periodo_prueba = Periodo.objects.create(
            semestre="20",
            fecha_inicio="2023-01-01",
            fecha_fin="2023-05-31"
        )

        # Crear una materia de prueba asociada al departamento de prueba
        self.materia_prueba = Materia.objects.create(
            codigo="MAT001",
            nombre="Materia",
            creditos=3,
            departamento=self.departamento_prueba
        )

        # Crear un curso de prueba relacionado con la materia de prueba, usuario de prueba y periodo de prueba
        self.curso = Curso.objects.create(
            nrc="12",
            grupo="23",
            cupo=30,
            materia=self.materia_prueba,
            usuario=self.usuario_prueba,
            periodo=self.periodo_prueba
        )

        self.facultad2 = Facultad.objects.create(id='01', nombre='por')

        self.tipoprograma = TipoPrograma.objects.create(id='90', nombre='por')

        self.ciudad = Ciudad.objects.create(id='01', nombre='c')

        self.directorprueba = Director.objects.create(ciudad=self.ciudad)

        self.Programa_prueba = Programa.objects.create(codigo='00', nombre='Programa', descripcion="lalo",
                                                       facultad=self.facultad2, tipo_de_programa=self.tipoprograma,
                                                       director=self.directorprueba)

    def test_subject_list_view(self):
        # Prueba que la vista de lista de materias carga correctamente y utiliza el template adecuado
        response = self.client.get(reverse('program_subjects', kwargs={'codigo': '00'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'program_details_subjects.html')

    def test_course_view(self):
        response = self.client.get(reverse('courseview', kwargs={'codigo': 00, 'codigo_materia': 'MateriaCodigo'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'postgraduateManagement/../course_list.html')

    def test_course_view_with_material_code(self):
        response = self.client.get(reverse('courseview', kwargs={'codigo': 00, 'codigo_materia': 'MAT001'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'postgraduateManagement/../course_list.html')

    def test_course_view_with_nonexistent_material_code(self):
        response = self.client.get(reverse('courseview', kwargs={'codigo': 98, 'codigo_materia': 'NO_EXISTE'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'postgraduateManagement/../course_list.html')
        self.assertEqual(response.context['object_list'].count(), 0)

    def test_course_delete_view(self):
        response = self.client.post(
            reverse('course_delete', kwargs={'codigo': 00, 'codigo_materia': 'MAT001', 'pk': self.curso.pk}))
        self.assertEqual(response.status_code, 302)

    def test_nonexistent_course_delete_view(self):
        response = self.client.post(
            reverse('course_delete', kwargs={'codigo': 00, 'codigo_materia': 'MAT001', 'pk': 99}))
        self.assertEqual(response.status_code, 404)  # Asegurar que se devuelve un error 404 para el curso inexistente

    def test_course_update_view(self):
        response = self.client.post(
            reverse('course_update', kwargs={'codigo': '00', 'codigo_materia': 'MAT001', 'pk': self.curso.pk}),
            {
                'grupo': '58',
                'cupo': 40,
                'usuario': self.usuario_prueba.pk,
                'periodo': self.periodo_prueba.semestre
            })
        self.assertEqual(response.status_code, 200)

    def test_invalid_course_update_view(self):
        response = self.client.post(
            reverse('course_update', kwargs={'codigo': '00', 'codigo_materia': 'MAT001', 'pk': self.curso.pk}),
            {
                'grupo': '',  # Grupo vacío, lo que debería ser inválido
                'cupo': -10,  # Cupo negativo, lo que debería ser inválido
                'usuario': 99,  # ID de usuario no existente
                'periodo': '2023-10'  # Período inexistente
            })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'postgraduateManagement/../edit_course.html')

    def test_duplicate_group_course_update_view(self):
        otro_curso = Curso.objects.create(
            nrc="56",
            grupo="59",
            cupo=20,
            materia=self.materia_prueba,
            usuario=self.usuario_prueba,
            periodo=self.periodo_prueba
        )

        response = self.client.post(
            reverse('course_update', kwargs={'codigo': '00', 'codigo_materia': 'MAT001', 'pk': self.curso.pk}),
            {
                'grupo': '23',
                'cupo': 40,
                'usuario': self.usuario_prueba.pk,
                'periodo': self.periodo_prueba.semestre
            })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'postgraduateManagement/../edit_course.html')

    def test_course_create_view(self):
        response = self.client.post(reverse('course_create', kwargs={'codigo': '00', 'codigo_materia': 'MAT001'}), {
            'materia': self.materia_prueba.pk,
            'nrc': '54',
            'grupo': '6',
            'cupo': 20,
            'usuario': self.usuario_prueba.pk,
            'periodo': self.periodo_prueba.semestre
        })
        self.assertEqual(response.status_code, 200)

    def test_invalid_course_create_view(self):
        response = self.client.post(reverse('course_create', kwargs={'codigo': '00', 'codigo_materia': 'MAT001'}), {
            'materia': 99,  # ID de materia no existente
            'nrc': '',  # NRC vacío, lo que debería ser inválido
            'grupo': '35',
            'cupo': -5,  # Cupo negativo, lo que debería ser inválido
            'usuario': 999,  # ID de usuario no existente
            'periodo': '2023-10'  # Período inexistente
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'postgraduateManagement/../create_course.html')

    def test_duplicate_course_create_view(self):
        response = self.client.post(reverse('course_create', kwargs={'codigo': '00', 'codigo_materia': 'MAT001'}), {
            'materia': self.materia_prueba.pk,
            'nrc': '54',
            'grupo': '25',
            'cupo': 20,
            'usuario': self.usuario_prueba.pk,
            'periodo': self.periodo_prueba.semestre
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'postgraduateManagement/../create_course.html')


if __name__ == '__main__':
    unittest.main()
