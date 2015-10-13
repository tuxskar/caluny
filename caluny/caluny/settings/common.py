"""
Django settings for caluny project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import random
import string

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
ADMINS = [('Oscar Ramirez', 'tuxskar@gmail.com')]
SERVER_EMAIL = 'django@caluny-production.com'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
try:
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
except KeyError:
    try:
        with open('secret.keys', 'r') as f:
            SECRET_KEY = f.readline()
    except IOError:
        with open('secret.keys', 'w') as f:
            choices = string.ascii_letters + ''.join(map(str, range(9))) + '/&%_-!()$'
            SECRET_KEY = ''.join([random.choice(choices) for _ in range(50)])
            f.write(SECRET_KEY)
            print 'Added secret key as {}'.format(SECRET_KEY)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']


# Application definition

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

INSTALLED_APPS = (
    'wpadmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    # 'django_extensions',
    'push_notifications',
    'model_utils',
    'core',
    'caluny_api',
    'caluny_api.chat_messages',
)

PUSH_NOTIFICATIONS_SETTINGS = {
    "GCM_API_KEY": "<your api key>",
    # "APNS_CERTIFICATE": "/path/to/your/certificate.pem",
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'PAGINATE_BY': 10
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'caluny.urls'

WSGI_APPLICATION = 'caluny.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(SITE_ROOT, '/static/')

WPADMIN = {
    'admin': {
        'title': 'Caluma admin panel',
        'menu': {
            'top': 'wpadmin.menu.menus.BasicTopMenu',
            'left': 'wpadmin.menu.menus.BasicLeftMenu',
        },
        'dashboard': {
            'breadcrumbs': True,
        },
        'custom_style': STATIC_URL + 'wpadmin/css/themes/coffe.css',
        # 'custom_style': STATIC_URL + 'wpadmin/css/themes/blue.css',
    }
}

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR + '/emails'  # change this to a proper location

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'email_backend': 'django.core.mail.backends.filebased.EmailBackend',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR + '/logs/django.error.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['mail_admins', 'file_error'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
