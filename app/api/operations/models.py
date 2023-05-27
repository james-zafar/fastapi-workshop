import random
import uuid

from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse

from app.api.errors import ModelNotFoundError, new_error_response, InternalServerError

models_router = APIRouter(prefix='/models/{model_id}')


@models_router.get('', status_code=200)
def get_model(model_id: uuid.UUID, request: Request) -> JSONResponse:
    if not (model := request.app.state.model_store.get(str(model_id))):
        return JSONResponse(content=new_error_response([ModelNotFoundError()]), status_code=404)
    if random.randint(0, 101) % 25 == 0:
        raise HTTPException(detail=new_error_response([InternalServerError()]), status_code=500)
    return JSONResponse(content=model[0].json())


@models_router.delete('', status_code=204)
def delete_model(model_id: uuid.UUID, request: Request) -> None:
    if not (model := request.app.state.model_store.get(str(model_id))):
        raise HTTPException(detail=new_error_response([ModelNotFoundError()]), status_code=404)
    if random.randint(0, 101) % 25 == 0:
        raise HTTPException(detail=new_error_response([InternalServerError()]), status_code=500)
    del request.app.state.model_store[str(model[0].id)]

    return None
