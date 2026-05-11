// Python Installation Guide - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
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
        button.innerHTML = '<i class="bi bi-clipboard"></i> Копировать';
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
                button.innerHTML = '<i class="bi bi-check"></i> Скопировано!';
                button.classList.remove('btn-outline-secondary');
                button.classList.add('btn-success');
                
                setTimeout(function() {
                    button.innerHTML = '<i class="bi bi-clipboard"></i> Копировать';
                    button.classList.remove('btn-success');
                    button.classList.add('btn-outline-secondary');
                }, 2000);
            }).catch(function(err) {
                console.error('Не удалось скопировать текст: ', err);
                button.innerHTML = '<i class="bi bi-x"></i> Ошибка';
                button.classList.remove('btn-outline-secondary');
                button.classList.add('btn-danger');
                
                setTimeout(function() {
                    button.innerHTML = '<i class="bi bi-clipboard"></i> Копировать';
                    button.classList.remove('btn-danger');
                    button.classList.add('btn-outline-secondary');
                }, 2000);
            });
        });
    });

    // Progress indicator for installation steps
    const steps = document.querySelectorAll('.step-item');
    if (steps.length > 0) {
        // Add progress bar
        const progressContainer = document.createElement('div');
        progressContainer.className = 'progress-container mb-4';
        progressContainer.innerHTML = `
            <div class="d-flex justify-content-between align-items-center mb-2">
                <span class="progress-label">Прогресс выполнения:</span>
                <span class="progress-text">0/${steps.length} шагов</span>
            </div>
            <div class="progress">
                <div class="progress-bar" role="progressbar" style="width: 0%" aria-valuenow="0" aria-valuemin="0" aria-valuemax="${steps.length}"></div>
            </div>
        `;
        
        const firstStep = steps[0];
        firstStep.parentElement.insertBefore(progressContainer, firstStep);

        // Add checkboxes to steps
        steps.forEach((step, index) => {
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.className = 'form-check-input step-checkbox me-2';
            checkbox.id = `step-${index}`;
            
            const label = document.createElement('label');
            label.className = 'form-check-label';
            label.htmlFor = `step-${index}`;
            
            const stepContent = step.querySelector('.step-content');
            const stepTitle = stepContent.querySelector('h5');
            
            stepTitle.insertBefore(checkbox, stepTitle.firstChild);
            stepTitle.insertBefore(label, stepTitle.firstChild);
            
            // Update progress on checkbox change
            checkbox.addEventListener('change', updateProgress);
        });

        function updateProgress() {
            const checkedSteps = document.querySelectorAll('.step-checkbox:checked').length;
            const totalSteps = steps.length;
            const percentage = (checkedSteps / totalSteps) * 100;
            
            const progressBar = document.querySelector('.progress-bar');
            const progressText = document.querySelector('.progress-text');
            
            progressBar.style.width = percentage + '%';
            progressBar.setAttribute('aria-valuenow', checkedSteps);
            progressText.textContent = `${checkedSteps}/${totalSteps} шагов`;
            
            // Mark completed steps
            steps.forEach((step, index) => {
                const checkbox = document.getElementById(`step-${index}`);
                if (checkbox.checked) {
                    step.classList.add('completed-step');
                    step.style.opacity = '0.7';
                } else {
                    step.classList.remove('completed-step');
                    step.style.opacity = '1';
                }
            });
        }
    }

    // Command line tool detection
    function detectOS() {
        const userAgent = window.navigator.userAgent;
        const platform = window.navigator.platform;
        const macosPlatforms = ['Macintosh', 'MacIntel', 'MacPPC', 'Mac68K'];
        const windowsPlatforms = ['Win32', 'Win64', 'Windows', 'WinCE'];
        const linuxPlatforms = ['Linux', 'X11'];

        if (macosPlatforms.indexOf(platform) !== -1) {
            return 'macos';
        } else if (windowsPlatforms.indexOf(platform) !== -1) {
            return 'windows';
        } else if (linuxPlatforms.indexOf(platform) !== -1) {
            return 'linux';
        }
        return 'unknown';
    }

    // Highlight OS-specific commands
    const userOS = detectOS();
    const osBadges = document.querySelectorAll('.os-badge');
    osBadges.forEach(badge => {
        if (badge.dataset.os === userOS) {
            badge.classList.add('badge-success');
            badge.classList.remove('badge-secondary');
        }
    });

    // Search functionality (if implemented)
    const searchInput = document.getElementById('search-input');
    if (searchInput) {
        let searchTimeout;
        
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            const query = this.value.toLowerCase();
            
            searchTimeout = setTimeout(function() {
                performSearch(query);
            }, 300);
        });
    }

    function performSearch(query) {
        const content = document.querySelectorAll('.card-body, .section-content');
        
        content.forEach(section => {
            const text = section.textContent.toLowerCase();
            if (text.includes(query) || query === '') {
                section.parentElement.style.display = 'block';
            } else {
                section.parentElement.style.display = 'none';
            }
        });
    }

    // Print functionality
    const printBtn = document.getElementById('print-btn');
    if (printBtn) {
        printBtn.addEventListener('click', function() {
            window.print();
        });
    }

    // Theme toggle (if implemented)
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            document.body.classList.toggle('dark-theme');
            const isDark = document.body.classList.contains('dark-theme');
            localStorage.setItem('theme', isDark ? 'dark' : 'light');
            
            // Update button text
            this.innerHTML = isDark ? '<i class="bi bi-sun"></i> Светлая тема' : '<i class="bi bi-moon"></i> Темная тема';
        });

        // Load saved theme
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme === 'dark') {
            document.body.classList.add('dark-theme');
            themeToggle.innerHTML = '<i class="bi bi-sun"></i> Светлая тема';
        }
    }

    // Feedback form (if implemented)
    const feedbackForm = document.getElementById('feedback-form');
    if (feedbackForm) {
        feedbackForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Show loading state
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Отправка...';
            submitBtn.disabled = true;
            
            // Simulate form submission
            setTimeout(function() {
                submitBtn.innerHTML = '<i class="bi bi-check"></i> Отправлено!';
                submitBtn.classList.remove('btn-primary');
                submitBtn.classList.add('btn-success');
                
                // Reset form
                feedbackForm.reset();
                
                // Reset button after 3 seconds
                setTimeout(function() {
                    submitBtn.innerHTML = originalText;
                    submitBtn.disabled = false;
                    submitBtn.classList.remove('btn-success');
                    submitBtn.classList.add('btn-primary');
                }, 3000);
            }, 1500);
        });
    }

    // Initialize tooltips for code examples
    document.querySelectorAll('.code-example pre').forEach(function(pre) {
        pre.setAttribute('title', 'Нажмите на кнопку "Копировать" чтобы скопировать код');
    });

    // Add keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        // Ctrl/Cmd + K for search
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            const searchInput = document.getElementById('search-input');
            if (searchInput) {
                searchInput.focus();
            }
        }
        
        // Escape to close modals
        if (e.key === 'Escape') {
            const modals = document.querySelectorAll('.modal.show');
            modals.forEach(modal => {
                bootstrap.Modal.getInstance(modal).hide();
            });
        }
    });

    console.log('Python Installation Guide initialized successfully!');
});
