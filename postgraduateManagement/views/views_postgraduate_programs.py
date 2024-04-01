from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from postgraduateManagement.models import Programa
from django.views import View


@method_decorator(login_required, name='dispatch')
class ProgramsView(View):
    def get(self, request):
        programasListados = Programa.objects.all()
        return render(request, "postgraduate_programs.html", {"programas": programasListados})

    def post(self, request):
        programa_codigo = request.POST.get('programa_codigo')
        programa_seleccionado = None
        if programa_codigo:
            programa_seleccionado = Programa.objects.get(
                codigo=programa_codigo)
        programasListados = Programa.objects.all()
        return render(request, "postgraduate_programs.html", {"programas": programasListados, "programa_seleccionado": programa_seleccionado})
