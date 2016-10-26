from django.conf.urls import url, include
from rest_framework import routers

from api import rest

router = routers.DefaultRouter()
router.register(r'clubs', rest.ClubViewSet, base_name='clubs')

urlpatterns = [
    url(r'(?P<version>(v1))/', include(router.urls)),
    url(r'(?P<version>(v1))/clubs/(?P<club_id>\d+)/cash/transactions', rest.TransactionsList.as_view(), name='cash'),
    url(r'(?P<version>(v1))/clubs/(?P<club_id>\d+)/cash', rest.CashView.as_view(), name='cash'),
]
