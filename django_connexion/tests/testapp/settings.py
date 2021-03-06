from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

USE_TZ = True

SECRET_KEY = 'INSECURE'

DEBUG = True

INSTALLED_APPS = [
    'django_connexion.tests.testapp',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

ROOT_URLCONF = 'django_connexion.tests.testapp.urls'
