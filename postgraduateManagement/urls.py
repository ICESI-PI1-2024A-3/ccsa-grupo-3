from django.urls import path
from .views import ProgramsView, TeachersView
from .views import postgraduate_program_details

import postgraduateManagement.views.CourseViews

urlpatterns = [
    # path('', views.home, name='home'),
    # cuando se incluya home, cambiar el name=home de "programas/", ademas de agregarle un path
    path('', ProgramsView.as_view(), name='home'),
    path('programas/', ProgramsView.as_view(), name='programs'),

    path('docentes/', TeachersView.as_view(), name='teachers'),
    path('programas/<codigo>/', postgraduate_program_details.viewProgramPosgraduates),

    path('example/', postgraduateManagement.views.CourseViews.SubjectManagment.as_view(),
         name='subjectmanagment'),
    path('subjectmanagment/<str:codigo_materia>/',
         postgraduateManagement.views.CourseViews.CourseView.as_view(), name='courseview'),
    path('courses/<int:pk>/delete/', postgraduateManagement.views.CourseViews.CourseDeleteView.as_view(),
         name='course_delete'),
    path('courses/<str:codigo_materia>/<int:pk>/update/',
         postgraduateManagement.views.CourseViews.CourseUpdateView.as_view(), name='course_update'),
    path('courses/create/',
         postgraduateManagement.views.CourseViews.CourseCreateView.as_view(), name='course_create'),


    path('editarProgramacion/<str:codigo>/',
         postgraduate_program_details.editarProgramacion, name='editar_programacion'),
    path('edicionPrograma/', postgraduate_program_details.edicionPrograma,
         name='edicion_programa'),
    path('eliminarPrograma/<str:codigo>/',
         postgraduate_program_details.eliminarPrograma, name='eliminar_programa'),
    path('editarDirector/<str:cedula>/',
         postgraduate_program_details.editarDirector, name='editar_director'),
    path('editingDirector/', postgraduate_program_details.editingDirector,
         name='editing_director'),
]
