from forecaster.models import AccuracyRating, AccuracyRatingArchive, Forecaster
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

class ForecasterOptions(admin.ModelAdmin):
    #list_display = ('forecaster', 'date',)
    #list_filter = ('forecaster', 'date',)
    prepopulated_fields = {'slug': ("user",)}

class AccuracyRatingOptions(admin.ModelAdmin):
    list_display = ('forecaster', 'type', 'daytype', 'avg', 'correct', 'count', 'correctratio')
    list_filter = ('forecaster', 'type', 'daytype', 'avg', 'correct', 'count', 'correctratio')
    radio_fields = {'type': admin.VERTICAL, 'daytype': admin.VERTICAL}


class AccuracyRatingArchiveOptions(admin.ModelAdmin):
    list_display = ('forecaster', 'date', 'type', 'daytype', 'avg', 'correct', 'count', 'correctratio')
    list_filter = ('forecaster', 'date', 'type', 'daytype', 'avg', 'correct', 'count', 'correctratio')

admin.site.register(Forecaster, ForecasterOptions)
admin.site.register(AccuracyRating, AccuracyRatingOptions)
admin.site.register(AccuracyRatingArchive, AccuracyRatingArchiveOptions)

