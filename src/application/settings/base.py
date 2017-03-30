import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',

    'wagtail.contrib.wagtailapi',
    'wagtail.contrib.settings',
    'wagtail.contrib.wagtailsitemaps',

    'rest_framework',
    'modelcluster',
    'taggit',

    'wagtailfontawesome',
    'wagtailthemes',

    'application.apps.pages',
    'application.apps.social',
]

LANGUAGE_CODE = 'en-us'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media')

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
    'wagtailthemes.middleware.ThemeMiddleware',
]

ROOT_URLCONF = 'application.urls'

SECRET_KEY = '7b&ova34-9b(dj$gevm65$lc!m3#^#g1z*v#gv-g8k0wlo7#l8'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'public/static')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'wagtailthemes.loaders.ThemeLoader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

WAGTAIL_SITE_NAME = 'Application'

WAGTAILAPI_BASE_URL = 'http://localhost:8000'

WSGI_APPLICATION = 'application.wsgi.application'


# Wagtail-themes
# https://github.com/moorinteractive/wagtail-themes

WAGTAIL_THEME_PATH = 'themes'
WAGTAIL_THEMES = [
    ('default', 'Default theme'),
    ('winter', 'Winter theme')
]
