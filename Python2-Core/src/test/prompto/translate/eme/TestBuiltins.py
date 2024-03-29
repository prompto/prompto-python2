from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestBuiltins(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testBooleanJson(self):
        self.compareResourceEME("builtins/booleanJson.pec")

    def testBooleanText(self):
        self.compareResourceEME("builtins/booleanText.pec")

    def testCategoryCategory(self):
        self.compareResourceEME("builtins/categoryCategory.pec")

    def testCategoryJson(self):
        self.compareResourceEME("builtins/categoryJson.pec")

    def testCategoryText(self):
        self.compareResourceEME("builtins/categoryText.pec")

    def testCharCodePoint(self):
        self.compareResourceEME("builtins/charCodePoint.pec")

    def testCharJson(self):
        self.compareResourceEME("builtins/charJson.pec")

    def testCharText(self):
        self.compareResourceEME("builtins/charText.pec")

    def testCursorToList(self):
        self.compareResourceEME("builtins/cursorToList.pec")

    def testDateDayOfMonth(self):
        self.compareResourceEME("builtins/dateDayOfMonth.pec")

    def testDateDayOfYear(self):
        self.compareResourceEME("builtins/dateDayOfYear.pec")

    def testDateJson(self):
        self.compareResourceEME("builtins/dateJson.pec")

    def testDateMonth(self):
        self.compareResourceEME("builtins/dateMonth.pec")

    def testDateText(self):
        self.compareResourceEME("builtins/dateText.pec")

    def testDateTimeDate(self):
        self.compareResourceEME("builtins/dateTimeDate.pec")

    def testDateTimeDayOfMonth(self):
        self.compareResourceEME("builtins/dateTimeDayOfMonth.pec")

    def testDateTimeDayOfYear(self):
        self.compareResourceEME("builtins/dateTimeDayOfYear.pec")

    def testDateTimeHour(self):
        self.compareResourceEME("builtins/dateTimeHour.pec")

    def testDateTimeJson(self):
        self.compareResourceEME("builtins/dateTimeJson.pec")

    def testDateTimeMilli(self):
        self.compareResourceEME("builtins/dateTimeMilli.pec")

    def testDateTimeMinute(self):
        self.compareResourceEME("builtins/dateTimeMinute.pec")

    def testDateTimeMonth(self):
        self.compareResourceEME("builtins/dateTimeMonth.pec")

    def testDateTimeSecond(self):
        self.compareResourceEME("builtins/dateTimeSecond.pec")

    def testDateTimeTZName(self):
        self.compareResourceEME("builtins/dateTimeTZName.pec")

    def testDateTimeTZOffset(self):
        self.compareResourceEME("builtins/dateTimeTZOffset.pec")

    def testDateTimeText(self):
        self.compareResourceEME("builtins/dateTimeText.pec")

    def testDateTimeTime(self):
        self.compareResourceEME("builtins/dateTimeTime.pec")

    def testDateTimeYear(self):
        self.compareResourceEME("builtins/dateTimeYear.pec")

    def testDateYear(self):
        self.compareResourceEME("builtins/dateYear.pec")

    def testDecimalJson(self):
        self.compareResourceEME("builtins/decimalJson.pec")

    def testDecimalText(self):
        self.compareResourceEME("builtins/decimalText.pec")

    def testDictCount(self):
        self.compareResourceEME("builtins/dictCount.pec")

    def testDictJson(self):
        self.compareResourceEME("builtins/dictJson.pec")

    def testDictKeys(self):
        self.compareResourceEME("builtins/dictKeys.pec")

    def testDictText(self):
        self.compareResourceEME("builtins/dictText.pec")

    def testDictValues(self):
        self.compareResourceEME("builtins/dictValues.pec")

    def testDocumentCount(self):
        self.compareResourceEME("builtins/documentCount.pec")

    def testDocumentJson(self):
        self.compareResourceEME("builtins/documentJson.pec")

    def testDocumentKeys(self):
        self.compareResourceEME("builtins/documentKeys.pec")

    def testDocumentText(self):
        self.compareResourceEME("builtins/documentText.pec")

    def testDocumentValues(self):
        self.compareResourceEME("builtins/documentValues.pec")

    def testEnumName(self):
        self.compareResourceEME("builtins/enumName.pec")

    def testEnumSymbols(self):
        self.compareResourceEME("builtins/enumSymbols.pec")

    def testEnumValue(self):
        self.compareResourceEME("builtins/enumValue.pec")

    def testIntegerFormat(self):
        self.compareResourceEME("builtins/integerFormat.pec")

    def testIntegerJson(self):
        self.compareResourceEME("builtins/integerJson.pec")

    def testIntegerText(self):
        self.compareResourceEME("builtins/integerText.pec")

    def testIteratorToList(self):
        self.compareResourceEME("builtins/iteratorToList.pec")

    def testIteratorToSet(self):
        self.compareResourceEME("builtins/iteratorToSet.pec")

    def testListCount(self):
        self.compareResourceEME("builtins/listCount.pec")

    def testListIndexOf(self):
        self.compareResourceEME("builtins/listIndexOf.pec")

    def testListJson(self):
        self.compareResourceEME("builtins/listJson.pec")

    def testListText(self):
        self.compareResourceEME("builtins/listText.pec")

    def testListToSet(self):
        self.compareResourceEME("builtins/listToSet.pec")

    def testPeriodDays(self):
        self.compareResourceEME("builtins/periodDays.pec")

    def testPeriodHours(self):
        self.compareResourceEME("builtins/periodHours.pec")

    def testPeriodJson(self):
        self.compareResourceEME("builtins/periodJson.pec")

    def testPeriodMillis(self):
        self.compareResourceEME("builtins/periodMillis.pec")

    def testPeriodMinutes(self):
        self.compareResourceEME("builtins/periodMinutes.pec")

    def testPeriodMonths(self):
        self.compareResourceEME("builtins/periodMonths.pec")

    def testPeriodSeconds(self):
        self.compareResourceEME("builtins/periodSeconds.pec")

    def testPeriodText(self):
        self.compareResourceEME("builtins/periodText.pec")

    def testPeriodWeeks(self):
        self.compareResourceEME("builtins/periodWeeks.pec")

    def testPeriodYears(self):
        self.compareResourceEME("builtins/periodYears.pec")

    def testSetCount(self):
        self.compareResourceEME("builtins/setCount.pec")

    def testSetJson(self):
        self.compareResourceEME("builtins/setJson.pec")

    def testSetText(self):
        self.compareResourceEME("builtins/setText.pec")

    def testSetToList(self):
        self.compareResourceEME("builtins/setToList.pec")

    def testTextCapitalize(self):
        self.compareResourceEME("builtins/textCapitalize.pec")

    def testTextCount(self):
        self.compareResourceEME("builtins/textCount.pec")

    def testTextEndsWith(self):
        self.compareResourceEME("builtins/textEndsWith.pec")

    def testTextJson(self):
        self.compareResourceEME("builtins/textJson.pec")

    def testTextLowercase(self):
        self.compareResourceEME("builtins/textLowercase.pec")

    def testTextReplace(self):
        self.compareResourceEME("builtins/textReplace.pec")

    def testTextReplaceAll(self):
        self.compareResourceEME("builtins/textReplaceAll.pec")

    def testTextSplit(self):
        self.compareResourceEME("builtins/textSplit.pec")

    def testTextStartsWith(self):
        self.compareResourceEME("builtins/textStartsWith.pec")

    def testTextText(self):
        self.compareResourceEME("builtins/textText.pec")

    def testTextTrim(self):
        self.compareResourceEME("builtins/textTrim.pec")

    def testTextUppercase(self):
        self.compareResourceEME("builtins/textUppercase.pec")

    def testTimeHour(self):
        self.compareResourceEME("builtins/timeHour.pec")

    def testTimeJson(self):
        self.compareResourceEME("builtins/timeJson.pec")

    def testTimeMilli(self):
        self.compareResourceEME("builtins/timeMilli.pec")

    def testTimeMinute(self):
        self.compareResourceEME("builtins/timeMinute.pec")

    def testTimeSecond(self):
        self.compareResourceEME("builtins/timeSecond.pec")

    def testTimeText(self):
        self.compareResourceEME("builtins/timeText.pec")

    def testTupleCount(self):
        self.compareResourceEME("builtins/tupleCount.pec")

    def testTupleText(self):
        self.compareResourceEME("builtins/tupleText.pec")

    def testUuidJson(self):
        self.compareResourceEME("builtins/uuidJson.pec")

    def testUuidText(self):
        self.compareResourceEME("builtins/uuidText.pec")

    def testVersionMembers(self):
        self.compareResourceEME("builtins/versionMembers.pec")


