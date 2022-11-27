# pylint: disable=too-few-public-methods
from ..security import Logs


class LogFactory:
    """logs factory"""

    @staticmethod
    def create() -> Logs:
        """create log instance"""
        logs = Logs()
        return logs
