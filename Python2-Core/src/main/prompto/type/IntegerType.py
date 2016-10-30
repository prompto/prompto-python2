from numbers import Number
from prompto.type.NativeType import NativeType
from prompto.type.TypeFamily import TypeFamily



class IntegerType(NativeType):

    instance = None

    def __init__(self):
        super(IntegerType, self).__init__(TypeFamily.INTEGER)

    def isAssignableTo(self, context, other):
        from prompto.type.AnyType import AnyType
        from prompto.type.DecimalType import DecimalType
        return isinstance(other, IntegerType) or isinstance(other, DecimalType) or isinstance(other, AnyType)

    def checkAdd(self, context, other, tryReverse):
        if isinstance(other, IntegerType):
            return self
        from prompto.type.DecimalType import DecimalType
        if isinstance(other, DecimalType):
            return other
        return super(IntegerType, self).checkAdd(context, other, tryReverse)

    def checkSubstract(self, context, other):
        if isinstance(other, IntegerType):
            return self
        from prompto.type.DecimalType import DecimalType
        if isinstance(other, DecimalType):
            return other
        return super(IntegerType, self).checkSubstract(context, other)

    def checkMultiply(self, context, other, tryReverse):
        from prompto.type.CharacterType import CharacterType
        from prompto.type.TextType import TextType
        from prompto.type.PeriodType import PeriodType
        from prompto.type.ListType import ListType
        if isinstance(other, IntegerType):
            return self
        from prompto.type.DecimalType import DecimalType
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
        from prompto.type.DecimalType import DecimalType
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
        from prompto.type.DecimalType import DecimalType
        from prompto.type.BooleanType import BooleanType
        if isinstance(other, IntegerType):
            return BooleanType.instance
        if isinstance(other, DecimalType):
            return BooleanType.instance
        return super(IntegerType, self).checkCompare(context, other)

    def checkRange(self, context, other):
        if isinstance(other, IntegerType):
            from prompto.type.RangeType import RangeType
            return RangeType(self)
        return super(IntegerType, self).checkRange(context, other)

    def newRange(self, left, right):
        from prompto.value.Integer import Integer
        from prompto.value.IntegerRange import IntegerRange
        if isinstance(left, Integer) and isinstance(right, Integer):
            return IntegerRange(left, right)
        return super(IntegerType, self).newRange(left, right)

    def sort(self, context, source, desc):
        return sorted(source, reverse=desc)

    def convertPythonValueToPromptoValue(self, context, value, returnType):
        if isinstance(value, Number):
            from prompto.value.Integer import Integer
            return Integer(long(value))
        else:
            return value  # TODO for now


IntegerType.instance = IntegerType()