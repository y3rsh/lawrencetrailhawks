from __future__ import absolute_import

from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

from .models import Post


blog_info_dict = {
    'queryset': Post.objects.all(),
    'date_field': 'publish',
}

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.date_based.archive_index', blog_info_dict, 'blog_index'),
    url(r'^(?P<year>\d{4})/$', 'django.views.generic.date_based.archive_year', blog_info_dict, 'blog_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 'django.views.generic.date_based.archive_month', blog_info_dict, 'blog_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'django.views.generic.date_based.archive_day', blog_info_dict, 'blog_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'django.views.generic.date_based.object_detail', blog_info_dict, 'blog_detail'),
)