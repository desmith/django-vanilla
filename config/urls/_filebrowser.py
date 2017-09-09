from django.conf.urls import include, url
from django.core.files.storage import FileSystemStorage
from filebrowser.sites import site
site.storage = FileSystemStorage(location='/data/dhamseva/media', base_url='/media/')

filebrowser_patterns = [

  # filebrowser
  url(r'^admin/filebrowser/', include(site.urls)),

  # grappelli
  url(r'^grappelli/', include('grappelli.urls')),

]
