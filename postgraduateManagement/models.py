from django.db import models


class Facultad(models.Model):
    """
    Modelo para representar las facultades.

    Atributos:
        id (IntegerField): Identificador único de la facultad.
        nombre (CharField): Nombre descriptivo de la facultad.
    """

    id = models.AutoField(
        primary_key=True
    )

    nombre = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return self.nombre


class TipoPrograma(models.Model):
    """
    Modelo para representar los tipos de programa de posgrado.

    Atributos:
        id (IntegerField): Identificador único del tipo de programa.
        nombre (CharField): Nombre descriptivo del tipo de programa.
    """

    id = models.AutoField(
        primary_key=True
    )

    nombre = models.CharField(
        max_length=60,
        unique=True
    )

    def __str__(self):
        return self.nombre


class Departamento(models.Model):
    """
    Modelo para representar los departamentos académicos de la Universidad.

    Atributos:
        código (CharField): código único del departamento.
        nombre (CharField): nombre único del departamento. 
    """

    codigo = models.CharField(
        primary_key=True,
        max_length=10
    )

    nombre = models.CharField(
        max_length=255,
        unique=True
    )

    def __str__(self):
        return self.nombre


class TipoContrato(models.Model):
    """
    Modelo para representar los tipos de contratos que pueden haber.

    Atributos:
        código (CharField) = Código único de los tipos de contrato.
        tipo (CharField) = Nombre descriptivo del tipo de contrato.
    """

    codigo = models.CharField(
        primary_key=True,
        max_length=16
    )

    tipo = models.CharField(
        max_length=80,
        unique=True
    )

    def __str__(self):
        return self.tipo


class EstadoContrato(models.Model):
    """
    Modelo para representar los posibles estados que puede tener un contrato.

    Atributos:
        id (ChardField) = Identificador único del estado de un contrato.
        nombre (ChardField) = Nombre descriptivo de un estado del contrato.

    """

    id = models.CharField(
        primary_key=True,
        max_length=1
    )

    nombre = models.CharField(
        max_length=20,
        unique=True
    )

    def __str__(self):
        return self.nombre


class Modalidad(models.Model):
    """
    Modelo para representar las posibles modalidades que puede tener una clase

    Atributos:
        código (CharField) = Código único de las modalidades.
        nombre (CharField) = Nombre descriptivo de una modalidad.
    """
    codigo = models.CharField(
        max_length=1,
        primary_key=True
    )

    nombre = models.CharField(
        max_length=20,
        unique=True
    )

    def __str__(self):
        return self.nombre


class Ciudad(models.Model):
    """
    Modelo que representa las ciudades

    Atributos:
        id (IntegerField) = Identificador único de la ciudad.
        nombre (CharField) = Nombre descriptivo de la ciudad.
    """

    id = models.IntegerField(
        primary_key=True
    )

    nombre = models.CharField(
        max_length=20,
        unique=True
    )

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    """
    Modelo que representa los usuarios de la oficina del CCSA

    Atributos:
        id (IntegerField) = Identificador único que da la universidad a sus trabajadores.
        nombre (CharField) = Nombre del usuario.
        apellido (CharField) = Apellido del usuario.
    """
    id = models.IntegerField(
        primary_key=True
    )

    nombre = models.CharField(
        max_length=120
    )

    apellido = models.CharField(
        max_length=120
    )

    def __str__(self):
        return f"{self.id} | {self.apellido} {self.nombre}"


class Espacio(models.Model):
    """
    Modelo que representa los espacios de la universidad

    Atributos:
        id_espacio (CharField) = Identificador único del espacio.
        id_subespacio (CharField) = Identificador único del subespacio (en caso de que exista).
        tipo (CharField) = Tipo de espacio (Salón, laboratorio, etc).
        capacidad (IntegerField) = Capacidad del espacio.
    """

    id_espacio = models.CharField(
        primary_key=True,
        max_length=4
    )

    id_subespacio = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        default='00'
    )

    tipo = models.CharField(
        max_length=24,
        default="Salon"
    )

    capacidad = models.IntegerField(
        blank=True,
        default=0
    )

    def __str__(self):
        if self.id_subespacio:
            return f"{self.id_espacio}-{self.id_subespacio}"
        else:
            return f"{self.id_espacio}"


class Persona(models.Model):
    """
    Modelo abstracto que representa las personas que pueden ser docentes o directores. 

    Atributos:
        cédula (CharField) = Cédula de la persona.
        nombre (CharField) = Nombre de la persona.
        apellido (CharField) = Apellido de la persona.
        email (EmailField) = Correo electrónico de la persona.
        teléfono (IntegerField) = Número de teléfono de la persona.
        url_foto (URLField) = Dirección web de la foto de la persona.
    """

    cedula = models.CharField(
        primary_key=True,
        max_length=32
    )

    nombre = models.CharField(
        max_length=120
    )

    apellido = models.CharField(
        max_length=120
    )

    email = models.EmailField(
        max_length=120
    )

    telefono = models.CharField(
        max_length=16
    )

    url_foto = models.URLField()

    ciudad = models.ForeignKey(
        Ciudad,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.cedula} | {self.apellido} {self.nombre}"

    class Meta:
        abstract = True


class Director(Persona):
    """
    Representa a los directores de programa de posgrado
    """
    pass


class Docente(Persona):
    """
    Representa a los docentes obtenidos people.net
    """

    STATUS_CHOICES = (
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo')
    )

    estado = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default='activo'
    )


class Programa(models.Model):
    """
    Modelo para representar los programas académicos.

    Atributos:
        código (CharField): Código único del programa.
        nombre (CharField): Nombre descriptivo del programa.
        descripción (TextField): Descripción del programa.
        facultad (ForeignKey): Facultad a la que pertenece el programa.
        tipo_de_programa (ForeignKey): Tipo de programa.
        director (ForeignKey): Director del programa.
    """

    codigo = models.CharField(
        primary_key=True,
        max_length=10
    )

    nombre = models.CharField(
        max_length=255

    )

    descripcion = models.TextField()

    url_image = models.URLField()

    facultad = models.ForeignKey(
        'Facultad', on_delete=models.CASCADE
    )

    tipo_de_programa = models.ForeignKey(
        'TipoPrograma', on_delete=models.CASCADE
    )

    director = models.ForeignKey(
        'Director',
        on_delete=models.CASCADE
    )


class Contrato(models.Model):
    """
    Modelo que representa los contratos almacenados de los docentes

    codigo (AutoField) = Código único del contrato.
    fecha_elaboración (DateField) = Fecha de elaboración del contrato.
    tipo_contrato (ForeignKey) = Tipo de contrato.
    estado_contrato (ForeignKey) = Estado del contrato.
    docente (ForeignKey) = Docente al que pertenece el contrato.
    """

    codigo = models.AutoField(
        primary_key=True
    )

    fecha_elaboracion = models.DateField()

    tipo_contrato = models.ForeignKey(
        "TipoContrato",
        on_delete=models.CASCADE
    )

    estado_contrato = models.ForeignKey(
        "EstadoContrato",
        on_delete=models.CASCADE
    )

    docente = models.ForeignKey(
        "Docente",
        on_delete=models.CASCADE
    )


class Periodo(models.Model):
    """
    Modelo para representar los periodos académicos.

    Atributos:
        id (IntegerField): Identificador único del periodo.
        semestre (CharField): Periodo académico.
        fecha_inicio (DateField): Fecha de inicio del periodo.
        fecha_fin (DateField): Fecha de fin del periodo.
    """

    id = models.AutoField(
        primary_key=True,
        default=1
    )

    semestre = models.CharField(
        max_length=2
    )

    fecha_inicio = models.DateField()

    fecha_fin = models.DateField()

    def __str__(self):
        return self.semestre


class Materia(models.Model):
    """
    Representa las materias que se imparten en la universidad

    Atributos:
        código (CharField) = Código único de la materia.
        nombre (CharField) = Nombre descriptivo de la materia.
        créditos (IntegerField) = Número de créditos que cuesta la materia.
        departamento (ForeignKey) = Código del departamento al que pertenece la materia.
        programas (ManyToManyField) = Programas asociados a la materia a través de la malla curricular.
    """

    codigo = models.CharField(
        primary_key=True,
        max_length=88
    )

    nombre = models.CharField(
        max_length=120
    )

    creditos = models.IntegerField()

    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.CASCADE,
    )

    programas = models.ManyToManyField(
        Programa,
        through='Pensum'
    )

    docente = models.ManyToManyField(
        'Docente'
    )

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    """
    Representa un curso de una materia dictado por uno o mas docentes

    Atributos:
        nrc (CharField) = Número de registro del curso.
        grupo (CharField) = Grupo al que pertenece el curso.
        cupo (IntegerField) = Cantidad de maxima del curso.
        materia (ForeignKey) = Materia a la que pertenece el curso.
        usuario (ForeignKey) = Usuario que crea el curso.
        periodo (ForeignKey) = Periodo académico al que pertenece el curso.
        docente (ManyToManyField) = Docentes que pueden impartir el curso.

    """
    nrc = models.CharField(
        primary_key=True,
        max_length=6
    )

    grupo = models.CharField(
        max_length=2,
    )

    cupo = models.IntegerField()

    materia = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE,
    )

    usuario = models.ForeignKey(
        Usuario,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    periodo = models.ForeignKey(
        Periodo,
        on_delete=models.CASCADE
    )

    docente = models.ForeignKey(
        Docente,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('grupo', 'materia', 'docente')

    def __str__(self):
        return f"{self.materia.nombre} - {self.grupo}"

class Clase(models.Model):
    """
    Modelo que representa una clase de un curso.

    Atributos:
        id (AutoField) = Identificador único de la clase.
        fecha_inicio (DateTimeField) = Fecha y hora de inicio de la clase.
        fecha_fin (DateTimeField) = Fecha y hora de fin de la clase.
        curso (ForeignKey) = Curso al que pertenece la clase.
        modalidad (ForeignKey) = Modalidad de enseñanza de la clase.
        espacio (ForeignKey) = Espacio físico de la clase.
        espacio_asignado (ForeignKey) = Espacio físico asignado para la clase.
    """

    id = models.AutoField(
        primary_key=True
    )

    fecha_inicio = models.DateTimeField(
        null=True
    )

    fecha_fin = models.DateTimeField(
        null=True
    )

    curso = models.ForeignKey(
        'Curso',
        on_delete=models.CASCADE,

    )

    curso = models.ForeignKey(
        'Curso',
        on_delete=models.CASCADE,

    )

    modalidad = models.ForeignKey(
        'Modalidad',
        on_delete=models.CASCADE,

    )

    espacio = models.ForeignKey(
        'Espacio',
        on_delete=models.CASCADE,
        related_name='espacio'
    )

    espacio_asignado = models.ForeignKey(
        'Espacio',
        on_delete=models.CASCADE,
        related_name='espacio_asignado'
    )


class Pensum(models.Model):
    """
    Modelo que representa el pensum de un programa de posgrado
    Atributos:
        programa (ForeignKey) = Programa al que pertenece la materia.
        materia (ForeignKey) = Materia que se imparte en el programa.
        periodo (ForeignKey) = Periodo académico al que pertenece el pensum.
    """

    programa = models.ForeignKey(
        'Programa',
        on_delete=models.CASCADE,
    )

    materia = models.ForeignKey(
        'Materia',
        on_delete=models.CASCADE,
    )

    periodo = models.ForeignKey(
        Periodo,
        on_delete=models.CASCADE,
    )


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["materia", "programa"],
                name="unique_materia_programa",
            )
        ]

    def __str__(self):
        return f"{self.programa.nombre} - {self.materia.nombre} - {self.semestre}"


class Viatico(models.Model):
    """
    Modelo que representa las solicitudes de viáticos para los maestros.

    Atributos:
        codigo(AutoField): representa el idenficador unico del viatico
        estado_viatico (CharField): representa el estado del viatico
        descripcion(TextField): representa la descripcion del tipo del viatico
        fecha_solicitud(DateField): representa la fecha en la que el viatico fue solicitado
        presupuesto (IntegerField): Presupuesto asignado para los viáticos.
        docente (ForeignKey): Docente al que se le asignarán los viáticos.
        clase(ForeignKey): Clase a la que se le asigna el viatico
    """
    codigo = models.AutoField(
        primary_key=True
    )

    STATUS_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
        ('finalizado', 'Finalizado')
    )

    estado_viatico = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='Pendiente'
    )

    descripcion = models.TextField()

    fecha_solicitud = models.DateField(
        auto_now_add=True
    )
    presupuesto = models.IntegerField()

    docente = models.ForeignKey(
        Docente,
        on_delete=models.CASCADE
    )

    clase = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.clase.materia,self.clase.nrc} - {self.docente.cedula}"