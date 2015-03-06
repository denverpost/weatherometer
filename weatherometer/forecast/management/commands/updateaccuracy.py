from django.core.management.base import BaseCommand, CommandError
from forecast.models import *
from forecaster.models import *
from forecast.forms import Updaters

class Command(BaseCommand):
    help = """Updates the "differential" field of the weather ForecastItem model
    with how far off the forecast was from the actual temperature."""
    args = '[appname ...]'

    def handle(self, *app_labels, **options):
        up = Updaters()
        up.update_accuracy()
