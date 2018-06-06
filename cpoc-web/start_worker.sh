#!/usr/bin/env bash

cd cpoc_web
celery -A cpoc_web worker -l info -Q ${WORKER_QUEUE} -B --scheduler django_celery_beat.schedulers:DatabaseScheduler
