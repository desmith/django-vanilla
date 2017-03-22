"""Production settings and globals."""
from .base import *
from .logging import *

from ConfigParser import RawConfigParser

config = RawConfigParser()
config_file = '/etc/environments/production/{{project_name}}.org.ini'
config.read(config_file)

LOGGING['handlers']['logfile']['filename'] = '/var/log/django/{{project_name}}.log'
SECRET_KEY = config.get('django', 'SECRET_KEY')
SESSION_COOKIE_DOMAIN = '.iskconnews.org'
CSRF_COOKIE_DOMAIN = SESSION_COOKIE_DOMAIN

ALLOWED_HOSTS = [
    'admin.{{project_name}}.org',
    '.{{project_name}}.org',
]

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
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES['default']['LOCATION'] = config.get('cache', 'REDIS_URL')
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

