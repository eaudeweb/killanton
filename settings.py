import os
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__)) + '/'
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = (
    ('Anton Cupcea', 'anton@eaudeweb.ro'),
)
MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db.sqlite3',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
TIME_ZONE = 'Europe/Bucharest'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = PROJECT_PATH + 'media'
MEDIA_URL = 'http://localhost/media/killanton/'
ADMIN_MEDIA_PREFIX = '/media/'
SECRET_KEY = 'dkngu=lzr%p%*smcz6w944-)ju%(oneg^tf1nozrpt)_2r!v&m'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'killanton.urls'

TEMPLATE_DIRS = (
        PROJECT_PATH + 'templates'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'taskmanager',
)
