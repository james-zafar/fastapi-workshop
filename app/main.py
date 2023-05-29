import os
from typing import Final

import uvicorn as uvicorn
from fastapi import FastAPI, APIRouter
from app.store import ModelStore
from app.api.operations import healthz_router, models_router, post_models_router, results_router

BASE_PATH: Final[str] = '/v1'

app = FastAPI()
router = APIRouter()
router.prefix = BASE_PATH
app.include_router(router)
app.include_router(post_models_router)
app.include_router(models_router)
app.include_router(healthz_router)
app.include_router(results_router)

app.state.model_store = ModelStore()


if __name__ == '__main__':
    port = os.getenv('PORT', 8080)
    uvicorn.run(app=app, port=port)
    # Launch the API here
