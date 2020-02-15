from prompto.error.IndexOutOfRangeError import IndexOutOfRangeError
from prompto.value.RangeValue import RangeValue
from prompto.value.TimeValue import TimeValue
from prompto.value.PeriodValue import PeriodValue


class TimeRange(RangeValue):

    def __init__(self, left, right):
        from prompto.type.TimeType import TimeType
        super(TimeRange, self).__init__(TimeType.instance, left, right)

    def size(self):
        return 1 + (self.high.getMillisOfDay() - self.low.getMillisOfDay()) / 1000;

    def compare(self, o1, o2):
        return cmp(o1.value, o2.value)

    def computeItem(self, index):
        result = self.low.plus(PeriodValue(seconds=index - 1))
        if cmp(result.value,self.high.value)>0:
            raise IndexOutOfRangeError()
        return result

    def newInstance(self, left, right):
        return TimeRange(left, right)
