from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from .models import Materia, Curso, Clase

# Esto solo esta de forma temporal para ayudar a revisar si se esta agregando de forma adecuada


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_materias = Materia.objects.all().count()
    num_curso = Curso.objects.all().count()
    num_clase = Clase.objects.all().count()

    context = {
        'num_materias': num_materias,
        'num_curso': num_curso,
        'num_clase': num_clase,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class MateriaListView(generic.ListView):
    template_name = 'materia_list.html'

    model = Materia
    paginate_by = 10


class CursoListView(generic.ListView):
    template_name = 'curso_list.html'

    model = Curso
    paginate_by = 10


class ClaseListView(generic.ListView):
    template_name = 'clase_list.html'

    model = Clase
    paginate_by = 10


def home(request):
    materiasListadas = Materia.objects.all()
    messages.success(request, '¡Materias listadas!')
    return render(request, "gestionCursos.html", {"materias": materiasListadas})


def registrarMateria(request):
    id_curso = request.POST['txtID']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    materia = Materia.objects.create(
        id_curso=id_curso, nombre=nombre, creditos=creditos)
    messages.success(request, '¡Materia registrada!')
    return redirect('/')


def edicionMateria(request, id_curso):
    materia = Materia.objects.get(id_curso=id_curso)
    return render(request, "edicionCurso.html", {"materia": materia})


def editarMateria(request):
    id_curso = request.POST['txtID']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    materia = Materia.objects.get(id_curso=id_curso)
    materia.nombre = nombre
    materia.creditos = creditos
    materia.save()

    messages.success(request, '¡Materia actualizada!')

    return redirect('/')


def eliminarMateria(request, id_curso):
    materia = Materia.objects.get(id_curso=id_curso)
    materia.delete()

    messages.success(request, '¡Materia eliminada!')

    return redirect('/')


def programasView(request):
    return render(request, "programas_posgrado.html")
