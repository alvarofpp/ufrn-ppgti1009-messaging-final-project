from typing import List, Union

from pydantic import BaseModel


class BaseRequest(BaseModel):

    def get(self, keys_or_key: Union[List[str], str], default=None):
        """Gets an attribute from the Request's body.

        :param keys_or_key: a list of keys or a unique key.
        :param default: default value if the key is not found in the request.
        :return: a found value or defined default value.
        """
        if isinstance(keys_or_key, list):
            return {key: self.get(key, default) for key in keys_or_key}

        if hasattr(self, keys_or_key):
            return getattr(self, keys_or_key)

        return default
