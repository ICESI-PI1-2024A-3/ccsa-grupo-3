from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('materia/', views.MateriaListView.as_view(), name='materia'),
    path('curso/', views.CursoListView.as_view(), name='curso'),
    path('clase/', views.ClaseListView.as_view(), name='clase'),
]