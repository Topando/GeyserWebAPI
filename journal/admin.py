from django.contrib import admin
from django import forms
from django.utils import timezone
from django.utils.safestring import mark_safe

from journal.models import Journal

admin.site.site_header = "Управление проектом"
admin.site.site_title = "Гейзер"
admin.site.index_title = "Добро пожаловать в панель управления"


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'order', 'beginning_activity', 'created_date', 'updated_date')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('order', '-updated_date')
    list_editable = ('is_active', 'order')

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'slug', 'announcement', 'description', 'order')
        }),
        ('Активность', {
            'fields': ('is_active', 'beginning_activity'),
        }),
        ('Медиа', {
            'fields': ('photo_detail', 'photo_announcement'),
        }),
        ('SEO', {
            'fields': ('seo_title', 'seo_description'),
            'classes': ('collapse',),  # Свернуть эту секцию
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not obj:
            form.base_fields['beginning_activity'].initial = timezone.localdate()
        return form

    def save_model(self, request, obj, form, change):
        if not obj.beginning_activity:
            obj.beginning_activity = timezone.localdate()
        super().save_model(request, obj, form, change)

