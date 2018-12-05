from django.conf.urls import url

from control.purchase_order.views import purchase_order

urlpatterns = [

    url(r'^purchasing/$', purchase_order, name='purchase_order'),
]