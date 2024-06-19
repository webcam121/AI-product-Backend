from __future__ import absolute_import

import os

from celery import Celery
from celery.schedules import crontab
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

app = Celery('aiproduct')

tasks = {}

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every_day_get_AI_product': {
        'task': 'aiproduct.apps.product.tasks.scrape_and_insert_ai_product_data',
        'schedule': crontab(minute=0, hour=0),
    },
}