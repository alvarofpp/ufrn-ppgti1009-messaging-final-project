from dataclasses import dataclass
from typing import Dict


@dataclass
class Item:
    id: str
    name: str
    description: str
    price: float
    order_id: int

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'order_id': self.order_id,
        }

    @staticmethod
    def create(data: Dict) -> 'Item':
        return Item(
            id=data['id'],
            name=data['name'],
            description=data['description'],
            price=data['price'],
            order_id=data['order_id'],
        )
