import codecs
from antlr4 import *
from antlr4.InputStream import InputStream
from prompto.parser.MParser import MParser
from prompto.parser.MIndentingLexer import MIndentingLexer
from prompto.parser.MPromptoBuilder import MPromptoBuilder


class MCleverParser(MParser):

    def __init__(self, path=None, stream=None, text=None):
        chars = None
        self.path = path
        if stream is not None:
            bytes = stream.read()
            data = bytes if isinstance(bytes, unicode) else codecs.decode(bytes, "utf-8")
            chars = InputStream(data)
            stream.close()
        elif text is not None:
            chars = InputStream(text)
        if chars is not None:
            lexer = MIndentingLexer(chars)
            tokens = CommonTokenStream(lexer)
            super(MCleverParser, self).__init__(tokens)


    def parse(self):
        return self.doParse(self.declaration_list, False)

    def equalToken(self):
        return MParser.EQ

    def doParse(self, rule, addLF):
        self.getTokenStream().tokenSource.addLF = addLF
        tree = rule()
        builder = MPromptoBuilder(self)
        walker = ParseTreeWalker()
        walker.walk(builder, tree)
        return builder.getNodeValue(tree)
