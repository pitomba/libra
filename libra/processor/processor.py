# coding utf-8
from bs4 import BeautifulSoup
import requests
import logging
import re
from urllib import parse

class TagProcessor(object):
    http_re = re.compile("^(http(s)?://)")

    def __init__(self, tag, base_url):
        self.base_url = base_url
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
        url = self.tag.attrs["src"]
        if not self.http_re.search(url):
            url = parse.urljoin(self.base_url, url)
        return url

    @classmethod
    def is_resource(cls, tag):
        return tag.name == "img" and tag.has_attr("src")


class ScriptProcessor(TagProcessor):
    def get_resource_url(self):
        url = self.tag.attrs["src"]
        if not self.http_re.search(url):
            url = parse.urljoin(self.base_url, url)
        return url


    @classmethod
    def is_resource(cls, tag):
        return tag.name == "script" and tag.has_attr("src")


class LinkProcessor(TagProcessor):
    def get_resource_url(self):
        url = self.tag.attrs["href"]
        if not self.http_re.search(url):
            url = parse.urljoin(self.base_url, url)
        return url

    @classmethod
    def is_resource(cls, tag):
        return tag.name == "link" and tag.has_attr("rel") and tag.attrs["rel"] == ["stylesheet"]


class EmbedProcessor(TagProcessor):
    def get_resource_url(self):
        url = self.tag.attrs["src"]
        if not self.http_re.search(url):
            url = parse.urljoin(self.base_url, url)
        return url

    @classmethod
    def is_resource(cls, tag):
        return tag.name == "embed" and tag.has_attr("src")


class ObjectProcessor(TagProcessor):
    def get_resource_url(self):
        url =  self.tag.attrs["data"]
        if not self.http_re.search(url):
            url = parse.urljoin(self.base_url, url)
        return url

    @classmethod
    def is_resource(cls, tag):
        return tag.name == "object" and tag.has_attr("data")
