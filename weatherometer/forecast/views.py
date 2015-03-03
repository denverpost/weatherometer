from models import * 
from forms import ForecastForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import datetime

def forecast_today(request):
    return object_list(request,
        queryset=Forecast.objects.filter(date__exact=datetime.date.today),
        paginate_by=50, allow_empty=True)

def update_forecast(request):
    if request.method == POST:
        pass
    else:
        form = ForecastForm()

    return render(request, 'forecast/form.html', {'form': form})
