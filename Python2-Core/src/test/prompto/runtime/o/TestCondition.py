from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestCondition(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testComplexIf(self):
        self.checkOutput("condition/complexIf.poc")

    def testEmbeddedIf(self):
        self.checkOutput("condition/embeddedIf.poc")

    def testLocalScope(self):
        self.checkOutput("condition/localScope.poc")

    def testReturnTextIf(self):
        self.checkOutput("condition/returnTextIf.poc")

    def testReturnVoidIf(self):
        self.checkOutput("condition/returnVoidIf.poc")

    def testSimpleIf(self):
        self.checkOutput("condition/simpleIf.poc")

    def testSwitch(self):
        self.checkOutput("condition/switch.poc")

    def testTernary(self):
        self.checkOutput("condition/ternary.poc")

    def testTernaryType(self):
        self.checkOutput("condition/ternaryType.poc")


