# ######### MIDDLEWARE CONFIGURATION
MIDDLEWARE = (
  'django.middleware.common.CommonMiddleware',
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

SERIALIZATION_MODULES = {
  'xml': 'tagulous.serializers.xml_serializer',
  'json': 'tagulous.serializers.json',
  'python': 'tagulous.serializers.python',
  'yaml': 'tagulous.serializers.pyyaml',
}

######### STATIC FILE CONFIGURATION
THUMBNAIL_FORMAT = 'png'
STATICFILES_FINDERS = [
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'inews.storage_backends.StaticFilesStorage'
########## END MIDDLEWARE CONFIGURATION
