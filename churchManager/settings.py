"""
Django settings for Optar project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path
from telnetlib import LOGOUT

import dj_database_url
import django_on_heroku
from decouple import config
from django.contrib.messages import constants
from dotenv import find_dotenv, load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-l15#=v&h9vh9t!b(^a$vs1zpx86dr&wtmz@osze88-eun$bio9'  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#config('DEBUG', cast=bool, default=False)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'fontawesomefree',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # my apps
    'account',
    'crispy_bootstrap5',
    'crispy_forms'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Optar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Optar.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
load_dotenv(find_dotenv())

'''
DATABASES = {'default': dj_database_url.config(
    default='sqlite://db.sqlite3', conn_max_age=600, ssl_require=False)}

'''
# Using Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa
    },

    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'base_static')
]


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Autentication Settings
AUTH_USER_MODEL = "company.Company"

# login settings
SESSION_COOKIE_AGE = 1800
SESSION_SAVE_EVERY_REQUEST = True

# crispy forms settings
CRISPY_ALLOWED_TEMPLATE_PACK = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

# Messages settings
MESSAGE_TAGS = {
    constants.DEBUG: 'message-debug',
    constants.SUCCESS: 'message-sucess',
    constants.INFO: 'message-info',
    constants.ERROR: 'message-error',
    constants.WARNING: 'message-warning',
}

# incrementing a longer time for DB

DATABASE_OPTIONS = {'timeout': 30}

# Mask Date
USE_L1ON = True
DATE_INPUT_FORMATS = ('%d/%m/%Y',)

django_on_heroku.settings(locals())
