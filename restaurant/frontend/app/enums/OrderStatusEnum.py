from enum import Enum

from app.mixins import EnumToListMixin


class OrderStatusEnum(EnumToListMixin, Enum):
    ORDER_NEW = 'ORDER_NEW'
    ORDER_ACCEPTED = 'ORDER_ACCEPTED'
    ORDER_IN_DELIVERY = 'ORDER_IN_DELIVERY'
    ORDER_DELIVERED = 'ORDER_DELIVERED'
