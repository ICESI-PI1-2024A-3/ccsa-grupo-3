from typing import Any
from venv import logger
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from django.shortcuts import render
from postgraduateManagement.models import Docente, Ciudad
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from postgraduateManagement.models import Curso, Materia, DocentesCursos
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views import View
from django.http import JsonResponse

@method_decorator(login_required, name='dispatch')
class TeachersView(View):
    @staticmethod
    def is_valid_queryparam(param):
        return param != '' and param is not None

    def get(self, request):
        teacher_list = self.filter_teachers(request)
        cities = Ciudad.objects.all()
        return render(request, 'teachers.html', {"teacher_list": teacher_list, "cities": cities})

    def filter_teachers(self, request):
        teachers = Docente.objects.all()

        search_contains = request.GET.get('search_contains')
        status = request.GET.get('status')
        city = request.GET.get('city')

        if self.is_valid_queryparam(search_contains):
            teachers = teachers.filter(nombre__icontains=search_contains)
            # filtrar apellidos
            # reonocer si es numerico o no

        if self.is_valid_queryparam(status):
            teachers = teachers.filter(estado=status)

        if self.is_valid_queryparam(city):
            teachers = teachers.filter(ciudad=city)

        return teachers

@method_decorator(login_required, name='dispatch')
class DocenteUpdateView(UpdateView):
    model = Docente
    fields = ['estado']  # Solo incluir el campo de estado en el formulario
    template_name = 'postgraduateManagement/../edit_state_teacher.html'  # Nombre de tu template
    success_url = reverse_lazy('teachers')

    def get_object(self, queryset=None):
        # Obtener el objeto Docente que se está actualizando utilizando la cédula de la URL
        cedula = self.kwargs.get('cedula')
        return Docente.objects.get(cedula=cedula)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar la instancia del docente al contexto para acceder a sus datos en el template
        context['docente'] = self.object
        return context
    




@method_decorator(login_required, name='dispatch')
class teacherAssignCourse(UpdateView):
    model = Docente
    fields = ['estado'] 
    template_name = 'postgraduateManagement/../assign_course_to_teacher.html'  # Nombre del template
    success_url = reverse_lazy('teachers')

    def get_object(self, queryset=None):
        # Obtener el objeto Docente que se está actualizando utilizando la cédula de la URL
        cedula = self.kwargs.get('cedula')
        return Docente.objects.get(cedula=cedula)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar la instancia del docente al contexto para acceder a sus datos en el template
        context['docente'] = self.object

        # Obtener todas las materias y agregarlas al contexto
        context['materias'] = Materia.objects.all()

        return context
    


@login_required
def view_courses_for_teacher(request, cedula_docente, codigo_materia):
    # Obtener el profesor y la materia
    docente = get_object_or_404(Docente, cedula=cedula_docente)
    materia = get_object_or_404(Materia, codigo=codigo_materia)
    
    # Obtener los cursos disponibles para esa materia
    cursos_disponibles = Curso.objects.filter(materia=materia)
    
    context = {
        'docente': docente,
        'materia': materia,
        'cursos_disponibles': cursos_disponibles,
    }
    return render(request, 'postgraduateManagement/../course_list_for_teacher.html', context)



@login_required
def assing_course_for_teacher(request,cedula_docente, nrc_curso,codigo_materia):
    materia = get_object_or_404(Materia, codigo=codigo_materia)
    docente = get_object_or_404(Docente, cedula=cedula_docente)
    curso = get_object_or_404(Curso, nrc=nrc_curso)
    prioridad = 2
    
    if DocentesCursos.objects.filter(curso=curso, docente=docente).exists():
        return JsonResponse({'error': 'Este curso ya está asignado a este docente.'}, status=400)

    else:
        asociacion = DocentesCursos.objects.create(prioridad=prioridad, curso_id=curso.nrc, docente_id=docente.cedula)
        return redirect('teachers')








# Info del docente
@method_decorator(login_required, name='dispatch')
class teacherInfo(UpdateView):
    model = Docente
    fields = '__all__'  # Puedes incluir todos los campos del modelo
    template_name = 'postgraduateManagement/../show_teacher_info.html'
    success_url = reverse_lazy('teachers')

    def get_object(self, queryset=None):
        cedula = self.kwargs.get('cedula')
        return Docente.objects.get(cedula=cedula)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['docente'] = self.object  # Pasar el objeto del docente al contexto
        
        docentes_cursos = DocentesCursos.objects.filter(docente=self.object)
        context['docentes_cursos'] = docentes_cursos
        
        # Pasa también el objeto del docente al contexto
        context['docente'] = self.object  
        return context
