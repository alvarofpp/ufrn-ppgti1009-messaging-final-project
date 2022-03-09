from typing import List

from app.enums import OrderStatusEnum
from app.http.requests import BaseRequest
from app.http.requests.inputs import ItemInput
from pydantic import Field, validator


class StoreRequest(BaseRequest):
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
        title='Total price',
    )
    items: List[ItemInput] = Field(
        None,
        title='A item list',
        min_items=1,
    )

    @validator('status')
    def name_must_be_at_least_five_chars(cls, value: str) -> str:
        if value not in OrderStatusEnum.list():
            raise ValueError('Status invalid')

        return value

    class Config:
        schema_extra = {
            'example': {
                'customer_id': 1,
                'status': OrderStatusEnum.ORDER_NEW,
                'total_price': 15.0,
                'items': [
                    {
                        'name': 'Item 1',
                        'description': 'Lorem ipsum dolor sit amet',
                        'price': 5.0,
                    },
                ],
            },
        }
