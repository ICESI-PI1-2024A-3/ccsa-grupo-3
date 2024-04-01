from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.shortcuts import render
from postgraduateManagement.models import Docente, Ciudad
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views import View

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
