# coding: utf-8
from tornado.web import RequestHandler
from libra.handlers.base import authenticated


class HomeHandler(RequestHandler):

    @authenticated
    def get(self, user, **kwargs):
        self.render("home.html", user=user)
