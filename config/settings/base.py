import re
from os.path import dirname, join, normpath, realpath
from sys import path
from django.utils.translation import ugettext_lazy as _

# Name of the directory for the project.
PROJECT_DIRNAME = "{{project_name}}"

CONF_DIR = dirname(realpath(__file__))
ROOT_DIR = realpath(dirname(__name__))
APPS_DIR = join(ROOT_DIR, PROJECT_DIRNAME)

########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False
########## END DEBUG CONFIGURATION

#########
# PATHS #
#########

########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
#DJANGO_ROOT = dirname(dirname(abspath(__file__)))
# Absolute filesystem path to the top-level project folder:
#SITE_ROOT = dirname(DJANGO_ROOT)
# Site name:
#SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(ROOT_DIR)
########## END PATH CONFIGURATION

LOCALE_PATHS = (
  normpath(join(ROOT_DIR, 'locale')),
)

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

########## MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
  ('Name', 'email@{{project_name}}.org'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION

########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 1025
EMAIL_HOST = '127.0.0.1'
DEFAULT_FROM_EMAIL = '[{{project_name}}] <noreply@{{project_name}}.org>'
EMAIL_SUBJECT_PREFIX = '[{{project_name}}]'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
########## END EMAIL CONFIGURATION

########## GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
#
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
########## END GENERAL CONFIGURATION

LOGIN_URL = "/admin/login"
########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = '/data/{{project_name}}/static/'
STATIC_SRC = join(ROOT_DIR, 'static')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
#STATIC_URL = 'http://d29gd5sqnzhdax.cloudfront.net/'
STATIC_URL = '/static/'

ASSETS_ROOT = normpath(join(ROOT_DIR, 'assets'))

FILES_ROOT = "/data/{{project_name}}/media/files/"
FILES_URL = "/files/"

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    ASSETS_ROOT,
    STATIC_SRC,
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
########## END STATIC FILE CONFIGURATION

########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = '/data/{{project_name}}/media/'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

########## END MEDIA CONFIGURATION




# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".

########## URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = 'config.urls'
########## END URL CONFIGURATION

# Tuple of IP addresses, as strings, that:
#   * See debug comments, when DEBUG is true
#   * Receive x-headers
#INTERNAL_IPS = ("127.0.0.1",)

########## FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
  normpath(join(APPS_DIR, 'fixtures')),
)
########## END FIXTURE CONFIGURATION

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
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


)

# Apps specific for this project go here.
LOCAL_APPS = (

)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION


IGNORABLE_404_URLS = (
  #re.compile(r'^/$'),
  re.compile(r'^/archive/.*$'),
  re.compile(r'\.(php|cgi)$'),
  re.compile(r'^/phpmyadmin/'),
  re.compile(r'^/apple-touch-icon.*\.png$'),
  #re.compile(r'^/favicon\.ico$'),
  #re.compile(r'^/robots\.txt$'),
)


#adminfiles
THUMBNAIL_FORMAT = 'png'

########################
# FILEBROWSER SETTINGS #
########################

# PATH AND URL SETTINGS
# Main Media Settings




# ######### SECURITY
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 0
#SECURE_SSL_REDIRECT=True

SESSION_COOKIE_SECURE = False
#X_FRAME_OPTIONS = 'Deny'
# ######### END SECURITY

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

########## AUTHENTICATION BACKENDS
AUTHENTICATION_BACKENDS = (
  'django.contrib.auth.backends.ModelBackend',
)
########## END AUTHENTICATION BACKENDS

# ########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
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
