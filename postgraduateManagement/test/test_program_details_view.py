from django.contrib.auth.models import User
from postgraduateManagement.models import Programa, Director, Ciudad, Facultad, TipoPrograma, Pensum, Materia
from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username='testuser', password='12345')
        self.client.force_login(self.user)

        self.ciudad = Ciudad.objects.create(id=1, nombre="ciudadEjemplo1")
        self.facultad = Facultad.objects.create(nombre="Facultad de Ciencias")
        self.tipo_de_programa = TipoPrograma.objects.create(nombre="Maestría")
        self.director = Director.objects.create(
            cedula='123456789',
            nombre='Juan',
            apellido='Pérez',
            email='juan.perez@example.com',
            telefono='1234567890',
            ciudad=self.ciudad
        )
        self.programa = Programa.objects.create(
            codigo='PGM1',
            nombre='Programa 1',
            descripcion='Este es el programa 1',
            facultad=self.facultad,
            tipo_de_programa=self.tipo_de_programa,
            director=self.director
        )

    def test_view_program_summary(self):
        response = self.client.get(reverse('program_summary', args=[self.programa.codigo]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'program_details_summary.html')

    def test_view_program_planning(self):
        response = self.client.get(reverse('program_planning', args=[self.programa.codigo]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'program_details_planning.html')

    def test_view_program_teachers(self):
        response = self.client.get(reverse('program_teachers', args=[self.programa.codigo]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'program_details_teachers.html')

    def test_view_program_subjects(self):
        response = self.client.get(reverse('program_subjects', args=[self.programa.codigo]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'program_details_subjects.html')