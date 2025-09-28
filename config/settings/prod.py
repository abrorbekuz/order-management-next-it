from .base import *

from decouple import Config, RepositoryEnv
env = Config(RepositoryEnv(".prod.env"))

DEBUG = env("DEBUG")
ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(",")
SECRET_KEY = env("SECRET_KEY")

THIRD_PARTY_APPS = [
    'rest_framework',
    "rest_framework_simplejwt",

    "django_filters",
    'corsheaders',

    'drf_spectacular',
]

INSTALLED_APPS = LOCAL_APPS + THIRD_PARTY_APPS

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': env('POSTGRES_DB', 'lead_management'),
#         'USER': env('POSTGRES_USER', 'postgres'),
#         'PASSWORD': env('POSTGRES_PASSWORD', 'postgres'),
#         'HOST': env('DB_HOST', 'db'),
#         'PORT': env('DB_PORT', '5432'),
#     }
# }

# hozircha docker ichida ketti osonroq ko'rish uchun
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=env("DJ_DATABASE_URL")
    )
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

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "file": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"},
    },
    "handlers": {
        "file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "formatter": "file",
            "filename": "errors.log",
        },
    },
    "loggers": {
        "": {"level": "ERROR", "handlers": ["file"]},
        "django.request": {"level": "INFO", "handlers": ["file"]},
    },
}

SITE_ID = 1

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 0