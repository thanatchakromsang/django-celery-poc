#!/usr/bin/env bash

cd $APPLICATION_ROOT\cpoc_web
celery -A cpoc_web worker -l info -Q ${WORKER_QUEUE} -n ${WORKER_NAME}
