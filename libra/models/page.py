from bson import ObjectId
from libra.repository.mongodb.mongodb import Repository
from libra.repository import Property, PropertyDict

import datetime

class Site(Repository):
    __collection__ = 'site'
    _id = Property(ObjectId, "site id")
    url =  Property(str, "url id")
    date = Property(datetime, "Created on")
    length = Property(int, "length id")
