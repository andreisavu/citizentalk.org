
from django.conf.urls.defaults import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='issues-index'),
    url(r'^explore', views.explore, name='issues-explore'),
)
