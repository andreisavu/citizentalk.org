
from django.conf.urls.defaults import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'^$', views.search, name='institutions-index'),
    url(r'^edit$', views.edit, name='institutions-edit'),
    url(r'^(?P<id>\d+)$', views.view, name='institutions-view'),
)

