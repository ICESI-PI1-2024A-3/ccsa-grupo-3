from django.urls import path
from django.views.generic import RedirectView
from .views import ProgramsView, TeachersView, DocenteUpdateView
from .views import postgraduate_program_details
from .views import views_home
import postgraduateManagement.views.views_course
from .views import teacherAssignCourse
from .views import teacherInfo
from .views import view_courses_for_teacher
from .views import views_teacher

from .views import views_contract
from .views.views_viatic import ViaticoListView, ViaticoCreateView, ViaticoDeleteView, ViaticoUpdateView

urlpatterns = [
    path('', views_home.homeView, name='home'),
    # cuando se incluya home, cambiar el name=home de "programas/", ademas de agregarle un path
    # Redirecciona a /programas/
    path('', RedirectView.as_view(pattern_name='home', permanent=False)),
    path('programas/', ProgramsView.as_view(), name='programs'),

    path('docentes/', TeachersView.as_view(), name='teachers'),
    path('docentes/<str:cedula>/', DocenteUpdateView.as_view(), name='state'),

    path('teacher/<str:cedula>/assign_course/',
         teacherAssignCourse.as_view(), name='teacher_assign_course'),
    path('profesor/<str:cedula_docente>/materia/<str:codigo_materia>/cursos/',
         view_courses_for_teacher, name='view_courses_for_teacher'),
    path('docentes/<str:cedula>/información_docente/',
         teacherInfo.as_view(), name='teacher_info'),

    path('programas/<codigo>/resumen',
         postgraduate_program_details.view_program_summary, name="program_summary"),
    path('programas/<codigo>/planeacion',
         postgraduate_program_details.view_program_planning, name="program_planning"),
    path('programas/<codigo>/docentes',
         postgraduate_program_details.view_program_teachers, name="program_teachers"),
    path('programas/<codigo>/materias',
         postgraduate_program_details.view_program_subjects, name="program_subjects"),

    path('programas/<codigo>/<str:codigo_materia>/',
         postgraduateManagement.views.views_course.CourseView.as_view(), name="courseview"),
    path('programas/<codigo>/<str:codigo_materia>/nuevo_curso',
         postgraduateManagement.views.views_course.CourseCreateView.as_view(), name='course_create'),
         ####
     path('programas/<codigo>/<str:codigo_materia>/<int:pk>/eliminar/', postgraduateManagement.views.views_course.CourseDeleteView.as_view(),
         name='course_delete'),
         path('programas/<codigo>/<str:codigo_materia>/<int:pk>/actualizar/', postgraduateManagement.views.views_course.CourseUpdateView.as_view(), name='course_update'),
          ###

    path('viaticos/', ViaticoListView.as_view(), name='viatic_list'),
    path('viaticos/crear/', ViaticoCreateView.as_view(), name='crear_viatico'),
    path('viaticos/<int:pk>/editar/',
         ViaticoUpdateView.as_view(), name='actualizar_viatico'),
    path('viaticos/<int:pk>/eliminar/',
         ViaticoDeleteView.as_view(), name='eliminar_viatico'),
    
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
    path('profesor/<str:cedula_docente>/materia/<str:codigo_materia>/cursos/assingCourse/<str:nrc_curso>/',
         views_teacher.assing_course_for_teacher, name='assing_course_for_teacher',),
    path('viewContract/', views_contract.viewContract, name='ver_contratos'),
    path('editingContract/', views_contract.editingContract,
         name='edicion_contratos'),
    path('viewContract/editContract/<codigo>/',
         views_contract.editContract, name='editar_contratos'),
]
