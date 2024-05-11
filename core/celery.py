from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from kombu import Queue

# from core.settings import ELASTIC_CACHE_URL
ELASTIC_CACHE_URL = 'redis://localhost:6379'

# Configuração padrão do Django para o programa Celery.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Inicialização do Celery
app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.loader.override_backends[
    'django-db'
] = 'django_celery_results.backends.database:DatabaseBackend'

# Configuração das filas
app.conf.task_queues = (
    Queue('fast', routing_key='fast'),
    Queue('medium', routing_key='medium')
)

app.autodiscover_tasks()

app.conf.broker_url = ELASTIC_CACHE_URL
