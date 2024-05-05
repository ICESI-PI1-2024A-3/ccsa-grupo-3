from django.urls import path
from django.views.generic import RedirectView ##
from .views import ProgramsView, TeachersView
from .views import postgraduate_program_details
import postgraduateManagement.views.views_course
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views



urlpatterns = [
    # path('', views.home, name='home'),
    # cuando se incluya home, cambiar el name=home de "programas/", ademas de agregarle un path

    path('', RedirectView.as_view(pattern_name='programs', permanent=False)),  # Redirecciona a /programas/
    
    path('programas/', ProgramsView.as_view(), name='programs'),

    path('docentes/', TeachersView.as_view(), name='teachers'),
    path('programas/<codigo>/', postgraduate_program_details.viewProgramPosgraduates),

    path('example/', postgraduateManagement.views.views_course.SubjectManagment.as_view(),
         name='subjectmanagment'),
    path('subjectmanagment/<str:codigo_materia>/',
         postgraduateManagement.views.views_course.CourseView.as_view(), name='courseview'),
    path('courses/<int:pk>/delete/', postgraduateManagement.views.views_course.CourseDeleteView.as_view(),
         name='course_delete'),
    path('courses/<str:codigo_materia>/<int:pk>/update/',
         postgraduateManagement.views.views_course.CourseUpdateView.as_view(), name='course_update'),
    path('courses/create/',
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

    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),


     #recuperar contraseña

     #Template para poner correo y recuperar contraseña
     path('Recuperar/', auth_views.PasswordResetView.as_view(
    template_name='registration/recover_password.html'
     ), name='reset_password'),

     #Template de mensaje que indica que se ha enviado el correo
     path('mensaje_enviado', auth_views.PasswordResetDoneView.as_view(
    template_name='registration/password_message_done.html'
    ), name='password_reset_done'),


      # Vista para restablecer la contraseña
    path('nueva_contraseña/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/restore_password.html'
    ), name='password_reset_confirm'),


     # URL para el mensaje de confirmación de restablecimiento de contraseña
    path('contraseña_restablecida/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_complete.html'
    ), name='password_reset_complete'),



]
