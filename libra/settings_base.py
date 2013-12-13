import os
import logging
from functools import partial


get_path_to = partial(os.path.join, os.path.dirname(__file__))

DEBUG = True

TEMPLATE_PATH = get_path_to("templates")
STATIC_PATH = get_path_to("static")

LOG_FILENAME = 'libra-app.log'
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    filename=LOG_FILENAME,
                    level=logging.DEBUG)
