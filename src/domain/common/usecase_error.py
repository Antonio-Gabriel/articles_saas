# pylint: disable=super-init-not-called,too-few-public-methods
from abc import ABC
from typing import Type
from dataclasses import dataclass


@dataclass
class IUseCaseErrorProps:
    """usecase error props"""
    message: str


class UseCaseError(ABC, IUseCaseErrorProps):
    """usecase error base"""

    def __init__(self, error: Type[IUseCaseErrorProps]) -> None:
        self.message = error.message
