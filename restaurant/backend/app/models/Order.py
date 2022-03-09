from database.db import Base
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    costumer_id = Column(Integer, unique=False)
    status = Column(String, unique=False)
    total_price = Column(Float, unique=False)

    items = relationship(
        'Item',
        back_populates='order',
    )
