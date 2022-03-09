from typing import List

from app.config import get_config
from app.models import Order
import requests


class OrderService:

    def __init__(self):
        config_service = get_config('services.orders')
        self.backend_url = 'http://{}:{}'.format(
            config_service['host'],
            config_service['port'],
        )

    def get_all(self) -> List[Order]:
        orders = requests.get(self.backend_url + '/v1/orders').json()['data']
        return [Order.create(order) for order in orders]
