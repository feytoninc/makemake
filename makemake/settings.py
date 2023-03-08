from decouple import config
from pathlib import Path
import cloudinary
import cloudinary.api
import cloudinary.uploader

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-d3cz#^dzq^6i(__o41!*ac2%gu+u00##vh7s8ouc6arzbm8i7b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "django.contrib.humanize",
    'django.contrib.staticfiles',
    "django.contrib.sites",
    'index',
    'user',
    'cloudinary',
    # CK Editor
    'tinymce',
    # AllAuth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'makemake.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/"templates",],
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

WSGI_APPLICATION = 'makemake.wsgi.application'
RUN_MODE = config("MODE", default="development")

if RUN_MODE == "production":
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    DEBUG = False
    APPEND_SLASH = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


STATIC_URL = '/static/'
DEFAULT_STATIC = BASE_DIR/"assets"
STATIC_ROOT = config("STATIC_ROOT", default=DEFAULT_STATIC)
STATICFILES_DIRS = [BASE_DIR/"static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR/"media"


# REGISTRATION-LOGIN URLS
LOGIN_URL = 'account_login'
LOGOUT_URL = 'account_logout'
LOGIN_REDIRECT_URL = 'index'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)
cloudinary.config(cloud_name=config("cloud_name"), api_key=config(
    "api_key"), api_secret=config("api_secret"), secure=True)


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'user.User'
# All Auth SETTINGS
SIGNUP_FORM_CLASS = 'user.forms.CreateUserForm'
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
SOCIALACCOUNT_AUTO_SIGNUP = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_FORM_CLASS = SIGNUP_FORM_CLASS
ACCOUNT_LOGIN_ON_EMAIL_COMFIRMATION = True
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'Certified Builders |'


def ACCOUNT_USER_DISPLAY(user):
    return user.get_full_name()


SITE_ID = 1
