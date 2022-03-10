from decouple import config

config = {
    'orders': {
        'host': config('SERVICE_ORDERS_HOST', 'restaurant-backend'),
        'port': config('SERVICE_ORDERS_PORT', '8000'),
    },
}
