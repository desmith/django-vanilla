from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page


static_patterns = [

  # 404 page
  url(
    regex=r'^404/$',
    view=cache_page(settings.CACHE_TIMEOUT)(TemplateView.as_view(template_name='404.html')),
    name='error_page'
  ),

  # 500 error
  url(
    regex=r'^500/$',
    view=cache_page(settings.CACHE_TIMEOUT)(TemplateView.as_view(template_name='500.html')),
    name='error_app'
  ),


  # robots.txt
  url(
    regex=r'^robots\.txt$',
    view=cache_page(settings.CACHE_TIMEOUT)(TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    name='robotstxt',
  ),

  url(
    regex=r'^humans\.txt$',
    view=cache_page(settings.CACHE_TIMEOUT)(TemplateView.as_view(template_name='humans.txt', content_type='text/plain')),
    name='humanstxt'
    ),

]
