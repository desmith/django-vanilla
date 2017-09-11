from ._paths import ROOT_DIR

LOGGING = {
  'version': 1,
  'disable_existing_loggers': True,
  'root': {
    #'level': 'DEBUG',
    #'level': 'WARN',
    'level': 'ERROR',
    'handlers': ['console'],
  },
  'formatters': {
    'verbose': {
      'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
    },
    'simple': {
      'format': '%(levelname)s %(message)s'
    },
    'standard': {
      'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
      'datefmt': "%d/%b/%Y %H:%M:%S"
    },
  },
  'filters': {
    'require_debug_false': {
      '()': 'django.utils.log.RequireDebugFalse'
    },
  },
  'handlers': {
    'console': {
      'level': 'DEBUG',
      'class': 'logging.StreamHandler',
      'formatter': 'verbose'
    },
    'logfile': {
      'level': 'DEBUG',
      'class': 'logging.handlers.RotatingFileHandler',
      'filename': ROOT_DIR + "/logs/django.log",
      'maxBytes': 150000,
      'backupCount': 6,
      'formatter': 'standard',
    },
    'mail_admins': {
      'level': 'ERROR',
      'filters': ['require_debug_false'],
      'class': 'django.utils.log.AdminEmailHandler'
    },
  },
  'loggers': {
    'django': {
      'handlers': ['console'],
      'propagate': True,
      'level': 'WARN',
    },
    'django.request': {
      'handlers': ['mail_admins'],
      'level': 'ERROR',
      'propagate': True,
    },
    'django.db.backends': {
      'level': 'ERROR',
      'handlers': ['console'],
      'propagate': False,
    },
    'stdout': {
      'handlers': ['logfile'],
      'level': 'DEBUG',
    },
    'log': {
      'handlers': ['logfile'],
      'level': 'DEBUG',
    },
    'dual': {
      'handlers': ['console', 'logfile'],
      'level': 'DEBUG',
    },
  },

}
