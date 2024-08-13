# region				-----External Imports-----
import os
# endregion

# region				-----Internal Imports-----
from .django import *
from .third_party import *
# endregion

SECRET_KEY = 'django-insecure-f3b^5-n1zgj1z&(6vl=uykrs6kppw1k)xov8)y^**!d0a-zp!l^'

DEBUG = False

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')\
                + ["185.174.101.137"]

DATABASES = {
    'default': {
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'NAME': os.environ.get('DATABASE_NAME'),
        'PORT': os.environ.get('DATABASE_PORT'),
        'USER': os.environ.get('DATABASE_USER'),
        'ENGINE': os.environ.get('ENGINE'),
        'ATOMIC_REQUESTS': True
    }
}

# CORS
INSTALLED_APPS += ['corsheaders']

MIDDLEWARE.insert(
    MIDDLEWARE.index('django.middleware.common.CommonMiddleware') - 1,
    'corsheaders.middleware.CorsMiddleware'
)

CORS_ALLOWED_ORIGINS = [
    'http://185.174.101.137',
    'https://185.174.101.137',
    'http://127.0.0.1:3000',
    'http://127.0.0.1:5173',
    'http://127.0.0.1',
    'http://localhost:3000',
    'http://localhost:5173',
    'http://localhost'
]

CSRF_TRUSTED_ORIGINS = [
    'http://185.174.101.137',
    'https://185.174.101.137',
    'http://127.0.0.1:3000',
    'http://127.0.0.1:5173',
    'http://127.0.0.1',
    'http://localhost:3000',
    'http://localhost:5173',
    'http://localhost'
]

CSRF_COOKIE_DOMAIN = '185.174.101.137'
# 500 middleware

print(">>> START PROJECT WITH PROD SETTINGS <<<")
