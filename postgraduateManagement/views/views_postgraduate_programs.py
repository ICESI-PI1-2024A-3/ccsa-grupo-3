from django.shortcuts import render
from postgraduateManagement.models import Programa
from django.views import View


class ProgramsView(View):
    def get(self, request):
        programasListados = Programa.objects.all()
        return render(request, "programas_posgrado.html", {"programas": programasListados})

    def post(self, request):
        programa_codigo = request.POST.get('programa_codigo')
        programa_seleccionado = None
        if programa_codigo:
            programa_seleccionado = Programa.objects.get(
                codigo=programa_codigo)
        programasListados = Programa.objects.all()
        return render(request, "programas_posgrado.html", {"programas": programasListados, "programa_seleccionado": programa_seleccionado})
