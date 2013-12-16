# coding: utf-8
from tornado.web import URLSpec

from libra.handlers.page import PageHandler
from libra.handlers.session import SessionHandler

urls = (
    URLSpec(r'/(?P<page>index.html)?', PageHandler, name='home_index'),
    URLSpec(r'/(?P<context>.[\w-]+)/?', PageHandler, name='home'),

    URLSpec(r'/api/authenticate/(?P<fb_id>.[0-9]+)/$', SessionHandler, name='authenticate')
)
