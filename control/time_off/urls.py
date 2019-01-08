from django.conf.urls import url

from control.time_off.views import time_off

urlpatterns = [

    url(r'^time_off/$', time_off, name='time_off'),
]