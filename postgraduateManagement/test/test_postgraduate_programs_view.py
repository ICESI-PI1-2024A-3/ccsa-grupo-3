import unittest

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from postgraduateManagement.models import Director, Ciudad, Programa, Facultad, TipoPrograma


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

    def test_home_view_get(self):
        """
        Prueba la vista de inicio.

        Realiza una solicitud GET a la URL raíz. Verifica que se utilice la plantilla 'home.html'.

        :return: None
        """
        response = self.client.get('')
        self.assertTemplateUsed('home.html')

    def test_programs_view_get(self):
        """
        Prueba la vista de programas con una solicitud GET.

        Realiza una solicitud GET a la URL '/programas/'. Verifica que el número de programas en el contexto sea igual a 2.

        :return: None
        """
        response = self.client.get('/programas/')
        self.assertEqual(len(response.context['programas']), 2)

    def test_programs_view_post(self):
        """
        Prueba la vista de programas con una solicitud POST.

        Realiza una solicitud POST a la URL '/programas/' con el código de programa 'PGM1'. Verifica que el programa
        seleccionado en el contexto sea igual a 'programa1'.

        :return: None
        """
        response = self.client.post('/programas/', data={'programa_codigo': 'PGM1'})
        self.assertEqual(response.context['programa_seleccionado'], self.programa1)

    def test_programs_view_post_with_existing_program(self):
        """
        Prueba la vista de programas con una solicitud POST con un programa existente.

        Realiza una solicitud POST a la URL '/programas/' con el código de programa 'PGM1'. Verifica que la respuesta tenga
        un código de estado 200 y que el programa seleccionado en el contexto sea igual a 'programa1'.

        :return: None
        """
        response = self.client.post('/programas/', data={'programa_codigo': 'PGM1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['programa_seleccionado'], self.programa1)

    def test_programs_view_post_with_non_existing_program(self):
        """
        Prueba la vista de programas con una solicitud POST con un programa no existente.

        Realiza una solicitud POST a la URL '/programas/' con un código de programa no existente 'PGM99'. Verifica que se
        genere una excepción de 'ObjectDoesNotExist'.

        :return: None
        """
        with self.assertRaises(ObjectDoesNotExist):
            response = self.client.post('/programas/', data={'programa_codigo': 'PGM99'})

    def test_programs_view_post_with_no_program_code(self):
        """
        Prueba la vista de programas con una solicitud POST sin código de programa.

        Realiza una solicitud POST a la URL '/programas/' sin datos. Verifica que la respuesta tenga un código de estado 200
        y que no haya ningún programa seleccionado en el contexto.

        :return: None
        """
        response = self.client.post('/programas/')
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context['programa_seleccionado'])


if __name__ == '__main__':
    unittest.main()
