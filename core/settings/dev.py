from .base import *

# Development-specific settings
DEBUG = True

ALLOWED_HOSTS = ['*']

# Example: you can use SQLite for local development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SECURE_SSL_REDIRECT = False