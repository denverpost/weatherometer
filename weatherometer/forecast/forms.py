from django import forms
from models import Forecast, ForecastItem
from django.conf import settings

class ForecastForm(forms.ModelForm):
    class Meta:
        model = Forecast
        fields = '__all__'
