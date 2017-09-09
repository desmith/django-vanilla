from django.conf import settings
from django.conf.urls import include, url

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = []

from _admin import admin_patterns
urlpatterns += admin_patterns

#from _filebrowser import filebrowser_patterns
#urlpatterns += filebrowser_patterns

from content.urls import content_patterns
urlpatterns += content_patterns

#from _rest import rest_patterns
#urlpatterns += rest_patterns

from _static import static_patterns
urlpatterns += static_patterns


if settings.DEBUG:
  import debug_toolbar
  urlpatterns += [
    url(r'^__debug__/', include(debug_toolbar.urls)),

    #url(r'^media/(.+)', ServeStatic, {'document_root': settings.MEDIA_ROOT}),
    #url(r'^static/(.+)', ServeStatic, {'document_root': settings.STATIC_ROOT}),
    #url(r'^images/(.+)', ServeStatic, {'document_root': os.path.join(settings.MEDIA_ROOT, "images")}),
    #url(r'^imgvers/(.+)', ServeStatic, {'document_root': os.path.join(settings.MEDIA_ROOT, "imgvers")}),

  ]
