from django.urls import path
from . import views
from .views import ProgramsView

urlpatterns = [
    path('home/', views.home, name='home'),
    path('programas/', ProgramsView.as_view(), name='home')
]
