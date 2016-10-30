from prompto.expression.IExpression import IExpression
from prompto.declaration.CategoryDeclaration import CategoryDeclaration
from prompto.parser.Section import Section
from prompto.error.SyntaxError import SyntaxError
from prompto.type.BooleanType import BooleanType
from prompto.store.DataStore import DataStore
from prompto.type.CategoryType import CategoryType
from prompto.value.NullValue import NullValue

class FetchOneExpression(Section, IExpression):

    def __init__(self, typ, predicate):
        self.typ = typ
        self.predicate = predicate

    def toEDialect (self, writer):
        writer.append ("fetch one ")
        if self.typ:
            writer.append (self.typ.typeName)
            writer.append(" ")
        writer.append ("where ")
        self.predicate.toDialect (writer)

    def toODialect (self, writer):
        writer.append ("fetch one ")
        if self.typ:
            writer.append("(")
            writer.append (self.typ.typeName)
            writer.append(") ")
        writer.append ("where (")
        self.predicate.toDialect (writer)
        writer.append (")")

    def toSDialect (self, writer):
        writer.append ("fetch one ")
        if self.typ:
            writer.append (self.typ.typeName)
            writer.append(" ")
        writer.append ("where ")
        self.predicate.toDialect (writer)

    def check (self, context):
        if self.typ is not None:
            decl = context.getRegisteredDeclaration (CategoryDeclaration, self.typ.typeName)
            if decl is None:
                raise SyntaxError ("Unknown category: " + self.typ.typeName)
        filterType = self.predicate.check (context)
        if filterType is not BooleanType.instance:
            raise SyntaxError ("Filtering expression must return a boolean !")
        return self.typ

    def interpret (self, context):
        stored = DataStore.instance.interpretFetchOne (context, self.typ, self.predicate)
        if stored is None:
            return NullValue.instance
        else:
            typeName = stored.getData("category")[-1]
            typ = CategoryType(typeName)
            if self.typ is not None:
                typ.mutable = self.typ.mutable
            return typ.newInstanceFromStored (context, stored)

