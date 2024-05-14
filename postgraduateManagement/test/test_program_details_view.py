from datetime import date

from django.contrib.auth.models import User
from postgraduateManagement.models import Programa, Periodo, Director, Ciudad, Facultad, TipoPrograma, Pensum, Materia, \
    Docente, Departamento
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            username='testuser', password='12345')
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
        self.docente1 = Docente.objects.create(
            cedula='987654321',
            nombre='Maria',
            apellido='Gomez',
            email='maria.gomez@example.com',
            telefono='0987654321',
            ciudad=self.ciudad
        )
        self.periodo1 = Periodo.objects.create(
            id=1,
            semestre='1',
            fecha_inicio=date(2022, 1, 1),
            fecha_fin=date(2022, 6, 30)
        )
        self.periodo2 = Periodo.objects.create(
            id=2,
            semestre='2',
            fecha_inicio=date(2022, 7, 1),
            fecha_fin=date(2022, 12, 31)
        )

        self.departamento = Departamento.objects.create(nombre='Departamento 1')
        self.materia1 = Materia.objects.create(codigo='MAT1', nombre='Materia 1', creditos=3,
                                               departamento=self.departamento)
        self.materia1.docente.add(self.docente1)
        self.materia2 = Materia.objects.create(codigo='MAT2', nombre='Materia 2', creditos=3,
                                               departamento=self.departamento)
        self.materia2.docente.add(self.docente1)

        self.pensum1 = Pensum.objects.create(programa=self.programa, materia=self.materia1, periodo=self.periodo1)
        self.pensum2 = Pensum.objects.create(programa=self.programa, materia=self.materia2, periodo=self.periodo2)

    def test_view_program_summary(self):
        """
        Prueba la vista de resumen de un programa.

        Realiza una solicitud GET a la URL para ver el resumen de un programa específico. Verifica que la respuesta tenga un
        código de estado 200 y que se utilice la plantilla 'program_details_summary.html'.

        :return: None
        """
        response = self.client.get(reverse('program_summary', args=[self.programa.codigo]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'program_details_summary.html')

    def test_view_program_planning(self):
        """
        Prueba la vista de planificación de un programa.

        Realiza una solicitud GET a la URL para ver la planificación de un programa específico. Verifica que la respuesta
        tenga un código de estado 200 y que se utilice la plantilla 'program_details_planning.html'.

        :return: None
        """
        response = self.client.get(reverse('program_planning', args=[self.programa.codigo]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'program_details_planning.html')

    def test_view_program_teachers(self):
        """
        Prueba la vista de docentes de un programa.

        Realiza una solicitud GET a la URL para ver los docentes de un programa específico. Verifica que la respuesta tenga
        un código de estado 200 y que se utilice la plantilla 'program_details_teachers.html'.

        :return: None
        """
        response = self.client.get(reverse('program_teachers', args=[self.programa.codigo]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'program_details_teachers.html')

    def test_view_program_subjects(self):
        """
        Prueba la vista de materias de un programa.

        Realiza una solicitud GET a la URL para ver las materias de un programa específico. Verifica que la respuesta tenga
        un código de estado 200 y que se utilice la plantilla 'program_details_subjects.html'.

        :return: None
        """
        response = self.client.get(reverse('program_subjects', args=[self.programa.codigo]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'program_details_subjects.html')

    def test_view_program_teachers_with_filters(self):
        """
        Prueba la vista de docentes de un programa con filtros.

        Realiza una solicitud GET a la URL para ver los docentes de un programa específico con filtros. Verifica que la
        respuesta tenga un código de estado 200, que se utilice la plantilla 'program_details_teachers.html' y que la lista
        de docentes esté vacía.

        :return: None
        """
        expected_number_of_teachers = 0
        response = self.client.get(reverse('program_teachers', args=[self.programa.codigo]), {
            'search_contains': 'search_term',
            'status': 'status_value',
            'city': 'city_value',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'program_details_teachers.html')
        self.assertEqual(len(response.context['teacher_list']), expected_number_of_teachers)

    def test_view_program_subjects_with_subjects(self):
        """
        Prueba la vista de materias de un programa con materias existentes.

        Realiza una solicitud GET a la URL para ver las materias de un programa específico. Verifica que la respuesta tenga
        un código de estado 200, que se utilice la plantilla 'program_details_subjects.html' y que la cantidad de materias
        en el contexto sea igual a 2.

        :return: None
        """
        expected_number_of_subjects = 2
        response = self.client.get(reverse('program_subjects', args=[self.programa.codigo]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'program_details_subjects.html')
        self.assertEqual(len(response.context['subjects']), expected_number_of_subjects)
