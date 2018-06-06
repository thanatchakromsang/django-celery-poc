#!/usr/bin/env bash

cd cpoc_web
celery -A cpoc_web worker -l info
