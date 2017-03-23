"""Development settings and globals."""
from .base import *
from .logging import *
from ConfigParser import RawConfigParser


config = RawConfigParser()
config_file = '/etc/environments/local/{{project_name}}.ini'
config.read(config_file)

DEBUG = True
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

SECRET_KEY = config.get('django', 'SECRET_KEY')
CSRF_COOKIE_DOMAIN = SESSION_COOKIE_DOMAIN = None

ALLOWED_HOSTS = [
  u'{{project_name}}.localhost',
  u'localhost',
  '127.0.0.1',
]

INTERNAL_IPS = [
  '127.0.0.1',
  '10.0.2.2',
]

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
TEMPLATES[0]['OPTIONS']['loaders'] = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
]

########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES['default']['NAME'] = config.get('database', 'DATABASE_NAME')
DATABASES['default']['USER'] = config.get('database', 'DATABASE_USER')
DATABASES['default']['PASSWORD'] = config.get('database', 'DATABASE_PASSWORD')
########## END DATABASE CONFIGURATION

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INSTALLED_APPS += (
    'debug_toolbar',
    #'memcache_toolbar',
    #'haystack_panel',
    #'redis_panel', (?)
)

########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
#CACHES['default']['BACKEND'] = 'django.core.cache.backends.dummy.DummyCache'
CACHES['default']['LOCATION'] = config.get('cache', 'REDIS_URL')
CACHE_COUNT_TIMEOUT = 60  # seconds, not too long.
CACHE_TIMEOUT = (60 * 60)
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_CACHE_ALIAS = 'default'
# ------------------------------------------------------------------------------
########## END CACHE CONFIGURATION

########## SEARCH CONFIGURATION
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
  #'haystack_panel.panel.HaystackDebugPanel',
  #'redis_panel.panel.RedisDebugPanel', (?)
)

MIDDLEWARE_CLASSES += (
  'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# TIP: How different are your settings from the Django defaults?
#  run the 'diffsettings' management command.
