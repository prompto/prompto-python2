from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestSingleton(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAttribute(self):
        self.checkOutput("singleton/attribute.pec")

    def testDictionary(self):
        self.checkOutput("singleton/dictionary.pec")

    def testInitialize(self):
        self.checkOutput("singleton/initialize.pec")

    def testInternal(self):
        self.checkOutput("singleton/internal.pec")

    def testMember(self):
        self.checkOutput("singleton/member.pec")


