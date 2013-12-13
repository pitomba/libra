# coding: utf-8
from tornado.web import RequestHandler


class PageHandler(RequestHandler):

    def get(self, **kwargs):
        self.render("index.html")

    def post(self, **kwargs):
        url = self.get_argument("url")

        self.render("index.html")
