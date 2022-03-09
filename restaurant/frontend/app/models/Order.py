from app.models import Item
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Order:
    id: str
    customer_id: str
    status: str
    total_price: float
    items: List[Item]

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'status': self.status,
            'total_price': self.total_price,
            'items': self.items,
        }

    @staticmethod
    def create(data: Dict) -> 'Order':
        if 'items' not in data.keys():
            data['items'] = []

        if data['items'] is None:
            data['items'] = []

        return Order(
            id=data['id'],
            customer_id=data['customer_id'],
            status=data['status'],
            total_price=data['total_price'],
            items=[Item.create(item) for item in data['items']],
        )
