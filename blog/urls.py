from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.PostArchive.as_view(), name='blog_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.PostDateDetail.as_view(), name='blog_detail'),
]
