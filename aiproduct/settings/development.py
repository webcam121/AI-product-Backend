from boto3 import Session

from .base import *  # noqa

DEBUG = True

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    "localhost"
    # ...
]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'PORT': 5432,
    }
}


CORS_ORIGIN_ALLOW_ALL = True
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False

ENVIRONMENT = 'development'

FRONTEND_BASE_URL = 'http://localhost:3000/'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

# django-s3-storage settings
AWS_REGION = 'us-east-2'
AWS_S3_BUCKET_AUTH = False
AWS_S3_REGION_NAME = 'us-east-2'
AWS_S3_MAX_AGE_SECONDS = 60 * 60 * 24 * 365
DEFAULT_FILE_STORAGE = 'django_s3_storage.storage.S3Storage'
AWS_S3_SIGNATURE_VERSION = 's3v4'

AWS_S3_BUCKET_NAME = 'AI-product-backend-api-client-assets'


STATICFILES_LOCATION = 'static'
AWS_PUBLIC_STATIC_STORAGE_BUCKET_NAME = 'ai-product-backend-public-assets-staging'

INSTALLED_APPS.append('django_extensions')  # noqa

SITE_URL = 'http://localhost:8000'

# CELERY settings
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

boto3_session = Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_REGION
)
