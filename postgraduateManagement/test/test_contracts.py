from datetime import datetime
from multiprocessing.connection import Client

from django.test import TestCase
from django.urls import reverse
from postgraduateManagement.models import Contrato, Docente,TipoContrato, Ciudad, EstadoContrato

class ViewContractTestCase(TestCase):
    def setUp(self):
        date_str = "12/03/21"
        fecha_elaboracion = datetime.strptime(date_str, "%d/%m/%y").strftime("%Y-%m-%d")

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



    