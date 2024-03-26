from django.shortcuts import render

# Create your views here.
def show_all(request):
    return render(request, 'teachers.html')