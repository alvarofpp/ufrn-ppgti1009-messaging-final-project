from typing import Dict

from app.models import Order
from app.services import ModelServiceBase, ModelType
from sqlalchemy.orm import Session


class OrderService(ModelServiceBase):

    def __init__(self):
        super().__init__(Order)

    def search(self, db: Session, filters: Dict) -> ModelType:
        query = self.query(db)

        if 'status' in filters.keys():
            query = query.where(self.model.status == filters['status'])

        return query.all()
