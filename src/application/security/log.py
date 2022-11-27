# pylint: disable=too-few-public-methods
import os
from typing import Optional, Union
from logging import basicConfig, DEBUG
from logging import warning, error, info
from logging import FileHandler, StreamHandler


class Logs:
    """logs security"""

    ROOT = os.path.dirname(os.path.abspath(__file__))

    def __init__(self) -> None:

        basicConfig(
            level=DEBUG,
            encoding="utf-8",
            format='%(levelname)s:%(asctime)s:%(message)s',
            handlers=[FileHandler(
                f"{self.ROOT}/logs/logs.log", "a"), StreamHandler()]
        )

    def set_log(self, message: Optional[Union[str, dict]], _type: str) -> None:
        """set log on file"""
        match _type:
            case "info":
                info(message)
            case "error":
                error(message)
            case "warning":
                warning(message)
