from prompto.python.PythonExpression import PythonExpression

class PythonLiteral (PythonExpression):

    def __init__(self, text):
        super(PythonLiteral,self).__init__()
        self.text = text
        self.value = eval(compile(text, "__no_file__", mode='eval'))

    def __str__(self):
        return self.text

    def interpret(self, context, module):
        return self.value

    def toDialect(self, writer):
        writer.append(self.text)
