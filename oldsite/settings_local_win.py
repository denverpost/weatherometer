# Server-specific stuff
MEDIA_ROOT = 'C:\django\weather\templates\media'
MEDIA_URL = 'http://localhost/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'dev.db'
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_PORT = ''

TEMPLATE_DIRS = (
    '/django/weather/templates/',
)

SECRET_KEY = ''

SITE_URL = 'http://localhost/'

CACHE_MIDDLEWARE_SECONDS = 10
#CACHE_BACKEND = 'file:///home2/freejoe76/dj_cache'
CACHE_BACKEND = 'dummy:///'
