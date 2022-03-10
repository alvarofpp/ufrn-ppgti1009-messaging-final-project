from decouple import config


config = {
    'title': config('APP_TITLE', 'app'),
}
