from postgraduateManagement.models import Docente, Ciudad
import unittest
from django.test import TestCase


class TestViews(TestCase):
    def test_teacher_filter_by_city1(self):
        response = self.client.get('/docentes/?search_contains=&status=activo&city=1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teachers.html')
        self.assertTrue(all(teachers.ciudad.id == 1 for teachers in response.context['teacher_list']))
        self.assertTrue(all(teachers.estado == 'activo' for teachers in response.context['teacher_list']))

    def test_teacher_filter_by_city2(self):
        response = self.client.get('/docentes/?search_contains=&status=activo&city=2')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teachers.html')
        self.assertTrue(all(teachers.ciudad.id == 2 for teachers in response.context['teacher_list']))
        self.assertTrue(all(teachers.estado == 'activo' for teachers in response.context['teacher_list']))

    def test_teacher_filter_by_status(self):
        response = self.client.get('/docentes/?search_contains=&status=inactivo&city=')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teachers.html')
        self.assertTrue(all(teachers.estado == 'inactivo' for teachers in response.context['teacher_list']))

    def test_teacher_filter_by_search1(self):
        response = self.client.get('/docentes/?search_contains=Test1&status=activo&city=')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teachers.html')
        self.assertTrue(all('Test1' in teachers.nombre for teachers in response.context['teacher_list']))

    def test_teacher_filter_by_search2(self):
        response = self.client.get('/docentes/?search_contains=Test3&status=activo&city=')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teachers.html')
        self.assertTrue(all('Test3' in teachers.nombre for teachers in response.context['teacher_list']))


if __name__ == '__main__':
    unittest.main()
