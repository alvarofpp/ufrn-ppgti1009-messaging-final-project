import logging

from app.enums import QueueEnum
from app.mixins import SingletonMixin
from app.queue import RabbitConsumerBase
import streamlit as st


class OrdersStatusUpdatedConsumer(RabbitConsumerBase, metaclass=SingletonMixin):
    def __init__(self):
        super().__init__()
        self.queue = str(QueueEnum.ORDERS_STATUS_UPDATED.value)

    @staticmethod
    def callback(channel, method, properties, body):
        message = body.decode('utf-8')
        logging.info('RECEIVED: {}'.format(message))

        if message.isdigit():
            # st.experimental_rerun()
            st.info('Order #{} status changes. Refresh the page.'.format(message))
