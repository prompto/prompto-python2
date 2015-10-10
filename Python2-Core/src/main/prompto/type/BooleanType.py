from prompto.type.AnyType import AnyType
from prompto.type.NativeType import NativeType

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

    def convertPythonValueToPromptoValue(self, context, value, returnType):
        if isinstance(value, bool):
            from prompto.value.Boolean import Boolean
            return Boolean.ValueOf(value)
        else:
            return value  # TODO for now


BooleanType.instance = BooleanType()

