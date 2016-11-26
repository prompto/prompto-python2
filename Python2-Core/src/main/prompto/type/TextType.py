from prompto.declaration.BuiltInMethodDeclaration import BuiltInMethodDeclaration
from prompto.type.NativeType import NativeType
from prompto.store.TypeFamily import TypeFamily



class TextType(NativeType):
    instance = None

    def __init__(self):
        super(TextType, self).__init__(TypeFamily.TEXT)

    def isAssignableFrom(self, context, other):
        from prompto.type.CharacterType import CharacterType
        return super(TextType, self).isAssignableFrom(context, other) or \
               other is CharacterType.instance


    def checkAdd(self, context, other, tryReverse):
        return self

    def checkMultiply(self, context, other, tryReverse):
        from prompto.type.IntegerType import IntegerType
        if isinstance(other, IntegerType):
            return self
        else:
            return super(TextType, self).checkMultiply(context, other, tryReverse)

    def checkCompare(self, context, other):
        from prompto.type.BooleanType import BooleanType
        from prompto.type.CharacterType import CharacterType
        if isinstance(other, TextType) or isinstance(other, CharacterType):
            return BooleanType.instance
        return super(TextType, self).checkCompare(context, other)


    def checkItem(self, context, other):
        from prompto.type.IntegerType import IntegerType
        from prompto.type.CharacterType import CharacterType
        if other == IntegerType.instance:
            return CharacterType.instance
        else:
            return super(TextType, self).checkItem(context, other)


    def checkMember(self, context, name):
        from prompto.type.IntegerType import IntegerType
        if "count" == name:
            return IntegerType.instance
        else:
            return super(TextType, self).checkMember(context, name)


    def checkContains(self, context, other):
        from prompto.type.BooleanType import BooleanType
        from prompto.type.CharacterType import CharacterType
        if isinstance(other, TextType) or isinstance(other, CharacterType):
            return BooleanType.instance
        return super(TextType, self).checkContains(context, other)


    def checkContainsAllOrAny(self, context, other):
        from prompto.type.BooleanType import BooleanType
        return BooleanType.instance


    def checkSlice(self, context):
        return self


    def sort(self, context, list_, desc):
        return sorted(list_, reverse=desc)


    def convertPythonValueToPromptoValue(self, context, value, returnType):
        from prompto.value.Text import Text
        if isinstance(value, basestring):
            return Text(value)
        else:
            return value  # TODO for now

    def getMemberMethods(self, context, name):
        if name == "toLowerCase":
            return [ToLowerCaseMethodDeclaration()]
        elif name == "toUpperCase":
            return [ToUpperCaseMethodDeclaration()]
        elif name == "toCapitalized":
            return [ToCapitalizedMethodDeclaration()]
        elif name == "split":
            return [SplitMethodDeclaration()]
        elif name == "trim":
            return [TrimMethodDeclaration()]
        else:
            return super(TextType, self).getMemberMethods(context, name)


TextType.instance = TextType()


class SplitMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        from prompto.argument.CategoryArgument import CategoryArgument
        from prompto.literal.TextLiteral import TextLiteral
        SINGLE_SPACE_ARGUMENT = CategoryArgument(TextType.instance, "separator", TextLiteral('" "'))
        super(SplitMethodDeclaration, self).__init__("split", SINGLE_SPACE_ARGUMENT)


    def interpret(self, context):
        from prompto.value.Text import Text
        from prompto.value.ListValue import ListValue
        value = self.getValue(context).value
        sep = context.getValue("separator").value
        parts = [ Text(part) for part in value.split(sep)]
        return ListValue(TextType.instance, parts, mutable = False)


    def check(self, context):
        from prompto.type.ListType import ListType
        return ListType(TextType.instance)


class ToLowerCaseMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        super(ToLowerCaseMethodDeclaration, self).__init__("toLowerCase")


    def interpret(self, context):
        from prompto.value.Text import Text
        value = self.getValue(context).getStorableData()
        return Text(value.lower())

    def check(self, context):
        return TextType.instance



class ToUpperCaseMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        super(ToUpperCaseMethodDeclaration, self).__init__("toUpperCase")



    def interpret(self, context):
        from prompto.value.Text import Text
        value = self.getValue(context).getStorableData()
        return Text(value.upper())



    def check(self, context):
        return TextType.instance



class ToCapitalizedMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        super(ToCapitalizedMethodDeclaration, self).__init__("toCapitalized")



    def interpret(self, context):
        from prompto.value.Text import Text
        value = self.getValue(context).getStorableData()
        return Text(value.title())



    def check(self, context):
        return TextType.instance


class TrimMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        super(TrimMethodDeclaration, self).__init__("trim")



    def interpret(self, context):
        from prompto.value.Text import Text
        value = self.getValue(context).getStorableData()
        return Text(value.strip())



    def check(self, context):
        return TextType.instance


