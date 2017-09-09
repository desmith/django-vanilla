from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth.models import User
#import tagulous

from .models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
  """
  Admin class for pages
  """

  ordering = ['-id', ]
  list_display = ['id',
    'slug',
    'title',
    'status',
    'created',
    'modified',
    'publish_date'
  ]

  list_filter = ['status',
    'publish_date',
   ]

  list_display_links = ['id', 'title', ]

  readonly_fields = ['slug', ]

  date_hierarchy = 'publish_date'

  search_fields = ['id',
    'slug',
    'title',
    'content'
  ]

  fieldsets = (
    ("Metadata",
      {"fields":
        ("status", )
      }
    ),
    ("Content",
      {"fields":
        ("title", "content", )
      }
    ),
    ("Info",
      {"fields":
        ("slug", "publish_date", ),
       "classes": ('grp-collapse grp-closed',)
      }
    ),
  )

  class Media:
    js = [
      '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
      '/static/grappelli/tinymce_setup/tinymce_setup.js',
    ]

  def get_tags(self, obj):
    tags = ', '.join([s.name for s in obj.tags.all()])
    return tags
  get_tags.short_description = "Tags"

