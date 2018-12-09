from prompto.grammar.IDialectElement import IDialectElement
from prompto.grammar.INamedValue import INamedValue


class IArgument(INamedValue, IDialectElement):

    def getType(self, context=None):
        raise Exception("Should never get there!")
