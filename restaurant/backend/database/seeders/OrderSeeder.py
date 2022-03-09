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

            OrderSeeder.start_id_seq('orders')
            OrderSeeder.start_id_seq('items')

    @staticmethod
    def start_id_seq(table: str):
        query_id_seq = 'SELECT setval(\'{}_id_seq\', max(id)+1) FROM {};'
        engine.execute(query_id_seq.format(table, table))

    @staticmethod
    def map(data) -> Dict:
        return {
            'id': data['id'],
            'customer_id': data['customer_id'],
            'status': data['status'],
            'total_price': data['total_price'],
        }
