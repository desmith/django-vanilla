from django.conf import settings
from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from content.views import Homepage, Listings, PageDetail, Thanks


content_patterns = [

  path('', Homepage.as_view(), name='homepage_view'),
  path('listings/', Listings.as_view(), name='listings_view'),

  path('^listings/',
       Listings.as_view(),
       'listings_view'
       ),

  path('^page/<slug:slug>,<int:page_id>/',
       PageDetail.as_view(),
       'page_slug_view'
       ),

  re_path('^preview/page/(?P<slug>[-\w\d]+),[\s]?(?P<page_id>\d+)/$',
       PageDetail.as_view(status='preview'),
       'page_slug_preview'
       ),

  path('thanks/',
       cache_page(settings.CACHE_TIMEOUT)(Thanks.as_view()),
       name='thanks'
       ),

  '''
  path('preview/video/<slug:slug>,<int:video_id>/',
       views.VideoSlugDetail.as_view(), {'status': 'preview'},
       name='video_preview'
       ),
  '''

]
