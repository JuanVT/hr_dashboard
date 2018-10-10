from django.conf.urls import url

from control.users.views import get_users, get_user_details

urlpatterns =[

    url(r'^users/$', get_users, name='get_users'),
    url(r'^user/(?P<user_id>\d+)/$', get_user_details, name='get_user_details'),

]
