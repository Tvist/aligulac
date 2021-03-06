# Path of the folder where manage.py is located
PROJECT_PATH = '/home/eivind/repos/aligulac/aligulac/'

# Path of folder where database dumps are saved
# If you never call dump.py this is not necessary
DUMP_PATH = '/home/eivind/repos/aligulac/untracked/'

# Path of folder where the locales are stored
LOCALE_PATHS = ('/home/eivind/repos/aligulac/locale/',)

# Random string, 50 characters
SECRET_KEY = ''

# API key to openexchangerates.org
EXCHANGE_ID = ''

# Database username and password
DB_USER = ''
DB_PASSWORD = ''

# Folder where the templates are stored
TEMPLATE_DIRS = ('/home/eivind/repos/aligulac/templates/',)

# Host names this server accepts connections to
ALLOWED_HOSTS = ['.aligulac.com', 'localhost']

# Necessary for django debug toolbar to work
INTERNAL_IPS = ('127.0.0.1',)

# Cache backend (use DummyCache in development)
CACHE_BACKEND = 'django.core.cache.backends.dummy.DummyCache'

# Cache location (where to store cached views with FileBasedCache, just leave empty if DummyCache)
CACHE_LOCATION = '/home/eivind/repos/aligulac/untracked/cache/'

# Debug mode (boolean, should be True in development)
DEBUG = True

# Include debug toolbar in debug mode?
DEBUG_TOOLBAR = True

# Log file for errors
ERROR_LOG_FILE = '/home/eivind/repos/aligulac/untracked/error.log'
