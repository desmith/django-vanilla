
from django.conf import settings
from django.views.generic.base import View, TemplateView


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
