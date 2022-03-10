from app.http.requests import BaseRequest
from pydantic import Field


class ItemInput(BaseRequest):
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

    class Config:
        schema_extra = {
            'example': {
                'name': 'Item 1',
                'description': 'Lorem ipsum dolor sit amet',
                'price': 5.0,
            },
        }
