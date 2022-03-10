from app.enums import QueueEnum
from app.queue import RabbitConsumerBase


class OrdersStatusUpdatedProducer(RabbitConsumerBase):
    def __init__(self):
        super().__init__()
        self.queue = str(QueueEnum.ORDERS_STATUS_UPDATED.value)

    def send(self, message: str) -> None:
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue,
            body=message.encode(),
        )
