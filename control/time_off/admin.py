from django.contrib import admin

from control.time_off.models import TimeOffRequest


@admin.register(TimeOffRequest)
class TimeOffRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']