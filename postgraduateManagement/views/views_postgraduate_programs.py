from django.shortcuts import render
from postgraduateManagement.models import Programa
from django.views import View


class ProgramsView(View):
    @staticmethod
    def get(request):
        programasListados = Programa.objects.all()
        programa_seleccionado = None

        if request.method == 'POST':
            programa_codigo = request.POST.get('programa_codigo')
            if programa_codigo:
                programa_seleccionado = Programa.objects.get(
                    codigo=programa_codigo)

        return render(request, "programas_posgrado.html", {"programas": programasListados, "programa_seleccionado": programa_seleccionado})
