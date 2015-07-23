"""
Django settings for shooter project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f6g292j1z+vel3eyr0w%v3m3d#k++$u5@lt8r+0qd%_7mzgah='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

# provide our get_profile()
AUTH_USER_MODEL = 'userprofile.User'

LOGIN_URL = '/account/login/' 
LOGIN_REDIRECT_URL = 'account/profile/'

DELETE_MESSAGE = 50

MESSAGE_TAGS = {
    DELETE_MESSAGE: 'deleted', 
}

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
    'userprofile.context_processors.say_hello',
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_bootstrap_breadcrumbs',
    'userprofile',
    'tournament',
    'article',
    'contact',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'shooter.urls'

WSGI_APPLICATION = 'shooter.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'testdatabase',
        'USER': 'shoter',
        'PASSWORD': 'shooter',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pl-pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

#USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

#Template location
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static", "templates"),
)


if DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static-only")
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")
    STATICFILES_DIRS = (
        os.path.join(os.path.dirname(BASE_DIR), "static", "static"),
    )

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'projekt.strzelec@gmail.com'
EMAIL_HOST_PASSWORD = 'DjangoStrzelec01'
EMAIL_USE_TLS = True
LIST_OF_EMAIL_RECIPIENTS = ['projekt.strzelec@gmail.com']
