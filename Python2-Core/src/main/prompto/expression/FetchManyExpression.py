from prompto.expression.IExpression import IExpression
from prompto.declaration.CategoryDeclaration import CategoryDeclaration
from prompto.parser.Section import Section
from prompto.error.SyntaxError import SyntaxError
from prompto.store.AttributeInfo import AttributeInfo
from prompto.store.InvalidValueError import InvalidValueError
from prompto.store.MatchOp import MatchOp
from prompto.store.TypeFamily import TypeFamily
from prompto.type.AnyType import AnyType
from prompto.type.BooleanType import BooleanType
from prompto.type.CursorType import CursorType
from prompto.store.DataStore import DataStore
from prompto.value.CursorValue import CursorValue

class FetchManyExpression(Section, IExpression):

    def __init__(self, typ, predicate, first, last, include, orderBy):
        self.typ = typ
        self.first = first
        self.last = last
        self.predicate = predicate
        self.include = include
        self.orderBy = orderBy


    def toEDialect (self, writer):
        writer.append("fetch ")
        if self.first is None:
            writer.append("all ")
        if self.typ is not None:
            if self.typ.mutable:
                writer.append("mutable ")
            writer.append(self.typ.typeName)
        if self.first is not None:
            self.first.toDialect(writer)
            writer.append(" to ")
            self.last.toDialect(writer)
            writer.append(" ")
        if self.predicate is not None:
            writer.append("where ")
            self.predicate.toDialect(writer)
        if self.include is not None:
            writer.append(" include ")
            if len(self.include) == 1:
                writer.append(self.include[0])
            else:
                for i in range(0, len(self.include) - 1):
                    writer.append(self.include[i]).append(", ")
                writer.trimLast(len(", "))
                writer.append(" and ")
                writer.append(self.include[-1])
        if self.orderBy is not None:
            self.orderBy.toDialect(writer)


    def toODialect (self, writer):
        writer.append("fetch ")
        if self.first is None:
            writer.append("all ")
        if self.typ is not None:
            writer.append("( ")
            if self.typ.mutable:
                writer.append("mutable ")
            writer.append(self.typ.typeName)
            writer.append(" ) ")
        if self.first is not None:
            writer.append("rows ( ")
            self.first.toDialect(writer)
            writer.append(" to ")
            self.last.toDialect(writer)
            writer.append(") ")
        if self.predicate is not None:
            writer.append(" where ( ")
            self.predicate.toDialect(writer)
            writer.append(") ")
        if self.include is not None:
            writer.append("include (")
            for name in self.include:
                writer.append(name).append(", ")
            writer.trimLast(len(", "))
            writer.append(") ")
        if self.orderBy is not None:
            self.orderBy.toDialect(writer)


    def toMDialect (self, writer):
        writer.append("fetch ")
        if self.first is not None:
            writer.append("rows ")
            self.first.toDialect(writer)
            writer.append(" to ")
            self.last.toDialect(writer)
            writer.append(" ")
        else:
            writer.append("all ")
        writer.append("(")
        if self.typ is not None:
            writer.append(" ")
            if self.typ.mutable:
                writer.append("mutable ")
            writer.append(self.typ.typeName)
            writer.append(" ")
        writer.append(") ")
        if self.predicate is not None:
            writer.append("where ")
            self.predicate.toDialect(writer)
            writer.append(" ")
        if self.include is not None:
            writer.append(" include ")
            for name in self.include:
                writer.append(name).append(", ")
            writer.trimLast(len(", "))
        if self.orderBy is not None:
            self.orderBy.toDialect(writer)

    def check (self, context):
        typ = self.typ
        if typ is None:
            typ = AnyType.instance
        else:
            decl = context.getRegisteredDeclaration (CategoryDeclaration, typ.typeName)
            if decl is None:
                raise SyntaxError ("Unknown category: " + typ.typeName)
        self.checkPredicate(context)
        self.checkInclude(context)
        self.checkOrderBy(context)
        self.checkLimits(context)
        return CursorType (typ)

    def checkInclude (self, context):
        pass # TODO

    def checkOrderBy (self, context):
        pass # TODO


    def checkLimits (self, context):
        pass # TODO


    def checkPredicate (self, context):
        if self.predicate is None:
            return
        self.predicate.checkQuery (context)


    def interpret (self, context):
        store = DataStore.instance
        query = self.buildFetchManyQuery(context, store)
        docs = store.fetchMany (query)
        typ = AnyType.instance if self.typ is None else self.typ
        return CursorValue(context, typ, docs)


    def buildFetchManyQuery(self, context, store):
        builder = store.newQueryBuilder()
        builder.setFirst(self.interpretLimit(context, self.first))
        builder.setLast(self.interpretLimit(context, self.last))
        if self.typ is not None:
            info = AttributeInfo("category", TypeFamily.TEXT, True, None)
            builder.verify(info, MatchOp.HAS, self.typ.typeName)
        if self.predicate is not None:
            self.predicate.interpretQuery(context, builder)
        if self.typ is not None and self.predicate is not None:
            builder.And()
        if self.include is not None:
            builder.project(self.include)
        if self.orderBy is not None:
            self.orderBy.interpretQuery(context, builder)
        return builder.build()


    def interpretLimit(self, context, exp):
        if exp is None:
            return None
        value = exp.interpret(context).getStorableData()
        if not isinstance(value, (int, long)):
            raise InvalidValueError("Expecting an Integer, found:" + value.type.typeName)
        return value
