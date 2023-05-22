"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# initialize environment variables

env = environ.Env()

environ.Env.read_env(os.path.join(BASE_DIR, '.env.local'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', default=True)

ALLOWED_HOSTS = ["*"]

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'widget_tweaks',
    'django_cleanup.apps.CleanupConfig',
    'django_user_agents',
]

LOCAL_APPS = [
    'core.login',
    'core.pos',
    'core.reports',
    'core.security',
    'core.user',
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'crum.CurrentRequestUserMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
]

ROOT_URLCONF = 'config.urls'

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
                'core.security.context_processors.site_settings'
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

def get_db_config(environ_var='DATABASE_URL'):
    """Get Database configuration."""
    options = env.db(var=environ_var, default='sqlite:///db.sqlite3')
    if options.get('ENGINE') != 'django.db.backends.sqlite3':
        return options

    # This will allow use a relative to the project root DB path
    # for SQLite like 'sqlite:///db.sqlite3'
    if not options['NAME'] == ':memory:' and not os.path.isabs(options['NAME']):
        options.update({'NAME': os.path.join(BASE_DIR, options['NAME'])})

    return options


DATABASES = {
    'default': get_db_config()
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es-ec'

TIME_ZONE = 'US/Pacific'

USE_I18N = True

USE_TZ = True

USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'

# Auth

LOGIN_REDIRECT_URL = '/dashboard/'

LOGOUT_REDIRECT_URL = '/'

LOGIN_URL = '/'

AUTH_USER_MODEL = 'user.User'

# Email

EMAIL_USE_TLS = env('EMAIL_USE_TLS', default=True)
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

# Sessions

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

SESSION_COOKIE_NAME = 'pos-store'

SESSION_COOKIE_AGE = 60 * 240

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
