# coding: utf-8
#!/usr/bin/python
from datetime import datetime
import logging
from libra.models.page import Page, PageData
from bson.objectid import ObjectId
from libra.processor.page_analytic import PageAnalytic
import time

def run():
    while True:
        start = datetime.now()
        logging.debug("===================================================")
        logging.debug("Starting at {0}".format(start))

        for page in Page().find():
            logging.debug("Verifying data for site {0}".format(page['url']))

            try:
                page_analytic = PageAnalytic(url=page['url'])

                page_data = PageData()
                page_data._id = ObjectId()
                page_data.page_url = str(page['url'])
                page_data.date = datetime.now()
                page_data.weight = page_analytic.get_page_size()
                page_data.save()
            except:
                logging.exception("Error getting weight for {0}".format(page['url']))

        logging.debug("Finished!: {0}".format(datetime.now() - start))
        logging.debug("===================================================")
        time.sleep(30)
