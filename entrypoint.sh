#!/bin/bash
if [[ $CNAME == 'celery-small' ]]
then
    echo 'Start workers'
    celery -A core worker -n fast -c 5 -P gevent -l info -Q fast --detach

    echo 'Start Application - Celery'
    newrelic-admin run-program \
        celery \
        -A core worker \
        -P gevent \
        -c 5 \
        -n %h-01 \
        -l info \
        -Q celery
elif [[ $CNAME == 'celery-medium' ]]
then
    echo 'Start Application - Celery'
    newrelic-admin run-program \
        celery \
        -A core worker \
        -P gevent \
        -c 5 \
        -n %h-01 \
        -l info \
        -Q medium
elif [[ $CNAME == 'celery-large' ]]
then
    echo 'Start Application - Celery'
    newrelic-admin run-program \
        celery \
        -A core worker \
        -P gevent \
        -c 5 \
        -n %h-01 \
        -l info \
        -Q long
elif [[ $CNAME == 'celery-joker' ]]
then
    echo 'Start workers'
    celery -A core worker -n agio2 -c 4 -P gevent -l info -Q agio2 --detach
    celery -A core worker -n NUs -c 4 -P gevent -l info -Q NUs --detach
    celery -A core worker -n divide_carteiras -c 1 -P gevent -l info -Q divide_carteiras --detach
    celery -A core worker -n pf001 -c 2 -P gevent -l info -Q pf001 --detach

    echo 'Start Application - Celery'
    newrelic-admin run-program \
        celery \
        -A core worker \
        -P gevent \
        -c 1 \
        -n %h-01 \
        -l info \
        -Q celery
elif [[ $CNAME == 'celery' ]]
then
    echo 'Start workers'
    celery -A core worker -n fast -c 8 -P gevent -l info -Q fast --detach
    celery -A core worker -n medium -c 2 -P gevent -l info -Q medium --detach
    celery -A core worker -n long -c 1 -P gevent -l info -Q long --detach
    celery -A core worker -n divide_carteiras -c 1 -P gevent -l info -Q divide_carteiras --detach
    celery -A core worker -n NUs -c 1 -P gevent -l info -Q NUs --detach
    celery -A core worker -n agio2 -c 1 -P gevent -l info -Q agio2 --detach
    celery -A core worker -n pf001 -c 2 -P gevent -l info -Q pf001 --detach
    celery -A core worker --beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

    echo 'Start Application - Celery'
    newrelic-admin run-program \
        celery \
        -A core worker \
        -P gevent \
        -c 8 \
        -n %h-01 \
        -l info \
        -Q celery

elif [[ $CNAME == 'flower' ]]
then
    echo 'Start Application - Celery and Flower'
    newrelic-admin run-program celery -A core --broker=$CELERY_BROKER_URL flower --basic-auth=$FLOWER_BASIC_AUTH --port=80

elif [[ $CNAME == 'gerar_lotes' ]]
then
    echo 'Start Gerar Lotes'
    python manage.py gerar_lotes
    echo 'Stop Gerar Lotes'
elif [[ $CNAME == 'atualizar_dynamo_roteador' ]]
then
    echo 'Start Atualizar Contrato(s) Roteador'
    python manage.py atualizar_dynamo_roteador
    echo 'Stop Atualizar Contrato(s) Roteador'
elif [[ $CNAME == 'consumer' ]]
then
    newrelic-admin run-program python manage.py startconsumer
else
    echo 'Start NGINX'
    service nginx start
    echo '------------------'
    sleep 2
    echo 'Start Migrate'
    python manage.py migrate
    python manage.py migrate --database=audit
    echo '------------------'
    echo 'Start Collectstatic'
    python manage.py collectstatic
    echo '------------------'
    echo 'Start Application - Core'
    newrelic-admin run-program \
        gunicorn core.wsgi:application \
            --bind ${GUNICORNADDRESS}:${GUNICORNPORT} \
            --workers 2 \
            --threads 4 \
            --timeout 120
fi
