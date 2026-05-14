from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('install/', views.python_installation, name='python_installation'),
    path('ide/', views.ide_setup, name='ide_setup'),
    path('about/', views.about, name='about'),
    path('section/<slug:slug>/', views.section_detail, name='section_detail'),
    path('style.css', views.style_css, name='style_css'),
    path('main.js', views.main_js, name='main_js'),
]