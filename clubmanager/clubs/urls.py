from django.conf.urls import url

from clubs import views

urlpatterns = [
    url('^$', views.index)
]