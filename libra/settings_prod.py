from settings_base import *

PORT = 9083

SERVER_NAME = 'http://pitomba.org'

DEBUG = False

LOGGING['root']['handlers'] = ['file']
LOGGING['handlers']['file'] = {
    'level': 'INFO',
    'class': 'logging.FileHandler',
    'formatter': 'detailed',
    'filename': '/opt/logs/libra/app.log',
    'encoding': 'utf-8',
}
