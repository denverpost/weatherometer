from django.conf import settings
from django import template
from django.contrib.contenttypes.models import ContentType
from django.template import Library, Node, TemplateSyntaxError, resolve_variable
#from forecaster.models import *
from forecast.models import *
from datetime import datetime, timedelta
register = template.Library()

def multiply(value, factor):
    "Removes all underscores from the given string and replace them with a space"
    return float(value * float(factor))
    #return value
register.filter(multiply)

"""
forecaster = Forecaster.objects.get(pk=2)
items = ForecastItem.objects.filter(differential__isnull=False, items__forecaster=forecaster)
diffs = [row.differential_abs for row in items]
avg = float(sum(d)) / len(d)
correct = d.count(0)
correctratio = float(d.count(0)) / len(d)
"""
class AccuracyForForecasterNode(Node):
    def __init__(self, forecaster, type, context_var):
        self.forecaster = forecaster
        self.type = type
        self.context_var = context_var

    def render(self, context):
        type = resolve_variable(self.type, '')
        forecaster = resolve_variable(self.forecaster, context)

        if type == 'all':
            items = ForecastItem.objects.filter(differential__isnull=False, items__forecaster=forecaster)
        elif type == 'week':
            date = datetime.today().date() - timedelta(7)
            items = ForecastItem.objects.filter(items__date__gte=date, differential__isnull=False, items__forecaster=forecaster)
        elif type == 'month':
            date = datetime.today().date() - timedelta(30)
            items = ForecastItem.objects.filter(items__date__gte=date, differential__isnull=False, items__forecaster=forecaster)

        diffs, diffs_high, diffs_low = [], [], []
        if len(items) > 0:
            for row in items:
                diffs += [row.differential_abs]
                if row.type > 0:
                    diffs_high += [row.differential_abs]
                elif row.type < 0:
                    diffs_low += [row.differential_abs]


            if len(diffs_low) > 0:
                avg_low = float(sum(diffs_low)) / len(diffs_low)
                correct_low = diffs_low.count(0)
                correctratio_low = float(diffs_low.count(0)) / len(diffs_low)
            
            if len(diffs_high) > 0:
                avg_high = float(sum(diffs_high)) / len(diffs_high)
                correct_high = diffs_high.count(0)
                correctratio_high = float(diffs_high.count(0)) / len(diffs_high)

            avg = float(sum(diffs)) / len(diffs)
            correct = diffs.count(0)
            count = len(diffs)
            count_high = len(diffs_high)
            count_low = len(diffs_low)
            correctratio = float(diffs.count(0)) / len(diffs)
    
            context[self.context_var] = { 'diffs': diffs, 'avg': avg, 'correct': correct, 'count': count, 'correctratio': correctratio }
        return ''

def do_accuracy_for_forecaster(parser, token):
    """
    Retrieves a list of ``ForecastItem`` objects from a particular day and
    stores them in a context variable.

    Example usage::

        {% accuracy_for_forecaster forecaster type(all/week/month) as item %}
    """
    bits = token.contents.split()
    if len(bits) != 5:
        raise TemplateSyntaxError('%s tag requires exactly four arguments' % bits[0])
    if bits[3] != 'as':
        raise TemplateSyntaxError("second argument to %s fan must be 'as'" % bits[0])
    return AccuracyForForecasterNode(bits[1], bits[2], bits[4])

register.tag('accuracy_for_forecaster', do_accuracy_for_forecaster)



"""
class AccuracyListForForecasterNode(Node):
    def __init__(self, forecaster, type, context_var):
        self.forecaster = forecaster
        self.type = type
        self.context_var = context_var
        self.items = ''
        self.date = ''


    def get_items(self):
        if self.date <> False:
            returnit = ForecastItem.objects.filter(items__date__gte=self.date, differential__isnull=False, items__forecaster=self.forecaster)
        else:
            returnit = ForecastItem.objects.filter(differential__isnull=False, items__forecaster=self.forecaster)
        returnit = ForecastItem.objects.filter(differential__isnull=False, items__forecaster=self.forecaster)
        
        return returnit

    def render(self, context):
        self.type = resolve_variable(self.type, '')
        self.forecaster = resolve_variable(self.forecaster, context)

        if type == 'all':
            self.date = False
            self.items = get_items()
        elif type == 'week':
            self.date = datetime.today().date() - timedelta(7)
            self.items = get_items()
        elif type == 'month':
            self.date = datetime.today().date() - timedelta(30)
            self.items = get_items()

        diffs = [row.differential_abs for row in self.items]
        avg = float(sum(diffs)) / len(diffs)
        correct = diffs.count(0)
        count = len(diffs)
        correctratio = float(diffs.count(0)) / len(diffs)
        

        context[self.context_var] = diffs, diffs
        return ''
"""

class AccuracyListForForecasterNode(Node):
    def __init__(self, forecaster, type, context_var):
        self.forecaster = forecaster
        self.type = type
        self.context_var = context_var

    def render(self, context):
        type = resolve_variable(self.type, '')
        forecaster = resolve_variable(self.forecaster, context)

        if type == 'all':
            items = ForecastItem.objects.filter(differential__isnull=False, items__forecaster=forecaster)
        elif type == 'week':
            date = datetime.today().date() - timedelta(7)
            items = ForecastItem.objects.filter(items__date__gte=date, differential__isnull=False, items__forecaster=forecaster)
        elif type == 'month':
            date = datetime.today().date() - timedelta(30)
            items = ForecastItem.objects.filter(items__date__gte=date, differential__isnull=False, items__forecaster=forecaster)

        #diffs = [row.differential_abs for row in items]
        diffs, diffs_high, diffs_low = [], [], []
        for row in items:
            diffs += [row.differential_abs]
            if row.type > 0:
                diffs_high += [row.differential_abs]
            elif row.type < 0:
                diffs_low += [row.differential_abs]

        avg = float(sum(diffs)) / len(diffs)
        avg_high = float(sum(diffs_high)) / len(diffs_high)
        avg_low = float(sum(diffs_low)) / len(diffs_low)

        correct = diffs.count(0)
        correct_high = diffs_high.count(0)
        correct_low = diffs_low.count(0)

        count = len(diffs)
        count_high = len(diffs_high)
        count_low = len(diffs_low)

        correctratio = float(diffs.count(0)) / len(diffs)
        correctratio_high = float(diffs_high.count(0)) / len(diffs_high)
        correctratio_low = float(diffs_low.count(0)) / len(diffs_low)
        

        context[self.context_var] = diffs_high,diffs_low
        return ''

def do_accuracy_list_for_forecaster(parser, token):
    """
    Retrieves a list of ``ForecastItem`` objects from a particular day and
    stores them in a context variable.

    Example usage::

        {% accuracy_list_for_forecaster forecaster type(all/week/month) as item %}
    """
    bits = token.contents.split()
    if len(bits) != 5:
        raise TemplateSyntaxError('%s tag requires exactly four arguments' % bits[0])
    if bits[3] != 'as':
        raise TemplateSyntaxError("second argument to %s must be 'as'" % bits[0])
    return AccuracyListForForecasterNode(bits[1], bits[2], bits[4])

register.tag('accuracy_list_for_forecaster', do_accuracy_list_for_forecaster)

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

class AccuracyListNode(Node):
    def __init__(self, type, context_var):
        self.type = type
        self.context_var = context_var

    def render(self, context):
        type = resolve_variable(self.type, '')
        #forecaster = resolve_variable(self.forecaster, context)

        if type == 'all':
            type = 1
        elif type == 'week':
            type = 2
        elif type == 'month':
            type = 3
        
        items = AccuracyRating.objects.filter(type__exact=type, daytype__exact=-1).order_by('avg')

        context[self.context_var] = items
        return ''

def do_accuracy_list(parser, token):
    """
    Retrieves a list of ``AccuracyRating`` objects from a particular day and
    stores them in a context variable.

    Example usage::

        {% accuracy_list type(all/week/month) as list %}
    """
    bits = token.contents.split()
    if len(bits) != 4:
        raise TemplateSyntaxError('%s tag requires exactly three arguments' % bits[0])
    if bits[2] != 'as':
        raise TemplateSyntaxError("second argument to %s must be 'as'" % bits[0])
    return AccuracyListNode(bits[1], bits[3])

register.tag('accuracy_list', do_accuracy_list)


class AccuracyItemNode(Node):
    def __init__(self, type, context_var):
        self.type = type
        self.context_var = context_var

    def render(self, context):
        type = resolve_variable(self.type, '')

        if type == 'all':
            type = 1
        elif type == 'week':
            type = 2
        elif type == 'month':
            type = 3
        
        item_high = AccuracyRating.objects.filter(type__exact=type, daytype__exact=-1).order_by('avg')[0:1]
        item_low = AccuracyRating.objects.filter(type__exact=type, daytype__exact=-1).order_by('-avg')[0:1]
        context[self.context_var] = { 'high': item_high, 'low': item_low }
        return ''

def do_accuracy_item(parser, token):
    """
    Retrieves a list of ``AccuracyRating`` objects from a particular day and
    stores them in a context variable.

    Example usage::

        {% accuracy_item type(all/week/month) as list %}
    """
    bits = token.contents.split()
    if len(bits) != 4:
        raise TemplateSyntaxError('%s tag requires exactly three arguments' % bits[0])
    if bits[2] != 'as':
        raise TemplateSyntaxError("second argument to %s must be 'as'" % bits[0])
    return AccuracyListNode(bits[1], bits[3])

register.tag('accuracy_item', do_accuracy_item)