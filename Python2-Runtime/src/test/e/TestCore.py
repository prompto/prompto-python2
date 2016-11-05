from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestCore(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
        self.coreContext = None
        self.loadDependency("core")
    
    def tearDown(self):
        Out.restore()

    def testAny(self):
        self.runTests("core/any.pec")
        self.assertEqual("a","b")

    def testAttribute(self):
        self.runTests("core/attribute.pec")
        self.error()

    def testAttributes(self):
        self.runTests("core/attributes.pec")

    def testError(self):
        self.runTests("core/error.pec")

    def testMath(self):
        self.runTests("core/math.pec")

    def testTime(self):
        self.runTests("core/time.pec")


