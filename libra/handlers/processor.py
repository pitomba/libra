# coding utf-8
from bs4 import BeautifulSoup

class TagProcessor(object):

    def __init__(self, tag):
        self.tag = tag

    def get_resource_url(self):
        #should return the resource url for download
        raise NotImplementedError

    @classmethod
    def is_resource(cls, tag):
        #should return a boolean
        raise NotImplementedError


class ImgProcessor(TagProcessor):
    def get_resource_url(self,):
        return self.tag.attrs["src"]

    @classmethod
    def is_resource(cls, tag):
        return tag.name == "object"

# class TagProcessor(object):
#     def __init__(self, html_doc):
#         self.soup = BeautifulSoup(html_doc)
#
#     def get_resource_url(self, tag):
#         #should return the resource url for download
#         url_tags = {
#             'link': 'href',
#             'script': 'src',
#             'img': 'src',
#             'embed': 'src',
#             'object': 'data'
#         }
#
#         for key, value in url_tags.items():
#             if key == tag:
#                 return tag.get(value)
#
#         return None
#
#     def is_resource(self, tag):
#         #should return a boolean
#         elements = self.soup.find_all(tag)
#         if len(elements):
#             return True
#         else:
#             return False