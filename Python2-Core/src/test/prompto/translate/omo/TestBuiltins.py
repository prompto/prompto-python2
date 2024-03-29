from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestBuiltins(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDateDayOfMonth(self):
        self.compareResourceOMO("builtins/dateDayOfMonth.poc")

    def testDateDayOfYear(self):
        self.compareResourceOMO("builtins/dateDayOfYear.poc")

    def testDateMonth(self):
        self.compareResourceOMO("builtins/dateMonth.poc")

    def testDateTimeDayOfMonth(self):
        self.compareResourceOMO("builtins/dateTimeDayOfMonth.poc")

    def testDateTimeDayOfYear(self):
        self.compareResourceOMO("builtins/dateTimeDayOfYear.poc")

    def testDateTimeHour(self):
        self.compareResourceOMO("builtins/dateTimeHour.poc")

    def testDateTimeMinute(self):
        self.compareResourceOMO("builtins/dateTimeMinute.poc")

    def testDateTimeMonth(self):
        self.compareResourceOMO("builtins/dateTimeMonth.poc")

    def testDateTimeSecond(self):
        self.compareResourceOMO("builtins/dateTimeSecond.poc")

    def testDateTimeTZName(self):
        self.compareResourceOMO("builtins/dateTimeTZName.poc")

    def testDateTimeTZOffset(self):
        self.compareResourceOMO("builtins/dateTimeTZOffset.poc")

    def testDateTimeYear(self):
        self.compareResourceOMO("builtins/dateTimeYear.poc")

    def testDateYear(self):
        self.compareResourceOMO("builtins/dateYear.poc")

    def testDictCount(self):
        self.compareResourceOMO("builtins/dictCount.poc")

    def testDictSwap(self):
        self.compareResourceOMO("builtins/dictSwap.poc")

    def testDocumentCount(self):
        self.compareResourceOMO("builtins/documentCount.poc")

    def testEnumName(self):
        self.compareResourceOMO("builtins/enumName.poc")

    def testEnumSymbols(self):
        self.compareResourceOMO("builtins/enumSymbols.poc")

    def testEnumValue(self):
        self.compareResourceOMO("builtins/enumValue.poc")

    def testIntegerFormat(self):
        self.compareResourceOMO("builtins/integerFormat.poc")

    def testListCount(self):
        self.compareResourceOMO("builtins/listCount.poc")

    def testListIndexOf(self):
        self.compareResourceOMO("builtins/listIndexOf.poc")

    def testListJoin(self):
        self.compareResourceOMO("builtins/listJoin.poc")

    def testPeriodDays(self):
        self.compareResourceOMO("builtins/periodDays.poc")

    def testPeriodHours(self):
        self.compareResourceOMO("builtins/periodHours.poc")

    def testPeriodMillis(self):
        self.compareResourceOMO("builtins/periodMillis.poc")

    def testPeriodMinutes(self):
        self.compareResourceOMO("builtins/periodMinutes.poc")

    def testPeriodMonths(self):
        self.compareResourceOMO("builtins/periodMonths.poc")

    def testPeriodSeconds(self):
        self.compareResourceOMO("builtins/periodSeconds.poc")

    def testPeriodWeeks(self):
        self.compareResourceOMO("builtins/periodWeeks.poc")

    def testPeriodYears(self):
        self.compareResourceOMO("builtins/periodYears.poc")

    def testSetCount(self):
        self.compareResourceOMO("builtins/setCount.poc")

    def testSetJoin(self):
        self.compareResourceOMO("builtins/setJoin.poc")

    def testTextCapitalize(self):
        self.compareResourceOMO("builtins/textCapitalize.poc")

    def testTextCount(self):
        self.compareResourceOMO("builtins/textCount.poc")

    def testTextIndexOf(self):
        self.compareResourceOMO("builtins/textIndexOf.poc")

    def testTextLowercase(self):
        self.compareResourceOMO("builtins/textLowercase.poc")

    def testTextReplace(self):
        self.compareResourceOMO("builtins/textReplace.poc")

    def testTextReplaceAll(self):
        self.compareResourceOMO("builtins/textReplaceAll.poc")

    def testTextSplit(self):
        self.compareResourceOMO("builtins/textSplit.poc")

    def testTextTrim(self):
        self.compareResourceOMO("builtins/textTrim.poc")

    def testTextUppercase(self):
        self.compareResourceOMO("builtins/textUppercase.poc")

    def testTimeHour(self):
        self.compareResourceOMO("builtins/timeHour.poc")

    def testTimeMinute(self):
        self.compareResourceOMO("builtins/timeMinute.poc")

    def testTimeSecond(self):
        self.compareResourceOMO("builtins/timeSecond.poc")

    def testTupleCount(self):
        self.compareResourceOMO("builtins/tupleCount.poc")

    def testTupleJoin(self):
        self.compareResourceOMO("builtins/tupleJoin.poc")


