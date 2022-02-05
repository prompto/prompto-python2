from prompto.declaration.AbstractMethodDeclaration import AbstractMethodDeclaration


class ClosureDeclaration(AbstractMethodDeclaration):

    def __init__(self, closure):
        super(ClosureDeclaration, self).__init__(closure.itype.method.getName(), closure.itype.method.parameters, closure.itype.method.returnType)
        self.closure = closure

    def interpret(self, context):
        return self.closure.interpret(context)
