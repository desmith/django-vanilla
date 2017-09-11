# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from os.path import basename, isfile, join, normpath
import re

from django.conf import settings
from django.core import management
from django.db import models

from django.conf import settings
from django.dispatch import receiver
from django.db import models
from django.db.models import Q
#from django.db.models import signals
from django.db.models.signals import post_save
from django.core import management
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.models import TimeStampedModel


def shellquote(s):
  return s.replace(" ", "\ ")


def unique_slugify(instance,
                   value,
                   slug_field_name='slug',
                   queryset=None,
                   slug_separator='-'
                   ):
  """
  Calculates and stores a unique slug of ``value`` for an instance.

  ``slug_field_name`` should be a string matching the name of the field to
  store the slug in (and the field to check against for uniqueness).

  ``queryset`` usually doesn't need to be explicitly provided - it'll default
  to using the ``.all()`` queryset from the model's default manager.
  """
  slug_field = instance._meta.get_field(slug_field_name)

  slug = getattr(instance, slug_field.attname)
  slug_len = slug_field.max_length

  # Sort out the initial slug, limiting its length if necessary.
  slug = slugify(value)
  if slug_len:
      slug = slug[:slug_len]
  slug = _slug_strip(slug, slug_separator)
  original_slug = slug

  # Create the queryset if one wasn't explicitly provided and exclude the
  # current instance from the queryset.
  if queryset is None:
      queryset = instance.__class__._default_manager.all()
  if instance.pk:
      queryset = queryset.exclude(pk=instance.pk)

  # Find a unique slug. If one matches, at '-2' to the end and try again
  # (then '-3', etc).
  next = 2
  while not slug or queryset.filter(**{slug_field_name: slug}):
    slug = original_slug
    end = '%s%s' % (slug_separator, next)
    if slug_len and len(slug) + len(end) > slug_len:
      slug = slug[:slug_len - len(end)]
      slug = _slug_strip(slug, slug_separator)
    slug = '%s%s' % (slug, end)
    next += 1

  setattr(instance, slug_field.attname, slug)


def _slug_strip(value, separator='-'):
  """
  Cleans up a slug by removing slug separator characters that occur at the
  beginning or end of a slug.

  If an alternate separator is used, it will also replace any instances of
  the default '-' separator with the new separator.
  """
  separator = separator or ''
  if separator == '-' or not separator:
    re_sep = '-'
  else:
    re_sep = '(?:-|%s)' % re.escape(separator)
  # Remove multiple instances and if an alternate separator is provided,
  # replace the default '-' separator.
  if separator != re_sep:
    value = re.sub('%s+' % re_sep, separator, value)
  # Remove separator from the beginning and end of the slug.
  if separator:
    if separator != '-':
      re_sep = re.escape(separator)
    value = re.sub(r'^%s+|%s+$' % (re_sep, re_sep), '', value)
  return value


# Create your models here.
class Page(TimeStampedModel, models.Model):
  """
  A simple page model.
  """

  slug = models.SlugField(
    max_length=255
  )

  publish_date = models.DateTimeField(
    blank=True,
    null=True,
    default=None
  )

  STATUS = Choices(
    'draft',
    'published'
  )

  status = StatusField(
    db_index=True
  )

  title = models.CharField(
    max_length=255,
    blank=False
  )

  content = models.TextField(
    blank=True,
    null=True
  )

  class Meta:
    ordering = ("-publish_date",)
    get_latest_by = ("publish_date")

  def __unicode__(self):
    return '%s, %s' % (self.slug, self.title)

  def save(self, *args, **kwargs):

    self.title = self.title.strip()
    unique_slugify(self, self.title)

    if not self.publish_date:
      self.publish_date = timezone.now()

    cache.clear()
    super(Page, self).save(*args, **kwargs)

  def get_absolute_url(self):
    if self.status == 'draft':
      return reverse('page_slug_preview', kwargs={'slug': self.slug, 'page_id': self.id})
    else:
      return reverse('page_slug_view', kwargs={'slug': self.slug, 'page_id': self.id})
