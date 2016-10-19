from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^shouyin/$', views.shouyin, name='shouyin'),
    url(r'^ruku/$', views.ruku, name='ruku'),
    url(r'^get/txt/$', views.gettxt, name='gettxt'),
]