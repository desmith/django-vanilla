"""Development settings and globals."""
from .base import *
from .logging import *

from ConfigParser import RawConfigParser

config = RawConfigParser()
config_file = '/etc/environments/local/{{project_name}}.org.ini'
config.read(config_file)

DEBUG = True

SECRET_KEY = config.get('django', 'SECRET_KEY')
CSRF_COOKIE_DOMAIN = config.get('django', 'CSRF_COOKIE_DOMAIN')

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
TEMPLATES[0]['OPTIONS']['loaders'] = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
]


ALLOWED_HOSTS = ['{{project_name}}.localhost',
                 'localhost',
                 '127.0.0.1',
                 ]

########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES['default']['NAME'] = config.get('database', 'DATABASE_NAME')
DATABASES['default']['USER'] = config.get('database', 'DATABASE_USER')
DATABASES['default']['PASSWORD'] = config.get('database', 'DATABASE_PASSWORD')
########## END DATABASE CONFIGURATION

STATICFILES_STORAGE = COMPRESS_STORAGE = config.get('storage', 'STATICFILES_STORAGE')

STATIC_URL = '/static/'
COMPRESS_URL = STATIC_URL

########## TOOLBAR CONFIGURATION
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INSTALLED_APPS += (
    'debug_toolbar',
)

########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES['default']['LOCATION'] = config.get('cache', 'REDIS_URL')
CACHES['default']['KEY_PREFIX'] = config.get('cache', 'KEY_PREFIX')
########## END CACHE CONFIGURATION

########## SEARCH CONFIGURATION
HAYSTACK_CONNECTIONS['default']['INDEX_NAME'] = config.get('search', 'INDEX_NAME')
HAYSTACK_CONNECTIONS['default']['URL'] = config.get('search', 'URL')
########## END SEARCH CONFIGURATION


#DEBUG_TOOLBAR_CONFIG = {"INTERCEPT_REDIRECTS": False}
DEBUG_TOOLBAR_PANELS = (
  'debug_toolbar.panels.timer.TimerPanel',
  'debug_toolbar.panels.settings.SettingsPanel',
  'debug_toolbar.panels.headers.HeadersPanel',
  'debug_toolbar.panels.request.RequestPanel',
  'debug_toolbar.panels.sql.SQLPanel',
  'debug_toolbar.panels.templates.TemplatesPanel',
  'debug_toolbar.panels.versions.VersionsPanel',
  'debug_toolbar.panels.staticfiles.StaticFilesPanel',
  'debug_toolbar.panels.cache.CachePanel',
  'debug_toolbar.panels.signals.SignalsPanel',
  'debug_toolbar.panels.logging.LoggingPanel',
  'debug_toolbar.panels.redirects.RedirectsPanel',
)

MIDDLEWARE_CLASSES += (
  'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# TIP: How different are your settings from the Django defaults?
#  run the 'diffsettings' management command.
