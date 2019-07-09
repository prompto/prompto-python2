from prompto.expression.IExpression import IExpression
from prompto.value.TypeValue import TypeValue


class TypeExpression(IExpression):

    def __init__(self, typ):
        self.typ = typ

    def __str__(self):
        return str(self.typ)

    def check(self, context):
        return self.typ

    def interpret(self, context):
        return TypeValue(self.typ)

    def getMemberValue(self, context, name):
        return self.typ.getMemberValue(context, name)

    def toDialect(self, writer):
        self.typ.toDialect(writer)