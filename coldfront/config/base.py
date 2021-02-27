"""
Base Django settings for ColdFront project.
"""
import os
import coldfront
from django.core.management.utils import get_random_secret_key
from coldfront.config.settings import ENV, PROJECT_ROOT

#------------------------------------------------------------------------------
# Base Django config for ColdFront
#------------------------------------------------------------------------------
VERSION = coldfront.VERSION
ALLOWED_HOSTS = ['*']
DEBUG = ENV.bool('COLDFRONT_DEBUG', default=False)
DEVELOP = ENV.bool('COLDFRONT_DEVELOP', default=False)
SECRET_KEY = ENV.str('COLDFRONT_SECRET_KEY', default=get_random_secret_key())
WSGI_APPLICATION = 'coldfront.config.wsgi.application'
ROOT_URLCONF = 'coldfront.config.urls'

#------------------------------------------------------------------------------
# Locale settings
#------------------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#------------------------------------------------------------------------------
# Django Apps
#------------------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
]

# Additional Apps
INSTALLED_APPS += [
    'crispy_forms',
    'sslserver',
    'django_q',
    'simple_history',
]

# ColdFront Apps
INSTALLED_APPS += [
    'coldfront.core.user',
    'coldfront.core.field_of_science',
    'coldfront.core.utils',
    'coldfront.core.portal',
    'coldfront.core.project',
    'coldfront.core.resource',
    'coldfront.core.allocation',
    'coldfront.core.grant',
    'coldfront.core.publication',
    'coldfront.core.research_output',
]

#------------------------------------------------------------------------------
# Django Middleware
#------------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

#------------------------------------------------------------------------------
# Django template and site settings
#------------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            PROJECT_ROOT('site/templates'),
            '/usr/share/coldfront/site/templates',
            PROJECT_ROOT('coldfront/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_settings_export.settings_export',
            ],
        },
    },
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
SETTINGS_EXPORT = []

STATIC_URL = '/static/'
STATIC_ROOT = PROJECT_ROOT('static_root')
STATICFILES_DIRS = [
    PROJECT_ROOT('coldfront/static'),
]

# Add local site static files
if os.path.isdir(PROJECT_ROOT('site/static')):
    STATICFILES_DIRS.insert(0, PROJECT_ROOT('site/static'))

# Add system site static files
if os.path.isdir('/usr/share/coldfront/site/static'):
    STATICFILES_DIRS.insert(0, '/usr/share/coldfront/site/static')