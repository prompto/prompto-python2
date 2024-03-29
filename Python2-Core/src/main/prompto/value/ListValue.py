from io import StringIO

from prompto.value.BaseValueList import BaseValueList
from prompto.value.IFilterable import IFilterable
from prompto.value.IntegerValue import IntegerValue
from prompto.error.SyntaxError import SyntaxError
from prompto.value.NullValue import NullValue


class ListValue(BaseValueList, IFilterable):

    def __init__(self, itemType, items = None, item = None, mutable = False):
        from prompto.type.ListType import ListType
        super(ListValue, self).__init__(ListType(itemType, mutable=mutable), items, mutable)
        self.storables = None
        if item is not None:
            self.items.append(item)


    def newInstance(self, items):
        return ListValue(self.itype.itemType, items=items, mutable=self.mutable)


    def getStorableData(self):
        if self.storables is None:
            self.storables = [item.getStorableData() for item in self.items]
        return self.storables


    def convertToPython(self):
        return [ o.convertToPython() for o in self.items ]


    def Add(self, context, value):
        from prompto.value.SetValue import SetValue
        if isinstance(value, (ListValue, SetValue)):
            return self.merge(value)
        else:
            return super(ListValue, self).Add(context, value)


    def Subtract(self, context, value):
        from prompto.value.SetValue import SetValue
        if isinstance(value, ListValue):
            setValue = SetValue(self.itype.itemType)
            value = setValue.Add(context, value)
        if isinstance(value, SetValue):
            return self.remove(value)
        else:
            return super(ListValue, self).Add(context, value)

    def removeItem(self, item):
        del self.items[item.value - 1]

    def removeValue(self, value):
        idx = self.items.index(value)
        if idx > -1:
            del self.items[idx]

    def addValue(self, value):
        self.items.append(value)

    def insertValue(self, value, atIndex):
        self.items.insert(atIndex.value - 1, value)

    def indexOfValue(self, value):
        idx = self.items.index(value)
        return NullValue.instance if idx < 0 else IntegerValue(idx + 1)

    def Multiply(self, context, value):
        if isinstance(value, IntegerValue):
            count = value.IntegerValue()
            if count < 0:
                raise SyntaxError("Negative repeat count:" + count)
            elif count == 0:
                return ListValue(self.itype.itemType)
            elif count == 1:
                return self
            else:
                result = []
                for i in range(1,count+1):
                    result.extend(self.items)
                return ListValue(self.itype.itemType, items=result)
        else:
            raise SyntaxError("Illegal: List * " + type(value).__name__)


    def toJson(self, context, generator, instanceId, fieldName, withType, binaries):
        generator.writeStartArray()
        [ o.toJson(context, generator, instanceId, fieldName, withType, binaries) for o in self.items ]
        generator.writeEndArray()


    def __str__(self):
        with StringIO() as sb:
            sb.write(u"[")
            for v in self.items:
                sb.write(unicode(v))
                sb.write(u", ")
            len = sb.tell()
            if len > 2:
                sb.seek(len - 2)
                sb.truncate(len - 2)
            sb.write(u"]")
            return sb.getvalue()


    def filter(self, predicate):
        items = list(filter(predicate, self.items))
        return ListValue(self.itype.itemType, items)


    def collectStorables(self, list):
        for item in self.items:
            item.collectStorables(list)


    def toSetValue(self, context):
        from prompto.value.SetValue import SetValue
        return SetValue(self.itype.itemType, items=set(self.items))
