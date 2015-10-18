from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start, name='start'),
    url(r'^browse/$', views.browse, name='browse'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^resourcefilter/$', views.resource_filter, name='resourcefilter'),
]
