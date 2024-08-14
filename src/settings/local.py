# region				-----External Imports-----
import os
from dotenv import load_dotenv
from pathlib import Path
# endregion

# region				-----Internal Imports-----
from .django import *
from .third_party import *
# endregion

load_dotenv()

SECRET_KEY = 'django-insecure-f3b^5-n1zgjz&(6vl=uykrs6kppw1k)xov8)y^**!d0a-zp!l^'

DEBUG = True

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1,0.0.0.0').split(',')

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': 'localhost',
            'PORT': '5432',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASS'),
        }
    }

print(">>> START PROJECT WITH LOCAL SETTINGS <<<")