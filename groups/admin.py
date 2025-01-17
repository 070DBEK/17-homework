from django.contrib import admin
from .models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'teacher', 'students_count')
    search_fields = ('name', 'teacher__first_name', 'teacher__last_name')
    list_filter = ('teacher',)
    ordering = ('name',)
    filter_horizontal = ('students',)
    def students_count(self, obj):
        return obj.students.count()
    students_count.short_description = 'Number of Students'
