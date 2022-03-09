from dataclasses import dataclass
from typing import Dict


@dataclass
class Item:
    id: str
    name: str
    description: str
    price: float
    available: bool
    menu_id: str
    created_at: str
    update_at: str

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'available': self.available,
            'menu_id': self.menu_id,
            'created_at': self.created_at,
            'update_at': self.update_at,
        }
