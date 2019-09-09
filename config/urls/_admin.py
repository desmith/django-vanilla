from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin


admin.autodiscover()

admin_patterns = [

  path('admin/', admin.site.urls),

]
