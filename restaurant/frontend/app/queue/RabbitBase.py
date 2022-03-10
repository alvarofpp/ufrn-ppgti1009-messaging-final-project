import logging

from app.config import get_config
from pika import BlockingConnection, ConnectionParameters
from pika.adapters.blocking_connection import BlockingChannel
from pika.credentials import PlainCredentials


class RabbitBase:
    def __init__(self):
        self.channel = None
        self.queue = None

    def _get_connection(self) -> BlockingConnection:
        credentials = PlainCredentials(
            username=get_config('rabbitmq.user'),
            password=get_config('rabbitmq.password'),
        )
        parameters = ConnectionParameters(
            host=get_config('rabbitmq.host'),
            port=get_config('rabbitmq.port'),
            credentials=credentials,
        )
        return BlockingConnection(parameters)

    def _get_channel(self, connection: BlockingConnection) -> BlockingChannel:
        channel = connection.channel()
        channel.queue_declare(queue=self.queue)

        return channel

    def init(self) -> 'RabbitBase':
        connection = self._get_connection()
        self.channel = self._get_channel(connection)
        return self

    def close(self) -> None:
        if self.channel is not None:
            self.channel.close()
            logging.info('Channel closed!')
