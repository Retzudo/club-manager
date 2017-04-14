from django.conf.urls import url, include
from rest_framework_nested import routers

from api import rest

router = routers.SimpleRouter()
router.register(r'clubs', rest.ClubViewSet, base_name='clubs')

transactions_router = routers.NestedSimpleRouter(router, 'clubs', lookup='club')
transactions_router.register('transactions', rest.TransactionsViewSet, base_name='transactions')

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'', include(transactions_router.urls)),
]
