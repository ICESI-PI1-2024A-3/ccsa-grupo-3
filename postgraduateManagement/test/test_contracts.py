from datetime import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from postgraduateManagement.models import Contrato, Docente, TipoContrato, Ciudad, EstadoContrato


class ViewContractTestCase(TestCase):
    def setUp(self):
        date_str = "12/03/21"
        fecha_elaboracion = datetime.strptime(date_str, "%d/%m/%y").strftime("%Y-%m-%d")
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.ciudad = Ciudad.objects.create(id=1, nombre='San Francisco')
        self.estadoContrato = EstadoContrato.objects.create(id=1, nombre='activo')
        self.tipoContrato = TipoContrato.objects.create(codigo=1, tipo='San Francisco')
        self.docente = Docente.objects.create(nombre="Juan", cedula=1234567890, ciudad_id=self.ciudad.id,
                                              telefono="1234567890", apellido="Perez", email="juanle.com")
        self.contrato = Contrato.objects.create(codigo=self.docente.cedula, docente_id=self.docente.cedula,
                                                fecha_elaboracion=fecha_elaboracion,
                                                estado_contrato_id=self.estadoContrato.id,
                                                tipo_contrato_id=self.tipoContrato.codigo)

    def test_view_contract(self):
        """
        Prueba la visualización de contratos.

        Realiza una solicitud GET a la URL para ver los contratos. Verifica que la respuesta tenga un código de estado 302,
        lo que indica una redirección, posiblemente a la página de inicio de sesión.

        :return: None
        """
        response = self.client.get(reverse('ver_contratos'))
        self.assertEqual(response.status_code, 302)

    def test_view_contract2(self):
        """
        Prueba adicional para la visualización de contratos.

        Realiza dos solicitudes GET consecutivas a la URL para ver los contratos. La primera solicitud debería redirigir
        (código 302), y la segunda solicitud sigue esa redirección.

        :return: None
        """
        response = self.client.get(reverse('ver_contratos'))
        response = self.client.get(response.url)

    def test_edit_contract3(self):
        """
        Prueba la edición de un contrato.

        Realiza una solicitud GET a la URL para editar un contrato específico. Verifica que la respuesta tenga un código de
        estado 302, lo que indica una redirección, posiblemente a la página de inicio de sesión.

        :return: None
        """
        response = self.client.get(reverse('editar_contratos', kwargs={'codigo': self.contrato.codigo}))
        self.assertEqual(response.status_code, 302)

    def test_edit_contract4(self):
        """
        Otra prueba para la edición de un contrato.

        Realiza una solicitud GET a la URL para editar un contrato específico. Verifica que la respuesta tenga un código de
        estado 302, lo que indica una redirección, posiblemente a la página de inicio de sesión.

        :return: None
        """
        response = self.client.get(reverse('editar_contratos', kwargs={'codigo': self.contrato.codigo}))
        self.assertEqual(response.status_code, 302)

    def test_editing_contract_redirect(self):
        """
        Prueba la redirección después de editar un contrato.

        Inicia sesión como un usuario, realiza una solicitud POST para editar un contrato y verifica que la respuesta tenga
        un código de estado 302 y que redirija a la página '/viewContract'.

        :return: None
        """
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('edicion_contratos'), {
            'txtCodigo': self.contrato.codigo,
            'fecha_elaboracion': '2024-05-12',
            'tipo_contrato': self.tipoContrato.codigo,
            'estado_contrato': self.estadoContrato.id,
            'docente': self.docente.cedula
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/viewContract')

    def test_edit_contract6(self):
        """
        Prueba la edición de un contrato con un código no válido.

        Realiza una solicitud GET a la URL para editar un contrato con un código no válido. Verifica que la respuesta tenga
        un código de estado 302 y que redirija a la página de inicio de sesión.

        :return: None
        """
        response = self.client.get(reverse('editar_contratos', kwargs={'codigo': "gfh"}))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)