from django.db import models

# Create your models here.
class Periodo(models.Model):
    """Representa el periodo académico"""

    version = models.CharField(
        primary_key = True,
        default = "0000",
        max_length = 4,
        null = False
    )

    fecha_inicio = models.DateField(
        null = False
    )

    fecha_fin = models.DateField(
        null = True,
        blank = True
    )

    def __str__(self):
        return self.version

class Facultad(models.Model):
    """Representa una facultad de la Universidad"""

    nombre = models.CharField(
        max_length = 120,
        unique = True,
        blank = False
    )

    def __str__(self):
        return self.nombre
    
class TipoPrograma(models.Model):
    """Representa los tipos de programas de un Posgrado"""

    codigo = models.CharField(
        max_length = 1,
        primary_key = True
    )

    nombre = models.CharField(
        max_length = 120,
        unique = True,
        blank = False
    )

    def __str__(self):
        return self.nombre
    
class Departamento(models.Model):
    """Representa los departamentos académicos de la Universidad"""

    nombre = models.CharField(
        max_length = 120,
        unique = True,
        blank = False
    )

    def __str__(self):
        return self.nombre

class TipoContrato(models.Model):
    """Representa los tipos de contratos que pueden haber"""

    tipo = models.CharField(
        max_length = 120,
        unique = True
    )

    def __str__(self):
        return self.nombre

class EstadoContrato(models.Model):
    """Representa los posibles estados que puede tener un contrato"""

    nombre = models.CharField(
        max_length = 120,
        unique = True
    )

    def __str__(self):
        return self.nombre
    
class Modalidad(models.Model):
    """Representa las posibles modalidades que puede tener una clase"""

    codigo = models.CharField(
        max_length = 1,
        primary_key = True
    )

    nombre = models.CharField(
        max_length = 80,
        unique = True
    )

    def __str__(self):
        return self.nombre

class Cuidad(models.Model):
    """Representa las ciudades que pertenecen las personas"""

    nombre = models.CharField(
        max_length = 20,
        unique = True
    )

    def __str__(self):
        return self.nombre

class Materia(models.Model):
    """Representa las materias que se están en banner"""

    codigo = models.CharField(
        primary_key = True,
        max_length = 8
    )

    nombre = models.CharField(
        max_length = 120
    )

    creditos = models.IntegerField()

    departamento_codigo = models.ForeignKey(
        "Departamento", 
        on_delete = models.CASCADE,
        null = False
    )

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    """Representa los usuarios que pertenecen a la oficina del CCSA"""

    codigo = models.CharField(
        primary_key = True,
        max_length = 10
    )

    nombre = models.CharField(
        max_length = 120,
        blank = False
    )

    apellido = models.CharField(
        max_length = 120,
        blank = False
    )

    def __str__(self):
        return f"{self.codigo} | {self.apellido} {self.nombre}"

class Espacio(models.Model):

    id_espacio = models.CharField(
        primary_key = True,
        max_length = 4
    )

    id_subespacio = models.CharField(
        max_length = 2,
        null = True,
        blank = True,
    )

    tipo = models.CharField(
        max_length = 24,
        blank = False,
        default = "Salon"
    )

    capacidad = models.IntegerField(
        blank = True,
        null = False,
        default = 30
    )

    def __str__(self):
        if self.id_subespacio:
            return f"{self.id_espacio}-{self.id_subespacio}"
        else:
            return f"{self.id_espacio}"

class Persona(models.Model):
    """Modelo abstracto que representa las personas que se obtiene de people.net"""

    cedula = models.CharField(
        primary_key = True, 
        max_length = 32
    )
    
    nombre = models.CharField(
        max_length = 120
    )

    apellido = models.CharField(
        max_length = 120
    )

    email = models.EmailField(
        max_length = 120
    )

    telefono = models.CharField(
        max_length = 16,
        blank = False
    )

    cuidad_id =  models.ForeignKey(
        "Cuidad",
        on_delete=models.CASCADE,
        blank = False
    )

    contrato_codigo =  models.ForeignKey(
        "Contrato",
        on_delete=models.CASCADE,
        blank = True,
        null = False
    )

    def __str__(self):
        return f"{self.cedula} | {self.apellido} {self.nombre}"

    class Meta:
        abstract = True


class Director(Persona):
    """Representa a los directores de programa de posgrado"""
    cedula = models.CharField(
        primary_key = True, 
        max_length = 32
    )

class Docente(Persona):
    """Representa a los docentes obtenidos people.net"""
    cedula = models.CharField(
        primary_key = True, 
        max_length = 32
    )

class Curso(models.Model):
    """Representa un curso de una materia dictado por uno o mas docentes"""
    nrc = models.CharField(
        primary_key = True,
        max_length = 6
    )
    
    grupo = models.CharField(
        max_length = 2,
    )

    cupo = models.IntegerField()

    materia_codigo = models.ForeignKey(
        "Materia", 
        on_delete = models.CASCADE,
        null = False
    )

    usuario_codigo = models.ForeignKey(
        "Usuario", 
        on_delete = models.CASCADE,
        null = False
    )

    docente = models.ManyToManyField(
        "Docente"
    )

class Clase(models.Model):
    """Representa una instancia de clase (toda la información para buscarla)"""

    codigo = models.CharField(
        primary_key = True,
        max_length = 12
    )

    fecha = models.DateField(
        blank = False,
        null = False
    )

    hora_inicio = models.DateTimeField(
        blank = False,
        null = False
    )

    hora_fin = models.DateTimeField(
        blank = False,
        null = False
    )

    curso_nrc = models.ForeignKey(
        "Curso", 
        on_delete = models.CASCADE,
        blank = False
    )

    modalidad_codigo = models.ForeignKey(
        "Modalidad", 
        on_delete = models.CASCADE,
        blank = False
    )
    
    espacio_id_espacio = models.ForeignKey(
        "Espacio", 
        on_delete = models.CASCADE,
        blank = False
    )

class Pensum(models.Model):
    """Representa el pensum de un programa"""

    materia_codigo = models.ForeignKey(
        "Materia", 
        on_delete = models.CASCADE,
        null = False
    )

    programa_codigo = models.ForeignKey(
        "Programa", 
        on_delete = models.CASCADE,
        null = False
    )

    periodo_version = models.ForeignKey(
        "Periodo", 
        on_delete = models.CASCADE,
        null = False
    )

class Programa(models.Model):
    """Representa los programas de posgrado obtenidos por banner"""

    codigo = models.CharField(
        primary_key = True,
        max_length = 32
    )

    nombre = models.CharField(
        max_length = 120
    )

    tipoPrograma_codigo = models.ForeignKey(
        "TipoPrograma", 
        on_delete = models.CASCADE,
        null = False
    )

    facultad_id = models.ForeignKey(
        "Facultad", 
        on_delete = models.CASCADE,
        null = False
    )

    director_cedula = models.ForeignKey(
        "Director", 
        on_delete = models.CASCADE,
        null = False
    )

class Contrato(models.Model):
    """Representa los contratos almacenados de los docentes"""

    codigo = models.CharField(
        max_length = 8,
        primary_key = True
    )

    fecha_elaboracion = models.DateField()

    tipoContrato_id = models.ForeignKey(
        "TipoContrato", 
        on_delete=models.CASCADE
    )

    estadoContrato = models.ForeignKey(
        "EstadoContrato", 
        on_delete=models.CASCADE
    )

    docente_cedula = models.ForeignKey(
        "Docente", 
        on_delete=models.CASCADE
    )

