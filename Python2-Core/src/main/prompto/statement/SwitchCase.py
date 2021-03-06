from prompto.parser.ISection import ISection
from prompto.parser.Section import Section


class SwitchCase ( Section, ISection ):

    def __init__(self, expression, statements):
        super(SwitchCase, self).__init__()
        self.expression = expression
        self.statements = statements

    def checkReturnType(self, context):
        return self.statements.check(context, None)

    def interpret(self, context):
        return self.statements.interpret(context)


class SwitchCaseList(list):

    def __init__(self, item=None):
        super(SwitchCaseList, self).__init__()
        if item is not None:
            self.append(item)
