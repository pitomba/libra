# coding: utf-8
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import requests
from tornado.web import RequestHandler
from handlers.processor import TagProcessor


class PageAnalytic(object):

    tagsClass = TagProcessor.__subclasses__()

    def __init__(self, page):
        response = requests.get(page)
        self.html_size = int(response.headers["content-length"])
        self.page_object = BeautifulSoup(response.content)
        self._tags = []

    def _get_tag_size(self, tag):
        for subCls in self.tagsClass:
            if subCls.is_resource(tag):
                self._tags.append(subCls(tag))
                return True
        else:
            return False

    def get_size_tag(self):
        size = 0
        self.page_object.find_all(self._get_tag_size)
        for tag in self._tags:
            #threading?
            resp = requests.get(tag.get_resource_url())
            if resp.status_code == 200:
                size += int(resp.headers["content-length"])
        self._tags = []
        return size

    def get_page_size(self):
        return self.html_size + self.get_size_tag()

class PageHandler(RequestHandler):

    def get(self, **kwargs):
        self.render("index.html")

    def post(self, **kwargs):
        page = PageAnalytic(self.get_argument("url"))
        self.render("index.html")
