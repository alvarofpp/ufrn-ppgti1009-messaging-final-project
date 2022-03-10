from decouple import config


config = {
    'host': config('DB_HOST', 'localhost'),
    'port': config('DB_PORT', '5432'),
    'database': config('DB_DATABASE', 'pokemon-dev'),
    'username': config('DB_USERNAME', 'postgres'),
    'password': config('DB_PASSWORD', 'postgres'),
}
