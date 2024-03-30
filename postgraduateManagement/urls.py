from django.contrib import admin
from django.urls import path

import postgraduateManagement.views.CourseViews
from postgraduateManagement import views

urlpatterns = [
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