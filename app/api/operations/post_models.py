from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, HttpUrl, Extra

from app.api.errors import new_error_response, BadConfigError
from app.api.resources import Model

post_models_router = APIRouter(prefix='/models')


class CreateModelConfig(BaseModel, extra=Extra.allow):
    data_source: HttpUrl
    data_api_key: str


class PostModelsBody(BaseModel):
    config: CreateModelConfig


@post_models_router.post('')
async def create_model(config: PostModelsBody, request: Request) -> JSONResponse:
    if 'airbus.com' in config.config.data_source:
        raise HTTPException(detail=new_error_response([BadConfigError()]), status_code=400)
    model = Model.new_model()
    request.app.state.model_store[str(model.id)] = model
    headers = {'Location': f'{str(request.url)}/{str(model.id)}'}
    return JSONResponse(content=model.json(), headers=headers, status_code=201)
