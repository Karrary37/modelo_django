import json
import pika
from typing import Dict

from core.settings import RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_USERNAME, RABBITMQ_PASSWORD


class RabbitmqPublisher:
    def __int__(self) -> None:
        self.__host = "localhost"
        self.__port = "15670"
        self.__username = "admin"
        self.__password = "123"
        self.__exchange = "data_exchange"
        self.__routing_key = ""
        self.__channel = self.__create_channel()

    def __create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__port,
                password=self.__password
            )
        )
        print(connection_parameters)

        channel = pika.BlockingConnection(connection_parameters).channel()
        print(channel)
        print('--------------------------------------------------------')
        return channel

    def send_message(self, body: Dict):
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        self.__channel.basic_publish(
            exchange=self.__exchange,
            routing_key=self.__routing_key,
            body=json.dumps(body),
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )


def publicar_mensagem_rabbitmq():
    print('======================================')
    print(RABBITMQ_HOST)
    print(RABBITMQ_PORT)
    print(RABBITMQ_USERNAME)
    print(RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        port=RABBITMQ_PORT,
        credentials=pika.PlainCredentials(
            RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
    ))
    print('------------------------------------------------')
    print(connection)
    channel = connection.channel()

    channel.queue_declare(queue='minha_fila')

    mensagem = f'Mensagem para Teste'
    channel.basic_publish(exchange='',
                          routing_key='minha_fila',
                          body=mensagem)

    connection.close()
