# coding: utf-8
from bs4 import BeautifulSoup
from bson.objectid import ObjectId
from tornado.web import RequestHandler
from processor.page_analytic import PageAnalytic
from processor.processor import TagProcessor
from libra import settings
from libra.handlers.base import authenticated
from libra.handlers.base import logged
from libra.models.page import Page, PageData

import requests


class PageHandler(RequestHandler):

    @logged
    def get(self, **kwargs):
        self.render("index.html",
                    SERVER_NAME=settings.SERVER_NAME)


class UserPageHandler(RequestHandler):

    @authenticated
    def post(self, user, **kwargs):
        page = Page()
        page._id = ObjectId()
        page.user_id = str(user['_id'])
        page.url = self.get_argument('url')
        page.save()

        self.write({"msg": "Created!",
                    "name": page.url,
                    "url": settings.SERVER_NAME + '/' + str(user['fb_id']) + '/' + page.url + '/'})


class SiteHandler(RequestHandler):

    @authenticated
    def get(self, user, **kwargs):
        url = kwargs['url']
        data = []

        for page_data in PageData().find({"page_url": url}):
            data.append({'date': page_data['date'].strftime("%Y/%m/%d %H:%M"),
                         'weight': "{0:0.2f}".format(page_data['weight'] / 1024.0)})

        self.render("graph.html",
                    dataSource=data, site=url,
                    SERVER_NAME=settings.SERVER_NAME)
