from django.conf.urls import url, include
from rest_framework import routers

from api import rest

router = routers.DefaultRouter()
router.register(r'clubs', rest.ClubViewSet, base_name='clubs')

urlpatterns = [
    url(r'(?P<version>(v1))/', include(router.urls)),
]