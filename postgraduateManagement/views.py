from django.shortcuts import render
from django.views import generic
from .models import Materia, Curso, Clase

# Esto solo esta de forma temporal para ayudar a revisar si se esta agregando de forma adecuada
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_materias = Materia.objects.all().count()
    num_curso = Curso.objects.all().count()
    num_clase = Clase.objects.all().count()

    context  = {
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