from django.contrib import admin
from control.users.models import HRUser, Department


@admin.register(HRUser)
class HRUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'department']
