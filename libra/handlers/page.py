# coding: utf-8
import datetime
from bs4 import BeautifulSoup
from bson.objectid import ObjectId
from tornado.web import RequestHandler
from processor.page_analytic import PageAnalytic
from processor.processor import TagProcessor
from libra.handlers.base import authenticated
from libra.models.page import Page, PageData

import requests


class PageHandler(RequestHandler):

    def get(self, **kwargs):
        self.render("index.html")


class UserPageHandler(RequestHandler):

    @authenticated
    def post(self, user, **kwargs):
        page = Page()
        page._id = ObjectId()
        page.user_id = str(user['_id'])
        page.url = self.get_argument('url')
        page.save()

        self.write({"msg": "Success"})


class SiteHandler(RequestHandler):

    @authenticated
    def get(self, user, **kwargs):
        url = kwargs['url']
        data = []

        for page_data in PageData().find({"page_url": url,
                                          "date": {"$gte": datetime.datetime.now() - datetime.timedelta(minutes=10)}}):
            data.append({'date': page_data['date'].strftime("%Y/%m/%d %H:%M:%S"),
                         'weight': page_data['weight']/1024.0})
        data.sort(key=lambda x: x["date"])
        self.render("graph.html", dataSource=data, site=url)
