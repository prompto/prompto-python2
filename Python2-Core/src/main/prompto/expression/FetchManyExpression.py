from prompto.expression.IExpression import IExpression
from prompto.declaration.CategoryDeclaration import CategoryDeclaration
from prompto.parser.Section import Section
from prompto.error.SyntaxError import SyntaxError
from prompto.type.BooleanType import BooleanType
from prompto.type.CursorType import CursorType
from prompto.store.DataStore import DataStore
from prompto.value.Cursor import Cursor

class FetchManyExpression(Section, IExpression):

    def __init__(self, typ, predicate, start, stop, orderBy):
        self.typ = typ
        self.xstart = start
        self.xstop = stop
        self.predicate = predicate
        self.orderBy = orderBy

    def toEDialect (self, writer):
        writer.append("fetch ")
        if self.xstart is None:
            writer.append("all ")
        if self.typ is not None:
            writer.append(self.typ.typeName)
        if self.xstart is not None:
            self.xstart.toDialect(writer)
            writer.append(" to ")
            self.xstop.toDialect(writer)
            writer.append(" ")
        if self.predicate is not None:
            writer.append("where ")
            self.predicate.toDialect(writer)
        if self.orderBy is not None:
            self.orderBy.toDialect(writer)

    def toODialect (self, writer):
        writer.append("fetch ")
        if self.xstart is None:
            writer.append("all ")
        if self.typ is not None:
            writer.append("( ")
            writer.append(self.typ.typeName)
            writer.append(" ) ")
        if self.xstart is not None:
            writer.append("rows ( ")
            self.xstart.toDialect(writer)
            writer.append(" to ")
            self.xstop.toDialect(writer)
            writer.append(") ")
        if self.predicate is not None:
            writer.append(" where ( ")
            self.predicate.toDialect(writer)
            writer.append(") ")
        if self.orderBy is not None:
            self.orderBy.toDialect(writer)


    def toSDialect (self, writer):
        writer.append("fetch ")
        if self.xstart is not None:
            writer.append("rows ")
            self.xstart.toDialect(writer)
            writer.append(" to ")
            self.xstop.toDialect(writer)
            writer.append(" ")
        else:
            writer.append("all ")
        if self.typ is not None:
            writer.append(" ( ")
            writer.append(self.typ.typeName)
            writer.append(" ) ")
        if self.predicate is not None:
            writer.append("where ")
            self.predicate.toDialect(writer)
        if self.orderBy is not None:
            self.orderBy.toDialect(writer)

    def check (self, context):
        decl = context.getRegisteredDeclaration (CategoryDeclaration, self.typ.typeName)
        if decl is None:
            raise SyntaxError ("Unknown category: " + self.typ.typeName)
        self.checkFilter(context)
        self.checkOrderBy(context)
        self.checkLimits(context)
        return CursorType (self.typ)

    def checkOrderBy (self, context):
        pass # TODO

    def checkLimits (self, context):
        pass # TODO

    def checkFilter (self, context):
        if self.predicate is None:
            return
        filterType = self.predicate.check (context)
        if filterType is not BooleanType.instance:
            raise SyntaxError ("Filtering expression must return a boolean !")

    def interpret (self, context):
        docs = DataStore.instance.interpretFetchMany (context, self.typ, self.xstart, self.xstop, self.predicate, self.orderBy)
        return Cursor(context, self.typ, docs)
