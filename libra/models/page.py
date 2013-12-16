# coding: utf-8
from bson import ObjectId
from libra.repository.mongodb.mongodb import Repository
from libra.repository import Property

import datetime


class Page(Repository):
    __collection__ = 'site'
    _id = Property(ObjectId, "site id")
    date = Property(datetime, "Created on")
    weight = Property(int, "page weight")
    url = Property(str, "page url")
