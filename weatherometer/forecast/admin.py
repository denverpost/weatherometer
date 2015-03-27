from forecast.models import Forecast, ForecastItem, ActualTemperature
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


class ForecastItem_Inline(admin.TabularInline):
    model = ForecastItem
    extra = 20


class ActualTemperatureOptions(admin.ModelAdmin):
    list_display = ('date', 'temperature_high', 'temperature_low',)
    list_filter = ('date', 'temperature_high', 'temperature_low',)
    save_on_top = True


class ForecastItemOptions(admin.ModelAdmin):
    list_display = ('forecast_day', 'temperature', 
        'type', 'differential', 'date',)
    list_filter = ('forecast_day', 'temperature', 'type', 'differential',)
    radio_fields = {'type': admin.VERTICAL}
    save_on_top = True


class ForecastOptions(admin.ModelAdmin):
    inlines = [ForecastItem_Inline]
    list_display = ('forecaster', 'date',)
    list_filter = ('forecaster', 'date',)
    save_on_top = True

admin.site.register(ActualTemperature, ActualTemperatureOptions)
admin.site.register(ForecastItem, ForecastItemOptions)
admin.site.register(Forecast, ForecastOptions)
