# coding: utf-8
from bson.objectid import ObjectId
from libra.repository import Property, PropertyDict
from libra.repository.mongodb.mongodb import Repository

import datetime


class User(Repository):
    __collection__ = 'user'

    _id = Property(ObjectId, "user id")
    create_dt = Property(datetime, "Created on")
    fb_id = Property(str, "Facebook id")
    pages = Property(PropertyDict, "user's pages")
