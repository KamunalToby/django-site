from django.db import models
from django.utils import timezone


class TutorialSection(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Step(models.Model):
    section = models.ForeignKey(TutorialSection, on_delete=models.CASCADE, related_name='steps')
    title = models.CharField(max_length=200)
    content = models.TextField()
    code_example = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    is_optional = models.BooleanField(default=False)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.section.title} - {self.title}"
