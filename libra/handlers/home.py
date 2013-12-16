# coding: utf-8
from tornado.web import RequestHandler
from libra.handlers.base import authenticated
from libra.models.user import User


class HomeHandler(RequestHandler):

    @authenticated
    def get(self, user, **kwargs):
        #TODO - alterar 'user' para ser object
        pages = User.pages(user_id=str(user['_id']))

        self.render("home.html", pages=pages)
