#!/usr/bin/env bash

cd $APPLICATION_ROOT\cpoc_web
celery -A cpoc_web beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
