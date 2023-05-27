
import os
from pathlib import Path
# from . import * 
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t^11*)5w+c5zy34ms0@f&67lztf1x$aon(5yg52ss1t@(k%0j-'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False

ALLOWED_HOSTS = ['*']
ADMINS = [
 ('Timson F', 'timson@technokraftz.com'),
]
#ALLOWED_HOSTS = ['*']
# DATABASES = {
#  'default': {
#  'ENGINE': 'django.db.backends.sqlite3',
#  'NAME': BASE_DIR / 'db.sqlite3',
#  }
# }
#ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'channels',
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #installed apps
    'courses',
    'students',
    'chat',
    #ext app
    'embed_video',
    'debug_toolbar',
    'redisboard',
    'rest_framework',
    'whitenoise',
    #'dj-database-url',
    
    "crispy_forms",
    #'channels',
    
    

]


MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
   # 'django.contrib.staticfiles.handlers.ASGIStaticFilesHandler',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'educa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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



WSGI_APPLICATION = 'educa.wsgi.application'
ASGI_APPLICATION = 'educa.asgi.application'
#ASGI_APPLICATION = 'django.core.asgi.get_asgi_application'



# Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('POSTGRES_DB'),
#         'USER': os.environ.get('POSTGRES_USER'),
#         'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
#         'HOST': 'db',
#         'PORT': 5432,
#     }
# }
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost/dbname')
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

REDIS_URL = 'redis://cache:6379'




#caching
# CACHES = {
#  'default': {
#  'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
#  'LOCATION': '127.0.0.1:11211',
#  }
# }
# CACHES = {
#  'default': {
#  'BACKEND':  'django.core.cache.backends.redis.RedisCache',
#  'LOCATION': 'redis://127.0.0.1:6379',
#  }
# }
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.environ.get('REDIS_URL', 'redis://localhost:6379'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

#CACHES['default']['LOCATION'] = REDIS_URL

# CHANNEL_LAYERS = {
#  'default': {
#  'BACKEND': 'channels_redis.core.RedisChannelLayer',
#  'CONFIG': {
#  'hosts': [('127.0.0.1', 6379)],
#  },
#  },
# }
#CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]


# Configure Django Channels
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        },
    },
}




CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 60 * 15 # 15 minutes
CACHE_MIDDLEWARE_KEY_PREFIX = 'educa'


# REST
REST_FRAMEWORK = {
 'DEFAULT_PERMISSION_CLASSES': [
 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
 ]
}


# REDIS_URL = 'redis://cache:6379'
# CACHES['default']['LOCATION'] = REDIS_URL
# CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]




# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

#STATIC_ROOT = '/static/'
STATIC_URL = 'static/'
# Tell WhiteNoise where your static files are located
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Add WhiteNoise to the static file finders
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

from django.urls import reverse_lazy
LOGIN_REDIRECT_URL = reverse_lazy('student_course_list')

#DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


INTERNAL_IPS = [
 '127.0.0.1',
] 

CRISPY_TEMPLATE_PACK = 'bootstrap4'  # or 'bootstrap3', depending on your preferred Bootstrap version

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_TRUSTED_ORIGINS = ['https://technokraftz-class.herokuapp.com/']