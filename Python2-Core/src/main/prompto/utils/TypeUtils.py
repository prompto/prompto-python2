import types

from datetime import datetime, timedelta, time, date
from uuid import UUID

from prompto.type.AnyType import AnyType
from prompto.type.DateTimeType import DateTimeType
from prompto.type.DateType import DateType
from prompto.type.DecimalType import DecimalType
from prompto.type.DocumentType import DocumentType
from prompto.type.IntegerType import IntegerType
from prompto.type.BooleanType import BooleanType
from prompto.type.PeriodType import PeriodType
from prompto.type.TextType import TextType
from prompto.type.TimeType import TimeType
from prompto.type.UUIDType import UUIDType
from prompto.type.VoidType import VoidType

def fieldToValue(context, name, data):
    if data is None:
        return None
    else:
        typ = fieldType(context, name, data)
        return typ.convertPythonValueToPromptoValue(context, data, None)


def fieldType(context, name, data):
    if name=="dbId":
        return typeToIType(type(data))
    else:
        decl = context.getRegisteredDeclaration(name)
        return decl.itype

typeToITypeDict = { types.NoneType: VoidType.instance,
                    types.BooleanType : BooleanType.instance,
                    types.IntType : IntegerType.instance,
                    types.FloatType : DecimalType.instance,
                    types.StringType : TextType.instance,
                    types.UnicodeType : TextType.instance,
                    type(UUID) : UUIDType.instance,
                    type(date) : DateType.instance ,
                    type(time) : TimeType.instance,
                    type(datetime) : DateTimeType.instance,
                    type(timedelta) : PeriodType.instance,
                    type(dict) : DocumentType.instance,
                    type(object) : AnyType.instance
                  }

def typeToIType(typ):
    return typeToITypeDict.get(typ, None)



