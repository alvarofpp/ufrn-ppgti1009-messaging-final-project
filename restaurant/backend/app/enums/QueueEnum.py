from enum import Enum

from app.mixins import EnumToListMixin


class QueueEnum(EnumToListMixin, Enum):
    ORDERS_CREATED = 'ORDERS_CREATED'
    ORDERS_STATUS_UPDATED = 'ORDERS_STATUS_UPDATED'
