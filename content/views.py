from django.core.exceptions import ObjectDoesNotExist

from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View, TemplateView

from .models import Page


class Homepage(TemplateView):

  template_name = 'homepage.html'

  def get_context_data(self, **kwargs):
    context = super(Homepage, self).get_context_data(**kwargs)

    """
    try:
      context['slideshow'] = Slideshow.objects.get(name='Homepage Slideshow')
    except ObjectDoesNotExist:
      context['slideshow'] = None
    """


    context['cache_timeout'] = settings.CACHE_TIMEOUT

    return context


class PageDetail(TemplateView):
  """
  Primary view for displaying pages.
  """
  template_name = 'content/page_detail.html'
  status = 'published'
  page = None

  def get_context_data(self, *args, **kwargs):
    page_id = None
    context = super(PageDetail, self).get_context_data(**kwargs)

    if self.kwargs:
      page_id = self.kwargs.get('page_id')
      if 'status' in self.kwargs:
        self.status = self.kwargs.get('status')
      if 'page' in self.kwargs:
        self.page = self.kwargs.get('page')

    if self.status == 'preview':
      page = get_object_or_404(Page, id=page_id)
    else:
      cache_name = ''.join(['page-', str(page_id)])
      page = cache.get_or_set(cache_name, get_object_or_404(Page, id=page_id, status=self.status), settings.CACHE_TIMEOUT)

    context['page'] = page

    return context

class Thanks(TemplateView):

  template_name = 'content/thanks.html'

  def get_context_data(self, *args, **kwargs):
    context = super(Thanks, self).get_context_data(**kwargs)

    return context
