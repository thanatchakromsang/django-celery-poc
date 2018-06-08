from __future__ import absolute_import
import os
from celery import Celery
# from kombu import Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cpoc_web.settings')

app = Celery('cpoc_web')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.task_default_queue = 'queue_a'
app.conf.task_routes = {
    'tasks.tasks.create_random_word': {
        'queue': 'queue_a'
    },
    'tasks.tasks.create_random_word_long': {
        'queue': 'queue_b'
    }
}

## We can use kombu instead if we need more control
# app.conf.task_queues = (
#     Queue('queue_a', routing_key='tasks.tasks.create_random_word'),
#     Queue('queue_b', routing_key='tasks.tasks.create_random_word_long'),
#     Queue('queue_c', routing_key='tasks.tasks.create_random_word_periodic')
# )


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# WorkerQueue
class DynamicQueue(object):
    def add_consumer(queue):
        app.control.add_consumer(queue, reply=True)

    def cancel_consumer(queue):
        app.control.cancel_consumer(queue, reply=True)
