from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.utils.six.moves import input
from taggit.models import Tag, TaggedItem

class Command(BaseCommand):
  args = '<tag_slug tag_slug ... >'
  help = 'deletes tag(s) from Tag and TaggedItem tables'


  def handle(self, *args, **options):

    if len(args) < 1:
      raise CommandError('Please provide at least one tag to delete.')

    for slug in args:
      try:
        tag = Tag.objects.get(slug=slug)
      except ObjectDoesNotExist:
        raise CommandError('Tag "%s" does not exist' % slug)

      items = TaggedItem.objects.filter(tag=tag)
      message = ['\n']
      for item in items:
        obj = item.content_object
        self.stdout.write('Deleting obj:' + obj.title + ', slug: ' + tag.slug)
        self.stdout.write(' url:' + obj.get_absolute_url())
        #message.append(
        #  'Are you sure you want to do this?\n\n'
        #  "Type 'yes' to continue, or 'no' to cancel: "
        #  )

        #if input(''.join(message)) != 'yes':
        #  raise CommandError("Collecting static files cancelled.")
        #  exit

        obj.tags.remove(tag)
      tag.delete()

      self.stdout.write('Successfully deleted tag "%s"\n' % slug)
