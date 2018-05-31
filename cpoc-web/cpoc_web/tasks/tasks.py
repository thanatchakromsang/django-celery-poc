import string

from django.utils.crypto import get_random_string

from celery import shared_task


@shared_task
def create_random_word():
    random_word = get_random_string(12)
    return '{}'.format(random_word)
