from prompto.expression.FetchManyExpression import FetchManyExpression
from prompto.type.CursorType import CursorType


class FetchManyStatement(FetchManyExpression):

    def __init__(self, typ, predicate, first, last, orderBy, thenWith):
        super(FetchManyStatement, self).__init__(typ,predicate, first, last, orderBy)
        self.thenWith = thenWith


    def canReturn(self):
        return False

    def isSimple(self):
        return False


    def check(self, context):
        super(FetchManyStatement, self).check(context)
        return self.thenWith.check(context, CursorType(self.typ))


    def interpret(self, context):
        record = super(FetchManyStatement, self).interpret(context)
        return self.thenWith.interpret(context, record)


    def toDialect(self, writer):
        super(FetchManyStatement, self).toDialect(writer)
        self.thenWith.toDialect(writer, CursorType(self.typ))

