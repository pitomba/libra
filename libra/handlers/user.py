# coding: utf-8
from tornado.web import RequestHandler
from libra.handlers.base import authenticated


class UserHandler(RequestHandler):

    @authenticated
    def post(self, user, **kwargs):
        self.write({"msg": "Success"})
