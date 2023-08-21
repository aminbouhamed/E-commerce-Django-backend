
from pathlib import Path
import os
import firebase_admin
from firebase_admin import credentials
from .routers import MongoRouter

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import environ 
env=environ.Env()
environ.Env.read_env()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '10.0.2.2']


# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user_auth',
    'rest_framework',
    'admin_auth',
    'event',
    'ModelTracker',
    'notification',
    'review',
    'favoris'
    
    
]


# Path to your Firebase service account key JSON file
service_account_path = os.path.join(BASE_DIR, 'secret.json')

try:
    # Initialize the Firebase Admin SDK
    cred = credentials.Certificate(service_account_path)
    firebase_admin.initialize_app(cred)

    # Print a message to indicate that the Firebase Admin SDK is initialized
    print("Firebase Admin SDK initialized successfully.")
except Exception as e:
    print("Failed to initialize Firebase Admin SDK:", str(e))



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'user_auth.middleware.firebase_auth_middleware',
    'corsheaders.middleware.CorsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
}

ROOT_URLCONF = 'eCommerceProject.urls'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


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

WSGI_APPLICATION = 'eCommerceProject.wsgi.application'

DATABASE_ROUTERS = ['eCommerceProject.routers.MongoRouter']




# settings.py
DATABASES = {
    'default': {
        "ENGINE": "mssql",
        "NAME": "dataB",
        "HOST": "LAPTOP-6CH6ODMJ\SQLEXPRESS",
        "PORT": "",
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server", 
    },
    'mongo': {
        "ENGINE": 'djongo',  
        "CLIENT": {
            'name': 'appdatabase',
            'host' : 'mongodb+srv://aminbouhamed:amin123@cluster0.m2yssz9.mongodb.net/',                              
            'username': 'aminbouhamed',
            'password' : 'amin123'
                    }
    },
}}




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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'




CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True  
