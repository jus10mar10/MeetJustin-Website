"""
Django settings for portfolio_website project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from decouple import config
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='cc+rrq$!r7-y^u(yah07-*cwc@_m_csy(-udqka(++c-_tb#sp')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = ['https://localhost:8000']

# Application definition
# Add the apps directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'apps'))

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.portfolio",
    "apps.account",
    'ckeditor',
    'ckeditor_uploader',
    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates'),],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.account.context_processors.avatar_context",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE", default="django.db.backends.sqlite3"),
        "NAME": config("DB_NAME", default=os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": config("DB_USER", default=""),
        "PASSWORD": config("DB_PASSWORD", default=""),
        "HOST": config("DB_HOST", default=""),
        "PORT": config("DB_PORT", default=""),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"),]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',  # Use 'full' for a comprehensive toolbar
    },
}

CKEDITOR_UPLOAD_PATH = "uploads/"

# settings.py

# Slugify filenames
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = True  # False if you want to disable

# Restrict access to uploaded images to the uploading user
CKEDITOR_RESTRICT_BY_USER = False  # Set to True if you want to enable

# Show directories on the “Browse Server” page
CKEDITOR_BROWSE_SHOW_DIRS = False  # Set to True if you want to enable

# Bucket uploaded files by date
CKEDITOR_RESTRICT_BY_DATE = False  # Set to True if you want to enable

# Custom storage backend
# CKEDITOR_STORAGE_BACKEND = 'your_custom_backend'

# Thumbnails
CKEDITOR_IMAGE_BACKEND = 'ckeditor_uploader.backends.PillowBackend'

# Thumbnail size
CKEDITOR_THUMBNAIL_SIZE = (75, 75)

# Force JPEG compression
CKEDITOR_FORCE_JPEG_COMPRESSION = False  # Set to True if you want to enable

# Image Quality
CKEDITOR_IMAGE_QUALITY = 75  # Set between 1 and 95


# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

TEMPLATE_DIRS = [
    os.path.join(PROJECT_PATH, 'templates/'),
]