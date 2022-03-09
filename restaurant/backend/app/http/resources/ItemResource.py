from typing import Dict

from app.models import Item
from pydantic import BaseModel, Field


class ItemResource(BaseModel):
    id: int = Field(
        None,
        title='Item identifier',
    )
    name: str = Field(
        None,
        title='Name',
    )
    description: str = Field(
        None,
        title='Description',
    )
    price: float = Field(
        None,
        title='Price',
    )
    order_id: int = Field(
        None,
        title='Order identifier',
    )

    @staticmethod
    def to_dict(item: Item) -> Dict:
        return {
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'price': item.price,
            'order_id': item.order_id,
        }
