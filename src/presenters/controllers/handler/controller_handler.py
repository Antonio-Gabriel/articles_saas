from abc import ABC
from typing import Type, Optional
from dataclasses import dataclass


@dataclass
class Request:
    """request params"""
    body: dict = None
    params: list = None


class ControllerBase(ABC):
    """handler"""

    async def handle(self, request: Optional[Type[Request]] = None):
        """controller handling"""

        raise NotImplementedError("Method not implemented")
