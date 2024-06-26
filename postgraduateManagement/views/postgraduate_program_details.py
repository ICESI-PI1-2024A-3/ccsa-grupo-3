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

    return render(request, "program_details_summary.html", {"programa": programaP, "directors": directors, "subjects_1": subjects_1, "subjects_2": subjects_2})

@login_required
def view_program_planning(request, codigo):
    programaP = Programa.objects.get(codigo=codigo)
    return render (request, "program_details_planning.html", {"programa": programaP})

@login_required
def view_program_teachers(request, codigo):
    programaP = Programa.objects.get(codigo=codigo)
    pensum = Pensum.objects.filter(programa_id=programaP)
    subjects = [p.materia for p in pensum]
    teacher_set = set()

    for subject in subjects:
        teachers = subject.docente.all()
        for teacher in teachers:
            teacher_set.add(teacher)

    teacher_list = list(teacher_set)

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
    cities = Ciudad.objects.all()

    return render (request, "program_details_teachers.html", {"programa": programaP, "teacher_list": teacher_list, "cities": cities})

@login_required
def view_program_subjects(request, codigo):
    programaP = Programa.objects.get(codigo=codigo)
    temp = Pensum.objects.filter(programa_id=programaP.codigo)

    subjects = []

    for i in temp:
        subjects.append(i.materia) 

    return render (request, "program_details_subjects.html", {"programa": programaP, "subjects": subjects})

@login_required
def eliminarPrograma(request, codigo):
    progrmaP = Programa.objects.get(codigo=codigo)
    progrmaP.delete()
    return redirect('/')

@login_required
def editarDirector(request, cedula):
    directors = Director.objects.get(cedula=cedula)
    ciudad = Ciudad.objects.all()
    return render(request, "edit_director.html", {"director": directors, "ciudad": ciudad})

@login_required
def editingDirector(request):
    if request.method == 'POST':
        try:
            cedula = request.POST['txtCodigo']
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            email = request.POST['email']
            telefono = request.POST['telefono']
            ciudad = request.POST['ciudad']

            ciudadObject = Ciudad.objects.get(nombre=ciudad)

            director = Director.objects.get(cedula=cedula)
            director.nombre = nombre
            director.apellido = apellido
            director.email = email
            director.telefono = telefono
            director.ciudad = ciudadObject
            director.save()
            return redirect('/')
        except Exception as a:
            return HttpResponseServerError(f"Error: {a}")
        else:
            return HttpResponseBadRequest("Método no permitido")

@login_required
def editarProgramacion(request, codigo):
    progrmaP = Programa.objects.get(codigo=codigo)
    facultades = Facultad.objects.all()
    tipoProgramas = TipoPrograma.objects.all()
    return render(request, "edicion_programa.html", {"programa": progrmaP, "facultades": facultades, "tipoProgramas": tipoProgramas})

@login_required
def edicionPrograma(request):
    if request.method == 'POST':
        try:
            codigo = request.POST['txtCodigo']
            facultad = request.POST['facultad']
            facultadObject = Facultad.objects.get(nombre=facultad)
            tipoPrograma = request.POST['tipoPrograma']
            tipoProgramaObject = TipoPrograma.objects.get(nombre=tipoPrograma)
            programa = Programa.objects.get(codigo=codigo)
            programa.facultad = facultadObject
            programa.tipo_de_programa = tipoProgramaObject
            programa.save()
            return redirect('/')
        except Exception as e:
            return HttpResponseServerError(f"Error: {e}")
    else:
        return HttpResponseBadRequest("Método no permitido")
