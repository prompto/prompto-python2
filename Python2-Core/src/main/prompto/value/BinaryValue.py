from prompto.value.BaseValue import BaseValue


class BinaryValue(BaseValue):

    def __init__(self, itype, mimeType, data):
        super(BinaryValue, self).__init__(itype)
        self.mimeType = mimeType
        self.data = data

