from django.conf.urls import patterns, url

from pypi import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
