from handlers.page import PageAnalytic
from page import Site

site = Site()
site.url = "http://globoesporte.globo.com"
pg = PageAnalytic(site.url)
site.length = pg.get_page_size()

print (site.length)
