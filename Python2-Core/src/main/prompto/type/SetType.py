from prompto.type.BooleanType import BooleanType
from prompto.type.ContainerType import ContainerType, BaseJoinMethodDeclaration
from prompto.store.TypeFamily import TypeFamily



class SetType(ContainerType):

    def __init__(self, itemType):
        super(SetType, self).__init__(TypeFamily.SET, itemType)
        self.typeName = itemType.typeName + "<>"


    def isAssignableFrom(self, context, other):
        return super(SetType, self).isAssignableFrom(context, other) or \
               (isinstance(other, SetType) and self.itemType.isAssignableFrom(context, other.itemType))


    def __eq__(self, obj):
        if id(obj) == id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, SetType):
            return False
        return self.itemType == obj.itemType


    def checkAdd(self, context, other, tryReverse):
        from prompto.type.ListType import ListType
        if isinstance(other, (ListType, SetType)) and self.itemType.isAssignableFrom(context, other.itemType):
            return self
        else:
            return super(SetType, self).checkAdd(context, other, tryReverse)


    def checkSubstract(self, context, other):
        from prompto.type.ListType import ListType
        if isinstance(other, (ListType, SetType)) and self.itemType == other.itemType:
            return self
        else:
            return super(SetType, self).checkSubstract(context, other)


    def checkItem(self, context, other):
        from prompto.type.IntegerType import IntegerType
        if other == IntegerType.instance:
            return self.itemType
        else:
            return super(SetType, self).checkItem(context, other)


    def checkContainsAllOrAny(self, context, other):
        return BooleanType.instance


    def checkIterator(self, context):
        return self.itemType


    def checkMember(self, context, name):
        from prompto.type.IntegerType import IntegerType
        if "count" == name:
            return IntegerType.instance
        else:
            return super(SetType, self).checkMember(context, name)


    def getMemberMethods(self, context, name):
        if name == "join":
            return [JoinSetMethodDeclaration()]
        else:
            return super(SetType, self).getMemberMethods(context, name)


    def withItemType(self, itemType):
        return SetType(itemType)


class JoinSetMethodDeclaration(BaseJoinMethodDeclaration):

    def getItems(self, context):
        return self.getValue(context).items
