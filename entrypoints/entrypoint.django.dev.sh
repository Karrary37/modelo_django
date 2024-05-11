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
echo '------------------'
python3 manage.py collectstatic
echo 'Start Application - Core'
echo '------------------'
python3 manage.py runserver
echo 'Start Runserver'
echo '------------------'
