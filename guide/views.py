from django.shortcuts import get_object_or_404
from .models import TutorialSection, Step
from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import escape


def _get_base_layout(title, content):
    """Вспомогательная функция для создания базовой разметки страницы"""
    return f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title} | Python Guide</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css">
        <link rel="stylesheet" href="{reverse('style_css')}">
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
            <div class="container">
                <a class="navbar-brand" href="{reverse('home')}">PythonУстановка</a>
                <div class="navbar-nav">
                    <a class="nav-link" href="{reverse('python_installation')}">Установка</a>
                    <a class="nav-link" href="{reverse('ide_setup')}">Настройка IDE</a>
                    <a class="nav-link" href="{reverse('about')}">О проекте</a>
                </div>
            </div>
        </nav>
        <div class="container">
            {content}
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        <script src="{reverse('main_js')}"></script>
    </body>
    </html>
    """


def home(request):
    """Главная страница с оглавлением"""
    sections = TutorialSection.objects.all()
    
    sections_html = ""
    for section in sections:
        sections_html += f'''
        <div class="col-md-6 mb-4">
            <div class="card h-100">
                <div class="card-body">
                    <h5 class="card-title text-primary">{section.title}</h5>
                    <p class="card-text text-muted">{escape(section.content[:100])}...</p>
                    <a href="{reverse('section_detail', args=[section.slug])}" class="btn btn-outline-primary">Читать далее</a>
                </div>
            </div>
        </div>
        '''

    content = f"""
    <div class="hero-section text-white p-5 mb-5 text-center">
        <h1 class="display-4">Добро пожаловать в мир Python!</h1>
         <p class="lead">Все, что нужно для начала разработки, в одном месте.</p>
    </div>

    <h2 class="mb-4">Основные этапы</h2>
    <div class="row mb-5">
        <div class="col-md-4">
            <div class="card border-primary mb-3">
                <div class="card-body text-center">
                    <i class="bi bi-download h1 text-primary"></i>
                    <h5 class="card-title mt-2">1. Установка Python</h5>
                    <p class="card-text small">Базовая настройка интерпретатора для Windows, macOS и Linux.</p>
                    <a href="{reverse('python_installation')}" class="btn btn-primary">Перейти</a>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card border-info mb-3">
                <div class="card-body text-center">
                    <i class="bi bi-code-square h1 text-info"></i>
                    <h5 class="card-title mt-2">2. VS Code</h5>
                    <p class="card-text small">Легкий и мощный редактор с огромным количеством плагинов.</p>
                    <a href="{reverse('ide_setup')}#vscode" class="btn btn-info text-white">Настроить</a>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card border-success mb-3">
                <div class="card-body text-center">
                    <i class="bi bi-terminal h1 text-success"></i>
                    <h5 class="card-title mt-2">3. PyCharm</h5>
                    <p class="card-text small">Профессиональная IDE для серьезных проектов на Python.</p>
                    <a href="{reverse('ide_setup')}#pycharm" class="btn btn-success">Настроить</a>
                </div>
            </div>
        </div>
    </div>

    <h2 class="mb-4">Дополнительные руководства</h2>
    </div>
    <div class="row">
        {sections_html if sections_html else '<p class="text-center">Разделы скоро появятся...</p>'}
    </div>
    """
    return HttpResponse(_get_base_layout("Главная", content))


def section_detail(request, slug):
    """Детальная страница раздела"""
    section = get_object_or_404(TutorialSection, slug=slug)
    steps = section.steps.all()
    
    steps_html = ""
    for i, step in enumerate(steps, 1):
        code_html = f'<pre class="code-example"><code>{escape(step.code_example)}</code></pre>' if step.code_example else ''
        optional_badge = '<span class="badge bg-info text-dark mb-2">Необязательно</span>' if step.is_optional else ''
        
        steps_html += f'''
        <div class="step-item mb-4 p-3 border-start border-4 border-primary bg-light">
            {optional_badge}
            <h4>Шаг {i}: {escape(step.title)}</h4>
            <div class="step-content">{escape(step.content).replace('\n', '<br>')}</div>
            {code_html}
        </div>
        '''

    if not steps_html:
        steps_html = '<p class="text-muted">В этом разделе пока нет шагов.</p>'

    content = f"""
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><a href="{reverse('home')}">Главная</a></li>
        <li class="breadcrumb-item active">{escape(section.title)}</li>
      </ol>
    </nav>
    <h1 class="mb-4">{escape(section.title)}</h1>
    <div class="description mb-5 lead">{escape(section.content).replace('\n', '<br>')}</div>
    <div class="steps">
        {steps_html}
    </div>
    """
    return HttpResponse(_get_base_layout(section.title, content))


def python_installation(request):
    content = """
    <h1 class="mb-4">Установка Python 3</h1>
    <div class="row">
        <div class="col-lg-8">
            <section class="mb-5">
                <h3>Шаг 1: Скачивание</h3>
                <p>Перейдите на официальный сайт <a href="https://www.python.org/downloads/" target="_blank">python.org</a>. Сайт автоматически предложит версию для вашей ОС.</p>
            </section>
            <section class="mb-5">
                <h3>Шаг 2: Установка (Windows)</h3>
                <div class="alert alert-warning">
                    <i class="bi bi-exclamation-triangle-fill"></i> 
                    <strong>Важно:</strong> При запуске инсталлятора обязательно отметьте галочку <strong>"Add Python to PATH"</strong>.
                </div>
                <p>Это позволит вам запускать Python из любого окна терминала.</p>
            </section>
            <section class="mb-5">
                <h3>Шаг 3: Проверка</h3>
                <p>Откройте терминал (cmd или PowerShell) и введите команду:</p>
                <pre class="bg-dark text-light p-3 rounded"><code>python --version</code></pre>
            </section>
        </div>
    </div>
    """
    return HttpResponse(_get_base_layout("Установка", content))


def ide_setup(request):
     content = """
    <h1 class="mb-4">Настройка среды разработки (IDE)</h1>
    
    <div id="vscode" class="mb-5 p-4 border rounded shadow-sm">
        <h2 class="text-info"><i class="bi bi-code-square"></i> Visual Studio Code</h2>
        <p>Лучший выбор для тех, кто любит скорость и кастомизацию.</p>
        <ol>
            <li>Скачайте с <a href="https://code.visualstudio.com/" target="_blank">официального сайта</a>.</li>
            <li>Откройте вкладку <strong>Extensions</strong> (Ctrl+Shift+X).</li>
            <li>Найдите и установите расширение <strong>"Python"</strong> от Microsoft.</li>
            <li>Нажмите <code>Ctrl+Shift+P</code> и выберите <strong>Python: Select Interpreter</strong>.</li>
        </ol>
    </div>

    <div id="pycharm" class="mb-5 p-4 border rounded shadow-sm">
        <h2 class="text-success"><i class="bi bi-terminal"></i> PyCharm</h2>
        <p>Полноценный комбайн для Python разработчиков.</p>
        <ol>
            <li>Скачайте версию <strong>Community</strong> (она бесплатная) с сайта <a href="https://www.jetbrains.com/pycharm/download/" target="_blank">JetBrains</a>.</li>
            <li>При создании проекта PyCharm сам предложит создать виртуальное окружение (venv).</li>
            <li>Нажмите "Create" и подождите индексации файлов.</li>
        </ol>
    </div>
    """
     return HttpResponse(_get_base_layout("Настройка IDE", content))


def about(request):
    content = "<h1>О проекте</h1><p>Этот сайт создан полностью на языке Python с использованием Django.</p>"
    return HttpResponse(_get_base_layout("О проекте", content))


def style_css(request):
    css_content = """/* Python Installation Guide - Custom Styles */

.hero-section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.hero-section .btn {
    border-radius: 25px;
    padding: 12px 30px;
    font-weight: 500;
}

.card {
    border: none;
    box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
}

.step-number {
    min-width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    flex-shrink: 0;
}

.step-item {
    position: relative;
}

.optional-step {
    background-color: #fff8e1;
    border-radius: 8px;
    padding: 15px;
}

.code-example {
    background-color: #f8f9fa;
    border-radius: 8px;
    padding: 15px;
    margin-top: 10px;
}
"""
    return HttpResponse(css_content, content_type="text/css")


def main_js(request):
    js_content = """// Python Installation Guide - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle=\"tooltip\"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^=\"#\"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Copy code functionality
    document.querySelectorAll('pre code').forEach(function(codeBlock) {
        // Add copy button
        const button = document.createElement('button');
        button.className = 'btn btn-sm btn-outline-secondary copy-btn';
        button.innerHTML = '<i class=\"bi bi-clipboard\"></i> \u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c';
        button.style.position = 'absolute';
        button.style.top = '10px';
        button.style.right = '10px';
        
        const pre = codeBlock.parentElement;
        pre.style.position = 'relative';
        pre.appendChild(button);

        // Copy on click
        button.addEventListener('click', function() {
            const text = codeBlock.textContent;
            navigator.clipboard.writeText(text).then(function() {
                button.innerHTML = '<i class=\"bi bi-check\"></i> \u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u043e!';
                button.classList.remove('btn-outline-secondary');
                button.classList.add('btn-success');
                
                setTimeout(function() {
                    button.innerHTML = '<i class=\"bi bi-clipboard\"></i> \u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c';
                    button.classList.remove('btn-success');
                    button.classList.add('btn-outline-secondary');
                }, 2000);
            });
        });
    });
});"""
    return HttpResponse(js_content, content_type="application/javascript")
