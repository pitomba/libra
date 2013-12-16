# coding: utf-8
from pymongo import MongoClient
from libra import settings

import logging


__database__ = None


def get_database():
    global __database__

    if not __database__:
        logging.info("MONGODB connecting database...")

        host = settings.MONGODB_DATABASE_URL
        port = settings.MONGODB_DATABASE_PORT
        dbuser = settings.MONGODB_DATABASE_USER
        dbpass = settings.MONGODB_DATABASE_PWD

        __database__ = MongoClient(host=host, port=port).libra

    return __database__
