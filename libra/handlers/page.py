# coding: utf-8
from bs4 import BeautifulSoup
import requests
from tornado.web import RequestHandler
from processor.page_analytic import PageAnalytic
from processor.processor import TagProcessor
from libra.handlers.base import authenticated


class PageHandler(RequestHandler):

    def get(self, **kwargs):
        self.render("index.html")

    def post(self, **kwargs):
        page = PageAnalytic(self.get_argument("url"))
        self.render("index.html")


class UserPageHandler(RequestHandler):

    @authenticated
    def post(self, user, **kwargs):
        id_dict = {"_id": user['_id']}

        update_dict = {"$push": {"pages": {"url": self.get_argument('url')}}}

        user.update(id_dict=id_dict, update_dict=update_dict)

        self.write({"msg": "Success"})
