from presto.error.ExecutionError import ExecutionError


class IndexOutOfRangeError ( ExecutionError ):

    def getExpression(self, context):
        from presto.grammar.CategorySymbol import CategorySymbol
        return context.getRegisteredValue(CategorySymbol, "INDEX_OUT_OF_RANGE")
