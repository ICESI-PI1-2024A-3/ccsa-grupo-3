from django.urls import path
from . import views
from .views import TeachersView

urlpatterns = [
    path('home/', views.home, name='home'),
    path('teachers/', TeachersView.as_view(), name='home'),
]
