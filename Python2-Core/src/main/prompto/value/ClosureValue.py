from prompto.value.BaseValue import BaseValue

class ClosureValue(BaseValue):

    def __init__(self, context, typ):
        super(ClosureValue, self).__init__(typ)
        self.context = context


    def interpret(self, context):
        parentMost = self.context.getParentMostContext()
        savedParent = parentMost.getParentContext()
        parentMost.setParentContext(context)
        try:
            local = self.context.newChildContext()
            return self.doInterpret(local)
        finally:
            parentMost.setParentContext(savedParent)

    def doInterpret(self, local):
        return self.itype.method.interpret(local)

