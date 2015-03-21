from presto.declaration.AbstractMethodDeclaration import AbstractMethodDeclaration


class ClosureDeclaration(AbstractMethodDeclaration):

    def __init__(self, closure):
        super(ClosureDeclaration, self).__init__(closure.method.getName(), closure.method.getArguments(), closure.method.getReturnType())
        self.closure = closure

    def interpret(self, context):
        return self.closure.interpret(context)
