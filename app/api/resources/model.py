import uuid
from dataclasses import dataclass

from app.api.resources.status import Status


@dataclass
class Model:
    id: uuid.uuid4
    status: Status

    @classmethod
    def new_model(cls) -> 'Model':
        return cls(id=uuid.uuid4(), status=Status.PENDING)

    def json(self) -> dict[str, str]:
        return {
            'id': str(self.id),
            'status': self.status.value
        }

    def __hash__(self) -> int:
        return hash(self.id)
