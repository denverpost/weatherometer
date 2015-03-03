from django.conf import settings
from django import template
from django.contrib.contenttypes.models import ContentType
from django.template import Library, Node, TemplateSyntaxError, resolve_variable
#from forecaster.models import *
from forecast.models import *
from datetime import datetime, timedelta
register = template.Library()


@register.inclusion_tag('templatetags/actualtemperature_item.html')
def get_actualtemperature_item(day=1):
    date = datetime.today().date() - timedelta(day)
    try:
        item = ActualTemperature.objects.get(date=date)
    except:
        return
    return {'item': item,}
    
class TemperatureItemNode(Node):
    def __init__(self, type, context_var):
        self.type = type
        self.context_var = context_var

    def render(self, context):
        type = resolve_variable(self.type, '')
        
        if type == 'today':
            type = 1
        elif type == 'yesterday':
            type = 2
        elif type == 'month':
            type = 3
        dater = datetime.today().date() - timedelta(1)
        yesterday = datetime.today() - timedelta(1)
        try:
            item = ActualTemperature.objects.get(date_added__gte=yesterday, date__gte=dater)
        except:
            return ''

        context[self.context_var] = item
        return ''

def do_temperature_item(parser, token):
    """
    Retrieves a list of ``ActualTemperature`` objects from a particular day and
    stores them in a context variable.

    Example usage::

        {% temperature_item type(today/yesterday) as item %}
    """
    bits = token.contents.split()
    if len(bits) != 4:
        raise TemplateSyntaxError('%s tag requires exactly three arguments' % bits[0])
    if bits[2] != 'as':
        raise TemplateSyntaxError("second argument to %s must be 'as'" % bits[0])
    return TemperatureItemNode(bits[1], bits[3])

register.tag('temperature_item', do_temperature_item)
