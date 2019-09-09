from ._middleware import MIDDLEWARE

DEBUG_TOOLBAR_CONFIG = {
  'INTERCEPT_REDIRECTS': False,
  'SHOW_TOOLBAR_CALLBACK': False,
  'HIDE_DJANGO_SQL': False,
  'TAG': 'div',
  'ENABLE_STACKTRACES': True,
}

DEBUG_TOOLBAR_PATCH_SETTINGS = False
DEBUG_TOOLBAR_PANELS = (
  'debug_toolbar.panels.timer.TimerPanel',
  'debug_toolbar.panels.request.RequestPanel',
  'debug_toolbar.panels.templates.TemplatesPanel',
  'debug_toolbar.panels.sql.SQLPanel',
  'debug_toolbar.panels.cache.CachePanel',
  #'haystack_panel.panel.HaystackDebugPanel',
  'debug_toolbar.panels.settings.SettingsPanel',
  'debug_toolbar.panels.headers.HeadersPanel',
  'debug_toolbar.panels.versions.VersionsPanel',
  'debug_toolbar.panels.staticfiles.StaticFilesPanel',
  'debug_toolbar.panels.signals.SignalsPanel',
  'debug_toolbar.panels.logging.LoggingPanel',
  'debug_toolbar.panels.redirects.RedirectsPanel',
)

MIDDLEWARE += (
  'debug_toolbar.middleware.DebugToolbarMiddleware',
)
