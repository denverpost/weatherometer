from django.conf import settings
#import settings
from django.contrib.syndication.feeds import Feed
from settings_guide import *
from list.models import *
from photo.models import *
from location.models import *
from django.contrib.comments.models import Comment, FreeComment
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

class ListFeed(Feed):
    title = SITE_TITLE + ": Recent Lists"
    link = SITE_URL + "lists/"
    description = "Guides to Colorado's good stuff."
    def items(self):
        return List.published_objects.order_by('-date_published')[:50]
    def item_pubdate(self, item):
        return item.date_added
    def item_author_name(self, item):
        return "%s %s" % (item.author.first_name,  item.author.last_name)
    def item_author_email(self, item):
        return item.author.email
    def item_author_link(self, item):
        return "%sauthors/%s" % (SITE_URL,  item.author.username)

class PhotoFeed(Feed):
    title = SITE_TITLE + ": Recent Photos"
    link = SITE_URL + "photos/"
    description = "Photos (of Colorado's good stuff)."
    def items(self):
        return Photo.objects.order_by('-date_published')[:50]
    def item_pubdate(self, item):
        return item.date_added
    def item_author_name(self, item):
        if item.author <> None:
            return "%s %s" % (item.author.first_name,  item.author.last_name)
        else:
            return "The Denver Post"
    def item_author_email(self, item):
        if item.author <> None:
            return item.author.email
        else:
            return ''
    def item_author_link(self, item):
        if item.author <> None:
            return "%sauthors/%s" % (SITE_URL,  item.author.username)
        else:
            return 'http://guide.denverpost.com/'


"""
class LatestTheoriesFeed(Feed):
    title = "Planck Studios: Photos"
    link = "http://planckstudios.com/photos/"
    description = "Latest photos posted at Planck Studios"
    def items(self):
        return Photo.objects.order_by('-created')[:25]
    def item_author_name(self, item):
        try:
            #return item.created
            return item.get_lost_user().get_display_name().encode("utf-8")
        except:
            return 'Unknown'
    def item_author_link(self, item):
        try:
            return item.get_lost_user().homepage.encode("utf-8")
        except:
            return 'None'
    def item_pubdate(self, item):
        return item.created
    item_author_email = "user@planckstudios.com"
"""