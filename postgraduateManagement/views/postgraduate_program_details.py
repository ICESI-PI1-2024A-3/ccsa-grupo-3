from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from postgraduateManagement.models import Programa, Director, Ciudad, Facultad, TipoPrograma, Pensum, Materia
from django.http import HttpResponseBadRequest, HttpResponseServerError


@login_required
def view_program_summary(request, codigo):
    programaP = Programa.objects.get(codigo=codigo)
    directors = programaP.director

    temp = Pensum.objects.filter(programa_id=programaP, periodo_id=1)
    subjects_1 = []

    for i in temp:
        subjects_1.append(i.materia.nombre)

    temp = Pensum.objects.filter(programa_id=programaP, periodo_id=2)
    subjects_2 = []

    for i in temp:
        subjects_2.append(i.materia.nombre)

    return render(request, "program_details_summary.html",
                  {"programa": programaP, "directors": directors, "subjects_1": subjects_1, "subjects_2": subjects_2})


@login_required
def view_program_planning(request, codigo):
    programaP = Programa.objects.get(codigo=codigo)
    return render(request, "program_details_planning.html", {"programa": programaP})


@login_required
def view_program_teachers(request, codigo):
    programaP = Programa.objects.get(codigo=codigo)
    pensum = Pensum.objects.filter(programa_id=programaP)  # Materias del programa
    subjects = [p.materia for p in pensum]
    teacher_list = [docente for materia in subjects for docente in materia.docente.all()]

    def is_valid_queryparam(param):
        return param != '' and param is not None

    def filter_teachers(request, teacher_list):
        search_contains = request.GET.get('search_contains')
        status = request.GET.get('status')
        city = request.GET.get('city')

        if is_valid_queryparam(search_contains):
            teacher_list = list(filter(lambda docente: search_contains.lower() in docente.nombre.lower(), teacher_list))

        if is_valid_queryparam(status):
            teacher_list = list(filter(lambda docente: docente.estado == status, teacher_list))

        if is_valid_queryparam(city):
            teacher_list = list(filter(lambda docente: docente.ciudad == city, teacher_list))

        return teacher_list

    teacher_list = filter_teachers(request, teacher_list)

    return render(request, "program_details_teachers.html", {"programa": programaP, "teacher_list": teacher_list})


@login_required
def view_program_subjects(request, codigo):
    programaP = Programa.objects.get(codigo=codigo)
    temp = Pensum.objects.filter(programa_id=programaP.codigo)

    subjects = []

    for i in temp:
        subjects.append(i.materia)

    return render(request, "program_details_subjects.html", {"programa": programaP, "subjects": subjects})
