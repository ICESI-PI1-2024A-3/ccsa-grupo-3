from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from postgraduateManagement.models import Curso, Materia


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
    success_url = reverse_lazy('course_list')


class CourseUpdateView(UpdateView):
    model = Curso
    fields = ['nrc', 'grupo', 'cupo', 'usuario', 'periodo']
    success_url = reverse_lazy('course_list')


class CourseCreateView(CreateView):
    model = Curso
    fields = ['nrc', 'grupo', 'cupo', 'usuario', 'periodo']  # Excluyendo 'materia' del formulario

    def form_valid(self, form):
        codigo_materia = self.kwargs.get('codigo_materia')
        form.instance.materia_id = codigo_materia
        return super().form_valid(form)

    def get_success_url(self):
        codigo_materia = self.kwargs.get('codigo_materia')
        return reverse_lazy('course_list', kwargs={'codigo_materia': codigo_materia})
