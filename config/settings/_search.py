########## SEARCH CONFIGURATION
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 20
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_CONNECTIONS = {
  'default': {
    'INDEX_NAME': '',
    'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
    'TIMEOUT': 60
  }
}
########## END SEARCH CONFIGURATION
