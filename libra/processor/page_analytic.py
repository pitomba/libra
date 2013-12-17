from bs4 import BeautifulSoup
import requests
from processor.processor import TagProcessor


class PageAnalytic(object):
    headers={"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11",
             "Accept-Encoding": "gzip"}
    tagsClass = TagProcessor.__subclasses__()

    def __init__(self, page):
        response = requests.get(page, headers=self.headers)
        self.html_size = int(response.headers["content-length"])
        self.page_object = BeautifulSoup(response.content)
        self._tags = []

    def _get_tag_size(self, tag):
        for subCls in self.tagsClass:
            if subCls.is_resource(tag):
                self._tags.append(subCls(tag, base_url=))
                return True
        else:
            return False

    def get_size_tag(self):
        size = 0
        self.page_object.find_all(self._get_tag_size)
        for tag in self._tags:
            #threading?
            resp = requests.head(tag.get_resource_url(), headers=self.headers)
            if resp.status_code == 200:
                size += int(resp.headers["content-length"])
        self._tags = []
        return size

    def get_page_size(self):
        return self.html_size + self.get_size_tag()
