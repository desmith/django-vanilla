from os.path import join

import six
import elasticsearch
from boto.s3.connection import OrdinaryCallingFormat
from requests_aws4auth import AWS4Auth

from .__base import *
from ._paths import *
from ._apps import INSTALLED_APPS
from ._templates import TEMPLATES
from ._middleware import (
  MIDDLEWARE_CLASSES,
  SERIALIZATION_MODULES,
  THUMBNAIL_FORMAT,
  STATICFILES_FINDERS,
  STATICFILES_STORAGE,
)
from ._cache import (
  CACHES,
  ADV_CACHE_RESOLVE_NAME,
  SESSION_ENGINE,
  SESSION_CACHE_ALIAS,
  CACHE_COUNT_TIMEOUT,
  CACHE_TIMEOUT
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

from ConfigParser import RawConfigParser


config = RawConfigParser()
config_file = '/etc/environments/production/{{project_name}}.ini'
config.read(config_file)

TEMPLATE_DEBUG = DEBUG

PROJET_DOMAIN_NAME = '{{project_name}}'

LOGGING['handlers']['logfile']['filename'] = ''.join(['/var/log/django/', PROJET_DOMAIN_NAME, '.log'])
SESSION_COOKIE_DOMAIN = '.{{project_name}}.org'
CSRF_COOKIE_DOMAIN = SESSION_COOKIE_DOMAIN
GOOGLE_RECAPTCHA_SECRET_KEY = config.get('django', 'GOOGLE_RECAPTCHA_SECRET_KEY')

ALLOWED_HOSTS = [
    '.{{project_name}}.org',
]

### TinyMCE
TINYMCE_JS_URL = join(STATIC_URL, 'tiny_mce/tiny_mce.js')
TINYMCE_JS_ROOT = join(STATIC_ROOT, 'tiny_mce/')

GRAPPELLI_ADMIN_TITLE = 'Default Grappelli Title'
GRAPPELLI_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
#GRAPPELLI_ADMIN_URL =


### Filebrowser
FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT
FILEBROWSER_MEDIA_URL = MEDIA_URL
FILEBROWSER_PATH_FILEBROWSER_MEDIA = join(STATIC_ROOT, 'filebrowser/')
FILEBROWSER_URL_FILEBROWSER_MEDIA = join(STATIC_URL, 'filebrowser/')
FILEBROWSER_URL_TINYMCE = join(STATIC_URL, 'grappelli/tinymce/jscripts/tiny_mce/')
FILEBROWSER_PATH_TINYMCE = join(STATIC_ROOT, 'grappelli/tinymce/jscripts/tiny_mce/')
### end Filebrowser

# ######### DATABASE CONFIGURATION
DATABASES['default']['NAME'] = config.get('database', 'DATABASE_NAME')
DATABASES['default']['USER'] = config.get('database', 'DATABASE_USER')
DATABASES['default']['PASSWORD'] = config.get('database', 'DATABASE_PASSWORD')
DATABASES['default']['HOST'] = config.get('database', 'DATABASE_HOST')
# ######### END DATABASE CONFIGURATION

########## EMAIL CONFIGURATION
EMAIL_PORT = config.get('email', 'EMAIL_PORT')
EMAIL_HOST = config.get('email', 'EMAIL_HOST')
EMAIL_HOST_USER = config.get('email', 'EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config.get('email', 'EMAIL_HOST_PASSWORD')
########## END EMAIL CONFIGURATION

########## AWS CONFIGURATION
AWSHOST = config.get('aws', 'AWSHOST')
AWS_ACCESS_KEY_ID = config.get('aws', 'AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config.get('aws', 'AWS_SECRET_ACCESS_KEY')

AWSAUTH = AWS4Auth(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, 'us-east-1', 'es')
AWS_AUTO_CREATE_BUCKET = True
AWS_QUERYSTRING_AUTH = False
WS_STATIC_STORAGE_BUCKET = '{{project_name}}static'
AWS_MEDIA_STORAGE_BUCKET = '{{project_name}}media'
AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()

AWS_EXPIRY = 60 * 60 * 24 * 7
AWS_HEADERS = {
  'Cache-Control': six.b('max-age=%d, s-maxage=%d, must-revalidate' % (
    AWS_EXPIRY, AWS_EXPIRY))
}

STATIC_FILES_BUCKET = AWS_STATIC_STORAGE_BUCKET
MEDIA_FILES_BUCKET = AWS_MEDIA_STORAGE_BUCKET
########## END AWS CONFIGURATION

########## CACHE CONFIGURATION
CACHES['default']['LOCATION'] = config.get('cache', 'REDIS_URL')
CACHES['default']['KEY_PREFIX'] = config.get('cache', 'KEY_PREFIX')
########## END CACHE CONFIGURATION

########## SEARCH CONFIGURATION
HAYSTACK_CONNECTIONS['default']['URL'] = AWSHOST
HAYSTACK_CONNECTIONS['default']['KWARGS'] = {
  'port': 443,
  'http_auth': AWSAUTH,
  'use_ssl': True,
  'verify_certs': True,
  'connection_class': elasticsearch.RequestsHttpConnection
}
########## END SEARCH CONFIGURATION

### URL Shortener
#BITLY_ACCESS_TOKEN = config.get('api_keys', 'BITLY_ACCESS_TOKEN')

### Twitter
#TWITTER_CONSUMER_KEY = config.get('api_keys', 'TWITTER_CONSUMER_KEY')
#TWITTER_CONSUMER_SECRET = config.get('api_keys', 'TWITTER_CONSUMER_SECRET')
#TWITTER_ACCESS_TOKEN = config.get('api_keys', 'TWITTER_ACCESS_TOKEN')
#TWITTER_ACCESS_TOKEN_SECRET = config.get('api_keys', 'TWITTER_ACCESS_TOKEN_SECRET')

### Facebook
#FACEBOOK_APP_ID = config.get('api_keys', 'FACEBOOK_APP_ID')
#FACEBOOK_APP_SECRET = config.get('api_keys', 'FACEBOOK_APP_SECRET')

