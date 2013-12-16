# coding: utf-8
from bson import ObjectId
from libra.repository.mongodb.mongodb import Repository
from libra.repository import Property

import datetime


class Page(Repository):
    __collection__ = 'page'

    _id = Property(ObjectId, "page id")
    user = Property(str, "user id")
    url = Property(str, "page url")


class PageData(Repository):
    __collection__ = 'page_data'

    _id = Property(ObjectId, "page data id")
    page_id = Property(int, "page id")
    date = Property(datetime, "created on")
    weight = Property(int, "page weight")
