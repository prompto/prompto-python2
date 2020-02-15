from prompto.literal.Literal import *
from prompto.type.TextType import *
from prompto.utils.StringUtils import unescape


class TextLiteral(Literal):

    def __init__(self, text):
        from prompto.value.TextValue import TextValue
        s = unescape(text)
        value = TextValue(s)
        super(TextLiteral, self).__init__(text, value)

    def check(self, context):
        return TextType.instance
