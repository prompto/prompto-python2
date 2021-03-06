from prompto.literal.Literal import Literal

class CharacterLiteral(Literal):

    def __init__(self, text):
        from prompto.value.CharacterValue import CharacterValue
        value = CharacterValue(eval(compile(text, "__no_file__", mode='eval')))
        super(CharacterLiteral, self).__init__(text, value)

    def check(self, context):
        from prompto.type.CharacterType import CharacterType
        return CharacterType.instance
