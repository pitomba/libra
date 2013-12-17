# coding: utf-8
from bson.objectid import ObjectId
from datetime import datetime
from libra.models.user import User
from tornado.web import RequestHandler


class SessionHandler(RequestHandler):
    def get(self, **kwargs):
        fb_id = kwargs['fb_id']

        user = User().find_one({'fb_id': fb_id})

        if not user:
            user = User()
            user._id = ObjectId()
            user.fb_id = fb_id
            user.create_dt = datetime.now()
            user.save()

        self.set_secure_cookie(name="LIBRAID",
                               value=str(user['_id']),
                               path="/",
                               expires_days=None)

        self.write({"msg": "Success"})
