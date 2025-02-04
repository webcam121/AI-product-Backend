from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
    bucket_name = settings.AWS_PUBLIC_STATIC_STORAGE_BUCKET_NAME
    custom_domain = '{}.s3.amazonaws.com'.format(bucket_name)
