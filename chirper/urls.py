from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', include('chirper_web.urls')),
    url(r'^api/$', include('chirper_api.urls')),
    # Examples:
    # url(r'^$', 'chirper.views.home', name='home'),
    # url(r'^chirper/', include('chirper.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
