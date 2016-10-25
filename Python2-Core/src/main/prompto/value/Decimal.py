from prompto.value.BaseValue import BaseValue
from prompto.value.INumber import INumber
from prompto.value.IMultiplyable import IMultiplyable
from prompto.error.SyntaxError import SyntaxError


class Decimal(BaseValue, INumber, IMultiplyable):

    @staticmethod
    def Parse(text):
        return Decimal(float(text))

    def __init__(self, value):
        from prompto.type.DecimalType import DecimalType
        super(Decimal, self).__init__(DecimalType.instance)
        self.value = value

    def convertToPython(self):
        return self.value

    def IntegerValue(self):
        return long(self.value)

    def DecimalValue(self):
        return self.value

    def Add(self, context, value):
        from prompto.value.Integer import Integer
        if isinstance(value, Integer):
            return Decimal(self.value + value.IntegerValue())
        elif isinstance(value, Decimal):
            return Decimal(self.value + value.DecimalValue())
        else:
            raise SyntaxError("Illegal: Decimal + " + type(value).__name__)

    def Subtract(self, context, value):
        from prompto.value.Integer import Integer
        if isinstance(value, Integer):
            return Decimal(self.value - value.IntegerValue())
        elif isinstance(value, Decimal):
            return Decimal(self.value - value.DecimalValue())
        else:
            raise SyntaxError("Illegal: Decimal - " + type(value).__name__)


    def Multiply(self, context, value):
        from prompto.value.Integer import Integer
        if isinstance(value, Integer):
            return Decimal(self.DecimalValue() * value.IntegerValue())
        elif isinstance(value, Decimal):
            return Decimal(self.DecimalValue() * value.DecimalValue())
        else:
            raise SyntaxError("Illegal: Decimal * " + type(value).__name__)


    def Divide(self, context, value):
        from prompto.error.DivideByZeroError import DivideByZeroError
        if isinstance(value, INumber):
            if value.DecimalValue() == 0.0:
                raise DivideByZeroError()
            else:
                return Decimal(self.DecimalValue() / value.DecimalValue())
        else:
            raise SyntaxError("Illegal: Decimal / " + type(value).__name__)

    def IntDivide(self, context, value):
        from prompto.error.DivideByZeroError import DivideByZeroError
        from prompto.value.Integer import Integer
        if isinstance(value, Integer):
            if value.IntegerValue() == 0.:
                raise DivideByZeroError()
            else:
                return Integer(int(self.DecimalValue() // value.IntegerValue()))
        else:
            raise SyntaxError("Illegal: Decimal / " + type(value).__name__)

    def Modulo(self, context, value):
        from prompto.error.DivideByZeroError import DivideByZeroError
        if isinstance(value, INumber):
            if value.DecimalValue() == 0.0:
                raise DivideByZeroError()
            else:
                return Decimal(self.DecimalValue() % value.DecimalValue())
        else:
            raise SyntaxError("Illegal: Decimal % " + type(value).__name__)

    def compareTo(self, context, value):
        if isinstance(value, INumber):
            return cmp(self.value,value.DecimalValue())
        else:
            raise SyntaxError("Illegal comparison: Decimal and " + type(value).__name__)


    def ConvertTo(self, type_):
        return self.value


    def __str__(self):
        return str(self.value)  #.ToString("0.0######")


    def __eq__(self, obj):
        if isinstance(obj, INumber):
            return self.value == obj.value
        else:
            return False


    def __cmp__(self, other):
        if isinstance(other, INumber):
            return cmp(self.value, other.value)
        else:
            return cmp(self.value, other)


    def __hash__(self):
        return hash(self.value)
