from app.queue import RabbitBase
from pika import BlockingConnection
from pika.adapters.blocking_connection import BlockingChannel


class RabbitConsumerBase(RabbitBase):
    def _get_channel(self, connection: BlockingConnection) -> BlockingChannel:
        channel = super()._get_channel(connection)
        channel.basic_consume(
            queue=self.queue,
            on_message_callback=self.callback,
            auto_ack=True,
        )

        return channel

    def start_consuming(self) -> None:
        self.channel.start_consuming()

    @staticmethod
    def callback(channel, method, properties, body):
        raise NotImplementedError('You must implement the "callback" method')
