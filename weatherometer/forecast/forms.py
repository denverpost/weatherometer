from django import forms
from django.forms.models import inlineformset_factory
from models import Forecast, ForecastItem
from django.conf import settings

ForecastItemFormSet = inlineformset_factory(Forecast, ForecastItem)
#forecast = Forecast.objects.get(pk=1)
forecast = Forecast.objects.get(pk=2)
#forecast = Forecast.objects.create()
formset = ForecastItemFormSet(instance=forecast)

class ForecastForm(forms.ModelForm):
    class Meta:
        model = Forecast
        fields = '__all__'
