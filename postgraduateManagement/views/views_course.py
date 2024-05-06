from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from postgraduateManagement.models import Curso, Materia
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['codigo_materia'] = self.kwargs.get('codigo_materia')
        return context


@method_decorator(login_required, name='dispatch')
class CourseDeleteView(DeleteView):
    template_name = 'postgraduateManagement/../delete_course.html'
    model = Curso

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['codigo'] = self.kwargs.get('codigo')
        context['codigo_materia'] = self.kwargs.get('codigo_materia')
        return context

    def get_success_url(self):
        # Obtén el código de materia de la URL
        materia_codigo = self.kwargs.get('codigo_materia')
        # Aquí asumimos que 'codigo' es otro parámetro en tu URL
        codigo = self.kwargs.get('codigo')
        # Construye la URL de redirección
        return reverse('courseview', args=[codigo, materia_codigo])


@method_decorator(login_required, name='dispatch')
class CourseUpdateView(UpdateView):
    template_name = 'postgraduateManagement/../edit_course.html'
    model = Curso
    fields = ['grupo', 'cupo', 'usuario', 'periodo']
    success_url = reverse_lazy('subjectmanagment')


@method_decorator(login_required, name='dispatch')
class CourseCreateView(CreateView):
    template_name = 'postgraduateManagement/../create_course.html'
    model = Curso
    fields = ['nrc', 'grupo', 'cupo', 'usuario', 'periodo']

    def form_valid(self, form):
        # Obtén el código de materia de la URL
        materia_codigo = self.kwargs.get('codigo_materia')
        # Obtiene la materia correspondiente al código
        materia = get_object_or_404(Materia, codigo=materia_codigo)
        # Asigna la materia al curso antes de guardarlo
        form.instance.materia = materia
        # Llama al método form_valid de la clase base para guardar el curso
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        materia_codigo = self.kwargs.get('codigo_materia')
        materia = get_object_or_404(Materia, codigo=materia_codigo)
        kwargs['initial'] = {'materia': materia}
        return kwargs
    
    def get_success_url(self):
        # Obtén el código de materia de la URL
        materia_codigo = self.kwargs.get('codigo_materia')
        # Aquí asumimos que 'codigo' es otro parámetro en tu URL
        codigo = self.kwargs.get('codigo')
        # Construye la URL de redirección
        return reverse('courseview', args=[codigo, materia_codigo])
