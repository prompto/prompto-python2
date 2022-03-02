from prompto.value.BaseValue import BaseValue
from prompto.value.INumber import INumber
from prompto.value.IMultiplyable import IMultiplyable
from prompto.value.DecimalValue import DecimalValue
from prompto.error.SyntaxError import SyntaxError

class IntegerValue(BaseValue, INumber, IMultiplyable):

    @staticmethod
    def Parse(text):
        return IntegerValue(long(text))

    def __init__(self, value):
        from prompto.type.IntegerType import IntegerType
        super(IntegerValue, self).__init__(IntegerType.instance)
        self.value = value

    def getStorableData(self):
        return self.value

    def convertoPython(self):
        return self.value

    def IntegerValue(self):
        return self.value

    def DecimalValue(self):
        return float(self.value)

    def Add(self, context, value):
        if isinstance(value, IntegerValue):
            return IntegerValue(self.IntegerValue() + value.IntegerValue())
        elif isinstance(value, DecimalValue):
            return DecimalValue(value.DecimalValue() + self.value)
        else:
            raise SyntaxError("Illegal: Integer + " + type(value).__name__)

    def Subtract(self, context, value):
        if isinstance(value, IntegerValue):
            return IntegerValue(self.IntegerValue() - value.IntegerValue())
        elif isinstance(value, DecimalValue):
            return DecimalValue(self.DecimalValue() - value.DecimalValue())
        else:
            raise SyntaxError("Illegal: Integer - " + type(value).__name__)

    def Multiply(self, context, value):
        if isinstance(value, IntegerValue):
            return IntegerValue(self.IntegerValue() * value.IntegerValue())
        elif isinstance(value, DecimalValue):
            return DecimalValue(value.DecimalValue() * self.IntegerValue())
        elif isinstance(value, IMultiplyable):
            return value.Multiply(context, self)
        else:
            raise SyntaxError("Illegal: Integer * " + type(value).__name__)

    def Divide(self, context, value):
        from prompto.error.DivideByZeroError import DivideByZeroError
        if isinstance(value, INumber):
            if value.DecimalValue() == 0.0:
                raise DivideByZeroError()
            else:
                return DecimalValue(self.DecimalValue() / value.DecimalValue())
        else:
            raise SyntaxError("Illegal: Integer / " + type(value).__name__)

    def IntDivide(self, context, value):
        from prompto.error.DivideByZeroError import DivideByZeroError
        if isinstance(value, IntegerValue):
            if value.IntegerValue() == 0:
                raise DivideByZeroError()
            else:
                return IntegerValue(int(self.IntegerValue() // value.IntegerValue()))
        else:
            raise SyntaxError("Illegal: Integer \\ " + type(value).__name__)

    def Modulo(self, context, value):
        from prompto.error.DivideByZeroError import DivideByZeroError
        if isinstance(value, IntegerValue):
            mod = value.IntegerValue()
            if mod == 0:
                raise DivideByZeroError()
            return IntegerValue(self.IntegerValue() % mod)
        else:
            raise SyntaxError("Illegal: Integer % " + type(value).__name__)

    def CompareTo(self, context, value):
        if isinstance(value, IntegerValue):
            return cmp(self.value, value.IntegerValue())
        elif isinstance(value, DecimalValue):
            return cmp(self.DecimalValue(), value.DecimalValue())
        else:
            raise SyntaxError("Illegal comparison: Integer and " + type(value).__name__)

    def ConvertTo(self, itype):
        return self.value

    def __str__(self):
        return str(self.value)

    def __cmp__(self, obj):
        return isinstance(obj, (IntegerValue, DecimalValue) ) and cmp(self.value, obj.value)

    def __eq__(self, obj):
        return isinstance(obj, (IntegerValue, DecimalValue) ) and self.value == obj.value

    def __hash__(self):
        return hash(self.value)

    def toJson(self, context, generator, instanceId, fieldName, withType, binaries):
        generator.writeLong(self.value)

    def toJsonNode(self):
        return self.value
