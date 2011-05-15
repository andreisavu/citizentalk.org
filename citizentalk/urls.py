
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'citizentalk.views.home', name='home'),
    # url(r'^citizentalk/', include('citizentalk.foo.urls')),

    url(r'^$', include('citizentalk.dashboard.urls')),
    url(r'^issues/', include('citizentalk.issues.urls')),
    url(r'^institutions/', include('citizentalk.institutions.urls')),

    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', 
        {'next_page': '/'}, name='logout'),
    url('^join/$', 'profiles.views.join', name='profiles-join'),

    # Use django comments framework
    url(r'^comments/', include('django.contrib.comments.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

