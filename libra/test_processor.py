# coding utf-8
import unittest
from handlers.processor import *
from bs4 import BeautifulSoup


class TestProcessor(unittest.TestCase):

   def setUp(self):
      html = """
               <html>
                  <head>
                     <link href="link_link" rel="stylesheet" />
                     <script></script>
                     <script src="link_script"></script>
                  </head>
                  <body>
                     <img src="link_img" />
                     <embed src="link_embed">
                     <object data="link_object"></object>
                  </body>
               </html>
               """

      self.soup = BeautifulSoup(html)

   def test_img_is_resource(self):
      tags_imgs = self.soup.find_all('img')
      for img in tags_imgs:
         self.assertTrue(ImgProcessor.is_resource(img))

   def test_img_get_resource_url(self):
      tags_imgs = self.soup.find_all('img')
      for img in tags_imgs:
         imagem = ImgProcessor(img)
         if ImgProcessor.is_resource(img):
            self.assertEqual(imagem.get_resource_url(), 'link_img')

   def test_script_is_resource(self):
      tags_script = self.soup.find_all('script')
      self.assertFalse(ScriptProcessor.is_resource(tags_script[0]))
      self.assertTrue(ScriptProcessor.is_resource(tags_script[1]))


   def test_script_get_resource_url(self):
      tags_script = self.soup.find_all('script')
      for script in tags_script:
         scr = ScriptProcessor(script)
         if ScriptProcessor.is_resource(script):
            self.assertEqual(scr.get_resource_url(), 'link_script')

   def test_link_is_resource(self):
      tags_links = self.soup.find_all('link')
      for link in tags_links:
         self.assertTrue(LinkProcessor.is_resource(link))

   def test_link_get_resource_url(self):
      tags_link = self.soup.find_all('link')
      for link in tags_link:
         lnk = LinkProcessor(link)
         if LinkProcessor.is_resource(link):
            self.assertEqual(lnk.get_resource_url(), 'link_link')

   def test_embed_is_resource(self):
      tags_embeds = self.soup.find_all('embed')
      for embed in tags_embeds:
         self.assertTrue(EmbedProcessor.is_resource(embed))

   def test_embed_get_resource_url(self):
      tags_embeds = self.soup.find_all('embed')
      for embed in tags_embeds:
         ebd = EmbedProcessor(embed)
         if EmbedProcessor.is_resource(embed):
            self.assertEqual(ebd.get_resource_url(), 'link_embed')

   def test_object_is_resource(self):
      tags_objects = self.soup.find_all('object')
      for objecte in tags_objects:
         self.assertTrue(ObjectProcessor.is_resource(objecte))

   def test_object_get_resource_url(self):
      tags_objects = self.soup.find_all('object')
      for objecte in tags_objects:
         obj = ObjectProcessor(objecte)
         if ObjectProcessor.is_resource(objecte):
            self.assertEqual(obj.get_resource_url(), 'link_object')

unittest.main()