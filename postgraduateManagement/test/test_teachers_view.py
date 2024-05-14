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
        """
        Prueba de filtrado de docentes por ciudad (Caso 1).

        Se crea un superusuario para simular la sesión. Luego, se realiza una solicitud GET con los parámetros de búsqueda
        correspondientes a la ciudad 1 y estado activo. Se verifica que la página responda correctamente (código 200) y que
        la plantilla 'teachers.html' sea utilizada. Se asegura que todos los docentes en la lista de contexto pertenezcan a
        la ciudad 1 y tengan estado activo.

        :return: None
        """

        self.user = User.objects.create_superuser(username='testuser', password='12345')
        self.client.force_login(self.user)
        response = self.client.get('/docentes/?search_contains=&status=activo&city=1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teachers.html')
        self.assertTrue(all(teachers.ciudad.id == 1 for teachers in response.context['teacher_list']))
        self.assertTrue(all(teachers.estado == 'activo' for teachers in response.context['teacher_list']))

    def test_teacher_filter_by_city2(self):
        """
        Prueba de filtrado de docentes por ciudad (Caso 2).

        Similar a test_teacher_filter_by_city1, pero para la ciudad 2.

        :return: None
        """

        self.user = User.objects.create_superuser(username='testuser', password='12345')
        self.client.force_login(self.user)
        response = self.client.get('/docentes/?search_contains=&status=activo&city=2')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teachers.html')
        self.assertTrue(all(teachers.ciudad.id == 2 for teachers in response.context['teacher_list']))
        self.assertTrue(all(teachers.estado == 'activo' for teachers in response.context['teacher_list']))

    def test_teacher_filter_by_status(self):
        """
        Prueba de filtrado de docentes por estado.

        Se crea un superusuario para simular la sesión. Se realiza una solicitud GET con el estado 'inactivo' y sin
        especificar ciudad. Se verifica que la página responda correctamente (código 200) y que la plantilla 'teachers.html'
        sea utilizada. Se asegura que todos los docentes en la lista de contexto tengan estado 'inactivo'.

        :return: None
        """

        self.user = User.objects.create_superuser(username='testuser', password='12345')
        self.client.force_login(self.user)
        response = self.client.get('/docentes/?search_contains=&status=inactivo&city=')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teachers.html')
        self.assertTrue(all(teachers.estado == 'inactivo' for teachers in response.context['teacher_list']))

    def test_teacher_filter_by_search1(self):
        """
        Prueba de filtrado de docentes por búsqueda (Caso 1).

        Se crea un superusuario para simular la sesión. Se realiza una solicitud GET con el parámetro 'search_contains'
        establecido como 'Test1' para buscar docentes cuyo nombre contenga esa cadena, y se especifica estado activo y sin
        ciudad. Se verifica que la página responda correctamente (código 200) y que la plantilla 'teachers.html' sea
        utilizada. Se asegura que todos los docentes en la lista de contexto tengan 'Test1' en su nombre.

        :return: None
        """

        self.user = User.objects.create_superuser(username='testuser', password='12345')
        self.client.force_login(self.user)
        response = self.client.get('/docentes/?search_contains=Test1&status=activo&city=')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teachers.html')
        self.assertTrue(all('Test1' in teachers.nombre for teachers in response.context['teacher_list']))

    def test_teacher_filter_by_search2(self):
        """
        Prueba de filtrado de docentes por búsqueda (Caso 2).

        Similar a test_teacher_filter_by_search1, pero para buscar la cadena 'Test3'.

        :return: None
        """

        self.user = User.objects.create_superuser(username='testuser', password='12345')
        self.client.force_login(self.user)
        response = self.client.get('/docentes/?search_contains=Test3&status=activo&city=')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teachers.html')
        self.assertTrue(all('Test3' in teachers.nombre for teachers in response.context['teacher_list']))


if __name__ == '__main__':
    unittest.main()
