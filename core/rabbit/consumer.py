import pika
import traceback


from core.settings import RABBITMQ_AMQP_URL


def printar_teste(ch, method, properties, body):
    print(f'Consumindo Mensagem | {body}')


class RabbitMQConsumer:
    def __init__(self):
        try:
            parameters = pika.URLParameters(RABBITMQ_AMQP_URL)
            channel = pika.BlockingConnection(parameters).channel()
            channel.queue_declare(
                queue="data_exchange",
                durable=True,
            )

            channel.exchange_declare(
                exchange="data_exchange",
                durable=True,
            )
            # Declara a fila
            queue = channel.queue_declare(
                queue="data_exchange", durable=True, exclusive=False
            )
            # Declara o bind da fila com a exchange
            channel.queue_bind(
                exchange="data_exchange",
                queue=queue.method.queue,
            )
            # Declara o consumo da fila
            channel.basic_consume(
                queue=queue.method.queue,
                on_message_callback=printar_teste,
                auto_ack=True,
            )
            channel.start_consuming()

        except Exception as e:
            print(f'ERRO {traceback.format_exc()} | {e.__traceback__.tb_lineno}')
