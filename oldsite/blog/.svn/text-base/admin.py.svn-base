from blog.models import Category, Article
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

class Article_Inline(admin.StackedInline):
    model = Article
    extra = 0

class Article_Inline(admin.StackedInline):
    model = Article

class Article_Inline(admin.StackedInline):
    model = Article

class CategoryOptions(admin.ModelAdmin):
    ordering = ['-name']
    list_display = ('name', 'slug', 'date_created', 'description',)
    list_filter = ('date_created',)
    prepopulated_fields = {'slug': ('name',)}

# class BandOptions(admin.ModelAdmin):
#     inlines = [Article_Inline]

# class LocationOptions(admin.ModelAdmin):
#     inlines = [Article_Inline]

class ArticleOptions(admin.ModelAdmin):
    ordering = ['-date_created']
    list_display = ('name', 'slug', 'date_created', 'is_live',)
    list_filter = ('date_created', 'date_modified', 'is_live', 'enable_comments')
    prepopulated_fields = {'slug': ('name',)}

# class EventOptions(admin.ModelAdmin):
#     inlines = [Article_Inline]

admin.site.register(Category, CategoryOptions)
admin.site.register(Article, ArticleOptions)

