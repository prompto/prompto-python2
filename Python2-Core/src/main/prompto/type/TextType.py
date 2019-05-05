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


    def convertPythonValueToPromptoValue(self, context, value, returnType):
        from prompto.value.Text import Text
        if isinstance(value, basestring):
            return Text(value)
        else:
            return value  # TODO for now

    def getMemberMethods(self, context, name):
        if name == "startsWith":
            return [StartsWithMethodDeclaration()]
        elif name == "endsWith":
            return [EndsWithMethodDeclaration()]
        elif name == "toLowerCase":
            return [ToLowerCaseMethodDeclaration()]
        elif name == "toUpperCase":
            return [ToUpperCaseMethodDeclaration()]
        elif name == "toCapitalized":
            return [ToCapitalizedMethodDeclaration()]
        elif name == "replace":
            return [ReplaceMethodDeclaration()]
        elif name == "replaceAll":
            return [ReplaceAllMethodDeclaration()]
        elif name == "split":
            return [SplitMethodDeclaration()]
        elif name == "trim":
            return [TrimMethodDeclaration()]
        elif name == "indexOf":
            return [IndexOfMethodDeclaration()]
        else:
            return super(TextType, self).getMemberMethods(context, name)


TextType.instance = TextType()

class StartsWithMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        from prompto.argument.CategoryArgument import CategoryArgument
        VALUE_ARGUMENT = CategoryArgument(TextType.instance, "value")
        super(StartsWithMethodDeclaration, self).__init__("startsWith", VALUE_ARGUMENT)


    def interpret(self, context):
        from prompto.value.Boolean import Boolean
        value = self.getValue(context).value
        find = context.getValue("value").value
        startsWith = value.startswith(find)
        return Boolean.ValueOf(startsWith)


    def check(self, context, isStart):
        from prompto.type.BooleanType import BooleanType
        return BooleanType.instance


class EndsWithMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        from prompto.argument.CategoryArgument import CategoryArgument
        VALUE_ARGUMENT = CategoryArgument(TextType.instance, "value")
        super(EndsWithMethodDeclaration, self).__init__("endsWith", VALUE_ARGUMENT)


    def interpret(self, context):
        from prompto.value.Boolean import Boolean
        value = self.getValue(context).value
        find = context.getValue("value").value
        endsWith = value.endswith(find)
        return Boolean.ValueOf(endsWith)


    def check(self, context, isStart):
        from prompto.type.BooleanType import BooleanType
        return BooleanType.instance




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


    def check(self, context, isStart):
        from prompto.type.ListType import ListType
        return ListType(TextType.instance)


class ReplaceMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        from prompto.argument.CategoryArgument import CategoryArgument
        TO_REPLACE_ARGUMENT = CategoryArgument(TextType.instance, "toReplace")
        REPLACE_WITH_ARGUMENT = CategoryArgument(TextType.instance, "replaceWith")
        super(ReplaceMethodDeclaration, self).__init__("replace", TO_REPLACE_ARGUMENT, REPLACE_WITH_ARGUMENT)


    def interpret(self, context):
        from prompto.value.Text import Text
        value = self.getValue(context).value
        toReplace = context.getValue("toReplace").value
        replaceWith = context.getValue("replaceWith").value
        value = value.replace(toReplace, replaceWith, 1)
        return Text(value)


    def check(self, context, isStart):
        return TextType.instance


class ReplaceAllMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        from prompto.argument.CategoryArgument import CategoryArgument
        TO_REPLACE_ARGUMENT = CategoryArgument(TextType.instance, "toReplace")
        REPLACE_WITH_ARGUMENT = CategoryArgument(TextType.instance, "replaceWith")
        super(ReplaceAllMethodDeclaration, self).__init__("replaceAll", TO_REPLACE_ARGUMENT, REPLACE_WITH_ARGUMENT)


    def interpret(self, context):
        from prompto.value.Text import Text
        value = self.getValue(context).value
        toReplace = context.getValue("toReplace").value
        replaceWith = context.getValue("replaceWith").value
        value = value.replace(toReplace, replaceWith)
        return Text(value)


    def check(self, context, isStart):
        return TextType.instance


class ToLowerCaseMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        super(ToLowerCaseMethodDeclaration, self).__init__("toLowerCase")


    def interpret(self, context):
        from prompto.value.Text import Text
        value = self.getValue(context).getStorableData()
        return Text(value.lower())

    def check(self, context, isStart):
        return TextType.instance



class ToUpperCaseMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        super(ToUpperCaseMethodDeclaration, self).__init__("toUpperCase")


    def interpret(self, context):
        from prompto.value.Text import Text
        value = self.getValue(context).getStorableData()
        return Text(value.upper())


    def check(self, context, isStart):
        return TextType.instance



class ToCapitalizedMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        super(ToCapitalizedMethodDeclaration, self).__init__("toCapitalized")


    def interpret(self, context):
        from prompto.value.Text import Text
        value = self.getValue(context).getStorableData()
        return Text(value.title())


    def check(self, context, isStart):
        return TextType.instance


class TrimMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        super(TrimMethodDeclaration, self).__init__("trim")


    def interpret(self, context):
        from prompto.value.Text import Text
        value = self.getValue(context).getStorableData()
        return Text(value.strip())


    def check(self, context, isStart):
        return TextType.instance


class IndexOfMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        from prompto.argument.CategoryArgument import CategoryArgument
        VALUE_ARGUMENT = CategoryArgument(TextType.instance, "value")
        super(IndexOfMethodDeclaration, self).__init__("indexOf", VALUE_ARGUMENT)


    def interpret(self, context):
        from prompto.value.Integer import Integer
        value = self.getValue(context).value
        find = context.getValue("value").value
        index = value.index(find)
        return Integer(index + 1)


    def check(self, context, isStart):
        from prompto.type.IntegerType import IntegerType
        return IntegerType.instance


