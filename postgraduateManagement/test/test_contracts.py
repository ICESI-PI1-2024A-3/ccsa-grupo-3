from datetime import datetime
from multiprocessing.connection import Client

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from postgraduateManagement.models import Contrato, Docente,TipoContrato, Ciudad, EstadoContrato

class ViewContractTestCase(TestCase):
    def setUp(self):
        date_str = "12/03/21"
        fecha_elaboracion = datetime.strptime(date_str, "%d/%m/%y").strftime("%Y-%m-%d")
        self.user = User.objects.create_user(username='testuser', password='12345')

        self.ciudad = Ciudad.objects.create(id=1, nombre='San Francisco')
        self.estadoContrato = EstadoContrato.objects.create(id=1, nombre='activo')
        self.tipoContrato = TipoContrato.objects.create(codigo=1, tipo='San Francisco')
        self.docente = Docente.objects.create(nombre="Juan",cedula= 1234567890,ciudad_id=self.ciudad.id,telefono="1234567890", apellido="Perez", email="juanle.com")
        self.contrato = Contrato.objects.create(codigo=self.docente.cedula, docente_id=self.docente.cedula,fecha_elaboracion=fecha_elaboracion, estado_contrato_id=self.estadoContrato.id, tipo_contrato_id=self.tipoContrato.codigo)

    def test_view_contract(self):

        response = self.client.get(reverse('ver_contratos'))
        self.assertEqual(response.status_code, 302)

    def test_view_contract2(self):
        response = self.client.get(reverse('ver_contratos'))
        response = self.client.get(response.url)

    def test_edit_contract3(self):
        response = self.client.get(reverse('editar_contratos', kwargs={'codigo': self.contrato.codigo}))
        self.assertEqual(response.status_code, 302)

    def test_edit_contract4(self):
        response = self.client.get(reverse('editar_contratos', kwargs={'codigo': self.contrato.codigo}))
        self.assertEqual(response.status_code, 302)

    def test_editing_contract_redirect(self):
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
        response = self.client.get(reverse('editar_contratos', kwargs={'codigo': "gfh"}))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)




    