from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start, name='start'),
    url(r'^browse/$', views.browse, name='browse'),
    url(r'^result/$', views.result, name='result'),
    url(r'^resourcefilter/$', views.resource_filter, name='resourcefilter'),
    #url(r'^host/(?P<pk>[0-9]+)/$', views.host, name = 'host'),
    #url(r'^guests/(?P<pk>[0-9]+)/$', views.guests, name = 'guests'),
    #url(r'^assignment_email/(?P<pk>[0-9]+)/$', views.assignment_email, name = 'assignment_email'),
]
