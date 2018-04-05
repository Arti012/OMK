"""
Django settings for omk project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bz=xn0cf0ra=ias6o=u&6l^@2!d=+jb*y49v)k!=m9u2d9o_h-'

# SECURITY WARNING: don't run with debug turned on in production!
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']


DEBUG = True

if DEBUG:
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'omkidsorg@gmail.com '
    EMAIL_HOST_PASSWORD = 'Python@123'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = 'omkidsorg@gmail.com'

#ALLOWED_HOSTS = ['*']

try:
    from .local_settings import *
except ImportError:
    pass

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'django.contrib.admin',
    'social_django',
 'social.apps.django_app.default',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'omk.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'omk.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd2gsfmtnf5s740',
        'USER': 'clthqkwjaztxyl',
        'PASSWORD': 'cfca3298a991fc2de70b0502b5bb4832cdeb6c1361817f325e10d7dd2c14255f',
        'HOST': 'ec2-54-243-54-6.compute-1.amazonaws.com',
        'PORT': '5432',
      # 'ENGINE': 'django.db.backends.sqlite3',
      # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

#STATIC_ROOT = "C:/Python/OMK/home/static"

#PROJECT_ROOT = "C:/Python/OMK/home/"

#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
#STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = '/mentorhome'

#STATICFILES_DIRS = (os.path.join(BASE_DIR,"static") ,)

#STATICFILES_DIRS = (
 #   os.path.join(PROJECT_ROOT, 'staticfiles'),)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)


STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

#Social auth
AUTHENTICATION_BACKENDS = (

    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_TWITTER_KEY = 'm5YIDiKfcsfg62lxkq3bfQZyD'
SOCIAL_AUTH_TWITTER_SECRET = 'pOwX6LmZiPq5Z40iKrGoYNZ9dyLPEvZ3oHjEvSfrxD580wpyvb'


#twilio

TWILIO_ACCOUNT_SID = 'ACecb6bc927ff32ab8e3958168cfd394dd'
TWILIO_AUTH_TOKEN = 'e9a6f27e842c331b8c0a814e28d10627'
TWILIO_PHONE_NUMBER = '+15312017692'