from presto.type.AnyType import AnyType
from presto.type.NativeType import NativeType

class BooleanType(NativeType):

    instance = None

    def __init__(self):
        super(BooleanType, self).__init__("Boolean")

    def isAssignableTo(self, context, other):
        return isinstance(other, BooleanType) or isinstance(other, AnyType)

    def sort(self, context, source):
        def compare(o1, o2):
            return cmp(o1.value,o2.value)
        return sorted(source, cmp=compare)

    def convertPythonValueToPrestoValue(self, value):
        if isinstance(value, bool):
            from presto.value.Boolean import Boolean
            return Boolean.ValueOf(value)
        else:
            return value  # TODO for now


BooleanType.instance = BooleanType()

