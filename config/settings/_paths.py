import re
from sys import path
from os.path import dirname, join, normpath, realpath

##########
# PATH CONFIGURATION
##########

MEDIA_ROOT = '/data/{{project_name}}/media/'
MEDIA_URL = '/media/'
STATIC_ROOT = '/data/{{project_name}}/static/'
STATIC_URL = '/static/'

#FILES_ROOT = join(MEDIA_ROOT, 'files')
#FILES_URL = '/files/'

ROOT_DIR = realpath(dirname(__name__))
ASSETS_ROOT = normpath(join(ROOT_DIR, 'assets'))
CONF_DIR = dirname(realpath(__file__))
ROOT_URLCONF = 'config.urls'
STATIC_SRC = join(ROOT_DIR, 'static')

LOGIN_URL = '/admin/login'
FIXTURE_DIRS = (
  normpath(join(ROOT_DIR, 'data')),
)
LOCALE_PATHS = (
  normpath(join(ROOT_DIR, 'locale')),
)
# Add our project to our pythonpath, this way we don't
# need to type our project name in our dotted import paths:
path.append(ROOT_DIR)

IGNORABLE_404_URLS = (
  # re.compile(r'^/$'),
  re.compile(r'^/archive/.*$'),
  re.compile(r'\.(php|cgi)$'),
  re.compile(r'^/phpmyadmin/'),
  re.compile(r'^/apple-touch-icon.*\.png$'),
  # re.compile(r'^/favicon\.ico$'),
  # re.compile(r'^/robots\.txt$'),
)

STATICFILES_DIRS = [
  ASSETS_ROOT,
  STATIC_SRC,
]

########### END PATH CONFIGURATION
