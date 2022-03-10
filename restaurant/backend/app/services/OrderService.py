from typing import Dict

from app.enums import OrderStatusEnum
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

    def change_status(self, db: Session, order_id: int) -> ModelType:
        order = self.find_or_fail(db, order_id)
        self.update(db, order_id, {
            'status': self.get_next_status(order),
        })

        return order

    def get_next_status(self, order: Order) -> str:
        if order.status == OrderStatusEnum.ORDER_NEW.value:
            return OrderStatusEnum.ORDER_ACCEPTED.value
        if order.status == OrderStatusEnum.ORDER_ACCEPTED.value:
            return OrderStatusEnum.ORDER_IN_DELIVERY.value

        return OrderStatusEnum.ORDER_DELIVERED.value
