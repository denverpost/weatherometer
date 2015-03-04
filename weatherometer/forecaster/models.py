from django.db import models
from users.models import User
from datetime import datetime

ACCURACY_TYPE = (  
    (1, 'All'), 
    (2, 'Week'), 
    (3, 'Month'), 
    (4, 'Year'), 
    (5, 'Day'), 
    (6, 'Two-Week'), 
    (7, 'Three-Month'), 
    (8, 'Six-Month'), 
)
ACCURACY_DAYTYPE = (  
    (-1, 'All'), 
    (0, '0-day'), 
    (1, '1-day'), 
    (2, '2-day'), 
    (3, '3-day'), 
    (4, '4-day'), 
    (5, '5-day'), 
    (6, '6-day'), 
    (7, '7-day'), 
    (8, '8-day'), 
    (9, '9-day'), 
)
class AccuracyRating(models.Model):
    forecaster = models.ForeignKey('Forecaster')
    type = models.SmallIntegerField(default=1, choices=ACCURACY_TYPE)
    daytype = models.SmallIntegerField(default=1, choices=ACCURACY_DAYTYPE)
    avg = models.FloatField(default=0)
    avg_high = models.FloatField(default=0)
    avg_low = models.FloatField(default=0)

    correct = models.PositiveIntegerField(default=0)
    correct_high = models.PositiveIntegerField(default=0)
    correct_low = models.PositiveIntegerField(default=0)

    count = models.PositiveIntegerField(default=0)
    count_high = models.PositiveIntegerField(default=0)
    count_low = models.PositiveIntegerField(default=0)

    correctratio = models.FloatField(default=0)
    correctratio_high = models.FloatField(default=0)
    correctratio_low = models.FloatField(default=0)

    #def __unicode__(self):
    #    return "%i %i" % (self.type, self.daytype)
    def get_absolute_url(self):
        return "/forecaster/%s/today/" % ( self.forecaster.slug )

    class Admin:
        list_display = ('forecaster', 'type', 'daytype', 'avg', 'correct', 'count', 'correctratio')
        list_filter = ('forecaster', 'type', 'daytype', 'avg', 'correct', 'count', 'correctratio')


class AccuracyRatingArchive(AccuracyRating):
    date = models.DateField(default=datetime.today())
    class Admin:
        list_display = ('forecaster', 'date', 'type', 'daytype', 'avg', 'correct', 'count', 'correctratio')
        list_filter = ('forecaster', 'date', 'type', 'daytype', 'avg', 'correct', 'count', 'correctratio')

class Forecaster(models.Model):
    user = models.ForeignKey(User)
    slug = models.SlugField(unique=True)
    nickname = models.CharField(max_length=25, blank=True, null=True)
    call_letters = models.CharField(max_length=5, blank=True, null=True)
    is_professional = models.BooleanField(default=True)
    weather_url = models.URLField(blank=True, null=True)
    homepage_url = models.URLField(blank=True, null=True)

    class Admin:
        pass
        #list_display = ('forecaster', 'date',)
        #list_filter = ('forecaster', 'date',)

    def get_accuracy_week(self):
        from forecast.models import *
        from datetime import datetime, timedelta
        timediff = datetime.today() - timedelta(7)
        items = ForecastItem.objects.filter(items__forecaster=self, differential__isnull=False, items__date__gte=timediff)
        diffs = [row.differential_abs for row in items]
        dates = [row.date for row in items]
        
        return diffs

    def get_forecast_high(self, day=0):
        from forecast.models import *
        from datetime import datetime
        try:
            forecast = Forecast.objects.get(forecaster=self, date=datetime.now)
        except:
            forecast = 'hey'
        return forecast

    def get_forecastitem_today(self):
        from forecast.models import *
        from datetime import datetime
        try:
            high = ForecastItem.objects.get(items__forecaster=self, forecast_day=0, type=1, items__date=datetime.now)
            low = ForecastItem.objects.get(items__forecaster=self, forecast_day=1, type=-1, items__date=datetime.now)
        except:
            high = {'temperature': 1}
            low = {'temperature': 1}
        return (high.temperature, low.temperature)
    
    #def get_accuracy(self):

    def __unicode__(self):
        return "%s" % (self.nickname)
        
    def get_absolute_url(self):
        return "/forecaster/%s/" % ( self.slug )
