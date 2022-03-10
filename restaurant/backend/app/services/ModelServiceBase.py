from typing import Any, Dict, Generic, List, Optional, Type, TypeVar

from database import Base
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

ModelType = TypeVar('ModelType', bound=Base)


class ModelServiceBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def query(self, db: Session):
        return db.query(self.model)

    def exists(self, db: Session, attributes: Dict) -> bool:
        exists = self.query(db).filter_by(**attributes).exists()
        return db.query(exists).scalar()

    def find(self, db: Session, id: Any) -> Optional[ModelType]:
        return self.query(db).get(id)

    def find_or_fail(self, db: Session, id: Any, detail: str = 'Not found.') -> Optional[ModelType]:
        model = self.find(db, id)

        if model is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=detail,
            )

        return self.query(db).get(id)

    def get(self, db: Session, attributes: Dict) -> Optional[ModelType]:
        return self.query(db).filter_by(**attributes)

    def get_first(self, db: Session, attributes: Dict) -> Optional[ModelType]:
        return self.get(db, attributes).first()

    def get_all(self, db: Session, attributes: Dict) -> Optional[ModelType]:
        return self.get(db, attributes).all()

    def create(self, db: Session, attributes: Dict) -> ModelType:
        database_object = self.model(**attributes)
        db.add(database_object)
        db.commit()
        db.refresh(database_object)
        return database_object

    def insert(self, db: Session, entitites: List) -> bool:
        try:
            db.add_all(entitites)
            db.commit()
        except Exception:
            return False

        return True

    def update(self, db: Session, id: Any, attributes: Dict) -> bool:
        try:
            self.query(db).filter(self.model.id == id).update(attributes)
            db.commit()
        except Exception:
            return False

        return True

    def delete(self, db: Session, attributes: Dict) -> bool:
        try:
            self.query(db).filter_by(**attributes).delete()
            db.commit()
        except Exception:
            return False

        return True
