from os.path import join

# TinyMCE Settings
TINYMCE_JS_URL = None # defined in _paths.py
TINYMCE_JS_ROOT = None # defined in _paths.py
TINYMCE_CONFIG_PLUGINS = "inlinepopups,visualchars,paste,media,template,table"
TINYMCE_CONFIG_THEME = "advanced"
TINMYCE_CONFIG_MODE = "textareas"
TINYMCE_CONFIG_THEME_ADVANCED_BUTTONS1 = "formatselect,styleselect,|,bold,italic,underline,|,undo,redo,|,bullist,numlist,hr,|,link,unlink,anchor,|,charmap,|,image,media,|,code,|,pastetext,pasteword,tablecontrols"
TINYMCE_CONFIG_THEME_ADVANCED_BUTTONS2 = ""
TINYMCE_CONFIG_THEME_ADVANCED_BUTTONS3 = ""
TINYMCE_CONFIG_THEME_ADVANCED_BUTTONS4 = ""
TINYMCE_CONFIG_THEME_ADVANCED_TOOLBAR_LOCATION = "top"
TINYMCE_CONFIG_THEME_ADVANCED_TOOLBAR_ALIGN = "left"
TINYMCE_CONFIG_THEME_ADVANCED_STATUSBAR_LOCATION = "bottom"
TINYMCE_CONFIG_THEME_ADVANCED_PATH = 0
TINYMCE_CONFIG_THEME_ADVANCED_RESIZING = 1
TINYMCE_CONFIG_RELATIVE_URLS = 0
TINYMCE_CONFIG_WIDTH = '90%'
TINYMCE_CONFIG_HEIGHT = '300'
TINYMCE_CONFIG_DELTA_HEIGHT = '300'
TINYMCE_CONFIG_THEME_ADVANCED_RESIZE_HORIZONTAL = 0
#TINYMCE_CONFIG_CONTENT_CSS = MEDIA_URL +"css/style_tinymce.css"
TINYMCE_CONFIG_THEME_ADVANCED_BLOCKFORMATS = "p,h2,h3,h4,h5,blockquote" #h1,
TINYMCE_CONFIG_THEME_ADVANCED_STYLES = "Big=big;Uppercase=uppercase;h1=h1;h2=h2;h3=h3;h4=h4;h5=h5;h6=h6"
TINYMCE_DEFAULT_CONFIG = {
  'plugins': TINYMCE_CONFIG_PLUGINS,
  'theme': TINYMCE_CONFIG_THEME,
  'mode': TINMYCE_CONFIG_MODE,
  'theme_advanced_buttons1': TINYMCE_CONFIG_THEME_ADVANCED_BUTTONS1,
  'theme_advanced_buttons2': TINYMCE_CONFIG_THEME_ADVANCED_BUTTONS2,
  'theme_advanced_buttons3': TINYMCE_CONFIG_THEME_ADVANCED_BUTTONS3,
  'theme_advanced_buttons4': TINYMCE_CONFIG_THEME_ADVANCED_BUTTONS4,
  'theme_advanced_toolbar_location': TINYMCE_CONFIG_THEME_ADVANCED_TOOLBAR_LOCATION,
  'theme_advanced_toolbar_align': TINYMCE_CONFIG_THEME_ADVANCED_TOOLBAR_ALIGN,
  'theme_advanced_statusbar_location': TINYMCE_CONFIG_THEME_ADVANCED_STATUSBAR_LOCATION,
  'theme_advanced_path': TINYMCE_CONFIG_THEME_ADVANCED_PATH,
  'theme_advanced_resizing': TINYMCE_CONFIG_THEME_ADVANCED_RESIZING,
  'relative_urls': TINYMCE_CONFIG_RELATIVE_URLS,
  'width': TINYMCE_CONFIG_WIDTH,
  'delta_height': TINYMCE_CONFIG_DELTA_HEIGHT,
  'theme_advanced_resize_horizontal': TINYMCE_CONFIG_THEME_ADVANCED_RESIZE_HORIZONTAL,
  #'content_css' : TINYMCE_CONFIG_CONTENT_CSS,
  'theme_advanced_blockformats': TINYMCE_CONFIG_THEME_ADVANCED_BLOCKFORMATS,
  'external_link_list_url': 'ss.mp4',
  #"file_browser_callback": TINYMCE_CONFIG_FILEBROWSER_CALLBACK,
  # Style formats
  'theme_advanced_styles': TINYMCE_CONFIG_THEME_ADVANCED_STYLES,
  'paste_auto_cleanup_on_paste': 1,
  'cleanup_on_startup': 1,
  'custom_undo_redo_levels': 20,
  'paste_remove_styles': 1,
  'paste_remove_styles_if_webkit': 1,
  'paste_strip_class_attributes': 1,
}

# HTML tags which come from TinyMCE will be whitelisted to this list.
TINYMCE_DISABLE_CLEANING = True
TINYMCE_ALLOWED_TAGS = [
  'a', 'b', 'em', 'i', 'h1', 'h2', 'h3', 'h4', 'h5',
  'li', 'ol', 'p', 'strong', 'ul', 'img', 'br', 'table',
  'thead', 'tbody', 'th', 'tr', 'td', 'blockquote', 'hr'
]
TINYMCE_ALLOWED_ATTRIBUTES = {
  'a': ['href', 'title', 'style', 'align', 'class'],
  'img': ['id', 'src', 'alt', 'style', 'width', 'height', 'class', 'title', 'align'],
  'div': ['class', 'style'],
  'table': ['cellpadding', 'cellspacing', 'border', ],
  'object': ['class', 'style', 'width', 'height', 'data', 'type', 'id', 'align'],
  'param': ['name', 'value'],
}
TINYMCE_ALLOWED_STYLES = ['width', 'height']
