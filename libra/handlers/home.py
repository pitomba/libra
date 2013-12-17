# coding: utf-8
from libra import settings
from libra.handlers.base import authenticated
from libra.models.user import User
from tornado.web import RequestHandler


class HomeHandler(RequestHandler):

    @authenticated
    def get(self, user, **kwargs):
        #TODO - alterar 'user' para ser object
        pages = User.pages(user_id=str(user['_id']))

        self.render("home.html",
                    SERVER_NAME=settings.SERVER_NAME,
                    pages=pages,
                    user=user)
