from django.shortcuts import get_object_or_404, render_to_response
from django.template import Context, loader
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
"""
def index(request):
    #sitedata = SiteData.objects.all()
    nowplaying_list = Movie.objects.filter(
        start_date__lte=datetime.now()).filter(
            end_date__gte=datetime.now())
    comingsoon_list = Movie.objects.filter(
        start_date__gte=datetime.now()).filter(
            specialevent__exact=0)
    specialevents_list = Movie.objects.filter(
        start_date__gte=datetime.now()).filter(
            specialevent__exact=1)
    showtime_object = SiteMeta.objects.get(slug__exact='show-time')
    t = loader.get_template('theater/index.html')
    c = Context({
        'specialevents_list': specialevents_list,
        'nowplaying_list': nowplaying_list,
        'comingsoon_list': comingsoon_list,
        'showtime_object': showtime_object,
    })
    return HttpResponse(t.render(c))
"""
def detail(request, slug):
    category_item = Category.objects.get(slug__exact=slug)
    article_list = Article.objects.filter(category__slug__exact=slug)
    #return HttpResponse(slug)
    #article_list = Article.objects.all()
    t = loader.get_template('news/category_detail.html')
    c = Context({
        'category_item': category_item,
        'article_list': article_list,
    })
    return HttpResponse(t.render(c))

