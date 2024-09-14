from .base import *

DEBUG = False

ALLOWED_HOSTS = ['167.172.224.226']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

# S3 settings
USE_S3 = True

# Security settings
SECURE_SSL_REDIRECT = False  # Change this to True once you have HTTPS set up
SESSION_COOKIE_SECURE = False  # Change this to True once you have HTTPS set up
CSRF_COOKIE_SECURE = False  # Change this to True once you have HTTPS set up