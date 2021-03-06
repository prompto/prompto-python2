from prompto.value.BaseValue import BaseValue
from prompto.type.AnyType import AnyType

class AnyValue(BaseValue):

    def __init__(self):
        super(AnyValue, self).__init__(AnyType.instance)
        self.text = None
        self.id = id(self)

    def __str__(self):
        return "{id:" + str(self.id) + ", text:" + str(self.text) + "}"



