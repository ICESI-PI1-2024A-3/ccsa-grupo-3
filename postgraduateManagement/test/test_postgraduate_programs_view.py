from django.contrib.auth.models import User

from postgraduateManagement.models import Director, Ciudad, Programa, Facultad, TipoPrograma
import unittest
from django.test import TestCase


class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='testuser', password='12345')
        self.client.force_login(self.user)
        self.ciudad = Ciudad.objects.create(
            id=1,
            nombre="ciudadEjemplo1"
        )
        self.facultad = Facultad.objects.create(nombre="Facultad de Ciencias")
        self.tipo_de_programa = TipoPrograma.objects.create(nombre="Maestría")

        self.director = Director.objects.create(
            cedula='123456789',
            nombre='Juan',
            apellido='Pérez',
            email='juan.perez@example.com',
            telefono='1234567890',
            url_foto='http://example.com/image.jpg',
            ciudad=self.ciudad
        )

        self.programa1 = Programa.objects.create(
            codigo='PGM1',
            nombre='Programa 1',
            descripcion='Este es el programa 1',
            url_image='http://example.com/image1.jpg',
            facultad=self.facultad,
            tipo_de_programa=self.tipo_de_programa,
            director=self.director
        )

        self.programa2 = Programa.objects.create(
            codigo='PGM2',
            nombre='Programa 2',
            descripcion='Este es el programa 2',
            url_image='http://example.com/image2.jpg',
            facultad=self.facultad,
            tipo_de_programa=self.tipo_de_programa,
            director=self.director
        )

    def test_programs_view_get(self):
        response = self.client.get('/programas/')
        self.assertEqual(len(response.context['programas']), 2)

    def test_programs_view_post(self):
        response = self.client.post(
            '/programas/', data={'programa_codigo': 'PGM1'})
        self.assertEqual(
            response.context['programa_seleccionado'], self.programa1)


if __name__ == '__main__':
    unittest.main()
