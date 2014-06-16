from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'comparison.views.home', name='home'),
    url(r'^items/', 'comparison.views.items', name='items'),
    url(r'^add/', 'comparison.views.add', name='add'),
    url(r'^reset/', 'comparison.views.reset', name='reset'),
    url(r'^save/', 'comparison.views.save', name='save'),
    url(r'^l/(?P<url_hash>[0-9a-f]{5})', 'comparison.views.list', name='list'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    try:
        import debug_toolbar
        urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
    except ImportError:
        pass
