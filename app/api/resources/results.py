import uuid
from dataclasses import dataclass
from typing import Any


@dataclass
class ResultItem:
    cluster: float
    occurrences: int
    members: list[str]

    def json(self) -> dict[str, Any]:
        return {
            'cluster_label': self.cluster,
            'occurrences': self.occurrences,
            'members': self.members
        }


@dataclass
class Results:
    experiment_id: uuid.UUID
    model_id: uuid.UUID
    results: list[ResultItem]

    def json(self) -> dict[str, Any]:
        return {
            'experiment_id': str(self.experiment_id),
            'model_id': str(self.model_id),
            'results': [result.json() for result in self.results]
        }
