from django.contrib import admin
from .models import Employee, Department  


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'salary', 'height', 'weight']
    filter_horizontal = ('departments',)  


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
