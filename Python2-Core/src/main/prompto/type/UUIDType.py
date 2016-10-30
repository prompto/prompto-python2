from prompto.type.AnyType import AnyType
from prompto.type.NativeType import NativeType
from prompto.type.TypeFamily import TypeFamily



class UUIDType(NativeType):
    instance = None

    def __init__(self):
        super(UUIDType, self).__init__(TypeFamily.UUID)

    def isAssignableTo(self, context, other):
        return isinstance(other, UUIDType) or isinstance(other, AnyType)

    def toString(self, value):
        return "'" + str(value) + "'"


UUIDType.instance = UUIDType()

