# Create your tests here.
import unittest
from django.test import TestCase
from django.urls import reverse
from postgraduateManagement.views.CourseViews import *
from postgraduateManagement.models import Departamento, Usuario, Periodo


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
            '/subjects/subjectmanagment/MateriaCodigo/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'postgraduateManagement/../courseList.html')

    def test_course_view_with_material_code(self):
        response = self.client.get('/subjects/subjectmanagment/MAT001/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'postgraduateManagement/../courseList.html')
        # Asegurar que solo los cursos con el código de materia correcto se muestran en la lista
        self.assertTrue(all(course.materia.codigo == 'MAT001' for course in response.context['object_list']))

    def test_course_view_with_nonexistent_material_code(self):
        response = self.client.get('/subjects/subjectmanagment/NO_EXISTE/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'postgraduateManagement/../courseList.html')
        # Asegurar que no se encuentren cursos en la lista
        self.assertEqual(response.context['object_list'].count(), 0)

    def test_course_delete_view(self):
        response = self.client.post(reverse('course_delete', kwargs={'pk': self.curso.pk}))
        self.assertEqual(response.status_code, 302)

    def test_nonexistent_course_delete_view(self):
        response = self.client.post(reverse('course_delete', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, 404)  # Asegurar que se devuelve un error 404 para el curso inexistente

    def test_course_update_view(self):
        response = self.client.post(reverse('course_update', kwargs={'codigo_materia': 'MAT001', 'pk': self.curso.pk}),
                                    {
                                        'grupo': 'Nuevo Grupo',
                                        'cupo': 40,
                                        'usuario': self.usuario_prueba.pk,
                                        'periodo': self.periodo_prueba.semestre
                                    })
        self.assertEqual(response.status_code, 200)

    def test_invalid_course_update_view(self):
        response = self.client.post(reverse('course_update', kwargs={'codigo_materia': 'MAT001', 'pk': self.curso.pk}),
                                    {
                                        'grupo': '',  # Grupo vacío, lo que debería ser inválido
                                        'cupo': -10,  # Cupo negativo, lo que debería ser inválido
                                        'usuario': 999,  # ID de usuario no existente
                                        'periodo': '2023-10'  # Período inexistente
                                    })
        self.assertEqual(response.status_code, 200)

    def test_duplicate_group_course_update_view(self):
        # Crear otro curso con el mismo grupo
        otro_curso = Curso.objects.create(
            nrc="54321",
            grupo="Nuevo Grupo Duplicado",
            cupo=20,
            materia=self.materia_prueba,
            usuario=self.usuario_prueba,
            periodo=self.periodo_prueba
        )

        # Intentar actualizar el curso existente con el mismo grupo que el curso recién creado
        response = self.client.post(reverse('course_update', kwargs={'codigo_materia': 'MAT001', 'pk': self.curso.pk}),
                                    {
                                        'grupo': 'Nuevo Grupo Duplicado',
                                        'cupo': 40,
                                        'usuario': self.usuario_prueba.pk,
                                        'periodo': self.periodo_prueba.semestre
                                    })

        # Verificar que la vista redirige de nuevo al formulario de edición
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'postgraduateManagement/../editCourse.html')

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

    def test_invalid_course_create_view(self):
        response = self.client.post(reverse('course_create'), {
            'materia': 999,  # ID de materia no existente
            'nrc': '',  # NRC vacío, lo que debería ser inválido
            'grupo': 'Nuevo Grupo',
            'cupo': -5,  # Cupo negativo, lo que debería ser inválido
            'usuario': 999,  # ID de usuario no existente
            'periodo': '2023-10'  # Período inexistente
        })
        self.assertEqual(response.status_code, 200)

    def test_duplicate_course_create_view(self):
        # Intentar crear una materia con la misma clave primaria que otra ya existente
        response = self.client.post(reverse('course_create'), {
            'materia': self.materia_prueba.pk,  # Utilizamos el ID de una materia ya existente
            'nrc': '54321',
            'grupo': 'Nuevo Grupo',
            'cupo': 20,
            'usuario': self.usuario_prueba.pk,
            'periodo': self.periodo_prueba.semestre
        })
        # Verificar que la vista redirige a la misma página de creación
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'postgraduateManagement/../createCourse.html')


if __name__ == '__main__':
    unittest.main()
