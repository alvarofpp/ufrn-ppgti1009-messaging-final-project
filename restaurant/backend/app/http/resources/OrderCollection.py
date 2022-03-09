from typing import List

from app.http.resources import OrderResource
from app.models import Order
from pydantic import BaseModel, Field


class OrderCollection(BaseModel):
    data: List[OrderResource] = Field(
        None,
        title='A list with orders',
    )

    @staticmethod
    def to_dict(orders: List[Order]):
        return {
            'data': [OrderResource.to_dict(order) for order in orders],
        }
