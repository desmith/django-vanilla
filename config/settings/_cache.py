########## CACHE CONFIGURATION
ADV_CACHE_RESOLVE_NAME = True
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_CACHE_ALIAS = 'default'
CACHE_COUNT_TIMEOUT = 60  # seconds, not too long.
CACHE_TIMEOUT = (60 * 60)
# ------------------------------------------------------------------------------
CACHES = {
  'default': {
    'BACKEND': 'django_redis.cache.RedisCache',
    'OPTIONS': {
      'CLIENT_CLASS': 'django_redis.client.DefaultClient',
      'MAX_ENTRIES': 10000,
      'IGNORE_EXCEPTIONS': True,  # mimics memcache behavior.
      # http://niwinz.github.io/django-redis/latest/#_memcached_exceptions_behavior
    }
  },
}
########## END CACHE CONFIGURATION
