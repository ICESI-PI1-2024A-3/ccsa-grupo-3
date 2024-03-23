from django.db import models
from postgraduateManagement.models import Programa, Usuario, Espacio, Docente
# Create your models here.


class EstadoSolicitud(models.Model):
    """
    Modelo que representa los posibles estados que puede tener una solicitud.

    Atributos:
        código (CharField): Código que identifica el estado.
        nombre (CharField): Nombre del estado.
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


class TipoContable(models.Model):
    """
    Modelo que rRepresenta los posibles tipos que puede haber de una solicitud contable.

    Atributos:
        id (AutoField): Identificador único de la solicitud contable.
        tipo (CharField): Nombre de los tipos de solicitud contable.
    """

    id = models.AutoField(
        primary_key=True
    )

    tipo = models.CharField(
        max_length=40,
        unique=True
    )

    def __str__(self):
        return self.tipo


class Solicitud(models.Model):
    """
    Modelo abstracto que representa las solicitudes.

    Atributos:
        código (AutoField): Código que identifica la solicitud.
        descripción (TextField): Descripción de la solicitud.
        fecha_solicitud (DateField): Fecha en la que se realizó la solicitud.
        usuario (ForeignKey): Usuario que realizó la solicitud.
        estado_solicitud (ForeignKey): Estado actual de la solicitud.
        programa (ManyToManyField): Programas asociados a la solicitud.
    """

    codigo = models.AutoField(
        primary_key=True
    )

    descripcion = models.TextField()

    fecha_solicitud = models.DateField(
        auto_now_add=True
    )

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE
    )

    estado_solicitud = models.ForeignKey(
        EstadoSolicitud,
        on_delete=models.CASCADE
    )

    programa = models.ManyToManyField(
        Programa
    )

    def __str__(self):
        return self.codigo

    class Meta:
        abstract = True


class Reserva(Solicitud):
    """
    Modelo que representa las solicitudes de reserva de espacios físicos.

    Atributos:
        fecha_inicio (DateTimeField): Fecha y hora en la que inicia la reserva.
        fecha_fin (DateTimeField): Fecha y hora en la que finaliza la reserva.
        espacio (ForeignKey): Espacio físico que se desea reservar. 
    """

    fecha_inicio = models.DateTimeField()

    fecha_fin = models.DateTimeField()

    espacio = models.ForeignKey(
        Espacio,
        on_delete=models.CASCADE
    )


class Contable(Solicitud):
    """
    Modelo que representa las solicitudes de viáticos para los maestros.

    Atributos:
        presupuesto (IntegerField): Presupuesto asignado para los viáticos.
        cuenta_cobro (CharField): Cuenta de cobro asociada a la solicitud.
        tipo_contable (ForeignKey): Tipo de solicitud contable.
        docente (ForeignKey): Docente al que se le asignarán los viáticos.
    """

    presupuesto = models.IntegerField()

    cuenta_cobro = models.CharField(max_length=50)

    tipo_contable = models.ForeignKey(
        TipoContable,
        on_delete=models.CASCADE
    )

    docente = models.ForeignKey(
        Docente,
        on_delete=models.CASCADE
    )