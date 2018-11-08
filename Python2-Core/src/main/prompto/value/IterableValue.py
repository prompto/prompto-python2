from io import StringIO

from prompto.value.BaseValue import BaseValue
from prompto.value.IIterable import IIterable
from prompto.store.InvalidValueError import InvalidValueError
from prompto.runtime.Variable import Variable

class IterableValue(BaseValue, IIterable):

    def __init__(self, context, name, itemType, source, length, expression):
        from prompto.type.IteratorType import IteratorType
        super(IterableValue, self).__init__(IteratorType(itemType))
        self.context = context
        self.name = name
        self.itemType = itemType
        self.source = source
        self.length = length
        self.expression = expression


    def getIterator(self, context):
        for value in self.source:
            child = context.newChildContext()
            child.registerValue(Variable(self.name, self.itemType))
            child.setValue(self.name, value)
            value = self.expression.interpret(child)
            yield value


    def getMemberValue(self, context, name, autoCreate):
        if "count"==name:
            return self.length
        else:
            return super(IterableValue, self).getMemberValue(context, name, autoCreate)


    def __str__(self):
        with StringIO() as sb:
            for item in self.getIterator(self.context):
                sb.write(unicode(item))
                sb.write(u", ")
            len = sb.tell()
            if len > 0:
                sb.truncate(len - 2)
            return sb.getvalue()

