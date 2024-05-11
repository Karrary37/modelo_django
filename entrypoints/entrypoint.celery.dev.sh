#!/bin/bash
cd app
echo 'Start workers'
celery -A core worker -n fast -c 8 -P gevent -l INFO -Q fast &
celery -A core worker -n medium -c 2 -P gevent -l INFO -Q medium &
celery -A core worker -n long -c 1 -P gevent -l INFO -Q long &
celery -A core worker -n divide_carteiras -c 1 -P gevent -l INFO -Q divide_carteiras &
celery -A core worker -n NUs -c 1 -P gevent -l INFO -Q NUs &
celery -A core worker -n agio2 -c 1 -P gevent -l INFO -Q agio2 &
celery -A core worker -n pf001 -c 1 -P gevent -l INFO -Q pf001 &

echo 'Start Application - Celery and Flower'
newrelic-admin run-program celery -A core --broker=$CELERY_BROKER_URL flower -l INFO --basic-auth=$FLOWER_BASIC_AUTH --port=80
