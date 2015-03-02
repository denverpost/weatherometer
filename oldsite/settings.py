# Django settings for Weather-O-Meter (weather) project.

# This pulls in the environment-specific variables
from settings_common import *
#from settings_local_pro import *
#from settings_local import *
import os.path
from settings_local_win import *
BASEDIR = os.path.dirname(__file__)
'''
if BASEDIR == 'T:\\django\\weather':
    from settings_local import *
else:
    from settings_local_pro import *
'''
SITE_ID = 2
SITE_TITLE = 'Weather-O-Meter'
DEFAULT_CHARSET = 'utf-8'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS += (
#     'django.core.context_processors.auth',
     'django.core.context_processors.request',
#     'django.core.context_processors.media',
#     'django.core.context_processors.debug',
)

MIDDLEWARE_CLASSES = (
#    'middleware.profiling.ProfileMiddleware',
#    'middleware.stats.StatsMiddleware',
#    'middleware.debugfooter.DebugFooter',
    'django.middleware.cache.CacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
#    'middleware.minidetector.Middleware',
#    'middleware.threadlocals.ThreadLocals',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
#    'django.middleware.cache.CacheMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS += (
    # Put strings here, like "/home/html/django_templates".
    # Always use forward slashes, even on Windows.
    #'/',
    '/home/30304/containers/django/weather/templates/',
    '/home/30304/data/python/django/django/contrib/admin/templates/',
    #'/templates/',
)

FIXTURE_DIRS = (
    #'/home/30304/containers/django/weather/fixtures/',
    #'/django/dj/fixtures/',
)

INSTALLED_APPS = (
    'forecast',
    'forecaster',
    'charts',
#    'tagging',
#    'django.contrib.comments',
#    'contact',
#    'templatetags',
#    'utils',    # See http://www.nyquistrate.com/django/orderedlist/
#    'genericadmin',
#    'template_utils',
#    'typogrify',
    'django.contrib.flatpages',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.markup',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'django.contrib.redirects',
    'django.contrib.databrowse',
)

#AUTHENTICATION_BACKENDS = (
#    'django.contrib.auth.backends.ModelBackend',
#)
INTERNAL_IPS = (
    '72.165.229.187',
    '127.0.0.1',
)
#AKISMET_API_KEY = ''
SEND_BROKEN_LINK_EMAILS = False
EMAIL_HOST = 'mail.postdev.com'
EMAIL_PORT = '25'
EMAIL_HOST_USER = 'admin@postdev.com'
EMAIL_HOST_PASSWORD = ''
#EMAIL_USE_TLS
DEFAULT_FROM_EMAIL = 'admin@denverpost.com'
SERVER_EMAIL = 'admin@denverpost.com'

"""
Added Modules Information:
===============================================
Google Chartwrapper:

http://code.google.com/p/google-chartwrapper/
/charts/
===============================================


===============================================
Database Dump:
Used to handle model field updates.
http://code.google.com/p/db-dump/
/db_dump.py
===============================================
Help:
 python db_dump.py -h

Dumping the database:
 cddj
 python db_dump.py --settings=settings_guide dump

Resetting a model, after changes are made to its fields:
 python db_dump.py --settings=settings_guide load [applist]

===============================================
RSysLog:
Used to handle model field updates.
http://www.rsyslog.com/doc-install.html
/home/30304/data/rsyslog-3.14.0

Installation:
 ./configure --enable-mysql
 make
===============================================


===============================================
Minidetector:
This application is a simple middleware and associated decorator that will add a ".mobile" attribute to your request objects, which, if True, means the requester is coming to you from a mobile phone (cellphone), PDA, or other device that should be considered small screened, or have an underpowered browser, such as games consoles.
http://code.google.com/p/minidetector/
===============================================


===============================================
Robots:
This is a basic Django application to manage robots.txt files following the robots exclusion protocol, complementing the Django Sitemap contrib app.
http://code.google.com/p/django-robots/
===============================================


python manage.py reset facility list daytrip photo pageview fan
python db_dump.py load facility list daytrip photo pageview fan
"""
