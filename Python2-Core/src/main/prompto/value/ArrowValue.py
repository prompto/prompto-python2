from prompto.value.ContextualExpression import ContextualExpression


class ArrowValue(ContextualExpression):

    def __init__(self, method, calling, arrow):
        super(ArrowValue, self).__init__(calling, arrow)
        self.method = method


    def interpret(self, context):
        parent = context.getParentContext()
        try:
            context.setParentContext(self.calling)
            return self.expression.interpret(context)
        except:
            context.setParentContext(parent)
