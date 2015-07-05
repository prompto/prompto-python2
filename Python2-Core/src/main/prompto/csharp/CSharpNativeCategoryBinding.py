from prompto.grammar.NativeCategoryBinding import NativeCategoryBinding


class CSharpNativeCategoryBinding ( NativeCategoryBinding ):

    def __init__(self, expression):
        super(CSharpNativeCategoryBinding, self).__init__()
        self.expression = expression

    def toDialect(self, writer):
        writer.append("C#: ")
        self.expression.toDialect(writer)
