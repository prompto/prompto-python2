from prompto.expression.FetchOneExpression import FetchOneExpression


class FetchOneStatement(FetchOneExpression):

    def __init__(self, typ, predicate, thenWith):
        super(FetchOneStatement, self).__init__(typ, predicate)
        self.thenWith = thenWith


    def canReturn(self):
        return False


    def isSimple(self):
        return False


    def check(self, context):
        super(FetchOneStatement, self).check(context)
        return self.thenWith.check(context, self.typ)


    def interpret(self, context):
        record = super(FetchOneStatement, self).interpret(context)
        return self.thenWith.interpret(context, record)


    def toDialect(self, writer):
        super(FetchOneStatement, self).toDialect(writer)
        self.thenWith.toDialect(writer, self.typ)

