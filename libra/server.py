# coding: utf-8
import sys

from tornado.web import Application
from tornado.ioloop import IOLoop
from libra import settings
from libra import urls

application = Application(urls.urls,
    template_path=settings.TEMPLATE_PATH,
    static_path=settings.STATIC_PATH,
    autoescape=None,
    debug=settings.DEBUG
)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = settings.PORT

    application.listen(port)
    IOLoop.instance().start()
