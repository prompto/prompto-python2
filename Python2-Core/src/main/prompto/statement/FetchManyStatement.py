from prompto.expression.FetchManyExpression import FetchManyExpression


class FetchManyStatement(FetchManyExpression):

    def __init__(self, typ, predicate, first, last, orderBy, name, stmts):
        super(FetchManyStatement, self).__init__(typ,predicate, first, last, orderBy)
        self.name = name
        self.stmts = stmts


    def canReturn(self):
        return False

    def isSimple(self):
        return False
