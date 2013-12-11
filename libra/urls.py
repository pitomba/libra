# coding: utf-8
from tornado.web import URLSpec

from libra.handlers.page import PageHandler

urls = (
    URLSpec(r'/(?P<page>index.html)?', PageHandler, name='home_index'),
    URLSpec(r'/(?P<context>.[\w-]+)/?', PageHandler, name='home')
)
