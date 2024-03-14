from django.db import models
from postgraduateManagement.models import Programa, Usuario, Docente, Espacio
# Create your models here.
class EstadoSolicitud(models.Model):
    """Representa los posibles estados que puede tener una solicitud"""

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

class TipoContable(models.Model):
    """Representa los posibles tipos que puede haber de una solicitud contable"""

    id = models.CharField(
        max_length = 1,
        primary_key = True
    )

    tipo = models.CharField(
        max_length = 32,
        unique = True
    )

    def __str__(self):
        return self.tipo

class Solicitud(models.Model):
    """Modelo abstracto para representar las solicitudes"""

    codigo = models.CharField(
        max_length = 8,
        primary_key = True
    )

    descripcion = models.TextField(
        blank = False
    )

    fecha_solicitud = models.DateField(
        auto_now_add = True
    )

    usuario_codigo = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        blank = False
    )

    estadoSolicitud_codigo = models.ForeignKey(
        "EstadoSolicitud",
        on_delete=models.CASCADE,
        blank = False
    )

    programa = models.ManyToManyField(
        Programa
    )

    def __str__(self):
        return self.codigo
    
    class Meta:
        abstract = True

class Reserva(Solicitud):
    """Representa las solicitudes de reserva de espacios físicos"""

    fecha_reserva = models.DateField(
        blank = False,
        null = False
    )

    hora_inicio = models.DateTimeField(
        auto_now=False, 
        auto_now_add=False
    )

    hora_fin = models.DateTimeField(
        auto_now=False, 
        auto_now_add=False
    )

    espacio_id_espacio = models.ForeignKey(
        Espacio,
        on_delete=models.CASCADE,
        blank = False
    )

class Contable(Solicitud):
    """Representa las solicitudes de viáticos para los maestros"""

    presupuesto = models.IntegerField(
        blank = False,
        null = False
    )

    cuenta_cobro = models.CharField(
        max_length = 10
    )

    tipoContable_id = models.ForeignKey(
        "TipoContable",
        on_delete=models.CASCADE,
        blank = False
    )

    docente_cedula = models.ForeignKey(
        Docente,
        on_delete=models.CASCADE,
        blank = False
    )