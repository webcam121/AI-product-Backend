import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from boto3.session import Session

from .base import *  # noqa

DEBUG = False

sentry_sdk.init(
    dsn="https://612639e1937b41d8a994ebfa26c7c1d3@o1181905.ingest.sentry.io/6418670",
    integrations=[DjangoIntegration()],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
    before_send=before_send,  # noqa
)

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'ai-product-api-staging-env.eba-czbwjitv.us-east-2.elasticbeanstalk.com',
    'ai-product-frontend-staging-env.eba-hnupms6p.us-east-2.elasticbeanstalk.com'
]

ec2_instance_ip = get_ec2_instance_ip()  # noqa
if ec2_instance_ip:
    ALLOWED_HOSTS.append(ec2_instance_ip)

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

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

# django-s3-storage settings
AWS_REGION = 'us-east-2'
AWS_S3_BUCKET_AUTH = False
AWS_S3_REGION_NAME = 'us-east-2'
AWS_S3_MAX_AGE_SECONDS = 60 * 60 * 24 * 365
DEFAULT_FILE_STORAGE = 'django_s3_storage.storage.S3Storage'
AWS_S3_BUCKET_NAME = 'AI-product-backend-api-client-assets'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_S3_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

STATICFILES_LOCATION = 'static'
AWS_LOCATION = 'static'
STATICFILES_STORAGE = 'aiproduct.storage_backends.StaticStorage'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
AWS_PUBLIC_STATIC_STORAGE_BUCKET_NAME = 'ai-product-backend-public-assets-staging'

SECURE_BROWSER_XSS_FILTER = True

# https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-USE_X_FORWARDED_HOST
USE_X_FORWARDED_HOST = True

# https://docs.djangoproject.com/en/3.1/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = True

# https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-SESSION_COOKIE_SECURE
SESSION_COOKIE_SECURE = True

# https://docs.djangoproject.com/en/3.1/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True

# https://docs.djangoproject.com/en/3.1/ref/middleware/#http-strict-transport-security
SECURE_HSTS_SECONDS = 60

# https://docs.djangoproject.com/en/3.1/ref/settings/#secure-hsts-preload
SECURE_HSTS_PRELOAD = True

# https://docs.djangoproject.com/en/3.1/ref/settings/#secure-hsts-include-subdomains
# enforcing https on request through subdomain
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CORS_ORIGIN_ALLOW_ALL = False

CSRF_TRUSTED_ORIGINS = [
    'https://ai-product-frontend-staging-env.eba-hnupms6p.us-east-2.elasticbeanstalk.com',
]

CORS_ALLOWED_ORIGINS = [
    'https://ai-product-frontend-staging-env.eba-hnupms6p.us-east-2.elasticbeanstalk.com'
]
FRONTEND_BASE_URL = 'https://ai-product-frontend-staging-env.eba-hnupms6p.us-east-2.elasticbeanstalk.com/'

ENVIRONMENT = 'production'

INSTALLED_APPS.append('django_extensions')  # noqa

boto3_session = Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_REGION
)