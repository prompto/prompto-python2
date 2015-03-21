from presto.error.IndexOutOfRangeError import IndexOutOfRangeError
from presto.value.Date import Date
from presto.value.Period import Period
from presto.value.Range import Range


class DateRange(Range):

    def __init__(self, left, right):
        from presto.type.DateType import DateType
        super(DateRange, self).__init__(DateType.instance, left, right)

    def size(self):
        h = self.high.getValue().toordinal()
        l = self.low.getValue().toordinal()
        return 1 + h - l

    def compare(self, o1, o2):
        return cmp(o1.value, o2.value)

    def computeItem(self, index):
        result = self.low.plus(Period(days=index - 1))
        if cmp(result,self.high)>0:
            raise IndexOutOfRangeError()
        return result

    def newInstance(self, left, right):
        return DateRange(left, right)
