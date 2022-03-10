from config import get_config
from fastapi import FastAPI
from routes import api_router

tags_metadata = [
    {
        'name': 'orders',
        'description': 'Operations with orders.',
    },
]

app = FastAPI(
    title=get_config('app.title'),
    openapi_tags=tags_metadata,
)
app.include_router(api_router)
