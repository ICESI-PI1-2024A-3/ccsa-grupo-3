from django.urls import path
from django.views.generic import RedirectView  ##
from .views import ProgramsView, TeachersView, DocenteUpdateView
from .views import postgraduate_program_details
import postgraduateManagement.views.views_course
from .views import teacherAssignCourse
from .views import teacherInfo

urlpatterns = [
    # path('', views.home, name='home'),
    # cuando se incluya home, cambiar el name=home de "programas/", ademas de agregarle un path
    path('', RedirectView.as_view(pattern_name='programs', permanent=False)),  # Redirecciona a /programas/
    path('programas/', ProgramsView.as_view(), name='programs'),

    path('docentes/', TeachersView.as_view(), name='teachers'),
    path('docentes/<str:cedula>/', DocenteUpdateView.as_view(), name='state'),
    
    path('teacher/<str:cedula>/assign_course/', teacherAssignCourse.as_view(), name='teacher_assign_course'),

    path('docentes/<str:cedula>/información_docente/', teacherInfo.as_view(), name='teacher_info'),


    
    path('programas/<codigo>/', postgraduate_program_details.viewProgramPosgraduates),

    path('subjectmanagment/', postgraduateManagement.views.views_course.SubjectManagment.as_view(),
         name='subjectmanagment'),
    path('courseview/<str:codigo_materia>/',
         postgraduateManagement.views.views_course.CourseView.as_view(), name='courseview'),
    path('courses/<int:pk>/delete/', postgraduateManagement.views.views_course.CourseDeleteView.as_view(),
         name='course_delete'),
    path('courses/<str:codigo_materia>/<int:pk>/update/',
         postgraduateManagement.views.views_course.CourseUpdateView.as_view(), name='course_update'),
    path('courses/create/<str:codigo_materia>',
         postgraduateManagement.views.views_course.CourseCreateView.as_view(), name='course_create'),

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
