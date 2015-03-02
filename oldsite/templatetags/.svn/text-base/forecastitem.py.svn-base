from django.db import models
from django.conf import settings
from django import template
#from django.contrib.contenttypes.models import ContentType
from django.template import Library, Node, TemplateSyntaxError, resolve_variable
#from forecaster.models import *
#from forecast.models import *
from datetime import datetime, timedelta
register = template.Library()


class ForecastForDayNode(Node):
    def __init__(self, day, context_var):
        self.day = day
        self.context_var = context_var

    def render(self, context):
        from forecast.models import ForecastItem
        day = resolve_variable(self.day, 0)
        forecast_day = 0
        
        # For future / past forecasts (we pull past forecasts to display the forecasts' accuracy)
        if day < 0:
            forecast_day = day * -1
            day = 0
        
        date = datetime.today().date() - timedelta(day)

        try:
            items = ForecastItem.objects.filter(items__date=date, forecast_day=forecast_day)
        except:
            date = date - timedelta(1)
            items = ForecastItem.objects.filter(items__date=date, forecast_day=forecast_day)
        if len(items) == 0:
            date = date - timedelta(1)
            items = ForecastItem.objects.filter(items__date=date, forecast_day=forecast_day)
        #except:
        #    return
        #date = date - timedelta(1)
        #items = ForecastItem.objects.filter(items__date=date, forecast_day=forecast_day)
        #context[self.context_var] = { 'len': len(items), 'items': items }
        context[self.context_var] = items
        return ''

def do_forecast_for_day(parser, token):
    """
    Retrieves a list of ``ForecastItem`` objects from a particular day and
    stores them in a context variable.

    Example usage::

        {% forecast_for_day day_integer as item_list %}
    """
    bits = token.contents.split()
    if len(bits) != 4:
        raise TemplateSyntaxError('%s tag requires exactly three arguments' % bits[0])
    if bits[2] != 'as':
        raise TemplateSyntaxError("second argument to %s fan must be 'as'" % bits[0])
    return ForecastForDayNode(bits[1], bits[3])

register.tag('forecast_for_day', do_forecast_for_day)

'''
class ForecastItemListNode(template.Node):
    def __init__(self,varname):
        self.varname = varname

    def __repr__(self):
        return "<ForecastItemList Node>"

    def render(self, context):
        context[self.varname] = ForecastItem.objects.filter(date=True)
        return ''

class DoGetForecastItemList:
    """
    {% get_forecastitem_list as forecastitem_list %}
    """
    def __init__(self, tag_name):
        self.tag_name = tag_name

    def __call__(self, parser, token):
        bits = token.contents.split()
        if len(bits) != 3:
            raise template.TemplateSyntaxError, "'%s' tag takes two arguments" % bits[0]
        if bits[1] != "as":
            raise template.TemplateSyntaxError, "First argument to '%s' tag must be 'as'" % bits[0]
        return TripPhotoNode(bits[2])
register.tag('get_trip_photo', DoGetTripPhoto('get_trip_photo'))
'''