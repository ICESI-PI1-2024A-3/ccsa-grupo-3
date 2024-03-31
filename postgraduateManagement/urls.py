from django.urls import path
from . import views
from .views import ProgramsView

import postgraduateManagement.views.CourseViews
from postgraduateManagement import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('programas/', ProgramsView.as_view(), name='home'),
    path('', postgraduateManagement.views.CourseViews.SubjectManagment.as_view(), name='subjectmanagment'),
    path('subjectmanagment/<str:codigo_materia>/',
         postgraduateManagement.views.CourseViews.CourseView.as_view(), name='courseview'),
    path('courses/<int:pk>/delete/', postgraduateManagement.views.CourseViews.CourseDeleteView.as_view(),
         name='course_delete'),
    path('courses/<str:codigo_materia>/<int:pk>/update/',
         postgraduateManagement.views.CourseViews.CourseUpdateView.as_view(), name='course_update'),
    path('courses/create/',
         postgraduateManagement.views.CourseViews.CourseCreateView.as_view(), name='course_create'),
]

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
