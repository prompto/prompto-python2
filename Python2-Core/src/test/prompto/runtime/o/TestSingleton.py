from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestSingleton(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAttribute(self):
        self.checkOutput("singleton/attribute.poc")

    def testDictionary(self):
        self.checkOutput("singleton/dictionary.poc")

    def testInitialize(self):
        self.checkOutput("singleton/initialize.poc")

    def testInternal(self):
        self.checkOutput("singleton/internal.poc")

    def testMember(self):
        self.checkOutput("singleton/member.poc")


