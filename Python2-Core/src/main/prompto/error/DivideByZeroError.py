from prompto.error.ExecutionError import ExecutionError


class DivideByZeroError ( ExecutionError ) :

    def getExpression(self, context):
        from prompto.grammar.CategorySymbol import CategorySymbol
        return context.getRegisteredValue(CategorySymbol, "DIVIDE_BY_ZERO")
