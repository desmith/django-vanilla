from os.path import join, normpath
from pyclbr import readmodule_ex

from ._paths import ROOT_DIR

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
      normpath(join(ROOT_DIR, 'templates')),
      #normpath(join(dirname(readmodule_ex('reversion')['__path__'][0]), 'templates')),
    ],
    'OPTIONS': {
      'debug': False,
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
