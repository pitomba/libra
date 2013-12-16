# coding: utf-8
from html.parser import HTMLParser
from tornado.web import RequestHandler

from urllib import request

inTD = False


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global inTD
        if tag.upper() == "META":
            inTD = True

    def handle_endtag(self, tag):
        global inTD
        if tag.upper() == "META":
            inTD = False

    def handle_data(self, data):
        global inTD
        if inTD:
            print(data)


class PageHandler(RequestHandler):

    def get(self, **kwargs):
        self.render("index.html")

    def post(self, **kwargs):
        parser = MyHTMLParser()
        page = request.urlopen(self.get_argument("url")).read().decode("utf-8")
        parser.feed(page)

        import pdb;pdb.set_trace()
        self.render("index.html")
