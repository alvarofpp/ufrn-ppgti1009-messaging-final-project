from typing import List


class EnumToListMixin:

    @classmethod
    def list(cls) -> List:
        return [element.value for element in cls]
