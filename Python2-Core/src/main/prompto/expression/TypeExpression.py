from prompto.expression.IExpression import IExpression
from prompto.value.TypeValue import TypeValue
from prompto.type.TypeType import TypeType


class TypeExpression(IExpression):

    def __init__(self, itype):
        self.itype = itype

    def __str__(self):
        return str(self.itype)

    def check(self, context):
        return TypeType(self.itype)

    def interpret(self, context):
        return TypeValue(self.itype)

    def getMemberValue(self, context, name):
        return self.itype.getStaticMemberValue(context, name)

    def toDialect(self, writer):
        writer.append(str(self.itype))