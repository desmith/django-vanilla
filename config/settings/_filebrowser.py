########################
# FILEBROWSER SETTINGS #
########################

# Main FileBrowser Directory. This has to be a directory within MEDIA_ROOT.
# Leave empty in order to browse all files under MEDIA_ROOT.
# DO NOT USE A SLASH AT THE BEGINNING, DO NOT FORGET THE TRAILING SLASH AT THE END.
FILEBROWSER_DIRECTORY = 'images/'

# Directory to Save Image Versions (and Thumbnails). Relative to MEDIA_ROOT.
# If no directory is given, versions are stored within the Image directory.
# VERSION URL: VERSIONS_BASEDIR/original_path/originalfilename_versionsuffix.extension
FILEBROWSER_VERSIONS_BASEDIR = 'img_versions/'

FILEBROWSER_CONVERT_FILENAME = True
FILEBROWSER_DEFAULT_PERMISSIONS = 0o755
FILEBROWSER_DEFAULT_SORTING_BY = 'date'
FILEBROWSER_DEFAULT_SORTING_ORDER = 'desc'
FILEBROWSER_FOLDER_REGEX = r'^(?u)[ \w-][ \w.-]*$'
#FILEBROWSER_FOLDER_REGEX = r'^[\w._\ /-]+$'
FILEBROWSER_LIST_PER_PAGE = 50
FILEBROWSER_MAX_UPLOAD_SIZE = 10485760
FILEBROWSER_NORMALIZE_FILENAME = True
FILEBROWSER_OVERWRITE_EXISTING = False
FILEBROWSER_SEARCH_TRAVERSE = False
FILEBROWSER_SHOW_AT_ADMIN_PANEL = True
FILEBROWSER_SUIT_TEMPLATE = False
FILEBROWSER_VERSION_QUALITY = 85

# EXTRA SETTINGS
# True to save the URL including MEDIA_URL to your model fields
# or False (default) to save path relative to MEDIA_URL.
# Note: Full URL does not necessarily means absolute URL.
FILEBROWSER_SAVE_FULL_URL = False

# Versions available within the Admin-Interface.
FILEBROWSER_ADMIN_VERSIONS = ['thumbnail', 'small', 'medium', 'featured', ]
# Which Version should be used as Admin-thumbnail.
FILEBROWSER_ADMIN_THUMBNAIL = 'thumbnail'
FILEBROWSER_PREVIEW_VERSION = 'medium'

# Allowed Extensions for File Upload. Lower case is important.
FILEBROWSER_EXTENSIONS = {
  'Folder': [''],
  'Image': ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff', '.bmp'],
  'Document': ['.pdf', '.doc', '.docx', '.rtf', '.txt', '.xls', '.csv'],
  'Video': ['.mov', '.wmv', '.mpeg', '.mpg', '.avi', '.rm'],
  'Audio': ['.mp3', '.mp4', '.wav', '.aiff', '.midi', '.m4p']
}

# Define different formats for allowed selections.
# This has to be a subset of EXTENSIONS.
# e.g., add ?type=image to the browse-URL ...
FILEBROWSER_SELECT_FORMATS = {
  'file': ['Folder', 'Image', 'Document', 'Video', 'Audio'],
  'image': ['Image'],
  'document': ['Document'],
  'media': ['Video', 'Audio'],
}

# Versions Format. Available Attributes: verbose_name, width, height, opts
FILEBROWSER_VERSIONS = {
  'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
  'thumbnail': {'verbose_name': 'Thumbnail [60x45]', 'width': 60, 'height': 45, 'opts': 'crop'},
  'small': {'verbose_name': 'Small [140w X 90h]', 'width': 140, 'height': 90, 'opts': 'crop'},
  'medium': {'verbose_name': 'Medium [225w x 150h]', 'width': 225, 'height': 150, 'opts': 'crop'},
  'featured': {'verbose_name': 'Featured [300w x 200h]', 'width': 300, 'height': 200, 'opts': 'crop'},
  'large': {'verbose_name': 'Big [625w x 352h]', 'width': 625, 'height': 352, 'opts': 'crop'},
  'slideshow': {'verbose_name': 'Slideshow [750w x 422h]', 'width': 750, 'height': 422, 'opts': 'crop'},
  'comic': {'verbose_name': 'Comic [1024w x 768h]', 'width': 1024, 'height': 768, 'opts': 'crop'},
}
