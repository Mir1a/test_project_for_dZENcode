# region				-----External Imports-----
import os
from dotenv import load_dotenv
# endregion

# region				-----Internal Imports-----
from .django import *
from .third_party import *
# endregion

load_dotenv()

SECRET_KEY = 'django-insecure-f3b^5-n1zgjz&(6vl=uykrs6kppw1k)xov8)y^**!d0a-zp!l^'

DEBUG = True

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1,0.0.0.0').split(',')

DATABASES = {
    'default': {
        'PASSWORD': os.environ.get('DB_PASS'),
        'HOST': os.environ.get('DB_HOST'),
        'NAME': os.environ.get('DB_NAME'),
        'PORT': os.environ.get('DB_PORT'),
        'USER': os.environ.get('DB_USER'),
        'ENGINE': 'django.db.backends.postgresql',
        'ATOMIC_REQUESTS': True,
        'TEST': {
            'NAME': 'tests',
        },
    }
}

print(">>> START PROJECT WITH LOCAL SETTINGS <<<")