#/usr/bin/env bash

cd $APPLICATION_ROOT\cpoc_web
while ! nc -z db 5432; do sleep 1; done
python manage.py migrate --settings=cpoc_web.settings
python manage.py runserver 0.0.0.0:8000 --settings=cpoc_web.settings
