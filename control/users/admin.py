from django.contrib import admin

from control.users.models import HRUser, TimeOffRequest, Department


@admin.register(HRUser)
class HRUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name']


@admin.register(TimeOffRequest)
class TimeOffRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'department']
