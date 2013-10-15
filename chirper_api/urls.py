from django.conf.urls import patterns, include, url
import views

user_urls = patterns('',
    url(r'^$', views.UserList.as_view(), name='user-list'),
    
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)/$', views.UserDetails.as_view(), name='user-details'),
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)/follow/(?P<followed>[0-9a-zA-Z_-]+)$', views.follow, name='follow'),
)

chirps_urls = patterns('',
    url(r'^$', views.ChirpsList.as_view(), name='chirp-list'),
    url(r'^/create$', views.create_chirp, name='create-chirp'),
)

urlpatterns = patterns('',
    url(r'^register$', views.register_user, name='register'),
    url(r'^users', include(user_urls)),
    url(r'^chirps', include(chirps_urls)),
    url(r'^token-auth', 'rest_framework.authtoken.views.obtain_auth_token', name='token-auth'),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)