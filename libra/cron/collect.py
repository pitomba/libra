# coding: utf-8
#!/usr/bin/python
from datetime import datetime
import logging


def run():
    start = datetime.now()
    logging.debug("===================================================")
    logging.debug("Verifying data for site {0} at {1}".format("site", start))

    logging.debug("Finished!: {0}".format(datetime.now() - start))
    logging.debug("===================================================")
