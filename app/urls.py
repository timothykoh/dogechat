from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_success/$', views.login_success, name='login_success'),
    url(r'^friends/$',views.getfriend,name='search'),
)