from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestMethods(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAbstractMember(self):
        self.compareResourceEME("methods/abstractMember.pec")

    def testAnonymous(self):
        self.compareResourceEME("methods/anonymous.pec")

    def testAttribute(self):
        self.compareResourceEME("methods/attribute.pec")

    def testDefault(self):
        self.compareResourceEME("methods/default.pec")

    def testE_as_e_bug(self):
        self.compareResourceEME("methods/e_as_e_bug.pec")

    def testEmpty(self):
        self.compareResourceEME("methods/empty.pec")

    def testExplicit(self):
        self.compareResourceEME("methods/explicit.pec")

    def testExplicitMember(self):
        self.compareResourceEME("methods/explicitMember.pec")

    def testExpressionMember(self):
        self.compareResourceEME("methods/expressionMember.pec")

    def testExpressionWith(self):
        self.compareResourceEME("methods/expressionWith.pec")

    def testExtended(self):
        self.compareResourceEME("methods/extended.pec")

    def testGlobal(self):
        self.compareResourceEME("methods/global.pec")

    def testHomonym(self):
        self.compareResourceEME("methods/homonym.pec")

    def testHomonym2(self):
        self.compareResourceEME("methods/homonym2.pec")

    def testImplicitAnd(self):
        self.compareResourceEME("methods/implicitAnd.pec")

    def testMember(self):
        self.compareResourceEME("methods/member.pec")

    def testMemberCall(self):
        self.compareResourceEME("methods/memberCall.pec")

    def testMemberRef(self):
        self.compareResourceEME("methods/memberRef.pec")

    def testOverride(self):
        self.compareResourceEME("methods/override.pec")

    def testParameter(self):
        self.compareResourceEME("methods/parameter.pec")

    def testPolymorphicAbstract(self):
        self.compareResourceEME("methods/polymorphicAbstract.pec")

    def testPolymorphicMember(self):
        self.compareResourceEME("methods/polymorphicMember.pec")

    def testPolymorphicNamed(self):
        self.compareResourceEME("methods/polymorphicNamed.pec")

    def testPolymorphicRuntime(self):
        self.compareResourceEME("methods/polymorphicRuntime.pec")

    def testReturn(self):
        self.compareResourceEME("methods/return.pec")

    def testSpecified(self):
        self.compareResourceEME("methods/specified.pec")

    def testTextAsync(self):
        self.compareResourceEME("methods/textAsync.pec")

    def testVoidAsync(self):
        self.compareResourceEME("methods/voidAsync.pec")


