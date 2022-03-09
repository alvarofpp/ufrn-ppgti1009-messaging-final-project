from app.http.controllers import order_router
from fastapi import APIRouter

api_router = APIRouter()

# Version 1
version_one = '/v1'
api_router.include_router(
    order_router,
    prefix='{}/orders'.format(version_one),
    tags=['orders'],
)
