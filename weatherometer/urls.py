# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from forecast.models import *
from forecaster.models import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

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
    url(r'^$',  # noqa
        TemplateView.as_view(template_name='pages/home.html'),
        name="home"),
    url(r'^about/$',
        TemplateView.as_view(template_name='pages/about.html'),
        name="about"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Uncomment the next line to enable avatars
    url(r'^avatar/', include('avatar.urls')),

    # Your stuff: custom urls go here
    # Home
    url(r'^$', 'django.views.generic.list.ListView', home_dict, 'home'),
    
    # Model: Forecaster
    (r'^forecaster/(?P<slug>[-\w]+)/$', 'forecaster.views.detail'),
    (r'^forecaster/$', 'django.views.generic.list.ListView', forecaster_dict),
    
    # Model: Forecast
    (r'^forecast/today/$', 'forecast.views.forecast_today'),
    (r'^forecast/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', 'django.views.generic.dates.DayArchiveView', forecast_date_dict),
    (r'^forecast/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'django.views.generic.dates.MonthArchiveView', forecast_date_dict),
    (r'^forecast/(?P<year>\d{4})/$', 'django.views.generic.dates.YearArchiveView', forecast_date_year_dict),
    (r'^forecast/$', 'django.views.generic.dates.ArchiveIndexView', forecast_dict),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/django/weather/templates/media'}),
        #(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/joe/djang/weather/templates/media'}),
    )
