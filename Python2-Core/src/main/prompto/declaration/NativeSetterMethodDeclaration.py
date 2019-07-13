from prompto.declaration.SetterMethodDeclaration import SetterMethodDeclaration

class NativeSetterMethodDeclaration(SetterMethodDeclaration):

    def __init__(self, name, statements):
        super(NativeSetterMethodDeclaration, self).__init__(name, statements)


    def checkStatements(self, context, returnType):
        return self.statements.checkNative(context, returnType)
