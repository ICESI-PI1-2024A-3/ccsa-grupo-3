from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Departamento(models.Model):
    name = models.CharField(
        max_length = 200,
        help_text = 'Nombre del departamento'
    )

class Materia(models.Model):
    id_curso = models.CharField(
        primary_key = True,
        max_length = 8,
        help_text = 'Código de la materia'
    )

    nombre = models.CharField(
        max_length = 120,
        help_text = 'Nombre de la materia'
    )

    creditos = models.IntegerField(
        default = 1,
        validators = [
            MinValueValidator(0, message="Los créditos deben ser al menos 0."),
            MaxValueValidator(20, message="Los créditos no pueden exceder 20."),
            ],
        help_text = 'Cantidad de créditos que pesa la materia'
    )

class Periodo(models.Model):
    semestre = models.IntegerField(
        MinValueValidator(0, message="El semestre debe ser mayor a 0."),
        help_text = "Semestre académico"        
        )
    
    fecha_inicio = models.DateField(
        help_text = "Fecha de inicio del semestre"  
        )
    
    fecha_fin = models.DateField(
        help_text = "Fecha de finalización del semestre"  
        )

class Curso(models.Model):
    nrc = models.IntegerField(
        primary_key = True,
        help_text = 'NRC del curso'
    )

    materia = models.ForeignKey(
        'Materia', 
        on_delete = models.CASCADE,
        null = False
    )
    
    grupo = models.IntegerField(
        help_text = 'numero del curso'
    )

    cupo = models.IntegerField(
        help_text = 'Cantidad de personas que tendrá el curso'
    )

    

class Clase(models.Model):
    """aquí van las clases que se dictaran en un programa de posgrado"""

    curso = models.ForeignKey(
        'Curso',
        on_delete = models.CASCADE,
        null = False
    )

    MODALIDAD_CLASE = (
        ('p', 'presencial'),
        ('v', 'virtual'),
        ('h', 'híbrida')
    )

    modalidad = models.CharField(
        max_length = 1,
        choices = MODALIDAD_CLASE,
        blank = True,
        default = 'p',
        help_text = 'Modalidad de la clase'
    )

    # Se supone que esto debe insertarse de manera autónoma por el sistema.
    fecha = models.DateField(
        null = False,
        help_text =  'Fecha de la clase'
    )

    hora_inicio = models.DateTimeField(
        help_text =  'Hora de inicio'
    )

    hora_fin = models.DateTimeField(
        help_text =  'Hora de finalización'
    )