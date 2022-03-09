from typing import Dict

from app.http.requests.orders import StoreRequest
from app.models import Order
from app.services import ItemService, ModelServiceBase, ModelType
from sqlalchemy.orm import Session


class OrderService(ModelServiceBase):

    def __init__(self):
        super().__init__(Order)

    def create_from_request(self, db: Session, request: StoreRequest) -> ModelType:
        order = self.create(db, {
            'customer_id': request.get('customer_id'),
            'status': request.get('status'),
            'total_price': request.get('total_price'),
        })

        item_service = ItemService()
        for item in request.get('items'):
            item_service.create(db, {
                'name': item.name,
                'description': item.description,
                'price': item.price,
                'order_id': order.id,
            })

        return order

    def search(self, db: Session, filters: Dict) -> ModelType:
        query = self.query(db)

        if 'status' in filters.keys():
            query = query.where(self.model.status == filters['status'])

        return query.all()
