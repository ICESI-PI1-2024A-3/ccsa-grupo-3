from django.contrib.auth.models import User
from django.urls import reverse

from postgraduateManagement.models import Docente, Ciudad
import unittest
from django.test import TestCase


class TestViews(TestCase):

    def setUp(self):
        # Creamos un objeto de prueba Docente para usar en las pruebas
        self.docente = Docente.objects.create(
            cedula='123456789',
            nombre='Juan',
            apellido='Perez',
            email='juan@example.com',
            telefono='123456789',
            url_foto='http://example.com',
            ciudad=Ciudad.objects.create(id=1, nombre='Ciudad de Ejemplo'),
            estado='activo'
        )

    def test_teacher_filter_by_city1(self):
        self.user = User.objects.create_superuser(username='testuser', password='12345')
        self.client.force_login(self.user)
        response = self.client.get('/docentes/?search_contains=&status=activo&city=1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teachers.html')
        self.assertTrue(all(teachers.ciudad.id == 1 for teachers in response.context['teacher_list']))
        self.assertTrue(all(teachers.estado == 'activo' for teachers in response.context['teacher_list']))

    def test_teacher_filter_by_city2(self):
        self.user = User.objects.create_superuser(username='testuser', password='12345')
        self.client.force_login(self.user)
        response = self.client.get('/docentes/?search_contains=&status=activo&city=2')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teachers.html')
        self.assertTrue(all(teachers.ciudad.id == 2 for teachers in response.context['teacher_list']))
        self.assertTrue(all(teachers.estado == 'activo' for teachers in response.context['teacher_list']))

    def test_teacher_filter_by_status(self):
        self.user = User.objects.create_superuser(username='testuser', password='12345')
        self.client.force_login(self.user)
        response = self.client.get('/docentes/?search_contains=&status=inactivo&city=')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teachers.html')
        self.assertTrue(all(teachers.estado == 'inactivo' for teachers in response.context['teacher_list']))

    def test_teacher_filter_by_search1(self):
        self.user = User.objects.create_superuser(username='testuser', password='12345')
        self.client.force_login(self.user)
        response = self.client.get('/docentes/?search_contains=Test1&status=activo&city=')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teachers.html')
        self.assertTrue(all('Test1' in teachers.nombre for teachers in response.context['teacher_list']))

    def test_teacher_filter_by_search2(self):
        self.user = User.objects.create_superuser(username='testuser', password='12345')
        self.client.force_login(self.user)
        response = self.client.get('/docentes/?search_contains=Test3&status=activo&city=')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teachers.html')
        self.assertTrue(all('Test3' in teachers.nombre for teachers in response.context['teacher_list']))

        def test_get_object(self):
            response = self.client.get(reverse('state', kwargs={'cedula': self.docente.cedula}))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.context['docente'], self.docente)

        def test_get_context_data(self):
            # Testeamos si el contexto contiene el objeto Docente
            response = self.client.get(reverse('state', kwargs={'cedula': self.docente.cedula}))
            self.assertEqual(response.status_code, 200)
            self.assertTrue('docente' in response.context)
            self.assertEqual(response.context['docente'], self.docente)

        def test_update_view(self):
            # Testeamos si la vista de actualización funciona correctamente
            new_estado = 'inactivo'
            response = self.client.post(reverse('state', kwargs={'cedula': self.docente.cedula}),
                                        {'estado': new_estado})
            self.assertEqual(response.status_code, 302)  # Debería redirigir después de una actualización exitosa
            updated_docente = Docente.objects.get(cedula=self.docente.cedula)
            self.assertEqual(updated_docente.estado, new_estado)


if __name__ == '__main__':
    unittest.main()
