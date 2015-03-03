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
    if request.method == 'POST':
        pass
    else:
        forms = []
        forecasters = Forecaster.objects.all()
        for item in forecasters:
            forms.append(ForecastForm(initial={'forecaster': item.pk}))

    return render(request, 'forecast/form.html', {'forms': forms})
