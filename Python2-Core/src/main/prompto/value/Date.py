from datetime import date, datetime, timedelta

from prompto.value.BaseValue import BaseValue
from prompto.value.Integer import Integer
from prompto.value.Period import Period
from prompto.error.SyntaxError import SyntaxError

class Date ( BaseValue ):

    @staticmethod
    def Parse(text):
        years = int(text[0:4])
        months = int(text[5:7])
        days = int(text[8:10])
        return Date(years=years,months=months,days=days)

    def __init__(self, value=None, years=None, months=None, days=None):
        from prompto.type.DateType import DateType
        super(Date, self).__init__(DateType.instance)
        if value is None:
            value = date(years, months, days)
        self.value = value

    def getValue(self):
        return self.value

    def Add(self, context, value):
        if isinstance(value, Period):
            return self.plus(value)
        else:
            raise SyntaxError("Illegal: Date + " + type(value).__name__)
 
    def Subtract(self, context, value):
        if isinstance(value, Date):
            td = self.value - value.value
            return Period(delta=td)
        elif isinstance(value, Period):
            return self.minus(value)
        else:
            raise SyntaxError("Illegal: Date - " + type(value).__name__)

    def compareTo(self, context, value):
        if isinstance(value, Date):
            return cmp(self.value,value.value)
        else:
            raise SyntaxError("Illegal comparison: Date - " + type(value).__name__)

    def GetMember(self, context, name, autoCreate=False):
        if "year"==name:
            return Integer(self.value.year)
        elif "month"==name:
            return Integer(self.value.month)
        elif "dayOfMonth"==name:
            return Integer(self.value.day)
        elif "dayOfYear"==name:
            day = 1 + self.value.toordinal() - date(self.value.year,1,1).toordinal()
            return Integer(day)
        else:
            raise SyntaxError("No such member:" + name)
 
    def ConvertTo(self, type_):
        return self.value
    
    def toDateMidnight(self):
        return self

    def minus(self, period):
        dt = datetime(self.value.year, self.value.month, self.value.day)
        td = timedelta(weeks=period.weeks, days=period.days)
        month = self.value.month - period.months
        year = self.value.year - period.years - month / 12
        month %= 12
        value = dt.replace(year=year, month=month) - td
        return Date(value.date())

    def plus(self, period):
        dt = datetime(self.value.year, self.value.month, self.value.day)
        td = timedelta(weeks=period.weeks, days=period.days)
        month = self.value.month + period.months
        year = self.value.year + period.years + month / 12
        month %= 12
        value = dt.replace(year=year, month=month) + td
        return Date(value.date())

    def __eq__(self, other):
        return self.value == other.value

    def __cmp__(self, other):
        if isinstance(other, Date):
            return cmp(self.value,other.value)
        else:
            return cmp(self.value,other)

    def __str__(self):
        return self.value.isoformat()

    def __hash__(self):
        return hash(self.value)