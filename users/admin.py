from django.contrib import admin
from django.contrib.auth.models import User
from .models import Student, PreExistingStudent

# Unregister User model if it is already registered
if admin.site.is_registered(User):
    admin.site.unregister(User)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'matric_number')
    search_fields = ('user__username', 'matric_number')


@admin.register(PreExistingStudent)
class PreExistingStudentAdmin(admin.ModelAdmin):
    list_display = ('matric_number', 'last_name')
    search_fields = ('matric_number', 'last_name')
