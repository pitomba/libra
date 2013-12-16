# coding utf-8
from bs4 import BeautifulSoup
import requests


class TagProcessor(object):

    def __init__(self, tag):
        self.tag = tag

    def get_resource_url(self):
        #should return the resource url for download
        raise NotImplementedError

    @classmethod
    def is_resource(cls, tag):
        #should return a boolean
        raise NotImplementedError


class ImgProcessor(TagProcessor):
    def get_resource_url(self):
        return self.tag.attrs["src"]

    @classmethod
    def is_resource(cls, tag):
        return tag.name == "img"


class ScriptProcessor(TagProcessor):
    def get_resource_url(self):
        return self.tag.attrs["src"]

    @classmethod
    def is_resource(cls, tag):
        return tag.name == "script" and  tag.has_attr("src")


class LinkProcessor(TagProcessor):
    def get_resource_url(self):
        return self.tag.attrs["href"]

    @classmethod
    def is_resource(cls, tag):
        return tag.name == "link" and tag.has_attr("rel") and tag.attrs["rel"] == ["stylesheet"]


class EmbedProcessor(TagProcessor):
    def get_resource_url(self):
        return self.tag.attrs["src"]

    @classmethod
    def is_resource(cls, tag):
        return tag.name == "embed"


class ObjectProcessor(TagProcessor):
    def get_resource_url(self):
        return self.tag.attrs["data"]

    @classmethod
    def is_resource(cls, tag):
        return tag.name == "object"
