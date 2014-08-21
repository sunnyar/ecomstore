from django.conf.urls.defaults import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecomstore.views.home', name='home'),
    # url(r'^ecomstore/', include('ecomstore.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^', include('ecomstore.catalog.urls')),
    (r'^cart/', include('ecomstore.cart.urls')),
    (r'^accounts/', include('ecomstore.accounts.urls')),
    (r'^accounts/', include('django.contrib.auth.urls')),
#    (r'^catalog/$', 'preview.views.home'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root' : settings.STATIC_ROOT }),
)

handler404 = 'ecomstore.views.file_not_found_404'