from django.core.management.base import BaseCommand

from core.rabbit.consumer import RabbitMQConsumer


class Command(BaseCommand):
    help = 'Inicia consumidor do RabbitMQ'

    def handle(self, *args, **options):

        try:
            RabbitMQConsumer()
            self.stdout.write(self.style.SUCCESS('Starting RabbitMQ consumer...'))
        except KeyboardInterrupt:
            self.stdout.write(self.style.SUCCESS('RabbitMQ consumer stopped.'))
