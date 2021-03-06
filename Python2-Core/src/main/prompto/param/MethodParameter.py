from prompto.expression.ArrowExpression import ArrowExpression
from prompto.param.BaseParameter import BaseParameter
from prompto.declaration.IMethodDeclaration import IMethodDeclaration
from prompto.grammar.INamedInstance import INamedInstance
from prompto.type.MethodType import MethodType
from prompto.error.SyntaxError import SyntaxError
from prompto.value.ArrowValue import ArrowValue
from prompto.value.ContextualExpression import ContextualExpression


class MethodParameter (BaseParameter):


    def __init__(self, name):
        super(MethodParameter, self).__init__(name)


    def getSignature(self, dialect):
        return self.getName()


    def __str__(self):
        return self.getName()


    def getProto(self):
        return self.getName()


    def __eq__(self, obj):
        if id(obj)==id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, MethodParameter):
            return False
        return self.getName()==obj.getName()


    def register(self, context):
        actual = context.getRegisteredValue(INamedInstance, self.name)
        if actual is not None:
            raise SyntaxError("Duplicate argument: \"" + self.name + "\"")
        context.registerValue(self)


    def check(self, context):
        actual = context.getRegisteredDeclaration(IMethodDeclaration,self.name)
        if actual is None:
            raise SyntaxError("Unknown method: \"" + self.name + "\"")


    def checkValue(self, context, expression):
        isArrow = isinstance(expression, ContextualExpression) and isinstance(expression.expression, ArrowExpression)
        if isArrow:
            return self.checkArrowValue(context, expression)
        else:
            return super(MethodParameter, self).checkValue(context, expression)


    def checkArrowValue(self, context, expression):
        return ArrowValue(self.getDeclaration(context), expression.calling, expression.expression) # TODO check


    def getType(self, context):
        method = self.getDeclaration(context)
        return MethodType(method)


    def getDeclaration(self, context):
        from prompto.runtime.Context import MethodDeclarationMap
        methods = context.getRegisteredDeclaration(MethodDeclarationMap, self.name)
        if methods is not None:
            return methods.getFirst()
        else:
            return None
