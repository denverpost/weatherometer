# Server-specific stuff
MEDIA_URL = 'http://weather.s30304.gridserver.com/media'
#MEDIA_ROOT = '/home/30304/domains/postdev.s30304.gridserver.com/html/media/'
MEDIA_ROOT = '/home/30304/containers/django/weather/templates/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

#DEBUG = True
DEBUG = False
#TEMPLATE_DEBUG = DEBUG

SITE_URL = 'http://forecast.denverpost.com/'

# Sensitive stuff
DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'db24723_dj_weather'
DATABASE_USER = 'db24723'
DATABASE_PASSWORD = ''
DATABASE_HOST = 'internal-db.s24723.gridserver.com'


TEMPLATE_DIRS = ()

SECRET_KEY = ''

CACHE_MIDDLEWARE_SECONDS = 1200
CACHE_MIDDLEWARE_KEY_PREFIX = 'dpweather'
CACHE_BACKEND = 'memcached://10.2.140.69:2022/'
#CACHE_MIDDLEWARE_SECONDS = 10
#CACHE_BACKEND = 'file:///home2/freejoe76/dj_cache'
#CACHE_BACKEND = 'dummy:///'
