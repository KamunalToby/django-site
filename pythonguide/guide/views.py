from django.shortcuts import render, get_object_or_404
from .models import TutorialSection, Step


def home(request):
    """Главная страница с оглавлением"""
    sections = TutorialSection.objects.all()
    return render(request, 'guide/home.html', {'sections': sections})


def section_detail(request, slug):
    """Детальная страница раздела"""
    section = get_object_or_404(TutorialSection, slug=slug)
    steps = section.steps.all()
    return render(request, 'guide/section_detail.html', {
        'section': section,
        'steps': steps
    })


def python_installation(request):
    """Страница установки Python"""
    return render(request, 'guide/python_installation.html')


def ide_setup(request):
    """Страница настройки IDE"""
    return render(request, 'guide/ide_setup.html')


def about(request):
    """Страница о сайте"""
    return render(request, 'guide/about.html')
