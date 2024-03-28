from django.urls import path
from . import views

urlpatterns = [
    path('', views.index2, name="inicio2"),
    path('', views.indexHome, name="inicio"),
]
