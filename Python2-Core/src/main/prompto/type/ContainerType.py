from prompto.type.IterableType import IterableType


class ContainerType ( IterableType ) :

    def __init__(self, name, itemType):
        super(ContainerType, self).__init__(name, itemType)

    def checkContains(self, context, other):
        if self.itemType.isAssignableTo(context, other):
            from prompto.type.BooleanType import BooleanType
            return BooleanType.instance
        else:
            return super(ContainerType, self).checkContains(context, other)