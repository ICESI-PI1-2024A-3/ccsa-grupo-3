from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('teachers/', views.show_all, name='home'),
]
