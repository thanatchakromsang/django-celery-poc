from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cpoc_web.settings')

app = Celery('cpoc_web')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# app.conf.task_default_queue = 'queue_a'
app.conf.task_routes = {
    'tasks.tasks.create_random_word': {
        'queue': 'queue_a'
    },
    'tasks.tasks.create_random_word_long': {
        'queue': 'queue_b'
    },
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
