import logging

from decouple import config
from pika import BlockingConnection, ConnectionParameters
from pika.adapters.blocking_connection import BlockingChannel
from pika.credentials import PlainCredentials


class RabbitClient:
    def __init__(self):
        self.channel = None

    def _get_connection(self) -> BlockingConnection:
        credentials = PlainCredentials(
            username=config('RABBITMQ_USER', 'guest'),
            password=config('RABBITMQ_PASSWORD', 'guest'),
        )
        parameters = ConnectionParameters(
            host=config('RABBITMQ_HOST', 'localhost'),
            port=config('RABBITMQ_PORT', 5672),
            credentials=credentials,
        )
        return BlockingConnection(parameters)

    def _get_channel(self, connection: BlockingConnection) -> BlockingChannel:
        channel = connection.channel()
        queue = config('RABBITMQ_QUEUE', 'default')
        channel.queue_declare(queue=queue)

        return channel

    def init(self) -> None:
        connection = self._get_connection()
        self.channel = self._get_channel(connection)

    def close(self) -> None:
        if self.channel is not None:
            self.channel.close()
            logging.info('Channel closed!')

    def send(self, message: str) -> None:
        self.channel.basic_publish(
            exchange='',
            routing_key=config('RABBITMQ_QUEUE', 'default'),
            body=message.encode(),
        )
