#from django.utils.translation import ugettext_lazy as _

#import sys
#reload(sys)
#sys.setdefaultencoding("utf8")

DEBUG = False

######### GENERAL CONFIGURATION
PROJET_NICKNAME = '{{project_name}}'
PROJET_DOMAIN_NAME = ''
TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
USE_THOUSAND_SEPARATOR = False
########## END GENERAL CONFIGURATION

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
SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_DOMAIN = SESSION_COOKIE_DOMAIN
CSRF_COOKIE_SECURE = SESSION_COOKIE_SECURE
CSRF_COOKIE_AGE = 31449600  # approx 1 year
# ######### END SECURITY

CRISPY_TEMPLATE_PACK = 'bootstrap4'
TASTYPIE_ALLOW_MISSING_SLASH = True
APPEND_SLASH = True

########## MANAGER CONFIGURATION
# They get emails when things break, esp in production
# where debug is turned off
ADMINS = [
  ('Name', 'email@{{project_name}}.org'),
]
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION

########## AUTHENTICATION BACKENDS
AUTHENTICATION_BACKENDS = (
  'django.contrib.auth.backends.ModelBackend',
)
########## END AUTHENTICATION BACKENDS

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

########## WSGI CONFIGURATION
# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'config.wsgi.application'
########## END WSGI CONFIGURATION
