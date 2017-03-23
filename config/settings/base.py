import re
from sys import path
from os.path import dirname, join, normpath, realpath
from pyclbr import readmodule_ex
from django.utils.translation import ugettext_lazy as _

import sys
reload(sys)
sys.setdefaultencoding("utf8")

DEBUG = False

######### GENERAL CONFIGURATION
PROJECT_DIRNAME = "{{project_name}}"
TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
########## END GENERAL CONFIGURATION

##########
# PATH CONFIGURATION
##########
ROOT_URLCONF = 'config.urls'
CONF_DIR = dirname(realpath(__file__))
ROOT_DIR = realpath(dirname(__name__))
# Add our project to our pythonpath, this way we don't
# need to type our project name in our dotted import paths:
path.append(ROOT_DIR)

STATIC_ROOT = '/data/{{project_name}}/static/'
STATIC_SRC = join(ROOT_DIR, 'static')
STATIC_URL = '/static/'
ASSETS_ROOT = normpath(join(ROOT_DIR, 'assets'))
FILES_ROOT = "/data/{{project_name}}/media/files/"
FILES_URL = "/files/"
LOGIN_URL = "/admin/login"
MEDIA_ROOT = '/data/{{project_name}}/media/'
MEDIA_URL = '/media/'
FIXTURE_DIRS = (
  normpath(join(ROOT_DIR, 'fixtures')),
)
LOCALE_PATHS = (
  normpath(join(ROOT_DIR, 'locale')),
)
########## END PATH CONFIGURATION

########## MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
  ('Name', 'email@{{project_name}}.org'),
)
# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION

########## AUTHENTICATION BACKENDS
AUTHENTICATION_BACKENDS = (
  'django.contrib.auth.backends.ModelBackend',
)
########## END AUTHENTICATION BACKENDS

########## STATIC FILE CONFIGURATION
ADMIN_MEDIA_PREFIX = STATIC_URL
#ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
THUMBNAIL_FORMAT = 'png'
STATICFILES_FINDERS = [
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    ASSETS_ROOT,
    STATIC_SRC,
]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
########## END STATIC FILE CONFIGURATION

########## COMPRESSOR
COMPRESS_ENABLED = False
COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter', 'compressor.filters.cssmin.CSSMinFilter']
COMPRESS_OFFLINE = True
COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_STORAGE = STATICFILES_STORAGE
########## END COMPRESSOR
########## END STATIC FILE CONFIGURATION

# ######### SECURITY
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_BROWSER_XSS_FILTER = True
#SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 3600
SESSION_COOKIE_AGE = 1209600  # 2 weeks
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_NAME = 'sessionid'
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_DOMAIN = '.iskconnews.org'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_DOMAIN = SESSION_COOKIE_DOMAIN
CSRF_COOKIE_SECURE = SESSION_COOKIE_SECURE
CSRF_COOKIE_AGE = 31449600  # approx 1 year
# ######### END SECURITY

# ########## DATABASE CONFIGURATION
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': '',
    'USER': '',
    'PASSWORD': '',
    'HOST': 'localhost',
    'PORT': 5432,
    'ATOMIC_REQUESTS': True
  }
}
# ########## END DATABASE CONFIGURATION

########## EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 1025
EMAIL_HOST = '127.0.0.1'
DEFAULT_FROM_EMAIL = '[{{project_name}}] <noreply@{{project_name}}.org>'
EMAIL_SUBJECT_PREFIX = '[{{project_name}}]'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
########## END EMAIL CONFIGURATION

################
# APPLICATIONS #
################
DJANGO_APPS = (
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django.contrib.redirects',

  # grappelli and filebrowser MUST be before django-admin!

  # Uncomment the next line to enable the admin:
  'django.contrib.admin',

)

THIRD_PARTY_APPS = (
  'django_extensions',

)

# Apps specific for this project go here.
LOCAL_APPS = (

)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION

IGNORABLE_404_URLS = [
  #re.compile(r'^/$'),
  re.compile(r'^/archive/.*$'),
  re.compile(r'\.(php|cgi)$'),
  re.compile(r'^/phpmyadmin/'),
  re.compile(r'^/apple-touch-icon.*\.png$'),
  #re.compile(r'^/favicon\.ico$'),
  #re.compile(r'^/robots\.txt$'),
]


# ######### MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
########## END MIDDLEWARE CONFIGURATION

########## TEMPLATE CONFIGURATION
TEMPLATES = [
  {
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
    'BACKEND': 'django.template.backends.django.DjangoTemplates',

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    'DIRS': [
      normpath(join(ROOT_DIR, 'templates')),
    ],

    'OPTIONS': {
      # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
      'debug': DEBUG,

      # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
      'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.template.context_processors.i18n',
        'django.template.context_processors.media',
        'django.template.context_processors.static',
        'django.template.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        # Your stuff: custom template context processors go here
       ],

      # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
      # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
      'loaders': [
        ('django.template.loaders.cached.Loader', [
         'django.template.loaders.filesystem.Loader',
         'django.template.loaders.app_directories.Loader',
         ]),
       ],
    },
  },
]
########## END TEMPLATE CONFIGURATION

########## CACHE CONFIGURATION
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHE_COUNT_TIMEOUT = 60  # seconds, not too long.
CACHE_TIMEOUT = (60 * 60)
# ------------------------------------------------------------------------------
CACHES = {
  'default': {
    'BACKEND': 'django_redis.cache.RedisCache',
    'KEY_PREFIX': '{{project_name}}',
    # Heroku URL does not pass the DB number, so we parse it in
    'OPTIONS': {
      'CLIENT_CLASS': 'django_redis.client.DefaultClient',
      'MAX_ENTRIES': 10000,
      'IGNORE_EXCEPTIONS': True,  # mimics memcache behavior.
      # http://niwinz.github.io/django-redis/latest/#_memcached_exceptions_behavior
    }
  }
}
########## END CACHE CONFIGURATION

########## SEARCH CONFIGURATION
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 20
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_CONNECTIONS = {
  'default': {
    'INDEX_NAME': '{{project_name}}',
    'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
    'TIMEOUT': 60
  }
}
########## END SEARCH CONFIGURATION

########## FACEBOOK CONFIGURATION
FACEBOOK_REDIRECT_URI = 'https://www.facebook.com/connect/login_success.html'
# AUTH_USER_MODEL = 'django_facebook.FacebookCustomUser'
# AUTH_PROFILE_MODULE = 'django_facebook.FacebookProfile'
########## END FACEBOOK CONFIGURATION

########## WSGI CONFIGURATION
# Python dotted path to the WSGI application used by Django's runserver.
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'
########## END WSGI CONFIGURATION
