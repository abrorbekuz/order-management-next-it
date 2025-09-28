from .base import *

DEBUG = True
SECRET_KEY = "SALOM"

ALLOWED_HOSTS = ['*']

THIRD_PARTY_APPS = [

    'rest_framework',
    "rest_framework_simplejwt",

    "django_filters",
    'corsheaders',

    'drf_spectacular',
]

INSTALLED_APPS = LOCAL_APPS + THIRD_PARTY_APPS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend"
    ],

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Order Management API",
    "DESCRIPTION": "API for managing orders, stock, and status updates.",
    "VERSION": "1.0.0",
}

SITE_ID = 1

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 0