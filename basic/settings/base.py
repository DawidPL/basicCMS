from django.utils.translation import ugettext_lazy as _
import os

from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SECRET_KEY = config('SECRET_KEY', default='123456')

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'pages.apps.PagesConfig',
    'optimized_image',
    'ckeditor',
    'ckeditor_uploader',
    'imagekit',
    'sass_processor',
    'django_distill',
    'adminsortable2',

]

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_FORCE_JPEG_COMPRESSION = True

CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_CONFIGS = {
    'default': {
        "removePlugins": "stylesheetparser",  # styles in source code
        'allowedContent': True,  # styles in source code
        'width': 1500,
        'height': 700,
        'entities_latin': False,  # problem with polish encoding,
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'basic.urls'

LANGUAGES = (
    ('en', _('English')),
    ('pl', _('Polish')),

)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'pages.context_processors.common_context',
                'pages.context_processors.nav_tree_generator',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'basic.wsgi.application'

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = False

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# Django Sass
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]

SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR, 'static')

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Sendgrid settings
SENDGRID_API_KEY = config('SENDGRID_API')
SENDGRID_SANDBOX_MODE_IN_DEBUG = False
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
DEFAULT_EMAIL_ADRESS = config('DEFAULT_EMAIL')

# ignore GIFs
OPTIMIZED_IMAGE_IGNORE_EXTENSIONS = ['gif']
# TinyPNG or Pillow - your choice :)
OPTIMIZED_IMAGE_METHOD = 'pillow'
# TinyPng provide 100 pics/month limit
TINYPNG_KEY = config('TINYPNG_API')

# Google recaptcha
GOOGLE_RECAPTCHA = config('RECAPTCHA')

# PAGE INFORMATION
PAGE_NAME = 'BasicCMS'
PAGE_URL = 'https://www.internet-plus.pl'

# Django - jet
JET_DEFAULT_THEME = 'light-blue'
JET_SIDE_MENU_COMPACT = True

JET_SIDE_MENU_ITEMS = [
    {'label': _('Elementy strony'), 'app_label': 'core', 'items': [
        {'name': 'pages.project', 'label': _('Projekty')},
        {'name': 'pages.homepage', 'label': _('Strona główna')},
        {'name': 'pages.subpage', 'label': _('Podstrony')},
        {'name': 'pages.contactpage', 'label': _('Podstrona kontakt')},
        {'name': 'pages.blogpost', 'label': _('Wpisy bloga')},
    ]},
    {'label': _('Media'), 'items': [
        {'name': 'pages.gallery', 'label': _('Galerie')},
        {'name': 'pages.image', 'label': _('Grafiki')},
        {'name': 'pages.carousel', 'label': _('Slider')},
        {'name': 'pages.socialmedia', 'label': _('Social media')},
    ]},
    {'label': _('Narzędzia SEO'), 'items': [
        {'name': 'pages.sitesettings', 'label': _('Ustawienia strony')},
        {'label': _('Google Analytics'), 'url': 'https://analytics.google.com/analytics/web/provision/#/provision',
         'url_blank': True},
        {'label': _('Google Search Console'), 'url': 'https://search.google.com/search-console/about',
         'url_blank': True},
        {'label': _('Google Tag Manager'), 'url': 'https://tagmanager.google.com/', 'url_blank': True},
        {'label': _('Page Speed'), 'url': f'https://developers.google.com/speed/pagespeed/insights/',
         'url_blank': True},
    ]},
    {'label': _('Dodatki'), 'items': [
        {'name': 'pages.box', 'label': _('Boxy')},
        {'name': 'pages.customcss', 'label': _('Własny css')},
    ]},
]

DISTILL_DIR = 'statyczna'
