from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Tashkent')
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
# Celery beat settings
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-email-every-day-at-8': {
        'task': 'apps.main.send_email.send_email_date',
        'schedule': crontab(minute='*/1'),
        # 'args': ()
    }
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
