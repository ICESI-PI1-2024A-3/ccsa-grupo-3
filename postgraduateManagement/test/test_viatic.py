# Create your tests here.
import unittest

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from postgraduateManagement.views.views_course import *
from postgraduateManagement.models import Departamento, Usuario, Periodo, Viatico, Docente, Ciudad


class TestViews(TestCase):

    def setUp(self):
        self.viatico = Viatico.objects.create(
            estado_viatico='pendiente',
            descripcion='Descripción de prueba',
            presupuesto=100,
            fecha_solicitud=timezone.now(),
            docente_id=1,  # ID de docente de prueba
            clase_id=1  # ID de clase de prueba
        )
        self.docente = Docente.objects.create(cedula='1', nombre='Pedro', apellido='González',
                                              email='pedro@example.com', telefono=987654321,
                                              ciudad=Ciudad.objects.create(id=2, nombre='Ejemplo2'))
        self.periodo = Periodo.objects.create(
            semestre='29', fecha_inicio='2024-01-01', fecha_fin='2024-05-31')
        self.materia = Materia.objects.create(codigo='MAT01', nombre='Materia de Ejemplo', creditos=3,
                                              departamento=Departamento.objects.create(codigo='DEP01',
                                                                                       nombre='Departamento de Ejemplo'))
        self.curso = Curso.objects.create(nrc='1', grupo='01', cupo=30, materia=self.materia,
                                          usuario=Usuario.objects.create(id=1, nombre='Usuario', apellido='Prueba'),
                                          periodo=self.periodo)

        self.user = User.objects.create_superuser(username='testuser', password='12345')
        self.client.force_login(self.user)

    def test_viatico_list_view(self):
        """
        Prueba la vista para mostrar una lista de viáticos.

        Realiza una solicitud GET a la URL de la lista de viáticos y verifica si el código de estado de la respuesta es 200
        (éxito) y si se está utilizando la plantilla correcta para renderizar la página.

        :return: None
        """
        response = self.client.get(reverse('viatic_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'postgraduateManagement/../viatic_list.html')

    def test_viatico_create_view(self):
        """
        Prueba la funcionalidad de creación de un nuevo viático.

        Realiza una solicitud POST a la URL de creación de viáticos con datos simulados y verifica si la redirección después
        de la creación es exitosa (código de estado 302).

        :return: None
        """
        response = self.client.post(reverse('crear_viatico'), {
            'estado_viatico': 'pendiente',
            'descripcion': 'Nueva descripción',
            'presupuesto': 200,
            'docente': 1,
            'clase': 1
        })
        self.assertEqual(response.status_code, 302)  # Redirección después de crear exitosamente

    def test_viatico_update_view(self):
        """
        Prueba la funcionalidad de actualización de un viático existente.

        Realiza una solicitud POST a la URL de actualización de viáticos con datos simulados y verifica si la redirección
        después de la actualización es exitosa (código de estado 302). Luego, actualiza el objeto viático desde la base de
        datos y verifica si los campos actualizados coinciden con los datos simulados.

        :return: None
        """
        response = self.client.post(reverse('actualizar_viatico', args=[self.viatico.pk]), {
            'estado_viatico': 'aprobado',
            'descripcion': 'Descripción actualizada',
            'presupuesto': 150
        })
        self.assertEqual(response.status_code, 302)  # Redirección después de actualizar exitosamente
        self.viatico.refresh_from_db()  # Actualizar el objeto desde la base de datos
        self.assertEqual(self.viatico.estado_viatico, 'aprobado')
        self.assertEqual(self.viatico.descripcion, 'Descripción actualizada')
        self.assertEqual(self.viatico.presupuesto, 150)

    def test_viatico_delete_view(self):
        """
        Prueba la funcionalidad de eliminación de un viático existente.

        Realiza una solicitud POST a la URL de eliminación de viáticos y verifica si la redirección después de la eliminación
        es exitosa (código de estado 302). Luego, verifica si el objeto viático se ha eliminado correctamente de la base de
        datos.

        :return: None
        """
        response = self.client.post(reverse('eliminar_viatico', args=[self.viatico.pk]))
        self.assertEqual(response.status_code, 302)  # Redirección después de eliminar exitosamente
        self.assertFalse(
            Viatico.objects.filter(pk=self.viatico.pk).exists())  # Verificar que el objeto se haya eliminado


if __name__ == '__main__':
    unittest.main()
