from django.db import models
from datetime import datetime
import xmlrpclib
from django.contrib.sitemaps import ping_google
from comment_utils.moderation import CommentModerator, moderator

# Models
class Category(models.Model):
    # Basic info
    name = models.CharField(max_length=200, core=True)
    slug = models.SlugField(prepopulate_from=('name',))
    description = models.TextField(help_text="This is displayed on the list of posts in this category", null=True, blank=True)
    # Dates
    date_created = models.DateTimeField(auto_now_add=True)

    class Admin:
        ordering = ['-name']
        list_display = ('name', 'slug', 'date_created', 'description',)
        list_filter = ('date_created',)
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return "/news/category/%s/" % (self.slug)

    class Meta:
        verbose_name_plural = "Categories"

class Article(models.Model):
    # Basic info
    name = models.CharField(max_length=200, core=True)
    slug = models.SlugField(prepopulate_from=('name',), unique=True)
    # Details
    intro = models.TextField(help_text="This is displayed on the news index")
    body = models.TextField(help_text="Use Markdown syntax.")
    #body_html = models.TextField(help_text="This is the HTML displayed on the actual article", blank=True, null=True)
    summary = models.TextField(help_text="This is displayed on the sidebar of the actual entry")
    pull_quote = models.TextField(null=True, blank=True, help_text="If you want to highlight a sentence from this entry, paste it here and it will show up in a quote box on the entry")
    # Images
    supplementary_image = models.ImageField(upload_to='images/news-posts/supplementary/', null=True, blank=True, help_text="For adding images that aren't about existing photos or videos")
    supplementary_thumbnail = models.ImageField(upload_to='images/news-posts/supplementary/', null=True, blank=True, help_text="For thumbnails cropped differently than the supplementary image.")
    image_hide = models.BooleanField(default=True, null=True, blank=True, help_text="This hides the supplementary image on articles")
    # Dates
    date_created = models.DateTimeField(auto_now_add=True)
    ##published = models.DateTimeField()
    date_modified = models.DateTimeField(auto_now=True)
    # Related
    location = models.ForeignKey(Location, edit_inline=False, null=True, blank=True, num_in_admin=0)
    #tags = models.ManyToManyField(Tag, filter_interface=models.TABULAR, null=True, blank=True)
    category = models.ManyToManyField(Category, filter_interface=models.TABULAR)
    tag = TagField(null=True, blank=True)
    photo = models.ManyToManyField(Photo, filter_interface=models.TABULAR, null=True, blank=True, help_text="If this article is about a photo or two, select it / them here")
    video = models.ManyToManyField(Video, filter_interface=models.TABULAR, null=True, blank=True, help_text="If this article is about a video or two, select it / them here")
    band = models.ForeignKey(Band, edit_inline=False, null=True, blank=True)
    event = models.ForeignKey(Event, edit_inline=False, null=True, blank=True)
    # Misc
    enable_comments = models.BooleanField(default=True)
    is_live = models.BooleanField(default=True)
    
    # Manager calls
    objects = models.Manager()
    published_objects = PublishedManager()

    #Admin
    class Admin:
        ordering = ['-date_created']
        list_display = ('name', 'slug', 'date_created', 'is_live',)
        list_filter = ('date_created', 'date_modified', 'is_live', 'enable_comments')

    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/blog/%s/%s/" % (self.date_created.strftime("%Y/%b/%d").lower(), self.slug)

    def save(self):
        import markdown
        self.body_html = markdown.markdown(self.body)
        j = xmlrpclib.Server('http://rpc.technorati.com/rpc/ping')
        reply = j.weblogUpdates.ping('Weather-O-Meter Update','http://forecast.denverpost.com/')
        super(Article,self).save()
        try:
            ping_google()
        except Exception:
            # Bare 'except' because we could get a variety
            # of HTTP-related exceptions.
            pass

'''
class ArticleModerator(CommentModerator):
    akismet = True 
    email_notification = True
    enable_field = 'enable_comments'

moderator.register(Article, ArticleModerator)
'''