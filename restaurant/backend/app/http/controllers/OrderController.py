from typing import Optional

from app.http.requests.orders import StoreRequest
from app.http.resources import OrderCollection, OrderResource
from app.services import OrderService
from app.services.clean import clean_dict
from database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

order_router = APIRouter()


@order_router.get('', response_model=OrderCollection)
async def index(status: Optional[str] = None, db: Session = Depends(get_db)):
    service = OrderService()
    query_parameters = {
        'status': status,
    }
    filters = clean_dict(query_parameters)

    return OrderCollection.to_dict(service.search(db, filters))


@order_router.get('/{order_id}', response_model=OrderResource)
async def show(order_id: int, db: Session = Depends(get_db)):
    service = OrderService()
    order = service.find_or_fail(db, order_id)

    return OrderResource.to_dict(order)


@order_router.post('', response_model=OrderResource)
async def create(request: StoreRequest, db: Session = Depends(get_db)):
    service = OrderService()
    order = service.create_from_request(db, request)

    return OrderResource.to_dict(order)
