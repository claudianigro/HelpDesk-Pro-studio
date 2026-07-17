# backend/config/settings.py
import os
from pathlib import Path
from datetime import timedelta

# ----------------------------
# BASE DIRECTORY
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------
# DEBUG & ALLOWED_HOSTS
# ----------------------------
DEBUG = True  # sviluppo locale
ALLOWED_HOSTS = ["*"]  # sviluppo locale, NON usare in produzione

# ----------------------------
# SECRET KEY (sviluppo)
# ----------------------------
SECRET_KEY = "django-insecure-your-secret-key"  # sostituire in produzione

# ----------------------------
# INSTALLED APPS
# ----------------------------
INSTALLED_APPS = [
    # Django base
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Terze parti
    "rest_framework",
    "django_filters",
    "drf_yasg",
    "corsheaders",  # ✅ CORS
    "drf_spectacular",

    # App custom
    "apps.users.apps.UsersConfig",
    "apps.tickets.apps.TicketsConfig",
    "apps.comments.apps.CommentsConfig",
    "apps.categories.apps.CategoriesConfig",
    "apps.ai_service.apps.AiServiceConfig",
]

# ----------------------------
# MIDDLEWARE
# ----------------------------
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # ✅ CORS PRIMA di CommonMiddleware
    "django.middleware.common.CommonMiddleware",

    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ----------------------------
# ROOT URLCONF
# ----------------------------
ROOT_URLCONF = "config.urls"

# ----------------------------
# TEMPLATES
# ----------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ----------------------------
# WSGI
# ----------------------------
WSGI_APPLICATION = "config.wsgi.application"

# ----------------------------
# DATABASE (sviluppo sqlite)
# ----------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ----------------------------
# AUTH USER MODEL
# ----------------------------
AUTH_USER_MODEL = "users.CustomUser"

# ----------------------------
# PASSWORD VALIDATION
# ----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ----------------------------
# INTERNATIONALIZATION
# ----------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ----------------------------
# STATIC FILES
# ----------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# ----------------------------
# REST FRAMEWORK + JWT
# ----------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# ----------------------------
# CORS CONFIGURATION
# ----------------------------
# Opzione sviluppo locale: React su localhost:3000 e 5173
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

# Per sviluppo rapido, meno sicuro:
# CORS_ALLOW_ALL_ORIGINS = True

# Permette header Authorization con credenziali
CORS_ALLOW_CREDENTIALS = True

# ----------------------------
# DEFAULT AUTO FIELD
# ----------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ----------------------------
# SWAGGER (DRF-YASG) CONFIG
# ----------------------------
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
    'USE_SESSION_AUTH': False,
}