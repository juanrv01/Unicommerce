"""
Django settings for Unicommerce project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

import cloudinary
import cloudinary.uploader
import cloudinary.api
from pathlib import Path
from datetime import timedelta
import os, environ
import dj_database_url
import stripe

STRIPE_API_KEY = os.environ.get('sk_test_51N4C2MCnAe4mWFw2TKo8V3gkpZAfU7YE7oJF0MAJUZakxSOjm6jXC01q2knSLXfNI0moAvwoSF9Vhm9setmKAqJ400kB90PKWO')
STRIPE_API_SECRET = os.environ.get('pk_test_51N4C2MCnAe4mWFw2fLdkdIxaFOibNbuLjEBZRWOUmLEXyK68JmvmAr5aKhisWfsiaXaZTzz6z6uysSrNeAWwCsf1001cwsuWQq')
stripe.api_key='sk_test_51N4C2MCnAe4mWFw2TKo8V3gkpZAfU7YE7oJF0MAJUZakxSOjm6jXC01q2knSLXfNI0moAvwoSF9Vhm9setmKAqJ400kB90PKWO'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# initialize environment variables
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4(!ryx6%+j6$v4_f13+_%dc&k&-5+5(@ju73o00z4@@)n74#uy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', default=False)

ALLOWED_HOSTS = ['* ']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'users',
    'products',
    'cart',
    'orders',
    'docs',
    'rest_framework',
    'corsheaders',
    'django_filters',
    'drf_spectacular',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Unicommerce.urls'

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS=[
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:8000',
    'https://checkout.stripe.com',
    'https://checkout.stripe.com',
    'http://localhost:5173'

]
CORS_ALLOWED_ORIGIN_REGEXES = [
    'http://localhost:3000',
]
CORS_ALLOW_METHODS = [
'DELETE',
'GET',
'OPTIONS',
'PATCH',
'POST',
'PUT',
]


SITE_URL = 'http://localhost:3000'
ROOT_URLCONF = 'Unicommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Unicommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.postgresql',
    #    'NAME': 'unicommerce_db',
    #    'USER': 'postgres',
    #    'PASSWORD': 'password123',
    #    'HOST': 'localhost',  # Si está en tu máquina local
    #    'PORT': '5432',  # Puerto por defecto de PostgreSQL
    #}
    'default': dj_database_url.config(
        default=env('DATABASE_URL')
    )

}


AUTH_USER_MODEL = 'users.CustomUser'


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'
# This production code might break development mode, so we check whether we're in DEBUG mode
if not DEBUG:
    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

cloudinary.config(
  cloud_name = "ddk98mjzn",
  api_key = "645519149712985",
  api_secret = "A_bL776CwLO54Elq8AoeyTLBlmM"
)

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=15),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "SIGNING_KEY": 'somesecretsecretsomekeysecret',
}



STRIPE_SECRET_WEBHOOK='whsec_03ce6b586620eec93594579b709130478dcfcaad93cfd2cf2f75f64f10d6c397'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

JAZZMIN_SETTINGS = {
    "site_title": "E-Commerce Dashboard",
    
    "site_header": "E-Commerce Dashboard",
    
        "site_brand": "E-Commerce Admin",

    "login_logo": 'images.png',
    "site_logo": "images.png",
    
    "welcome_sign": "Welcome to the e-commerce Dashboard ITI",

    "copyright": "e-commerce Dashboard ITI",
    
        "search_model": ["auth.User", "auth.Group"],
        
        
      "topmenu_links": [

        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        {"model": "auth.User"},

        {"app": "books"},
    ],
}