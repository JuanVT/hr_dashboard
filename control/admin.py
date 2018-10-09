from django.contrib import admin

from control.models import HRUser


@admin.register(HRUser)
class HRUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name']

