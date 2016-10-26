from django.conf.urls import url, include

from core import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^account$', views.account, name='account'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^clubs/(?P<slug>[-\w]+)/', include('clubs.urls', namespace='clubs'))
]