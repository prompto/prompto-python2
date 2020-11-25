# Generated from ArgsLexer.g4 by ANTLR 4.9
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"\7\60\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\3\2\3\2\3\2\7\2\23\n\2\f\2\16\2\26\13\2\3\2\3\2")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\"\n\3\3\4\3\4\3")
        buf.write(u"\5\3\5\3\6\3\6\3\6\3\6\3\7\6\7-\n\7\r\7\16\7.\2\2\b\3")
        buf.write(u"\3\5\2\7\4\t\5\13\6\r\7\3\2\5\6\2\f\f\17\17$$^^\n\2$")
        buf.write(u"$))^^ddhhppttvv\b\2\13\f\17\17\"\"$$//??\2\64\2\3\3\2")
        buf.write(u"\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write(u"\3\17\3\2\2\2\5\31\3\2\2\2\7#\3\2\2\2\t%\3\2\2\2\13\'")
        buf.write(u"\3\2\2\2\r,\3\2\2\2\17\24\7$\2\2\20\23\5\5\3\2\21\23")
        buf.write(u"\n\2\2\2\22\20\3\2\2\2\22\21\3\2\2\2\23\26\3\2\2\2\24")
        buf.write(u"\22\3\2\2\2\24\25\3\2\2\2\25\27\3\2\2\2\26\24\3\2\2\2")
        buf.write(u"\27\30\7$\2\2\30\4\3\2\2\2\31!\7^\2\2\32\"\t\3\2\2\33")
        buf.write(u"\34\4\62\65\2\34\35\4\629\2\35\"\4\629\2\36\37\4\629")
        buf.write(u"\2\37\"\4\629\2 \"\4\629\2!\32\3\2\2\2!\33\3\2\2\2!\36")
        buf.write(u"\3\2\2\2! \3\2\2\2\"\6\3\2\2\2#$\7?\2\2$\b\3\2\2\2%&")
        buf.write(u"\7/\2\2&\n\3\2\2\2\'(\7\"\2\2()\3\2\2\2)*\b\6\2\2*\f")
        buf.write(u"\3\2\2\2+-\n\4\2\2,+\3\2\2\2-.\3\2\2\2.,\3\2\2\2./\3")
        buf.write(u"\2\2\2/\16\3\2\2\2\7\2\22\24!.\3\b\2\2")
        return buf.getvalue()


class ArgsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    STRING = 1
    EQUALS = 2
    DASH = 3
    WS = 4
    ELEMENT = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'='", u"'-'", u"' '" ]

    symbolicNames = [ u"<INVALID>",
            u"STRING", u"EQUALS", u"DASH", u"WS", u"ELEMENT" ]

    ruleNames = [ u"STRING", u"EscapeSequence", u"EQUALS", u"DASH", u"WS", 
                  u"ELEMENT" ]

    grammarFileName = u"ArgsLexer.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(ArgsLexer, self).__init__(input, output=output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


