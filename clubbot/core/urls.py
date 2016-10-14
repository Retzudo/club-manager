from django.conf.urls import url, include
from rest_framework import routers

from core import rest
from core import views

router = routers.DefaultRouter()
router.register(r'clubs', rest.ClubViewSet)


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'api/(?P<version>(v1))/', include(router.urls)),
]