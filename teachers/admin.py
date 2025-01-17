from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'subject', 'phone', 'email', 'experience', 'photo_display')
    list_editable = ('phone', 'email')
    search_fields = ('first_name', 'last_name', 'phone', 'email', 'subject__name')
    list_filter = ('subject', 'experience')
    ordering = ('-experience',)
    readonly_fields = ('photo_display',)
    def photo_display(self, obj):
        """Suratni admin panelda ko'rsatish."""
        if obj.photo:
            return f'<img src="{obj.photo.url}" width="50" height="50" style="object-fit:cover;"/>'
        return "No Photo"
    photo_display.allow_tags = True
    photo_display.short_description = 'Photo'
