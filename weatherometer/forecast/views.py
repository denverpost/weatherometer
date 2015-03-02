from models import * 
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
import datetime

def forecast_today(request):
    return object_list(request,
            queryset=Forecast.objects.filter(date__exact=datetime.date.today),
            paginate_by=50, allow_empty=True)
