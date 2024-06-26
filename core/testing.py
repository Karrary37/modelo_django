from pathlib import Path
import os
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = os.path.dirname(__file__)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&pu=l=z@ho&i()97tu*9^11sj#-yew*xok1p&2u&9=4^wzk41w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'custom_auth',
    # 'core',

    'celery',
    'django_celery_results',

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

ROOT_URLCONF = 'core.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


if 'test' in sys.argv:
    MIGRATION_MODULES = DisableMigrations()


DATABASES = {
    'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'testing.sqlite3'},
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/


LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = "/home/staticfiles/core"

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_DIR, "media")

CORS_ORIGIN_ALLOW_ALL = True

X_FRAME_OPTIONS = 'SAMEORIGIN'

AUTH_USER_MODEL = 'custom_auth.UserProfile'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'PAGE_SIZE': 20
}

ONE_SIGNAL_APP_ID = ""
ONE_SIGNAL_REST_API_KEY = ""
ONE_SIGNAL_USER_AUTH_KEY = ""

BASE_URL = ""

CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Sao_Paulo'
DJANGO_CELERY_RESULTS_TASK_ID_MAX_LENGTH = 191
CELERY_RESULT_EXTENDED = True
# CELERY_CREATE_MISSING_QUEUES = False
CELERY_DEFAULT_QUEUE = 'celery'
CELERY_TASK_TRACK_STARTED = True
CELERY_SEND_EVENTS = True
CELERY_SEND_SENT_EVENT = True
CELERY_WORKER_MAX_TASKS_PER_CHILD = 25
CELERY_TASK_REJECT_ON_WORKER_LOST = True
CELERYD_TIME_LIMIT = 60
CELERYD_SOFT_TIME_LIMIT = 50
CELERY_ACKS_LATE = True
CELERYD_PREFETCH_MULTIPLIER = 1
CELERY_RESULT_EXPIRES = 1 * 60

ELASTIC_CACHE_URL = os.getenv('ELASTIC_CACHE_URL')

RABBITMQ_AMQP_URL = os.getenv('RABBITMQ_AMQP_URL')
RABBITMQ_AMQP_URL = 'amqp://admin:123@rabbitmq:5672'

try:
    from core.local_settings import * # noqa: F403
except ImportError:
    pass

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
