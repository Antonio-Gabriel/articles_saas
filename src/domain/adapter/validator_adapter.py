# pylint: disable=too-few-public-methods
from typing import Union

from cerberus import Validator


class ValidatorAdapter:
    """validator adapter"""

    @staticmethod
    def validate(payload: dict, validator_schema: dict) -> Union[str, dict]:
        """validate payload"""

        validator = Validator()
        is_valid = validator.validate(payload, validator_schema)

        return is_valid, validator.errors
