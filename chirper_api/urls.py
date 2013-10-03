from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',

    url(r'^/?$', views.ChirpsCreateView.as_view(), name="chirps_list_create"),
)