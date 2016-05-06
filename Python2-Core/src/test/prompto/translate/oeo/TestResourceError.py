from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestResourceError(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testBadRead(self):
        self.compareResourceOEO("resourceError/badRead.poc")

    def testBadResource(self):
        self.compareResourceOEO("resourceError/badResource.poc")

    def testBadWrite(self):
        self.compareResourceOEO("resourceError/badWrite.poc")


