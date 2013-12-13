from settings_base import *

PORT = 9083
SERVER_NAME = 'http://pitomba.org'

LOG_FILENAME = 'libra-app.log'
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    filename=LOG_FILENAME,
                    level=logging.WARNING)
