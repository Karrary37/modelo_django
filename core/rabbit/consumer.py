import pika


class RabbitmqConsumer:
    def __int__(self) -> None:
        self.__host = "localhost"
        self.__port = "15670"
        self.__username = "admin"
        self.__password = "123"
        self.__queue = "data_queue"
        self.__callback = callback
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

        channel = pika.BlockingConnection(connection_parameters).channel()
        channel.queue_declare(
            queue=self.__queue,
            durable=True,
        )

        channel.basic_consumer(
            queue=self.__queue,
            auto_ack=True,
            on_message_callback=self.__callback
        )

        return channel

    def start(self):
        print('-----------------------------------------------')
        print('Ouvindo porta 15670')
        channel.start_consuming()


def minha_callback(ch, method, properties, body):
    print(body)
