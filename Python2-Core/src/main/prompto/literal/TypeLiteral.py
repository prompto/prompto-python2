from prompto.expression.IExpression import IExpression
from prompto.parser.Dialect import Dialect
from prompto.parser.Section import Section
from prompto.type.TypeType import TypeType
from prompto.value.TypeValue import TypeValue


class TypeLiteral(Section, IExpression):

    def __init__(self, typ):
        self.typ = typ


    def check(self, context):
        return TypeType(self.typ)


    def interpret(self, context):
        return TypeValue(self.typ)


    def toDialect(self, writer):
        if writer.dialect is Dialect.E:
            writer.append("Type: ")
        self.typ.toDialect(writer)

    def parentToDialect(self, writer):
        self.typ.toDialect(writer)


    def __str__(self):
        return str(self.typ)
