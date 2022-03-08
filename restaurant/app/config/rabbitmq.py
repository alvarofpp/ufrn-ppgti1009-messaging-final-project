from decouple import config

config = {
    'host': config('RABBITMQ_HOST', 'localhost'),
    'port': config('RABBITMQ_PORT', '5672'),
    'user': config('RABBITMQ_USER', 'guest'),
    'password': config('RABBITMQ_PASSWORD', 'guest'),
}
