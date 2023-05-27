from abc import ABC
from collections.abc import Sequence


def new_error_response(errors: Sequence['Error']) -> dict[str, list[dict[str, str]]]:
    return {
        'errors': [error.json() for error in errors]
    }


class Error(ABC):
    code: str
    message: str
    status_code: int

    def json(self) -> dict[str, str]:
        return {
            'code': self.code,
            'message': self.message
        }


