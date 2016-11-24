from prompto.expression.IExpression import IExpression
from prompto.value.TypeValue import TypeValue


class TypeExpression(IExpression):

    def __init__(self, type):
        self.type = type

    def __str__(self):
        return str(self.type)

    def check(self, context):
        return self.type

    def interpret(self, context):
        return TypeValue(self.type)

    def getMemberValue(self, context, name):
        return self.type.getMemberValue(context, name)

    def toDialect(self, writer):
        self.type.toDialect(writer)