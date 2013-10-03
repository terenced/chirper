from django.conf.urls import patterns, url

from chirper_web import views

urlpatterns = patterns('',
    url(r'^', views.HomeView.as_view(), name="home"),
)