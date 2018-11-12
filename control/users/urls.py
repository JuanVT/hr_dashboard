from django.conf.urls import url

from control.users.views import get_users, get_user_details, index_view
from control.users.views import users_import

urlpatterns = [
    url(r'^users/$', get_users, name='get_users'),
    url(r'^index/$', index_view, name='index_view'),
    url(r'^user/(?P<user_id>\d+)/$', get_user_details, name='get_user_details'),
    url(r'^import-user/$', users_import, name='users_import'),
]
