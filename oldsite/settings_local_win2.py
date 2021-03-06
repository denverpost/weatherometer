# Server-specific stuff
MEDIA_ROOT = '/home/joe/djang/weather/templates/media'
MEDIA_URL = 'http://localhost/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

DEBUG = True
#TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'dev.db'
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_PORT = ''

TEMPLATE_DIRS = (
    '/home/joe/djang/weather/templates/',
)

SECRET_KEY = ''

# Used in coordinates_field and hacked into geopy
# Get an api key: http://code.google.com/apis/maps/signup.html
# CoordinatesField: http://code.google.com/p/django-coordinatesfield/
# GeoPy: http://exogen.case.edu/projects/geopy/
MAP_API = 'google'
MAP_API_KEY = ''

SITE_URL = 'http://localhost/'

CACHE_MIDDLEWARE_SECONDS = 10
#CACHE_BACKEND = 'file:///home2/freejoe76/dj_cache'
CACHE_BACKEND = 'dummy:///'
