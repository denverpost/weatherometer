from models import * 
from forecast.models import ActualTemperature
from forecaster.models import Forecaster
from forms import ForecastForm, ActualTemperatureForm, Updaters
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

def update_temperature(request):
    forms = []
    items = ActualTemperature.objects.all()
    form = ActualTemperatureForm()
    message = ''
    if request.method == 'POST':
        # Create a new ActualTemperature, or update existing.
        date = datetime.datetime.strptime(request.POST['date'], "%Y-%m-%d")
        high = int(request.POST['temperature_high'])
        low = int(request.POST['temperature_low'])
        try:
            a = ActualTemperature.objects.get(date=date)
            a.update(
                temperature_high=high,
                temperature_low=low)
            a.save()
            message = 'Temperature for %s updated' % request.POST['date']
        except:
            a = ActualTemperature.objects.create(
                date=date,
                temperature_high=high,
                temperature_low=low)
            message = 'Temperature for %s created' % request.POST['date']
    else:
        pass

    return render(request, 'forecast/temperature_form.html', {'forms': forms, 'form': form, 'message': message, 'items': items})

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
