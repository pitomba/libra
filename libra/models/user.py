# coding: utf-8
from libra.repository import Property
from libra.repository.mongodb.mongodb import Repository
from bson.objectid import ObjectId


class User(Repository):
    __collection__ = 'user'
    _id = Property(ObjectId, "user id")
    fb_id = Property(str, "Facebook id")
