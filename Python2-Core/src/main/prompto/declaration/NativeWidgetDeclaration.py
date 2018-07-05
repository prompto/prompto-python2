from prompto.declaration.NativeCategoryDeclaration import NativeCategoryDeclaration


class NativeWidgetDeclaration(NativeCategoryDeclaration):

    def __init__(self,name, categoryBindings, methods):
        super(NativeWidgetDeclaration, self).__init__(name, None, categoryBindings, None, methods)


    def categoryTypeToEDialect(self, writer):
        writer.append("native widget")

    def categoryTypeToODialect(self, writer):
        writer.append("native widget")

    def categoryTypeToMDialect(self, writer):
        writer.append("native widget")
