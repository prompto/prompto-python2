from presto.error.ExecutionError import ExecutionError


class DivideByZeroError ( ExecutionError ) :

    def getExpression(self, context):
        from presto.grammar.CategorySymbol import CategorySymbol
        return context.getRegisteredValue(CategorySymbol, "DIVIDE_BY_ZERO")
