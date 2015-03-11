from django.db import models
from datetime import datetime, date, timedelta
from forecaster.models import *

TEMPERATURE_TYPE = (  
    (1, 'High'), 
    (-1, 'Low'), 
)

class Forecast(models.Model):
    forecaster = models.ForeignKey(Forecaster)
    date = models.DateField(default=datetime.today())

    class Meta:
        unique_together = ("forecaster", "date")

    class Admin:
        list_display = ('forecaster', 'date',)
        list_filter = ('forecaster', 'date',)
        save_on_top = True

    def __unicode__(self):
        return "%s: %s" % (self.forecaster, self.date.__str__())
    '''
    def save(self):
        """This does some light checking and field-writing to make the admin interface friendlier.
        """
        #ct = ContentType.objects.get(pk=self.content_type_id)
        #object = ct.get_object_for_this_type(id=self.object_id)
        #self.object_name = object.__str__()

        for item in self.forecastitem_set.all():
            item.date = item.get_forecast_date()

        super(Forecast, self).save()
    '''

class ForecastItem(models.Model):
    forecast_day = models.PositiveIntegerField()    #core=True
    temperature = models.IntegerField(null=True, blank=True)
    type = models.SmallIntegerField(default=1, choices=TEMPERATURE_TYPE)
    differential = models.IntegerField(max_length=3, editable=False, null=True, blank=True)
    differential_abs = models.PositiveIntegerField(max_length=3, editable=False, null=True, blank=True)
    items = models.ForeignKey(Forecast)
    # edit_inline=models.TABULAR, 
    #    min_num_in_admin=2, num_in_admin=20, num_extra_on_change=10, max_num_in_admin=30)
    date = models.DateField(blank=True, null=True)


    def get_forecast_date(self):
        from datetime import datetime, timedelta
        forecast_date = self.items.date + timedelta(self.forecast_day)
        return forecast_date
    date = property(get_forecast_date)

    class Admin:
        list_display = ('forecast_day', 'temperature', 'type', 'differential', 'date',)
        list_filter = ('forecast_day', 'temperature', 'type', 'differential',)
        save_on_top = True

    def __unicode__(self):
    	if self.temperature <> None:
        	return '%i: %s: %i' % (self.forecast_day, self.get_type_display(), self.temperature)
        else:
        	return '%i: %s: No temperature' % (self.forecast_day, self.get_type_display())

class ActualTemperature(models.Model):
    date = models.DateField(default=date.today() - timedelta(1))
    temperature_high = models.IntegerField(null=True, blank=True)
    temperature_low = models.IntegerField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, default=datetime.today(), null=True, blank=True)

    class Admin:
        list_display = ('date', 'temperature_high', 'temperature_low',)
        list_filter = ('date', 'temperature_high', 'temperature_low',)
        save_on_top = True

    def __unicode__(self):
        return "High %i, Low %i" % (self.temperature_high, self.temperature_low)

    def get_absolute_url(self):
        return "/forecast/%s/" % (self.date.strftime("%Y-%b-%d").lower())
