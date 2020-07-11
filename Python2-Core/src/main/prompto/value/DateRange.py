from prompto.error.IndexOutOfRangeError import IndexOutOfRangeError
from prompto.value.PeriodValue import PeriodValue
from prompto.value.RangeValue import RangeValue


class DateRange(RangeValue):

    def __init__(self, left, right):
        from prompto.type.DateType import DateType
        super(DateRange, self).__init__(DateType.instance, left, right)

    def size(self):
        h = self.high.getValue().toordinal()
        l = self.low.getValue().toordinal()
        return 1 + h - l

    def compare(self, o1, o2):
        return cmp(o1.value, o2.value)

    def computeItem(self, index):
        result = self.low.plusPeriod(PeriodValue(days=index - 1))
        if cmp(result,self.high)>0:
            raise IndexOutOfRangeError()
        return result

    def newInstance(self, left, right):
        return DateRange(left, right)
