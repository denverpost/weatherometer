from models import * 
from forecaster.models import Forecaster
from forms import ForecastForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import datetime

class ForecastToday():
    pass

def forecast_today(request):
    return object_list(request,
        queryset=Forecast.objects.filter(date__exact=datetime.date.today),
        paginate_by=50, allow_empty=True)

def update_forecast(request):
    forms = []
    forecasters = Forecaster.objects.all()
    if request.method == 'POST':
        # Loop through the forecasters.
        # If we have forecast values for the forecaster, and we don't already
        # have a forecast for that slot on this day, we add it.
        # The values for each forecast look like:
        # - id_date_{{item.pk}}
        # -- For each forecast item:
        # -- id_forecastitem-{{item.pk}}-temperature_{{count}}
        # -- id_forecastitem-{{item.pk}}-forecast_day_{{count}} // day being 0 for today, 1 for tomorrow, 2 day after
        # -- id_forecastitem-{{item.pk}}-type_{{count}} // type being high or low
        for item in forecasters:
            # Create the wrapper forecast object
            f, created = Forecast.objects.get_or_create(forecaster=item)
            for i in [0,1]:
                prefix = "forecastitem_%d_" % item.pk
                temp = request.POST.get("%stemperature_%d" % (prefix, i))
                day = request.POST.get("%sforecast_day_%d" % (prefix, i))
                ftype = request.POST.get("%stype_%d" % (prefix, i))
                if temp == '':
                    continue
                fi, created = ForecastItem.objects.get_or_create(items=f, temperature=temp, forecast_day=day, type=ftype)
    else:
        for item in forecasters:
            forms.append(ForecastForm(initial={'forecaster': item.pk}))

    return render(request, 'forecast/form.html', {'forecasters': forecasters, 'forms': forms})
