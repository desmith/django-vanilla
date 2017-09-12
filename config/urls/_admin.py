from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from django.contrib import admin


admin.autodiscover()

admin_patterns = [

#  url(r'^grappelli/', include('grappelli.urls')),
  url(r'^admin/', include(admin.site.urls)),

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

]
