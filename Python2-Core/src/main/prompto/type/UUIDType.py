from prompto.type.AnyType import AnyType
from prompto.type.NativeType import NativeType
from prompto.store.TypeFamily import TypeFamily



class UUIDType(NativeType):
    instance = None

    def __init__(self):
        super(UUIDType, self).__init__(TypeFamily.UUID)


    def toString(self, value):
        return "'" + str(value) + "'"


UUIDType.instance = UUIDType()

