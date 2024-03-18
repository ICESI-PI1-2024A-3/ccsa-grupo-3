from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('materia/', views.MateriaListView.as_view(), name='materia'),
    path('curso/', views.CursoListView.as_view(), name='curso'),
    path('clase/', views.ClaseListView.as_view(), name='clase'),
    path('', views.home, name='home'),
    path('registrarCurso/', views.registrarMateria),
    path('edicionCurso/<id_curso>', views.edicionMateria),
    path('editarCurso/', views.editarMateria),
    path('eliminarCurso/<id_curso>', views.eliminarMateria),
    path('programas/', views.programasView)
]
