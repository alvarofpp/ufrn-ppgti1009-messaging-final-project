from .app import config as config_app
from .database import config as config_database
from .rabbitmq import config as config_rabbitmq

config = {
    'app': config_app,
    'database': config_database,
    'rabbitmq': config_rabbitmq,
}


def get_config(full_path: str, default=None):
    current_config = config

    for path in full_path.split('.'):
        if path in current_config.keys():
            current_config = current_config[path]
        else:
            return default

    return current_config
