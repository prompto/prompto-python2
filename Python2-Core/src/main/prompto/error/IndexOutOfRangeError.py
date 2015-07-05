from prompto.error.ExecutionError import ExecutionError


class IndexOutOfRangeError ( ExecutionError ):

    def getExpression(self, context):
        from prompto.grammar.CategorySymbol import CategorySymbol
        return context.getRegisteredValue(CategorySymbol, "INDEX_OUT_OF_RANGE")
