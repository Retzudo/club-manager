from django.conf.urls import url

from clubs import views

urlpatterns = [
    url('^$', views.news, name='club.news'),
    url('^events$', views.events, name='club.events'),
    url('^members$', views.members, name='club.members'),
    url('^cash$', views.cash, name='club.cash'),
    url('^settings$', views.settings, name='club.settings'),
]