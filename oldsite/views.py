from django.conf import settings
from django.contrib.comments.views.comments import post_free_comment
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.template import Context, loader
# For search functionality
from django.db.models import Q
from django.shortcuts import render_to_response
# Models
from django.contrib.comments.models import Comment
import string


def my_post_free_comment(request):
    if request.POST.has_key('url'):
        url = request.POST['url']
    else:
        url = '/comments/posted'
    response = post_free_comment(request)
    return HttpResponseRedirect(url)

def sorter(left, right):
    return cmp(left.date_updated, right.date_updated)

def my_post_free_comment(request):
    if request.POST.has_key('url'):
        url = request.POST['url']
    else:
        url = '/comments/posted.html'
    response = post_free_comment(request)
    return HttpResponseRedirect(url)

def mobilesniffer(request):
    t = loader.get_template('screenscrape/mobilesniffer.html')
    c = Context({
        'request': request,
    })
    return HttpResponse(t.render(c))
