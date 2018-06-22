from prompto.utils.BaseParserTest import BaseParserTest
from prompto.parser.MCleverParser import *


class BaseMParserTest(BaseParserTest):

    def __init__(self, args=None):
        super(BaseMParserTest, self).__init__(args)

    def parseString(self, code):
        return self.parseMString(code)

    def parseResource(self, resourceName):
        return self.parseMResource(resourceName)


