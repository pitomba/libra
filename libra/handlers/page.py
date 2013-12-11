# coding: utf-8
from libra import settings
from tornado.web import RequestHandler


class PageHandler(RequestHandler):

    def get(self, **kwargs):
        self.render("index.html", SERVER_NAME=settings.SERVER_NAME)
