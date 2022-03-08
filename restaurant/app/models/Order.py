from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Order:
    id: str
    costumer_id: str
    status: str
    total_price: float
    items: List
    created_at: str
    update_at: str

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'costumer_id': self.costumer_id,
            'status': self.status,
            'total_price': self.total_price,
            'items': self.items,
            'created_at': self.created_at,
            'update_at': self.update_at,
        }
