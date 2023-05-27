from fastapi import APIRouter

healthz_router = APIRouter(prefix='/healthz')


@healthz_router.get('', status_code=204)
def get_healthz() -> None:
    return None
