import json
import pika
import traceback

from core.settings import RABBITMQ_AMQP_URL


class RabbitMQPublisher:
    def __init__(self):
        self.amqp_url = RABBITMQ_AMQP_URL
        self.connection = None
        self.channel = None

    def connect(self):
        try:
            parameters = pika.URLParameters(self.amqp_url)
            self.connection = pika.BlockingConnection(parameters)
            self.channel = self.connection.channel()
            print('Connected to RabbitMQ')
        except Exception as e:
            print(f'Connection error: {traceback.format_exc()} |'
                  f' Line: {e.__traceback__.tb_lineno}')
            raise

    def declare_exchange(self, exchange_name, exchange_type='direct', durable=True):
        try:
            if not self.channel:
                raise Exception("Channel is not established."
                                " Call connect() first.")
            self.channel.exchange_declare(
                exchange=exchange_name,
                exchange_type=exchange_type,
                durable=durable)
            print(f'Exchange {exchange_name} declared')
        except Exception as e:
            print(f'Exchange declaration error: {traceback.format_exc()} |'
                  f' Line: {e.__traceback__.tb_lineno}')
            raise

    def publish_message(self, exchange_name, routing_key, message):
        try:
            if not self.channel:
                raise Exception("Channel is not established. Call connect() first.")
            body = json.dumps(message)
            self.channel.basic_publish(
                exchange=exchange_name,
                routing_key=routing_key,
                body=body,
                properties=pika.BasicProperties(delivery_mode=2)
            )
            print('Message published')
        except Exception as e:
            print(f'Publishing error: {traceback.format_exc()} |'
                  f' Line: {e.__traceback__.tb_lineno}')
            raise

    def close(self):
        if self.connection and not self.connection.is_closed:
            self.connection.close()
            print('Connection closed')
