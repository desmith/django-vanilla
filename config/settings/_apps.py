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

)

DJANGO_PRE_ADMIN = (
#  'grappelli.dashboard',
#  'grappelli',
#  'filebrowser',

)

DJANGO_ADMIN = (
  # Uncomment the next line to enable the admin:
  'django.contrib.admin',

)

THIRD_PARTY_APPS = (
#  'adv_cache_tag',
#  'autoslug',
  'django_extensions',
#  'haystack',
#  'tagulous',
#  'tastypie',

)

# Apps specific for this project go here.
LOCAL_APPS = (
  'content',
)

INSTALLED_APPS = DJANGO_APPS + DJANGO_PRE_ADMIN + DJANGO_ADMIN + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION
