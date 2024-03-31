from django.urls import path
from .import views

urlpatterns = [
    path('', views.posgraduateP),
    path('verProgramacion/<codigo>/', views.viewProgramPosgraduates),
    path('editarProgramacion/<str:codigo>/',
         views.editarProgramacion, name='editar_programacion'),
    path('edicionPrograma/', views.edicionPrograma, name='edicion_programa'),
    path('eliminarPrograma/<str:codigo>/',
         views.eliminarPrograma, name='eliminar_programa'),
    path('editarDirector/<str:cedula>/',
         views.editarDirector, name='editar_director'),
    path('editingDirector/', views.editingDirector, name='editing_director'),
]
