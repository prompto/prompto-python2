# used to ensure downcast local resolves to actual value */
from presto.value.IValue import IValue


class LinkedValue(IValue):

    def __init__(self, context):
        self.context = context
