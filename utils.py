import logging
import logging.config
from config import BASE_DIR
import os

def configure_logger(name, log_path):
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple',
                'stream': 'ext://sys.stdout'
            },
            'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': os.path.join(BASE_DIR, 'simulation_result/log', log_path),
                'formatter': 'verbose',
            }
        },
        'loggers': {
            'betting': {
                'handlers': ['console','file'],
                'level': 'DEBUG',
                'propagate': False,
            },
        }
    })
    return logging.getLogger(name)

def get_class_name(mod_name):
    """Return the class name from a plugin name"""
    output = ""

    # Split on the _
    words = mod_name.split("_")

    # Capitalise the first letter of each word and add to string
    for word in words:
        output += word.title()
    return output
