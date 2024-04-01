# this is gerson file

from django.shortcuts import render, redirect
from postgraduateManagement.models import Programa, Director, Ciudad, Facultad, TipoPrograma
from django.http import HttpResponseBadRequest, HttpResponseServerError
# Create your views here.


def viewProgramPosgraduates(request, codigo):
    programaP = Programa.objects.get(codigo=codigo)
    directors = programaP.director

    return render(request, "viewProgramP.html", {"programa": programaP, "directors": directors})


def eliminarPrograma(request, codigo):
    progrmaP = Programa.objects.get(codigo=codigo)
    progrmaP.delete()
    return redirect('/')


def editarDirector(request, cedula):
    directors = Director.objects.get(cedula=cedula)
    ciudad = Ciudad.objects.all()
    return render(request, "edit_director.html", {"director": directors, "ciudad": ciudad})


def editingDirector(request):
    if request.method == 'POST':
        try:
            cedula = request.POST['txtCodigo']
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            email = request.POST['email']
            telefono = request.POST['telefono']
            ciudad = request.POST['ciudad']

            ciudadObject = Ciudad.objects.get(nombre=ciudad)

            director = Director.objects.get(cedula=cedula)
            director.nombre = nombre
            director.apellido = apellido
            director.email = email
            director.telefono = telefono
            director.ciudad = ciudadObject
            director.save()
            return redirect('/')
        except Exception as a:
            return HttpResponseServerError(f"Error: {a}")
        else:
            return HttpResponseBadRequest("Método no permitido")


def editarProgramacion(request, codigo):
    progrmaP = Programa.objects.get(codigo=codigo)
    facultades = Facultad.objects.all()
    tipoProgramas = TipoPrograma.objects.all()
    return render(request, "edicion_programa.html", {"programa": progrmaP, "facultades": facultades, "tipoProgramas": tipoProgramas})


def edicionPrograma(request):
    if request.method == 'POST':
        try:
            codigo = request.POST['txtCodigo']
            facultad = request.POST['facultad']
            facultadObject = Facultad.objects.get(nombre=facultad)
            tipoPrograma = request.POST['tipoPrograma']
            tipoProgramaObject = TipoPrograma.objects.get(nombre=tipoPrograma)
            programa = Programa.objects.get(codigo=codigo)
            programa.facultad = facultadObject
            programa.tipo_de_programa = tipoProgramaObject
            programa.save()
            return redirect('/')
        except Exception as e:
            return HttpResponseServerError(f"Error: {e}")
    else:
        return HttpResponseBadRequest("Método no permitido")
