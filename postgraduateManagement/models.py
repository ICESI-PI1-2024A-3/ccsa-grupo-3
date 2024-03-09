from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse


# Create your models here.


class Materia(models.Model):
    nrc = \
        models.CharField(max_length=8, help_text='Ingrese el nrc de la materia')
    syllabus = \
        models.FileField()
    descripcion = \
        models.CharField(max_length=256,
                         help_text='Ingrese la descripcion de la materia')
    numero = \
        models.CharField(max_length=64,
                         help_text='Ingrese  el numero de identificacion de la materia')
    horas = \
        models.CharField(max_length=2,
                         help_text='Ingrese el numero de horas de la materia')
    campus = \
        models.CharField(max_length=128,
                         help_text='Ingrese el campus donde se dictara la  materia')
    asientos = \
        models.IntegerField(max_length=2,
                            help_text='Ingrese el numero de asientos')
    primary_key = \
        nrc


class Curso(models.Model):
    materia_nrc = \
        models.ForeignKey(Materia.nrc, on_delete=models.CASCADE)
    numgrupo = \
        models.CharField(max_length=8, help_text='Ingrese el numero de grupo')
    tipodegrupo = \
        models.CharField(max_length=12, help_text=' ingrese el tipo de grupo')
    primary_key = \
        (materia_nrc, numgrupo)


class Docente(models.Model):
    cedula = \
        models.CharField(max_length=32, help_text='ingrese numero de cedula')
    nombre = \
        models.CharField(max_length=250, help_text='ingrese su nombre')
    apellido = \
        models.CharField(max_length=250, help_text='ingrese su apellido')
    foto = \
        models.ImageField()
    ciudad = \
        models.CharField(max_length=250, help_text='ingrese su ciudad de origen')
    pais = \
        models.CharField(max_length=32, help_text='ingrese su pais de origen')
    telefono = \
        models.CharField(max_length=250, help_text='ingrese su numero de telefono')
    correo = \
        models.CharField(max_length=250, help_text='ingrese su correo electronico')
    primary_key = \
        cedula


class Contrato(models.Model):
    docente_cedula = \
        models.ForeignKey(Docente.cedula, on_delete=models.CASCADE)
    archivo = \
        models.FileField()