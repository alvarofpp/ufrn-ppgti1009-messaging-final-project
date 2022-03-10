import logging

from app import SessionState
from app.enums import QueueEnum
from app.queue import RabbitConsumerBase
import streamlit as st


class OrdersCreatedConsumer(RabbitConsumerBase):
    def __init__(self):
        super().__init__()
        self.queue = str(QueueEnum.ORDERS_CREATED)

    @staticmethod
    def callback(channel, method, properties, body):
        message = body.decode('utf-8')
        logging.info('RECEIVED: {}'.format(message))

        if message.isdigit():
            st.experimental_rerun()
            st.info('You have received a new order (#{}). Refresh the page.'.format(message))
            SessionState.set('order_id', int(message))
