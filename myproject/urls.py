from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^ws/$', 'ws.views.ws', name='ws'),
    url(r'^', include(admin.site.urls)),
)
