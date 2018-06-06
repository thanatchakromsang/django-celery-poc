#!/usr/bin/env bash

# while IFS='' read -r line || [[ -n "$line" ]]; do line=$(echo $line | sed -e "s/=/='/"); echo export ${line}\' >> $HOME/.env; done < <(env)

cd $APPLICATION_ROOT\cpoc_web
# celery -A tasks worker -l info -B --scheduler django_celery_beat.schedulers:DatabaseScheduler
celery -A cpoc_web worker -l info -Q ${WORKER_QUEUE} -B --scheduler django_celery_beat.schedulers:DatabaseScheduler
