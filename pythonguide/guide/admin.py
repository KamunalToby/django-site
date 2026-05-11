from django.contrib import admin
from .models import TutorialSection, Step


class StepInline(admin.TabularInline):
    model = Step
    extra = 1


@admin.register(TutorialSection)
class TutorialSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'order', 'created_at']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [StepInline]
    search_fields = ['title', 'content']


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ['title', 'section', 'order', 'is_optional']
    list_editable = ['order', 'is_optional']
    list_filter = ['section', 'is_optional']
    search_fields = ['title', 'content']
