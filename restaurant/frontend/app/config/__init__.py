from .app import config as config_app
from .rabbitmq import config as config_rabbitmq
from .services import config as config_services

config = {
    'app': config_app,
    'rabbitmq': config_rabbitmq,
    'services': config_services,
}


def get_config(full_path: str, default=None):
    current_config = config

    for path in full_path.split('.'):
        if path in current_config.keys():
            current_config = current_config[path]
        else:
            return default

    return current_config
