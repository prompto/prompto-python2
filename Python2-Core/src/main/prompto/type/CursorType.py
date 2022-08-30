from prompto.declaration.BuiltInMethodDeclaration import BuiltInMethodDeclaration
from prompto.type.IterableType import IterableType
from prompto.type.IntegerType import IntegerType
from prompto.store.TypeFamily import TypeFamily
from prompto.type.ListType import ListType


class CursorType(IterableType):

    def __init__(self, itemType):
        super(CursorType, self).__init__(TypeFamily.CURSOR, itemType)
        self.typeName = "Cursor<" + itemType.typeName+">"


    def isAssignableFrom(self, context, other):
        return super(CursorType, self).isAssignableFrom(context, other) or \
               (isinstance(other, CursorType) and self.itemType.isAssignableFrom(context, other.itemType))


    def __eq__(self, obj):
        if obj is self:
            return True
        if not isinstance(obj, CursorType):
            return False
        return self.itemType==obj.itemType


    def checkIterator(self, context):
        return self.itemType


    def checkMember(self, context, name):
        if "count"==name:
            return IntegerType.instance
        elif "totalCount" == name:
            return IntegerType.instance
        else:
            return super(CursorType, self).checkMember(context, name)


    def withItemType(self, itemType):
        return CursorType(itemType)


    def getMemberMethods(self, context, name):
        if name == "toList":
            return [ToListMethodDeclaration(self.itemType)]
        else:
            return super(CursorType, self).getMemberMethods(context, name)


class ToListMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self, itemType):
        super(ToListMethodDeclaration, self).__init__("toList")
        self.itemType = itemType


    def interpret(self, context):
        value = self.getValue(context)
        return value.toListValue(context)


    def check(self, context):
        return ListType(self.itemType, False)
