from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from postgraduateManagement.models import Curso, Materia, Viatico
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone


@method_decorator(login_required, name='dispatch')
class ViaticoListView(ListView):
    model = Viatico
    template_name = 'postgraduateManagement/../viatic_list.html'
    context_object_name = 'viaticos'


@method_decorator(login_required, name='dispatch')
class ViaticoCreateView(CreateView):
    model = Viatico
    fields = ['estado_viatico', 'descripcion', 'presupuesto', 'presupuesto', 'docente', 'clase']
    template_name = 'postgraduateManagement/../create_viatic.html'
    success_url = reverse_lazy('viatic_list')

    def form_valid(self, form):
        form.instance.fecha_solicitud = timezone.now()  # Asigna la fecha actual
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ViaticoUpdateView(UpdateView):
    model = Viatico
    fields = ['estado_viatico', 'descripcion', 'presupuesto']
    template_name = 'postgraduateManagement/../edit_viatic.html'
    success_url = reverse_lazy('viatic_list')


@method_decorator(login_required, name='dispatch')
class ViaticoDeleteView(DeleteView):
    model = Viatico
    template_name = 'postgraduateManagement/../delete_viatic.html'
    success_url = reverse_lazy('viatic_list')
