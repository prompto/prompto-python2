from prompto.error.IndexOutOfRangeError import IndexOutOfRangeError
from prompto.error.InternalError import InternalError
from prompto.value.BaseValue import BaseValue
from prompto.value.IRange import IRange
from prompto.value.IValue import IValue
from prompto.value.IntegerValue import IntegerValue


class RangeValue(BaseValue, IRange):

    def __init__(self, itemType, left, right):
        from prompto.type.RangeType import RangeType
        super(RangeValue, self).__init__(RangeType(itemType))
        # can't just use T extends Comparable<T> because LocalDate and LocalTime extend Comparable<R>
        cmp_ = self.compare(left, right)
        if cmp_ < 0:
            self.low = left
            self.high = right
        else:
            self.low = right
            self.high = left

    def __str__(self):
        return "[" + ("" if self.low is None else str(self.low)) + ".." \
               + ("" if self.high is None else str(self.high)) + "]"

    def getLow(self):
        return self.low

    def getHigh(self):
        return self.high

    def isEmpty(self):
        return self.size() == 0

    def __eq__(self, obj):
        if not isinstance(obj, RangeValue):
            return False
        else:
            return self.low == obj.low and self.high == obj.high

    def getMemberValue(self, context, name, autoCreate=False):
        if name == "count":
            return IntegerValue(self.size())
        else:
            return super(RangeValue, self).getMemberValue(context, name, autoCreate)


    def hasItem(self, context, val):
        return cmp(val,self.low) >= 0 and cmp(val,self.high) <= 0


    def getItem(self, context, index):
        if isinstance(index, IntegerValue):
            try:
                value = self.computeItem(index.IntegerValue())
                if isinstance(value, IValue):
                    return value
                else:
                    raise InternalError("Item not a value!")
            except IndexError:
                raise IndexOutOfRangeError()
        else:
            raise SyntaxError("No such item:" + str(index))

    def slice(self, fi, li):
        size = self.size()
        _fi = 1L if fi is None else fi.IntegerValue()
        if _fi < 1:
            raise IndexOutOfRangeError()
        _li = size if li is None else li.IntegerValue()
        if _li < 1:
            _li = size + 1 + _li;
        elif _li > size:
            raise IndexOutOfRangeError()
        return self.newInstance(self.computeItem(_fi), self.computeItem(_li))

    def getIterator(self, context):
        size = self.size()
        index = 1
        while index <= size:
            yield self.getItem(context, IntegerValue(index))
            index += 1
