"""Production settings and globals."""
from .base import *
from .logging import *

from ConfigParser import RawConfigParser

config = RawConfigParser()
config_file = '/etc/environments/production/{{project_name}}.org.ini'
config.read(config_file)

LOGGING['handlers']['logfile']['filename'] = '/var/log/django/{{project_name}}.log'
SECRET_KEY = config.get('django', 'SECRET_KEY')

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

########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES['default']['LOCATION'] = config.get('cache', REDIS_URL)
CACHES['default']['KEY_PREFIX'] = config.get('cache', KEY_PREFIX)
########## END CACHE CONFIGURATION
