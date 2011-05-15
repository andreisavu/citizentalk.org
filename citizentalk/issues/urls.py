
from django.conf.urls.defaults import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='issues-index'),
    url(r'^new', views.new, name='issues-new'),
    url(r'view/(\d+)$', views.view, name='issues-view'),
    url(r'comment/new/$', views.add_comment, name='issues-comment-new'),
)

