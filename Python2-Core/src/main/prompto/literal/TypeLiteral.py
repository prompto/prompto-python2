from prompto.expression.IExpression import IExpression
from prompto.parser.Dialect import Dialect
from prompto.parser.Section import Section
from prompto.runtime.Context import MethodDeclarationMap
from prompto.type.TypeType import TypeType
from prompto.value.TypeValue import TypeValue


class TypeLiteral(Section, IExpression):

    def __init__(self, itype):
        super(Section, self).__init__()
        self.itype = itype


    def check(self, context):
        return TypeType(self.itype)


    def interpret(self, context):
        return TypeValue(self.itype)


    def toDialect(self, writer):
        if writer.dialect is Dialect.E:
            decl = writer.context.getRegisteredDeclaration(MethodDeclarationMap, self.itype.typeName)
            if isinstance(decl, MethodDeclarationMap):
                writer.append("Method: ")
            else:
                writer.append("Type: ")
        self.itype.toDialect(writer)


    def parentToDialect(self, writer):
        self.itype.toDialect(writer)


    def __str__(self):
        return str(self.itype)
