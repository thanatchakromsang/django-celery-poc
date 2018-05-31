#!/usr/bin/env bash

cd cpoc_web
celery -A tasks worker -l info
