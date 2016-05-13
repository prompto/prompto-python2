import unittest
from cgi import escape
from HTMLParser import HTMLParser

class TestHtml(unittest.TestCase):


    def testEncode(self):
        value = escape("a<b")
        self.assertEquals("a&lt;b", value)



    def testDecode(self):
        value = HTMLParser().unescape("a&lt;b")
        self.assertEquals("a<b", value)

