from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from postgraduateManagement.models import Curso, Materia
from django.urls import reverse


class SubjectManagment(ListView):
    model = Materia


class CourseView(ListView):
    model = Curso

    def get_queryset(self):
        codigo_materia = self.kwargs.get('codigo_materia')  # Obtén el código de materia de la URL
        queryset = super().get_queryset()
        if codigo_materia:
            queryset = queryset.filter(materia__codigo=codigo_materia)
        return queryset


class CourseDeleteView(DeleteView):
    model = Curso
    success_url = reverse_lazy('subjectmanagment')


class CourseUpdateView(UpdateView):
    model = Curso
    fields = ['grupo', 'cupo', 'usuario', 'periodo']
    success_url = reverse_lazy('subjectmanagment')


class CourseCreateView(CreateView):
    model = Curso
    fields = ['materia', 'nrc', 'grupo', 'cupo', 'usuario', 'periodo']
    template_name = 'postgraduateManagement/curso_createform.html'
    print('Create')
    success_url = reverse_lazy('subjectmanagment')