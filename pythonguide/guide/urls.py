from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('section/<slug:slug>/', views.section_detail, name='section_detail'),
    path('python-installation/', views.python_installation, name='python_installation'),
    path('ide-setup/', views.ide_setup, name='ide_setup'),
    path('about/', views.about, name='about'),
]
