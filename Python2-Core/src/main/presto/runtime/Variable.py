from presto.grammar.INamedValue import INamedValue


class Variable ( INamedValue ):

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __str__(self):
        return self.name

    def getName(self):
        return self.name

    def getType(self, context):
        return self.type
