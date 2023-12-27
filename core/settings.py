from pathlib import Path
import os, dj_database_url, dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent
dotenv.load_dotenv(os.path.join(BASE_DIR / ".eVar", ".env"))

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG") == "True"
ALLOWED_HOSTS = [
    ".vercel.app",
    "127.0.0.1",
]

STATICFILES_DIRS = [BASE_DIR / "ui" / "static"]
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "ui" / "staticfiles"

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "home",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "ui" / "templates"],
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

WSGI_APPLICATION = "core.wsgi.application"


# Database

DATABASES = {
    "prod": dj_database_url.config(),
    "dev": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("DEV_DB_NAME"),
        "USER": os.environ.get("DEV_DB_USER"),
        "PASSWORD": os.environ.get("DEV_DB_PASS"),
        "HOST": os.environ.get("DEV_DB_HOST"),
        "PORT": os.environ.get("DEV_DB_PORT"),
    },
}
DATABASES["default"] = DATABASES["dev" if DEBUG else "prod"]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
