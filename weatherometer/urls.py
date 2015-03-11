# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from forecast.models import *
from forecaster.models import *
from forecast.views import *
from forecast.views import ForecastToday
from forecaster.views import ForecasterList, ForecasterDetail

from bakery.views import BuildableDetailView, BuildableListView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

forecaster_dict = {
    'queryset': Forecaster.objects.all(),
}

class HomeView(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        return AccuracyRating.objects.all()

class BakeryHomeView(BuildableDetailView):
    template_name = 'home.html'
    queryset = AccuracyRating.objects.all()

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
    #url(r'^$',  # noqa
    #    TemplateView.as_view(template_name='pages/home.html'),
    #    name="home"),
    url(r'^about/$',
        TemplateView.as_view(template_name='pages/about.html'),
        name="about"),

    # ADMIN
    url(r'^admin/', include(admin.site.urls)),
    url(r'^forecast/add/$', update_forecast),
    url(r'^temperature/add/$', update_temperature),

    # User management
    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Uncomment the next line to enable avatars
    url(r'^avatar/', include('avatar.urls')),

    # Your stuff: custom urls go here
    url(r'^$', HomeView.as_view(), name='home'),
    
    # Model: Forecaster
    #(r'^forecaster/(?P<slug>[-\w]+)/today/$', AccuracyRatingDetail.as_view()),
    (r'^forecaster/(?P<slug>[-\w]+)/$', ForecasterDetail.as_view()),
    (r'^forecaster/$', ForecasterList.as_view()),
    
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
