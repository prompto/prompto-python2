from presto.error.IndexOutOfRangeError import *
from presto.value.Range import *


class CharacterRange(Range):

    def __init__(self, left, right):
        from presto.type.CharacterType import CharacterType
        super(CharacterRange, self).__init__(CharacterType.instance, left, right)

    def size(self):
        return 1 + ord(self.high.getValue()[0]) - ord(self.low.getValue()[0])

    def compare(self, o1, o2):
        return cmp(o1.value, o2.value)

    def computeItem(self, index):
        from presto.value.Character import Character
        result = chr(ord(self.low.getValue()[0]) + index - 1)
        if result > self.high.getValue():
            raise IndexOutOfRangeError()
        return Character(result)

    def newInstance(self, left, right):
        return CharacterRange(left, right)
