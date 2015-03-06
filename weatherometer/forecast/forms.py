from django import forms
from django.forms.models import inlineformset_factory
from models import Forecast, ForecastItem
from django.conf import settings

ForecastItemFormSet = inlineformset_factory(Forecast, ForecastItem)
#forecast = Forecast.objects.get(pk=2)
#formset = ForecastItemFormSet(instance=forecast)

class ForecastForm(forms.ModelForm):
    class Meta:
        model = Forecast
        fields = '__all__'

def update_temp_diff():
    """ This does two major actions:
    
    1. Take the ForecastItem records with dates no more recent than yesterday --
    those are the only ones we could be updating.
    
    2. Take the ActualTemperature records with dates that match the ForecastItem
    dates. Compare the temperatures. Take the result and add it to the ForecastItem
    differential field, and then save it.
    """
    yesterday = datetime.today().date() - timedelta(1)
    temperature = ActualTemperature.objects.get(date=yesterday)
    items = ForecastItem.objects.filter(differential__isnull=True)
    i = 0
    for item in items:
        if item.date <= yesterday:
            if item.type == 1:
                differential = item.temperature - temperature.temperature_high
            else:
                differential = item.temperature - temperature.temperature_low
            
            if differential < 0:
                differential_abs = differential * -1
            else:
                differential_abs = differential

            item.differential = differential
            item.differential_abs = differential_abs
            item.save()
            i = i + 1
    
        print '\n ForecastItem differentials updated. %i records updated' % ( i )
