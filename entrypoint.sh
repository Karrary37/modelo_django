#!/bin/bash
cd app
echo 'Start workers'
celery -A core worker -n fast -c 8 -P gevent -l INFO -Q fast &
celery -A core worker -n medium -c 2 -P gevent -l INFO -Q medium &
echo 'Start Application - Celery and Flower'
echo '------------------'
echo 'Start NGINX'
service nginx start
echo '------------------'
sleep 2
echo 'Start Migrate'
python3 manage.py migrate
echo '------------------'
echo 'Start Collectstatic'
echo '------------------'
python3 manage.py collectstatic
echo 'Start Application - Core'
echo '------------------'
#python3 manage.py runserver
#echo 'Start Runserver'
#echo '------------------'

echo "Starting Gunicorn..."
exec gunicorn core.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 2 \
    --threads 4 \
    --timeout 120