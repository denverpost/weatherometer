from models import * 
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class ForecasterList(ListView):
    def get_queryset(self):
        return Forecaster.objects.all()
    #def list(request):
    #    return object_list(request,
    #        queryset=Forecaster.objects.all(),
    #        paginate_by=50, allow_empty=True)


class ForecasterDetail(DetailView):
    def get_queryset(self):
        return Forecaster.objects.all()
        #return DetailView(request,
        #    queryset=Forecaster.objects.all(),
        #    slug=slug, slug_field='slug')
