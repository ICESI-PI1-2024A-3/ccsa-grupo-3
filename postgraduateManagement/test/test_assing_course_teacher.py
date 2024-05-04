from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from postgraduateManagement.models import Docente, Materia, DocentesCursos, Ciudad, Departamento,Curso, Periodo, Usuario


class AssingCourseForTeacherViewTest(TestCase):
    def setUp(self):

        self.ciudad = Ciudad.objects.create(
            id=1,
            nombre='San Francisco'
        )

        self.docente_activo = Docente.objects.create(
            nombre="Juan",
            cedula=1234567890,
            ciudad_id=self.ciudad.id,
            telefono="1234567890",
            apellido="Perez",
            email="juanle.com",
            estado="activo"
        )


        self.departamento_prueba = Departamento.objects.create(
            codigo="DEP001",
            nombre="Departamento de Prueba"
        )

        self.usuario_prueba = Usuario.objects.create(
            id=1,
            nombre="Nombre de Prueba",
            apellido="Apellido de Prueba",
        )

        self.user = User.objects.create_superuser(username='testuser', password='12345')
        self.client.force_login(self.user)

        self.periodo_prueba = Periodo.objects.create(
            semestre="2023-01",
            fecha_inicio="2023-01-01",
            fecha_fin="2023-05-31"
        )

        self.materia_prueba = Materia.objects.create(
            codigo="MAT001",
            nombre="Materia de Prueba",
            creditos=3,
            departamento=self.departamento_prueba
        )

        self.curso = Curso.objects.create(
            nrc="12345",
            grupo="Grupo de Prueba",
            cupo=30,
            materia=self.materia_prueba,
            usuario=self.usuario_prueba,
            periodo=self.periodo_prueba
        )

        self.curso_disponible = DocentesCursos.objects.create(
            curso_id=self.curso.nrc,
            docente_id=self.docente_activo.cedula,
            prioridad=1
        )


    def test_assign_course_to_active_teacher(self):
        url = reverse('assing_course_for_teacher', kwargs={'cedula_docente': self.docente_activo.cedula,
                                                           'codigo_materia': self.materia_prueba.codigo, 'nrc_curso': self.curso.nrc})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)


    def test_no_courses_available_for_subject(self):
        materia_sin_cursos = Materia.objects.create(codigo='MAT002', creditos=2, departamento=self.departamento_prueba)
        url = reverse('assing_course_for_teacher', kwargs={'cedula_docente': self.docente_activo.cedula,
                                                           'codigo_materia': materia_sin_cursos.codigo,'nrc_curso': self.curso.nrc})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)



