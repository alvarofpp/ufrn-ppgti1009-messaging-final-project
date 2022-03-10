from app.queue import RabbitBase


class RabbitProducerBase(RabbitBase):
    def send(self, message: str) -> None:
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue,
            body=message.encode(),
        )
