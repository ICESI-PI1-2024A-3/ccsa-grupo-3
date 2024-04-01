from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from postgraduateManagement.models import Curso, Materia


class SubjectManagment(ListView):
    template_name = 'postgraduateManagement/../subject_list.html'
    model = Materia

    def get_queryset(self):
        queryset = super().get_queryset()
        # Obtener el ID del programa de la consulta
        programa_id = self.request.GET.get('programa_id')
        if programa_id:
            # Filtrar las materias por el programa dado
            queryset = queryset.filter(programas__id=programa_id)
        return queryset


class CourseView(ListView):
    template_name = 'postgraduateManagement/../course_list.html'
    model = Curso

    def get_queryset(self):
        # Obtén el código de materia de la URL
        codigo_materia = self.kwargs.get('codigo_materia')
        queryset = super().get_queryset()
        if codigo_materia:
            queryset = queryset.filter(materia__codigo=codigo_materia)
        return queryset


class CourseDeleteView(DeleteView):
    template_name = 'postgraduateManagement/../delete_course.html'
    model = Curso
    success_url = reverse_lazy('subjectmanagment')


class CourseUpdateView(UpdateView):
    template_name = 'postgraduateManagement/../edit_course.html'
    model = Curso
    fields = ['grupo', 'cupo', 'usuario', 'periodo']
    success_url = reverse_lazy('subjectmanagment')


class CourseCreateView(CreateView):
    template_name = 'postgraduateManagement/../create_course.html'
    model = Curso
    fields = ['materia', 'nrc', 'grupo', 'cupo', 'usuario', 'periodo']
    success_url = reverse_lazy('subjectmanagment')
