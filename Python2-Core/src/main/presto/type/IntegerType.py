from numbers import Number
from presto.type.NativeType import NativeType


class IntegerType(NativeType):
    instance = None

    def __init__(self):
        super(IntegerType, self).__init__("Integer")

    def isAssignableTo(self, context, other):
        from presto.type.AnyType import AnyType
        from presto.type.DecimalType import DecimalType
        return isinstance(other, IntegerType) or isinstance(other, DecimalType) or isinstance(other, AnyType)

    def checkAdd(self, context, other, tryReverse):
        if isinstance(other, IntegerType):
            return self
        from presto.type.DecimalType import DecimalType
        if isinstance(other, DecimalType):
            return other
        return super(IntegerType, self).checkAdd(context, other, tryReverse)

    def checkSubstract(self, context, other):
        if isinstance(other, IntegerType):
            return self
        from presto.type.DecimalType import DecimalType
        if isinstance(other, DecimalType):
            return other
        return super(IntegerType, self).checkSubstract(context, other)

    def checkMultiply(self, context, other, tryReverse):
        from presto.type.CharacterType import CharacterType
        from presto.type.TextType import TextType
        from presto.type.PeriodType import PeriodType
        from presto.type.ListType import ListType
        if isinstance(other, IntegerType):
            return self
        from presto.type.DecimalType import DecimalType
        if isinstance(other, DecimalType):
            return other
        if isinstance(other, CharacterType):
            return TextType.instance
        if isinstance(other, TextType):
            return other
        if isinstance(other, PeriodType):
            return other
        if isinstance(other, ListType):
            return other
        return super(IntegerType, self).checkMultiply(context, other, tryReverse)

    def checkDivide(self, context, other):
        from presto.type.DecimalType import DecimalType
        if isinstance(other, IntegerType):
            return DecimalType.instance
        if isinstance(other, DecimalType):
            return other
        return super(IntegerType, self).checkDivide(context, other)

    def checkIntDivide(self, context, other):
        if isinstance(other, IntegerType):
            return IntegerType.instance
        return super(IntegerType, self).checkIntDivide(context, other)

    def checkModulo(self, context, other):
        if isinstance(other, IntegerType):
            return IntegerType.instance
        return super(IntegerType, self).checkModulo(context, other)

    def checkCompare(self, context, other):
        from presto.type.DecimalType import DecimalType
        from presto.type.BooleanType import BooleanType
        if isinstance(other, IntegerType):
            return BooleanType.instance
        if isinstance(other, DecimalType):
            return BooleanType.instance
        return super(IntegerType, self).checkCompare(context, other)

    def checkRange(self, context, other):
        if isinstance(other, IntegerType):
            from presto.type.RangeType import RangeType
            return RangeType(self)
        return super(IntegerType, self).checkCompare(context, other)

    def newRange(self, left, right):
        from presto.value.Integer import Integer
        from presto.value.IntegerRange import IntegerRange
        if isinstance(left, Integer) and isinstance(right, Integer):
            return IntegerRange(left, right)
        return super(IntegerType, self).newRange(left, right)

    def sort(self, context, source):
        def compare(o1, o2):
            return cmp(o1.value,o2.value)
        return sorted(source, cmp=compare)

    def convertPythonValueToPrestoValue(self, context, value, returnType):
        if isinstance(value, Number):
            from presto.value.Integer import Integer
            return Integer(long(value))
        else:
            return value  # TODO for now


IntegerType.instance = IntegerType()