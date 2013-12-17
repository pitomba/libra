# coding: utf-8
from tornado.web import URLSpec

from libra.handlers.page import PageHandler
from libra.handlers.page import UserPageHandler
from libra.handlers.page import SiteHandler
from libra.handlers.session import SessionHandler
from libra.handlers.home import HomeHandler

urls = (
    URLSpec(r'/api/authenticate/(?P<fb_id>.[0-9]+)/$', SessionHandler, name='authenticate'),

    URLSpec(r'/api/page/$', UserPageHandler, name='page'),

    URLSpec(r'/(?P<fb_id>.[0-9]+)/$', HomeHandler, name='home'),
    URLSpec(r'/(?P<fb_id>.[0-9]+)/(?P<url>.*)$', SiteHandler, name='site'),

    URLSpec(r'/(?P<page>index.html)?', PageHandler, name='index_index'),

    URLSpec(r'/(?P<context>.[a-zA-Z]+)/?', PageHandler, name='index')
)
