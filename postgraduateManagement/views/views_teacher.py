from django.shortcuts import render
from postgraduateManagement.models import Docente


# Create your views here.
def show_all(request):
    teacher_list = Docente.objects.all()
    return render(request, 'teachers.html', {"teacher_list": teacher_list})