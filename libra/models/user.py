# coding: utf-8
from bson.objectid import ObjectId
from libra.repository import Property
from libra.repository.mongodb.mongodb import Repository

import datetime
from libra.models.page import Page


class User(Repository):
    __collection__ = 'user'

    _id = Property(ObjectId, "user id")
    create_dt = Property(datetime, "Created on")
    fb_id = Property(str, "Facebook id")

    @classmethod
    def pages(cls, user_id):
        return Page().find({"user_id": user_id})
