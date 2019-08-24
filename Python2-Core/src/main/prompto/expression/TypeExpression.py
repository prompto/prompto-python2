from prompto.expression.IExpression import IExpression
from prompto.value.TypeValue import TypeValue
from prompto.type.TypeType import TypeType


class TypeExpression(IExpression):

    def __init__(self, typ):
        self.typ = typ

    def __str__(self):
        return str(self.typ)

    def check(self, context):
        return TypeType(self.typ)

    def interpret(self, context):
        return TypeValue(self.typ)

    def getMemberValue(self, context, name):
        return self.typ.getStaticMemberValue(context, name)

    def toDialect(self, writer):
        self.typ.toDialect(writer)