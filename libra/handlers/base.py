# coding: utf-8
from libra.models.user import User
from bson.objectid import ObjectId
from libra import settings


def authenticated(fn):
    def authenticated_fn(self, *args, **kw):
        user_id = self.get_secure_cookie('LIBRAID')

        user = None

        if user_id:
            user = User().find_one({'_id': ObjectId(
                                            user_id.decode(encoding='UTF-8'))})

        if not user:
            self.redirect(settings.SERVER_NAME)

        return fn(self, user=user, *args, **kw)

    return authenticated_fn


def logged(fn):
    def logged_fn(self, *args, **kw):
        user_id = self.get_secure_cookie('LIBRAID')

        user = None

        if user_id:
            user = User().find_one({'_id': ObjectId(
                                            user_id.decode(encoding='UTF-8'))})

        if user:
            self.redirect(settings.SERVER_NAME + '/' + user['fb_id'] + '/')

        return fn(self, *args, **kw)

    return logged_fn
