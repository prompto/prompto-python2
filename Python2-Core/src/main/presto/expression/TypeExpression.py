from presto.expression.IExpression import IExpression
from presto.value.TypeValue import TypeValue


class TypeExpression(IExpression):

    def __init__(self, type):
        self.type = type

    def __str__(self):
        return str(self.type)

    def check(self, context):
        return self.type

    def interpret(self, context):
        return TypeValue(self.type)

    def getMember(self, context, name):
        return self.type.getMember(context, name)

    def toDialect(self, writer):
        self.type.toDialect(writer)