from uuid import UUID
from prompto.type.NativeType import NativeType
from prompto.store.TypeFamily import TypeFamily



class UUIDType(NativeType):
    instance = None

    def __init__(self):
        super(UUIDType, self).__init__(TypeFamily.UUID)


    def toString(self, value):
        return "'" + str(value) + "'"


    def convertPythonValueToPromptoValue(self, context, value, returnType):
        from prompto.value.UUIDValue import UUIDValue
        if isinstance(value, UUID):
            return UUIDValue(value)
        else:
            return super(self, UUIDType).convertPythonValueToPromptoValue(context, value, returnType)



UUIDType.instance = UUIDType()

