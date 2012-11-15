from django.conf.urls.defaults import patterns, url
from syncr.flickr.models import Photo
from syncr.flickr.views import flickr_photo_detail_in_set as photo_detail


photo_info_dict = {
    'queryset': Photo.objects.all(),
    'date_field': 'taken_date',
}

urlpatterns = patterns('',
    url(r'^$', ('photos.views.photo_list')),
    url(r'^(?P<year>\d{4})/$', 'django.views.generic.date_based.archive_year', photo_info_dict, 'race_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 'django.views.generic.date_based.archive_month', photo_info_dict, 'race_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'django.views.generic.date_based.archive_day', photo_info_dict, 'race_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[\w-]+)/$', photo_detail, name='photo_detail'),
)