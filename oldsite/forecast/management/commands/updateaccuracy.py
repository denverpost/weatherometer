from django.core.management.base import BaseCommand, CommandError
from forecast.models import *
from forecaster.models import *

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
        
        ratings = AccuracyRating.objects.all()
        i = 0
        for item in ratings:
            if item.type == 1:
                if item.daytype >= 0:
                    items = ForecastItem.objects.filter(differential__isnull=False, items__forecaster=item.forecaster, forecast_day=item.daytype)
                else:
                    items = ForecastItem.objects.filter(differential__isnull=False, items__forecaster=item.forecaster)
            else:
                if item.type == 2:
                    date = datetime.today().date() - timedelta(7)
                elif item.type == 3:
                    date = datetime.today().date() - timedelta(30)
                elif item.type == 4:
                    date = datetime.today().date() - timedelta(365)
                elif item.type == 5:
                    date = datetime.today().date() - timedelta(1)
                elif item.type == 6:
                    date = datetime.today().date() - timedelta(14)
                elif item.type == 7:
                    date = datetime.today().date() - timedelta(91)
                elif item.type == 8:
                    date = datetime.today().date() - timedelta(182)
                if item.daytype >= 0:
                    items = ForecastItem.objects.filter(items__date__gte=date, differential__isnull=False, items__forecaster=item.forecaster, forecast_day=item.daytype)
                else:
                    items = ForecastItem.objects.filter(items__date__gte=date, differential__isnull=False, items__forecaster=item.forecaster)
            if len(items) > 0:
                print len(items)
                print items
                diffs, diffs_high, diffs_low = [], [], []
                for row in items:
                    diffs += [row.differential_abs]
                    if row.type > 0:
                        diffs_high += [row.differential_abs]
                    elif row.type < 0:
                        diffs_low += [row.differential_abs]
                item.avg = float(sum(diffs)) / len(diffs)
                item.correct = diffs.count(0)
                item.count = len(diffs)
                item.correctratio = float(diffs.count(0)) / len(diffs)
                if len(diffs_high) > 0:
                    item.avg_high = float(sum(diffs_high)) / len(diffs_high)
                    item.correct_high = diffs_high.count(0)
                    item.count_high = len(diffs_high)
                    item.correctratio_high = float(diffs_high.count(0)) / len(diffs_high)
                if len(diffs_low) > 0:
                    item.correct_low = diffs_low.count(0)
                    item.avg_low = float(sum(diffs_low)) / len(diffs_low)
                    item.count_low = len(diffs_low)
                    item.correctratio_low = float(diffs_low.count(0)) / len(diffs_low)
                
                item.save()
                archive = AccuracyRatingArchive(forecaster=item.forecaster, date=datetime.today(), type = item.type, daytype = item.daytype, avg = item.avg, avg_high = item.avg_high, avg_low = item.avg_low, correct = item.correct, correct_high = item.correct_high, correct_low = item.correct_low, count = item.count, count_high = item.count_high, count_low = item.count_low, correctratio = item.correctratio, correctratio_high = item.correctratio_high, correctratio_low = item.correctratio_low)
                archive.save()
                i = i + 1

        
        print '\n items updated. %i records updated' % ( i )
