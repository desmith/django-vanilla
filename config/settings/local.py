from os.path import join

from .__base import *
from ._paths import *
from ._apps import INSTALLED_APPS
from ._middleware import (
  MIDDLEWARE_CLASSES,
  SERIALIZATION_MODULES,
  THUMBNAIL_FORMAT,
  STATICFILES_FINDERS,
  STATICFILES_STORAGE,
)

from ._templates import TEMPLATES
from ._cache import (
  ADV_CACHE_RESOLVE_NAME,
  SESSION_ENGINE,
  SESSION_CACHE_ALIAS,
  CACHE_COUNT_TIMEOUT,
  CACHE_TIMEOUT,
  CACHES,
)

from ._search import (
  HAYSTACK_SEARCH_RESULTS_PER_PAGE,
  HAYSTACK_SIGNAL_PROCESSOR,
  HAYSTACK_CONNECTIONS,
)

"""
from ._tinymce import (
  TINYMCE_JS_URL,
  TINYMCE_JS_ROOT,
  TINYMCE_DEFAULT_CONFIG,
  TINYMCE_DISABLE_CLEANING,
  TINYMCE_ALLOWED_TAGS,
  TINYMCE_ALLOWED_ATTRIBUTES,
  TINYMCE_ALLOWED_STYLES,
)
"""


from ._filebrowser import *
from ._logging import LOGGING
from ._debug_toolbar import (
  DEBUG_TOOLBAR_PATCH_SETTINGS,
  DEBUG_TOOLBAR_CONFIG,
  DEBUG_TOOLBAR_PANELS,
  MIDDLEWARE_CLASSES,
)

from ConfigParser import RawConfigParser


config = RawConfigParser()
config_file = '/etc/environments/local/{{project_name}}.ini'
config.read(config_file)

DEBUG = True
DEBUG_TOOLBAR = DEBUG
FILEBROWSER_DEBUG = False
TASTYPIE_FULL_DEBUG = DEBUG

def show_toolbar(request):
  if DEBUG and DEBUG_TOOLBAR:
    return True


TEST_RUNNER = 'django.test.runner.DiscoverRunner'
DEBUG_TOOLBAR_CONFIG['SHOW_TOOLBAR_CALLBACK'] = show_toolbar

PROJET_DOMAIN_NAME = '{{project_name}}.localhost'


### TinyMCE
TINYMCE_JS_URL = join(STATIC_URL, 'tiny_mce/tiny_mce.js')
TINYMCE_JS_ROOT = join(STATIC_ROOT, 'tiny_mce/')

### Filebrowser
ADMIN_MEDIA_PREFIX = STATIC_URL + 'grappelli/'
FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT
FILEBROWSER_MEDIA_URL = MEDIA_URL
FILEBROWSER_PATH_FILEBROWSER_MEDIA = join(STATIC_ROOT, 'filebrowser/')
FILEBROWSER_URL_FILEBROWSER_MEDIA = join(STATIC_URL, 'filebrowser/')
FILEBROWSER_URL_TINYMCE = join(STATIC_URL, 'grappelli/tinymce/jscripts/tiny_mce/')
FILEBROWSER_PATH_TINYMCE = join(STATIC_ROOT, 'grappelli/tinymce/jscripts/tiny_mce/')
### end Filebrowser

GRAPPELLI_ADMIN_TITLE = 'ISKCON News: The News Agency of the International Society for Krishna Consciousness'
GRAPPELLI_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
#GRAPPELLI_ADMIN_URL =

SECRET_KEY = config.get('django', 'SECRET_KEY')
CSRF_COOKIE_DOMAIN = SESSION_COOKIE_DOMAIN = None

INSTALLED_APPS += (
    'debug_toolbar',
    #'memcache_toolbar',
    #'haystack_panel',
)

ALLOWED_HOSTS = (
  PROJET_DOMAIN_NAME,
  u'localhost',
  '127.0.0.1',
)

INTERNAL_IPS = (
  '127.0.0.1',
)

SECURE_HSTS_INCLUDE_SUBDOMAINS = False

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

########## DATABASE CONFIGURATION
DATABASES['default']['NAME'] = config.get('database', 'DATABASE_NAME')
DATABASES['default']['USER'] = config.get('database', 'DATABASE_USER')
DATABASES['default']['PASSWORD'] = config.get('database', 'DATABASE_PASSWORD')
########## END DATABASE CONFIGURATION

########## CACHE CONFIGURATION
#CACHES['default']['BACKEND'] = 'django.core.cache.backends.dummy.DummyCache'
CACHES['default']['LOCATION'] = config.get('cache', 'REDIS_URL')
CACHES['default']['KEY_PREFIX'] = config.get('cache', 'KEY_PREFIX')
########## END CACHE CONFIGURATION

########## SEARCH CONFIGURATION
HAYSTACK_CONNECTIONS['default']['INDEX_NAME'] = config.get('search', 'INDEX_NAME')
HAYSTACK_CONNECTIONS['default']['URL'] = config.get('search', 'URL')
########## END SEARCH CONFIGURATION

## URL Shortener
#BITLY_ACCESS_TOKEN = config.get('api_keys', 'BITLY_ACCESS_TOKEN')

### Twitter
#TWITTER_CONSUMER_KEY = config.get('api_keys', 'TWITTER_CONSUMER_KEY')
#TWITTER_CONSUMER_SECRET = config.get('api_keys', 'TWITTER_CONSUMER_SECRET')
#TWITTER_ACCESS_TOKEN = config.get('api_keys', 'TWITTER_ACCESS_TOKEN')
#TWITTER_ACCESS_TOKEN_SECRET = config.get('api_keys', 'TWITTER_ACCESS_TOKEN_SECRET')
#TWITTER_OWNER_ID = config.get('api_keys', 'TWITTER_OWNER_ID')

### Facebook
#FACEBOOK_APP_ID = config.get('api_keys', 'FACEBOOK_APP_ID')
#FACEBOOK_APP_SECRET = config.get('api_keys', 'FACEBOOK_APP_SECRET')

# TIP: How different are your settings from the Django defaults?
#  run the 'diffsettings' management command.


MIDDLEWARE_CLASSES += (
  #'services.middleware.ResponseLoggingMiddleware',
)
