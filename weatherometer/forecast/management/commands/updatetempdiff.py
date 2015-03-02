from django.core.management.base import BaseCommand, CommandError
from forecast.models import *

class Command(BaseCommand):
    """This command does two major actions:
    
    1. Take the ForecastItem records with dates no more recent than yesterday --
    those are the only ones we could be updating.
    
    2. Take the ActualTemperature records with dates that match the ForecastItem
    dates. Compare the temperatures. Take the result and add it to the ForecastItem
    differential field, and then save it.
    """
    help = """Updates the "differential" field of the weather ForecastItem model
    with how far off the forecast was from the actual temperature."""
    args = '[appname ...]'

    def handle(self, *app_labels, **options):
        from django.db.models import get_app, get_apps, get_models
        from django.conf import settings
        from datetime import datetime, timedelta
        
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
