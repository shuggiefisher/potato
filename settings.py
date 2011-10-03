# Initialize App Engine and import the default settings (DB backend, etc.).
# If you want to use a different backend you have to remove all occurences
# of "djangoappengine" from this file.
from djangoappengine.settings_base import *

import os

# Activate django-dbindexer for the default database
DATABASES['native'] = DATABASES['default']
DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native'}
AUTOLOAD_SITECONF = 'indexes'

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

SITE_ID = 34

STATIC_URL = '/static/'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'djangotoolbox',
    'autoload',
    'mediagenerator',
    'dbindexer',
    'piston',
    'social_auth',
    'api',
    'blog',

    # djangoappengine should come last, so it can override a few manage.py commands
    'djangoappengine',
)

MIDDLEWARE_CLASSES = (
    # This loads the index definitions, so it has to come first
    'autoload.middleware.AutoloadMiddleware',
    
    'mediagenerator.middleware.MediaMiddleware',
    
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    "django.core.context_processors.static"
)

# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

ADMIN_MEDIA_PREFIX = '/media/admin/'
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

ROOT_URLCONF = 'urls'

REDIRECT_FIELD_NAME = 'redirect_to'

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'django.contrib.auth.backends.ModelBackend',
)


TWITTER_CONSUMER_KEY         = 'dybZdIMMXCVmUMehNySWA'
TWITTER_CONSUMER_SECRET      = 'HOdUMBJau5xxMs7ff6Mkd6rTeyu1AkC3oVCM06T44'

TWITTER_ACCESS_TOKEN         = '383257807-fCPaCWlWeBoQI560J6z8jmCJdju5mQbId6AftoIw'
TWITTER_ACCESS_TOKEN_SECRET  = 'hnBgnvTd4G61laeWVJMvwounoZTlpTqmbpbuq16KV3o'

TWITTER_EXTRA_DATA = [('profile_image_url', 'profile_image_url')]

LOGIN_URL          = '/login-form/'
LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_ERROR_URL    = '/login-error/'

REDIRECT_FIELD_NAME = 'next'

SOCIAL_AUTH_ERROR_KEY = 'social_errors'

SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'


MEDIA_DEV_MODE = DEBUG #DEBUG
DEV_MEDIA_URL = '/devmedia/'
PRODUCTION_MEDIA_URL = '/media/'

GLOBAL_MEDIA_DIRS = (os.path.join(os.path.dirname(__file__), 'static'),)

MEDIA_BUNDLES = (
    ('main.css',
        'css/bootstrap.css',
        'css/salt-n-sauce.css',
    ),
    ('main.js',
        'js/jquery-1.6.4.js',
        'js/bootstrap-dropdown.js',
        'js/bootstrap-twipsy.js',
        'js/spin.js',
        'js/potato.js',
    ),
)

ROOT_MEDIA_FILTERS = {
    'js': 'mediagenerator.filters.closure.Closure',
    'css': 'mediagenerator.filters.yuicompressor.YUICompressor',
}

CLOSURE_COMPILER_PATH = '../bin/closure'
YUICOMPRESSOR_PATH = '../bin/yuicompressor'