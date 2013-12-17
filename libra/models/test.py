# coding: utf-8
from handlers.page import PageAnalytic
from page import Page

page = Page()
page.url = "http://globoesporte.globo.com"
pg = PageAnalytic(page.url)
page.length = pg.get_page_size()

print (page.length)
