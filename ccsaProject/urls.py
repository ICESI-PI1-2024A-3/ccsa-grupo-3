"""
URL configuration for ccsaProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import postgraduateManagement.Views.CourseViews
from postgraduateManagement import Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', postgraduateManagement.Views.CourseViews.SubjectManagment.as_view(), name='subjectmanagment'),
    path('subjectmanagment/<str:codigo_materia>/',
         postgraduateManagement.Views.CourseViews.CourseView.as_view(), name='courseview'),
    path('courses/<int:pk>/delete/', postgraduateManagement.Views.CourseViews.CourseDeleteView.as_view(),
         name='course_delete'),
    path('courses/<str:codigo_materia>/<int:pk>/update/',
         postgraduateManagement.Views.CourseViews.CourseUpdateView.as_view(), name='course_update'),
    path('courses/create/', postgraduateManagement.Views.CourseViews.CourseCreateView.as_view(), name='course_create'),

]
