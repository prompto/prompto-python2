from prompto.declaration.ConcreteWidgetDeclaration import ConcreteWidgetDeclaration


class WrappingWidgetDeclaration(ConcreteWidgetDeclaration):

    def __init__(self, wrapped):
        super(WrappingWidgetDeclaration, self).__init__(wrapped.name, wrapped.derivedFrom, wrapped.methods)
