from models import * 
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import datetime

def forecast_today(request):
    return object_list(request,
            queryset=Forecast.objects.filter(date__exact=datetime.date.today),
            paginate_by=50, allow_empty=True)
