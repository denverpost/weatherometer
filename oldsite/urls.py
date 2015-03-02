from django.conf import settings
from django.conf.urls.defaults import *
from django.db.models import permalink
from django.contrib.comments.models import Comment
from django.template import RequestContext
from django.http import HttpRequest
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from forecast.models import *
from forecaster.models import *
from django.contrib.auth.models import *
from django.contrib import databrowse

databrowse.site.register(Forecast)
databrowse.site.register(ForecastItem)
databrowse.site.register(ActualTemperature)
databrowse.site.register(AccuracyRating)
#databrowse.site.register(AccuracyRatingArchive)
databrowse.site.register(Forecaster)
"""
from feeds import *
feed_dict = {
    'lists': ListFeed,
    'photos': PhotoFeed,
}
"""
forecaster_dict = {
    'queryset': Forecaster.objects.all(),
}

home_dict = {
    'queryset': AccuracyRating.objects.filter(type__exact=5, daytype__exact=0).order_by('avg'),
    'template_name': 'home.html',
}
forecast_date_year_dict = {
    'queryset': Forecast.objects.all(),
    'date_field': 'date',
    'make_object_list': True,
}
forecast_date_dict = {
    'queryset': Forecast.objects.all(),
    'date_field': 'date',
}
forecast_dict = {
    'queryset': Forecast.objects.all(),
    'date_field': 'date',
    'num_latest': 75,
}

temperature_date_year_dict = {
    'queryset': ActualTemperature.objects.all(),
    'date_field': 'date',
    'make_object_list': True,
}
temperature_date_dict = {
    'queryset': ActualTemperature.objects.all(),
    'date_field': 'date',
}
temperature_dict = {
    'queryset': ActualTemperature.objects.all(),
    'date_field': 'date',
    'num_latest': 75,
}

urlpatterns = patterns('',
    # Admin
    #(r'^admin/obj_lookup/$', 'genericadmin.views.generic_lookup'),
    (r'^admin/',include('django.contrib.admin.urls')),
    (r'^databrowse/(.*)', databrowse.site.root),

    # Home
    url(r'^$', 'django.views.generic.list_detail.object_list', home_dict, 'home'),
    
    # Model: Forecaster
    (r'^forecaster/(?P<slug>[-\w]+)/$', 'forecaster.views.detail'),
    (r'^forecaster/$', 'django.views.generic.list_detail.object_list', forecaster_dict),
    
    # Model: Forecast
    (r'^forecast/today/$', 'forecast.views.forecast_today'),
    (r'^forecast/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', 'django.views.generic.date_based.archive_day', forecast_date_dict),
    (r'^forecast/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'django.views.generic.date_based.archive_month', forecast_date_dict),
    (r'^forecast/(?P<year>\d{4})/$', 'django.views.generic.date_based.archive_year', forecast_date_year_dict),
    (r'^forecast/$', 'django.views.generic.date_based.archive_index', forecast_dict),

    # Feeds:
    #(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feed_dict}),
    
    # Google Sitemap:
    #(r'^sitemap.xml$', 'django.contrib.sitemaps.views.index', {'sitemaps': sitemaps_dict}),
    #(r'^sitemap-(?P<section>.+).xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps_dict}),

    # Charts
    (r'^charts/', include('charts.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/django/weather/templates/media'}),
        #(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/joe/djang/weather/templates/media'}),
    )
