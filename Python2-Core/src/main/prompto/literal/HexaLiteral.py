from prompto.literal.Literal import Literal
from prompto.value.IntegerValue import IntegerValue


class HexaLiteral(Literal):
    def __init__(self, text):
        super(HexaLiteral, self).__init__(text, HexaLiteral.parseHexa(text))

    def check(self, context):
        from prompto.type.IntegerType import IntegerType
        return IntegerType.instance

    @staticmethod
    def parseHexa(text):
        value = 0
        for c in text[2:]:
            value <<= 4
            if c >= '0' and c <= '9':
                value += (ord(c) - ord('0'))
            elif c >= 'a' and c <= 'f':
                value += (ord(c) - ord('a'))
            elif c >= 'A' and c <= 'F':
                value += 10 + (ord(c) - ord('A'))
            else:
                from prompto.store.InvalidValueError import InvalidValueError
                raise InvalidDataError(text + " is not a valid hexadecimal number")
        return IntegerValue(value)
