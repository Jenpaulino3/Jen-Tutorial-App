"""
Django settings for tutorial_project project.
For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y*-)o@*mzq((wjb03ybu+#@++@w-m)s)eiq86e74i1dn^9u2y$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False # when you have an error it will give you a log in real life it will be set to false
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*', 'localhost'] # Add the versions of the urls

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tutorial_app',
    'braces',
    'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware', #stores cookies
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', #secures form submission
    'django.contrib.auth.middleware.AuthenticationMiddleware', #creates a logged in user section
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware', #creates session cookies
    'django.contrib.messages.middleware.MessageMiddleware', #error messages if you mess up a form
    'django.middleware.clickjacking.XFrameOptionsMiddleware', 
)

PASSWORD_HASHERS = {
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
}

ROOT_URLCONF = 'tutorial_project.urls'
WSGI_APPLICATION = 'tutorial_project.wsgi.application'

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
TEMPLATE_DIRS = (
    TEMPLATE_PATH,
    )

STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    STATIC_PATH,
    )

MEDIA_PATH = os.path.join(BASE_DIR, 'media')
MEDIAFILES_DIRS =(
    MEDIA_PATH,
    )

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases


if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

if not DEBUG:
    DATABASES = {'default' : dj_database_url.config(default='postgres:///djclass')}
    DATABASES['default'] ['ENGINE'] = 'django_postgrespool'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'EST'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOGIN_URL = '/login/' #if someone goes to page they are not supposed to send them to this page

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com' #Simple mail transfer protocol 
EMAIL_PORT = 587
EMAIL_HOST_USER = 'jenpaulino3@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('MAIL_PASS')

if DEBUG:
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'

if not DEBUG:
    AWS_STORAGE_BUCKET_NAME = 'jenniferstutorialapp'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

    MEDIAFILES_LOCATION = 'media'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

AWS_HEADERS = {
    'Access-Control-Allow-Origin' : '*'
    }