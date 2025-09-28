from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from config import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')

app = Celery('config',  backend='redis://localhost:6379/0', broker='redis://localhost:6379/0',
             broker_connection_retry_on_startup=True)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

