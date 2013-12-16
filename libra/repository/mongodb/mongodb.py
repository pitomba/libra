# coding: utf-8
from libra.repository.mongodb import get_database
from libra.repository.mongodb.orm import __collections__
from datetime import datetime


class Repository(object):
    def as_dict(self):
        items = {}
        for attrname in dir(self):
            if attrname.startswith("_") and not attrname == '_id':
                continue

            attr = getattr(self, attrname)
            if isinstance(attr, (str, int, float, datetime)):
                items[attrname] = attr
            if hasattr(attr, 'serializable'):
                items[attr.serializable] = attr()

            if isinstance(attr, list):
                items[attrname] = [x.as_dict() for x in attr]

            if isinstance(attr, dict):
                items[attrname] = attr

            if attrname == '_id':
                items[attrname] = attr

        return items

    @classmethod
    def create(cls, dictionary):
        instance = cls()
        for (key, value) in dictionary.items():
            setattr(instance, str(key), value)

        return instance

    def get_collection(self):
        db = get_database()
        return getattr(db, self.__collection__)

    def update(self, id_dict, update_dict):
        self.get_collection().update(id_dict, update_dict, safe=True)

    def save(self):
        self.get_collection().insert(self.as_dict(), safe=True)

    def remove(self, filter):
        self.get_collection().remove(filter, safe=True)

    def remove_all(self):
        return self.get_collection().remove()

    def find_one(self, dict={}):
        if dict != {}:
            return self.get_collection().find_one(dict)

        return self.get_collection().find_one()

    def find(self):
        return self.get_collection().find()
