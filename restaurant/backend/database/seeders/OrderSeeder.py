import json
from typing import Dict

from app.models import Item, Order
from database.db import engine
from database.seeders import Seeder


class OrderSeeder(Seeder):

    @staticmethod
    def run():
        with open('storage/app/seed/orders.json') as orders_file:
            orders_data = json.load(orders_file)
            orders = []
            items = []

            for order in orders_data:
                orders.append(OrderSeeder.map(order))
                for item in order['items']:
                    item['order_id'] = order['id']
                    items.append(item)

            engine.execute(Order.__table__.insert(), orders)
            engine.execute(Item.__table__.insert(), items)

    @staticmethod
    def map(data) -> Dict:
        return {
            'id': data['id'],
            'costumer_id': data['costumer_id'],
            'status': data['status'],
            'total_price': data['total_price'],
        }
