import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cpoc_web.settings')

app = Celery('cpoc_web')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
