import codecs
from antlr4 import *
from antlr4.InputStream import InputStream
from prompto.parser.OParser import OParser
from prompto.parser.ONamingLexer import ONamingLexer
from prompto.parser.OPromptoBuilder import OPromptoBuilder


class OCleverParser(OParser):

    def __init__(self, path=None, stream=None, text=None):
        self.path = path
        chars = None
        if stream is not None:
            bytes = stream.read()
            data = bytes if isinstance(bytes, unicode) else codecs.decode(bytes, "utf-8")
            chars = InputStream(data)
            stream.close()
        elif text is not None:
            chars = InputStream(text)
        if chars is not None:
            lexer = ONamingLexer(chars)
            tokens = CommonTokenStream(lexer)
            super(OCleverParser, self).__init__(tokens)


    def parse(self):
        return self.doParse(self.declaration_list)


    def equalToken(self):
        return OParser.EQ


    def doParse(self, rule):
        tree = rule()
        builder = OPromptoBuilder(self)
        walker = ParseTreeWalker()
        walker.walk(builder, tree)
        return builder.getNodeValue(tree)
