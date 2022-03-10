from database.db import Base
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, unique=True)
    description = Column(String, unique=False)
    price = Column(Float, unique=False)
    order_id = Column(Integer, ForeignKey('orders.id'))

    order = relationship(
        'Order',
        back_populates='items',
    )
