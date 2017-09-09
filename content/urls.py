from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page

from content.views import Homepage, PageDetail, Thanks
from content.models import Page


content_patterns = [

  url(
    regex=r'^$',
    view=Homepage.as_view(),
    name='homepage_view'
  ),

  url(
    regex=r'^page/(?P<slug>[-\w\d]+),[\s]?(?P<page_id>\d+)/$',
    view=PageDetail.as_view(),
    name='page_slug_view'
  ),

  url(
    regex=r'^preview/page/(?P<slug>[-\w\d]+),[\s]?(?P<page_id>\d+)/$',
    view=PageDetail.as_view(status='preview'),
    name='page_slug_preview'
  ),

  url(
    regex=r'thanks/',
    view=cache_page(settings.CACHE_TIMEOUT)(Thanks.as_view()),
    name='thanks'
  ),

]

