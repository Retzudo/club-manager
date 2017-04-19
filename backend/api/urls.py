from django.conf.urls import url, include
from rest_framework import routers

from api import rest

router = routers.DefaultRouter()
router.register(r'clubs', rest.ClubModelViewSet, base_name='clubs')
router.register(r'transactions', rest.TransactionsModelViewSet, base_name='transactions')

urlpatterns = [
    url(r'', include(router.urls)),
]
