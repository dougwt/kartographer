"""Specify Django url patterns for Comparison views."""

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'comparison.views.home', name='home'),
    url(r'^kart-components/', 'comparison.views.components', name='components'),
    url(r'^reset/', 'comparison.views.reset', name='reset'),
    url(r'^save/', 'comparison.views.save', name='save'),
    url(r'^l/(?P<url_hash>[0-9a-f]{5})/', 'comparison.views.list', name='list'),
    url(r'^top/', 'comparison.views.top', name='top'),
)
