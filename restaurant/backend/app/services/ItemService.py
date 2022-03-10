from app.models import Item
from app.services import ModelServiceBase


class ItemService(ModelServiceBase):

    def __init__(self):
        super().__init__(Item)
