from prompto.store.InvalidValueError import InvalidValueError
from prompto.type.NativeType import NativeType
from prompto.type.IntegerType import IntegerType
from prompto.store.TypeFamily import TypeFamily



class CharacterType(NativeType):
    instance = None

    def __init__(self):
        super(CharacterType, self).__init__(TypeFamily.CHARACTER)


    def checkMember(self, context, name):
        if "codePoint" == name:
            return IntegerType.instance
        else:
            return super(CharacterType, self).checkMember(context, name)


    def checkAdd(self, context, other, tryReverse):
        from prompto.type.TextType import TextType
        return TextType.instance


    def checkMultiply(self, context, other, tryReverse):
        from prompto.type.IntegerType import IntegerType
        if isinstance(other, IntegerType):
            from prompto.type.TextType import TextType
            return TextType.instance
        else:
            return super(CharacterType, self).checkMultiply(context, other, tryReverse)


    def checkCompare(self, context, other):
        from prompto.type.TextType import TextType
        from prompto.type.BooleanType import BooleanType
        if isinstance(other, CharacterType) or isinstance(other, TextType):
            return BooleanType.instance
        return super(CharacterType, self).checkCompare(context, other)


    def checkRange(self, context, other):
        if isinstance(other, CharacterType):
            from prompto.type.RangeType import RangeType
            return RangeType(self)
        return super(CharacterType, self).checkRange(context, other)

    def newRange(self, left, right):
        from prompto.value.CharacterValue import CharacterValue
        if isinstance(left, CharacterValue) and isinstance(right, CharacterValue):
            from prompto.value.CharacterRange import CharacterRange
            return CharacterRange(left, right)
        return super(CharacterType, self).newRange(left, right)


    def toString(self, value):
        return "'" + str(value) + "'"


    def convertPythonValueToPromptoValue(self, context, value, returnType):
        if isinstance(value, basestring):
            from prompto.value.CharacterValue import CharacterValue
            return CharacterValue(value)
        else:
            return super(CharacterType, self).convertPythonValueToPromptoValue(context, value, returnType)  # TODO for now

    def nativeCast(self, context, value):
        from prompto.type.TextType import TextType
        if isinstance(value.itype, TextType) and len(value.value)>=1:
            from prompto.value.CharacterValue import CharacterValue
            return CharacterValue(value.value[0:1])
        else:
            raise InvalidValueError("Cannot convert " + str(value) + " to Character")

CharacterType.instance = CharacterType()

