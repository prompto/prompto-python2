from presto.error.IndexOutOfRangeError import IndexOutOfRangeError
from presto.value.Integer import Integer
from presto.value.Range import Range


class IntegerRange ( Range ):

    def __init__(self, left, right):
        from presto.type.IntegerType import IntegerType
        super(IntegerRange, self).__init__(IntegerType.instance, left, right)

    def size(self):
        return 1 + self.high.IntegerValue() - self.low.IntegerValue()

    def compare(self, o1,  o2):
        return cmp(o1.value,o2.value)

    def computeItem(self, index):
        result = self.low.IntegerValue() + index - 1
        if result>self.high.IntegerValue():
            raise IndexOutOfRangeError()
        return Integer(result)

    def newInstance(self, left, right):
        return IntegerRange(left, right)
