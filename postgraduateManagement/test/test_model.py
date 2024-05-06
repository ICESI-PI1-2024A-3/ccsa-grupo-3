import unittest

from django.db import IntegrityError
from django.test import TestCase
from postgraduateManagement.models import Facultad, TipoPrograma, Departamento, TipoContrato, Modalidad, EstadoContrato, \
    Usuario, Ciudad, Persona, Espacio, Docente, Director, Contrato, Programa, Materia, Periodo, DocentesCursos, Curso, \
    Pensum, Clase


class ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configurar datos de prueba una vez para toda la TestCase
        Facultad.objects.create(id=1, nombre='Facultad de Ingeniería')
        TipoPrograma.objects.create(nombre='Maestría')
        departamento = Departamento.objects.create(codigo='DEP001', nombre='Departamento de Matemáticas')
        TipoContrato.objects.create(codigo='TC001', tipo='Tiempo Completo')
        EstadoContrato.objects.create(id='A', nombre='Activo')
        modalidad = Modalidad.objects.create(codigo='P', nombre='Presencial')
        Ciudad.objects.create(id=1, nombre='Ciudad de Ejemplo')
        Usuario.objects.create(id=1, nombre='Juan', apellido='Pérez')
        ciudad = Ciudad.objects.create(id=2, nombre='Ciudad de')
        Director.objects.create(cedula='1234567890', nombre='Juan', apellido='Pérez', email='juan@example.com',
                                telefono=123456789, ciudad=ciudad)
        espacio = Espacio.objects.create(id_espacio='A001', tipo='Salon', capacidad=50)
        facultad = Facultad.objects.create(id=3, nombre='Facultad de Ejemplo')
        tipo_programa = TipoPrograma.objects.create(id=3, nombre='Tipo de Programa de Ejemplo')
        director = Director.objects.create(cedula='123456789', nombre='Juan', apellido='Pérez',
                                           email='juan@example.com', telefono=123456789,
                                           ciudad=Ciudad.objects.create(id=3, nombre='Ciudad'))
        programa = Programa.objects.create(codigo='PRG01', nombre='Programa de Ejemplo',
                                           descripcion='Descripción de Programa de Ejemplo', facultad=facultad,
                                           tipo_de_programa=tipo_programa, director=director)
        ciudad = Ciudad.objects.create(id=4, nombre='Ciuda de Ejemplo')
        Docente.objects.create(cedula='12345678', nombre='Juan', apellido='Pérez', email='juan@example.com',
                               telefono=123456789, ciudad=ciudad)
        tipo_contrato = TipoContrato.objects.create(codigo='TC01', tipo='Tipo de Contrato de Ejemplo')
        estado_contrato = EstadoContrato.objects.create(id='B', nombre='Activa')
        docente = Docente.objects.create(cedula='1234567890', nombre='Juan', apellido='Pérez', email='juan@example.com',
                                         telefono=123456789,
                                         ciudad=Ciudad.objects.create(id=6, nombre='Ciudad d Ejemplo'))
        Contrato.objects.create(fecha_elaboracion='2024-01-01', tipo_contrato=tipo_contrato,
                                estado_contrato=estado_contrato, docente=docente)
        periodo = Periodo.objects.create(semestre='2024A', fecha_inicio='2024-01-01', fecha_fin='2024-05-31')
        materia = Materia.objects.create(codigo='MAT01', nombre='Materia de Ejemplo', creditos=3,
                                         departamento=departamento)
        curso = Curso.objects.create(nrc='123456', grupo='01', cupo=30, materia=materia,
                                     usuario=Usuario.objects.create(id=3, nombre='Usuario', apellido='Prueba'),
                                     periodo=periodo)
        DocentesCursos.objects.create(docente=docente, curso=curso, prioridad=1)
        Clase.objects.create(curso=curso, modalidad=modalidad, espacio=espacio, espacio_asignado=espacio)
        Pensum.objects.create(programa=programa, materia=materia, periodo=periodo, semestre=1)

    def test_nombre_max_length_facultad(self):
        facultad = Facultad.objects.get(id=1)
        max_length = facultad._meta.get_field('nombre').max_length
        self.assertEqual(max_length, 255)

    def test_creacion_facultad_nombre_max_length(self):
        facultad = Facultad.objects.get(id=1)
        nombre = facultad.nombre
        self.assertEqual(nombre, 'Facultad de Ingeniería')

    def test_creacion_facultad_nombre_duplicado(self):
        with self.assertRaises(Exception):
            Facultad.objects.create(id=1, nombre='Facultad de Ingeniería')

    def test_nombre_max_length_tipo_de_programa(self):
        tipo_programa = TipoPrograma.objects.get(id=1)
        max_length = tipo_programa._meta.get_field('nombre').max_length
        self.assertEqual(max_length, 60)

    def test_creacion_tipo_programa_nombre_max_length(self):
        tipo_programa = TipoPrograma.objects.get(id=1)
        nombre = tipo_programa.nombre
        self.assertEqual(nombre, 'Maestría')

    def test_creacion_tipo_programa_nombre_duplicado(self):
        with self.assertRaises(Exception):
            TipoPrograma.objects.create(nombre='Maestría')

    def test_codigo_max_length_deparamento(self):
        departamento = Departamento.objects.get(codigo='DEP001')
        max_length = departamento._meta.get_field('codigo').max_length
        self.assertEqual(max_length, 10)

    def test_nombre_max_length_departamento(self):
        departamento = Departamento.objects.get(codigo='DEP001')
        max_length = departamento._meta.get_field('nombre').max_length
        self.assertEqual(max_length, 255)

    def test_creacion_departamento_nombre_max_length(self):
        departamento = Departamento.objects.get(codigo='DEP001')
        nombre = departamento.nombre
        self.assertEqual(nombre, 'Departamento de Matemáticas')

    def test_creacion_departamento_duplicado(self):
        with self.assertRaises(Exception):
            Facultad.objects.create(codigo="DEP001", nombre='Departamento de Ingeniería')

    def test_codigo_max_length_tipo_contrato(self):
        tipo_contrato = TipoContrato.objects.get(codigo='TC001')
        max_length = tipo_contrato._meta.get_field('codigo').max_length
        self.assertEqual(max_length, 16)

    def test_nombre_max_length_tipo_contrato(self):
        tipo_contrato = TipoContrato.objects.get(codigo='TC001')
        max_length = tipo_contrato._meta.get_field('tipo').max_length
        self.assertEqual(max_length, 80)

    def test_creacion_tipo_contrato_nombre_max_length(self):
        tipo_contrato = TipoContrato.objects.get(codigo='TC001')
        nombre = tipo_contrato.tipo
        self.assertEqual(nombre, 'Tiempo Completo')

    def test_creacion_tipo_contrato_duplicado(self):
        with self.assertRaises(Exception):
            Facultad.objects.create(codigo="TC001", nombre='Hora catedra')

    def test_id_max_length_estado_contrato(self):
        estado_contrato = EstadoContrato.objects.get(id='A')
        max_length = estado_contrato._meta.get_field('id').max_length
        self.assertEqual(max_length, 1)

    def test_nombre_max_length_estado_contrato(self):
        estado_contrato = EstadoContrato.objects.get(id='A')
        max_length = estado_contrato._meta.get_field('nombre').max_length
        self.assertEqual(max_length, 20)

    def test_creacion_estado_contrato_nombre_max_length(self):
        estado_contrato = EstadoContrato.objects.get(id='A')
        nombre = estado_contrato.nombre
        self.assertEqual(nombre, 'Activo')

    def test_creacion_estado_contrato_duplicado(self):
        with self.assertRaises(Exception):
            Facultad.objects.create(codigo="A", nombre='Activo')

    def test_codigo_max_length_modalidad(self):
        modalidad = Modalidad.objects.get(codigo='P')
        max_length = modalidad._meta.get_field('codigo').max_length
        self.assertEqual(max_length, 1)

    def test_nombre_max_length_modalidad(self):
        modalidad = Modalidad.objects.get(codigo='P')
        max_length = modalidad._meta.get_field('nombre').max_length
        self.assertEqual(max_length, 20)

    def test_creacion_modalidad_nombre_max_length(self):
        modalidad = Modalidad.objects.get(codigo='P')
        nombre = modalidad.nombre
        self.assertEqual(nombre, 'Presencial')

    def test_creacion_Modalidad_duplicado(self):
        with self.assertRaises(Exception):
            Facultad.objects.create(codigo="P", nombre='presencial')

    def test_nombre_max_length_ciudad(self):
        ciudad = Ciudad.objects.get(id=1)
        max_length = ciudad._meta.get_field('nombre').max_length
        self.assertEqual(max_length, 20)

    def test_creacion_ciudad_nombre_max_length(self):
        ciudad = Ciudad.objects.get(id=1)
        nombre = ciudad.nombre
        self.assertEqual(nombre, 'Ciudad de Ejemplo')

    def test_creacion_ciudad_duplicada(self):
        with self.assertRaises(Exception):
            Ciudad.objects.create(id=1, nombre='')

    def test_nombre_max_length_usuario(self):
        usuario = Usuario.objects.get(id=1)
        max_length = usuario._meta.get_field('nombre').max_length
        self.assertEqual(max_length, 120)

    def test_apellido_max_length_usuario(self):
        usuario = Usuario.objects.get(id=1)
        max_length = usuario._meta.get_field('apellido').max_length
        self.assertEqual(max_length, 120)

    def test_creacion_usuario_nombre_max_length(self):
        usuario = Usuario.objects.get(id=1)
        nombre = usuario.nombre
        self.assertEqual(nombre, 'Juan')

    def test_creacion_usuario_apellido_max_length(self):
        usuario = Usuario.objects.get(id=1)
        apellido = usuario.apellido
        self.assertEqual(apellido, 'Pérez')

    def test_creacion_usuario_duplicado(self):
        with self.assertRaises(Exception):
            Ciudad.objects.create(id=1, nombre='Juan', apellido="Perez")

    def test_id_espacio_max_length(self):
        espacio = Espacio.objects.get(id_espacio='A001')
        max_length = espacio._meta.get_field('id_espacio').max_length
        self.assertEqual(max_length, 4)

    def test_creacion_espacio_id_espacio_max_length(self):
        espacio = Espacio.objects.get(id_espacio='A001')
        id_espacio = espacio.id_espacio
        self.assertEqual(id_espacio, 'A001')

    def test_creacion_espacio_duplicado(self):
        with self.assertRaises(Exception):
            Espacio.objects.create(id_espacio='A001', tipo='Laboratorio', capacidad=30)

    def test_cedula_max_length_director(self):
        director = Director.objects.get(cedula='1234567890')
        max_length = director._meta.get_field('cedula').max_length
        self.assertEqual(max_length, 32)

    def test_nombre_max_length_director(self):
        director = Director.objects.get(cedula='1234567890')
        max_length = director._meta.get_field('nombre').max_length
        self.assertEqual(max_length, 120)

    def test_apellido_max_length_director(self):
        director = Director.objects.get(cedula='1234567890')
        max_length = director._meta.get_field('apellido').max_length
        self.assertEqual(max_length, 120)

    def test_email_max_length_director(self):
        director = Director.objects.get(cedula='1234567890')
        max_length = director._meta.get_field('email').max_length
        self.assertEqual(max_length, 120)

    def test_creacion_director_duplicado(self):
        with self.assertRaises(IntegrityError):
            ciudad = Ciudad.objects.create(id=2, nombre='Otra Ciudad de Ejemplo')
            Director.objects.create(cedula='1234567890', nombre='Pedro', apellido='González', email='pedro@example.com',
                                    telefono=987654321, ciudad=ciudad)

    def test_cedula_max_length_docente(self):
        docente = Docente.objects.get(cedula='12345678')
        max_length = docente._meta.get_field('cedula').max_length
        self.assertEqual(max_length, 32)

    def test_nombre_max_length_docente(self):
        docente = Docente.objects.get(cedula='12345678')
        max_length = docente._meta.get_field('nombre').max_length
        self.assertEqual(max_length, 120)

    def test_apellido_max_lengt_docenteh(self):
        docente = Docente.objects.get(cedula='12345678')
        max_length = docente._meta.get_field('apellido').max_length
        self.assertEqual(max_length, 120)

    def test_email_max_length_docente(self):
        docente = Docente.objects.get(cedula='12345678')
        max_length = docente._meta.get_field('email').max_length
        self.assertEqual(max_length, 120)

    def test_creacion_docente_duplicado(self):
        with self.assertRaises(IntegrityError):
            ciudad = Ciudad.objects.create(id=2, nombre='Otra Ciudad de Ejemplo')
            Docente.objects.create(cedula='12345678', nombre='Pedro', apellido='González', email='pedro@example.com',
                                   telefono=987654321, ciudad=ciudad)

    def test_codigo_max_length_programa(self):
        programa = Programa.objects.get(codigo='PRG01')
        max_length = programa._meta.get_field('codigo').max_length
        self.assertEqual(max_length, 10)

    def test_nombre_max_length_programa(self):
        programa = Programa.objects.get(codigo='PRG01')
        max_length = programa._meta.get_field('nombre').max_length
        self.assertEqual(max_length, 255)

    def test_creacion_programa_duplicado(self):
        with self.assertRaises(IntegrityError):
            facultad = Facultad.objects.create(id=2, nombre='Otra Facultad de Ejemplo')
            tipo_programa = TipoPrograma.objects.create(id=2, nombre='Otro Tipo de Programa de Ejemplo')
            director = Director.objects.create(cedula='0987654321', nombre='Pedro', apellido='González',
                                               email='pedro@example.com', telefono=987654321,
                                               ciudad=Ciudad.objects.create(id=2, nombre='Otra Ciudad de Ejemplo'))
            Programa.objects.create(codigo='PRG01', nombre='Otro Programa de Ejemplo',
                                    descripcion='Otra Descripción de Programa de Ejemplo', facultad=facultad,
                                    tipo_de_programa=tipo_programa, director=director)

    def test_fecha_elaboracion_not_null(self):
        contrato = Contrato.objects.get(fecha_elaboracion='2024-01-01')
        fecha_elaboracion = contrato.fecha_elaboracion
        self.assertIsNotNone(fecha_elaboracion)

    def test_creacion_contrato_duplicado(self):
        with self.assertRaises(IntegrityError):
            tipo_contrato = TipoContrato.objects.create(codigo='TC01', tipo='Otro Tipo de Contrato de Ejemplo')
            estado_contrato = EstadoContrato.objects.create(id='A', nombre='Inactivo')
            docente = Docente.objects.create(cedula='0987654321', nombre='Pedro', apellido='González',
                                             email='pedro@example.com', telefono=987654321,
                                             ciudad=Ciudad.objects.create(id=2, nombre='Otra Ciudad de Ejemplo'))
            Contrato.objects.create(fecha_elaboracion='2024-01-02', tipo_contrato=tipo_contrato,
                                    estado_contrato=estado_contrato, docente=docente)

    def test_semestre_max_length_periodo(self):
        periodo = Periodo.objects.get(semestre='2024A')
        max_length = periodo._meta.get_field('semestre').max_length
        self.assertEqual(max_length, 10)

    def test_creacion_periodo_duplicado(self):
        with self.assertRaises(IntegrityError):
            Periodo.objects.create(semestre='2024A', fecha_inicio='2024-01-01', fecha_fin='2024-05-31')

    def test_codigo_max_length_materia(self):
        materia = Materia.objects.get(codigo='MAT01')
        max_length = materia._meta.get_field('codigo').max_length
        self.assertEqual(max_length, 88)

    def test_nombre_max_length_materia(self):
        materia = Materia.objects.get(codigo='MAT01')
        max_length = materia._meta.get_field('nombre').max_length
        self.assertEqual(max_length, 120)

    def test_creacion_materia_duplicada(self):
        with self.assertRaises(IntegrityError):
            departamento = Departamento.objects.create(codigo='DEP02', nombre='Otro Departamento de Ejemplo')
            Materia.objects.create(codigo='MAT01', nombre='Otra Materia de Ejemplo', creditos=4,
                                   departamento=departamento)

    def test_nrc_max_length_curso(self):
        curso = Curso.objects.get(nrc='123456')
        max_length = curso._meta.get_field('nrc').max_length
        self.assertEqual(max_length, 6)

    def test_grupo_max_length_curso(self):
        curso = Curso.objects.get(nrc='123456')
        max_length = curso._meta.get_field('grupo').max_length
        self.assertEqual(max_length, 2)

    def test_creacion_curso_duplicado(self):
        with self.assertRaises(IntegrityError):
            periodo = Periodo.objects.create(semestre='2024B', fecha_inicio='2024-06-01', fecha_fin='2024-12-31')
            materia = Materia.objects.create(codigo='MAT02', nombre='Otra Materia de Ejemplo', creditos=4,
                                             departamento=Departamento.objects.create(codigo='DEP02',
                                                                                      nombre='EJEMPLO'))
            Curso.objects.create(nrc='123456', grupo='01', cupo=30, materia=materia,
                                 usuario=Usuario.objects.create(id=2, nombre='Otro Usuario', apellido='Prueba'),
                                 periodo=periodo)

    def test_creacion_relacion_docente_curso_duplicada(self):
        with self.assertRaises(IntegrityError):
            docente = Docente.objects.create(cedula='1234567890', nombre='Pedro', apellido='González',
                                             email='pedro@example.com', telefono=987654321,
                                             ciudad=Ciudad.objects.create(id=2, nombre='Otra Ciudad de Ejemplo'))
            curso = Curso.objects.create(nrc='123456', grupo='02', cupo=20, materia=Materia.objects.create(
                codigo='MAT02', nombre='Otra Materia de Ejemplo', creditos=4,
                departamento=Departamento.objects.create(codigo='DEP02', nombre='Otro Departamento de Ejemplo')),
                                         usuario=Usuario.objects.create(id=2, nombre='Otro Usuario', apellido='Prueba'),
                                         periodo=Periodo.objects.create
                                         (semestre='2024B', fecha_inicio='2024-06-01', fecha_fin='2024-12-31'))
            DocentesCursos.objects.create(docente=docente, curso=curso, prioridad=1)

    def test_creacion_clase_exitosa(self):
        clase = Clase.objects.get(pk=1)
        self.assertEqual(clase.curso.nrc, '123456')
        self.assertEqual(clase.modalidad.nombre, 'Presencial')
        self.assertEqual(clase.espacio.id_espacio, 'A001')
        self.assertEqual(clase.espacio_asignado.id_espacio, 'A001')

    def test_creacion_clase_duplicada(self):
        with self.assertRaises(IntegrityError):
            programa = Programa.objects.create(codigo='PRG02', nombre='Otro Programa de Ejemplo',
                                               descripcion='Otra Descripción de Programa de Ejemplo',
                                               facultad=Facultad.objects.create(id=2,
                                                                                nombre='Otra Facultad de Ejemplo'),
                                               tipo_de_programa=TipoPrograma.objects.create(id=2,
                                                                                            nombre='Ejemplo'),
                                               director=Director.objects.create(cedula='0987654321', nombre='Pedro',
                                                                                apellido='González',
                                                                                email='pedro@example.com',
                                                                                telefono=987654321,
                                                                                ciudad=Ciudad.objects.create(id=2,
                                                                                                             nombre='EJ'
                                                                                                             )))
            periodo = Periodo.objects.create(semestre='2024B', fecha_inicio='2024-06-01', fecha_fin='2024-12-31')
            materia = Materia.objects.create(codigo='MAT02', nombre='Otra Materia de Ejemplo', creditos=4,
                                             departamento=Departamento.objects.create(codigo='DEP02',
                                                                                      nombre='EJemplo'))
            curso = Curso.objects.create(nrc='654321', grupo='02', cupo=20, materia=materia,
                                         usuario=Usuario.objects.create(id=2, nombre='Otro Usuario', apellido='Prueba'),
                                         periodo=periodo)
            espacio = Espacio.objects.create(id_espacio='A102', tipo='Salon', capacidad=40)
            modalidad = Modalidad.objects.create(codigo='V', nombre='Virtual')
            Clase.objects.create(curso=curso, modalidad=modalidad, espacio=espacio, espacio_asignado=espacio)

    def test_creacion_pensum_exitosa(self):
        pensum = Pensum.objects.get(pk=1)
        self.assertEqual(pensum.programa.codigo, 'PRG01')
        self.assertEqual(pensum.materia.codigo, 'MAT01')
        self.assertEqual(pensum.semestre, 1)

    def test_creacion_pensum_duplicada(self):
        with self.assertRaises(IntegrityError):
            programa = Programa.objects.create(codigo='PRG01', nombre='Otro Programa de Ejemplo',
                                               descripcion='Otra Descripción de Programa de Ejemplo',
                                               facultad=Facultad.objects.create(id=2,
                                                                                nombre='Otra Facultad de Ejemplo'),
                                               tipo_de_programa=TipoPrograma.objects.create(
                                                   id=2, nombre='Otro Tipo de Programa'),
                                               director=Director.objects.create(cedula='0987654321', nombre='Pedro',
                                                                                apellido='González',
                                                                                email='pedro@example.com',
                                                                                telefono=987654321,
                                                                                ciudad=Ciudad.objects.create(
                                                                                    id=2, nombre='Ciudad')))
            periodo = Periodo.objects.create(semestre='2024B', fecha_inicio='2024-06-01', fecha_fin='2024-12-31')
            materia = Materia.objects.create(codigo='MAT02', nombre='Otra Materia de Ejemplo', creditos=4,
                                             departamento=Departamento.objects.create(codigo='DEP02',
                                                                                      nombre='Ejemplo'))
            Pensum.objects.create(programa=programa, materia=materia, periodo=periodo, semestre=1)
