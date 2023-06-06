import uuid

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from app.api.errors import ModelNotFoundError, new_error_response, ModelNotReadyError
from app.api.resources import Status

results_router = APIRouter(prefix='/models/{model_id}/results')


@results_router.get('', status_code=200)
def get_results(model_id: uuid.UUID, request: Request) -> JSONResponse:
    if not (model := request.app.state.model_store.get(str(model_id))):
        return JSONResponse(content=new_error_response([ModelNotFoundError()]), status_code=404)
    if not model[0].status == Status.COMPLETED:
        return JSONResponse(content=new_error_response([ModelNotReadyError()]), status_code=400)
    results_id, results = request.app.state.model_store.get_results(str(model_id))
    total_clusters = len(results)
    data_point_count = sum(cluster.occurrences for cluster in results)
    return JSONResponse(content={
        'id': results_id,
        'results': {
            'cluster_count': total_clusters,
            'total_data_points': data_point_count,
            'clusters': [cluster.json() for cluster in results]
        }
    })
