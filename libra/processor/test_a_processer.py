from handlers.page import PageAnalytic

__author__ = 'romulo.jales'

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        pg = PageAnalytic("http://globoesporte.globo.com")
        pg.get_size_tag()
        self.assertEqual(True, False)

    def test_get_page_size(self):
        pg = PageAnalytic("http://.globgloboesporteo.com")
        pg.get_page_size()

if __name__ == '__main__':
    unittest.main()
