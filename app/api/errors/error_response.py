from collections.abc import Sequence
from typing import TypeVar, Any

T = TypeVar('T', bound='BaseError')


def new_error_response(errors: Sequence['Error']) -> dict[str, list[dict[str, str]]]:
    return {
        'errors': [error.json() for error in errors]
    }


class Error:
    code: str
    message: str
    status_code: int

    def json(self) -> dict[str, str]:
        return {
            'code': self.code,
            'message': self.message
        }

    def __new__(cls: type[T], *args: Any, **kwargs: Any) -> T:
        if cls is Error:
            raise TypeError(f'The class \'{cls.__name__}\' can not be instantiated')
        return object.__new__(cls, *args, **kwargs)

