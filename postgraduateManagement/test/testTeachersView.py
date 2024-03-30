# Create your tests here.
import unittest
from django.test import TestCase
from django.urls import reverse
from postgraduateManagement.views.views_teacher import *
from postgraduateManagement.models import Docente


class TestViews(TestCase):
    def setUp(self):
        self.teacher1_test = Docente.objects.create(
            cedula='12-345-6789',
            nombre='Test1',
            apellido='Teacher',
            telefono='0987654321',
            url_foto='URL',
            cuidad_id=1,
            estado='activo',
        )

        self.teacher3_test = Docente.objects.create(
            cedula='23-456-4538',
            nombre='Test2',
            apellido='Teacher',
            telefono='0987654321',
            url_foto='URL',
            cuidad_id=4,
            estado='activo',
        )

        self.teacher3_test = Docente.objects.create(
            cedula='65-635-3627',
            nombre='Test3',
            apellido='Teacher',
            telefono='0987654321',
            url_foto='URL',
            cuidad_id=5,
            estado='inactivo',
        )
