# coding: utf-8
from tornado.web import Application
from tornado.ioloop import IOLoop
from libra import settings
from libra import urls

import base64
import uuid
import sys

application = Application(urls.urls,
    template_path=settings.TEMPLATE_PATH,
    static_path=settings.STATIC_PATH,
    autoescape=None,
    debug=settings.DEBUG,
    cookie_secret=base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = settings.PORT

    application.listen(port)
    IOLoop.instance().start()
