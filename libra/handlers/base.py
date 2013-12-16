# coding: utf-8
from libra.models.user import User


def authenticated(fn):
    def authenticated_fn(self, *args, **kw):

        request_handler = kw.get('request_handler')

        user_id = request_handler.get_secure_cookie('USERID')

        user = None

        if user_id:
            user = User().get(int(user_id))

        return fn(self, user=user, *args, **kw)

    return authenticated_fn
