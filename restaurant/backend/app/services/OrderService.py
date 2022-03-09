from typing import Dict, List

from app.models import Order
from app.services import ModelServiceBase, ModelType
from sqlalchemy.orm import Session


class OrderService(ModelServiceBase):

    def __init__(self):
        super().__init__(Order)

    def count_by_ids(self, db: Session, ids: List[int]) -> int:
        return self.query(db).filter(self.model.id.in_(ids)).count()

    def search(self, db: Session, filters: Dict) -> ModelType:
        query = self.query(db)

        if 'status' in filters.keys():
            query = query.where(self.model.status == filters['status'])

        return query.all()
