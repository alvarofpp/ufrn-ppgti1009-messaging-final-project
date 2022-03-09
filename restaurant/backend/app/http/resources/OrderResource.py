from typing import List

from app.http.resources import ItemResource
from app.models import Order
from pydantic import BaseModel, Field


class OrderResource(BaseModel):
    id: int = Field(
        None,
        title='Order identifier',
    )
    customer_id: int = Field(
        None,
        title='Customer identifier',
    )
    status: str = Field(
        None,
        title='Order status',
    )
    total_price: float = Field(
        None,
        title='Order total price',
    )
    items: List[ItemResource] = Field(
        None,
        title='A list of items',
    )

    @staticmethod
    def to_dict(order: Order):
        print(order.items)
        data = {
            'id': order.id,
            'customer_id': order.customer_id,
            'status': order.status,
            'total_price': order.total_price,
            'items': [ItemResource.to_dict(item) for item in order.items],
        }

        return data
