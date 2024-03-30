from postgraduateManagement.models import Docente, Ciudad
import unittest
from django.test import TestCase


class TestViews(TestCase):
    def setUp(self):
        self.ciudad1 = Ciudad.objects.create(
            id=1,
            nombre="ciudadEjemplo1"
        )

        self.ciudad2 = Ciudad.objects.create(
            id=2,
            nombre="ciudadEjemplo2"
        )

        self.ciudad3 = Ciudad.objects.create(
            id=3,
            nombre="ciudadEjemplo3"
        )

        self.teacher1_test = Docente.objects.create(
            cedula='12-345-6789',
            nombre='Test1',
            apellido='Teacher',
            email='emailexample@gmail.com',
            telefono='0987654321',
            url_foto='URL',
            ciudad=self.ciudad1,
            estado='activo',
        )

        self.teacher2_test = Docente.objects.create(
            cedula='23-456-4538',
            nombre='Test2',
            apellido='Teacher',
            email='emailexample@gmail.com',
            telefono='0987654321',
            url_foto='URL',
            ciudad=self.ciudad2,
            estado='activo',
        )

        self.teacher3_test = Docente.objects.create(
            cedula='65-635-3627',
            nombre='Test3',
            apellido='Teacher',
            email='emailexample@gmail.com',
            telefono='0987654321',
            url_foto='URL',
            ciudad=self.ciudad3,
            estado='inactivo',
        )

    def test_teacher_view(self):
        response = self.client.get('/graduate/teachers/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'teachers.html')
    
    def test_teacher_filter_by_city1(self):
        response = self.client.get('/graduate/teachers/?search_contains=&status=activo&city=1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'teachers.html')
        self.assertTrue(all(teachers.ciudad.id == 1 for teachers in response.context['teacher_list']))
        self.assertTrue(all(teachers.estado == 'activo' for teachers in response.context['teacher_list']))

    def test_teacher_filter_by_city2(self):
        response = self.client.get('/graduate/teachers/?search_contains=&status=activo&city=2')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'teachers.html')
        self.assertTrue(all(teachers.ciudad.id == 2 for teachers in response.context['teacher_list']))
        self.assertTrue(all(teachers.estado == 'activo' for teachers in response.context['teacher_list']))

    def test_teacher_filter_by_status(self):
        response = self.client.get('/graduate/teachers/?search_contains=&status=inactivo&city=')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'teachers.html')
        self.assertTrue(all(teachers.estado == 'inactivo' for teachers in response.context['teacher_list']))

    def test_teacher_filter_by_search1(self):
        response = self.client.get('/graduate/teachers/?search_contains=Test1&status=activo&city=')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'teachers.html')
        self.assertTrue(all('Test1' in teachers.nombre for teachers in response.context['teacher_list']))

    def test_teacher_filter_by_search2(self):
        response = self.client.get('/graduate/teachers/?search_contains=Test3&status=activo&city=')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'teachers.html')
        self.assertTrue(all('Test3' in teachers.nombre for teachers in response.context['teacher_list']))

if __name__ == '__main__':
    unittest.main()