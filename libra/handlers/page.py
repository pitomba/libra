# coding: utf-8
from bs4 import BeautifulSoup
from bson.objectid import ObjectId
from tornado.web import RequestHandler
from processor.page_analytic import PageAnalytic
from processor.processor import TagProcessor
from libra.handlers.base import authenticated
from libra.models.page import Page

import requests


class PageHandler(RequestHandler):

    def get(self, **kwargs):
        self.render("index.html")

    def post(self, **kwargs):
        page = PageAnalytic(self.get_argument("url"))
        self.render("index.html")


class UserPageHandler(RequestHandler):

    @authenticated
    def post(self, user, **kwargs):
        page = Page()
        page._id = ObjectId()
        page.user_id = user['_id']
        page.save()

        self.write({"msg": "Success"})
