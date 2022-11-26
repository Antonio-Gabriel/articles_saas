# pylint: disable=too-few-public-methods
from uuid import uuid4
from typing import Optional


class UniqueId:
    """value object to generate unique id"""
    @staticmethod
    def new(_id: Optional[str]) -> Optional[str]:
        """generate id method"""
        return _id if _id is None else str(uuid4())
