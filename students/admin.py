from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'date_of_birth', 'phone', 'address', 'photo_display')
    list_editable = ('phone', 'address')
    search_fields = ('full_name', 'phone', 'address')
    list_filter = ('group', 'date_of_birth')
    ordering = ('-id',)
    filter_horizontal = ('group',)
    readonly_fields = ('photo_display',)
    def photo_display(self, obj):
        """
        Talabaning suratini kichik ko'rinishda ko'rsatadi.
        """
        if obj.photo:
            return f'<img src="{obj.photo.url}" width="50" height="50" style="object-fit:cover;"/>'
        return "No Photo"
    photo_display.allow_tags = True
    photo_display.short_description = 'Photo'
