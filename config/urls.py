import os
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page
from django.views.static import serve as ServeStatic

admin.autodiscover()

urlpatterns = [

  # robots.txt
  url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
  url(r'^humans\.txt$', TemplateView.as_view(template_name='humans.txt', content_type='text/plain')),

  # Uncomment the next line to enable the admin:
  url(r'^admin/', include(admin.site.urls)),

  # Uncomment the admin/doc line below to enable admin documentation:
  # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

  url(
      regex=r'^admin/password_reset/$',
      view=auth_views.password_reset,
      name='admin_password_reset'
     ),

  url(
      regex=r'^admin/password_reset/done/$',
      view=auth_views.password_reset_done,
      name='password_reset_done'
     ),

  url(
      regex=r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
      view=auth_views.password_reset_confirm,
      name='password_reset_confirm'
     ),

  url(
      regex=r'^reset/done/$',
      view=auth_views.password_reset_complete,
      name='password_reset_complete'
     ),

  # 404 page
  url(r'^404/$', TemplateView.as_view(template_name='404.html')),
  url(r'^500/$', TemplateView.as_view(template_name='500.html')),


]

urlpatterns += [
]

if settings.DEBUG:
  import debug_toolbar
  urlpatterns += [
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^media/(.+)', ServeStatic, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(.+)', ServeStatic, {'document_root': settings.STATIC_ROOT}),
    url(r'^photos/(.+)', ServeStatic, {'document_root': os.path.join(settings.MEDIA_ROOT, "photos")}),
    url(r'^images/(.+)', ServeStatic, {'document_root': os.path.join(settings.MEDIA_ROOT, "images")}),
    url(r'^imgvers/(.+)', ServeStatic, {'document_root': os.path.join(settings.MEDIA_ROOT, "imgvers")}),
  ]
