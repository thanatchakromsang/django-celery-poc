import time
from django.utils.crypto import get_random_string

from celery import shared_task


@shared_task
def create_random_word():
    random_word = get_random_string(12)
    return '{}'.format(random_word)


@shared_task
def create_random_word_long():
    time.sleep(60)
    random_word = get_random_string(12)
    return '{}'.format(random_word)
