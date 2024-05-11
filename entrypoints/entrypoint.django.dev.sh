#!/bin/bash
cd app
echo 'Start NGINX'
service nginx start
echo '------------------'
sleep 2
echo 'Start Migrate'
python3 manage.py migrate
echo '------------------'
echo 'Start Collectstatic'
python3 manage.py collectstatic
echo 'Start Application - Core'
newrelic-admin run-program \
    gunicorn core.wsgi:application \
        --bind ${GUNICORNADDRESS}:${GUNICORNPORT} \
        --workers 2 \
        --threads 4 \
        --timeout 120 \
        --reload
