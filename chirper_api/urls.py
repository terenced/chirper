from django.conf.urls import patterns, include, url
import views

user_urls = patterns('',
    url(r'^$', views.UserList.as_view(), name='user-list'),
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)/$', views.UserDetails.as_view(), name='user-details'),
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)/follow/(?P<followed>[0-9a-zA-Z_-]+)$', views.follow, name='follow'),
)

chirps_urls = patterns('',
    url(r'^/timeline$', views.ChirpsList.as_view(), name='chirp-timeline'),
)

urlpatterns = patterns('',
    url(r'^users', include(user_urls)),
    url(r'^chirps', include(chirps_urls)),
)