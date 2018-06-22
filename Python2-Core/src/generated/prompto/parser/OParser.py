# Generated from OParser.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

from .AbstractParser import AbstractParser

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\u00ae\u098f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
        buf.write(u"\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4")
        buf.write(u"\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t")
        buf.write(u"\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27")
        buf.write(u"\4\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4")
        buf.write(u"\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t")
        buf.write(u"#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4")
        buf.write(u",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62")
        buf.write(u"\4\63\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\4")
        buf.write(u"8\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@")
        buf.write(u"\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\t")
        buf.write(u"I\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R")
        buf.write(u"\tR\4S\tS\4T\tT\4U\tU\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4")
        buf.write(u"[\t[\4\\\t\\\4]\t]\4^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\t")
        buf.write(u"c\4d\td\4e\te\4f\tf\4g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l")
        buf.write(u"\tl\4m\tm\4n\tn\4o\to\4p\tp\4q\tq\4r\tr\4s\ts\4t\tt\4")
        buf.write(u"u\tu\4v\tv\4w\tw\4x\tx\4y\ty\4z\tz\4{\t{\4|\t|\4}\t}")
        buf.write(u"\4~\t~\4\177\t\177\4\u0080\t\u0080\4\u0081\t\u0081\4")
        buf.write(u"\u0082\t\u0082\4\u0083\t\u0083\4\u0084\t\u0084\4\u0085")
        buf.write(u"\t\u0085\4\u0086\t\u0086\4\u0087\t\u0087\4\u0088\t\u0088")
        buf.write(u"\4\u0089\t\u0089\4\u008a\t\u008a\4\u008b\t\u008b\4\u008c")
        buf.write(u"\t\u008c\4\u008d\t\u008d\4\u008e\t\u008e\4\u008f\t\u008f")
        buf.write(u"\4\u0090\t\u0090\4\u0091\t\u0091\4\u0092\t\u0092\4\u0093")
        buf.write(u"\t\u0093\4\u0094\t\u0094\4\u0095\t\u0095\4\u0096\t\u0096")
        buf.write(u"\4\u0097\t\u0097\4\u0098\t\u0098\4\u0099\t\u0099\4\u009a")
        buf.write(u"\t\u009a\4\u009b\t\u009b\4\u009c\t\u009c\4\u009d\t\u009d")
        buf.write(u"\4\u009e\t\u009e\4\u009f\t\u009f\4\u00a0\t\u00a0\4\u00a1")
        buf.write(u"\t\u00a1\4\u00a2\t\u00a2\4\u00a3\t\u00a3\4\u00a4\t\u00a4")
        buf.write(u"\4\u00a5\t\u00a5\4\u00a6\t\u00a6\4\u00a7\t\u00a7\4\u00a8")
        buf.write(u"\t\u00a8\4\u00a9\t\u00a9\4\u00aa\t\u00aa\4\u00ab\t\u00ab")
        buf.write(u"\4\u00ac\t\u00ac\4\u00ad\t\u00ad\4\u00ae\t\u00ae\4\u00af")
        buf.write(u"\t\u00af\4\u00b0\t\u00b0\4\u00b1\t\u00b1\4\u00b2\t\u00b2")
        buf.write(u"\4\u00b3\t\u00b3\4\u00b4\t\u00b4\4\u00b5\t\u00b5\4\u00b6")
        buf.write(u"\t\u00b6\4\u00b7\t\u00b7\4\u00b8\t\u00b8\4\u00b9\t\u00b9")
        buf.write(u"\4\u00ba\t\u00ba\4\u00bb\t\u00bb\4\u00bc\t\u00bc\4\u00bd")
        buf.write(u"\t\u00bd\4\u00be\t\u00be\4\u00bf\t\u00bf\4\u00c0\t\u00c0")
        buf.write(u"\4\u00c1\t\u00c1\4\u00c2\t\u00c2\4\u00c3\t\u00c3\4\u00c4")
        buf.write(u"\t\u00c4\4\u00c5\t\u00c5\4\u00c6\t\u00c6\4\u00c7\t\u00c7")
        buf.write(u"\4\u00c8\t\u00c8\4\u00c9\t\u00c9\4\u00ca\t\u00ca\4\u00cb")
        buf.write(u"\t\u00cb\4\u00cc\t\u00cc\4\u00cd\t\u00cd\4\u00ce\t\u00ce")
        buf.write(u"\4\u00cf\t\u00cf\4\u00d0\t\u00d0\4\u00d1\t\u00d1\4\u00d2")
        buf.write(u"\t\u00d2\4\u00d3\t\u00d3\4\u00d4\t\u00d4\4\u00d5\t\u00d5")
        buf.write(u"\4\u00d6\t\u00d6\4\u00d7\t\u00d7\4\u00d8\t\u00d8\4\u00d9")
        buf.write(u"\t\u00d9\4\u00da\t\u00da\4\u00db\t\u00db\4\u00dc\t\u00dc")
        buf.write(u"\4\u00dd\t\u00dd\4\u00de\t\u00de\4\u00df\t\u00df\4\u00e0")
        buf.write(u"\t\u00e0\4\u00e1\t\u00e1\4\u00e2\t\u00e2\4\u00e3\t\u00e3")
        buf.write(u"\4\u00e4\t\u00e4\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u01d0")
        buf.write(u"\n\2\3\2\3\2\5\2\u01d4\n\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write(u"\5\3\5\3\5\3\5\3\5\3\6\5\6\u01ef\n\6\3\6\3\6\3\6\3\6")
        buf.write(u"\3\6\5\6\u01f6\n\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u01fe")
        buf.write(u"\n\6\5\6\u0200\n\6\3\6\3\6\3\7\5\7\u0205\n\7\3\7\3\7")
        buf.write(u"\3\7\3\7\3\7\3\7\5\7\u020d\n\7\3\7\3\7\5\7\u0211\n\7")
        buf.write(u"\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u021b\n\b\3\b\3")
        buf.write(u"\b\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u0225\n\t\f\t\16\t\u0228")
        buf.write(u"\13\t\3\n\3\n\3\n\5\n\u022d\n\n\3\n\5\n\u0230\n\n\3\13")
        buf.write(u"\5\13\u0233\n\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5")
        buf.write(u"\13\u023c\n\13\3\13\3\13\3\f\3\f\3\f\3\f\5\f\u0244\n")
        buf.write(u"\f\3\f\3\f\3\r\5\r\u0249\n\r\3\r\3\r\3\r\3\r\5\r\u024f")
        buf.write(u"\n\r\3\r\3\r\3\16\3\16\3\16\3\16\5\16\u0257\n\16\3\16")
        buf.write(u"\3\16\3\17\5\17\u025c\n\17\3\17\3\17\3\17\3\17\5\17\u0262")
        buf.write(u"\n\17\3\17\3\17\3\20\5\20\u0267\n\20\3\20\3\20\3\20\3")
        buf.write(u"\20\3\20\3\20\3\20\5\20\u0270\n\20\3\20\3\20\3\20\5\20")
        buf.write(u"\u0275\n\20\3\20\3\20\3\21\5\21\u027a\n\21\3\21\3\21")
        buf.write(u"\3\21\3\21\3\21\3\21\3\21\5\21\u0283\n\21\3\21\3\21\3")
        buf.write(u"\21\5\21\u0288\n\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write(u"\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u029a")
        buf.write(u"\n\23\f\23\16\23\u029d\13\23\3\24\3\24\5\24\u02a1\n\24")
        buf.write(u"\3\24\3\24\3\24\3\24\5\24\u02a7\n\24\3\24\3\24\3\24\3")
        buf.write(u"\25\5\25\u02ad\n\25\3\25\3\25\3\25\3\25\5\25\u02b3\n")
        buf.write(u"\25\3\25\3\25\3\25\5\25\u02b8\n\25\3\25\3\25\3\26\5\26")
        buf.write(u"\u02bd\n\26\3\26\5\26\u02c0\n\26\3\26\3\26\3\26\3\26")
        buf.write(u"\5\26\u02c6\n\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3")
        buf.write(u"\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write(u"\3\27\3\27\3\27\5\27\u02dd\n\27\3\30\3\30\3\30\3\31\3")
        buf.write(u"\31\3\31\3\31\3\31\5\31\u02e7\n\31\3\31\3\31\3\31\5\31")
        buf.write(u"\u02ec\n\31\3\32\3\32\3\32\3\32\3\32\5\32\u02f3\n\32")
        buf.write(u"\5\32\u02f5\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write(u"\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write(u"\3\33\3\33\3\33\5\33\u030c\n\33\3\34\3\34\3\34\3\34\3")
        buf.write(u"\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write(u"\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write(u"\35\3\35\3\35\5\35\u032a\n\35\3\36\3\36\3\36\3\36\3\36")
        buf.write(u"\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3")
        buf.write(u" \3 \3 \3 \5 \u0341\n \5 \u0343\n \3 \3 \3!\3!\3!\3!")
        buf.write(u"\5!\u034b\n!\3!\3!\3!\3!\3!\5!\u0352\n!\5!\u0354\n!\3")
        buf.write(u"\"\3\"\3\"\3\"\3\"\3\"\5\"\u035c\n\"\3\"\3\"\3\"\3\"")
        buf.write(u"\3\"\3#\3#\3#\5#\u0366\n#\3#\3#\3#\3#\3#\3#\3#\3$\3$")
        buf.write(u"\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\5%\u037b\n%\3%\3%\5%\u037f")
        buf.write(u"\n%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\7")
        buf.write(u"&\u0391\n&\f&\16&\u0394\13&\3\'\3\'\3\'\3\'\3(\3(\3(")
        buf.write(u"\3(\3(\3(\5(\u03a0\n(\3(\3(\5(\u03a4\n(\3(\3(\3(\3(\3")
        buf.write(u"(\3(\5(\u03ac\n(\3(\5(\u03af\n(\3(\3(\3(\5(\u03b4\n(")
        buf.write(u"\3(\5(\u03b7\n(\3)\3)\3)\3)\3)\3)\5)\u03bf\n)\3)\3)\3")
        buf.write(u")\3)\3)\3)\3)\3)\3)\5)\u03ca\n)\3)\3)\5)\u03ce\n)\3*")
        buf.write(u"\3*\3*\3+\3+\5+\u03d5\n+\3+\3+\3,\3,\3,\5,\u03dc\n,\3")
        buf.write(u",\3,\3-\3-\3-\3-\3-\5-\u03e5\n-\3.\3.\3.\3.\3.\7.\u03ec")
        buf.write(u"\n.\f.\16.\u03ef\13.\3/\3/\3/\3/\3/\3/\5/\u03f7\n/\3")
        buf.write(u"\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write(u"\60\3\60\3\60\5\60\u0411\n\60\3\60\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write(u"\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write(u"\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write(u"\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write(u"\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write(u"\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\3\60\3\60\3\60\7\60\u0485\n\60\f\60\16\60\u0488")
        buf.write(u"\13\60\3\61\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\63\3")
        buf.write(u"\63\3\63\7\63\u0495\n\63\f\63\16\63\u0498\13\63\3\64")
        buf.write(u"\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u04a3\n")
        buf.write(u"\64\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\5\66\u04ad")
        buf.write(u"\n\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write(u"\67\38\38\38\38\38\38\38\38\38\38\38\38\38\39\39\39\3")
        buf.write(u"9\39\39\59\u04cc\n9\39\39\39\39\39\39\39\39\39\39\39")
        buf.write(u"\59\u04d9\n9\39\39\39\39\59\u04df\n9\39\39\39\39\39\3")
        buf.write(u"9\39\59\u04e8\n9\39\39\39\39\39\59\u04ef\n9\39\39\39")
        buf.write(u"\39\39\39\59\u04f7\n9\59\u04f9\n9\3:\3:\5:\u04fd\n:\3")
        buf.write(u":\3:\3:\3:\3:\3:\3:\5:\u0506\n:\3:\3:\3;\3;\3;\3;\3;")
        buf.write(u"\3;\3;\3;\3;\3;\5;\u0514\n;\3<\3<\3<\3<\3<\5<\u051b\n")
        buf.write(u"<\3<\3<\3<\3<\3<\5<\u0522\n<\3<\3<\5<\u0526\n<\3=\3=")
        buf.write(u"\3=\3=\3=\3>\3>\3>\3>\3>\5>\u0532\n>\3>\3>\3>\7>\u0537")
        buf.write(u"\n>\f>\16>\u053a\13>\3?\3?\3?\3?\5?\u0540\n?\3@\3@\3")
        buf.write(u"@\3@\3@\3A\3A\3A\3A\3A\3A\5A\u054d\nA\3B\3B\3B\3B\3B")
        buf.write(u"\3C\3C\3D\5D\u0557\nD\3D\3D\3D\3E\3E\3E\3E\7E\u0560\n")
        buf.write(u"E\fE\16E\u0563\13E\3F\3F\3F\7F\u0568\nF\fF\16F\u056b")
        buf.write(u"\13F\3F\3F\3F\3F\3F\5F\u0572\nF\3G\3G\3H\3H\5H\u0578")
        buf.write(u"\nH\3I\3I\3I\3I\7I\u057e\nI\fI\16I\u0581\13I\3J\3J\3")
        buf.write(u"J\3J\7J\u0587\nJ\fJ\16J\u058a\13J\3K\3K\3K\7K\u058f\n")
        buf.write(u"K\fK\16K\u0592\13K\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\5L\u059e")
        buf.write(u"\nL\3M\5M\u05a1\nM\3M\3M\5M\u05a5\nM\3M\3M\3N\5N\u05aa")
        buf.write(u"\nN\3N\3N\5N\u05ae\nN\3N\3N\3O\3O\3O\7O\u05b5\nO\fO\16")
        buf.write(u"O\u05b8\13O\3P\3P\3P\3P\3P\3P\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3")
        buf.write(u"Q\3Q\3Q\3Q\3Q\5Q\u05cc\nQ\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\7Q")
        buf.write(u"\u05d6\nQ\fQ\16Q\u05d9\13Q\3R\3R\5R\u05dd\nR\3S\3S\3")
        buf.write(u"S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\5S\u05ee\nS\3T")
        buf.write(u"\3T\3U\5U\u05f3\nU\3U\3U\3V\3V\3W\3W\3W\5W\u05fc\nW\3")
        buf.write(u"X\3X\3X\7X\u0601\nX\fX\16X\u0604\13X\3Y\3Y\5Y\u0608\n")
        buf.write(u"Y\3Z\3Z\3Z\5Z\u060d\nZ\3[\3[\3\\\3\\\3]\3]\3^\3^\3_\3")
        buf.write(u"_\3_\7_\u061a\n_\f_\16_\u061d\13_\3`\3`\5`\u0621\n`\3")
        buf.write(u"`\5`\u0624\n`\3a\3a\5a\u0628\na\3b\3b\3b\5b\u062d\nb")
        buf.write(u"\3c\3c\3c\3d\3d\5d\u0634\nd\3e\3e\3e\3e\3e\3e\3e\3e\3")
        buf.write(u"e\7e\u063f\ne\fe\16e\u0642\13e\3f\3f\3f\3f\7f\u0648\n")
        buf.write(u"f\ff\16f\u064b\13f\3g\3g\3g\3g\3g\5g\u0652\ng\3h\3h\3")
        buf.write(u"h\3h\7h\u0658\nh\fh\16h\u065b\13h\3i\3i\3i\5i\u0660\n")
        buf.write(u"i\3j\3j\3j\3j\3j\3j\3j\3j\3j\3j\5j\u066c\nj\3k\3k\5k")
        buf.write(u"\u0670\nk\3l\3l\3l\3l\3l\3l\7l\u0678\nl\fl\16l\u067b")
        buf.write(u"\13l\3m\3m\5m\u067f\nm\3n\3n\3n\3n\5n\u0685\nn\3n\3n")
        buf.write(u"\3n\7n\u068a\nn\fn\16n\u068d\13n\3n\3n\5n\u0691\nn\3")
        buf.write(u"o\3o\3o\7o\u0696\no\fo\16o\u0699\13o\3p\3p\3p\7p\u069e")
        buf.write(u"\np\fp\16p\u06a1\13p\3q\3q\3q\3q\5q\u06a7\nq\3r\3r\3")
        buf.write(u"s\3s\3s\3s\7s\u06af\ns\fs\16s\u06b2\13s\3t\3t\3t\3t\3")
        buf.write(u"t\3t\3t\3t\3t\3t\5t\u06be\nt\3u\3u\5u\u06c2\nu\3u\5u")
        buf.write(u"\u06c5\nu\3v\3v\5v\u06c9\nv\3v\5v\u06cc\nv\3w\3w\3w\3")
        buf.write(u"w\7w\u06d2\nw\fw\16w\u06d5\13w\3x\3x\3x\3x\7x\u06db\n")
        buf.write(u"x\fx\16x\u06de\13x\3y\3y\3y\3y\7y\u06e4\ny\fy\16y\u06e7")
        buf.write(u"\13y\3z\3z\3z\3z\7z\u06ed\nz\fz\16z\u06f0\13z\3{\3{\3")
        buf.write(u"{\3{\3{\3{\3{\3{\3{\3{\3{\3{\3{\3{\5{\u0700\n{\3|\3|")
        buf.write(u"\3|\3|\3|\3|\3|\3|\3|\3|\3|\3|\3|\3|\3|\5|\u0711\n|\3")
        buf.write(u"}\3}\3}\7}\u0716\n}\f}\16}\u0719\13}\3~\3~\3~\3~\5~\u071f")
        buf.write(u"\n~\3\177\3\177\3\u0080\3\u0080\3\u0080\3\u0080\3\u0081")
        buf.write(u"\3\u0081\5\u0081\u0729\n\u0081\3\u0082\3\u0082\3\u0082")
        buf.write(u"\3\u0082\3\u0082\5\u0082\u0730\n\u0082\3\u0083\5\u0083")
        buf.write(u"\u0733\n\u0083\3\u0083\3\u0083\5\u0083\u0737\n\u0083")
        buf.write(u"\3\u0083\3\u0083\3\u0084\5\u0084\u073c\n\u0084\3\u0084")
        buf.write(u"\3\u0084\5\u0084\u0740\n\u0084\3\u0084\3\u0084\3\u0085")
        buf.write(u"\3\u0085\3\u0085\3\u0085\3\u0085\7\u0085\u0749\n\u0085")
        buf.write(u"\f\u0085\16\u0085\u074c\13\u0085\5\u0085\u074e\n\u0085")
        buf.write(u"\3\u0086\3\u0086\3\u0086\7\u0086\u0753\n\u0086\f\u0086")
        buf.write(u"\16\u0086\u0756\13\u0086\3\u0087\3\u0087\3\u0087\3\u0087")
        buf.write(u"\3\u0088\3\u0088\3\u0088\3\u0088\3\u0088\3\u0088\3\u0088")
        buf.write(u"\3\u0088\3\u0088\5\u0088\u0765\n\u0088\3\u0089\3\u0089")
        buf.write(u"\3\u0089\3\u0089\3\u008a\3\u008a\3\u008a\3\u008a\3\u008a")
        buf.write(u"\7\u008a\u0770\n\u008a\f\u008a\16\u008a\u0773\13\u008a")
        buf.write(u"\3\u008b\3\u008b\3\u008b\3\u008b\5\u008b\u0779\n\u008b")
        buf.write(u"\3\u008c\3\u008c\3\u008c\3\u008c\3\u008c\3\u008d\3\u008d")
        buf.write(u"\3\u008d\3\u008d\3\u008d\3\u008e\3\u008e\3\u008e\7\u008e")
        buf.write(u"\u0788\n\u008e\f\u008e\16\u008e\u078b\13\u008e\3\u008f")
        buf.write(u"\3\u008f\3\u008f\7\u008f\u0790\n\u008f\f\u008f\16\u008f")
        buf.write(u"\u0793\13\u008f\3\u008f\5\u008f\u0796\n\u008f\3\u0090")
        buf.write(u"\3\u0090\3\u0090\3\u0090\3\u0090\3\u0090\5\u0090\u079e")
        buf.write(u"\n\u0090\3\u0091\3\u0091\3\u0092\3\u0092\3\u0092\3\u0093")
        buf.write(u"\3\u0093\3\u0093\3\u0094\3\u0094\3\u0094\3\u0095\3\u0095")
        buf.write(u"\3\u0095\3\u0096\3\u0096\3\u0096\3\u0097\3\u0097\3\u0098")
        buf.write(u"\3\u0098\3\u0099\3\u0099\3\u009a\3\u009a\3\u009b\3\u009b")
        buf.write(u"\3\u009c\3\u009c\3\u009d\3\u009d\3\u009e\3\u009e\3\u009e")
        buf.write(u"\3\u009e\3\u009e\3\u009e\3\u009e\5\u009e\u07c6\n\u009e")
        buf.write(u"\3\u009f\3\u009f\3\u009f\3\u009f\3\u009f\7\u009f\u07cd")
        buf.write(u"\n\u009f\f\u009f\16\u009f\u07d0\13\u009f\3\u00a0\3\u00a0")
        buf.write(u"\3\u00a0\3\u00a0\3\u00a0\3\u00a0\3\u00a0\5\u00a0\u07d9")
        buf.write(u"\n\u00a0\3\u00a1\3\u00a1\3\u00a2\3\u00a2\3\u00a2\3\u00a3")
        buf.write(u"\3\u00a3\3\u00a3\3\u00a3\3\u00a3\5\u00a3\u07e5\n\u00a3")
        buf.write(u"\3\u00a4\3\u00a4\3\u00a4\5\u00a4\u07ea\n\u00a4\3\u00a4")
        buf.write(u"\3\u00a4\3\u00a5\3\u00a5\3\u00a5\3\u00a5\3\u00a5\3\u00a5")
        buf.write(u"\7\u00a5\u07f4\n\u00a5\f\u00a5\16\u00a5\u07f7\13\u00a5")
        buf.write(u"\3\u00a6\3\u00a6\3\u00a6\3\u00a6\3\u00a7\3\u00a7\3\u00a7")
        buf.write(u"\3\u00a7\3\u00a8\3\u00a8\3\u00a9\3\u00a9\3\u00a9\3\u00a9")
        buf.write(u"\3\u00a9\5\u00a9\u0808\n\u00a9\3\u00aa\3\u00aa\3\u00ab")
        buf.write(u"\3\u00ab\3\u00ab\5\u00ab\u080f\n\u00ab\3\u00ac\3\u00ac")
        buf.write(u"\3\u00ac\3\u00ac\3\u00ac\7\u00ac\u0816\n\u00ac\f\u00ac")
        buf.write(u"\16\u00ac\u0819\13\u00ac\3\u00ad\3\u00ad\3\u00ad\3\u00ad")
        buf.write(u"\3\u00ad\5\u00ad\u0820\n\u00ad\3\u00ae\3\u00ae\3\u00af")
        buf.write(u"\3\u00af\3\u00af\3\u00af\3\u00af\3\u00af\5\u00af\u082a")
        buf.write(u"\n\u00af\3\u00b0\3\u00b0\3\u00b0\5\u00b0\u082f\n\u00b0")
        buf.write(u"\3\u00b0\3\u00b0\3\u00b1\3\u00b1\3\u00b1\3\u00b1\3\u00b1")
        buf.write(u"\3\u00b1\5\u00b1\u0839\n\u00b1\3\u00b2\3\u00b2\3\u00b2")
        buf.write(u"\3\u00b2\3\u00b2\3\u00b2\7\u00b2\u0841\n\u00b2\f\u00b2")
        buf.write(u"\16\u00b2\u0844\13\u00b2\3\u00b3\3\u00b3\3\u00b3\3\u00b3")
        buf.write(u"\3\u00b3\3\u00b3\3\u00b3\3\u00b3\3\u00b3\3\u00b3\3\u00b3")
        buf.write(u"\7\u00b3\u0851\n\u00b3\f\u00b3\16\u00b3\u0854\13\u00b3")
        buf.write(u"\3\u00b4\3\u00b4\3\u00b4\3\u00b4\3\u00b5\3\u00b5\3\u00b5")
        buf.write(u"\5\u00b5\u085d\n\u00b5\3\u00b5\3\u00b5\3\u00b5\7\u00b5")
        buf.write(u"\u0862\n\u00b5\f\u00b5\16\u00b5\u0865\13\u00b5\3\u00b6")
        buf.write(u"\3\u00b6\3\u00b6\3\u00b6\3\u00b6\5\u00b6\u086c\n\u00b6")
        buf.write(u"\3\u00b7\3\u00b7\3\u00b8\3\u00b8\3\u00b8\3\u00b8\3\u00b8")
        buf.write(u"\3\u00b8\3\u00b8\5\u00b8\u0877\n\u00b8\3\u00b9\3\u00b9")
        buf.write(u"\3\u00b9\3\u00b9\3\u00b9\7\u00b9\u087e\n\u00b9\f\u00b9")
        buf.write(u"\16\u00b9\u0881\13\u00b9\3\u00ba\3\u00ba\3\u00ba\3\u00ba")
        buf.write(u"\3\u00ba\5\u00ba\u0888\n\u00ba\3\u00bb\3\u00bb\3\u00bc")
        buf.write(u"\3\u00bc\3\u00bc\3\u00bd\3\u00bd\3\u00bd\5\u00bd\u0892")
        buf.write(u"\n\u00bd\3\u00be\3\u00be\3\u00be\5\u00be\u0897\n\u00be")
        buf.write(u"\3\u00be\3\u00be\3\u00bf\3\u00bf\3\u00bf\3\u00bf\3\u00bf")
        buf.write(u"\3\u00bf\7\u00bf\u08a1\n\u00bf\f\u00bf\16\u00bf\u08a4")
        buf.write(u"\13\u00bf\3\u00c0\3\u00c0\3\u00c0\3\u00c0\3\u00c1\3\u00c1")
        buf.write(u"\3\u00c1\3\u00c1\3\u00c2\3\u00c2\3\u00c2\3\u00c2\3\u00c2")
        buf.write(u"\3\u00c2\7\u00c2\u08b4\n\u00c2\f\u00c2\16\u00c2\u08b7")
        buf.write(u"\13\u00c2\3\u00c3\3\u00c3\3\u00c3\3\u00c3\3\u00c3\7\u00c3")
        buf.write(u"\u08be\n\u00c3\f\u00c3\16\u00c3\u08c1\13\u00c3\3\u00c4")
        buf.write(u"\3\u00c4\3\u00c4\3\u00c4\3\u00c4\5\u00c4\u08c8\n\u00c4")
        buf.write(u"\3\u00c5\3\u00c5\3\u00c6\3\u00c6\3\u00c6\3\u00c6\3\u00c6")
        buf.write(u"\3\u00c6\3\u00c6\5\u00c6\u08d3\n\u00c6\3\u00c7\3\u00c7")
        buf.write(u"\3\u00c7\3\u00c7\3\u00c7\7\u00c7\u08da\n\u00c7\f\u00c7")
        buf.write(u"\16\u00c7\u08dd\13\u00c7\3\u00c8\3\u00c8\3\u00c8\3\u00c8")
        buf.write(u"\3\u00c8\5\u00c8\u08e4\n\u00c8\3\u00c9\3\u00c9\3\u00ca")
        buf.write(u"\3\u00ca\3\u00ca\3\u00cb\3\u00cb\3\u00cb\5\u00cb\u08ee")
        buf.write(u"\n\u00cb\3\u00cc\3\u00cc\3\u00cc\5\u00cc\u08f3\n\u00cc")
        buf.write(u"\3\u00cc\3\u00cc\3\u00cd\3\u00cd\3\u00cd\3\u00cd\3\u00cd")
        buf.write(u"\3\u00cd\7\u00cd\u08fd\n\u00cd\f\u00cd\16\u00cd\u0900")
        buf.write(u"\13\u00cd\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00cf\3\u00cf")
        buf.write(u"\3\u00cf\3\u00cf\3\u00d0\3\u00d0\3\u00d0\5\u00d0\u090d")
        buf.write(u"\n\u00d0\3\u00d0\3\u00d0\3\u00d0\7\u00d0\u0912\n\u00d0")
        buf.write(u"\f\u00d0\16\u00d0\u0915\13\u00d0\3\u00d1\3\u00d1\3\u00d1")
        buf.write(u"\3\u00d1\3\u00d1\5\u00d1\u091c\n\u00d1\3\u00d2\3\u00d2")
        buf.write(u"\3\u00d3\3\u00d3\5\u00d3\u0922\n\u00d3\3\u00d4\3\u00d4")
        buf.write(u"\3\u00d4\5\u00d4\u0927\n\u00d4\3\u00d4\3\u00d4\5\u00d4")
        buf.write(u"\u092b\n\u00d4\3\u00d5\3\u00d5\5\u00d5\u092f\n\u00d5")
        buf.write(u"\3\u00d5\3\u00d5\3\u00d6\3\u00d6\3\u00d6\5\u00d6\u0936")
        buf.write(u"\n\u00d6\3\u00d7\3\u00d7\3\u00d7\3\u00d7\3\u00d8\3\u00d8")
        buf.write(u"\3\u00d8\7\u00d8\u093f\n\u00d8\f\u00d8\16\u00d8\u0942")
        buf.write(u"\13\u00d8\3\u00d8\3\u00d8\3\u00d8\3\u00d9\3\u00d9\3\u00d9")
        buf.write(u"\7\u00d9\u094a\n\u00d9\f\u00d9\16\u00d9\u094d\13\u00d9")
        buf.write(u"\3\u00d9\3\u00d9\3\u00da\3\u00da\3\u00da\3\u00da\3\u00da")
        buf.write(u"\3\u00db\3\u00db\3\u00db\7\u00db\u0959\n\u00db\f\u00db")
        buf.write(u"\16\u00db\u095c\13\u00db\3\u00dc\3\u00dc\7\u00dc\u0960")
        buf.write(u"\n\u00dc\f\u00dc\16\u00dc\u0963\13\u00dc\3\u00dd\3\u00dd")
        buf.write(u"\3\u00dd\3\u00dd\3\u00de\3\u00de\3\u00de\3\u00df\3\u00df")
        buf.write(u"\5\u00df\u096e\n\u00df\3\u00e0\3\u00e0\3\u00e0\5\u00e0")
        buf.write(u"\u0973\n\u00e0\3\u00e1\3\u00e1\3\u00e1\3\u00e1\3\u00e1")
        buf.write(u"\5\u00e1\u097a\n\u00e1\3\u00e2\6\u00e2\u097d\n\u00e2")
        buf.write(u"\r\u00e2\16\u00e2\u097e\3\u00e3\3\u00e3\3\u00e3\3\u00e3")
        buf.write(u"\5\u00e3\u0985\n\u00e3\3\u00e3\5\u00e3\u0988\n\u00e3")
        buf.write(u"\3\u00e4\6\u00e4\u098b\n\u00e4\r\u00e4\16\u00e4\u098c")
        buf.write(u"\3\u00e4\2\31\20$JZ^dz\u00a0\u00c8\u0112\u013c\u0148")
        buf.write(u"\u0156\u0162\u0164\u0168\u0170\u017c\u0182\u0184\u018c")
        buf.write(u"\u0198\u019e\u00e5\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write(u"\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjl")
        buf.write(u"nprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c\u008e")
        buf.write(u"\u0090\u0092\u0094\u0096\u0098\u009a\u009c\u009e\u00a0")
        buf.write(u"\u00a2\u00a4\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0\u00b2")
        buf.write(u"\u00b4\u00b6\u00b8\u00ba\u00bc\u00be\u00c0\u00c2\u00c4")
        buf.write(u"\u00c6\u00c8\u00ca\u00cc\u00ce\u00d0\u00d2\u00d4\u00d6")
        buf.write(u"\u00d8\u00da\u00dc\u00de\u00e0\u00e2\u00e4\u00e6\u00e8")
        buf.write(u"\u00ea\u00ec\u00ee\u00f0\u00f2\u00f4\u00f6\u00f8\u00fa")
        buf.write(u"\u00fc\u00fe\u0100\u0102\u0104\u0106\u0108\u010a\u010c")
        buf.write(u"\u010e\u0110\u0112\u0114\u0116\u0118\u011a\u011c\u011e")
        buf.write(u"\u0120\u0122\u0124\u0126\u0128\u012a\u012c\u012e\u0130")
        buf.write(u"\u0132\u0134\u0136\u0138\u013a\u013c\u013e\u0140\u0142")
        buf.write(u"\u0144\u0146\u0148\u014a\u014c\u014e\u0150\u0152\u0154")
        buf.write(u"\u0156\u0158\u015a\u015c\u015e\u0160\u0162\u0164\u0166")
        buf.write(u"\u0168\u016a\u016c\u016e\u0170\u0172\u0174\u0176\u0178")
        buf.write(u"\u017a\u017c\u017e\u0180\u0182\u0184\u0186\u0188\u018a")
        buf.write(u"\u018c\u018e\u0190\u0192\u0194\u0196\u0198\u019a\u019c")
        buf.write(u"\u019e\u01a0\u01a2\u01a4\u01a6\u01a8\u01aa\u01ac\u01ae")
        buf.write(u"\u01b0\u01b2\u01b4\u01b6\u01b8\u01ba\u01bc\u01be\u01c0")
        buf.write(u"\u01c2\u01c4\u01c6\2\r\3\2\36\37\4\2\u008e\u008e\u00a2")
        buf.write(u"\u00a2\4\2\u008a\u008a\u0092\u0092\4\2HHYY\4\2\7\f\60")
        buf.write(u"\u009b\4\2##tt\f\2\609??wwzz\u0084\u0084\u008a\u008a")
        buf.write(u"\u0091\u0091\u009b\u009b\u00a0\u00a2\u00a4\u00a4\n\2")
        buf.write(u"\609??wwzz\u0084\u0084\u0091\u0092\u009b\u009b\u00a0")
        buf.write(u"\u00a2\13\2\609??wwzz\u0084\u0084\u008a\u008a\u0091\u0091")
        buf.write(u"\u009b\u009b\u00a0\u00a4\13\2\609??wwzz\u0084\u0084\u008a")
        buf.write(u"\u008a\u0091\u0091\u009b\u009b\u00a0\u00a2\5\2\26\27")
        buf.write(u"$$&&\2\u0a1a\2\u01c8\3\2\2\2\4\u01d9\3\2\2\2\6\u01e2")
        buf.write(u"\3\2\2\2\b\u01e8\3\2\2\2\n\u01ee\3\2\2\2\f\u0204\3\2")
        buf.write(u"\2\2\16\u0214\3\2\2\2\20\u021e\3\2\2\2\22\u022f\3\2\2")
        buf.write(u"\2\24\u0232\3\2\2\2\26\u023f\3\2\2\2\30\u0248\3\2\2\2")
        buf.write(u"\32\u0252\3\2\2\2\34\u025b\3\2\2\2\36\u0266\3\2\2\2 ")
        buf.write(u"\u0279\3\2\2\2\"\u028b\3\2\2\2$\u0291\3\2\2\2&\u029e")
        buf.write(u"\3\2\2\2(\u02ac\3\2\2\2*\u02bc\3\2\2\2,\u02cc\3\2\2\2")
        buf.write(u".\u02de\3\2\2\2\60\u02e1\3\2\2\2\62\u02f4\3\2\2\2\64")
        buf.write(u"\u030b\3\2\2\2\66\u030d\3\2\2\28\u0329\3\2\2\2:\u032b")
        buf.write(u"\3\2\2\2<\u0331\3\2\2\2>\u0337\3\2\2\2@\u0353\3\2\2\2")
        buf.write(u"B\u0355\3\2\2\2D\u0362\3\2\2\2F\u036e\3\2\2\2H\u0374")
        buf.write(u"\3\2\2\2J\u0380\3\2\2\2L\u0395\3\2\2\2N\u0399\3\2\2\2")
        buf.write(u"P\u03cd\3\2\2\2R\u03cf\3\2\2\2T\u03d2\3\2\2\2V\u03d8")
        buf.write(u"\3\2\2\2X\u03e4\3\2\2\2Z\u03e6\3\2\2\2\\\u03f6\3\2\2")
        buf.write(u"\2^\u0410\3\2\2\2`\u0489\3\2\2\2b\u048d\3\2\2\2d\u048f")
        buf.write(u"\3\2\2\2f\u04a2\3\2\2\2h\u04a4\3\2\2\2j\u04a9\3\2\2\2")
        buf.write(u"l\u04b0\3\2\2\2n\u04b8\3\2\2\2p\u04f8\3\2\2\2r\u04fa")
        buf.write(u"\3\2\2\2t\u0513\3\2\2\2v\u0525\3\2\2\2x\u0527\3\2\2\2")
        buf.write(u"z\u0531\3\2\2\2|\u053b\3\2\2\2~\u0541\3\2\2\2\u0080\u054c")
        buf.write(u"\3\2\2\2\u0082\u054e\3\2\2\2\u0084\u0553\3\2\2\2\u0086")
        buf.write(u"\u0556\3\2\2\2\u0088\u055b\3\2\2\2\u008a\u0569\3\2\2")
        buf.write(u"\2\u008c\u0573\3\2\2\2\u008e\u0577\3\2\2\2\u0090\u0579")
        buf.write(u"\3\2\2\2\u0092\u0582\3\2\2\2\u0094\u058b\3\2\2\2\u0096")
        buf.write(u"\u059d\3\2\2\2\u0098\u05a0\3\2\2\2\u009a\u05a9\3\2\2")
        buf.write(u"\2\u009c\u05b1\3\2\2\2\u009e\u05b9\3\2\2\2\u00a0\u05cb")
        buf.write(u"\3\2\2\2\u00a2\u05dc\3\2\2\2\u00a4\u05ed\3\2\2\2\u00a6")
        buf.write(u"\u05ef\3\2\2\2\u00a8\u05f2\3\2\2\2\u00aa\u05f6\3\2\2")
        buf.write(u"\2\u00ac\u05fb\3\2\2\2\u00ae\u05fd\3\2\2\2\u00b0\u0607")
        buf.write(u"\3\2\2\2\u00b2\u060c\3\2\2\2\u00b4\u060e\3\2\2\2\u00b6")
        buf.write(u"\u0610\3\2\2\2\u00b8\u0612\3\2\2\2\u00ba\u0614\3\2\2")
        buf.write(u"\2\u00bc\u0616\3\2\2\2\u00be\u0623\3\2\2\2\u00c0\u0627")
        buf.write(u"\3\2\2\2\u00c2\u0629\3\2\2\2\u00c4\u062e\3\2\2\2\u00c6")
        buf.write(u"\u0633\3\2\2\2\u00c8\u0635\3\2\2\2\u00ca\u0643\3\2\2")
        buf.write(u"\2\u00cc\u0651\3\2\2\2\u00ce\u0653\3\2\2\2\u00d0\u065f")
        buf.write(u"\3\2\2\2\u00d2\u066b\3\2\2\2\u00d4\u066d\3\2\2\2\u00d6")
        buf.write(u"\u0671\3\2\2\2\u00d8\u067c\3\2\2\2\u00da\u0680\3\2\2")
        buf.write(u"\2\u00dc\u0692\3\2\2\2\u00de\u069a\3\2\2\2\u00e0\u06a6")
        buf.write(u"\3\2\2\2\u00e2\u06a8\3\2\2\2\u00e4\u06aa\3\2\2\2\u00e6")
        buf.write(u"\u06bd\3\2\2\2\u00e8\u06bf\3\2\2\2\u00ea\u06c6\3\2\2")
        buf.write(u"\2\u00ec\u06cd\3\2\2\2\u00ee\u06d6\3\2\2\2\u00f0\u06df")
        buf.write(u"\3\2\2\2\u00f2\u06e8\3\2\2\2\u00f4\u06ff\3\2\2\2\u00f6")
        buf.write(u"\u0710\3\2\2\2\u00f8\u0712\3\2\2\2\u00fa\u071e\3\2\2")
        buf.write(u"\2\u00fc\u0720\3\2\2\2\u00fe\u0722\3\2\2\2\u0100\u0728")
        buf.write(u"\3\2\2\2\u0102\u072f\3\2\2\2\u0104\u0732\3\2\2\2\u0106")
        buf.write(u"\u073b\3\2\2\2\u0108\u0743\3\2\2\2\u010a\u074f\3\2\2")
        buf.write(u"\2\u010c\u0757\3\2\2\2\u010e\u0764\3\2\2\2\u0110\u0766")
        buf.write(u"\3\2\2\2\u0112\u076a\3\2\2\2\u0114\u0778\3\2\2\2\u0116")
        buf.write(u"\u077a\3\2\2\2\u0118\u077f\3\2\2\2\u011a\u0784\3\2\2")
        buf.write(u"\2\u011c\u078c\3\2\2\2\u011e\u079d\3\2\2\2\u0120\u079f")
        buf.write(u"\3\2\2\2\u0122\u07a1\3\2\2\2\u0124\u07a4\3\2\2\2\u0126")
        buf.write(u"\u07a7\3\2\2\2\u0128\u07aa\3\2\2\2\u012a\u07ad\3\2\2")
        buf.write(u"\2\u012c\u07b0\3\2\2\2\u012e\u07b2\3\2\2\2\u0130\u07b4")
        buf.write(u"\3\2\2\2\u0132\u07b6\3\2\2\2\u0134\u07b8\3\2\2\2\u0136")
        buf.write(u"\u07ba\3\2\2\2\u0138\u07bc\3\2\2\2\u013a\u07c5\3\2\2")
        buf.write(u"\2\u013c\u07c7\3\2\2\2\u013e\u07d8\3\2\2\2\u0140\u07da")
        buf.write(u"\3\2\2\2\u0142\u07dc\3\2\2\2\u0144\u07e4\3\2\2\2\u0146")
        buf.write(u"\u07e6\3\2\2\2\u0148\u07ed\3\2\2\2\u014a\u07f8\3\2\2")
        buf.write(u"\2\u014c\u07fc\3\2\2\2\u014e\u0800\3\2\2\2\u0150\u0807")
        buf.write(u"\3\2\2\2\u0152\u0809\3\2\2\2\u0154\u080e\3\2\2\2\u0156")
        buf.write(u"\u0810\3\2\2\2\u0158\u081f\3\2\2\2\u015a\u0821\3\2\2")
        buf.write(u"\2\u015c\u0829\3\2\2\2\u015e\u082b\3\2\2\2\u0160\u0838")
        buf.write(u"\3\2\2\2\u0162\u083a\3\2\2\2\u0164\u0845\3\2\2\2\u0166")
        buf.write(u"\u0855\3\2\2\2\u0168\u085c\3\2\2\2\u016a\u086b\3\2\2")
        buf.write(u"\2\u016c\u086d\3\2\2\2\u016e\u0876\3\2\2\2\u0170\u0878")
        buf.write(u"\3\2\2\2\u0172\u0887\3\2\2\2\u0174\u0889\3\2\2\2\u0176")
        buf.write(u"\u088b\3\2\2\2\u0178\u0891\3\2\2\2\u017a\u0893\3\2\2")
        buf.write(u"\2\u017c\u089a\3\2\2\2\u017e\u08a5\3\2\2\2\u0180\u08a9")
        buf.write(u"\3\2\2\2\u0182\u08ad\3\2\2\2\u0184\u08b8\3\2\2\2\u0186")
        buf.write(u"\u08c7\3\2\2\2\u0188\u08c9\3\2\2\2\u018a\u08d2\3\2\2")
        buf.write(u"\2\u018c\u08d4\3\2\2\2\u018e\u08e3\3\2\2\2\u0190\u08e5")
        buf.write(u"\3\2\2\2\u0192\u08e7\3\2\2\2\u0194\u08ed\3\2\2\2\u0196")
        buf.write(u"\u08ef\3\2\2\2\u0198\u08f6\3\2\2\2\u019a\u0901\3\2\2")
        buf.write(u"\2\u019c\u0905\3\2\2\2\u019e\u090c\3\2\2\2\u01a0\u091b")
        buf.write(u"\3\2\2\2\u01a2\u091d\3\2\2\2\u01a4\u0921\3\2\2\2\u01a6")
        buf.write(u"\u092a\3\2\2\2\u01a8\u092c\3\2\2\2\u01aa\u0935\3\2\2")
        buf.write(u"\2\u01ac\u0937\3\2\2\2\u01ae\u093b\3\2\2\2\u01b0\u0946")
        buf.write(u"\3\2\2\2\u01b2\u0950\3\2\2\2\u01b4\u0955\3\2\2\2\u01b6")
        buf.write(u"\u095d\3\2\2\2\u01b8\u0964\3\2\2\2\u01ba\u0968\3\2\2")
        buf.write(u"\2\u01bc\u096d\3\2\2\2\u01be\u096f\3\2\2\2\u01c0\u0979")
        buf.write(u"\3\2\2\2\u01c2\u097c\3\2\2\2\u01c4\u0987\3\2\2\2\u01c6")
        buf.write(u"\u098a\3\2\2\2\u01c8\u01c9\7_\2\2\u01c9\u01ca\7Q\2\2")
        buf.write(u"\u01ca\u01cf\5\u00b8]\2\u01cb\u01cc\7\22\2\2\u01cc\u01cd")
        buf.write(u"\5\u00dep\2\u01cd\u01ce\7\23\2\2\u01ce\u01d0\3\2\2\2")
        buf.write(u"\u01cf\u01cb\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d3")
        buf.write(u"\3\2\2\2\u01d1\u01d2\7c\2\2\u01d2\u01d4\5\u00b8]\2\u01d3")
        buf.write(u"\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d5\3\2\2")
        buf.write(u"\2\u01d5\u01d6\7\26\2\2\u01d6\u01d7\5\u0092J\2\u01d7")
        buf.write(u"\u01d8\7\27\2\2\u01d8\3\3\2\2\2\u01d9\u01da\7_\2\2\u01da")
        buf.write(u"\u01db\5\u00b8]\2\u01db\u01dc\7\22\2\2\u01dc\u01dd\5")
        buf.write(u"\u00a4S\2\u01dd\u01de\7\23\2\2\u01de\u01df\7\26\2\2\u01df")
        buf.write(u"\u01e0\5\u0090I\2\u01e0\u01e1\7\27\2\2\u01e1\5\3\2\2")
        buf.write(u"\2\u01e2\u01e3\5\u00ba^\2\u01e3\u01e4\7\22\2\2\u01e4")
        buf.write(u"\u01e5\5z>\2\u01e5\u01e6\7\23\2\2\u01e6\u01e7\7\16\2")
        buf.write(u"\2\u01e7\7\3\2\2\2\u01e8\u01e9\5\u00ba^\2\u01e9\u01ea")
        buf.write(u"\7)\2\2\u01ea\u01eb\5^\60\2\u01eb\u01ec\7\16\2\2\u01ec")
        buf.write(u"\t\3\2\2\2\u01ed\u01ef\7\u008e\2\2\u01ee\u01ed\3\2\2")
        buf.write(u"\2\u01ee\u01ef\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f1")
        buf.write(u"\7J\2\2\u01f1\u01f2\5\u00b6\\\2\u01f2\u01f3\7\r\2\2\u01f3")
        buf.write(u"\u01f5\5\u00a0Q\2\u01f4\u01f6\5\u0096L\2\u01f5\u01f4")
        buf.write(u"\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01ff\3\2\2\2\u01f7")
        buf.write(u"\u01f8\7\u0097\2\2\u01f8\u01fd\7n\2\2\u01f9\u01fa\7\22")
        buf.write(u"\2\2\u01fa\u01fb\5\u00dco\2\u01fb\u01fc\7\23\2\2\u01fc")
        buf.write(u"\u01fe\3\2\2\2\u01fd\u01f9\3\2\2\2\u01fd\u01fe\3\2\2")
        buf.write(u"\2\u01fe\u0200\3\2\2\2\u01ff\u01f7\3\2\2\2\u01ff\u0200")
        buf.write(u"\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u0202\7\16\2\2\u0202")
        buf.write(u"\13\3\2\2\2\u0203\u0205\7\u008e\2\2\u0204\u0203\3\2\2")
        buf.write(u"\2\u0204\u0205\3\2\2\2\u0205\u0206\3\2\2\2\u0206\u0207")
        buf.write(u"\7Q\2\2\u0207\u020c\5\u00b8]\2\u0208\u0209\7\22\2\2\u0209")
        buf.write(u"\u020a\5\u00dep\2\u020a\u020b\7\23\2\2\u020b\u020d\3")
        buf.write(u"\2\2\2\u020c\u0208\3\2\2\2\u020c\u020d\3\2\2\2\u020d")
        buf.write(u"\u0210\3\2\2\2\u020e\u020f\7c\2\2\u020f\u0211\5\20\t")
        buf.write(u"\2\u0210\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u0212")
        buf.write(u"\3\2\2\2\u0212\u0213\5\22\n\2\u0213\r\3\2\2\2\u0214\u0215")
        buf.write(u"\7\u008c\2\2\u0215\u021a\5\u00b8]\2\u0216\u0217\7\22")
        buf.write(u"\2\2\u0217\u0218\5\u00dep\2\u0218\u0219\7\23\2\2\u0219")
        buf.write(u"\u021b\3\2\2\2\u021a\u0216\3\2\2\2\u021a\u021b\3\2\2")
        buf.write(u"\2\u021b\u021c\3\2\2\2\u021c\u021d\5\22\n\2\u021d\17")
        buf.write(u"\3\2\2\2\u021e\u021f\b\t\1\2\u021f\u0220\5\u00b8]\2\u0220")
        buf.write(u"\u0226\3\2\2\2\u0221\u0222\f\3\2\2\u0222\u0223\7\17\2")
        buf.write(u"\2\u0223\u0225\5\u00b8]\2\u0224\u0221\3\2\2\2\u0225\u0228")
        buf.write(u"\3\2\2\2\u0226\u0224\3\2\2\2\u0226\u0227\3\2\2\2\u0227")
        buf.write(u"\21\3\2\2\2\u0228\u0226\3\2\2\2\u0229\u0230\7\16\2\2")
        buf.write(u"\u022a\u022c\7\26\2\2\u022b\u022d\5\u00caf\2\u022c\u022b")
        buf.write(u"\3\2\2\2\u022c\u022d\3\2\2\2\u022d\u022e\3\2\2\2\u022e")
        buf.write(u"\u0230\7\27\2\2\u022f\u0229\3\2\2\2\u022f\u022a\3\2\2")
        buf.write(u"\2\u0230\23\3\2\2\2\u0231\u0233\5\u00a0Q\2\u0232\u0231")
        buf.write(u"\3\2\2\2\u0232\u0233\3\2\2\2\u0233\u0234\3\2\2\2\u0234")
        buf.write(u"\u0235\7~\2\2\u0235\u0236\5\u011e\u0090\2\u0236\u0237")
        buf.write(u"\7\22\2\2\u0237\u0238\5\u00c0a\2\u0238\u0239\7\23\2\2")
        buf.write(u"\u0239\u023b\7\26\2\2\u023a\u023c\5\u00ecw\2\u023b\u023a")
        buf.write(u"\3\2\2\2\u023b\u023c\3\2\2\2\u023c\u023d\3\2\2\2\u023d")
        buf.write(u"\u023e\7\27\2\2\u023e\25\3\2\2\2\u023f\u0240\7\u008b")
        buf.write(u"\2\2\u0240\u0241\5\u00b4[\2\u0241\u0243\7\26\2\2\u0242")
        buf.write(u"\u0244\5\u00ecw\2\u0243\u0242\3\2\2\2\u0243\u0244\3\2")
        buf.write(u"\2\2\u0244\u0245\3\2\2\2\u0245\u0246\7\27\2\2\u0246\27")
        buf.write(u"\3\2\2\2\u0247\u0249\7v\2\2\u0248\u0247\3\2\2\2\u0248")
        buf.write(u"\u0249\3\2\2\2\u0249\u024a\3\2\2\2\u024a\u024b\7\u008b")
        buf.write(u"\2\2\u024b\u024c\5\u00b4[\2\u024c\u024e\7\26\2\2\u024d")
        buf.write(u"\u024f\5\u00e4s\2\u024e\u024d\3\2\2\2\u024e\u024f\3\2")
        buf.write(u"\2\2\u024f\u0250\3\2\2\2\u0250\u0251\7\27\2\2\u0251\31")
        buf.write(u"\3\2\2\2\u0252\u0253\7j\2\2\u0253\u0254\5\u00b4[\2\u0254")
        buf.write(u"\u0256\7\26\2\2\u0255\u0257\5\u00ecw\2\u0256\u0255\3")
        buf.write(u"\2\2\2\u0256\u0257\3\2\2\2\u0257\u0258\3\2\2\2\u0258")
        buf.write(u"\u0259\7\27\2\2\u0259\33\3\2\2\2\u025a\u025c\7v\2\2\u025b")
        buf.write(u"\u025a\3\2\2\2\u025b\u025c\3\2\2\2\u025c\u025d\3\2\2")
        buf.write(u"\2\u025d\u025e\7j\2\2\u025e\u025f\5\u00b4[\2\u025f\u0261")
        buf.write(u"\7\26\2\2\u0260\u0262\5\u00e4s\2\u0261\u0260\3\2\2\2")
        buf.write(u"\u0261\u0262\3\2\2\2\u0262\u0263\3\2\2\2\u0263\u0264")
        buf.write(u"\7\27\2\2\u0264\35\3\2\2\2\u0265\u0267\7\u008e\2\2\u0266")
        buf.write(u"\u0265\3\2\2\2\u0266\u0267\3\2\2\2\u0267\u0268\3\2\2")
        buf.write(u"\2\u0268\u0269\7v\2\2\u0269\u026a\7\u0086\2\2\u026a\u026f")
        buf.write(u"\5\u00b8]\2\u026b\u026c\7\22\2\2\u026c\u026d\5\u00de")
        buf.write(u"p\2\u026d\u026e\7\23\2\2\u026e\u0270\3\2\2\2\u026f\u026b")
        buf.write(u"\3\2\2\2\u026f\u0270\3\2\2\2\u0270\u0271\3\2\2\2\u0271")
        buf.write(u"\u0272\7\26\2\2\u0272\u0274\5\"\22\2\u0273\u0275\5\u00ce")
        buf.write(u"h\2\u0274\u0273\3\2\2\2\u0274\u0275\3\2\2\2\u0275\u0276")
        buf.write(u"\3\2\2\2\u0276\u0277\7\27\2\2\u0277\37\3\2\2\2\u0278")
        buf.write(u"\u027a\7\u008e\2\2\u0279\u0278\3\2\2\2\u0279\u027a\3")
        buf.write(u"\2\2\2\u027a\u027b\3\2\2\2\u027b\u027c\7v\2\2\u027c\u027d")
        buf.write(u"\7Q\2\2\u027d\u0282\5\u00b8]\2\u027e\u027f\7\22\2\2\u027f")
        buf.write(u"\u0280\5\u00dep\2\u0280\u0281\7\23\2\2\u0281\u0283\3")
        buf.write(u"\2\2\2\u0282\u027e\3\2\2\2\u0282\u0283\3\2\2\2\u0283")
        buf.write(u"\u0284\3\2\2\2\u0284\u0285\7\26\2\2\u0285\u0287\5\"\22")
        buf.write(u"\2\u0286\u0288\5\u00ceh\2\u0287\u0286\3\2\2\2\u0287\u0288")
        buf.write(u"\3\2\2\2\u0288\u0289\3\2\2\2\u0289\u028a\7\27\2\2\u028a")
        buf.write(u"!\3\2\2\2\u028b\u028c\7Q\2\2\u028c\u028d\7L\2\2\u028d")
        buf.write(u"\u028e\7\26\2\2\u028e\u028f\5$\23\2\u028f\u0290\7\27")
        buf.write(u"\2\2\u0290#\3\2\2\2\u0291\u0292\b\23\1\2\u0292\u0293")
        buf.write(u"\5\u00d2j\2\u0293\u0294\7\16\2\2\u0294\u029b\3\2\2\2")
        buf.write(u"\u0295\u0296\f\3\2\2\u0296\u0297\5\u00d2j\2\u0297\u0298")
        buf.write(u"\7\16\2\2\u0298\u029a\3\2\2\2\u0299\u0295\3\2\2\2\u029a")
        buf.write(u"\u029d\3\2\2\2\u029b\u0299\3\2\2\2\u029b\u029c\3\2\2")
        buf.write(u"\2\u029c%\3\2\2\2\u029d\u029b\3\2\2\2\u029e\u02a0\7B")
        buf.write(u"\2\2\u029f\u02a1\5\u00a0Q\2\u02a0\u029f\3\2\2\2\u02a0")
        buf.write(u"\u02a1\3\2\2\2\u02a1\u02a2\3\2\2\2\u02a2\u02a3\7r\2\2")
        buf.write(u"\u02a3\u02a4\5\u00b0Y\2\u02a4\u02a6\7\22\2\2\u02a5\u02a7")
        buf.write(u"\5\u00bc_\2\u02a6\u02a5\3\2\2\2\u02a6\u02a7\3\2\2\2\u02a7")
        buf.write(u"\u02a8\3\2\2\2\u02a8\u02a9\7\23\2\2\u02a9\u02aa\7\16")
        buf.write(u"\2\2\u02aa\'\3\2\2\2\u02ab\u02ad\5\u00a0Q\2\u02ac\u02ab")
        buf.write(u"\3\2\2\2\u02ac\u02ad\3\2\2\2\u02ad\u02ae\3\2\2\2\u02ae")
        buf.write(u"\u02af\7r\2\2\u02af\u02b0\5\u00b0Y\2\u02b0\u02b2\7\22")
        buf.write(u"\2\2\u02b1\u02b3\5\u00bc_\2\u02b2\u02b1\3\2\2\2\u02b2")
        buf.write(u"\u02b3\3\2\2\2\u02b3\u02b4\3\2\2\2\u02b4\u02b5\7\23\2")
        buf.write(u"\2\u02b5\u02b7\7\26\2\2\u02b6\u02b8\5\u00ecw\2\u02b7")
        buf.write(u"\u02b6\3\2\2\2\u02b7\u02b8\3\2\2\2\u02b8\u02b9\3\2\2")
        buf.write(u"\2\u02b9\u02ba\7\27\2\2\u02ba)\3\2\2\2\u02bb\u02bd\5")
        buf.write(u"\u00c6d\2\u02bc\u02bb\3\2\2\2\u02bc\u02bd\3\2\2\2\u02bd")
        buf.write(u"\u02bf\3\2\2\2\u02be\u02c0\7v\2\2\u02bf\u02be\3\2\2\2")
        buf.write(u"\u02bf\u02c0\3\2\2\2\u02c0\u02c1\3\2\2\2\u02c1\u02c2")
        buf.write(u"\7r\2\2\u02c2\u02c3\5\u00b0Y\2\u02c3\u02c5\7\22\2\2\u02c4")
        buf.write(u"\u02c6\5\u00bc_\2\u02c5\u02c4\3\2\2\2\u02c5\u02c6\3\2")
        buf.write(u"\2\2\u02c6\u02c7\3\2\2\2\u02c7\u02c8\7\23\2\2\u02c8\u02c9")
        buf.write(u"\7\26\2\2\u02c9\u02ca\5\u00e4s\2\u02ca\u02cb\7\27\2\2")
        buf.write(u"\u02cb+\3\2\2\2\u02cc\u02cd\7\u0091\2\2\u02cd\u02ce\7")
        buf.write(u"r\2\2\u02ce\u02cf\7\u00a5\2\2\u02cf\u02d0\7\22\2\2\u02d0")
        buf.write(u"\u02d1\7\23\2\2\u02d1\u02d2\7\26\2\2\u02d2\u02d3\5\u00ec")
        buf.write(u"w\2\u02d3\u02d4\7\27\2\2\u02d4\u02dc\7\u0096\2\2\u02d5")
        buf.write(u"\u02d6\7\26\2\2\u02d6\u02d7\5\u00eex\2\u02d7\u02d8\7")
        buf.write(u"\27\2\2\u02d8\u02dd\3\2\2\2\u02d9\u02da\5\u00ba^\2\u02da")
        buf.write(u"\u02db\7\16\2\2\u02db\u02dd\3\2\2\2\u02dc\u02d5\3\2\2")
        buf.write(u"\2\u02dc\u02d9\3\2\2\2\u02dd-\3\2\2\2\u02de\u02df\5^")
        buf.write(u"\60\2\u02df\u02e0\7\16\2\2\u02e0/\3\2\2\2\u02e1\u02e6")
        buf.write(u"\5\u00c6d\2\u02e2\u02e3\7\22\2\2\u02e3\u02e4\5\u00de")
        buf.write(u"p\2\u02e4\u02e5\7\23\2\2\u02e5\u02e7\3\2\2\2\u02e6\u02e2")
        buf.write(u"\3\2\2\2\u02e6\u02e7\3\2\2\2\u02e7\u02e8\3\2\2\2\u02e8")
        buf.write(u"\u02eb\5\u00b4[\2\u02e9\u02ea\7)\2\2\u02ea\u02ec\5\u0100")
        buf.write(u"\u0081\2\u02eb\u02e9\3\2\2\2\u02eb\u02ec\3\2\2\2\u02ec")
        buf.write(u"\61\3\2\2\2\u02ed\u02f5\5\64\33\2\u02ee\u02f2\7\26\2")
        buf.write(u"\2\u02ef\u02f0\5\u00ecw\2\u02f0\u02f1\7\27\2\2\u02f1")
        buf.write(u"\u02f3\3\2\2\2\u02f2\u02ef\3\2\2\2\u02f2\u02f3\3\2\2")
        buf.write(u"\2\u02f3\u02f5\3\2\2\2\u02f4\u02ed\3\2\2\2\u02f4\u02ee")
        buf.write(u"\3\2\2\2\u02f5\63\3\2\2\2\u02f6\u02f7\5V,\2\u02f7\u02f8")
        buf.write(u"\7\16\2\2\u02f8\u030c\3\2\2\2\u02f9\u030c\5~@\2\u02fa")
        buf.write(u"\u030c\5\u0082B\2\u02fb\u030c\58\35\2\u02fc\u030c\5\66")
        buf.write(u"\34\2\u02fd\u030c\5R*\2\u02fe\u030c\5T+\2\u02ff\u030c")
        buf.write(u"\5H%\2\u0300\u030c\5> \2\u0301\u030c\5B\"\2\u0302\u030c")
        buf.write(u"\5F$\2\u0303\u030c\5D#\2\u0304\u030c\5N(\2\u0305\u030c")
        buf.write(u"\5L\'\2\u0306\u030c\5l\67\2\u0307\u030c\5:\36\2\u0308")
        buf.write(u"\u030c\5<\37\2\u0309\u030c\5(\25\2\u030a\u030c\5\u00e2")
        buf.write(u"r\2\u030b\u02f6\3\2\2\2\u030b\u02f9\3\2\2\2\u030b\u02fa")
        buf.write(u"\3\2\2\2\u030b\u02fb\3\2\2\2\u030b\u02fc\3\2\2\2\u030b")
        buf.write(u"\u02fd\3\2\2\2\u030b\u02fe\3\2\2\2\u030b\u02ff\3\2\2")
        buf.write(u"\2\u030b\u0300\3\2\2\2\u030b\u0301\3\2\2\2\u030b\u0302")
        buf.write(u"\3\2\2\2\u030b\u0303\3\2\2\2\u030b\u0304\3\2\2\2\u030b")
        buf.write(u"\u0305\3\2\2\2\u030b\u0306\3\2\2\2\u030b\u0307\3\2\2")
        buf.write(u"\2\u030b\u0308\3\2\2\2\u030b\u0309\3\2\2\2\u030b\u030a")
        buf.write(u"\3\2\2\2\u030c\65\3\2\2\2\u030d\u030e\7g\2\2\u030e\u030f")
        buf.write(u"\7\22\2\2\u030f\u0310\7\23\2\2\u0310\u0311\7\16\2\2\u0311")
        buf.write(u"\67\3\2\2\2\u0312\u0313\7X\2\2\u0313\u0314\7\22\2\2\u0314")
        buf.write(u"\u0315\5\u009cO\2\u0315\u0316\7\23\2\2\u0316\u0317\7")
        buf.write(u"\16\2\2\u0317\u032a\3\2\2\2\u0318\u0319\7\u008f\2\2\u0319")
        buf.write(u"\u031a\7\22\2\2\u031a\u031b\5\u009cO\2\u031b\u031c\7")
        buf.write(u"\23\2\2\u031c\u031d\7\16\2\2\u031d\u032a\3\2\2\2\u031e")
        buf.write(u"\u031f\7X\2\2\u031f\u0320\7\22\2\2\u0320\u0321\5\u009c")
        buf.write(u"O\2\u0321\u0322\7\23\2\2\u0322\u0323\7E\2\2\u0323\u0324")
        buf.write(u"\7\u008f\2\2\u0324\u0325\7\22\2\2\u0325\u0326\5\u009c")
        buf.write(u"O\2\u0326\u0327\7\23\2\2\u0327\u0328\7\16\2\2\u0328\u032a")
        buf.write(u"\3\2\2\2\u0329\u0312\3\2\2\2\u0329\u0318\3\2\2\2\u0329")
        buf.write(u"\u031e\3\2\2\2\u032a9\3\2\2\2\u032b\u032c\7\u0097\2\2")
        buf.write(u"\u032c\u032d\7\22\2\2\u032d\u032e\5\u0110\u0089\2\u032e")
        buf.write(u"\u032f\7\23\2\2\u032f\u0330\5\62\32\2\u0330;\3\2\2\2")
        buf.write(u"\u0331\u0332\7\u0097\2\2\u0332\u0333\7\22\2\2\u0333\u0334")
        buf.write(u"\5\u00b8]\2\u0334\u0335\7\23\2\2\u0335\u0336\5\62\32")
        buf.write(u"\2\u0336=\3\2\2\2\u0337\u0338\7\u0090\2\2\u0338\u0339")
        buf.write(u"\7\22\2\2\u0339\u033a\5^\60\2\u033a\u033b\7\23\2\2\u033b")
        buf.write(u"\u033c\7\26\2\2\u033c\u0342\5\u00f0y\2\u033d\u033e\7")
        buf.write(u"V\2\2\u033e\u0340\7\r\2\2\u033f\u0341\5\u00ecw\2\u0340")
        buf.write(u"\u033f\3\2\2\2\u0340\u0341\3\2\2\2\u0341\u0343\3\2\2")
        buf.write(u"\2\u0342\u033d\3\2\2\2\u0342\u0343\3\2\2\2\u0343\u0344")
        buf.write(u"\3\2\2\2\u0344\u0345\7\27\2\2\u0345?\3\2\2\2\u0346\u0347")
        buf.write(u"\7O\2\2\u0347\u0348\5\u00f6|\2\u0348\u034a\7\r\2\2\u0349")
        buf.write(u"\u034b\5\u00ecw\2\u034a\u0349\3\2\2\2\u034a\u034b\3\2")
        buf.write(u"\2\2\u034b\u0354\3\2\2\2\u034c\u034d\7O\2\2\u034d\u034e")
        buf.write(u"\7m\2\2\u034e\u034f\5\u00f4{\2\u034f\u0351\7\r\2\2\u0350")
        buf.write(u"\u0352\5\u00ecw\2\u0351\u0350\3\2\2\2\u0351\u0352\3\2")
        buf.write(u"\2\2\u0352\u0354\3\2\2\2\u0353\u0346\3\2\2\2\u0353\u034c")
        buf.write(u"\3\2\2\2\u0354A\3\2\2\2\u0355\u0356\7h\2\2\u0356\u0357")
        buf.write(u"\7\\\2\2\u0357\u0358\7\22\2\2\u0358\u035b\5\u00b4[\2")
        buf.write(u"\u0359\u035a\7\17\2\2\u035a\u035c\5\u00b4[\2\u035b\u0359")
        buf.write(u"\3\2\2\2\u035b\u035c\3\2\2\2\u035c\u035d\3\2\2\2\u035d")
        buf.write(u"\u035e\7m\2\2\u035e\u035f\5^\60\2\u035f\u0360\7\23\2")
        buf.write(u"\2\u0360\u0361\5\62\32\2\u0361C\3\2\2\2\u0362\u0363\7")
        buf.write(u"Z\2\2\u0363\u0365\7\26\2\2\u0364\u0366\5\u00ecw\2\u0365")
        buf.write(u"\u0364\3\2\2\2\u0365\u0366\3\2\2\2\u0366\u0367\3\2\2")
        buf.write(u"\2\u0367\u0368\7\27\2\2\u0368\u0369\7\u009a\2\2\u0369")
        buf.write(u"\u036a\7\22\2\2\u036a\u036b\5^\60\2\u036b\u036c\7\23")
        buf.write(u"\2\2\u036c\u036d\7\16\2\2\u036dE\3\2\2\2\u036e\u036f")
        buf.write(u"\7\u009a\2\2\u036f\u0370\7\22\2\2\u0370\u0371\5^\60\2")
        buf.write(u"\u0371\u0372\7\23\2\2\u0372\u0373\5\62\32\2\u0373G\3")
        buf.write(u"\2\2\2\u0374\u0375\7l\2\2\u0375\u0376\7\22\2\2\u0376")
        buf.write(u"\u0377\5^\60\2\u0377\u0378\7\23\2\2\u0378\u037a\5\62")
        buf.write(u"\32\2\u0379\u037b\5J&\2\u037a\u0379\3\2\2\2\u037a\u037b")
        buf.write(u"\3\2\2\2\u037b\u037e\3\2\2\2\u037c\u037d\7]\2\2\u037d")
        buf.write(u"\u037f\5\62\32\2\u037e\u037c\3\2\2\2\u037e\u037f\3\2")
        buf.write(u"\2\2\u037fI\3\2\2\2\u0380\u0381\b&\1\2\u0381\u0382\7")
        buf.write(u"]\2\2\u0382\u0383\7l\2\2\u0383\u0384\7\22\2\2\u0384\u0385")
        buf.write(u"\5^\60\2\u0385\u0386\7\23\2\2\u0386\u0387\5\62\32\2\u0387")
        buf.write(u"\u0392\3\2\2\2\u0388\u0389\f\3\2\2\u0389\u038a\7]\2\2")
        buf.write(u"\u038a\u038b\7l\2\2\u038b\u038c\7\22\2\2\u038c\u038d")
        buf.write(u"\5^\60\2\u038d\u038e\7\23\2\2\u038e\u038f\5\62\32\2\u038f")
        buf.write(u"\u0391\3\2\2\2\u0390\u0388\3\2\2\2\u0391\u0394\3\2\2")
        buf.write(u"\2\u0392\u0390\3\2\2\2\u0392\u0393\3\2\2\2\u0393K\3\2")
        buf.write(u"\2\2\u0394\u0392\3\2\2\2\u0395\u0396\7\u0093\2\2\u0396")
        buf.write(u"\u0397\5^\60\2\u0397\u0398\7\16\2\2\u0398M\3\2\2\2\u0399")
        buf.write(u"\u039a\7\u0095\2\2\u039a\u039b\7\22\2\2\u039b\u039c\5")
        buf.write(u"\u00b4[\2\u039c\u039d\7\23\2\2\u039d\u039f\7\26\2\2\u039e")
        buf.write(u"\u03a0\5\u00ecw\2\u039f\u039e\3\2\2\2\u039f\u03a0\3\2")
        buf.write(u"\2\2\u03a0\u03a1\3\2\2\2\u03a1\u03a3\7\27\2\2\u03a2\u03a4")
        buf.write(u"\5\u00f2z\2\u03a3\u03a2\3\2\2\2\u03a3\u03a4\3\2\2\2\u03a4")
        buf.write(u"\u03ae\3\2\2\2\u03a5\u03a6\7P\2\2\u03a6\u03a7\7\22\2")
        buf.write(u"\2\u03a7\u03a8\7F\2\2\u03a8\u03a9\7\23\2\2\u03a9\u03ab")
        buf.write(u"\7\26\2\2\u03aa\u03ac\5\u00ecw\2\u03ab\u03aa\3\2\2\2")
        buf.write(u"\u03ab\u03ac\3\2\2\2\u03ac\u03ad\3\2\2\2\u03ad\u03af")
        buf.write(u"\7\27\2\2\u03ae\u03a5\3\2\2\2\u03ae\u03af\3\2\2\2\u03af")
        buf.write(u"\u03b6\3\2\2\2\u03b0\u03b1\7f\2\2\u03b1\u03b3\7\26\2")
        buf.write(u"\2\u03b2\u03b4\5\u00ecw\2\u03b3\u03b2\3\2\2\2\u03b3\u03b4")
        buf.write(u"\3\2\2\2\u03b4\u03b5\3\2\2\2\u03b5\u03b7\7\27\2\2\u03b6")
        buf.write(u"\u03b0\3\2\2\2\u03b6\u03b7\3\2\2\2\u03b7O\3\2\2\2\u03b8")
        buf.write(u"\u03b9\7P\2\2\u03b9\u03ba\7\22\2\2\u03ba\u03bb\5\u00ba")
        buf.write(u"^\2\u03bb\u03bc\7\23\2\2\u03bc\u03be\7\26\2\2\u03bd\u03bf")
        buf.write(u"\5\u00ecw\2\u03be\u03bd\3\2\2\2\u03be\u03bf\3\2\2\2\u03bf")
        buf.write(u"\u03c0\3\2\2\2\u03c0\u03c1\7\27\2\2\u03c1\u03ce\3\2\2")
        buf.write(u"\2\u03c2\u03c3\7P\2\2\u03c3\u03c4\7m\2\2\u03c4\u03c5")
        buf.write(u"\7\22\2\2\u03c5\u03c6\5\u0094K\2\u03c6\u03c7\7\23\2\2")
        buf.write(u"\u03c7\u03c9\7\26\2\2\u03c8\u03ca\5\u00ecw\2\u03c9\u03c8")
        buf.write(u"\3\2\2\2\u03c9\u03ca\3\2\2\2\u03ca\u03cb\3\2\2\2\u03cb")
        buf.write(u"\u03cc\7\27\2\2\u03cc\u03ce\3\2\2\2\u03cd\u03b8\3\2\2")
        buf.write(u"\2\u03cd\u03c2\3\2\2\2\u03ceQ\3\2\2\2\u03cf\u03d0\7M")
        buf.write(u"\2\2\u03d0\u03d1\7\16\2\2\u03d1S\3\2\2\2\u03d2\u03d4")
        buf.write(u"\7\u0087\2\2\u03d3\u03d5\5^\60\2\u03d4\u03d3\3\2\2\2")
        buf.write(u"\u03d4\u03d5\3\2\2\2\u03d5\u03d6\3\2\2\2\u03d6\u03d7")
        buf.write(u"\7\16\2\2\u03d7U\3\2\2\2\u03d8\u03d9\5X-\2\u03d9\u03db")
        buf.write(u"\7\22\2\2\u03da\u03dc\5z>\2\u03db\u03da\3\2\2\2\u03db")
        buf.write(u"\u03dc\3\2\2\2\u03dc\u03dd\3\2\2\2\u03dd\u03de\7\23\2")
        buf.write(u"\2\u03deW\3\2\2\2\u03df\u03e5\5\u00b0Y\2\u03e0\u03e1")
        buf.write(u"\5Z.\2\u03e1\u03e2\7\21\2\2\u03e2\u03e3\5\u00b0Y\2\u03e3")
        buf.write(u"\u03e5\3\2\2\2\u03e4\u03df\3\2\2\2\u03e4\u03e0\3\2\2")
        buf.write(u"\2\u03e5Y\3\2\2\2\u03e6\u03e7\b.\1\2\u03e7\u03e8\5\u00b2")
        buf.write(u"Z\2\u03e8\u03ed\3\2\2\2\u03e9\u03ea\f\3\2\2\u03ea\u03ec")
        buf.write(u"\5\\/\2\u03eb\u03e9\3\2\2\2\u03ec\u03ef\3\2\2\2\u03ed")
        buf.write(u"\u03eb\3\2\2\2\u03ed\u03ee\3\2\2\2\u03ee[\3\2\2\2\u03ef")
        buf.write(u"\u03ed\3\2\2\2\u03f0\u03f1\7\21\2\2\u03f1\u03f7\5\u00b4")
        buf.write(u"[\2\u03f2\u03f3\7\24\2\2\u03f3\u03f4\5^\60\2\u03f4\u03f5")
        buf.write(u"\7\25\2\2\u03f5\u03f7\3\2\2\2\u03f6\u03f0\3\2\2\2\u03f6")
        buf.write(u"\u03f2\3\2\2\2\u03f7]\3\2\2\2\u03f8\u03f9\b\60\1\2\u03f9")
        buf.write(u"\u0411\5\u01a4\u00d3\2\u03fa\u0411\5d\63\2\u03fb\u0411")
        buf.write(u"\5f\64\2\u03fc\u03fd\7\37\2\2\u03fd\u0411\5^\60&\u03fe")
        buf.write(u"\u03ff\7\31\2\2\u03ff\u0411\5^\60%\u0400\u0401\7\22\2")
        buf.write(u"\2\u0401\u0402\5\u00c6d\2\u0402\u0403\7\23\2\2\u0403")
        buf.write(u"\u0404\5^\60\37\u0404\u0411\3\2\2\2\u0405\u0406\7;\2")
        buf.write(u"\2\u0406\u0407\7\22\2\2\u0407\u0408\5^\60\2\u0408\u0409")
        buf.write(u"\7\23\2\2\u0409\u0411\3\2\2\2\u040a\u040b\7a\2\2\u040b")
        buf.write(u"\u040c\7\22\2\2\u040c\u040d\5\u00b4[\2\u040d\u040e\7")
        buf.write(u"\23\2\2\u040e\u0411\3\2\2\2\u040f\u0411\5b\62\2\u0410")
        buf.write(u"\u03f8\3\2\2\2\u0410\u03fa\3\2\2\2\u0410\u03fb\3\2\2")
        buf.write(u"\2\u0410\u03fc\3\2\2\2\u0410\u03fe\3\2\2\2\u0410\u0400")
        buf.write(u"\3\2\2\2\u0410\u0405\3\2\2\2\u0410\u040a\3\2\2\2\u0410")
        buf.write(u"\u040f\3\2\2\2\u0411\u0486\3\2\2\2\u0412\u0413\f$\2\2")
        buf.write(u"\u0413\u0414\5\u012e\u0098\2\u0414\u0415\5^\60%\u0415")
        buf.write(u"\u0485\3\2\2\2\u0416\u0417\f#\2\2\u0417\u0418\5\u0130")
        buf.write(u"\u0099\2\u0418\u0419\5^\60$\u0419\u0485\3\2\2\2\u041a")
        buf.write(u"\u041b\f\"\2\2\u041b\u041c\5\u0134\u009b\2\u041c\u041d")
        buf.write(u"\5^\60#\u041d\u0485\3\2\2\2\u041e\u041f\f!\2\2\u041f")
        buf.write(u"\u0420\5\u0132\u009a\2\u0420\u0421\5^\60\"\u0421\u0485")
        buf.write(u"\3\2\2\2\u0422\u0423\f \2\2\u0423\u0424\t\2\2\2\u0424")
        buf.write(u"\u0485\5^\60!\u0425\u0426\f\36\2\2\u0426\u0427\7&\2\2")
        buf.write(u"\u0427\u0485\5^\60\37\u0428\u0429\f\35\2\2\u0429\u042a")
        buf.write(u"\7\'\2\2\u042a\u0485\5^\60\36\u042b\u042c\f\34\2\2\u042c")
        buf.write(u"\u042d\7$\2\2\u042d\u0485\5^\60\35\u042e\u042f\f\33\2")
        buf.write(u"\2\u042f\u0430\7%\2\2\u0430\u0485\5^\60\34\u0431\u0432")
        buf.write(u"\f\30\2\2\u0432\u0433\7p\2\2\u0433\u0434\7x\2\2\u0434")
        buf.write(u"\u0485\5^\60\31\u0435\u0436\f\27\2\2\u0436\u0437\7p\2")
        buf.write(u"\2\u0437\u0485\5^\60\30\u0438\u0439\f\26\2\2\u0439\u043a")
        buf.write(u"\7+\2\2\u043a\u0485\5^\60\27\u043b\u043c\f\25\2\2\u043c")
        buf.write(u"\u043d\7*\2\2\u043d\u0485\5^\60\26\u043e\u043f\f\24\2")
        buf.write(u"\2\u043f\u0440\7,\2\2\u0440\u0485\5^\60\25\u0441\u0442")
        buf.write(u"\f\23\2\2\u0442\u0443\7T\2\2\u0443\u0485\5^\60\24\u0444")
        buf.write(u"\u0445\f\22\2\2\u0445\u0446\7m\2\2\u0446\u0485\5^\60")
        buf.write(u"\23\u0447\u0448\f\21\2\2\u0448\u0449\7k\2\2\u0449\u0485")
        buf.write(u"\5^\60\22\u044a\u044b\f\20\2\2\u044b\u044c\7k\2\2\u044c")
        buf.write(u"\u044d\7C\2\2\u044d\u0485\5^\60\21\u044e\u044f\f\17\2")
        buf.write(u"\2\u044f\u0450\7k\2\2\u0450\u0451\7F\2\2\u0451\u0485")
        buf.write(u"\5^\60\20\u0452\u0453\f\16\2\2\u0453\u0454\7x\2\2\u0454")
        buf.write(u"\u0455\7T\2\2\u0455\u0485\5^\60\17\u0456\u0457\f\r\2")
        buf.write(u"\2\u0457\u0458\7x\2\2\u0458\u0459\7m\2\2\u0459\u0485")
        buf.write(u"\5^\60\16\u045a\u045b\f\f\2\2\u045b\u045c\7x\2\2\u045c")
        buf.write(u"\u045d\7k\2\2\u045d\u0485\5^\60\r\u045e\u045f\f\13\2")
        buf.write(u"\2\u045f\u0460\7x\2\2\u0460\u0461\7k\2\2\u0461\u0462")
        buf.write(u"\7C\2\2\u0462\u0485\5^\60\f\u0463\u0464\f\n\2\2\u0464")
        buf.write(u"\u0465\7x\2\2\u0465\u0466\7k\2\2\u0466\u0467\7F\2\2\u0467")
        buf.write(u"\u0485\5^\60\13\u0468\u0469\f\t\2\2\u0469\u046a\7\35")
        buf.write(u"\2\2\u046a\u0485\5^\60\n\u046b\u046c\f\b\2\2\u046c\u046d")
        buf.write(u"\7\33\2\2\u046d\u0485\5^\60\t\u046e\u046f\f\7\2\2\u046f")
        buf.write(u"\u0470\7\30\2\2\u0470\u0471\5^\60\2\u0471\u0472\7\r\2")
        buf.write(u"\2\u0472\u0473\5^\60\b\u0473\u0485\3\2\2\2\u0474\u0475")
        buf.write(u"\f\32\2\2\u0475\u0476\7p\2\2\u0476\u0477\7x\2\2\u0477")
        buf.write(u"\u0485\5`\61\2\u0478\u0479\f\31\2\2\u0479\u047a\7p\2")
        buf.write(u"\2\u047a\u0485\5`\61\2\u047b\u047c\f\3\2\2\u047c\u047d")
        buf.write(u"\7h\2\2\u047d\u047e\7\\\2\2\u047e\u047f\7\22\2\2\u047f")
        buf.write(u"\u0480\5\u00b4[\2\u0480\u0481\7m\2\2\u0481\u0482\5^\60")
        buf.write(u"\2\u0482\u0483\7\23\2\2\u0483\u0485\3\2\2\2\u0484\u0412")
        buf.write(u"\3\2\2\2\u0484\u0416\3\2\2\2\u0484\u041a\3\2\2\2\u0484")
        buf.write(u"\u041e\3\2\2\2\u0484\u0422\3\2\2\2\u0484\u0425\3\2\2")
        buf.write(u"\2\u0484\u0428\3\2\2\2\u0484\u042b\3\2\2\2\u0484\u042e")
        buf.write(u"\3\2\2\2\u0484\u0431\3\2\2\2\u0484\u0435\3\2\2\2\u0484")
        buf.write(u"\u0438\3\2\2\2\u0484\u043b\3\2\2\2\u0484\u043e\3\2\2")
        buf.write(u"\2\u0484\u0441\3\2\2\2\u0484\u0444\3\2\2\2\u0484\u0447")
        buf.write(u"\3\2\2\2\u0484\u044a\3\2\2\2\u0484\u044e\3\2\2\2\u0484")
        buf.write(u"\u0452\3\2\2\2\u0484\u0456\3\2\2\2\u0484\u045a\3\2\2")
        buf.write(u"\2\u0484\u045e\3\2\2\2\u0484\u0463\3\2\2\2\u0484\u0468")
        buf.write(u"\3\2\2\2\u0484\u046b\3\2\2\2\u0484\u046e\3\2\2\2\u0484")
        buf.write(u"\u0474\3\2\2\2\u0484\u0478\3\2\2\2\u0484\u047b\3\2\2")
        buf.write(u"\2\u0485\u0488\3\2\2\2\u0486\u0484\3\2\2\2\u0486\u0487")
        buf.write(u"\3\2\2\2\u0487_\3\2\2\2\u0488\u0486\3\2\2\2\u0489\u048a")
        buf.write(u"\6\61$\3\u048a\u048b\7\u00a2\2\2\u048b\u048c\5\u00c6")
        buf.write(u"d\2\u048ca\3\2\2\2\u048d\u048e\5\u00b8]\2\u048ec\3\2")
        buf.write(u"\2\2\u048f\u0490\b\63\1\2\u0490\u0491\5\u00fa~\2\u0491")
        buf.write(u"\u0496\3\2\2\2\u0492\u0493\f\3\2\2\u0493\u0495\5t;\2")
        buf.write(u"\u0494\u0492\3\2\2\2\u0495\u0498\3\2\2\2\u0496\u0494")
        buf.write(u"\3\2\2\2\u0496\u0497\3\2\2\2\u0497e\3\2\2\2\u0498\u0496")
        buf.write(u"\3\2\2\2\u0499\u04a3\5h\65\2\u049a\u04a3\5j\66\2\u049b")
        buf.write(u"\u04a3\5n8\2\u049c\u04a3\5p9\2\u049d\u04a3\5\u0116\u008c")
        buf.write(u"\2\u049e\u04a3\5\u0118\u008d\2\u049f\u04a3\5r:\2\u04a0")
        buf.write(u"\u04a3\5V,\2\u04a1\u04a3\5v<\2\u04a2\u0499\3\2\2\2\u04a2")
        buf.write(u"\u049a\3\2\2\2\u04a2\u049b\3\2\2\2\u04a2\u049c\3\2\2")
        buf.write(u"\2\u04a2\u049d\3\2\2\2\u04a2\u049e\3\2\2\2\u04a2\u049f")
        buf.write(u"\3\2\2\2\u04a2\u04a0\3\2\2\2\u04a2\u04a1\3\2\2\2\u04a3")
        buf.write(u"g\3\2\2\2\u04a4\u04a5\7=\2\2\u04a5\u04a6\7\22\2\2\u04a6")
        buf.write(u"\u04a7\5^\60\2\u04a7\u04a8\7\23\2\2\u04a8i\3\2\2\2\u04a9")
        buf.write(u"\u04aa\7<\2\2\u04aa\u04ac\7\22\2\2\u04ab\u04ad\5^\60")
        buf.write(u"\2\u04ac\u04ab\3\2\2\2\u04ac\u04ad\3\2\2\2\u04ad\u04ae")
        buf.write(u"\3\2\2\2\u04ae\u04af\7\23\2\2\u04afk\3\2\2\2\u04b0\u04b1")
        buf.write(u"\7\u009b\2\2\u04b1\u04b2\7\22\2\2\u04b2\u04b3\5^\60\2")
        buf.write(u"\u04b3\u04b4\7\23\2\2\u04b4\u04b5\7\u0094\2\2\u04b5\u04b6")
        buf.write(u"\5^\60\2\u04b6\u04b7\7\16\2\2\u04b7m\3\2\2\2\u04b8\u04b9")
        buf.write(u"\7e\2\2\u04b9\u04ba\7\22\2\2\u04ba\u04bb\5^\60\2\u04bb")
        buf.write(u"\u04bc\7\23\2\2\u04bc\u04bd\7\u0097\2\2\u04bd\u04be\7")
        buf.write(u"\22\2\2\u04be\u04bf\5\u00b4[\2\u04bf\u04c0\7\23\2\2\u04c0")
        buf.write(u"\u04c1\7\u0099\2\2\u04c1\u04c2\7\22\2\2\u04c2\u04c3\5")
        buf.write(u"^\60\2\u04c3\u04c4\7\23\2\2\u04c4o\3\2\2\2\u04c5\u04c6")
        buf.write(u"\7d\2\2\u04c6\u04cb\7|\2\2\u04c7\u04c8\7\22\2\2\u04c8")
        buf.write(u"\u04c9\5\u00a8U\2\u04c9\u04ca\7\23\2\2\u04ca\u04cc\3")
        buf.write(u"\2\2\2\u04cb\u04c7\3\2\2\2\u04cb\u04cc\3\2\2\2\u04cc")
        buf.write(u"\u04cd\3\2\2\2\u04cd\u04ce\7\u0099\2\2\u04ce\u04cf\7")
        buf.write(u"\22\2\2\u04cf\u04d0\5^\60\2\u04d0\u04d1\7\23\2\2\u04d1")
        buf.write(u"\u04f9\3\2\2\2\u04d2\u04e7\7d\2\2\u04d3\u04d8\7C\2\2")
        buf.write(u"\u04d4\u04d5\7\22\2\2\u04d5\u04d6\5\u00a8U\2\u04d6\u04d7")
        buf.write(u"\7\23\2\2\u04d7\u04d9\3\2\2\2\u04d8\u04d4\3\2\2\2\u04d8")
        buf.write(u"\u04d9\3\2\2\2\u04d9\u04e8\3\2\2\2\u04da\u04db\7\22\2")
        buf.write(u"\2\u04db\u04dc\5\u00a8U\2\u04dc\u04dd\7\23\2\2\u04dd")
        buf.write(u"\u04df\3\2\2\2\u04de\u04da\3\2\2\2\u04de\u04df\3\2\2")
        buf.write(u"\2\u04df\u04e0\3\2\2\2\u04e0\u04e1\7\u0089\2\2\u04e1")
        buf.write(u"\u04e2\7\22\2\2\u04e2\u04e3\5^\60\2\u04e3\u04e4\7\u0094")
        buf.write(u"\2\2\u04e4\u04e5\5^\60\2\u04e5\u04e6\7\23\2\2\u04e6\u04e8")
        buf.write(u"\3\2\2\2\u04e7\u04d3\3\2\2\2\u04e7\u04de\3\2\2\2\u04e8")
        buf.write(u"\u04ee\3\2\2\2\u04e9\u04ea\7\u0099\2\2\u04ea\u04eb\7")
        buf.write(u"\22\2\2\u04eb\u04ec\5^\60\2\u04ec\u04ed\7\23\2\2\u04ed")
        buf.write(u"\u04ef\3\2\2\2\u04ee\u04e9\3\2\2\2\u04ee\u04ef\3\2\2")
        buf.write(u"\2\u04ef\u04f6\3\2\2\2\u04f0\u04f1\7\u0080\2\2\u04f1")
        buf.write(u"\u04f2\7N\2\2\u04f2\u04f3\7\22\2\2\u04f3\u04f4\5\u011a")
        buf.write(u"\u008e\2\u04f4\u04f5\7\23\2\2\u04f5\u04f7\3\2\2\2\u04f6")
        buf.write(u"\u04f0\3\2\2\2\u04f6\u04f7\3\2\2\2\u04f7\u04f9\3\2\2")
        buf.write(u"\2\u04f8\u04c5\3\2\2\2\u04f8\u04d2\3\2\2\2\u04f9q\3\2")
        buf.write(u"\2\2\u04fa\u04fc\7\u008d\2\2\u04fb\u04fd\7Y\2\2\u04fc")
        buf.write(u"\u04fb\3\2\2\2\u04fc\u04fd\3\2\2\2\u04fd\u04fe\3\2\2")
        buf.write(u"\2\u04fe\u04ff\7\22\2\2\u04ff\u0505\5d\63\2\u0500\u0501")
        buf.write(u"\7\17\2\2\u0501\u0502\5\u0124\u0093\2\u0502\u0503\7)")
        buf.write(u"\2\2\u0503\u0504\5d\63\2\u0504\u0506\3\2\2\2\u0505\u0500")
        buf.write(u"\3\2\2\2\u0505\u0506\3\2\2\2\u0506\u0507\3\2\2\2\u0507")
        buf.write(u"\u0508\7\23\2\2\u0508s\3\2\2\2\u0509\u050a\7\21\2\2\u050a")
        buf.write(u"\u0514\5\u00b4[\2\u050b\u050c\7\24\2\2\u050c\u050d\5")
        buf.write(u"^\60\2\u050d\u050e\7\25\2\2\u050e\u0514\3\2\2\2\u050f")
        buf.write(u"\u0510\7\24\2\2\u0510\u0511\5\u010e\u0088\2\u0511\u0512")
        buf.write(u"\7\25\2\2\u0512\u0514\3\2\2\2\u0513\u0509\3\2\2\2\u0513")
        buf.write(u"\u050b\3\2\2\2\u0513\u050f\3\2\2\2\u0514u\3\2\2\2\u0515")
        buf.write(u"\u0516\5\u00a8U\2\u0516\u0517\7\22\2\2\u0517\u051a\5")
        buf.write(u"x=\2\u0518\u0519\7\17\2\2\u0519\u051b\5z>\2\u051a\u0518")
        buf.write(u"\3\2\2\2\u051a\u051b\3\2\2\2\u051b\u051c\3\2\2\2\u051c")
        buf.write(u"\u051d\7\23\2\2\u051d\u0526\3\2\2\2\u051e\u051f\5\u00a8")
        buf.write(u"U\2\u051f\u0521\7\22\2\2\u0520\u0522\5z>\2\u0521\u0520")
        buf.write(u"\3\2\2\2\u0521\u0522\3\2\2\2\u0522\u0523\3\2\2\2\u0523")
        buf.write(u"\u0524\7\23\2\2\u0524\u0526\3\2\2\2\u0525\u0515\3\2\2")
        buf.write(u"\2\u0525\u051e\3\2\2\2\u0526w\3\2\2\2\u0527\u0528\7i")
        buf.write(u"\2\2\u0528\u0529\5\u012c\u0097\2\u0529\u052a\5^\60\2")
        buf.write(u"\u052a\u052b\6=&\3\u052by\3\2\2\2\u052c\u052d\b>\1\2")
        buf.write(u"\u052d\u052e\5^\60\2\u052e\u052f\6>\'\3\u052f\u0532\3")
        buf.write(u"\2\2\2\u0530\u0532\5|?\2\u0531\u052c\3\2\2\2\u0531\u0530")
        buf.write(u"\3\2\2\2\u0532\u0538\3\2\2\2\u0533\u0534\f\3\2\2\u0534")
        buf.write(u"\u0535\7\17\2\2\u0535\u0537\5|?\2\u0536\u0533\3\2\2\2")
        buf.write(u"\u0537\u053a\3\2\2\2\u0538\u0536\3\2\2\2\u0538\u0539")
        buf.write(u"\3\2\2\2\u0539{\3\2\2\2\u053a\u0538\3\2\2\2\u053b\u053f")
        buf.write(u"\5\u00b4[\2\u053c\u053d\5\u012c\u0097\2\u053d\u053e\5")
        buf.write(u"^\60\2\u053e\u0540\3\2\2\2\u053f\u053c\3\2\2\2\u053f")
        buf.write(u"\u0540\3\2\2\2\u0540}\3\2\2\2\u0541\u0542\5\u0112\u008a")
        buf.write(u"\2\u0542\u0543\5\u012c\u0097\2\u0543\u0544\5^\60\2\u0544")
        buf.write(u"\u0545\7\16\2\2\u0545\177\3\2\2\2\u0546\u0547\7\21\2")
        buf.write(u"\2\u0547\u054d\5\u00b4[\2\u0548\u0549\7\24\2\2\u0549")
        buf.write(u"\u054a\5^\60\2\u054a\u054b\7\25\2\2\u054b\u054d\3\2\2")
        buf.write(u"\2\u054c\u0546\3\2\2\2\u054c\u0548\3\2\2\2\u054d\u0081")
        buf.write(u"\3\2\2\2\u054e\u054f\5\u00dco\2\u054f\u0550\5\u012c\u0097")
        buf.write(u"\2\u0550\u0551\5^\60\2\u0551\u0552\7\16\2\2\u0552\u0083")
        buf.write(u"\3\2\2\2\u0553\u0554\7z\2\2\u0554\u0085\3\2\2\2\u0555")
        buf.write(u"\u0557\5\u0088E\2\u0556\u0555\3\2\2\2\u0556\u0557\3\2")
        buf.write(u"\2\2\u0557\u0558\3\2\2\2\u0558\u0559\5\u0136\u009c\2")
        buf.write(u"\u0559\u055a\7\2\2\3\u055a\u0087\3\2\2\2\u055b\u0561")
        buf.write(u"\5\u008aF\2\u055c\u055d\5\u0138\u009d\2\u055d\u055e\5")
        buf.write(u"\u008aF\2\u055e\u0560\3\2\2\2\u055f\u055c\3\2\2\2\u0560")
        buf.write(u"\u0563\3\2\2\2\u0561\u055f\3\2\2\2\u0561\u0562\3\2\2")
        buf.write(u"\2\u0562\u0089\3\2\2\2\u0563\u0561\3\2\2\2\u0564\u0565")
        buf.write(u"\5\u00e2r\2\u0565\u0566\5\u0138\u009d\2\u0566\u0568\3")
        buf.write(u"\2\2\2\u0567\u0564\3\2\2\2\u0568\u056b\3\2\2\2\u0569")
        buf.write(u"\u0567\3\2\2\2\u0569\u056a\3\2\2\2\u056a\u0571\3\2\2")
        buf.write(u"\2\u056b\u0569\3\2\2\2\u056c\u0572\5\n\6\2\u056d\u0572")
        buf.write(u"\5\u00acW\2\u056e\u0572\5\u008cG\2\u056f\u0572\5\u008e")
        buf.write(u"H\2\u0570\u0572\5\u00e0q\2\u0571\u056c\3\2\2\2\u0571")
        buf.write(u"\u056d\3\2\2\2\u0571\u056e\3\2\2\2\u0571\u056f\3\2\2")
        buf.write(u"\2\u0571\u0570\3\2\2\2\u0572\u008b\3\2\2\2\u0573\u0574")
        buf.write(u"\5\36\20\2\u0574\u008d\3\2\2\2\u0575\u0578\5\2\2\2\u0576")
        buf.write(u"\u0578\5\4\3\2\u0577\u0575\3\2\2\2\u0577\u0576\3\2\2")
        buf.write(u"\2\u0578\u008f\3\2\2\2\u0579\u057f\5\b\5\2\u057a\u057b")
        buf.write(u"\5\u0138\u009d\2\u057b\u057c\5\b\5\2\u057c\u057e\3\2")
        buf.write(u"\2\2\u057d\u057a\3\2\2\2\u057e\u0581\3\2\2\2\u057f\u057d")
        buf.write(u"\3\2\2\2\u057f\u0580\3\2\2\2\u0580\u0091\3\2\2\2\u0581")
        buf.write(u"\u057f\3\2\2\2\u0582\u0588\5\6\4\2\u0583\u0584\5\u0138")
        buf.write(u"\u009d\2\u0584\u0585\5\6\4\2\u0585\u0587\3\2\2\2\u0586")
        buf.write(u"\u0583\3\2\2\2\u0587\u058a\3\2\2\2\u0588\u0586\3\2\2")
        buf.write(u"\2\u0588\u0589\3\2\2\2\u0589\u0093\3\2\2\2\u058a\u0588")
        buf.write(u"\3\2\2\2\u058b\u0590\5\u00ba^\2\u058c\u058d\7\17\2\2")
        buf.write(u"\u058d\u058f\5\u00ba^\2\u058e\u058c\3\2\2\2\u058f\u0592")
        buf.write(u"\3\2\2\2\u0590\u058e\3\2\2\2\u0590\u0591\3\2\2\2\u0591")
        buf.write(u"\u0095\3\2\2\2\u0592\u0590\3\2\2\2\u0593\u0594\7m\2\2")
        buf.write(u"\u0594\u059e\5\u0098M\2\u0595\u0596\7m\2\2\u0596\u059e")
        buf.write(u"\5\u009aN\2\u0597\u0598\7m\2\2\u0598\u059e\5\u009eP\2")
        buf.write(u"\u0599\u059a\7q\2\2\u059a\u059e\7\u00a5\2\2\u059b\u059c")
        buf.write(u"\7q\2\2\u059c\u059e\5^\60\2\u059d\u0593\3\2\2\2\u059d")
        buf.write(u"\u0595\3\2\2\2\u059d\u0597\3\2\2\2\u059d\u0599\3\2\2")
        buf.write(u"\2\u059d\u059b\3\2\2\2\u059e\u0097\3\2\2\2\u059f\u05a1")
        buf.write(u"\7u\2\2\u05a0\u059f\3\2\2\2\u05a0\u05a1\3\2\2\2\u05a1")
        buf.write(u"\u05a2\3\2\2\2\u05a2\u05a4\7\24\2\2\u05a3\u05a5\5\u009c")
        buf.write(u"O\2\u05a4\u05a3\3\2\2\2\u05a4\u05a5\3\2\2\2\u05a5\u05a6")
        buf.write(u"\3\2\2\2\u05a6\u05a7\7\25\2\2\u05a7\u0099\3\2\2\2\u05a8")
        buf.write(u"\u05aa\7u\2\2\u05a9\u05a8\3\2\2\2\u05a9\u05aa\3\2\2\2")
        buf.write(u"\u05aa\u05ab\3\2\2\2\u05ab\u05ad\7&\2\2\u05ac\u05ae\5")
        buf.write(u"\u009cO\2\u05ad\u05ac\3\2\2\2\u05ad\u05ae\3\2\2\2\u05ae")
        buf.write(u"\u05af\3\2\2\2\u05af\u05b0\7$\2\2\u05b0\u009b\3\2\2\2")
        buf.write(u"\u05b1\u05b6\5^\60\2\u05b2\u05b3\7\17\2\2\u05b3\u05b5")
        buf.write(u"\5^\60\2\u05b4\u05b2\3\2\2\2\u05b5\u05b8\3\2\2\2\u05b6")
        buf.write(u"\u05b4\3\2\2\2\u05b6\u05b7\3\2\2\2\u05b7\u009d\3\2\2")
        buf.write(u"\2\u05b8\u05b6\3\2\2\2\u05b9\u05ba\7\24\2\2\u05ba\u05bb")
        buf.write(u"\5^\60\2\u05bb\u05bc\7\20\2\2\u05bc\u05bd\5^\60\2\u05bd")
        buf.write(u"\u05be\7\25\2\2\u05be\u009f\3\2\2\2\u05bf\u05c0\bQ\1")
        buf.write(u"\2\u05c0\u05cc\5\u00a2R\2\u05c1\u05c2\7A\2\2\u05c2\u05c3")
        buf.write(u"\7&\2\2\u05c3\u05c4\5\u00a0Q\2\u05c4\u05c5\7$\2\2\u05c5")
        buf.write(u"\u05cc\3\2\2\2\u05c6\u05c7\7@\2\2\u05c7\u05c8\7&\2\2")
        buf.write(u"\u05c8\u05c9\5\u00a0Q\2\u05c9\u05ca\7$\2\2\u05ca\u05cc")
        buf.write(u"\3\2\2\2\u05cb\u05bf\3\2\2\2\u05cb\u05c1\3\2\2\2\u05cb")
        buf.write(u"\u05c6\3\2\2\2\u05cc\u05d7\3\2\2\2\u05cd\u05ce\f\7\2")
        buf.write(u"\2\u05ce\u05d6\7(\2\2\u05cf\u05d0\f\6\2\2\u05d0\u05d1")
        buf.write(u"\7\24\2\2\u05d1\u05d6\7\25\2\2\u05d2\u05d3\f\5\2\2\u05d3")
        buf.write(u"\u05d4\7\26\2\2\u05d4\u05d6\7\27\2\2\u05d5\u05cd\3\2")
        buf.write(u"\2\2\u05d5\u05cf\3\2\2\2\u05d5\u05d2\3\2\2\2\u05d6\u05d9")
        buf.write(u"\3\2\2\2\u05d7\u05d5\3\2\2\2\u05d7\u05d8\3\2\2\2\u05d8")
        buf.write(u"\u00a1\3\2\2\2\u05d9\u05d7\3\2\2\2\u05da\u05dd\5\u00a4")
        buf.write(u"S\2\u05db\u05dd\5\u00a6T\2\u05dc\u05da\3\2\2\2\u05dc")
        buf.write(u"\u05db\3\2\2\2\u05dd\u00a3\3\2\2\2\u05de\u05ee\7\60\2")
        buf.write(u"\2\u05df\u05ee\7\61\2\2\u05e0\u05ee\7\62\2\2\u05e1\u05ee")
        buf.write(u"\7>\2\2\u05e2\u05ee\7\63\2\2\u05e3\u05ee\7\64\2\2\u05e4")
        buf.write(u"\u05ee\7<\2\2\u05e5\u05ee\7\65\2\2\u05e6\u05ee\7\67\2")
        buf.write(u"\2\u05e7\u05ee\7\66\2\2\u05e8\u05ee\78\2\2\u05e9\u05ee")
        buf.write(u"\79\2\2\u05ea\u05ee\7;\2\2\u05eb\u05ee\7=\2\2\u05ec\u05ee")
        buf.write(u"\7?\2\2\u05ed\u05de\3\2\2\2\u05ed\u05df\3\2\2\2\u05ed")
        buf.write(u"\u05e0\3\2\2\2\u05ed\u05e1\3\2\2\2\u05ed\u05e2\3\2\2")
        buf.write(u"\2\u05ed\u05e3\3\2\2\2\u05ed\u05e4\3\2\2\2\u05ed\u05e5")
        buf.write(u"\3\2\2\2\u05ed\u05e6\3\2\2\2\u05ed\u05e7\3\2\2\2\u05ed")
        buf.write(u"\u05e8\3\2\2\2\u05ed\u05e9\3\2\2\2\u05ed\u05ea\3\2\2")
        buf.write(u"\2\u05ed\u05eb\3\2\2\2\u05ed\u05ec\3\2\2\2\u05ee\u00a5")
        buf.write(u"\3\2\2\2\u05ef\u05f0\7\u00a1\2\2\u05f0\u00a7\3\2\2\2")
        buf.write(u"\u05f1\u05f3\7u\2\2\u05f2\u05f1\3\2\2\2\u05f2\u05f3\3")
        buf.write(u"\2\2\2\u05f3\u05f4\3\2\2\2\u05f4\u05f5\5\u00a6T\2\u05f5")
        buf.write(u"\u00a9\3\2\2\2\u05f6\u05f7\7;\2\2\u05f7\u00ab\3\2\2\2")
        buf.write(u"\u05f8\u05fc\5\f\7\2\u05f9\u05fc\5 \21\2\u05fa\u05fc")
        buf.write(u"\5\16\b\2\u05fb\u05f8\3\2\2\2\u05fb\u05f9\3\2\2\2\u05fb")
        buf.write(u"\u05fa\3\2\2\2\u05fc\u00ad\3\2\2\2\u05fd\u0602\5\u00b8")
        buf.write(u"]\2\u05fe\u05ff\7\17\2\2\u05ff\u0601\5\u00b8]\2\u0600")
        buf.write(u"\u05fe\3\2\2\2\u0601\u0604\3\2\2\2\u0602\u0600\3\2\2")
        buf.write(u"\2\u0602\u0603\3\2\2\2\u0603\u00af\3\2\2\2\u0604\u0602")
        buf.write(u"\3\2\2\2\u0605\u0608\5\u00b4[\2\u0606\u0608\5\u00b8]")
        buf.write(u"\2\u0607\u0605\3\2\2\2\u0607\u0606\3\2\2\2\u0608\u00b1")
        buf.write(u"\3\2\2\2\u0609\u060d\5\u00b4[\2\u060a\u060d\5\u00b8]")
        buf.write(u"\2\u060b\u060d\5\u00ba^\2\u060c\u0609\3\2\2\2\u060c\u060a")
        buf.write(u"\3\2\2\2\u060c\u060b\3\2\2\2\u060d\u00b3\3\2\2\2\u060e")
        buf.write(u"\u060f\7\u00a2\2\2\u060f\u00b5\3\2\2\2\u0610\u0611\t")
        buf.write(u"\3\2\2\u0611\u00b7\3\2\2\2\u0612\u0613\7\u00a1\2\2\u0613")
        buf.write(u"\u00b9\3\2\2\2\u0614\u0615\7\u00a0\2\2\u0615\u00bb\3")
        buf.write(u"\2\2\2\u0616\u061b\5\u00be`\2\u0617\u0618\7\17\2\2\u0618")
        buf.write(u"\u061a\5\u00be`\2\u0619\u0617\3\2\2\2\u061a\u061d\3\2")
        buf.write(u"\2\2\u061b\u0619\3\2\2\2\u061b\u061c\3\2\2\2\u061c\u00bd")
        buf.write(u"\3\2\2\2\u061d\u061b\3\2\2\2\u061e\u0624\5\u00c4c\2\u061f")
        buf.write(u"\u0621\7u\2\2\u0620\u061f\3\2\2\2\u0620\u0621\3\2\2\2")
        buf.write(u"\u0621\u0622\3\2\2\2\u0622\u0624\5\u00c0a\2\u0623\u061e")
        buf.write(u"\3\2\2\2\u0623\u0620\3\2\2\2\u0624\u00bf\3\2\2\2\u0625")
        buf.write(u"\u0628\5\u00c2b\2\u0626\u0628\5\60\31\2\u0627\u0625\3")
        buf.write(u"\2\2\2\u0627\u0626\3\2\2\2\u0628\u00c1\3\2\2\2\u0629")
        buf.write(u"\u062c\5\u00b4[\2\u062a\u062b\7)\2\2\u062b\u062d\5\u0100")
        buf.write(u"\u0081\2\u062c\u062a\3\2\2\2\u062c\u062d\3\2\2\2\u062d")
        buf.write(u"\u00c3\3\2\2\2\u062e\u062f\5\u00aaV\2\u062f\u0630\5\u00b4")
        buf.write(u"[\2\u0630\u00c5\3\2\2\2\u0631\u0634\5\u00a0Q\2\u0632")
        buf.write(u"\u0634\5\u00c8e\2\u0633\u0631\3\2\2\2\u0633\u0632\3\2")
        buf.write(u"\2\2\u0634\u00c7\3\2\2\2\u0635\u0636\be\1\2\u0636\u0637")
        buf.write(u"\7F\2\2\u0637\u0640\3\2\2\2\u0638\u0639\f\4\2\2\u0639")
        buf.write(u"\u063a\7\24\2\2\u063a\u063f\7\25\2\2\u063b\u063c\f\3")
        buf.write(u"\2\2\u063c\u063d\7\26\2\2\u063d\u063f\7\27\2\2\u063e")
        buf.write(u"\u0638\3\2\2\2\u063e\u063b\3\2\2\2\u063f\u0642\3\2\2")
        buf.write(u"\2\u0640\u063e\3\2\2\2\u0640\u0641\3\2\2\2\u0641\u00c9")
        buf.write(u"\3\2\2\2\u0642\u0640\3\2\2\2\u0643\u0649\5\u00ccg\2\u0644")
        buf.write(u"\u0645\5\u0138\u009d\2\u0645\u0646\5\u00ccg\2\u0646\u0648")
        buf.write(u"\3\2\2\2\u0647\u0644\3\2\2\2\u0648\u064b\3\2\2\2\u0649")
        buf.write(u"\u0647\3\2\2\2\u0649\u064a\3\2\2\2\u064a\u00cb\3\2\2")
        buf.write(u"\2\u064b\u0649\3\2\2\2\u064c\u0652\5\26\f\2\u064d\u0652")
        buf.write(u"\5\32\16\2\u064e\u0652\5(\25\2\u064f\u0652\5&\24\2\u0650")
        buf.write(u"\u0652\5\24\13\2\u0651\u064c\3\2\2\2\u0651\u064d\3\2")
        buf.write(u"\2\2\u0651\u064e\3\2\2\2\u0651\u064f\3\2\2\2\u0651\u0650")
        buf.write(u"\3\2\2\2\u0652\u00cd\3\2\2\2\u0653\u0659\5\u00d0i\2\u0654")
        buf.write(u"\u0655\5\u0138\u009d\2\u0655\u0656\5\u00d0i\2\u0656\u0658")
        buf.write(u"\3\2\2\2\u0657\u0654\3\2\2\2\u0658\u065b\3\2\2\2\u0659")
        buf.write(u"\u0657\3\2\2\2\u0659\u065a\3\2\2\2\u065a\u00cf\3\2\2")
        buf.write(u"\2\u065b\u0659\3\2\2\2\u065c\u0660\5\34\17\2\u065d\u0660")
        buf.write(u"\5\30\r\2\u065e\u0660\5*\26\2\u065f\u065c\3\2\2\2\u065f")
        buf.write(u"\u065d\3\2\2\2\u065f\u065e\3\2\2\2\u0660\u00d1\3\2\2")
        buf.write(u"\2\u0661\u0662\7\7\2\2\u0662\u066c\5\u0184\u00c3\2\u0663")
        buf.write(u"\u0664\7\b\2\2\u0664\u066c\5\u019e\u00d0\2\u0665\u0666")
        buf.write(u"\7\t\2\2\u0666\u066c\5\u00d4k\2\u0667\u0668\7\n\2\2\u0668")
        buf.write(u"\u066c\5\u00d4k\2\u0669\u066a\7\13\2\2\u066a\u066c\5")
        buf.write(u"\u00d8m\2\u066b\u0661\3\2\2\2\u066b\u0663\3\2\2\2\u066b")
        buf.write(u"\u0665\3\2\2\2\u066b\u0667\3\2\2\2\u066b\u0669\3\2\2")
        buf.write(u"\2\u066c\u00d3\3\2\2\2\u066d\u066f\5\u00b2Z\2\u066e\u0670")
        buf.write(u"\5\u00d6l\2\u066f\u066e\3\2\2\2\u066f\u0670\3\2\2\2\u0670")
        buf.write(u"\u00d5\3\2\2\2\u0671\u0672\7i\2\2\u0672\u0673\5\u0126")
        buf.write(u"\u0094\2\u0673\u0674\7\r\2\2\u0674\u0679\5\u00b2Z\2\u0675")
        buf.write(u"\u0676\7\21\2\2\u0676\u0678\5\u00b2Z\2\u0677\u0675\3")
        buf.write(u"\2\2\2\u0678\u067b\3\2\2\2\u0679\u0677\3\2\2\2\u0679")
        buf.write(u"\u067a\3\2\2\2\u067a\u00d7\3\2\2\2\u067b\u0679\3\2\2")
        buf.write(u"\2\u067c\u067e\5\u00b2Z\2\u067d\u067f\5\u00dan\2\u067e")
        buf.write(u"\u067d\3\2\2\2\u067e\u067f\3\2\2\2\u067f\u00d9\3\2\2")
        buf.write(u"\2\u0680\u0681\7i\2\2\u0681\u0682\5\u0126\u0094\2\u0682")
        buf.write(u"\u0684\7\r\2\2\u0683\u0685\7!\2\2\u0684\u0683\3\2\2\2")
        buf.write(u"\u0684\u0685\3\2\2\2\u0685\u0686\3\2\2\2\u0686\u068b")
        buf.write(u"\5\u0152\u00aa\2\u0687\u0688\7!\2\2\u0688\u068a\5\u0152")
        buf.write(u"\u00aa\2\u0689\u0687\3\2\2\2\u068a\u068d\3\2\2\2\u068b")
        buf.write(u"\u0689\3\2\2\2\u068b\u068c\3\2\2\2\u068c\u0690\3\2\2")
        buf.write(u"\2\u068d\u068b\3\2\2\2\u068e\u068f\7\21\2\2\u068f\u0691")
        buf.write(u"\5\u0152\u00aa\2\u0690\u068e\3\2\2\2\u0690\u0691\3\2")
        buf.write(u"\2\2\u0691\u00db\3\2\2\2\u0692\u0697\5\u00b4[\2\u0693")
        buf.write(u"\u0694\7\17\2\2\u0694\u0696\5\u00b4[\2\u0695\u0693\3")
        buf.write(u"\2\2\2\u0696\u0699\3\2\2\2\u0697\u0695\3\2\2\2\u0697")
        buf.write(u"\u0698\3\2\2\2\u0698\u00dd\3\2\2\2\u0699\u0697\3\2\2")
        buf.write(u"\2\u069a\u069f\5\u00b6\\\2\u069b\u069c\7\17\2\2\u069c")
        buf.write(u"\u069e\5\u00b6\\\2\u069d\u069b\3\2\2\2\u069e\u06a1\3")
        buf.write(u"\2\2\2\u069f\u069d\3\2\2\2\u069f\u06a0\3\2\2\2\u06a0")
        buf.write(u"\u00df\3\2\2\2\u06a1\u069f\3\2\2\2\u06a2\u06a7\5&\24")
        buf.write(u"\2\u06a3\u06a7\5(\25\2\u06a4\u06a7\5*\26\2\u06a5\u06a7")
        buf.write(u"\5,\27\2\u06a6\u06a2\3\2\2\2\u06a6\u06a3\3\2\2\2\u06a6")
        buf.write(u"\u06a4\3\2\2\2\u06a6\u06a5\3\2\2\2\u06a7\u00e1\3\2\2")
        buf.write(u"\2\u06a8\u06a9\7\6\2\2\u06a9\u00e3\3\2\2\2\u06aa\u06b0")
        buf.write(u"\5\u00e6t\2\u06ab\u06ac\5\u0138\u009d\2\u06ac\u06ad\5")
        buf.write(u"\u00e6t\2\u06ad\u06af\3\2\2\2\u06ae\u06ab\3\2\2\2\u06af")
        buf.write(u"\u06b2\3\2\2\2\u06b0\u06ae\3\2\2\2\u06b0\u06b1\3\2\2")
        buf.write(u"\2\u06b1\u00e5\3\2\2\2\u06b2\u06b0\3\2\2\2\u06b3\u06b4")
        buf.write(u"\7\7\2\2\u06b4\u06be\5\u016e\u00b8\2\u06b5\u06b6\7\b")
        buf.write(u"\2\2\u06b6\u06be\5\u018a\u00c6\2\u06b7\u06b8\7\t\2\2")
        buf.write(u"\u06b8\u06be\5\u00e8u\2\u06b9\u06ba\7\n\2\2\u06ba\u06be")
        buf.write(u"\5\u00e8u\2\u06bb\u06bc\7\13\2\2\u06bc\u06be\5\u00ea")
        buf.write(u"v\2\u06bd\u06b3\3\2\2\2\u06bd\u06b5\3\2\2\2\u06bd\u06b7")
        buf.write(u"\3\2\2\2\u06bd\u06b9\3\2\2\2\u06bd\u06bb\3\2\2\2\u06be")
        buf.write(u"\u00e7\3\2\2\2\u06bf\u06c1\5\u0154\u00ab\2\u06c0\u06c2")
        buf.write(u"\7\16\2\2\u06c1\u06c0\3\2\2\2\u06c1\u06c2\3\2\2\2\u06c2")
        buf.write(u"\u06c4\3\2\2\2\u06c3\u06c5\5\u00d6l\2\u06c4\u06c3\3\2")
        buf.write(u"\2\2\u06c4\u06c5\3\2\2\2\u06c5\u00e9\3\2\2\2\u06c6\u06c8")
        buf.write(u"\5\u013a\u009e\2\u06c7\u06c9\7\16\2\2\u06c8\u06c7\3\2")
        buf.write(u"\2\2\u06c8\u06c9\3\2\2\2\u06c9\u06cb\3\2\2\2\u06ca\u06cc")
        buf.write(u"\5\u00dan\2\u06cb\u06ca\3\2\2\2\u06cb\u06cc\3\2\2\2\u06cc")
        buf.write(u"\u00eb\3\2\2\2\u06cd\u06d3\5\64\33\2\u06ce\u06cf\5\u0138")
        buf.write(u"\u009d\2\u06cf\u06d0\5\64\33\2\u06d0\u06d2\3\2\2\2\u06d1")
        buf.write(u"\u06ce\3\2\2\2\u06d2\u06d5\3\2\2\2\u06d3\u06d1\3\2\2")
        buf.write(u"\2\u06d3\u06d4\3\2\2\2\u06d4\u00ed\3\2\2\2\u06d5\u06d3")
        buf.write(u"\3\2\2\2\u06d6\u06dc\5.\30\2\u06d7\u06d8\5\u0138\u009d")
        buf.write(u"\2\u06d8\u06d9\5.\30\2\u06d9\u06db\3\2\2\2\u06da\u06d7")
        buf.write(u"\3\2\2\2\u06db\u06de\3\2\2\2\u06dc\u06da\3\2\2\2\u06dc")
        buf.write(u"\u06dd\3\2\2\2\u06dd\u00ef\3\2\2\2\u06de\u06dc\3\2\2")
        buf.write(u"\2\u06df\u06e5\5@!\2\u06e0\u06e1\5\u0138\u009d\2\u06e1")
        buf.write(u"\u06e2\5@!\2\u06e2\u06e4\3\2\2\2\u06e3\u06e0\3\2\2\2")
        buf.write(u"\u06e4\u06e7\3\2\2\2\u06e5\u06e3\3\2\2\2\u06e5\u06e6")
        buf.write(u"\3\2\2\2\u06e6\u00f1\3\2\2\2\u06e7\u06e5\3\2\2\2\u06e8")
        buf.write(u"\u06ee\5P)\2\u06e9\u06ea\5\u0138\u009d\2\u06ea\u06eb")
        buf.write(u"\5P)\2\u06eb\u06ed\3\2\2\2\u06ec\u06e9\3\2\2\2\u06ed")
        buf.write(u"\u06f0\3\2\2\2\u06ee\u06ec\3\2\2\2\u06ee\u06ef\3\2\2")
        buf.write(u"\2\u06ef\u00f3\3\2\2\2\u06f0\u06ee\3\2\2\2\u06f1\u06f2")
        buf.write(u"\7\24\2\2\u06f2\u06f3\5\u00f6|\2\u06f3\u06f4\7\20\2\2")
        buf.write(u"\u06f4\u06f5\5\u00f6|\2\u06f5\u06f6\7\25\2\2\u06f6\u0700")
        buf.write(u"\3\2\2\2\u06f7\u06f8\7\24\2\2\u06f8\u06f9\5\u00f8}\2")
        buf.write(u"\u06f9\u06fa\7\25\2\2\u06fa\u0700\3\2\2\2\u06fb\u06fc")
        buf.write(u"\7&\2\2\u06fc\u06fd\5\u00f8}\2\u06fd\u06fe\7$\2\2\u06fe")
        buf.write(u"\u0700\3\2\2\2\u06ff\u06f1\3\2\2\2\u06ff\u06f7\3\2\2")
        buf.write(u"\2\u06ff\u06fb\3\2\2\2\u0700\u00f5\3\2\2\2\u0701\u0711")
        buf.write(u"\7\u009e\2\2\u0702\u0711\7\u009f\2\2\u0703\u0711\7\u00a7")
        buf.write(u"\2\2\u0704\u0711\7\u00a8\2\2\u0705\u0711\7\u009d\2\2")
        buf.write(u"\u0706\u0711\7\u00ac\2\2\u0707\u0711\7\u00ab\2\2\u0708")
        buf.write(u"\u0711\7\u00a5\2\2\u0709\u0711\7\u00a9\2\2\u070a\u0711")
        buf.write(u"\7\u00aa\2\2\u070b\u0711\7\u009c\2\2\u070c\u0711\7\u00ad")
        buf.write(u"\2\2\u070d\u0711\7\u00ae\2\2\u070e\u0711\7\u00a6\2\2")
        buf.write(u"\u070f\u0711\5\u0084C\2\u0710\u0701\3\2\2\2\u0710\u0702")
        buf.write(u"\3\2\2\2\u0710\u0703\3\2\2\2\u0710\u0704\3\2\2\2\u0710")
        buf.write(u"\u0705\3\2\2\2\u0710\u0706\3\2\2\2\u0710\u0707\3\2\2")
        buf.write(u"\2\u0710\u0708\3\2\2\2\u0710\u0709\3\2\2\2\u0710\u070a")
        buf.write(u"\3\2\2\2\u0710\u070b\3\2\2\2\u0710\u070c\3\2\2\2\u0710")
        buf.write(u"\u070d\3\2\2\2\u0710\u070e\3\2\2\2\u0710\u070f\3\2\2")
        buf.write(u"\2\u0711\u00f7\3\2\2\2\u0712\u0717\5\u00f6|\2\u0713\u0714")
        buf.write(u"\7\17\2\2\u0714\u0716\5\u00f6|\2\u0715\u0713\3\2\2\2")
        buf.write(u"\u0716\u0719\3\2\2\2\u0717\u0715\3\2\2\2\u0717\u0718")
        buf.write(u"\3\2\2\2\u0718\u00f9\3\2\2\2\u0719\u0717\3\2\2\2\u071a")
        buf.write(u"\u071f\5\u00fe\u0080\2\u071b\u071f\5\u0100\u0081\2\u071c")
        buf.write(u"\u071f\5\u00b2Z\2\u071d\u071f\5\u00fc\177\2\u071e\u071a")
        buf.write(u"\3\2\2\2\u071e\u071b\3\2\2\2\u071e\u071c\3\2\2\2\u071e")
        buf.write(u"\u071d\3\2\2\2\u071f\u00fb\3\2\2\2\u0720\u0721\t\4\2")
        buf.write(u"\2\u0721\u00fd\3\2\2\2\u0722\u0723\7\22\2\2\u0723\u0724")
        buf.write(u"\5^\60\2\u0724\u0725\7\23\2\2\u0725\u00ff\3\2\2\2\u0726")
        buf.write(u"\u0729\5\u00f6|\2\u0727\u0729\5\u0102\u0082\2\u0728\u0726")
        buf.write(u"\3\2\2\2\u0728\u0727\3\2\2\2\u0729\u0101\3\2\2\2\u072a")
        buf.write(u"\u0730\5\u009eP\2\u072b\u0730\5\u0098M\2\u072c\u0730")
        buf.write(u"\5\u009aN\2\u072d\u0730\5\u0106\u0084\2\u072e\u0730\5")
        buf.write(u"\u0104\u0083\2\u072f\u072a\3\2\2\2\u072f\u072b\3\2\2")
        buf.write(u"\2\u072f\u072c\3\2\2\2\u072f\u072d\3\2\2\2\u072f\u072e")
        buf.write(u"\3\2\2\2\u0730\u0103\3\2\2\2\u0731\u0733\7u\2\2\u0732")
        buf.write(u"\u0731\3\2\2\2\u0732\u0733\3\2\2\2\u0733\u0734\3\2\2")
        buf.write(u"\2\u0734\u0736\7\22\2\2\u0735\u0737\5\u0108\u0085\2\u0736")
        buf.write(u"\u0735\3\2\2\2\u0736\u0737\3\2\2\2\u0737\u0738\3\2\2")
        buf.write(u"\2\u0738\u0739\7\23\2\2\u0739\u0105\3\2\2\2\u073a\u073c")
        buf.write(u"\7u\2\2\u073b\u073a\3\2\2\2\u073b\u073c\3\2\2\2\u073c")
        buf.write(u"\u073d\3\2\2\2\u073d\u073f\7\26\2\2\u073e\u0740\5\u010a")
        buf.write(u"\u0086\2\u073f\u073e\3\2\2\2\u073f\u0740\3\2\2\2\u0740")
        buf.write(u"\u0741\3\2\2\2\u0741\u0742\7\27\2\2\u0742\u0107\3\2\2")
        buf.write(u"\2\u0743\u0744\5^\60\2\u0744\u074d\7\17\2\2\u0745\u074a")
        buf.write(u"\5^\60\2\u0746\u0747\7\17\2\2\u0747\u0749\5^\60\2\u0748")
        buf.write(u"\u0746\3\2\2\2\u0749\u074c\3\2\2\2\u074a\u0748\3\2\2")
        buf.write(u"\2\u074a\u074b\3\2\2\2\u074b\u074e\3\2\2\2\u074c\u074a")
        buf.write(u"\3\2\2\2\u074d\u0745\3\2\2\2\u074d\u074e\3\2\2\2\u074e")
        buf.write(u"\u0109\3\2\2\2\u074f\u0754\5\u010c\u0087\2\u0750\u0751")
        buf.write(u"\7\17\2\2\u0751\u0753\5\u010c\u0087\2\u0752\u0750\3\2")
        buf.write(u"\2\2\u0753\u0756\3\2\2\2\u0754\u0752\3\2\2\2\u0754\u0755")
        buf.write(u"\3\2\2\2\u0755\u010b\3\2\2\2\u0756\u0754\3\2\2\2\u0757")
        buf.write(u"\u0758\5^\60\2\u0758\u0759\7\r\2\2\u0759\u075a\5^\60")
        buf.write(u"\2\u075a\u010d\3\2\2\2\u075b\u075c\5^\60\2\u075c\u075d")
        buf.write(u"\7\r\2\2\u075d\u075e\5^\60\2\u075e\u0765\3\2\2\2\u075f")
        buf.write(u"\u0760\5^\60\2\u0760\u0761\7\r\2\2\u0761\u0765\3\2\2")
        buf.write(u"\2\u0762\u0763\7\r\2\2\u0763\u0765\5^\60\2\u0764\u075b")
        buf.write(u"\3\2\2\2\u0764\u075f\3\2\2\2\u0764\u0762\3\2\2\2\u0765")
        buf.write(u"\u010f\3\2\2\2\u0766\u0767\5\u00b4[\2\u0767\u0768\5\u012c")
        buf.write(u"\u0097\2\u0768\u0769\5^\60\2\u0769\u0111\3\2\2\2\u076a")
        buf.write(u"\u076b\b\u008a\1\2\u076b\u076c\5\u00b4[\2\u076c\u0771")
        buf.write(u"\3\2\2\2\u076d\u076e\f\3\2\2\u076e\u0770\5\u0080A\2\u076f")
        buf.write(u"\u076d\3\2\2\2\u0770\u0773\3\2\2\2\u0771\u076f\3\2\2")
        buf.write(u"\2\u0771\u0772\3\2\2\2\u0772\u0113\3\2\2\2\u0773\u0771")
        buf.write(u"\3\2\2\2\u0774\u0775\6\u008b/\3\u0775\u0776\7\u00a2\2")
        buf.write(u"\2\u0776\u0779\5\u00c6d\2\u0777\u0779\5^\60\2\u0778\u0774")
        buf.write(u"\3\2\2\2\u0778\u0777\3\2\2\2\u0779\u0115\3\2\2\2\u077a")
        buf.write(u"\u077b\7\u0084\2\2\u077b\u077c\7C\2\2\u077c\u077d\7i")
        buf.write(u"\2\2\u077d\u077e\5^\60\2\u077e\u0117\3\2\2\2\u077f\u0780")
        buf.write(u"\7\u0084\2\2\u0780\u0781\7|\2\2\u0781\u0782\7i\2\2\u0782")
        buf.write(u"\u0783\5^\60\2\u0783\u0119\3\2\2\2\u0784\u0789\5\u011c")
        buf.write(u"\u008f\2\u0785\u0786\7\17\2\2\u0786\u0788\5\u011c\u008f")
        buf.write(u"\2\u0787\u0785\3\2\2\2\u0788\u078b\3\2\2\2\u0789\u0787")
        buf.write(u"\3\2\2\2\u0789\u078a\3\2\2\2\u078a\u011b\3\2\2\2\u078b")
        buf.write(u"\u0789\3\2\2\2\u078c\u0791\5\u00b4[\2\u078d\u078e\7\21")
        buf.write(u"\2\2\u078e\u0790\5\u00b4[\2\u078f\u078d\3\2\2\2\u0790")
        buf.write(u"\u0793\3\2\2\2\u0791\u078f\3\2\2\2\u0791\u0792\3\2\2")
        buf.write(u"\2\u0792\u0795\3\2\2\2\u0793\u0791\3\2\2\2\u0794\u0796")
        buf.write(u"\t\5\2\2\u0795\u0794\3\2\2\2\u0795\u0796\3\2\2\2\u0796")
        buf.write(u"\u011d\3\2\2\2\u0797\u079e\7\36\2\2\u0798\u079e\7\37")
        buf.write(u"\2\2\u0799\u079e\5\u012e\u0098\2\u079a\u079e\5\u0130")
        buf.write(u"\u0099\2\u079b\u079e\5\u0132\u009a\2\u079c\u079e\5\u0134")
        buf.write(u"\u009b\2\u079d\u0797\3\2\2\2\u079d\u0798\3\2\2\2\u079d")
        buf.write(u"\u0799\3\2\2\2\u079d\u079a\3\2\2\2\u079d\u079b\3\2\2")
        buf.write(u"\2\u079d\u079c\3\2\2\2\u079e\u011f\3\2\2\2\u079f\u07a0")
        buf.write(u"\t\6\2\2\u07a0\u0121\3\2\2\2\u07a1\u07a2\7\u00a2\2\2")
        buf.write(u"\u07a2\u07a3\6\u0092\60\3\u07a3\u0123\3\2\2\2\u07a4\u07a5")
        buf.write(u"\7\u00a2\2\2\u07a5\u07a6\6\u0093\61\3\u07a6\u0125\3\2")
        buf.write(u"\2\2\u07a7\u07a8\7\u00a2\2\2\u07a8\u07a9\6\u0094\62\3")
        buf.write(u"\u07a9\u0127\3\2\2\2\u07aa\u07ab\7\u00a2\2\2\u07ab\u07ac")
        buf.write(u"\6\u0095\63\3\u07ac\u0129\3\2\2\2\u07ad\u07ae\7\u00a2")
        buf.write(u"\2\2\u07ae\u07af\6\u0096\64\3\u07af\u012b\3\2\2\2\u07b0")
        buf.write(u"\u07b1\7)\2\2\u07b1\u012d\3\2\2\2\u07b2\u07b3\7 \2\2")
        buf.write(u"\u07b3\u012f\3\2\2\2\u07b4\u07b5\7!\2\2\u07b5\u0131\3")
        buf.write(u"\2\2\2\u07b6\u07b7\7\"\2\2\u07b7\u0133\3\2\2\2\u07b8")
        buf.write(u"\u07b9\t\7\2\2\u07b9\u0135\3\2\2\2\u07ba\u07bb\3\2\2")
        buf.write(u"\2\u07bb\u0137\3\2\2\2\u07bc\u07bd\3\2\2\2\u07bd\u0139")
        buf.write(u"\3\2\2\2\u07be\u07bf\7\u0087\2\2\u07bf\u07c0\5\u013c")
        buf.write(u"\u009f\2\u07c0\u07c1\7\16\2\2\u07c1\u07c6\3\2\2\2\u07c2")
        buf.write(u"\u07c3\5\u013c\u009f\2\u07c3\u07c4\7\16\2\2\u07c4\u07c6")
        buf.write(u"\3\2\2\2\u07c5\u07be\3\2\2\2\u07c5\u07c2\3\2\2\2\u07c6")
        buf.write(u"\u013b\3\2\2\2\u07c7\u07c8\b\u009f\1\2\u07c8\u07c9\5")
        buf.write(u"\u013e\u00a0\2\u07c9\u07ce\3\2\2\2\u07ca\u07cb\f\3\2")
        buf.write(u"\2\u07cb\u07cd\5\u0144\u00a3\2\u07cc\u07ca\3\2\2\2\u07cd")
        buf.write(u"\u07d0\3\2\2\2\u07ce\u07cc\3\2\2\2\u07ce\u07cf\3\2\2")
        buf.write(u"\2\u07cf\u013d\3\2\2\2\u07d0\u07ce\3\2\2\2\u07d1\u07d9")
        buf.write(u"\5\u0140\u00a1\2\u07d2\u07d9\5\u0142\u00a2\2\u07d3\u07d9")
        buf.write(u"\5\u014c\u00a7\2\u07d4\u07d9\5\u014e\u00a8\2\u07d5\u07d9")
        buf.write(u"\5\u0150\u00a9\2\u07d6\u07d9\5\u0146\u00a4\2\u07d7\u07d9")
        buf.write(u"\5\u014a\u00a6\2\u07d8\u07d1\3\2\2\2\u07d8\u07d2\3\2")
        buf.write(u"\2\2\u07d8\u07d3\3\2\2\2\u07d8\u07d4\3\2\2\2\u07d8\u07d5")
        buf.write(u"\3\2\2\2\u07d8\u07d6\3\2\2\2\u07d8\u07d7\3\2\2\2\u07d9")
        buf.write(u"\u013f\3\2\2\2\u07da\u07db\5\u00fc\177\2\u07db\u0141")
        buf.write(u"\3\2\2\2\u07dc\u07dd\5\u0122\u0092\2\u07dd\u07de\5\u0146")
        buf.write(u"\u00a4\2\u07de\u0143\3\2\2\2\u07df\u07e0\7\21\2\2\u07e0")
        buf.write(u"\u07e5\5\u0146\u00a4\2\u07e1\u07e2\7\21\2\2\u07e2\u07e5")
        buf.write(u"\5\u0152\u00aa\2\u07e3\u07e5\5\u014a\u00a6\2\u07e4\u07df")
        buf.write(u"\3\2\2\2\u07e4\u07e1\3\2\2\2\u07e4\u07e3\3\2\2\2\u07e5")
        buf.write(u"\u0145\3\2\2\2\u07e6\u07e7\5\u0152\u00aa\2\u07e7\u07e9")
        buf.write(u"\7\22\2\2\u07e8\u07ea\5\u0148\u00a5\2\u07e9\u07e8\3\2")
        buf.write(u"\2\2\u07e9\u07ea\3\2\2\2\u07ea\u07eb\3\2\2\2\u07eb\u07ec")
        buf.write(u"\7\23\2\2\u07ec\u0147\3\2\2\2\u07ed\u07ee\b\u00a5\1\2")
        buf.write(u"\u07ee\u07ef\5\u013c\u009f\2\u07ef\u07f5\3\2\2\2\u07f0")
        buf.write(u"\u07f1\f\3\2\2\u07f1\u07f2\7\17\2\2\u07f2\u07f4\5\u013c")
        buf.write(u"\u009f\2\u07f3\u07f0\3\2\2\2\u07f4\u07f7\3\2\2\2\u07f5")
        buf.write(u"\u07f3\3\2\2\2\u07f5\u07f6\3\2\2\2\u07f6\u0149\3\2\2")
        buf.write(u"\2\u07f7\u07f5\3\2\2\2\u07f8\u07f9\7\24\2\2\u07f9\u07fa")
        buf.write(u"\5\u013c\u009f\2\u07fa\u07fb\7\25\2\2\u07fb\u014b\3\2")
        buf.write(u"\2\2\u07fc\u07fd\7\22\2\2\u07fd\u07fe\5\u013c\u009f\2")
        buf.write(u"\u07fe\u07ff\7\23\2\2\u07ff\u014d\3\2\2\2\u0800\u0801")
        buf.write(u"\5\u0152\u00aa\2\u0801\u014f\3\2\2\2\u0802\u0808\7\u00a7")
        buf.write(u"\2\2\u0803\u0808\7\u00a9\2\2\u0804\u0808\7\u00a5\2\2")
        buf.write(u"\u0805\u0808\7\u009c\2\2\u0806\u0808\7\u009d\2\2\u0807")
        buf.write(u"\u0802\3\2\2\2\u0807\u0803\3\2\2\2\u0807\u0804\3\2\2")
        buf.write(u"\2\u0807\u0805\3\2\2\2\u0807\u0806\3\2\2\2\u0808\u0151")
        buf.write(u"\3\2\2\2\u0809\u080a\t\b\2\2\u080a\u0153\3\2\2\2\u080b")
        buf.write(u"\u080c\7\u0087\2\2\u080c\u080f\5\u0156\u00ac\2\u080d")
        buf.write(u"\u080f\5\u0156\u00ac\2\u080e\u080b\3\2\2\2\u080e\u080d")
        buf.write(u"\3\2\2\2\u080f\u0155\3\2\2\2\u0810\u0811\b\u00ac\1\2")
        buf.write(u"\u0811\u0812\5\u0158\u00ad\2\u0812\u0817\3\2\2\2\u0813")
        buf.write(u"\u0814\f\3\2\2\u0814\u0816\5\u015c\u00af\2\u0815\u0813")
        buf.write(u"\3\2\2\2\u0816\u0819\3\2\2\2\u0817\u0815\3\2\2\2\u0817")
        buf.write(u"\u0818\3\2\2\2\u0818\u0157\3\2\2\2\u0819\u0817\3\2\2")
        buf.write(u"\2\u081a\u0820\5\u015a\u00ae\2\u081b\u0820\5\u0166\u00b4")
        buf.write(u"\2\u081c\u0820\5\u0168\u00b5\2\u081d\u0820\5\u016a\u00b6")
        buf.write(u"\2\u081e\u0820\5\u015e\u00b0\2\u081f\u081a\3\2\2\2\u081f")
        buf.write(u"\u081b\3\2\2\2\u081f\u081c\3\2\2\2\u081f\u081d\3\2\2")
        buf.write(u"\2\u081f\u081e\3\2\2\2\u0820\u0159\3\2\2\2\u0821\u0822")
        buf.write(u"\5\u00fc\177\2\u0822\u015b\3\2\2\2\u0823\u0824\7\21\2")
        buf.write(u"\2\u0824\u082a\5\u015e\u00b0\2\u0825\u0826\7\24\2\2\u0826")
        buf.write(u"\u0827\5\u0156\u00ac\2\u0827\u0828\7\25\2\2\u0828\u082a")
        buf.write(u"\3\2\2\2\u0829\u0823\3\2\2\2\u0829\u0825\3\2\2\2\u082a")
        buf.write(u"\u015d\3\2\2\2\u082b\u082c\5\u016c\u00b7\2\u082c\u082e")
        buf.write(u"\7\22\2\2\u082d\u082f\5\u0160\u00b1\2\u082e\u082d\3\2")
        buf.write(u"\2\2\u082e\u082f\3\2\2\2\u082f\u0830\3\2\2\2\u0830\u0831")
        buf.write(u"\7\23\2\2\u0831\u015f\3\2\2\2\u0832\u0839\5\u0162\u00b2")
        buf.write(u"\2\u0833\u0839\5\u0164\u00b3\2\u0834\u0835\5\u0162\u00b2")
        buf.write(u"\2\u0835\u0836\7\17\2\2\u0836\u0837\5\u0164\u00b3\2\u0837")
        buf.write(u"\u0839\3\2\2\2\u0838\u0832\3\2\2\2\u0838\u0833\3\2\2")
        buf.write(u"\2\u0838\u0834\3\2\2\2\u0839\u0161\3\2\2\2\u083a\u083b")
        buf.write(u"\b\u00b2\1\2\u083b\u083c\5\u0156\u00ac\2\u083c\u0842")
        buf.write(u"\3\2\2\2\u083d\u083e\f\3\2\2\u083e\u083f\7\17\2\2\u083f")
        buf.write(u"\u0841\5\u0156\u00ac\2\u0840\u083d\3\2\2\2\u0841\u0844")
        buf.write(u"\3\2\2\2\u0842\u0840\3\2\2\2\u0842\u0843\3\2\2\2\u0843")
        buf.write(u"\u0163\3\2\2\2\u0844\u0842\3\2\2\2\u0845\u0846\b\u00b3")
        buf.write(u"\1\2\u0846\u0847\5\u016c\u00b7\2\u0847\u0848\7)\2\2\u0848")
        buf.write(u"\u0849\5\u0156\u00ac\2\u0849\u0852\3\2\2\2\u084a\u084b")
        buf.write(u"\f\3\2\2\u084b\u084c\7\17\2\2\u084c\u084d\5\u016c\u00b7")
        buf.write(u"\2\u084d\u084e\7)\2\2\u084e\u084f\5\u0156\u00ac\2\u084f")
        buf.write(u"\u0851\3\2\2\2\u0850\u084a\3\2\2\2\u0851\u0854\3\2\2")
        buf.write(u"\2\u0852\u0850\3\2\2\2\u0852\u0853\3\2\2\2\u0853\u0165")
        buf.write(u"\3\2\2\2\u0854\u0852\3\2\2\2\u0855\u0856\7\22\2\2\u0856")
        buf.write(u"\u0857\5\u0156\u00ac\2\u0857\u0858\7\23\2\2\u0858\u0167")
        buf.write(u"\3\2\2\2\u0859\u085a\b\u00b5\1\2\u085a\u085d\7\u00a4")
        buf.write(u"\2\2\u085b\u085d\5\u016c\u00b7\2\u085c\u0859\3\2\2\2")
        buf.write(u"\u085c\u085b\3\2\2\2\u085d\u0863\3\2\2\2\u085e\u085f")
        buf.write(u"\f\3\2\2\u085f\u0860\7\21\2\2\u0860\u0862\5\u016c\u00b7")
        buf.write(u"\2\u0861\u085e\3\2\2\2\u0862\u0865\3\2\2\2\u0863\u0861")
        buf.write(u"\3\2\2\2\u0863\u0864\3\2\2\2\u0864\u0169\3\2\2\2\u0865")
        buf.write(u"\u0863\3\2\2\2\u0866\u086c\7\u00a7\2\2\u0867\u086c\7")
        buf.write(u"\u00a9\2\2\u0868\u086c\7\u00a5\2\2\u0869\u086c\7\u009c")
        buf.write(u"\2\2\u086a\u086c\7\u009d\2\2\u086b\u0866\3\2\2\2\u086b")
        buf.write(u"\u0867\3\2\2\2\u086b\u0868\3\2\2\2\u086b\u0869\3\2\2")
        buf.write(u"\2\u086b\u086a\3\2\2\2\u086c\u016b\3\2\2\2\u086d\u086e")
        buf.write(u"\t\t\2\2\u086e\u016d\3\2\2\2\u086f\u0870\7\u0087\2\2")
        buf.write(u"\u0870\u0871\5\u0170\u00b9\2\u0871\u0872\7\16\2\2\u0872")
        buf.write(u"\u0877\3\2\2\2\u0873\u0874\5\u0170\u00b9\2\u0874\u0875")
        buf.write(u"\7\16\2\2\u0875\u0877\3\2\2\2\u0876\u086f\3\2\2\2\u0876")
        buf.write(u"\u0873\3\2\2\2\u0877\u016f\3\2\2\2\u0878\u0879\b\u00b9")
        buf.write(u"\1\2\u0879\u087a\5\u0172\u00ba\2\u087a\u087f\3\2\2\2")
        buf.write(u"\u087b\u087c\f\3\2\2\u087c\u087e\5\u0178\u00bd\2\u087d")
        buf.write(u"\u087b\3\2\2\2\u087e\u0881\3\2\2\2\u087f\u087d\3\2\2")
        buf.write(u"\2\u087f\u0880\3\2\2\2\u0880\u0171\3\2\2\2\u0881\u087f")
        buf.write(u"\3\2\2\2\u0882\u0888\5\u0174\u00bb\2\u0883\u0888\5\u0176")
        buf.write(u"\u00bc\2\u0884\u0888\5\u0180\u00c1\2\u0885\u0888\5\u0182")
        buf.write(u"\u00c2\2\u0886\u0888\5\u0186\u00c4\2\u0887\u0882\3\2")
        buf.write(u"\2\2\u0887\u0883\3\2\2\2\u0887\u0884\3\2\2\2\u0887\u0885")
        buf.write(u"\3\2\2\2\u0887\u0886\3\2\2\2\u0888\u0173\3\2\2\2\u0889")
        buf.write(u"\u088a\5\u00fc\177\2\u088a\u0175\3\2\2\2\u088b\u088c")
        buf.write(u"\5\u0122\u0092\2\u088c\u088d\5\u017a\u00be\2\u088d\u0177")
        buf.write(u"\3\2\2\2\u088e\u088f\7\21\2\2\u088f\u0892\5\u017a\u00be")
        buf.write(u"\2\u0890\u0892\5\u017e\u00c0\2\u0891\u088e\3\2\2\2\u0891")
        buf.write(u"\u0890\3\2\2\2\u0892\u0179\3\2\2\2\u0893\u0894\5\u0188")
        buf.write(u"\u00c5\2\u0894\u0896\7\22\2\2\u0895\u0897\5\u017c\u00bf")
        buf.write(u"\2\u0896\u0895\3\2\2\2\u0896\u0897\3\2\2\2\u0897\u0898")
        buf.write(u"\3\2\2\2\u0898\u0899\7\23\2\2\u0899\u017b\3\2\2\2\u089a")
        buf.write(u"\u089b\b\u00bf\1\2\u089b\u089c\5\u0170\u00b9\2\u089c")
        buf.write(u"\u08a2\3\2\2\2\u089d\u089e\f\3\2\2\u089e\u089f\7\17\2")
        buf.write(u"\2\u089f\u08a1\5\u0170\u00b9\2\u08a0\u089d\3\2\2\2\u08a1")
        buf.write(u"\u08a4\3\2\2\2\u08a2\u08a0\3\2\2\2\u08a2\u08a3\3\2\2")
        buf.write(u"\2\u08a3\u017d\3\2\2\2\u08a4\u08a2\3\2\2\2\u08a5\u08a6")
        buf.write(u"\7\24\2\2\u08a6\u08a7\5\u0170\u00b9\2\u08a7\u08a8\7\25")
        buf.write(u"\2\2\u08a8\u017f\3\2\2\2\u08a9\u08aa\7\22\2\2\u08aa\u08ab")
        buf.write(u"\5\u0170\u00b9\2\u08ab\u08ac\7\23\2\2\u08ac\u0181\3\2")
        buf.write(u"\2\2\u08ad\u08ae\b\u00c2\1\2\u08ae\u08af\5\u0188\u00c5")
        buf.write(u"\2\u08af\u08b5\3\2\2\2\u08b0\u08b1\f\3\2\2\u08b1\u08b2")
        buf.write(u"\7\21\2\2\u08b2\u08b4\5\u0188\u00c5\2\u08b3\u08b0\3\2")
        buf.write(u"\2\2\u08b4\u08b7\3\2\2\2\u08b5\u08b3\3\2\2\2\u08b5\u08b6")
        buf.write(u"\3\2\2\2\u08b6\u0183\3\2\2\2\u08b7\u08b5\3\2\2\2\u08b8")
        buf.write(u"\u08b9\b\u00c3\1\2\u08b9\u08ba\5\u0182\u00c2\2\u08ba")
        buf.write(u"\u08bf\3\2\2\2\u08bb\u08bc\f\3\2\2\u08bc\u08be\7\u00a4")
        buf.write(u"\2\2\u08bd\u08bb\3\2\2\2\u08be\u08c1\3\2\2\2\u08bf\u08bd")
        buf.write(u"\3\2\2\2\u08bf\u08c0\3\2\2\2\u08c0\u0185\3\2\2\2\u08c1")
        buf.write(u"\u08bf\3\2\2\2\u08c2\u08c8\7\u00a7\2\2\u08c3\u08c8\7")
        buf.write(u"\u00a9\2\2\u08c4\u08c8\7\u00a5\2\2\u08c5\u08c8\7\u009c")
        buf.write(u"\2\2\u08c6\u08c8\7\u009d\2\2\u08c7\u08c2\3\2\2\2\u08c7")
        buf.write(u"\u08c3\3\2\2\2\u08c7\u08c4\3\2\2\2\u08c7\u08c5\3\2\2")
        buf.write(u"\2\u08c7\u08c6\3\2\2\2\u08c8\u0187\3\2\2\2\u08c9\u08ca")
        buf.write(u"\t\n\2\2\u08ca\u0189\3\2\2\2\u08cb\u08cc\7\u0087\2\2")
        buf.write(u"\u08cc\u08cd\5\u018c\u00c7\2\u08cd\u08ce\7\16\2\2\u08ce")
        buf.write(u"\u08d3\3\2\2\2\u08cf\u08d0\5\u018c\u00c7\2\u08d0\u08d1")
        buf.write(u"\7\16\2\2\u08d1\u08d3\3\2\2\2\u08d2\u08cb\3\2\2\2\u08d2")
        buf.write(u"\u08cf\3\2\2\2\u08d3\u018b\3\2\2\2\u08d4\u08d5\b\u00c7")
        buf.write(u"\1\2\u08d5\u08d6\5\u018e\u00c8\2\u08d6\u08db\3\2\2\2")
        buf.write(u"\u08d7\u08d8\f\3\2\2\u08d8\u08da\5\u0194\u00cb\2\u08d9")
        buf.write(u"\u08d7\3\2\2\2\u08da\u08dd\3\2\2\2\u08db\u08d9\3\2\2")
        buf.write(u"\2\u08db\u08dc\3\2\2\2\u08dc\u018d\3\2\2\2\u08dd\u08db")
        buf.write(u"\3\2\2\2\u08de\u08e4\5\u0190\u00c9\2\u08df\u08e4\5\u0192")
        buf.write(u"\u00ca\2\u08e0\u08e4\5\u019c\u00cf\2\u08e1\u08e4\5\u019e")
        buf.write(u"\u00d0\2\u08e2\u08e4\5\u01a0\u00d1\2\u08e3\u08de\3\2")
        buf.write(u"\2\2\u08e3\u08df\3\2\2\2\u08e3\u08e0\3\2\2\2\u08e3\u08e1")
        buf.write(u"\3\2\2\2\u08e3\u08e2\3\2\2\2\u08e4\u018f\3\2\2\2\u08e5")
        buf.write(u"\u08e6\5\u00fc\177\2\u08e6\u0191\3\2\2\2\u08e7\u08e8")
        buf.write(u"\5\u0122\u0092\2\u08e8\u08e9\5\u0196\u00cc\2\u08e9\u0193")
        buf.write(u"\3\2\2\2\u08ea\u08eb\7\21\2\2\u08eb\u08ee\5\u0196\u00cc")
        buf.write(u"\2\u08ec\u08ee\5\u019a\u00ce\2\u08ed\u08ea\3\2\2\2\u08ed")
        buf.write(u"\u08ec\3\2\2\2\u08ee\u0195\3\2\2\2\u08ef\u08f0\5\u01a2")
        buf.write(u"\u00d2\2\u08f0\u08f2\7\22\2\2\u08f1\u08f3\5\u0198\u00cd")
        buf.write(u"\2\u08f2\u08f1\3\2\2\2\u08f2\u08f3\3\2\2\2\u08f3\u08f4")
        buf.write(u"\3\2\2\2\u08f4\u08f5\7\23\2\2\u08f5\u0197\3\2\2\2\u08f6")
        buf.write(u"\u08f7\b\u00cd\1\2\u08f7\u08f8\5\u018c\u00c7\2\u08f8")
        buf.write(u"\u08fe\3\2\2\2\u08f9\u08fa\f\3\2\2\u08fa\u08fb\7\17\2")
        buf.write(u"\2\u08fb\u08fd\5\u018c\u00c7\2\u08fc\u08f9\3\2\2\2\u08fd")
        buf.write(u"\u0900\3\2\2\2\u08fe\u08fc\3\2\2\2\u08fe\u08ff\3\2\2")
        buf.write(u"\2\u08ff\u0199\3\2\2\2\u0900\u08fe\3\2\2\2\u0901\u0902")
        buf.write(u"\7\24\2\2\u0902\u0903\5\u018c\u00c7\2\u0903\u0904\7\25")
        buf.write(u"\2\2\u0904\u019b\3\2\2\2\u0905\u0906\7\22\2\2\u0906\u0907")
        buf.write(u"\5\u018c\u00c7\2\u0907\u0908\7\23\2\2\u0908\u019d\3\2")
        buf.write(u"\2\2\u0909\u090a\b\u00d0\1\2\u090a\u090d\7\u00a4\2\2")
        buf.write(u"\u090b\u090d\5\u01a2\u00d2\2\u090c\u0909\3\2\2\2\u090c")
        buf.write(u"\u090b\3\2\2\2\u090d\u0913\3\2\2\2\u090e\u090f\f\3\2")
        buf.write(u"\2\u090f\u0910\7\21\2\2\u0910\u0912\5\u01a2\u00d2\2\u0911")
        buf.write(u"\u090e\3\2\2\2\u0912\u0915\3\2\2\2\u0913\u0911\3\2\2")
        buf.write(u"\2\u0913\u0914\3\2\2\2\u0914\u019f\3\2\2\2\u0915\u0913")
        buf.write(u"\3\2\2\2\u0916\u091c\7\u00a7\2\2\u0917\u091c\7\u00a9")
        buf.write(u"\2\2\u0918\u091c\7\u00a5\2\2\u0919\u091c\7\u009c\2\2")
        buf.write(u"\u091a\u091c\7\u009d\2\2\u091b\u0916\3\2\2\2\u091b\u0917")
        buf.write(u"\3\2\2\2\u091b\u0918\3\2\2\2\u091b\u0919\3\2\2\2\u091b")
        buf.write(u"\u091a\3\2\2\2\u091c\u01a1\3\2\2\2\u091d\u091e\t\13\2")
        buf.write(u"\2\u091e\u01a3\3\2\2\2\u091f\u0922\5\u01a6\u00d4\2\u0920")
        buf.write(u"\u0922\5\u01a8\u00d5\2\u0921\u091f\3\2\2\2\u0921\u0920")
        buf.write(u"\3\2\2\2\u0922\u01a5\3\2\2\2\u0923\u092b\5\u01ae\u00d8")
        buf.write(u"\2\u0924\u0926\5\u01b0\u00d9\2\u0925\u0927\5\u01c2\u00e2")
        buf.write(u"\2\u0926\u0925\3\2\2\2\u0926\u0927\3\2\2\2\u0927\u0928")
        buf.write(u"\3\2\2\2\u0928\u0929\5\u01b2\u00da\2\u0929\u092b\3\2")
        buf.write(u"\2\2\u092a\u0923\3\2\2\2\u092a\u0924\3\2\2\2\u092b\u01a7")
        buf.write(u"\3\2\2\2\u092c\u092e\5\u01aa\u00d6\2\u092d\u092f\5\u01c2")
        buf.write(u"\u00e2\2\u092e\u092d\3\2\2\2\u092e\u092f\3\2\2\2\u092f")
        buf.write(u"\u0930\3\2\2\2\u0930\u0931\5\u01ac\u00d7\2\u0931\u01a9")
        buf.write(u"\3\2\2\2\u0932\u0933\7&\2\2\u0933\u0936\7$\2\2\u0934")
        buf.write(u"\u0936\7(\2\2\u0935\u0932\3\2\2\2\u0935\u0934\3\2\2\2")
        buf.write(u"\u0936\u01ab\3\2\2\2\u0937\u0938\7&\2\2\u0938\u0939\7")
        buf.write(u"!\2\2\u0939\u093a\7$\2\2\u093a\u01ad\3\2\2\2\u093b\u093c")
        buf.write(u"\7&\2\2\u093c\u0940\5\u01b4\u00db\2\u093d\u093f\5\u01be")
        buf.write(u"\u00e0\2\u093e\u093d\3\2\2\2\u093f\u0942\3\2\2\2\u0940")
        buf.write(u"\u093e\3\2\2\2\u0940\u0941\3\2\2\2\u0941\u0943\3\2\2")
        buf.write(u"\2\u0942\u0940\3\2\2\2\u0943\u0944\7!\2\2\u0944\u0945")
        buf.write(u"\7$\2\2\u0945\u01af\3\2\2\2\u0946\u0947\7&\2\2\u0947")
        buf.write(u"\u094b\5\u01b4\u00db\2\u0948\u094a\5\u01be\u00e0\2\u0949")
        buf.write(u"\u0948\3\2\2\2\u094a\u094d\3\2\2\2\u094b\u0949\3\2\2")
        buf.write(u"\2\u094b\u094c\3\2\2\2\u094c\u094e\3\2\2\2\u094d\u094b")
        buf.write(u"\3\2\2\2\u094e\u094f\7$\2\2\u094f\u01b1\3\2\2\2\u0950")
        buf.write(u"\u0951\7&\2\2\u0951\u0952\7!\2\2\u0952\u0953\5\u01b4")
        buf.write(u"\u00db\2\u0953\u0954\7$\2\2\u0954\u01b3\3\2\2\2\u0955")
        buf.write(u"\u095a\5\u01b6\u00dc\2\u0956\u0957\7\21\2\2\u0957\u0959")
        buf.write(u"\5\u01b6\u00dc\2\u0958\u0956\3\2\2\2\u0959\u095c\3\2")
        buf.write(u"\2\2\u095a\u0958\3\2\2\2\u095a\u095b\3\2\2\2\u095b\u01b5")
        buf.write(u"\3\2\2\2\u095c\u095a\3\2\2\2\u095d\u0961\5\u01bc\u00df")
        buf.write(u"\2\u095e\u0960\5\u01b8\u00dd\2\u095f\u095e\3\2\2\2\u0960")
        buf.write(u"\u0963\3\2\2\2\u0961\u095f\3\2\2\2\u0961\u0962\3\2\2")
        buf.write(u"\2\u0962\u01b7\3\2\2\2\u0963\u0961\3\2\2\2\u0964\u0965")
        buf.write(u"\6\u00ddB\3\u0965\u0966\7\37\2\2\u0966\u0967\5\u01ba")
        buf.write(u"\u00de\2\u0967\u01b9\3\2\2\2\u0968\u0969\6\u00deC\3\u0969")
        buf.write(u"\u096a\5\u01bc\u00df\2\u096a\u01bb\3\2\2\2\u096b\u096e")
        buf.write(u"\5\u00b2Z\2\u096c\u096e\5\u0120\u0091\2\u096d\u096b\3")
        buf.write(u"\2\2\2\u096d\u096c\3\2\2\2\u096e\u01bd\3\2\2\2\u096f")
        buf.write(u"\u0972\5\u01b6\u00dc\2\u0970\u0971\7)\2\2\u0971\u0973")
        buf.write(u"\5\u01c0\u00e1\2\u0972\u0970\3\2\2\2\u0972\u0973\3\2")
        buf.write(u"\2\2\u0973\u01bf\3\2\2\2\u0974\u097a\7\u00a5\2\2\u0975")
        buf.write(u"\u0976\7\26\2\2\u0976\u0977\5^\60\2\u0977\u0978\7\27")
        buf.write(u"\2\2\u0978\u097a\3\2\2\2\u0979\u0974\3\2\2\2\u0979\u0975")
        buf.write(u"\3\2\2\2\u097a\u01c1\3\2\2\2\u097b\u097d\5\u01c4\u00e3")
        buf.write(u"\2\u097c\u097b\3\2\2\2\u097d\u097e\3\2\2\2\u097e\u097c")
        buf.write(u"\3\2\2\2\u097e\u097f\3\2\2\2\u097f\u01c3\3\2\2\2\u0980")
        buf.write(u"\u0988\5\u01c6\u00e4\2\u0981\u0988\5\u01a6\u00d4\2\u0982")
        buf.write(u"\u0984\7\26\2\2\u0983\u0985\5^\60\2\u0984\u0983\3\2\2")
        buf.write(u"\2\u0984\u0985\3\2\2\2\u0985\u0986\3\2\2\2\u0986\u0988")
        buf.write(u"\7\27\2\2\u0987\u0980\3\2\2\2\u0987\u0981\3\2\2\2\u0987")
        buf.write(u"\u0982\3\2\2\2\u0988\u01c5\3\2\2\2\u0989\u098b\n\f\2")
        buf.write(u"\2\u098a\u0989\3\2\2\2\u098b\u098c\3\2\2\2\u098c\u098a")
        buf.write(u"\3\2\2\2\u098c\u098d\3\2\2\2\u098d\u01c7\3\2\2\2\u00dc")
        buf.write(u"\u01cf\u01d3\u01ee\u01f5\u01fd\u01ff\u0204\u020c\u0210")
        buf.write(u"\u021a\u0226\u022c\u022f\u0232\u023b\u0243\u0248\u024e")
        buf.write(u"\u0256\u025b\u0261\u0266\u026f\u0274\u0279\u0282\u0287")
        buf.write(u"\u029b\u02a0\u02a6\u02ac\u02b2\u02b7\u02bc\u02bf\u02c5")
        buf.write(u"\u02dc\u02e6\u02eb\u02f2\u02f4\u030b\u0329\u0340\u0342")
        buf.write(u"\u034a\u0351\u0353\u035b\u0365\u037a\u037e\u0392\u039f")
        buf.write(u"\u03a3\u03ab\u03ae\u03b3\u03b6\u03be\u03c9\u03cd\u03d4")
        buf.write(u"\u03db\u03e4\u03ed\u03f6\u0410\u0484\u0486\u0496\u04a2")
        buf.write(u"\u04ac\u04cb\u04d8\u04de\u04e7\u04ee\u04f6\u04f8\u04fc")
        buf.write(u"\u0505\u0513\u051a\u0521\u0525\u0531\u0538\u053f\u054c")
        buf.write(u"\u0556\u0561\u0569\u0571\u0577\u057f\u0588\u0590\u059d")
        buf.write(u"\u05a0\u05a4\u05a9\u05ad\u05b6\u05cb\u05d5\u05d7\u05dc")
        buf.write(u"\u05ed\u05f2\u05fb\u0602\u0607\u060c\u061b\u0620\u0623")
        buf.write(u"\u0627\u062c\u0633\u063e\u0640\u0649\u0651\u0659\u065f")
        buf.write(u"\u066b\u066f\u0679\u067e\u0684\u068b\u0690\u0697\u069f")
        buf.write(u"\u06a6\u06b0\u06bd\u06c1\u06c4\u06c8\u06cb\u06d3\u06dc")
        buf.write(u"\u06e5\u06ee\u06ff\u0710\u0717\u071e\u0728\u072f\u0732")
        buf.write(u"\u0736\u073b\u073f\u074a\u074d\u0754\u0764\u0771\u0778")
        buf.write(u"\u0789\u0791\u0795\u079d\u07c5\u07ce\u07d8\u07e4\u07e9")
        buf.write(u"\u07f5\u0807\u080e\u0817\u081f\u0829\u082e\u0838\u0842")
        buf.write(u"\u0852\u085c\u0863\u086b\u0876\u087f\u0887\u0891\u0896")
        buf.write(u"\u08a2\u08b5\u08bf\u08c7\u08d2\u08db\u08e3\u08ed\u08f2")
        buf.write(u"\u08fe\u090c\u0913\u091b\u0921\u0926\u092a\u092e\u0935")
        buf.write(u"\u0940\u094b\u095a\u0961\u096d\u0972\u0979\u097e\u0984")
        buf.write(u"\u0987\u098c")
        return buf.getvalue()


class OParser ( AbstractParser ):

    grammarFileName = "OParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"' '", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"'Java:'", u"'C#:'", u"'Python2:'", u"'Python3:'", 
                     u"'JavaScript:'", u"'Swift:'", u"':'", u"';'", u"<INVALID>", 
                     u"'..'", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"'!'", u"'&'", u"'&&'", u"'|'", u"'||'", 
                     u"<INVALID>", u"'-'", u"'*'", u"'/'", u"'\\'", u"'%'", 
                     u"'>'", u"'>='", u"'<'", u"'<='", u"'<>'", u"'='", 
                     u"'!='", u"'=='", u"'~='", u"'~'", u"'<-'", u"'->'", 
                     u"'Boolean'", u"'Character'", u"'Text'", u"'Integer'", 
                     u"'Decimal'", u"'Date'", u"'Time'", u"'DateTime'", 
                     u"'Period'", u"'Version'", u"'Method'", u"'Code'", 
                     u"'Document'", u"'Blob'", u"'Image'", u"'Uuid'", u"'Iterator'", 
                     u"'Cursor'", u"'abstract'", u"'all'", u"'always'", 
                     u"'and'", u"'any'", u"'as'", u"<INVALID>", u"'attr'", 
                     u"'attribute'", u"'attributes'", u"'bindings'", u"'break'", 
                     u"'by'", u"'case'", u"'catch'", u"'category'", u"'class'", 
                     u"'close'", u"'contains'", u"'def'", u"'default'", 
                     u"'define'", u"'delete'", u"<INVALID>", u"'do'", u"'doing'", 
                     u"'each'", u"'else'", u"'enum'", u"'enumerated'", u"'except'", 
                     u"'execute'", u"'expecting'", u"'extends'", u"'fetch'", 
                     u"'filtered'", u"'finally'", u"'flush'", u"'for'", 
                     u"'from'", u"'getter'", u"'has'", u"'if'", u"'in'", 
                     u"'index'", u"'invoke'", u"'is'", u"'matching'", u"'method'", 
                     u"'methods'", u"'modulo'", u"'mutable'", u"'native'", 
                     u"'None'", u"'not'", u"<INVALID>", u"'null'", u"'on'", 
                     u"'one'", u"'open'", u"'operator'", u"'or'", u"'order'", 
                     u"'otherwise'", u"'pass'", u"'raise'", u"'read'", u"'receiving'", 
                     u"'resource'", u"'return'", u"'returning'", u"'rows'", 
                     u"'self'", u"'setter'", u"'singleton'", u"'sorted'", 
                     u"'storable'", u"'store'", u"'switch'", u"'test'", 
                     u"'this'", u"'throw'", u"'to'", u"'try'", u"'verifying'", 
                     u"'with'", u"'when'", u"'where'", u"'while'", u"'write'", 
                     u"<INVALID>", u"<INVALID>", u"'MIN_INTEGER'", u"'MAX_INTEGER'" ]

    symbolicNames = [ u"<INVALID>", u"SPACE", u"WS", u"LF", u"COMMENT", 
                      u"JAVA", u"CSHARP", u"PYTHON2", u"PYTHON3", u"JAVASCRIPT", 
                      u"SWIFT", u"COLON", u"SEMI", u"COMMA", u"RANGE", u"DOT", 
                      u"LPAR", u"RPAR", u"LBRAK", u"RBRAK", u"LCURL", u"RCURL", 
                      u"QMARK", u"XMARK", u"AMP", u"AMP2", u"PIPE", u"PIPE2", 
                      u"PLUS", u"MINUS", u"STAR", u"SLASH", u"BSLASH", u"PERCENT", 
                      u"GT", u"GTE", u"LT", u"LTE", u"LTGT", u"EQ", u"XEQ", 
                      u"EQ2", u"TEQ", u"TILDE", u"LARROW", u"RARROW", u"BOOLEAN", 
                      u"CHARACTER", u"TEXT", u"INTEGER", u"DECIMAL", u"DATE", 
                      u"TIME", u"DATETIME", u"PERIOD", u"VERSION", u"METHOD_T", 
                      u"CODE", u"DOCUMENT", u"BLOB", u"IMAGE", u"UUID", 
                      u"ITERATOR", u"CURSOR", u"ABSTRACT", u"ALL", u"ALWAYS", 
                      u"AND", u"ANY", u"AS", u"ASC", u"ATTR", u"ATTRIBUTE", 
                      u"ATTRIBUTES", u"BINDINGS", u"BREAK", u"BY", u"CASE", 
                      u"CATCH", u"CATEGORY", u"CLASS", u"CLOSE", u"CONTAINS", 
                      u"DEF", u"DEFAULT", u"DEFINE", u"DELETE", u"DESC", 
                      u"DO", u"DOING", u"EACH", u"ELSE", u"ENUM", u"ENUMERATED", 
                      u"EXCEPT", u"EXECUTE", u"EXPECTING", u"EXTENDS", u"FETCH", 
                      u"FILTERED", u"FINALLY", u"FLUSH", u"FOR", u"FROM", 
                      u"GETTER", u"HAS", u"IF", u"IN", u"INDEX", u"INVOKE", 
                      u"IS", u"MATCHING", u"METHOD", u"METHODS", u"MODULO", 
                      u"MUTABLE", u"NATIVE", u"NONE", u"NOT", u"NOTHING", 
                      u"NULL", u"ON", u"ONE", u"OPEN", u"OPERATOR", u"OR", 
                      u"ORDER", u"OTHERWISE", u"PASS", u"RAISE", u"READ", 
                      u"RECEIVING", u"RESOURCE", u"RETURN", u"RETURNING", 
                      u"ROWS", u"SELF", u"SETTER", u"SINGLETON", u"SORTED", 
                      u"STORABLE", u"STORE", u"SWITCH", u"TEST", u"THIS", 
                      u"THROW", u"TO", u"TRY", u"VERIFYING", u"WITH", u"WHEN", 
                      u"WHERE", u"WHILE", u"WRITE", u"BOOLEAN_LITERAL", 
                      u"CHAR_LITERAL", u"MIN_INTEGER", u"MAX_INTEGER", u"SYMBOL_IDENTIFIER", 
                      u"TYPE_IDENTIFIER", u"VARIABLE_IDENTIFIER", u"NATIVE_IDENTIFIER", 
                      u"DOLLAR_IDENTIFIER", u"TEXT_LITERAL", u"UUID_LITERAL", 
                      u"INTEGER_LITERAL", u"HEXA_LITERAL", u"DECIMAL_LITERAL", 
                      u"DATETIME_LITERAL", u"TIME_LITERAL", u"DATE_LITERAL", 
                      u"PERIOD_LITERAL", u"VERSION_LITERAL" ]

    RULE_enum_category_declaration = 0
    RULE_enum_native_declaration = 1
    RULE_category_symbol = 2
    RULE_native_symbol = 3
    RULE_attribute_declaration = 4
    RULE_concrete_category_declaration = 5
    RULE_singleton_category_declaration = 6
    RULE_derived_list = 7
    RULE_category_method_list = 8
    RULE_operator_method_declaration = 9
    RULE_setter_method_declaration = 10
    RULE_native_setter_declaration = 11
    RULE_getter_method_declaration = 12
    RULE_native_getter_declaration = 13
    RULE_native_resource_declaration = 14
    RULE_native_category_declaration = 15
    RULE_native_category_bindings = 16
    RULE_native_category_binding_list = 17
    RULE_abstract_method_declaration = 18
    RULE_concrete_method_declaration = 19
    RULE_native_method_declaration = 20
    RULE_test_method_declaration = 21
    RULE_assertion = 22
    RULE_typed_argument = 23
    RULE_statement_or_list = 24
    RULE_statement = 25
    RULE_flush_statement = 26
    RULE_store_statement = 27
    RULE_with_resource_statement = 28
    RULE_with_singleton_statement = 29
    RULE_switch_statement = 30
    RULE_switch_case_statement = 31
    RULE_for_each_statement = 32
    RULE_do_while_statement = 33
    RULE_while_statement = 34
    RULE_if_statement = 35
    RULE_else_if_statement_list = 36
    RULE_raise_statement = 37
    RULE_try_statement = 38
    RULE_catch_statement = 39
    RULE_break_statement = 40
    RULE_return_statement = 41
    RULE_method_call = 42
    RULE_method_selector = 43
    RULE_callable_parent = 44
    RULE_callable_selector = 45
    RULE_expression = 46
    RULE_an_expression = 47
    RULE_closure_expression = 48
    RULE_instance_expression = 49
    RULE_method_expression = 50
    RULE_blob_expression = 51
    RULE_document_expression = 52
    RULE_write_statement = 53
    RULE_filtered_list_expression = 54
    RULE_fetch_store_expression = 55
    RULE_sorted_expression = 56
    RULE_selector_expression = 57
    RULE_constructor_expression = 58
    RULE_copy_from = 59
    RULE_argument_assignment_list = 60
    RULE_argument_assignment = 61
    RULE_assign_instance_statement = 62
    RULE_child_instance = 63
    RULE_assign_tuple_statement = 64
    RULE_null_literal = 65
    RULE_declaration_list = 66
    RULE_declarations = 67
    RULE_declaration = 68
    RULE_resource_declaration = 69
    RULE_enum_declaration = 70
    RULE_native_symbol_list = 71
    RULE_category_symbol_list = 72
    RULE_symbol_list = 73
    RULE_attribute_constraint = 74
    RULE_list_literal = 75
    RULE_set_literal = 76
    RULE_expression_list = 77
    RULE_range_literal = 78
    RULE_typedef = 79
    RULE_primary_type = 80
    RULE_native_type = 81
    RULE_category_type = 82
    RULE_mutable_category_type = 83
    RULE_code_type = 84
    RULE_category_declaration = 85
    RULE_type_identifier_list = 86
    RULE_method_identifier = 87
    RULE_identifier = 88
    RULE_variable_identifier = 89
    RULE_attribute_identifier = 90
    RULE_type_identifier = 91
    RULE_symbol_identifier = 92
    RULE_argument_list = 93
    RULE_argument = 94
    RULE_operator_argument = 95
    RULE_named_argument = 96
    RULE_code_argument = 97
    RULE_category_or_any_type = 98
    RULE_any_type = 99
    RULE_member_method_declaration_list = 100
    RULE_member_method_declaration = 101
    RULE_native_member_method_declaration_list = 102
    RULE_native_member_method_declaration = 103
    RULE_native_category_binding = 104
    RULE_python_category_binding = 105
    RULE_python_module = 106
    RULE_javascript_category_binding = 107
    RULE_javascript_module = 108
    RULE_variable_identifier_list = 109
    RULE_attribute_identifier_list = 110
    RULE_method_declaration = 111
    RULE_comment_statement = 112
    RULE_native_statement_list = 113
    RULE_native_statement = 114
    RULE_python_native_statement = 115
    RULE_javascript_native_statement = 116
    RULE_statement_list = 117
    RULE_assertion_list = 118
    RULE_switch_case_statement_list = 119
    RULE_catch_statement_list = 120
    RULE_literal_collection = 121
    RULE_atomic_literal = 122
    RULE_literal_list_literal = 123
    RULE_selectable_expression = 124
    RULE_this_expression = 125
    RULE_parenthesis_expression = 126
    RULE_literal_expression = 127
    RULE_collection_literal = 128
    RULE_tuple_literal = 129
    RULE_dict_literal = 130
    RULE_expression_tuple = 131
    RULE_dict_entry_list = 132
    RULE_dict_entry = 133
    RULE_slice_arguments = 134
    RULE_assign_variable_statement = 135
    RULE_assignable_instance = 136
    RULE_is_expression = 137
    RULE_read_all_expression = 138
    RULE_read_one_expression = 139
    RULE_order_by_list = 140
    RULE_order_by = 141
    RULE_operator = 142
    RULE_keyword = 143
    RULE_new_token = 144
    RULE_key_token = 145
    RULE_module_token = 146
    RULE_value_token = 147
    RULE_symbols_token = 148
    RULE_assign = 149
    RULE_multiply = 150
    RULE_divide = 151
    RULE_idivide = 152
    RULE_modulo = 153
    RULE_lfs = 154
    RULE_lfp = 155
    RULE_javascript_statement = 156
    RULE_javascript_expression = 157
    RULE_javascript_primary_expression = 158
    RULE_javascript_this_expression = 159
    RULE_javascript_new_expression = 160
    RULE_javascript_selector_expression = 161
    RULE_javascript_method_expression = 162
    RULE_javascript_arguments = 163
    RULE_javascript_item_expression = 164
    RULE_javascript_parenthesis_expression = 165
    RULE_javascript_identifier_expression = 166
    RULE_javascript_literal_expression = 167
    RULE_javascript_identifier = 168
    RULE_python_statement = 169
    RULE_python_expression = 170
    RULE_python_primary_expression = 171
    RULE_python_self_expression = 172
    RULE_python_selector_expression = 173
    RULE_python_method_expression = 174
    RULE_python_argument_list = 175
    RULE_python_ordinal_argument_list = 176
    RULE_python_named_argument_list = 177
    RULE_python_parenthesis_expression = 178
    RULE_python_identifier_expression = 179
    RULE_python_literal_expression = 180
    RULE_python_identifier = 181
    RULE_java_statement = 182
    RULE_java_expression = 183
    RULE_java_primary_expression = 184
    RULE_java_this_expression = 185
    RULE_java_new_expression = 186
    RULE_java_selector_expression = 187
    RULE_java_method_expression = 188
    RULE_java_arguments = 189
    RULE_java_item_expression = 190
    RULE_java_parenthesis_expression = 191
    RULE_java_identifier_expression = 192
    RULE_java_class_identifier_expression = 193
    RULE_java_literal_expression = 194
    RULE_java_identifier = 195
    RULE_csharp_statement = 196
    RULE_csharp_expression = 197
    RULE_csharp_primary_expression = 198
    RULE_csharp_this_expression = 199
    RULE_csharp_new_expression = 200
    RULE_csharp_selector_expression = 201
    RULE_csharp_method_expression = 202
    RULE_csharp_arguments = 203
    RULE_csharp_item_expression = 204
    RULE_csharp_parenthesis_expression = 205
    RULE_csharp_identifier_expression = 206
    RULE_csharp_literal_expression = 207
    RULE_csharp_identifier = 208
    RULE_jsx_expression = 209
    RULE_jsx_element = 210
    RULE_jsx_fragment = 211
    RULE_jsx_fragment_start = 212
    RULE_jsx_fragment_end = 213
    RULE_jsx_self_closing = 214
    RULE_jsx_opening = 215
    RULE_jsx_closing = 216
    RULE_jsx_element_name = 217
    RULE_jsx_identifier = 218
    RULE_jsx_hyphen_identifier = 219
    RULE_hyphen_identifier = 220
    RULE_identifier_or_keyword = 221
    RULE_jsx_attribute = 222
    RULE_jsx_attribute_value = 223
    RULE_jsx_children = 224
    RULE_jsx_child = 225
    RULE_jsx_text = 226

    ruleNames =  [ u"enum_category_declaration", u"enum_native_declaration", 
                   u"category_symbol", u"native_symbol", u"attribute_declaration", 
                   u"concrete_category_declaration", u"singleton_category_declaration", 
                   u"derived_list", u"category_method_list", u"operator_method_declaration", 
                   u"setter_method_declaration", u"native_setter_declaration", 
                   u"getter_method_declaration", u"native_getter_declaration", 
                   u"native_resource_declaration", u"native_category_declaration", 
                   u"native_category_bindings", u"native_category_binding_list", 
                   u"abstract_method_declaration", u"concrete_method_declaration", 
                   u"native_method_declaration", u"test_method_declaration", 
                   u"assertion", u"typed_argument", u"statement_or_list", 
                   u"statement", u"flush_statement", u"store_statement", 
                   u"with_resource_statement", u"with_singleton_statement", 
                   u"switch_statement", u"switch_case_statement", u"for_each_statement", 
                   u"do_while_statement", u"while_statement", u"if_statement", 
                   u"else_if_statement_list", u"raise_statement", u"try_statement", 
                   u"catch_statement", u"break_statement", u"return_statement", 
                   u"method_call", u"method_selector", u"callable_parent", 
                   u"callable_selector", u"expression", u"an_expression", 
                   u"closure_expression", u"instance_expression", u"method_expression", 
                   u"blob_expression", u"document_expression", u"write_statement", 
                   u"filtered_list_expression", u"fetch_store_expression", 
                   u"sorted_expression", u"selector_expression", u"constructor_expression", 
                   u"copy_from", u"argument_assignment_list", u"argument_assignment", 
                   u"assign_instance_statement", u"child_instance", u"assign_tuple_statement", 
                   u"null_literal", u"declaration_list", u"declarations", 
                   u"declaration", u"resource_declaration", u"enum_declaration", 
                   u"native_symbol_list", u"category_symbol_list", u"symbol_list", 
                   u"attribute_constraint", u"list_literal", u"set_literal", 
                   u"expression_list", u"range_literal", u"typedef", u"primary_type", 
                   u"native_type", u"category_type", u"mutable_category_type", 
                   u"code_type", u"category_declaration", u"type_identifier_list", 
                   u"method_identifier", u"identifier", u"variable_identifier", 
                   u"attribute_identifier", u"type_identifier", u"symbol_identifier", 
                   u"argument_list", u"argument", u"operator_argument", 
                   u"named_argument", u"code_argument", u"category_or_any_type", 
                   u"any_type", u"member_method_declaration_list", u"member_method_declaration", 
                   u"native_member_method_declaration_list", u"native_member_method_declaration", 
                   u"native_category_binding", u"python_category_binding", 
                   u"python_module", u"javascript_category_binding", u"javascript_module", 
                   u"variable_identifier_list", u"attribute_identifier_list", 
                   u"method_declaration", u"comment_statement", u"native_statement_list", 
                   u"native_statement", u"python_native_statement", u"javascript_native_statement", 
                   u"statement_list", u"assertion_list", u"switch_case_statement_list", 
                   u"catch_statement_list", u"literal_collection", u"atomic_literal", 
                   u"literal_list_literal", u"selectable_expression", u"this_expression", 
                   u"parenthesis_expression", u"literal_expression", u"collection_literal", 
                   u"tuple_literal", u"dict_literal", u"expression_tuple", 
                   u"dict_entry_list", u"dict_entry", u"slice_arguments", 
                   u"assign_variable_statement", u"assignable_instance", 
                   u"is_expression", u"read_all_expression", u"read_one_expression", 
                   u"order_by_list", u"order_by", u"operator", u"keyword", 
                   u"new_token", u"key_token", u"module_token", u"value_token", 
                   u"symbols_token", u"assign", u"multiply", u"divide", 
                   u"idivide", u"modulo", u"lfs", u"lfp", u"javascript_statement", 
                   u"javascript_expression", u"javascript_primary_expression", 
                   u"javascript_this_expression", u"javascript_new_expression", 
                   u"javascript_selector_expression", u"javascript_method_expression", 
                   u"javascript_arguments", u"javascript_item_expression", 
                   u"javascript_parenthesis_expression", u"javascript_identifier_expression", 
                   u"javascript_literal_expression", u"javascript_identifier", 
                   u"python_statement", u"python_expression", u"python_primary_expression", 
                   u"python_self_expression", u"python_selector_expression", 
                   u"python_method_expression", u"python_argument_list", 
                   u"python_ordinal_argument_list", u"python_named_argument_list", 
                   u"python_parenthesis_expression", u"python_identifier_expression", 
                   u"python_literal_expression", u"python_identifier", u"java_statement", 
                   u"java_expression", u"java_primary_expression", u"java_this_expression", 
                   u"java_new_expression", u"java_selector_expression", 
                   u"java_method_expression", u"java_arguments", u"java_item_expression", 
                   u"java_parenthesis_expression", u"java_identifier_expression", 
                   u"java_class_identifier_expression", u"java_literal_expression", 
                   u"java_identifier", u"csharp_statement", u"csharp_expression", 
                   u"csharp_primary_expression", u"csharp_this_expression", 
                   u"csharp_new_expression", u"csharp_selector_expression", 
                   u"csharp_method_expression", u"csharp_arguments", u"csharp_item_expression", 
                   u"csharp_parenthesis_expression", u"csharp_identifier_expression", 
                   u"csharp_literal_expression", u"csharp_identifier", u"jsx_expression", 
                   u"jsx_element", u"jsx_fragment", u"jsx_fragment_start", 
                   u"jsx_fragment_end", u"jsx_self_closing", u"jsx_opening", 
                   u"jsx_closing", u"jsx_element_name", u"jsx_identifier", 
                   u"jsx_hyphen_identifier", u"hyphen_identifier", u"identifier_or_keyword", 
                   u"jsx_attribute", u"jsx_attribute_value", u"jsx_children", 
                   u"jsx_child", u"jsx_text" ]

    EOF = Token.EOF
    SPACE=1
    WS=2
    LF=3
    COMMENT=4
    JAVA=5
    CSHARP=6
    PYTHON2=7
    PYTHON3=8
    JAVASCRIPT=9
    SWIFT=10
    COLON=11
    SEMI=12
    COMMA=13
    RANGE=14
    DOT=15
    LPAR=16
    RPAR=17
    LBRAK=18
    RBRAK=19
    LCURL=20
    RCURL=21
    QMARK=22
    XMARK=23
    AMP=24
    AMP2=25
    PIPE=26
    PIPE2=27
    PLUS=28
    MINUS=29
    STAR=30
    SLASH=31
    BSLASH=32
    PERCENT=33
    GT=34
    GTE=35
    LT=36
    LTE=37
    LTGT=38
    EQ=39
    XEQ=40
    EQ2=41
    TEQ=42
    TILDE=43
    LARROW=44
    RARROW=45
    BOOLEAN=46
    CHARACTER=47
    TEXT=48
    INTEGER=49
    DECIMAL=50
    DATE=51
    TIME=52
    DATETIME=53
    PERIOD=54
    VERSION=55
    METHOD_T=56
    CODE=57
    DOCUMENT=58
    BLOB=59
    IMAGE=60
    UUID=61
    ITERATOR=62
    CURSOR=63
    ABSTRACT=64
    ALL=65
    ALWAYS=66
    AND=67
    ANY=68
    AS=69
    ASC=70
    ATTR=71
    ATTRIBUTE=72
    ATTRIBUTES=73
    BINDINGS=74
    BREAK=75
    BY=76
    CASE=77
    CATCH=78
    CATEGORY=79
    CLASS=80
    CLOSE=81
    CONTAINS=82
    DEF=83
    DEFAULT=84
    DEFINE=85
    DELETE=86
    DESC=87
    DO=88
    DOING=89
    EACH=90
    ELSE=91
    ENUM=92
    ENUMERATED=93
    EXCEPT=94
    EXECUTE=95
    EXPECTING=96
    EXTENDS=97
    FETCH=98
    FILTERED=99
    FINALLY=100
    FLUSH=101
    FOR=102
    FROM=103
    GETTER=104
    HAS=105
    IF=106
    IN=107
    INDEX=108
    INVOKE=109
    IS=110
    MATCHING=111
    METHOD=112
    METHODS=113
    MODULO=114
    MUTABLE=115
    NATIVE=116
    NONE=117
    NOT=118
    NOTHING=119
    NULL=120
    ON=121
    ONE=122
    OPEN=123
    OPERATOR=124
    OR=125
    ORDER=126
    OTHERWISE=127
    PASS=128
    RAISE=129
    READ=130
    RECEIVING=131
    RESOURCE=132
    RETURN=133
    RETURNING=134
    ROWS=135
    SELF=136
    SETTER=137
    SINGLETON=138
    SORTED=139
    STORABLE=140
    STORE=141
    SWITCH=142
    TEST=143
    THIS=144
    THROW=145
    TO=146
    TRY=147
    VERIFYING=148
    WITH=149
    WHEN=150
    WHERE=151
    WHILE=152
    WRITE=153
    BOOLEAN_LITERAL=154
    CHAR_LITERAL=155
    MIN_INTEGER=156
    MAX_INTEGER=157
    SYMBOL_IDENTIFIER=158
    TYPE_IDENTIFIER=159
    VARIABLE_IDENTIFIER=160
    NATIVE_IDENTIFIER=161
    DOLLAR_IDENTIFIER=162
    TEXT_LITERAL=163
    UUID_LITERAL=164
    INTEGER_LITERAL=165
    HEXA_LITERAL=166
    DECIMAL_LITERAL=167
    DATETIME_LITERAL=168
    TIME_LITERAL=169
    DATE_LITERAL=170
    PERIOD_LITERAL=171
    VERSION_LITERAL=172

    def __init__(self, input, output=sys.stdout):
        super(OParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Enum_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Enum_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_identifier_listContext
            self.derived = None # Type_identifierContext
            self.symbols = None # Category_symbol_listContext

        def ENUMERATED(self):
            return self.getToken(OParser.ENUMERATED, 0)

        def CATEGORY(self):
            return self.getToken(OParser.CATEGORY, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def type_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Type_identifierContext)
            else:
                return self.getTypedRuleContext(OParser.Type_identifierContext,i)


        def category_symbol_list(self):
            return self.getTypedRuleContext(OParser.Category_symbol_listContext,0)


        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def EXTENDS(self):
            return self.getToken(OParser.EXTENDS, 0)

        def attribute_identifier_list(self):
            return self.getTypedRuleContext(OParser.Attribute_identifier_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_enum_category_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterEnum_category_declaration"):
                listener.enterEnum_category_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEnum_category_declaration"):
                listener.exitEnum_category_declaration(self)




    def enum_category_declaration(self):

        localctx = OParser.Enum_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_enum_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(OParser.ENUMERATED)
            self.state = 455
            self.match(OParser.CATEGORY)
            self.state = 456
            localctx.name = self.type_identifier()
            self.state = 461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 457
                self.match(OParser.LPAR)
                self.state = 458
                localctx.attrs = self.attribute_identifier_list()
                self.state = 459
                self.match(OParser.RPAR)


            self.state = 465
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.EXTENDS:
                self.state = 463
                self.match(OParser.EXTENDS)
                self.state = 464
                localctx.derived = self.type_identifier()


            self.state = 467
            self.match(OParser.LCURL)
            self.state = 468
            localctx.symbols = self.category_symbol_list()
            self.state = 469
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Enum_native_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Enum_native_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.typ = None # Native_typeContext
            self.symbols = None # Native_symbol_listContext

        def ENUMERATED(self):
            return self.getToken(OParser.ENUMERATED, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def native_type(self):
            return self.getTypedRuleContext(OParser.Native_typeContext,0)


        def native_symbol_list(self):
            return self.getTypedRuleContext(OParser.Native_symbol_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_enum_native_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterEnum_native_declaration"):
                listener.enterEnum_native_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEnum_native_declaration"):
                listener.exitEnum_native_declaration(self)




    def enum_native_declaration(self):

        localctx = OParser.Enum_native_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_enum_native_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(OParser.ENUMERATED)
            self.state = 472
            localctx.name = self.type_identifier()
            self.state = 473
            self.match(OParser.LPAR)
            self.state = 474
            localctx.typ = self.native_type()
            self.state = 475
            self.match(OParser.RPAR)
            self.state = 476
            self.match(OParser.LCURL)
            self.state = 477
            localctx.symbols = self.native_symbol_list()
            self.state = 478
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_symbolContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Category_symbolContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Symbol_identifierContext
            self.args = None # Argument_assignment_listContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(OParser.Symbol_identifierContext,0)


        def argument_assignment_list(self):
            return self.getTypedRuleContext(OParser.Argument_assignment_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_category_symbol

        def enterRule(self, listener):
            if hasattr(listener, "enterCategory_symbol"):
                listener.enterCategory_symbol(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategory_symbol"):
                listener.exitCategory_symbol(self)




    def category_symbol(self):

        localctx = OParser.Category_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_category_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            localctx.name = self.symbol_identifier()
            self.state = 481
            self.match(OParser.LPAR)
            self.state = 482
            localctx.args = self.argument_assignment_list(0)
            self.state = 483
            self.match(OParser.RPAR)
            self.state = 484
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_symbolContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_symbolContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Symbol_identifierContext
            self.exp = None # ExpressionContext

        def EQ(self):
            return self.getToken(OParser.EQ, 0)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(OParser.Symbol_identifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_native_symbol

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_symbol"):
                listener.enterNative_symbol(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_symbol"):
                listener.exitNative_symbol(self)




    def native_symbol(self):

        localctx = OParser.Native_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_native_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            localctx.name = self.symbol_identifier()
            self.state = 487
            self.match(OParser.EQ)
            self.state = 488
            localctx.exp = self.expression(0)
            self.state = 489
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Attribute_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Attribute_identifierContext
            self.typ = None # TypedefContext
            self.match = None # Attribute_constraintContext
            self.indices = None # Variable_identifier_listContext

        def ATTRIBUTE(self):
            return self.getToken(OParser.ATTRIBUTE, 0)

        def COLON(self):
            return self.getToken(OParser.COLON, 0)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def attribute_identifier(self):
            return self.getTypedRuleContext(OParser.Attribute_identifierContext,0)


        def typedef(self):
            return self.getTypedRuleContext(OParser.TypedefContext,0)


        def STORABLE(self):
            return self.getToken(OParser.STORABLE, 0)

        def WITH(self):
            return self.getToken(OParser.WITH, 0)

        def INDEX(self):
            return self.getToken(OParser.INDEX, 0)

        def attribute_constraint(self):
            return self.getTypedRuleContext(OParser.Attribute_constraintContext,0)


        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def variable_identifier_list(self):
            return self.getTypedRuleContext(OParser.Variable_identifier_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_attribute_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterAttribute_declaration"):
                listener.enterAttribute_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAttribute_declaration"):
                listener.exitAttribute_declaration(self)




    def attribute_declaration(self):

        localctx = OParser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.STORABLE:
                self.state = 491
                self.match(OParser.STORABLE)


            self.state = 494
            self.match(OParser.ATTRIBUTE)
            self.state = 495
            localctx.name = self.attribute_identifier()
            self.state = 496
            self.match(OParser.COLON)
            self.state = 497
            localctx.typ = self.typedef(0)
            self.state = 499
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.IN or _la==OParser.MATCHING:
                self.state = 498
                localctx.match = self.attribute_constraint()


            self.state = 509
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.WITH:
                self.state = 501
                self.match(OParser.WITH)
                self.state = 502
                self.match(OParser.INDEX)
                self.state = 507
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==OParser.LPAR:
                    self.state = 503
                    self.match(OParser.LPAR)
                    self.state = 504
                    localctx.indices = self.variable_identifier_list()
                    self.state = 505
                    self.match(OParser.RPAR)




            self.state = 511
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Concrete_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Concrete_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_identifier_listContext
            self.derived = None # Derived_listContext
            self.methods = None # Category_method_listContext

        def CATEGORY(self):
            return self.getToken(OParser.CATEGORY, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def category_method_list(self):
            return self.getTypedRuleContext(OParser.Category_method_listContext,0)


        def STORABLE(self):
            return self.getToken(OParser.STORABLE, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def EXTENDS(self):
            return self.getToken(OParser.EXTENDS, 0)

        def attribute_identifier_list(self):
            return self.getTypedRuleContext(OParser.Attribute_identifier_listContext,0)


        def derived_list(self):
            return self.getTypedRuleContext(OParser.Derived_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_concrete_category_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterConcrete_category_declaration"):
                listener.enterConcrete_category_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConcrete_category_declaration"):
                listener.exitConcrete_category_declaration(self)




    def concrete_category_declaration(self):

        localctx = OParser.Concrete_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_concrete_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.STORABLE:
                self.state = 513
                self.match(OParser.STORABLE)


            self.state = 516
            self.match(OParser.CATEGORY)
            self.state = 517
            localctx.name = self.type_identifier()
            self.state = 522
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 518
                self.match(OParser.LPAR)
                self.state = 519
                localctx.attrs = self.attribute_identifier_list()
                self.state = 520
                self.match(OParser.RPAR)


            self.state = 526
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.EXTENDS:
                self.state = 524
                self.match(OParser.EXTENDS)
                self.state = 525
                localctx.derived = self.derived_list(0)


            self.state = 528
            localctx.methods = self.category_method_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Singleton_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Singleton_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_identifier_listContext
            self.methods = None # Category_method_listContext

        def SINGLETON(self):
            return self.getToken(OParser.SINGLETON, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def category_method_list(self):
            return self.getTypedRuleContext(OParser.Category_method_listContext,0)


        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def attribute_identifier_list(self):
            return self.getTypedRuleContext(OParser.Attribute_identifier_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_singleton_category_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterSingleton_category_declaration"):
                listener.enterSingleton_category_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSingleton_category_declaration"):
                listener.exitSingleton_category_declaration(self)




    def singleton_category_declaration(self):

        localctx = OParser.Singleton_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_singleton_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.match(OParser.SINGLETON)
            self.state = 531
            localctx.name = self.type_identifier()
            self.state = 536
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 532
                self.match(OParser.LPAR)
                self.state = 533
                localctx.attrs = self.attribute_identifier_list()
                self.state = 534
                self.match(OParser.RPAR)


            self.state = 538
            localctx.methods = self.category_method_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Derived_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Derived_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_derived_list

     
        def copyFrom(self, ctx):
            super(OParser.Derived_listContext, self).copyFrom(ctx)


    class DerivedListItemContext(Derived_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Derived_listContext)
            super(OParser.DerivedListItemContext, self).__init__(parser)
            self.items = None # Derived_listContext
            self.item = None # Type_identifierContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def derived_list(self):
            return self.getTypedRuleContext(OParser.Derived_listContext,0)

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterDerivedListItem"):
                listener.enterDerivedListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDerivedListItem"):
                listener.exitDerivedListItem(self)


    class DerivedListContext(Derived_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Derived_listContext)
            super(OParser.DerivedListContext, self).__init__(parser)
            self.item = None # Type_identifierContext
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterDerivedList"):
                listener.enterDerivedList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDerivedList"):
                listener.exitDerivedList(self)



    def derived_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Derived_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_derived_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.DerivedListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 541
            localctx.item = self.type_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 548
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.DerivedListItemContext(self, OParser.Derived_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_derived_list)
                    self.state = 543
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 544
                    self.match(OParser.COMMA)
                    self.state = 545
                    localctx.item = self.type_identifier() 
                self.state = 550
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Category_method_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Category_method_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_category_method_list

     
        def copyFrom(self, ctx):
            super(OParser.Category_method_listContext, self).copyFrom(ctx)



    class EmptyCategoryMethodListContext(Category_method_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Category_method_listContext)
            super(OParser.EmptyCategoryMethodListContext, self).__init__(parser)
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterEmptyCategoryMethodList"):
                listener.enterEmptyCategoryMethodList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEmptyCategoryMethodList"):
                listener.exitEmptyCategoryMethodList(self)


    class CurlyCategoryMethodListContext(Category_method_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Category_method_listContext)
            super(OParser.CurlyCategoryMethodListContext, self).__init__(parser)
            self.items = None # Member_method_declaration_listContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)
        def member_method_declaration_list(self):
            return self.getTypedRuleContext(OParser.Member_method_declaration_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCurlyCategoryMethodList"):
                listener.enterCurlyCategoryMethodList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCurlyCategoryMethodList"):
                listener.exitCurlyCategoryMethodList(self)



    def category_method_list(self):

        localctx = OParser.Category_method_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_category_method_list)
        self._la = 0 # Token type
        try:
            self.state = 557
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.SEMI]:
                localctx = OParser.EmptyCategoryMethodListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 551
                self.match(OParser.SEMI)
                pass
            elif token in [OParser.LCURL]:
                localctx = OParser.CurlyCategoryMethodListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 552
                self.match(OParser.LCURL)
                self.state = 554
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ABSTRACT - 46)) | (1 << (OParser.GETTER - 46)))) != 0) or ((((_la - 112)) & ~0x3f) == 0 and ((1 << (_la - 112)) & ((1 << (OParser.METHOD - 112)) | (1 << (OParser.OPERATOR - 112)) | (1 << (OParser.SETTER - 112)) | (1 << (OParser.TYPE_IDENTIFIER - 112)))) != 0):
                    self.state = 553
                    localctx.items = self.member_method_declaration_list()


                self.state = 556
                self.match(OParser.RCURL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Operator_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Operator_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # TypedefContext
            self.op = None # OperatorContext
            self.arg = None # Operator_argumentContext
            self.stmts = None # Statement_listContext

        def OPERATOR(self):
            return self.getToken(OParser.OPERATOR, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def operator(self):
            return self.getTypedRuleContext(OParser.OperatorContext,0)


        def operator_argument(self):
            return self.getTypedRuleContext(OParser.Operator_argumentContext,0)


        def typedef(self):
            return self.getTypedRuleContext(OParser.TypedefContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_operator_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterOperator_method_declaration"):
                listener.enterOperator_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperator_method_declaration"):
                listener.exitOperator_method_declaration(self)




    def operator_method_declaration(self):

        localctx = OParser.Operator_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_operator_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or _la==OParser.TYPE_IDENTIFIER:
                self.state = 559
                localctx.typ = self.typedef(0)


            self.state = 562
            self.match(OParser.OPERATOR)
            self.state = 563
            localctx.op = self.operator()
            self.state = 564
            self.match(OParser.LPAR)
            self.state = 565
            localctx.arg = self.operator_argument()
            self.state = 566
            self.match(OParser.RPAR)
            self.state = 567
            self.match(OParser.LCURL)
            self.state = 569
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                self.state = 568
                localctx.stmts = self.statement_list()


            self.state = 571
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Setter_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Setter_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext

        def SETTER(self):
            return self.getToken(OParser.SETTER, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_setter_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterSetter_method_declaration"):
                listener.enterSetter_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSetter_method_declaration"):
                listener.exitSetter_method_declaration(self)




    def setter_method_declaration(self):

        localctx = OParser.Setter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_setter_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 573
            self.match(OParser.SETTER)
            self.state = 574
            localctx.name = self.variable_identifier()
            self.state = 575
            self.match(OParser.LCURL)
            self.state = 577
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                self.state = 576
                localctx.stmts = self.statement_list()


            self.state = 579
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_setter_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_setter_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Native_statement_listContext

        def SETTER(self):
            return self.getToken(OParser.SETTER, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def NATIVE(self):
            return self.getToken(OParser.NATIVE, 0)

        def native_statement_list(self):
            return self.getTypedRuleContext(OParser.Native_statement_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_native_setter_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_setter_declaration"):
                listener.enterNative_setter_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_setter_declaration"):
                listener.exitNative_setter_declaration(self)




    def native_setter_declaration(self):

        localctx = OParser.Native_setter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_native_setter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 582
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.NATIVE:
                self.state = 581
                self.match(OParser.NATIVE)


            self.state = 584
            self.match(OParser.SETTER)
            self.state = 585
            localctx.name = self.variable_identifier()
            self.state = 586
            self.match(OParser.LCURL)
            self.state = 588
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.JAVA) | (1 << OParser.CSHARP) | (1 << OParser.PYTHON2) | (1 << OParser.PYTHON3) | (1 << OParser.JAVASCRIPT))) != 0):
                self.state = 587
                localctx.stmts = self.native_statement_list()


            self.state = 590
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Getter_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Getter_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext

        def GETTER(self):
            return self.getToken(OParser.GETTER, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_getter_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterGetter_method_declaration"):
                listener.enterGetter_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitGetter_method_declaration"):
                listener.exitGetter_method_declaration(self)




    def getter_method_declaration(self):

        localctx = OParser.Getter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_getter_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self.match(OParser.GETTER)
            self.state = 593
            localctx.name = self.variable_identifier()
            self.state = 594
            self.match(OParser.LCURL)
            self.state = 596
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                self.state = 595
                localctx.stmts = self.statement_list()


            self.state = 598
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_getter_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_getter_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Native_statement_listContext

        def GETTER(self):
            return self.getToken(OParser.GETTER, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def NATIVE(self):
            return self.getToken(OParser.NATIVE, 0)

        def native_statement_list(self):
            return self.getTypedRuleContext(OParser.Native_statement_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_native_getter_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_getter_declaration"):
                listener.enterNative_getter_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_getter_declaration"):
                listener.exitNative_getter_declaration(self)




    def native_getter_declaration(self):

        localctx = OParser.Native_getter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_native_getter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 601
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.NATIVE:
                self.state = 600
                self.match(OParser.NATIVE)


            self.state = 603
            self.match(OParser.GETTER)
            self.state = 604
            localctx.name = self.variable_identifier()
            self.state = 605
            self.match(OParser.LCURL)
            self.state = 607
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.JAVA) | (1 << OParser.CSHARP) | (1 << OParser.PYTHON2) | (1 << OParser.PYTHON3) | (1 << OParser.JAVASCRIPT))) != 0):
                self.state = 606
                localctx.stmts = self.native_statement_list()


            self.state = 609
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_resource_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_resource_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_identifier_listContext
            self.bindings = None # Native_category_bindingsContext
            self.methods = None # Native_member_method_declaration_listContext

        def NATIVE(self):
            return self.getToken(OParser.NATIVE, 0)

        def RESOURCE(self):
            return self.getToken(OParser.RESOURCE, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def native_category_bindings(self):
            return self.getTypedRuleContext(OParser.Native_category_bindingsContext,0)


        def STORABLE(self):
            return self.getToken(OParser.STORABLE, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def attribute_identifier_list(self):
            return self.getTypedRuleContext(OParser.Attribute_identifier_listContext,0)


        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(OParser.Native_member_method_declaration_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_native_resource_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_resource_declaration"):
                listener.enterNative_resource_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_resource_declaration"):
                listener.exitNative_resource_declaration(self)




    def native_resource_declaration(self):

        localctx = OParser.Native_resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_native_resource_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.STORABLE:
                self.state = 611
                self.match(OParser.STORABLE)


            self.state = 614
            self.match(OParser.NATIVE)
            self.state = 615
            self.match(OParser.RESOURCE)
            self.state = 616
            localctx.name = self.type_identifier()
            self.state = 621
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 617
                self.match(OParser.LPAR)
                self.state = 618
                localctx.attrs = self.attribute_identifier_list()
                self.state = 619
                self.match(OParser.RPAR)


            self.state = 623
            self.match(OParser.LCURL)
            self.state = 624
            localctx.bindings = self.native_category_bindings()
            self.state = 626
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ANY - 46)) | (1 << (OParser.GETTER - 46)))) != 0) or ((((_la - 112)) & ~0x3f) == 0 and ((1 << (_la - 112)) & ((1 << (OParser.METHOD - 112)) | (1 << (OParser.NATIVE - 112)) | (1 << (OParser.SETTER - 112)) | (1 << (OParser.TYPE_IDENTIFIER - 112)))) != 0):
                self.state = 625
                localctx.methods = self.native_member_method_declaration_list()


            self.state = 628
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_identifier_listContext
            self.bindings = None # Native_category_bindingsContext
            self.methods = None # Native_member_method_declaration_listContext

        def NATIVE(self):
            return self.getToken(OParser.NATIVE, 0)

        def CATEGORY(self):
            return self.getToken(OParser.CATEGORY, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def native_category_bindings(self):
            return self.getTypedRuleContext(OParser.Native_category_bindingsContext,0)


        def STORABLE(self):
            return self.getToken(OParser.STORABLE, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def attribute_identifier_list(self):
            return self.getTypedRuleContext(OParser.Attribute_identifier_listContext,0)


        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(OParser.Native_member_method_declaration_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_native_category_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_category_declaration"):
                listener.enterNative_category_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_category_declaration"):
                listener.exitNative_category_declaration(self)




    def native_category_declaration(self):

        localctx = OParser.Native_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_native_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 631
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.STORABLE:
                self.state = 630
                self.match(OParser.STORABLE)


            self.state = 633
            self.match(OParser.NATIVE)
            self.state = 634
            self.match(OParser.CATEGORY)
            self.state = 635
            localctx.name = self.type_identifier()
            self.state = 640
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 636
                self.match(OParser.LPAR)
                self.state = 637
                localctx.attrs = self.attribute_identifier_list()
                self.state = 638
                self.match(OParser.RPAR)


            self.state = 642
            self.match(OParser.LCURL)
            self.state = 643
            localctx.bindings = self.native_category_bindings()
            self.state = 645
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ANY - 46)) | (1 << (OParser.GETTER - 46)))) != 0) or ((((_la - 112)) & ~0x3f) == 0 and ((1 << (_la - 112)) & ((1 << (OParser.METHOD - 112)) | (1 << (OParser.NATIVE - 112)) | (1 << (OParser.SETTER - 112)) | (1 << (OParser.TYPE_IDENTIFIER - 112)))) != 0):
                self.state = 644
                localctx.methods = self.native_member_method_declaration_list()


            self.state = 647
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_category_bindingsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_category_bindingsContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Native_category_binding_listContext

        def CATEGORY(self):
            return self.getToken(OParser.CATEGORY, 0)

        def BINDINGS(self):
            return self.getToken(OParser.BINDINGS, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def native_category_binding_list(self):
            return self.getTypedRuleContext(OParser.Native_category_binding_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_native_category_bindings

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_category_bindings"):
                listener.enterNative_category_bindings(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_category_bindings"):
                listener.exitNative_category_bindings(self)




    def native_category_bindings(self):

        localctx = OParser.Native_category_bindingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_native_category_bindings)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 649
            self.match(OParser.CATEGORY)
            self.state = 650
            self.match(OParser.BINDINGS)
            self.state = 651
            self.match(OParser.LCURL)
            self.state = 652
            localctx.items = self.native_category_binding_list(0)
            self.state = 653
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_category_binding_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_category_binding_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_native_category_binding_list

     
        def copyFrom(self, ctx):
            super(OParser.Native_category_binding_listContext, self).copyFrom(ctx)


    class NativeCategoryBindingListItemContext(Native_category_binding_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_category_binding_listContext)
            super(OParser.NativeCategoryBindingListItemContext, self).__init__(parser)
            self.items = None # Native_category_binding_listContext
            self.item = None # Native_category_bindingContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)
        def native_category_binding_list(self):
            return self.getTypedRuleContext(OParser.Native_category_binding_listContext,0)

        def native_category_binding(self):
            return self.getTypedRuleContext(OParser.Native_category_bindingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNativeCategoryBindingListItem"):
                listener.enterNativeCategoryBindingListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNativeCategoryBindingListItem"):
                listener.exitNativeCategoryBindingListItem(self)


    class NativeCategoryBindingListContext(Native_category_binding_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_category_binding_listContext)
            super(OParser.NativeCategoryBindingListContext, self).__init__(parser)
            self.item = None # Native_category_bindingContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)
        def native_category_binding(self):
            return self.getTypedRuleContext(OParser.Native_category_bindingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNativeCategoryBindingList"):
                listener.enterNativeCategoryBindingList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNativeCategoryBindingList"):
                listener.exitNativeCategoryBindingList(self)



    def native_category_binding_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Native_category_binding_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_native_category_binding_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.NativeCategoryBindingListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 656
            localctx.item = self.native_category_binding()
            self.state = 657
            self.match(OParser.SEMI)
            self._ctx.stop = self._input.LT(-1)
            self.state = 665
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.NativeCategoryBindingListItemContext(self, OParser.Native_category_binding_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_category_binding_list)
                    self.state = 659
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 660
                    localctx.item = self.native_category_binding()
                    self.state = 661
                    self.match(OParser.SEMI) 
                self.state = 667
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Abstract_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Abstract_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # TypedefContext
            self.name = None # Method_identifierContext
            self.args = None # Argument_listContext

        def ABSTRACT(self):
            return self.getToken(OParser.ABSTRACT, 0)

        def METHOD(self):
            return self.getToken(OParser.METHOD, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def method_identifier(self):
            return self.getTypedRuleContext(OParser.Method_identifierContext,0)


        def typedef(self):
            return self.getTypedRuleContext(OParser.TypedefContext,0)


        def argument_list(self):
            return self.getTypedRuleContext(OParser.Argument_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_abstract_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterAbstract_method_declaration"):
                listener.enterAbstract_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAbstract_method_declaration"):
                listener.exitAbstract_method_declaration(self)




    def abstract_method_declaration(self):

        localctx = OParser.Abstract_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_abstract_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 668
            self.match(OParser.ABSTRACT)
            self.state = 670
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or _la==OParser.TYPE_IDENTIFIER:
                self.state = 669
                localctx.typ = self.typedef(0)


            self.state = 672
            self.match(OParser.METHOD)
            self.state = 673
            localctx.name = self.method_identifier()
            self.state = 674
            self.match(OParser.LPAR)
            self.state = 676
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ANY - 46)))) != 0) or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (OParser.MUTABLE - 115)) | (1 << (OParser.TYPE_IDENTIFIER - 115)) | (1 << (OParser.VARIABLE_IDENTIFIER - 115)))) != 0):
                self.state = 675
                localctx.args = self.argument_list()


            self.state = 678
            self.match(OParser.RPAR)
            self.state = 679
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Concrete_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Concrete_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # TypedefContext
            self.name = None # Method_identifierContext
            self.args = None # Argument_listContext
            self.stmts = None # Statement_listContext

        def METHOD(self):
            return self.getToken(OParser.METHOD, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def method_identifier(self):
            return self.getTypedRuleContext(OParser.Method_identifierContext,0)


        def typedef(self):
            return self.getTypedRuleContext(OParser.TypedefContext,0)


        def argument_list(self):
            return self.getTypedRuleContext(OParser.Argument_listContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_concrete_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterConcrete_method_declaration"):
                listener.enterConcrete_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConcrete_method_declaration"):
                listener.exitConcrete_method_declaration(self)




    def concrete_method_declaration(self):

        localctx = OParser.Concrete_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_concrete_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 682
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or _la==OParser.TYPE_IDENTIFIER:
                self.state = 681
                localctx.typ = self.typedef(0)


            self.state = 684
            self.match(OParser.METHOD)
            self.state = 685
            localctx.name = self.method_identifier()
            self.state = 686
            self.match(OParser.LPAR)
            self.state = 688
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ANY - 46)))) != 0) or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (OParser.MUTABLE - 115)) | (1 << (OParser.TYPE_IDENTIFIER - 115)) | (1 << (OParser.VARIABLE_IDENTIFIER - 115)))) != 0):
                self.state = 687
                localctx.args = self.argument_list()


            self.state = 690
            self.match(OParser.RPAR)
            self.state = 691
            self.match(OParser.LCURL)
            self.state = 693
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                self.state = 692
                localctx.stmts = self.statement_list()


            self.state = 695
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # Category_or_any_typeContext
            self.name = None # Method_identifierContext
            self.args = None # Argument_listContext
            self.stmts = None # Native_statement_listContext

        def METHOD(self):
            return self.getToken(OParser.METHOD, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def method_identifier(self):
            return self.getTypedRuleContext(OParser.Method_identifierContext,0)


        def native_statement_list(self):
            return self.getTypedRuleContext(OParser.Native_statement_listContext,0)


        def NATIVE(self):
            return self.getToken(OParser.NATIVE, 0)

        def category_or_any_type(self):
            return self.getTypedRuleContext(OParser.Category_or_any_typeContext,0)


        def argument_list(self):
            return self.getTypedRuleContext(OParser.Argument_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_native_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_method_declaration"):
                listener.enterNative_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_method_declaration"):
                listener.exitNative_method_declaration(self)




    def native_method_declaration(self):

        localctx = OParser.Native_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_native_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 698
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ANY - 46)))) != 0) or _la==OParser.TYPE_IDENTIFIER:
                self.state = 697
                localctx.typ = self.category_or_any_type()


            self.state = 701
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.NATIVE:
                self.state = 700
                self.match(OParser.NATIVE)


            self.state = 703
            self.match(OParser.METHOD)
            self.state = 704
            localctx.name = self.method_identifier()
            self.state = 705
            self.match(OParser.LPAR)
            self.state = 707
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ANY - 46)))) != 0) or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (OParser.MUTABLE - 115)) | (1 << (OParser.TYPE_IDENTIFIER - 115)) | (1 << (OParser.VARIABLE_IDENTIFIER - 115)))) != 0):
                self.state = 706
                localctx.args = self.argument_list()


            self.state = 709
            self.match(OParser.RPAR)
            self.state = 710
            self.match(OParser.LCURL)
            self.state = 711
            localctx.stmts = self.native_statement_list()
            self.state = 712
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Test_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Test_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.stmts = None # Statement_listContext
            self.exps = None # Assertion_listContext
            self.error = None # Symbol_identifierContext

        def TEST(self):
            return self.getToken(OParser.TEST, 0)

        def METHOD(self):
            return self.getToken(OParser.METHOD, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def LCURL(self, i=None):
            if i is None:
                return self.getTokens(OParser.LCURL)
            else:
                return self.getToken(OParser.LCURL, i)

        def RCURL(self, i=None):
            if i is None:
                return self.getTokens(OParser.RCURL)
            else:
                return self.getToken(OParser.RCURL, i)

        def VERIFYING(self):
            return self.getToken(OParser.VERIFYING, 0)

        def TEXT_LITERAL(self):
            return self.getToken(OParser.TEXT_LITERAL, 0)

        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def assertion_list(self):
            return self.getTypedRuleContext(OParser.Assertion_listContext,0)


        def symbol_identifier(self):
            return self.getTypedRuleContext(OParser.Symbol_identifierContext,0)


        def getRuleIndex(self):
            return OParser.RULE_test_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterTest_method_declaration"):
                listener.enterTest_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTest_method_declaration"):
                listener.exitTest_method_declaration(self)




    def test_method_declaration(self):

        localctx = OParser.Test_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_test_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 714
            self.match(OParser.TEST)
            self.state = 715
            self.match(OParser.METHOD)
            self.state = 716
            localctx.name = self.match(OParser.TEXT_LITERAL)
            self.state = 717
            self.match(OParser.LPAR)
            self.state = 718
            self.match(OParser.RPAR)
            self.state = 719
            self.match(OParser.LCURL)
            self.state = 720
            localctx.stmts = self.statement_list()
            self.state = 721
            self.match(OParser.RCURL)
            self.state = 722
            self.match(OParser.VERIFYING)
            self.state = 730
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.LCURL]:
                self.state = 723
                self.match(OParser.LCURL)
                self.state = 724
                localctx.exps = self.assertion_list()
                self.state = 725
                self.match(OParser.RCURL)
                pass
            elif token in [OParser.SYMBOL_IDENTIFIER]:
                self.state = 727
                localctx.error = self.symbol_identifier()
                self.state = 728
                self.match(OParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssertionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.AssertionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_assertion

        def enterRule(self, listener):
            if hasattr(listener, "enterAssertion"):
                listener.enterAssertion(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssertion"):
                listener.exitAssertion(self)




    def assertion(self):

        localctx = OParser.AssertionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 732
            localctx.exp = self.expression(0)
            self.state = 733
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Typed_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Typed_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # Category_or_any_typeContext
            self.attrs = None # Attribute_identifier_listContext
            self.name = None # Variable_identifierContext
            self.value = None # Literal_expressionContext

        def category_or_any_type(self):
            return self.getTypedRuleContext(OParser.Category_or_any_typeContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def EQ(self):
            return self.getToken(OParser.EQ, 0)

        def attribute_identifier_list(self):
            return self.getTypedRuleContext(OParser.Attribute_identifier_listContext,0)


        def literal_expression(self):
            return self.getTypedRuleContext(OParser.Literal_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_typed_argument

        def enterRule(self, listener):
            if hasattr(listener, "enterTyped_argument"):
                listener.enterTyped_argument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTyped_argument"):
                listener.exitTyped_argument(self)




    def typed_argument(self):

        localctx = OParser.Typed_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_typed_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 735
            localctx.typ = self.category_or_any_type()
            self.state = 740
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 736
                self.match(OParser.LPAR)
                self.state = 737
                localctx.attrs = self.attribute_identifier_list()
                self.state = 738
                self.match(OParser.RPAR)


            self.state = 742
            localctx.name = self.variable_identifier()
            self.state = 745
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.EQ:
                self.state = 743
                self.match(OParser.EQ)
                self.state = 744
                localctx.value = self.literal_expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Statement_or_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Statement_or_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_statement_or_list

     
        def copyFrom(self, ctx):
            super(OParser.Statement_or_listContext, self).copyFrom(ctx)



    class CurlyStatementListContext(Statement_or_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Statement_or_listContext)
            super(OParser.CurlyStatementListContext, self).__init__(parser)
            self.items = None # Statement_listContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)
        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCurlyStatementList"):
                listener.enterCurlyStatementList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCurlyStatementList"):
                listener.exitCurlyStatementList(self)


    class SingleStatementContext(Statement_or_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Statement_or_listContext)
            super(OParser.SingleStatementContext, self).__init__(parser)
            self.stmt = None # StatementContext
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(OParser.StatementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSingleStatement"):
                listener.enterSingleStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSingleStatement"):
                listener.exitSingleStatement(self)



    def statement_or_list(self):

        localctx = OParser.Statement_or_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_statement_or_list)
        try:
            self.state = 754
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.COMMENT, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID, OParser.ITERATOR, OParser.CURSOR, OParser.BREAK, OParser.DELETE, OParser.DO, OParser.FLUSH, OParser.FOR, OParser.IF, OParser.METHOD, OParser.RETURN, OParser.STORE, OParser.SWITCH, OParser.THROW, OParser.TRY, OParser.WITH, OParser.WHILE, OParser.WRITE, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER]:
                localctx = OParser.SingleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 747
                localctx.stmt = self.statement()
                pass
            elif token in [OParser.LCURL]:
                localctx = OParser.CurlyStatementListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 748
                self.match(OParser.LCURL)
                self.state = 752
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                if la_ == 1:
                    self.state = 749
                    localctx.items = self.statement_list()
                    self.state = 750
                    self.match(OParser.RCURL)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_statement

     
        def copyFrom(self, ctx):
            super(OParser.StatementContext, self).copyFrom(ctx)



    class CommentStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.CommentStatementContext, self).__init__(parser)
            self.decl = None # Comment_statementContext
            self.copyFrom(ctx)

        def comment_statement(self):
            return self.getTypedRuleContext(OParser.Comment_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCommentStatement"):
                listener.enterCommentStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCommentStatement"):
                listener.exitCommentStatement(self)


    class StoreStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.StoreStatementContext, self).__init__(parser)
            self.stmt = None # Store_statementContext
            self.copyFrom(ctx)

        def store_statement(self):
            return self.getTypedRuleContext(OParser.Store_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterStoreStatement"):
                listener.enterStoreStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStoreStatement"):
                listener.exitStoreStatement(self)


    class WithSingletonStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.WithSingletonStatementContext, self).__init__(parser)
            self.stmt = None # With_singleton_statementContext
            self.copyFrom(ctx)

        def with_singleton_statement(self):
            return self.getTypedRuleContext(OParser.With_singleton_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterWithSingletonStatement"):
                listener.enterWithSingletonStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWithSingletonStatement"):
                listener.exitWithSingletonStatement(self)


    class WriteStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.WriteStatementContext, self).__init__(parser)
            self.stmt = None # Write_statementContext
            self.copyFrom(ctx)

        def write_statement(self):
            return self.getTypedRuleContext(OParser.Write_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterWriteStatement"):
                listener.enterWriteStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWriteStatement"):
                listener.exitWriteStatement(self)


    class WhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.WhileStatementContext, self).__init__(parser)
            self.stmt = None # While_statementContext
            self.copyFrom(ctx)

        def while_statement(self):
            return self.getTypedRuleContext(OParser.While_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterWhileStatement"):
                listener.enterWhileStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWhileStatement"):
                listener.exitWhileStatement(self)


    class WithResourceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.WithResourceStatementContext, self).__init__(parser)
            self.stmt = None # With_resource_statementContext
            self.copyFrom(ctx)

        def with_resource_statement(self):
            return self.getTypedRuleContext(OParser.With_resource_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterWithResourceStatement"):
                listener.enterWithResourceStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWithResourceStatement"):
                listener.exitWithResourceStatement(self)


    class RaiseStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.RaiseStatementContext, self).__init__(parser)
            self.stmt = None # Raise_statementContext
            self.copyFrom(ctx)

        def raise_statement(self):
            return self.getTypedRuleContext(OParser.Raise_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterRaiseStatement"):
                listener.enterRaiseStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRaiseStatement"):
                listener.exitRaiseStatement(self)


    class BreakStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.BreakStatementContext, self).__init__(parser)
            self.stmt = None # Break_statementContext
            self.copyFrom(ctx)

        def break_statement(self):
            return self.getTypedRuleContext(OParser.Break_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterBreakStatement"):
                listener.enterBreakStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBreakStatement"):
                listener.exitBreakStatement(self)


    class AssignInstanceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.AssignInstanceStatementContext, self).__init__(parser)
            self.stmt = None # Assign_instance_statementContext
            self.copyFrom(ctx)

        def assign_instance_statement(self):
            return self.getTypedRuleContext(OParser.Assign_instance_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterAssignInstanceStatement"):
                listener.enterAssignInstanceStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssignInstanceStatement"):
                listener.exitAssignInstanceStatement(self)


    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.IfStatementContext, self).__init__(parser)
            self.stmt = None # If_statementContext
            self.copyFrom(ctx)

        def if_statement(self):
            return self.getTypedRuleContext(OParser.If_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIfStatement"):
                listener.enterIfStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIfStatement"):
                listener.exitIfStatement(self)


    class SwitchStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.SwitchStatementContext, self).__init__(parser)
            self.stmt = None # Switch_statementContext
            self.copyFrom(ctx)

        def switch_statement(self):
            return self.getTypedRuleContext(OParser.Switch_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSwitchStatement"):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSwitchStatement"):
                listener.exitSwitchStatement(self)


    class TryStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.TryStatementContext, self).__init__(parser)
            self.stmt = None # Try_statementContext
            self.copyFrom(ctx)

        def try_statement(self):
            return self.getTypedRuleContext(OParser.Try_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterTryStatement"):
                listener.enterTryStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTryStatement"):
                listener.exitTryStatement(self)


    class MethodCallStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.MethodCallStatementContext, self).__init__(parser)
            self.stmt = None # Method_callContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)
        def method_call(self):
            return self.getTypedRuleContext(OParser.Method_callContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMethodCallStatement"):
                listener.enterMethodCallStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethodCallStatement"):
                listener.exitMethodCallStatement(self)


    class ReturnStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.ReturnStatementContext, self).__init__(parser)
            self.stmt = None # Return_statementContext
            self.copyFrom(ctx)

        def return_statement(self):
            return self.getTypedRuleContext(OParser.Return_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterReturnStatement"):
                listener.enterReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitReturnStatement"):
                listener.exitReturnStatement(self)


    class AssignTupleStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.AssignTupleStatementContext, self).__init__(parser)
            self.stmt = None # Assign_tuple_statementContext
            self.copyFrom(ctx)

        def assign_tuple_statement(self):
            return self.getTypedRuleContext(OParser.Assign_tuple_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterAssignTupleStatement"):
                listener.enterAssignTupleStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssignTupleStatement"):
                listener.exitAssignTupleStatement(self)


    class ClosureStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.ClosureStatementContext, self).__init__(parser)
            self.decl = None # Concrete_method_declarationContext
            self.copyFrom(ctx)

        def concrete_method_declaration(self):
            return self.getTypedRuleContext(OParser.Concrete_method_declarationContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterClosureStatement"):
                listener.enterClosureStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitClosureStatement"):
                listener.exitClosureStatement(self)


    class FlushStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.FlushStatementContext, self).__init__(parser)
            self.stmt = None # Flush_statementContext
            self.copyFrom(ctx)

        def flush_statement(self):
            return self.getTypedRuleContext(OParser.Flush_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterFlushStatement"):
                listener.enterFlushStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFlushStatement"):
                listener.exitFlushStatement(self)


    class DoWhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.DoWhileStatementContext, self).__init__(parser)
            self.stmt = None # Do_while_statementContext
            self.copyFrom(ctx)

        def do_while_statement(self):
            return self.getTypedRuleContext(OParser.Do_while_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterDoWhileStatement"):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDoWhileStatement"):
                listener.exitDoWhileStatement(self)


    class ForEachStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a OParser.StatementContext)
            super(OParser.ForEachStatementContext, self).__init__(parser)
            self.stmt = None # For_each_statementContext
            self.copyFrom(ctx)

        def for_each_statement(self):
            return self.getTypedRuleContext(OParser.For_each_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterForEachStatement"):
                listener.enterForEachStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitForEachStatement"):
                listener.exitForEachStatement(self)



    def statement(self):

        localctx = OParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_statement)
        try:
            self.state = 777
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                localctx = OParser.MethodCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 756
                localctx.stmt = self.method_call()
                self.state = 757
                self.match(OParser.SEMI)
                pass

            elif la_ == 2:
                localctx = OParser.AssignInstanceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 759
                localctx.stmt = self.assign_instance_statement()
                pass

            elif la_ == 3:
                localctx = OParser.AssignTupleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 760
                localctx.stmt = self.assign_tuple_statement()
                pass

            elif la_ == 4:
                localctx = OParser.StoreStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 761
                localctx.stmt = self.store_statement()
                pass

            elif la_ == 5:
                localctx = OParser.FlushStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 762
                localctx.stmt = self.flush_statement()
                pass

            elif la_ == 6:
                localctx = OParser.BreakStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 763
                localctx.stmt = self.break_statement()
                pass

            elif la_ == 7:
                localctx = OParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 764
                localctx.stmt = self.return_statement()
                pass

            elif la_ == 8:
                localctx = OParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 765
                localctx.stmt = self.if_statement()
                pass

            elif la_ == 9:
                localctx = OParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 766
                localctx.stmt = self.switch_statement()
                pass

            elif la_ == 10:
                localctx = OParser.ForEachStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 767
                localctx.stmt = self.for_each_statement()
                pass

            elif la_ == 11:
                localctx = OParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 768
                localctx.stmt = self.while_statement()
                pass

            elif la_ == 12:
                localctx = OParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 769
                localctx.stmt = self.do_while_statement()
                pass

            elif la_ == 13:
                localctx = OParser.TryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 770
                localctx.stmt = self.try_statement()
                pass

            elif la_ == 14:
                localctx = OParser.RaiseStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 771
                localctx.stmt = self.raise_statement()
                pass

            elif la_ == 15:
                localctx = OParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 772
                localctx.stmt = self.write_statement()
                pass

            elif la_ == 16:
                localctx = OParser.WithResourceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 773
                localctx.stmt = self.with_resource_statement()
                pass

            elif la_ == 17:
                localctx = OParser.WithSingletonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 774
                localctx.stmt = self.with_singleton_statement()
                pass

            elif la_ == 18:
                localctx = OParser.ClosureStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 775
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 19:
                localctx = OParser.CommentStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 19)
                self.state = 776
                localctx.decl = self.comment_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Flush_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Flush_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FLUSH(self):
            return self.getToken(OParser.FLUSH, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def getRuleIndex(self):
            return OParser.RULE_flush_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterFlush_statement"):
                listener.enterFlush_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFlush_statement"):
                listener.exitFlush_statement(self)




    def flush_statement(self):

        localctx = OParser.Flush_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_flush_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 779
            self.match(OParser.FLUSH)
            self.state = 780
            self.match(OParser.LPAR)
            self.state = 781
            self.match(OParser.RPAR)
            self.state = 782
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Store_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Store_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.to_del = None # Expression_listContext
            self.to_add = None # Expression_listContext

        def DELETE(self):
            return self.getToken(OParser.DELETE, 0)

        def LPAR(self, i=None):
            if i is None:
                return self.getTokens(OParser.LPAR)
            else:
                return self.getToken(OParser.LPAR, i)

        def RPAR(self, i=None):
            if i is None:
                return self.getTokens(OParser.RPAR)
            else:
                return self.getToken(OParser.RPAR, i)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def expression_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Expression_listContext)
            else:
                return self.getTypedRuleContext(OParser.Expression_listContext,i)


        def STORE(self):
            return self.getToken(OParser.STORE, 0)

        def AND(self):
            return self.getToken(OParser.AND, 0)

        def getRuleIndex(self):
            return OParser.RULE_store_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterStore_statement"):
                listener.enterStore_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStore_statement"):
                listener.exitStore_statement(self)




    def store_statement(self):

        localctx = OParser.Store_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_store_statement)
        try:
            self.state = 807
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 784
                self.match(OParser.DELETE)
                self.state = 785
                self.match(OParser.LPAR)
                self.state = 786
                localctx.to_del = self.expression_list()
                self.state = 787
                self.match(OParser.RPAR)
                self.state = 788
                self.match(OParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 790
                self.match(OParser.STORE)
                self.state = 791
                self.match(OParser.LPAR)
                self.state = 792
                localctx.to_add = self.expression_list()
                self.state = 793
                self.match(OParser.RPAR)
                self.state = 794
                self.match(OParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 796
                self.match(OParser.DELETE)
                self.state = 797
                self.match(OParser.LPAR)
                self.state = 798
                localctx.to_del = self.expression_list()
                self.state = 799
                self.match(OParser.RPAR)
                self.state = 800
                self.match(OParser.AND)
                self.state = 801
                self.match(OParser.STORE)
                self.state = 802
                self.match(OParser.LPAR)
                self.state = 803
                localctx.to_add = self.expression_list()
                self.state = 804
                self.match(OParser.RPAR)
                self.state = 805
                self.match(OParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class With_resource_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.With_resource_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmt = None # Assign_variable_statementContext
            self.stmts = None # Statement_or_listContext

        def WITH(self):
            return self.getToken(OParser.WITH, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def assign_variable_statement(self):
            return self.getTypedRuleContext(OParser.Assign_variable_statementContext,0)


        def statement_or_list(self):
            return self.getTypedRuleContext(OParser.Statement_or_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_with_resource_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterWith_resource_statement"):
                listener.enterWith_resource_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWith_resource_statement"):
                listener.exitWith_resource_statement(self)




    def with_resource_statement(self):

        localctx = OParser.With_resource_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_with_resource_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 809
            self.match(OParser.WITH)
            self.state = 810
            self.match(OParser.LPAR)
            self.state = 811
            localctx.stmt = self.assign_variable_statement()
            self.state = 812
            self.match(OParser.RPAR)
            self.state = 813
            localctx.stmts = self.statement_or_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class With_singleton_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.With_singleton_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # Type_identifierContext
            self.stmts = None # Statement_or_listContext

        def WITH(self):
            return self.getToken(OParser.WITH, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def statement_or_list(self):
            return self.getTypedRuleContext(OParser.Statement_or_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_with_singleton_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterWith_singleton_statement"):
                listener.enterWith_singleton_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWith_singleton_statement"):
                listener.exitWith_singleton_statement(self)




    def with_singleton_statement(self):

        localctx = OParser.With_singleton_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_with_singleton_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 815
            self.match(OParser.WITH)
            self.state = 816
            self.match(OParser.LPAR)
            self.state = 817
            localctx.typ = self.type_identifier()
            self.state = 818
            self.match(OParser.RPAR)
            self.state = 819
            localctx.stmts = self.statement_or_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Switch_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Switch_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.cases = None # Switch_case_statement_listContext
            self.stmts = None # Statement_listContext

        def SWITCH(self):
            return self.getToken(OParser.SWITCH, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def switch_case_statement_list(self):
            return self.getTypedRuleContext(OParser.Switch_case_statement_listContext,0)


        def DEFAULT(self):
            return self.getToken(OParser.DEFAULT, 0)

        def COLON(self):
            return self.getToken(OParser.COLON, 0)

        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_switch_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterSwitch_statement"):
                listener.enterSwitch_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSwitch_statement"):
                listener.exitSwitch_statement(self)




    def switch_statement(self):

        localctx = OParser.Switch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_switch_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 821
            self.match(OParser.SWITCH)
            self.state = 822
            self.match(OParser.LPAR)
            self.state = 823
            localctx.exp = self.expression(0)
            self.state = 824
            self.match(OParser.RPAR)
            self.state = 825
            self.match(OParser.LCURL)
            self.state = 826
            localctx.cases = self.switch_case_statement_list()
            self.state = 832
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.DEFAULT:
                self.state = 827
                self.match(OParser.DEFAULT)
                self.state = 828
                self.match(OParser.COLON)
                self.state = 830
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                    self.state = 829
                    localctx.stmts = self.statement_list()




            self.state = 834
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Switch_case_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Switch_case_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_switch_case_statement

     
        def copyFrom(self, ctx):
            super(OParser.Switch_case_statementContext, self).copyFrom(ctx)



    class AtomicSwitchCaseContext(Switch_case_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Switch_case_statementContext)
            super(OParser.AtomicSwitchCaseContext, self).__init__(parser)
            self.exp = None # Atomic_literalContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def CASE(self):
            return self.getToken(OParser.CASE, 0)
        def COLON(self):
            return self.getToken(OParser.COLON, 0)
        def atomic_literal(self):
            return self.getTypedRuleContext(OParser.Atomic_literalContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterAtomicSwitchCase"):
                listener.enterAtomicSwitchCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAtomicSwitchCase"):
                listener.exitAtomicSwitchCase(self)


    class CollectionSwitchCaseContext(Switch_case_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Switch_case_statementContext)
            super(OParser.CollectionSwitchCaseContext, self).__init__(parser)
            self.exp = None # Literal_collectionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def CASE(self):
            return self.getToken(OParser.CASE, 0)
        def IN(self):
            return self.getToken(OParser.IN, 0)
        def COLON(self):
            return self.getToken(OParser.COLON, 0)
        def literal_collection(self):
            return self.getTypedRuleContext(OParser.Literal_collectionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCollectionSwitchCase"):
                listener.enterCollectionSwitchCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCollectionSwitchCase"):
                listener.exitCollectionSwitchCase(self)



    def switch_case_statement(self):

        localctx = OParser.Switch_case_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_switch_case_statement)
        self._la = 0 # Token type
        try:
            self.state = 849
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                localctx = OParser.AtomicSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 836
                self.match(OParser.CASE)
                self.state = 837
                localctx.exp = self.atomic_literal()
                self.state = 838
                self.match(OParser.COLON)
                self.state = 840
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                    self.state = 839
                    localctx.stmts = self.statement_list()


                pass

            elif la_ == 2:
                localctx = OParser.CollectionSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 842
                self.match(OParser.CASE)
                self.state = 843
                self.match(OParser.IN)
                self.state = 844
                localctx.exp = self.literal_collection()
                self.state = 845
                self.match(OParser.COLON)
                self.state = 847
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                    self.state = 846
                    localctx.stmts = self.statement_list()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class For_each_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.For_each_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name1 = None # Variable_identifierContext
            self.name2 = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.stmts = None # Statement_or_listContext

        def FOR(self):
            return self.getToken(OParser.FOR, 0)

        def EACH(self):
            return self.getToken(OParser.EACH, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def IN(self):
            return self.getToken(OParser.IN, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(OParser.Variable_identifierContext,i)


        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def statement_or_list(self):
            return self.getTypedRuleContext(OParser.Statement_or_listContext,0)


        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)

        def getRuleIndex(self):
            return OParser.RULE_for_each_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterFor_each_statement"):
                listener.enterFor_each_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFor_each_statement"):
                listener.exitFor_each_statement(self)




    def for_each_statement(self):

        localctx = OParser.For_each_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_for_each_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 851
            self.match(OParser.FOR)
            self.state = 852
            self.match(OParser.EACH)
            self.state = 853
            self.match(OParser.LPAR)
            self.state = 854
            localctx.name1 = self.variable_identifier()
            self.state = 857
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.COMMA:
                self.state = 855
                self.match(OParser.COMMA)
                self.state = 856
                localctx.name2 = self.variable_identifier()


            self.state = 859
            self.match(OParser.IN)
            self.state = 860
            localctx.source = self.expression(0)
            self.state = 861
            self.match(OParser.RPAR)
            self.state = 862
            localctx.stmts = self.statement_or_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Do_while_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Do_while_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmts = None # Statement_listContext
            self.exp = None # ExpressionContext

        def DO(self):
            return self.getToken(OParser.DO, 0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def WHILE(self):
            return self.getToken(OParser.WHILE, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_do_while_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterDo_while_statement"):
                listener.enterDo_while_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDo_while_statement"):
                listener.exitDo_while_statement(self)




    def do_while_statement(self):

        localctx = OParser.Do_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_do_while_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 864
            self.match(OParser.DO)
            self.state = 865
            self.match(OParser.LCURL)
            self.state = 867
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                self.state = 866
                localctx.stmts = self.statement_list()


            self.state = 869
            self.match(OParser.RCURL)
            self.state = 870
            self.match(OParser.WHILE)
            self.state = 871
            self.match(OParser.LPAR)
            self.state = 872
            localctx.exp = self.expression(0)
            self.state = 873
            self.match(OParser.RPAR)
            self.state = 874
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class While_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.While_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_or_listContext

        def WHILE(self):
            return self.getToken(OParser.WHILE, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def statement_or_list(self):
            return self.getTypedRuleContext(OParser.Statement_or_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_while_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterWhile_statement"):
                listener.enterWhile_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWhile_statement"):
                listener.exitWhile_statement(self)




    def while_statement(self):

        localctx = OParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 876
            self.match(OParser.WHILE)
            self.state = 877
            self.match(OParser.LPAR)
            self.state = 878
            localctx.exp = self.expression(0)
            self.state = 879
            self.match(OParser.RPAR)
            self.state = 880
            localctx.stmts = self.statement_or_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.If_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_or_listContext
            self.elseIfs = None # Else_if_statement_listContext
            self.elseStmts = None # Statement_or_listContext

        def IF(self):
            return self.getToken(OParser.IF, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def statement_or_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Statement_or_listContext)
            else:
                return self.getTypedRuleContext(OParser.Statement_or_listContext,i)


        def ELSE(self):
            return self.getToken(OParser.ELSE, 0)

        def else_if_statement_list(self):
            return self.getTypedRuleContext(OParser.Else_if_statement_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_if_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterIf_statement"):
                listener.enterIf_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIf_statement"):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = OParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 882
            self.match(OParser.IF)
            self.state = 883
            self.match(OParser.LPAR)
            self.state = 884
            localctx.exp = self.expression(0)
            self.state = 885
            self.match(OParser.RPAR)
            self.state = 886
            localctx.stmts = self.statement_or_list()
            self.state = 888
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 887
                localctx.elseIfs = self.else_if_statement_list(0)


            self.state = 892
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.state = 890
                self.match(OParser.ELSE)
                self.state = 891
                localctx.elseStmts = self.statement_or_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Else_if_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Else_if_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_else_if_statement_list

     
        def copyFrom(self, ctx):
            super(OParser.Else_if_statement_listContext, self).copyFrom(ctx)


    class ElseIfStatementListContext(Else_if_statement_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Else_if_statement_listContext)
            super(OParser.ElseIfStatementListContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_or_listContext
            self.copyFrom(ctx)

        def ELSE(self):
            return self.getToken(OParser.ELSE, 0)
        def IF(self):
            return self.getToken(OParser.IF, 0)
        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)

        def statement_or_list(self):
            return self.getTypedRuleContext(OParser.Statement_or_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterElseIfStatementList"):
                listener.enterElseIfStatementList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitElseIfStatementList"):
                listener.exitElseIfStatementList(self)


    class ElseIfStatementListItemContext(Else_if_statement_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Else_if_statement_listContext)
            super(OParser.ElseIfStatementListItemContext, self).__init__(parser)
            self.items = None # Else_if_statement_listContext
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_or_listContext
            self.copyFrom(ctx)

        def ELSE(self):
            return self.getToken(OParser.ELSE, 0)
        def IF(self):
            return self.getToken(OParser.IF, 0)
        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)
        def else_if_statement_list(self):
            return self.getTypedRuleContext(OParser.Else_if_statement_listContext,0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)

        def statement_or_list(self):
            return self.getTypedRuleContext(OParser.Statement_or_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterElseIfStatementListItem"):
                listener.enterElseIfStatementListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitElseIfStatementListItem"):
                listener.exitElseIfStatementListItem(self)



    def else_if_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Else_if_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_else_if_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.ElseIfStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 895
            self.match(OParser.ELSE)
            self.state = 896
            self.match(OParser.IF)
            self.state = 897
            self.match(OParser.LPAR)
            self.state = 898
            localctx.exp = self.expression(0)
            self.state = 899
            self.match(OParser.RPAR)
            self.state = 900
            localctx.stmts = self.statement_or_list()
            self._ctx.stop = self._input.LT(-1)
            self.state = 912
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.ElseIfStatementListItemContext(self, OParser.Else_if_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_else_if_statement_list)
                    self.state = 902
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 903
                    self.match(OParser.ELSE)
                    self.state = 904
                    self.match(OParser.IF)
                    self.state = 905
                    self.match(OParser.LPAR)
                    self.state = 906
                    localctx.exp = self.expression(0)
                    self.state = 907
                    self.match(OParser.RPAR)
                    self.state = 908
                    localctx.stmts = self.statement_or_list() 
                self.state = 914
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Raise_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Raise_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def THROW(self):
            return self.getToken(OParser.THROW, 0)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_raise_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterRaise_statement"):
                listener.enterRaise_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRaise_statement"):
                listener.exitRaise_statement(self)




    def raise_statement(self):

        localctx = OParser.Raise_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_raise_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 915
            self.match(OParser.THROW)
            self.state = 916
            localctx.exp = self.expression(0)
            self.state = 917
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Try_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Try_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext
            self.handlers = None # Catch_statement_listContext
            self.anyStmts = None # Statement_listContext
            self.finalStmts = None # Statement_listContext

        def TRY(self):
            return self.getToken(OParser.TRY, 0)

        def LPAR(self, i=None):
            if i is None:
                return self.getTokens(OParser.LPAR)
            else:
                return self.getToken(OParser.LPAR, i)

        def RPAR(self, i=None):
            if i is None:
                return self.getTokens(OParser.RPAR)
            else:
                return self.getToken(OParser.RPAR, i)

        def LCURL(self, i=None):
            if i is None:
                return self.getTokens(OParser.LCURL)
            else:
                return self.getToken(OParser.LCURL, i)

        def RCURL(self, i=None):
            if i is None:
                return self.getTokens(OParser.RCURL)
            else:
                return self.getToken(OParser.RCURL, i)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def CATCH(self):
            return self.getToken(OParser.CATCH, 0)

        def ANY(self):
            return self.getToken(OParser.ANY, 0)

        def FINALLY(self):
            return self.getToken(OParser.FINALLY, 0)

        def statement_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(OParser.Statement_listContext,i)


        def catch_statement_list(self):
            return self.getTypedRuleContext(OParser.Catch_statement_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_try_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterTry_statement"):
                listener.enterTry_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTry_statement"):
                listener.exitTry_statement(self)




    def try_statement(self):

        localctx = OParser.Try_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_try_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 919
            self.match(OParser.TRY)
            self.state = 920
            self.match(OParser.LPAR)
            self.state = 921
            localctx.name = self.variable_identifier()
            self.state = 922
            self.match(OParser.RPAR)
            self.state = 923
            self.match(OParser.LCURL)
            self.state = 925
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                self.state = 924
                localctx.stmts = self.statement_list()


            self.state = 927
            self.match(OParser.RCURL)
            self.state = 929
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.state = 928
                localctx.handlers = self.catch_statement_list()


            self.state = 940
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.state = 931
                self.match(OParser.CATCH)
                self.state = 932
                self.match(OParser.LPAR)
                self.state = 933
                self.match(OParser.ANY)
                self.state = 934
                self.match(OParser.RPAR)
                self.state = 935
                self.match(OParser.LCURL)
                self.state = 937
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                    self.state = 936
                    localctx.anyStmts = self.statement_list()


                self.state = 939
                self.match(OParser.RCURL)


            self.state = 948
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.state = 942
                self.match(OParser.FINALLY)
                self.state = 943
                self.match(OParser.LCURL)
                self.state = 945
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                    self.state = 944
                    localctx.finalStmts = self.statement_list()


                self.state = 947
                self.match(OParser.RCURL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Catch_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Catch_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_catch_statement

     
        def copyFrom(self, ctx):
            super(OParser.Catch_statementContext, self).copyFrom(ctx)



    class CatchAtomicStatementContext(Catch_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Catch_statementContext)
            super(OParser.CatchAtomicStatementContext, self).__init__(parser)
            self.name = None # Symbol_identifierContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def CATCH(self):
            return self.getToken(OParser.CATCH, 0)
        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)
        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)
        def symbol_identifier(self):
            return self.getTypedRuleContext(OParser.Symbol_identifierContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCatchAtomicStatement"):
                listener.enterCatchAtomicStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCatchAtomicStatement"):
                listener.exitCatchAtomicStatement(self)


    class CatchCollectionStatementContext(Catch_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Catch_statementContext)
            super(OParser.CatchCollectionStatementContext, self).__init__(parser)
            self.exp = None # Symbol_listContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def CATCH(self):
            return self.getToken(OParser.CATCH, 0)
        def IN(self):
            return self.getToken(OParser.IN, 0)
        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)
        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)
        def symbol_list(self):
            return self.getTypedRuleContext(OParser.Symbol_listContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(OParser.Statement_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCatchCollectionStatement"):
                listener.enterCatchCollectionStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCatchCollectionStatement"):
                listener.exitCatchCollectionStatement(self)



    def catch_statement(self):

        localctx = OParser.Catch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_catch_statement)
        self._la = 0 # Token type
        try:
            self.state = 971
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                localctx = OParser.CatchAtomicStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 950
                self.match(OParser.CATCH)
                self.state = 951
                self.match(OParser.LPAR)
                self.state = 952
                localctx.name = self.symbol_identifier()
                self.state = 953
                self.match(OParser.RPAR)
                self.state = 954
                self.match(OParser.LCURL)
                self.state = 956
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                    self.state = 955
                    localctx.stmts = self.statement_list()


                self.state = 958
                self.match(OParser.RCURL)
                pass

            elif la_ == 2:
                localctx = OParser.CatchCollectionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 960
                self.match(OParser.CATCH)
                self.state = 961
                self.match(OParser.IN)
                self.state = 962
                self.match(OParser.LPAR)
                self.state = 963
                localctx.exp = self.symbol_list()
                self.state = 964
                self.match(OParser.RPAR)
                self.state = 965
                self.match(OParser.LCURL)
                self.state = 967
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                    self.state = 966
                    localctx.stmts = self.statement_list()


                self.state = 969
                self.match(OParser.RCURL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Break_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Break_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(OParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def getRuleIndex(self):
            return OParser.RULE_break_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterBreak_statement"):
                listener.enterBreak_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBreak_statement"):
                listener.exitBreak_statement(self)




    def break_statement(self):

        localctx = OParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 973
            self.match(OParser.BREAK)
            self.state = 974
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Return_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def RETURN(self):
            return self.getToken(OParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_return_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterReturn_statement"):
                listener.enterReturn_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitReturn_statement"):
                listener.exitReturn_statement(self)




    def return_statement(self):

        localctx = OParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 976
            self.match(OParser.RETURN)
            self.state = 978
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.LTGT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (OParser.EXECUTE - 95)) | (1 << (OParser.FETCH - 95)) | (1 << (OParser.FILTERED - 95)) | (1 << (OParser.MUTABLE - 95)) | (1 << (OParser.NULL - 95)) | (1 << (OParser.READ - 95)) | (1 << (OParser.SELF - 95)) | (1 << (OParser.SORTED - 95)) | (1 << (OParser.THIS - 95)) | (1 << (OParser.BOOLEAN_LITERAL - 95)) | (1 << (OParser.CHAR_LITERAL - 95)) | (1 << (OParser.MIN_INTEGER - 95)) | (1 << (OParser.MAX_INTEGER - 95)) | (1 << (OParser.SYMBOL_IDENTIFIER - 95)))) != 0) or ((((_la - 159)) & ~0x3f) == 0 and ((1 << (_la - 159)) & ((1 << (OParser.TYPE_IDENTIFIER - 159)) | (1 << (OParser.VARIABLE_IDENTIFIER - 159)) | (1 << (OParser.TEXT_LITERAL - 159)) | (1 << (OParser.UUID_LITERAL - 159)) | (1 << (OParser.INTEGER_LITERAL - 159)) | (1 << (OParser.HEXA_LITERAL - 159)) | (1 << (OParser.DECIMAL_LITERAL - 159)) | (1 << (OParser.DATETIME_LITERAL - 159)) | (1 << (OParser.TIME_LITERAL - 159)) | (1 << (OParser.DATE_LITERAL - 159)) | (1 << (OParser.PERIOD_LITERAL - 159)) | (1 << (OParser.VERSION_LITERAL - 159)))) != 0):
                self.state = 977
                localctx.exp = self.expression(0)


            self.state = 980
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_callContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Method_callContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.method = None # Method_selectorContext
            self.args = None # Argument_assignment_listContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def method_selector(self):
            return self.getTypedRuleContext(OParser.Method_selectorContext,0)


        def argument_assignment_list(self):
            return self.getTypedRuleContext(OParser.Argument_assignment_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_method_call

        def enterRule(self, listener):
            if hasattr(listener, "enterMethod_call"):
                listener.enterMethod_call(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethod_call"):
                listener.exitMethod_call(self)




    def method_call(self):

        localctx = OParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 982
            localctx.method = self.method_selector()
            self.state = 983
            self.match(OParser.LPAR)
            self.state = 985
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.LTGT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (OParser.EXECUTE - 95)) | (1 << (OParser.FETCH - 95)) | (1 << (OParser.FILTERED - 95)) | (1 << (OParser.MUTABLE - 95)) | (1 << (OParser.NULL - 95)) | (1 << (OParser.READ - 95)) | (1 << (OParser.SELF - 95)) | (1 << (OParser.SORTED - 95)) | (1 << (OParser.THIS - 95)) | (1 << (OParser.BOOLEAN_LITERAL - 95)) | (1 << (OParser.CHAR_LITERAL - 95)) | (1 << (OParser.MIN_INTEGER - 95)) | (1 << (OParser.MAX_INTEGER - 95)) | (1 << (OParser.SYMBOL_IDENTIFIER - 95)))) != 0) or ((((_la - 159)) & ~0x3f) == 0 and ((1 << (_la - 159)) & ((1 << (OParser.TYPE_IDENTIFIER - 159)) | (1 << (OParser.VARIABLE_IDENTIFIER - 159)) | (1 << (OParser.TEXT_LITERAL - 159)) | (1 << (OParser.UUID_LITERAL - 159)) | (1 << (OParser.INTEGER_LITERAL - 159)) | (1 << (OParser.HEXA_LITERAL - 159)) | (1 << (OParser.DECIMAL_LITERAL - 159)) | (1 << (OParser.DATETIME_LITERAL - 159)) | (1 << (OParser.TIME_LITERAL - 159)) | (1 << (OParser.DATE_LITERAL - 159)) | (1 << (OParser.PERIOD_LITERAL - 159)) | (1 << (OParser.VERSION_LITERAL - 159)))) != 0):
                self.state = 984
                localctx.args = self.argument_assignment_list(0)


            self.state = 987
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Method_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_method_selector

     
        def copyFrom(self, ctx):
            super(OParser.Method_selectorContext, self).copyFrom(ctx)



    class MethodParentContext(Method_selectorContext):

        def __init__(self, parser, ctx): # actually a OParser.Method_selectorContext)
            super(OParser.MethodParentContext, self).__init__(parser)
            self.parent = None # Callable_parentContext
            self.name = None # Method_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def callable_parent(self):
            return self.getTypedRuleContext(OParser.Callable_parentContext,0)

        def method_identifier(self):
            return self.getTypedRuleContext(OParser.Method_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMethodParent"):
                listener.enterMethodParent(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethodParent"):
                listener.exitMethodParent(self)


    class MethodNameContext(Method_selectorContext):

        def __init__(self, parser, ctx): # actually a OParser.Method_selectorContext)
            super(OParser.MethodNameContext, self).__init__(parser)
            self.name = None # Method_identifierContext
            self.copyFrom(ctx)

        def method_identifier(self):
            return self.getTypedRuleContext(OParser.Method_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMethodName"):
                listener.enterMethodName(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethodName"):
                listener.exitMethodName(self)



    def method_selector(self):

        localctx = OParser.Method_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_method_selector)
        try:
            self.state = 994
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                localctx = OParser.MethodNameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 989
                localctx.name = self.method_identifier()
                pass

            elif la_ == 2:
                localctx = OParser.MethodParentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 990
                localctx.parent = self.callable_parent(0)
                self.state = 991
                self.match(OParser.DOT)
                self.state = 992
                localctx.name = self.method_identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Callable_parentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Callable_parentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_callable_parent

     
        def copyFrom(self, ctx):
            super(OParser.Callable_parentContext, self).copyFrom(ctx)


    class CallableSelectorContext(Callable_parentContext):

        def __init__(self, parser, ctx): # actually a OParser.Callable_parentContext)
            super(OParser.CallableSelectorContext, self).__init__(parser)
            self.parent = None # Callable_parentContext
            self.select = None # Callable_selectorContext
            self.copyFrom(ctx)

        def callable_parent(self):
            return self.getTypedRuleContext(OParser.Callable_parentContext,0)

        def callable_selector(self):
            return self.getTypedRuleContext(OParser.Callable_selectorContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCallableSelector"):
                listener.enterCallableSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCallableSelector"):
                listener.exitCallableSelector(self)


    class CallableRootContext(Callable_parentContext):

        def __init__(self, parser, ctx): # actually a OParser.Callable_parentContext)
            super(OParser.CallableRootContext, self).__init__(parser)
            self.name = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(OParser.IdentifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCallableRoot"):
                listener.enterCallableRoot(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCallableRoot"):
                listener.exitCallableRoot(self)



    def callable_parent(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Callable_parentContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_callable_parent, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.CallableRootContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 997
            localctx.name = self.identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1003
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,65,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.CallableSelectorContext(self, OParser.Callable_parentContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_callable_parent)
                    self.state = 999
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1000
                    localctx.select = self.callable_selector() 
                self.state = 1005
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,65,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Callable_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Callable_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_callable_selector

     
        def copyFrom(self, ctx):
            super(OParser.Callable_selectorContext, self).copyFrom(ctx)



    class CallableItemSelectorContext(Callable_selectorContext):

        def __init__(self, parser, ctx): # actually a OParser.Callable_selectorContext)
            super(OParser.CallableItemSelectorContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCallableItemSelector"):
                listener.enterCallableItemSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCallableItemSelector"):
                listener.exitCallableItemSelector(self)


    class CallableMemberSelectorContext(Callable_selectorContext):

        def __init__(self, parser, ctx): # actually a OParser.Callable_selectorContext)
            super(OParser.CallableMemberSelectorContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCallableMemberSelector"):
                listener.enterCallableMemberSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCallableMemberSelector"):
                listener.exitCallableMemberSelector(self)



    def callable_selector(self):

        localctx = OParser.Callable_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_callable_selector)
        try:
            self.state = 1012
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.CallableMemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1006
                self.match(OParser.DOT)
                self.state = 1007
                localctx.name = self.variable_identifier()
                pass
            elif token in [OParser.LBRAK]:
                localctx = OParser.CallableItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1008
                self.match(OParser.LBRAK)
                self.state = 1009
                localctx.exp = self.expression(0)
                self.state = 1010
                self.match(OParser.RBRAK)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.ExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_expression

     
        def copyFrom(self, ctx):
            super(OParser.ExpressionContext, self).copyFrom(ctx)


    class IntDivideExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.IntDivideExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def idivide(self):
            return self.getTypedRuleContext(OParser.IdivideContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterIntDivideExpression"):
                listener.enterIntDivideExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIntDivideExpression"):
                listener.exitIntDivideExpression(self)


    class HasAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.HasAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def HAS(self):
            return self.getToken(OParser.HAS, 0)
        def ANY(self):
            return self.getToken(OParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterHasAnyExpression"):
                listener.enterHasAnyExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHasAnyExpression"):
                listener.exitHasAnyExpression(self)


    class HasExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.HasExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def HAS(self):
            return self.getToken(OParser.HAS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterHasExpression"):
                listener.enterHasExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHasExpression"):
                listener.exitHasExpression(self)


    class TernaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.TernaryExpressionContext, self).__init__(parser)
            self.test = None # ExpressionContext
            self.ifTrue = None # ExpressionContext
            self.ifFalse = None # ExpressionContext
            self.copyFrom(ctx)

        def QMARK(self):
            return self.getToken(OParser.QMARK, 0)
        def COLON(self):
            return self.getToken(OParser.COLON, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterTernaryExpression"):
                listener.enterTernaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTernaryExpression"):
                listener.exitTernaryExpression(self)


    class NotEqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.NotEqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def XEQ(self):
            return self.getToken(OParser.XEQ, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotEqualsExpression"):
                listener.enterNotEqualsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotEqualsExpression"):
                listener.exitNotEqualsExpression(self)


    class InExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.InExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(OParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterInExpression"):
                listener.enterInExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitInExpression"):
                listener.exitInExpression(self)


    class IsAnExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.IsAnExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # An_expressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(OParser.IS, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)

        def an_expression(self):
            return self.getTypedRuleContext(OParser.An_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIsAnExpression"):
                listener.enterIsAnExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsAnExpression"):
                listener.exitIsAnExpression(self)


    class JsxExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.JsxExpressionContext, self).__init__(parser)
            self.exp = None # Jsx_expressionContext
            self.copyFrom(ctx)

        def jsx_expression(self):
            return self.getTypedRuleContext(OParser.Jsx_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJsxExpression"):
                listener.enterJsxExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxExpression"):
                listener.exitJsxExpression(self)


    class NotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.NotExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def XMARK(self):
            return self.getToken(OParser.XMARK, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotExpression"):
                listener.enterNotExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotExpression"):
                listener.exitNotExpression(self)


    class GreaterThanExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.GreaterThanExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def GT(self):
            return self.getToken(OParser.GT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterGreaterThanExpression"):
                listener.enterGreaterThanExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitGreaterThanExpression"):
                listener.exitGreaterThanExpression(self)


    class OrExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.OrExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def PIPE2(self):
            return self.getToken(OParser.PIPE2, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterOrExpression"):
                listener.enterOrExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOrExpression"):
                listener.exitOrExpression(self)


    class CodeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.CodeExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(OParser.CODE, 0)
        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCodeExpression"):
                listener.enterCodeExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCodeExpression"):
                listener.exitCodeExpression(self)


    class LessThanOrEqualExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.LessThanOrEqualExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LTE(self):
            return self.getToken(OParser.LTE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterLessThanOrEqualExpression"):
                listener.enterLessThanOrEqualExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLessThanOrEqualExpression"):
                listener.exitLessThanOrEqualExpression(self)


    class NotHasAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.NotHasAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(OParser.NOT, 0)
        def HAS(self):
            return self.getToken(OParser.HAS, 0)
        def ANY(self):
            return self.getToken(OParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotHasAnyExpression"):
                listener.enterNotHasAnyExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotHasAnyExpression"):
                listener.exitNotHasAnyExpression(self)


    class AndExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.AndExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def AMP2(self):
            return self.getToken(OParser.AMP2, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterAndExpression"):
                listener.enterAndExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAndExpression"):
                listener.exitAndExpression(self)


    class NotHasExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.NotHasExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(OParser.NOT, 0)
        def HAS(self):
            return self.getToken(OParser.HAS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotHasExpression"):
                listener.enterNotHasExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotHasExpression"):
                listener.exitNotHasExpression(self)


    class ClosureExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.ClosureExpressionContext, self).__init__(parser)
            self.exp = None # Closure_expressionContext
            self.copyFrom(ctx)

        def closure_expression(self):
            return self.getTypedRuleContext(OParser.Closure_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterClosureExpression"):
                listener.enterClosureExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitClosureExpression"):
                listener.exitClosureExpression(self)


    class NotHasAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.NotHasAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(OParser.NOT, 0)
        def HAS(self):
            return self.getToken(OParser.HAS, 0)
        def ALL(self):
            return self.getToken(OParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotHasAllExpression"):
                listener.enterNotHasAllExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotHasAllExpression"):
                listener.exitNotHasAllExpression(self)


    class ContainsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.ContainsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(OParser.CONTAINS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterContainsExpression"):
                listener.enterContainsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitContainsExpression"):
                listener.exitContainsExpression(self)


    class NotContainsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.NotContainsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(OParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(OParser.CONTAINS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotContainsExpression"):
                listener.enterNotContainsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotContainsExpression"):
                listener.exitNotContainsExpression(self)


    class MultiplyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.MultiplyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def multiply(self):
            return self.getTypedRuleContext(OParser.MultiplyContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterMultiplyExpression"):
                listener.enterMultiplyExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMultiplyExpression"):
                listener.exitMultiplyExpression(self)


    class RoughlyEqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.RoughlyEqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def TEQ(self):
            return self.getToken(OParser.TEQ, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterRoughlyEqualsExpression"):
                listener.enterRoughlyEqualsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRoughlyEqualsExpression"):
                listener.exitRoughlyEqualsExpression(self)


    class IsNotAnExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.IsNotAnExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # An_expressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(OParser.IS, 0)
        def NOT(self):
            return self.getToken(OParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)

        def an_expression(self):
            return self.getTypedRuleContext(OParser.An_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIsNotAnExpression"):
                listener.enterIsNotAnExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsNotAnExpression"):
                listener.exitIsNotAnExpression(self)


    class ExecuteExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.ExecuteExpressionContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def EXECUTE(self):
            return self.getToken(OParser.EXECUTE, 0)
        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterExecuteExpression"):
                listener.enterExecuteExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExecuteExpression"):
                listener.exitExecuteExpression(self)


    class MethodExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.MethodExpressionContext, self).__init__(parser)
            self.exp = None # Method_expressionContext
            self.copyFrom(ctx)

        def method_expression(self):
            return self.getTypedRuleContext(OParser.Method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMethodExpression"):
                listener.enterMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethodExpression"):
                listener.exitMethodExpression(self)


    class GreaterThanOrEqualExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.GreaterThanOrEqualExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def GTE(self):
            return self.getToken(OParser.GTE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterGreaterThanOrEqualExpression"):
                listener.enterGreaterThanOrEqualExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitGreaterThanOrEqualExpression"):
                listener.exitGreaterThanOrEqualExpression(self)


    class NotInExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.NotInExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(OParser.NOT, 0)
        def IN(self):
            return self.getToken(OParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotInExpression"):
                listener.enterNotInExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotInExpression"):
                listener.exitNotInExpression(self)


    class IteratorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.IteratorExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.name = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(OParser.FOR, 0)
        def EACH(self):
            return self.getToken(OParser.EACH, 0)
        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)
        def IN(self):
            return self.getToken(OParser.IN, 0)
        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIteratorExpression"):
                listener.enterIteratorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIteratorExpression"):
                listener.exitIteratorExpression(self)


    class IsNotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.IsNotExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(OParser.IS, 0)
        def NOT(self):
            return self.getToken(OParser.NOT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterIsNotExpression"):
                listener.enterIsNotExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsNotExpression"):
                listener.exitIsNotExpression(self)


    class DivideExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.DivideExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def divide(self):
            return self.getTypedRuleContext(OParser.DivideContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterDivideExpression"):
                listener.enterDivideExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDivideExpression"):
                listener.exitDivideExpression(self)


    class IsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.IsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(OParser.IS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterIsExpression"):
                listener.enterIsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsExpression"):
                listener.exitIsExpression(self)


    class MinusExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.MinusExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(OParser.MINUS, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMinusExpression"):
                listener.enterMinusExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMinusExpression"):
                listener.exitMinusExpression(self)


    class AddExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.AddExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.op = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(OParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(OParser.MINUS, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAddExpression"):
                listener.enterAddExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAddExpression"):
                listener.exitAddExpression(self)


    class HasAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.HasAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def HAS(self):
            return self.getToken(OParser.HAS, 0)
        def ALL(self):
            return self.getToken(OParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterHasAllExpression"):
                listener.enterHasAllExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHasAllExpression"):
                listener.exitHasAllExpression(self)


    class InstanceExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.InstanceExpressionContext, self).__init__(parser)
            self.exp = None # Instance_expressionContext
            self.copyFrom(ctx)

        def instance_expression(self):
            return self.getTypedRuleContext(OParser.Instance_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterInstanceExpression"):
                listener.enterInstanceExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitInstanceExpression"):
                listener.exitInstanceExpression(self)


    class CastExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.CastExpressionContext, self).__init__(parser)
            self.right = None # Category_or_any_typeContext
            self.left = None # ExpressionContext
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)
        def category_or_any_type(self):
            return self.getTypedRuleContext(OParser.Category_or_any_typeContext,0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCastExpression"):
                listener.enterCastExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCastExpression"):
                listener.exitCastExpression(self)


    class ModuloExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.ModuloExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def modulo(self):
            return self.getTypedRuleContext(OParser.ModuloContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterModuloExpression"):
                listener.enterModuloExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitModuloExpression"):
                listener.exitModuloExpression(self)


    class LessThanExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.LessThanExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(OParser.LT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterLessThanExpression"):
                listener.enterLessThanExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLessThanExpression"):
                listener.exitLessThanExpression(self)


    class EqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a OParser.ExpressionContext)
            super(OParser.EqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def EQ2(self):
            return self.getToken(OParser.EQ2, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterEqualsExpression"):
                listener.enterEqualsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEqualsExpression"):
                listener.exitEqualsExpression(self)



    def expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1038
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                localctx = OParser.JsxExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1015
                localctx.exp = self.jsx_expression()
                pass

            elif la_ == 2:
                localctx = OParser.InstanceExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1016
                localctx.exp = self.instance_expression(0)
                pass

            elif la_ == 3:
                localctx = OParser.MethodExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1017
                localctx.exp = self.method_expression()
                pass

            elif la_ == 4:
                localctx = OParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1018
                self.match(OParser.MINUS)
                self.state = 1019
                localctx.exp = self.expression(36)
                pass

            elif la_ == 5:
                localctx = OParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1020
                self.match(OParser.XMARK)
                self.state = 1021
                localctx.exp = self.expression(35)
                pass

            elif la_ == 6:
                localctx = OParser.CastExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1022
                self.match(OParser.LPAR)
                self.state = 1023
                localctx.right = self.category_or_any_type()
                self.state = 1024
                self.match(OParser.RPAR)
                self.state = 1025
                localctx.left = self.expression(29)
                pass

            elif la_ == 7:
                localctx = OParser.CodeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1027
                self.match(OParser.CODE)
                self.state = 1028
                self.match(OParser.LPAR)
                self.state = 1029
                localctx.exp = self.expression(0)
                self.state = 1030
                self.match(OParser.RPAR)
                pass

            elif la_ == 8:
                localctx = OParser.ExecuteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1032
                self.match(OParser.EXECUTE)
                self.state = 1033
                self.match(OParser.LPAR)
                self.state = 1034
                localctx.name = self.variable_identifier()
                self.state = 1035
                self.match(OParser.RPAR)
                pass

            elif la_ == 9:
                localctx = OParser.ClosureExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1037
                localctx.exp = self.closure_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1156
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,69,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1154
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
                    if la_ == 1:
                        localctx = OParser.MultiplyExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1040
                        if not self.precpred(self._ctx, 34):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 34)")
                        self.state = 1041
                        self.multiply()
                        self.state = 1042
                        localctx.right = self.expression(35)
                        pass

                    elif la_ == 2:
                        localctx = OParser.DivideExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1044
                        if not self.precpred(self._ctx, 33):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 33)")
                        self.state = 1045
                        self.divide()
                        self.state = 1046
                        localctx.right = self.expression(34)
                        pass

                    elif la_ == 3:
                        localctx = OParser.ModuloExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1048
                        if not self.precpred(self._ctx, 32):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 32)")
                        self.state = 1049
                        self.modulo()
                        self.state = 1050
                        localctx.right = self.expression(33)
                        pass

                    elif la_ == 4:
                        localctx = OParser.IntDivideExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1052
                        if not self.precpred(self._ctx, 31):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 31)")
                        self.state = 1053
                        self.idivide()
                        self.state = 1054
                        localctx.right = self.expression(32)
                        pass

                    elif la_ == 5:
                        localctx = OParser.AddExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1056
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 1057
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==OParser.PLUS or _la==OParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 1058
                        localctx.right = self.expression(31)
                        pass

                    elif la_ == 6:
                        localctx = OParser.LessThanExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1059
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 1060
                        self.match(OParser.LT)
                        self.state = 1061
                        localctx.right = self.expression(29)
                        pass

                    elif la_ == 7:
                        localctx = OParser.LessThanOrEqualExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1062
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 1063
                        self.match(OParser.LTE)
                        self.state = 1064
                        localctx.right = self.expression(28)
                        pass

                    elif la_ == 8:
                        localctx = OParser.GreaterThanExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1065
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 1066
                        self.match(OParser.GT)
                        self.state = 1067
                        localctx.right = self.expression(27)
                        pass

                    elif la_ == 9:
                        localctx = OParser.GreaterThanOrEqualExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1068
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 1069
                        self.match(OParser.GTE)
                        self.state = 1070
                        localctx.right = self.expression(26)
                        pass

                    elif la_ == 10:
                        localctx = OParser.IsNotExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1071
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 1072
                        self.match(OParser.IS)
                        self.state = 1073
                        self.match(OParser.NOT)
                        self.state = 1074
                        localctx.right = self.expression(23)
                        pass

                    elif la_ == 11:
                        localctx = OParser.IsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1075
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 1076
                        self.match(OParser.IS)
                        self.state = 1077
                        localctx.right = self.expression(22)
                        pass

                    elif la_ == 12:
                        localctx = OParser.EqualsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1078
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 1079
                        self.match(OParser.EQ2)
                        self.state = 1080
                        localctx.right = self.expression(21)
                        pass

                    elif la_ == 13:
                        localctx = OParser.NotEqualsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1081
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 1082
                        self.match(OParser.XEQ)
                        self.state = 1083
                        localctx.right = self.expression(20)
                        pass

                    elif la_ == 14:
                        localctx = OParser.RoughlyEqualsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1084
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 1085
                        self.match(OParser.TEQ)
                        self.state = 1086
                        localctx.right = self.expression(19)
                        pass

                    elif la_ == 15:
                        localctx = OParser.ContainsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1087
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 1088
                        self.match(OParser.CONTAINS)
                        self.state = 1089
                        localctx.right = self.expression(18)
                        pass

                    elif la_ == 16:
                        localctx = OParser.InExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1090
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 1091
                        self.match(OParser.IN)
                        self.state = 1092
                        localctx.right = self.expression(17)
                        pass

                    elif la_ == 17:
                        localctx = OParser.HasExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1093
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 1094
                        self.match(OParser.HAS)
                        self.state = 1095
                        localctx.right = self.expression(16)
                        pass

                    elif la_ == 18:
                        localctx = OParser.HasAllExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1096
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 1097
                        self.match(OParser.HAS)
                        self.state = 1098
                        self.match(OParser.ALL)
                        self.state = 1099
                        localctx.right = self.expression(15)
                        pass

                    elif la_ == 19:
                        localctx = OParser.HasAnyExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1100
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 1101
                        self.match(OParser.HAS)
                        self.state = 1102
                        self.match(OParser.ANY)
                        self.state = 1103
                        localctx.right = self.expression(14)
                        pass

                    elif la_ == 20:
                        localctx = OParser.NotContainsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1104
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 1105
                        self.match(OParser.NOT)
                        self.state = 1106
                        self.match(OParser.CONTAINS)
                        self.state = 1107
                        localctx.right = self.expression(13)
                        pass

                    elif la_ == 21:
                        localctx = OParser.NotInExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1108
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 1109
                        self.match(OParser.NOT)
                        self.state = 1110
                        self.match(OParser.IN)
                        self.state = 1111
                        localctx.right = self.expression(12)
                        pass

                    elif la_ == 22:
                        localctx = OParser.NotHasExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1112
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 1113
                        self.match(OParser.NOT)
                        self.state = 1114
                        self.match(OParser.HAS)
                        self.state = 1115
                        localctx.right = self.expression(11)
                        pass

                    elif la_ == 23:
                        localctx = OParser.NotHasAllExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1116
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 1117
                        self.match(OParser.NOT)
                        self.state = 1118
                        self.match(OParser.HAS)
                        self.state = 1119
                        self.match(OParser.ALL)
                        self.state = 1120
                        localctx.right = self.expression(10)
                        pass

                    elif la_ == 24:
                        localctx = OParser.NotHasAnyExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1121
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 1122
                        self.match(OParser.NOT)
                        self.state = 1123
                        self.match(OParser.HAS)
                        self.state = 1124
                        self.match(OParser.ANY)
                        self.state = 1125
                        localctx.right = self.expression(9)
                        pass

                    elif la_ == 25:
                        localctx = OParser.OrExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1126
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 1127
                        self.match(OParser.PIPE2)
                        self.state = 1128
                        localctx.right = self.expression(8)
                        pass

                    elif la_ == 26:
                        localctx = OParser.AndExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1129
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 1130
                        self.match(OParser.AMP2)
                        self.state = 1131
                        localctx.right = self.expression(7)
                        pass

                    elif la_ == 27:
                        localctx = OParser.TernaryExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.test = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1132
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 1133
                        self.match(OParser.QMARK)
                        self.state = 1134
                        localctx.ifTrue = self.expression(0)
                        self.state = 1135
                        self.match(OParser.COLON)
                        self.state = 1136
                        localctx.ifFalse = self.expression(6)
                        pass

                    elif la_ == 28:
                        localctx = OParser.IsNotAnExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1138
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 1139
                        self.match(OParser.IS)
                        self.state = 1140
                        self.match(OParser.NOT)
                        self.state = 1141
                        localctx.right = self.an_expression()
                        pass

                    elif la_ == 29:
                        localctx = OParser.IsAnExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1142
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 1143
                        self.match(OParser.IS)
                        self.state = 1144
                        localctx.right = self.an_expression()
                        pass

                    elif la_ == 30:
                        localctx = OParser.IteratorExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.exp = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1145
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1146
                        self.match(OParser.FOR)
                        self.state = 1147
                        self.match(OParser.EACH)
                        self.state = 1148
                        self.match(OParser.LPAR)
                        self.state = 1149
                        localctx.name = self.variable_identifier()
                        self.state = 1150
                        self.match(OParser.IN)
                        self.state = 1151
                        localctx.source = self.expression(0)
                        self.state = 1152
                        self.match(OParser.RPAR)
                        pass

             
                self.state = 1158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,69,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class An_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.An_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # Category_or_any_typeContext

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def category_or_any_type(self):
            return self.getTypedRuleContext(OParser.Category_or_any_typeContext,0)


        def getRuleIndex(self):
            return OParser.RULE_an_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterAn_expression"):
                listener.enterAn_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAn_expression"):
                listener.exitAn_expression(self)




    def an_expression(self):

        localctx = OParser.An_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_an_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1159
            if not self.willBeAOrAn():
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.willBeAOrAn()")
            self.state = 1160
            self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1161
            localctx.typ = self.category_or_any_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Closure_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Closure_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def getRuleIndex(self):
            return OParser.RULE_closure_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterClosure_expression"):
                listener.enterClosure_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitClosure_expression"):
                listener.exitClosure_expression(self)




    def closure_expression(self):

        localctx = OParser.Closure_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_closure_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1163
            localctx.name = self.type_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Instance_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Instance_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_instance_expression

     
        def copyFrom(self, ctx):
            super(OParser.Instance_expressionContext, self).copyFrom(ctx)


    class SelectorExpressionContext(Instance_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Instance_expressionContext)
            super(OParser.SelectorExpressionContext, self).__init__(parser)
            self.parent = None # Instance_expressionContext
            self.selector = None # Selector_expressionContext
            self.copyFrom(ctx)

        def instance_expression(self):
            return self.getTypedRuleContext(OParser.Instance_expressionContext,0)

        def selector_expression(self):
            return self.getTypedRuleContext(OParser.Selector_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSelectorExpression"):
                listener.enterSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSelectorExpression"):
                listener.exitSelectorExpression(self)


    class SelectableExpressionContext(Instance_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Instance_expressionContext)
            super(OParser.SelectableExpressionContext, self).__init__(parser)
            self.parent = None # Selectable_expressionContext
            self.copyFrom(ctx)

        def selectable_expression(self):
            return self.getTypedRuleContext(OParser.Selectable_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSelectableExpression"):
                listener.enterSelectableExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSelectableExpression"):
                listener.exitSelectableExpression(self)



    def instance_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Instance_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_instance_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.SelectableExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1166
            localctx.parent = self.selectable_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1172
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,70,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.SelectorExpressionContext(self, OParser.Instance_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_expression)
                    self.state = 1168
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1169
                    localctx.selector = self.selector_expression() 
                self.state = 1174
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,70,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Method_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def blob_expression(self):
            return self.getTypedRuleContext(OParser.Blob_expressionContext,0)


        def document_expression(self):
            return self.getTypedRuleContext(OParser.Document_expressionContext,0)


        def filtered_list_expression(self):
            return self.getTypedRuleContext(OParser.Filtered_list_expressionContext,0)


        def fetch_store_expression(self):
            return self.getTypedRuleContext(OParser.Fetch_store_expressionContext,0)


        def read_all_expression(self):
            return self.getTypedRuleContext(OParser.Read_all_expressionContext,0)


        def read_one_expression(self):
            return self.getTypedRuleContext(OParser.Read_one_expressionContext,0)


        def sorted_expression(self):
            return self.getTypedRuleContext(OParser.Sorted_expressionContext,0)


        def method_call(self):
            return self.getTypedRuleContext(OParser.Method_callContext,0)


        def constructor_expression(self):
            return self.getTypedRuleContext(OParser.Constructor_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_method_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterMethod_expression"):
                listener.enterMethod_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethod_expression"):
                listener.exitMethod_expression(self)




    def method_expression(self):

        localctx = OParser.Method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_method_expression)
        try:
            self.state = 1184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1175
                self.blob_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1176
                self.document_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1177
                self.filtered_list_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1178
                self.fetch_store_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1179
                self.read_all_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1180
                self.read_one_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1181
                self.sorted_expression()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1182
                self.method_call()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 1183
                self.constructor_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Blob_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Blob_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BLOB(self):
            return self.getToken(OParser.BLOB, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def getRuleIndex(self):
            return OParser.RULE_blob_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterBlob_expression"):
                listener.enterBlob_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBlob_expression"):
                listener.exitBlob_expression(self)




    def blob_expression(self):

        localctx = OParser.Blob_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_blob_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1186
            self.match(OParser.BLOB)
            self.state = 1187
            self.match(OParser.LPAR)
            self.state = 1188
            self.expression(0)
            self.state = 1189
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Document_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Document_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DOCUMENT(self):
            return self.getToken(OParser.DOCUMENT, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_document_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterDocument_expression"):
                listener.enterDocument_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDocument_expression"):
                listener.exitDocument_expression(self)




    def document_expression(self):

        localctx = OParser.Document_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_document_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1191
            self.match(OParser.DOCUMENT)
            self.state = 1192
            self.match(OParser.LPAR)
            self.state = 1194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.LTGT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (OParser.EXECUTE - 95)) | (1 << (OParser.FETCH - 95)) | (1 << (OParser.FILTERED - 95)) | (1 << (OParser.MUTABLE - 95)) | (1 << (OParser.NULL - 95)) | (1 << (OParser.READ - 95)) | (1 << (OParser.SELF - 95)) | (1 << (OParser.SORTED - 95)) | (1 << (OParser.THIS - 95)) | (1 << (OParser.BOOLEAN_LITERAL - 95)) | (1 << (OParser.CHAR_LITERAL - 95)) | (1 << (OParser.MIN_INTEGER - 95)) | (1 << (OParser.MAX_INTEGER - 95)) | (1 << (OParser.SYMBOL_IDENTIFIER - 95)))) != 0) or ((((_la - 159)) & ~0x3f) == 0 and ((1 << (_la - 159)) & ((1 << (OParser.TYPE_IDENTIFIER - 159)) | (1 << (OParser.VARIABLE_IDENTIFIER - 159)) | (1 << (OParser.TEXT_LITERAL - 159)) | (1 << (OParser.UUID_LITERAL - 159)) | (1 << (OParser.INTEGER_LITERAL - 159)) | (1 << (OParser.HEXA_LITERAL - 159)) | (1 << (OParser.DECIMAL_LITERAL - 159)) | (1 << (OParser.DATETIME_LITERAL - 159)) | (1 << (OParser.TIME_LITERAL - 159)) | (1 << (OParser.DATE_LITERAL - 159)) | (1 << (OParser.PERIOD_LITERAL - 159)) | (1 << (OParser.VERSION_LITERAL - 159)))) != 0):
                self.state = 1193
                self.expression(0)


            self.state = 1196
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Write_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Write_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.what = None # ExpressionContext
            self.target = None # ExpressionContext

        def WRITE(self):
            return self.getToken(OParser.WRITE, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def TO(self):
            return self.getToken(OParser.TO, 0)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def getRuleIndex(self):
            return OParser.RULE_write_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterWrite_statement"):
                listener.enterWrite_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWrite_statement"):
                listener.exitWrite_statement(self)




    def write_statement(self):

        localctx = OParser.Write_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_write_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1198
            self.match(OParser.WRITE)
            self.state = 1199
            self.match(OParser.LPAR)
            self.state = 1200
            localctx.what = self.expression(0)
            self.state = 1201
            self.match(OParser.RPAR)
            self.state = 1202
            self.match(OParser.TO)
            self.state = 1203
            localctx.target = self.expression(0)
            self.state = 1204
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Filtered_list_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Filtered_list_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # ExpressionContext
            self.name = None # Variable_identifierContext
            self.predicate = None # ExpressionContext

        def FILTERED(self):
            return self.getToken(OParser.FILTERED, 0)

        def LPAR(self, i=None):
            if i is None:
                return self.getTokens(OParser.LPAR)
            else:
                return self.getToken(OParser.LPAR, i)

        def RPAR(self, i=None):
            if i is None:
                return self.getTokens(OParser.RPAR)
            else:
                return self.getToken(OParser.RPAR, i)

        def WITH(self):
            return self.getToken(OParser.WITH, 0)

        def WHERE(self):
            return self.getToken(OParser.WHERE, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def getRuleIndex(self):
            return OParser.RULE_filtered_list_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterFiltered_list_expression"):
                listener.enterFiltered_list_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFiltered_list_expression"):
                listener.exitFiltered_list_expression(self)




    def filtered_list_expression(self):

        localctx = OParser.Filtered_list_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_filtered_list_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1206
            self.match(OParser.FILTERED)
            self.state = 1207
            self.match(OParser.LPAR)
            self.state = 1208
            localctx.source = self.expression(0)
            self.state = 1209
            self.match(OParser.RPAR)
            self.state = 1210
            self.match(OParser.WITH)
            self.state = 1211
            self.match(OParser.LPAR)
            self.state = 1212
            localctx.name = self.variable_identifier()
            self.state = 1213
            self.match(OParser.RPAR)
            self.state = 1214
            self.match(OParser.WHERE)
            self.state = 1215
            self.match(OParser.LPAR)
            self.state = 1216
            localctx.predicate = self.expression(0)
            self.state = 1217
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fetch_store_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Fetch_store_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_fetch_store_expression

     
        def copyFrom(self, ctx):
            super(OParser.Fetch_store_expressionContext, self).copyFrom(ctx)



    class FetchOneContext(Fetch_store_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Fetch_store_expressionContext)
            super(OParser.FetchOneContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.predicate = None # ExpressionContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(OParser.FETCH, 0)
        def ONE(self):
            return self.getToken(OParser.ONE, 0)
        def WHERE(self):
            return self.getToken(OParser.WHERE, 0)
        def LPAR(self, i=None):
            if i is None:
                return self.getTokens(OParser.LPAR)
            else:
                return self.getToken(OParser.LPAR, i)
        def RPAR(self, i=None):
            if i is None:
                return self.getTokens(OParser.RPAR)
            else:
                return self.getToken(OParser.RPAR, i)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)

        def mutable_category_type(self):
            return self.getTypedRuleContext(OParser.Mutable_category_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterFetchOne"):
                listener.enterFetchOne(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFetchOne"):
                listener.exitFetchOne(self)


    class FetchManyContext(Fetch_store_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Fetch_store_expressionContext)
            super(OParser.FetchManyContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.xstart = None # ExpressionContext
            self.xstop = None # ExpressionContext
            self.predicate = None # ExpressionContext
            self.orderby = None # Order_by_listContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(OParser.FETCH, 0)
        def WHERE(self):
            return self.getToken(OParser.WHERE, 0)
        def LPAR(self, i=None):
            if i is None:
                return self.getTokens(OParser.LPAR)
            else:
                return self.getToken(OParser.LPAR, i)
        def RPAR(self, i=None):
            if i is None:
                return self.getTokens(OParser.RPAR)
            else:
                return self.getToken(OParser.RPAR, i)
        def ORDER(self):
            return self.getToken(OParser.ORDER, 0)
        def BY(self):
            return self.getToken(OParser.BY, 0)
        def ALL(self):
            return self.getToken(OParser.ALL, 0)
        def ROWS(self):
            return self.getToken(OParser.ROWS, 0)
        def TO(self):
            return self.getToken(OParser.TO, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)

        def order_by_list(self):
            return self.getTypedRuleContext(OParser.Order_by_listContext,0)

        def mutable_category_type(self):
            return self.getTypedRuleContext(OParser.Mutable_category_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterFetchMany"):
                listener.enterFetchMany(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFetchMany"):
                listener.exitFetchMany(self)



    def fetch_store_expression(self):

        localctx = OParser.Fetch_store_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_fetch_store_expression)
        self._la = 0 # Token type
        try:
            self.state = 1270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
            if la_ == 1:
                localctx = OParser.FetchOneContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1219
                self.match(OParser.FETCH)
                self.state = 1220
                self.match(OParser.ONE)
                self.state = 1225
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==OParser.LPAR:
                    self.state = 1221
                    self.match(OParser.LPAR)
                    self.state = 1222
                    localctx.typ = self.mutable_category_type()
                    self.state = 1223
                    self.match(OParser.RPAR)


                self.state = 1227
                self.match(OParser.WHERE)
                self.state = 1228
                self.match(OParser.LPAR)
                self.state = 1229
                localctx.predicate = self.expression(0)
                self.state = 1230
                self.match(OParser.RPAR)
                pass

            elif la_ == 2:
                localctx = OParser.FetchManyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1232
                self.match(OParser.FETCH)
                self.state = 1253
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [OParser.ALL]:
                    self.state = 1233
                    self.match(OParser.ALL)
                    self.state = 1238
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,74,self._ctx)
                    if la_ == 1:
                        self.state = 1234
                        self.match(OParser.LPAR)
                        self.state = 1235
                        localctx.typ = self.mutable_category_type()
                        self.state = 1236
                        self.match(OParser.RPAR)


                    pass
                elif token in [OParser.LPAR, OParser.ROWS]:
                    self.state = 1244
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==OParser.LPAR:
                        self.state = 1240
                        self.match(OParser.LPAR)
                        self.state = 1241
                        localctx.typ = self.mutable_category_type()
                        self.state = 1242
                        self.match(OParser.RPAR)


                    self.state = 1246
                    self.match(OParser.ROWS)
                    self.state = 1247
                    self.match(OParser.LPAR)
                    self.state = 1248
                    localctx.xstart = self.expression(0)
                    self.state = 1249
                    self.match(OParser.TO)
                    self.state = 1250
                    localctx.xstop = self.expression(0)
                    self.state = 1251
                    self.match(OParser.RPAR)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1260
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
                if la_ == 1:
                    self.state = 1255
                    self.match(OParser.WHERE)
                    self.state = 1256
                    self.match(OParser.LPAR)
                    self.state = 1257
                    localctx.predicate = self.expression(0)
                    self.state = 1258
                    self.match(OParser.RPAR)


                self.state = 1268
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
                if la_ == 1:
                    self.state = 1262
                    self.match(OParser.ORDER)
                    self.state = 1263
                    self.match(OParser.BY)
                    self.state = 1264
                    self.match(OParser.LPAR)
                    self.state = 1265
                    localctx.orderby = self.order_by_list()
                    self.state = 1266
                    self.match(OParser.RPAR)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Sorted_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Sorted_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # Instance_expressionContext
            self.key = None # Instance_expressionContext

        def SORTED(self):
            return self.getToken(OParser.SORTED, 0)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def instance_expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Instance_expressionContext)
            else:
                return self.getTypedRuleContext(OParser.Instance_expressionContext,i)


        def DESC(self):
            return self.getToken(OParser.DESC, 0)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)

        def key_token(self):
            return self.getTypedRuleContext(OParser.Key_tokenContext,0)


        def EQ(self):
            return self.getToken(OParser.EQ, 0)

        def getRuleIndex(self):
            return OParser.RULE_sorted_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterSorted_expression"):
                listener.enterSorted_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSorted_expression"):
                listener.exitSorted_expression(self)




    def sorted_expression(self):

        localctx = OParser.Sorted_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_sorted_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1272
            self.match(OParser.SORTED)
            self.state = 1274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.DESC:
                self.state = 1273
                self.match(OParser.DESC)


            self.state = 1276
            self.match(OParser.LPAR)
            self.state = 1277
            localctx.source = self.instance_expression(0)
            self.state = 1283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.COMMA:
                self.state = 1278
                self.match(OParser.COMMA)
                self.state = 1279
                self.key_token()
                self.state = 1280
                self.match(OParser.EQ)
                self.state = 1281
                localctx.key = self.instance_expression(0)


            self.state = 1285
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Selector_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_selector_expression

     
        def copyFrom(self, ctx):
            super(OParser.Selector_expressionContext, self).copyFrom(ctx)



    class SliceSelectorContext(Selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Selector_expressionContext)
            super(OParser.SliceSelectorContext, self).__init__(parser)
            self.xslice = None # Slice_argumentsContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)
        def slice_arguments(self):
            return self.getTypedRuleContext(OParser.Slice_argumentsContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSliceSelector"):
                listener.enterSliceSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSliceSelector"):
                listener.exitSliceSelector(self)


    class MemberSelectorContext(Selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Selector_expressionContext)
            super(OParser.MemberSelectorContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMemberSelector"):
                listener.enterMemberSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMemberSelector"):
                listener.exitMemberSelector(self)


    class ItemSelectorContext(Selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Selector_expressionContext)
            super(OParser.ItemSelectorContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterItemSelector"):
                listener.enterItemSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitItemSelector"):
                listener.exitItemSelector(self)



    def selector_expression(self):

        localctx = OParser.Selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_selector_expression)
        try:
            self.state = 1297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                localctx = OParser.MemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1287
                self.match(OParser.DOT)
                self.state = 1288
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = OParser.ItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1289
                self.match(OParser.LBRAK)
                self.state = 1290
                localctx.exp = self.expression(0)
                self.state = 1291
                self.match(OParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = OParser.SliceSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1293
                self.match(OParser.LBRAK)
                self.state = 1294
                localctx.xslice = self.slice_arguments()
                self.state = 1295
                self.match(OParser.RBRAK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Constructor_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Constructor_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_constructor_expression

     
        def copyFrom(self, ctx):
            super(OParser.Constructor_expressionContext, self).copyFrom(ctx)



    class ConstructorFromContext(Constructor_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Constructor_expressionContext)
            super(OParser.ConstructorFromContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.copyExp = None # Copy_fromContext
            self.args = None # Argument_assignment_listContext
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)
        def mutable_category_type(self):
            return self.getTypedRuleContext(OParser.Mutable_category_typeContext,0)

        def copy_from(self):
            return self.getTypedRuleContext(OParser.Copy_fromContext,0)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def argument_assignment_list(self):
            return self.getTypedRuleContext(OParser.Argument_assignment_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterConstructorFrom"):
                listener.enterConstructorFrom(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConstructorFrom"):
                listener.exitConstructorFrom(self)


    class ConstructorNoFromContext(Constructor_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Constructor_expressionContext)
            super(OParser.ConstructorNoFromContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.args = None # Argument_assignment_listContext
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)
        def mutable_category_type(self):
            return self.getTypedRuleContext(OParser.Mutable_category_typeContext,0)

        def argument_assignment_list(self):
            return self.getTypedRuleContext(OParser.Argument_assignment_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterConstructorNoFrom"):
                listener.enterConstructorNoFrom(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConstructorNoFrom"):
                listener.exitConstructorNoFrom(self)



    def constructor_expression(self):

        localctx = OParser.Constructor_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_constructor_expression)
        self._la = 0 # Token type
        try:
            self.state = 1315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,85,self._ctx)
            if la_ == 1:
                localctx = OParser.ConstructorFromContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1299
                localctx.typ = self.mutable_category_type()
                self.state = 1300
                self.match(OParser.LPAR)
                self.state = 1301
                localctx.copyExp = self.copy_from()
                self.state = 1304
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==OParser.COMMA:
                    self.state = 1302
                    self.match(OParser.COMMA)
                    self.state = 1303
                    localctx.args = self.argument_assignment_list(0)


                self.state = 1306
                self.match(OParser.RPAR)
                pass

            elif la_ == 2:
                localctx = OParser.ConstructorNoFromContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1308
                localctx.typ = self.mutable_category_type()
                self.state = 1309
                self.match(OParser.LPAR)
                self.state = 1311
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.LTGT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (OParser.EXECUTE - 95)) | (1 << (OParser.FETCH - 95)) | (1 << (OParser.FILTERED - 95)) | (1 << (OParser.MUTABLE - 95)) | (1 << (OParser.NULL - 95)) | (1 << (OParser.READ - 95)) | (1 << (OParser.SELF - 95)) | (1 << (OParser.SORTED - 95)) | (1 << (OParser.THIS - 95)) | (1 << (OParser.BOOLEAN_LITERAL - 95)) | (1 << (OParser.CHAR_LITERAL - 95)) | (1 << (OParser.MIN_INTEGER - 95)) | (1 << (OParser.MAX_INTEGER - 95)) | (1 << (OParser.SYMBOL_IDENTIFIER - 95)))) != 0) or ((((_la - 159)) & ~0x3f) == 0 and ((1 << (_la - 159)) & ((1 << (OParser.TYPE_IDENTIFIER - 159)) | (1 << (OParser.VARIABLE_IDENTIFIER - 159)) | (1 << (OParser.TEXT_LITERAL - 159)) | (1 << (OParser.UUID_LITERAL - 159)) | (1 << (OParser.INTEGER_LITERAL - 159)) | (1 << (OParser.HEXA_LITERAL - 159)) | (1 << (OParser.DECIMAL_LITERAL - 159)) | (1 << (OParser.DATETIME_LITERAL - 159)) | (1 << (OParser.TIME_LITERAL - 159)) | (1 << (OParser.DATE_LITERAL - 159)) | (1 << (OParser.PERIOD_LITERAL - 159)) | (1 << (OParser.VERSION_LITERAL - 159)))) != 0):
                    self.state = 1310
                    localctx.args = self.argument_assignment_list(0)


                self.state = 1313
                self.match(OParser.RPAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Copy_fromContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Copy_fromContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def FROM(self):
            return self.getToken(OParser.FROM, 0)

        def assign(self):
            return self.getTypedRuleContext(OParser.AssignContext,0)


        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_copy_from

        def enterRule(self, listener):
            if hasattr(listener, "enterCopy_from"):
                listener.enterCopy_from(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCopy_from"):
                listener.exitCopy_from(self)




    def copy_from(self):

        localctx = OParser.Copy_fromContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_copy_from)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1317
            self.match(OParser.FROM)
            self.state = 1318
            self.assign()
            self.state = 1319
            localctx.exp = self.expression(0)
            self.state = 1320
            if not self.willNotBe(self.equalToken()):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.willNotBe($parser.equalToken())")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argument_assignment_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Argument_assignment_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_argument_assignment_list

     
        def copyFrom(self, ctx):
            super(OParser.Argument_assignment_listContext, self).copyFrom(ctx)


    class ExpressionAssignmentListContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Argument_assignment_listContext)
            super(OParser.ExpressionAssignmentListContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterExpressionAssignmentList"):
                listener.enterExpressionAssignmentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExpressionAssignmentList"):
                listener.exitExpressionAssignmentList(self)


    class ArgumentAssignmentListContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Argument_assignment_listContext)
            super(OParser.ArgumentAssignmentListContext, self).__init__(parser)
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def argument_assignment(self):
            return self.getTypedRuleContext(OParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterArgumentAssignmentList"):
                listener.enterArgumentAssignmentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgumentAssignmentList"):
                listener.exitArgumentAssignmentList(self)


    class ArgumentAssignmentListItemContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Argument_assignment_listContext)
            super(OParser.ArgumentAssignmentListItemContext, self).__init__(parser)
            self.items = None # Argument_assignment_listContext
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def argument_assignment_list(self):
            return self.getTypedRuleContext(OParser.Argument_assignment_listContext,0)

        def argument_assignment(self):
            return self.getTypedRuleContext(OParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterArgumentAssignmentListItem"):
                listener.enterArgumentAssignmentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgumentAssignmentListItem"):
                listener.exitArgumentAssignmentListItem(self)



    def argument_assignment_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Argument_assignment_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 120
        self.enterRecursionRule(localctx, 120, self.RULE_argument_assignment_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,86,self._ctx)
            if la_ == 1:
                localctx = OParser.ExpressionAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1323
                localctx.exp = self.expression(0)
                self.state = 1324
                if not self.willNotBe(self.equalToken()):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willNotBe($parser.equalToken())")
                pass

            elif la_ == 2:
                localctx = OParser.ArgumentAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1326
                localctx.item = self.argument_assignment()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1334
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,87,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.ArgumentAssignmentListItemContext(self, OParser.Argument_assignment_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_assignment_list)
                    self.state = 1329
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1330
                    self.match(OParser.COMMA)
                    self.state = 1331
                    localctx.item = self.argument_assignment() 
                self.state = 1336
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,87,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Argument_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Argument_assignmentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.exp = None # ExpressionContext

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def assign(self):
            return self.getTypedRuleContext(OParser.AssignContext,0)


        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_argument_assignment

        def enterRule(self, listener):
            if hasattr(listener, "enterArgument_assignment"):
                listener.enterArgument_assignment(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgument_assignment"):
                listener.exitArgument_assignment(self)




    def argument_assignment(self):

        localctx = OParser.Argument_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_argument_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1337
            localctx.name = self.variable_identifier()
            self.state = 1341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,88,self._ctx)
            if la_ == 1:
                self.state = 1338
                self.assign()
                self.state = 1339
                localctx.exp = self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_instance_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Assign_instance_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.inst = None # Assignable_instanceContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(OParser.AssignContext,0)


        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def assignable_instance(self):
            return self.getTypedRuleContext(OParser.Assignable_instanceContext,0)


        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_assign_instance_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterAssign_instance_statement"):
                listener.enterAssign_instance_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign_instance_statement"):
                listener.exitAssign_instance_statement(self)




    def assign_instance_statement(self):

        localctx = OParser.Assign_instance_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_assign_instance_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1343
            localctx.inst = self.assignable_instance(0)
            self.state = 1344
            self.assign()
            self.state = 1345
            localctx.exp = self.expression(0)
            self.state = 1346
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Child_instanceContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Child_instanceContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_child_instance

     
        def copyFrom(self, ctx):
            super(OParser.Child_instanceContext, self).copyFrom(ctx)



    class MemberInstanceContext(Child_instanceContext):

        def __init__(self, parser, ctx): # actually a OParser.Child_instanceContext)
            super(OParser.MemberInstanceContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMemberInstance"):
                listener.enterMemberInstance(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMemberInstance"):
                listener.exitMemberInstance(self)


    class ItemInstanceContext(Child_instanceContext):

        def __init__(self, parser, ctx): # actually a OParser.Child_instanceContext)
            super(OParser.ItemInstanceContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterItemInstance"):
                listener.enterItemInstance(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitItemInstance"):
                listener.exitItemInstance(self)



    def child_instance(self):

        localctx = OParser.Child_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_child_instance)
        try:
            self.state = 1354
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.MemberInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1348
                self.match(OParser.DOT)
                self.state = 1349
                localctx.name = self.variable_identifier()
                pass
            elif token in [OParser.LBRAK]:
                localctx = OParser.ItemInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1350
                self.match(OParser.LBRAK)
                self.state = 1351
                localctx.exp = self.expression(0)
                self.state = 1352
                self.match(OParser.RBRAK)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_tuple_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Assign_tuple_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Variable_identifier_listContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(OParser.AssignContext,0)


        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def variable_identifier_list(self):
            return self.getTypedRuleContext(OParser.Variable_identifier_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_assign_tuple_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterAssign_tuple_statement"):
                listener.enterAssign_tuple_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign_tuple_statement"):
                listener.exitAssign_tuple_statement(self)




    def assign_tuple_statement(self):

        localctx = OParser.Assign_tuple_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_assign_tuple_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1356
            localctx.items = self.variable_identifier_list()
            self.state = 1357
            self.assign()
            self.state = 1358
            localctx.exp = self.expression(0)
            self.state = 1359
            self.match(OParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Null_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Null_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NULL(self):
            return self.getToken(OParser.NULL, 0)

        def getRuleIndex(self):
            return OParser.RULE_null_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterNull_literal"):
                listener.enterNull_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNull_literal"):
                listener.exitNull_literal(self)




    def null_literal(self):

        localctx = OParser.Null_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1361
            self.match(OParser.NULL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_declaration_list

     
        def copyFrom(self, ctx):
            super(OParser.Declaration_listContext, self).copyFrom(ctx)



    class FullDeclarationListContext(Declaration_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Declaration_listContext)
            super(OParser.FullDeclarationListContext, self).__init__(parser)
            self.copyFrom(ctx)

        def lfs(self):
            return self.getTypedRuleContext(OParser.LfsContext,0)

        def EOF(self):
            return self.getToken(OParser.EOF, 0)
        def declarations(self):
            return self.getTypedRuleContext(OParser.DeclarationsContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterFullDeclarationList"):
                listener.enterFullDeclarationList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFullDeclarationList"):
                listener.exitFullDeclarationList(self)



    def declaration_list(self):

        localctx = OParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            localctx = OParser.FullDeclarationListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 1364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.ABSTRACT - 64)) | (1 << (OParser.ANY - 64)) | (1 << (OParser.ATTRIBUTE - 64)) | (1 << (OParser.CATEGORY - 64)) | (1 << (OParser.ENUMERATED - 64)) | (1 << (OParser.METHOD - 64)) | (1 << (OParser.NATIVE - 64)))) != 0) or ((((_la - 138)) & ~0x3f) == 0 and ((1 << (_la - 138)) & ((1 << (OParser.SINGLETON - 138)) | (1 << (OParser.STORABLE - 138)) | (1 << (OParser.TEST - 138)) | (1 << (OParser.TYPE_IDENTIFIER - 138)))) != 0):
                self.state = 1363
                self.declarations()


            self.state = 1366
            self.lfs()
            self.state = 1367
            self.match(OParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.DeclarationsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(OParser.DeclarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.LfpContext)
            else:
                return self.getTypedRuleContext(OParser.LfpContext,i)


        def getRuleIndex(self):
            return OParser.RULE_declarations

        def enterRule(self, listener):
            if hasattr(listener, "enterDeclarations"):
                listener.enterDeclarations(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDeclarations"):
                listener.exitDeclarations(self)




    def declarations(self):

        localctx = OParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1369
            self.declaration()
            self.state = 1375
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.ABSTRACT - 64)) | (1 << (OParser.ANY - 64)) | (1 << (OParser.ATTRIBUTE - 64)) | (1 << (OParser.CATEGORY - 64)) | (1 << (OParser.ENUMERATED - 64)) | (1 << (OParser.METHOD - 64)) | (1 << (OParser.NATIVE - 64)))) != 0) or ((((_la - 138)) & ~0x3f) == 0 and ((1 << (_la - 138)) & ((1 << (OParser.SINGLETON - 138)) | (1 << (OParser.STORABLE - 138)) | (1 << (OParser.TEST - 138)) | (1 << (OParser.TYPE_IDENTIFIER - 138)))) != 0):
                self.state = 1370
                self.lfp()
                self.state = 1371
                self.declaration()
                self.state = 1377
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.DeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def attribute_declaration(self):
            return self.getTypedRuleContext(OParser.Attribute_declarationContext,0)


        def category_declaration(self):
            return self.getTypedRuleContext(OParser.Category_declarationContext,0)


        def resource_declaration(self):
            return self.getTypedRuleContext(OParser.Resource_declarationContext,0)


        def enum_declaration(self):
            return self.getTypedRuleContext(OParser.Enum_declarationContext,0)


        def method_declaration(self):
            return self.getTypedRuleContext(OParser.Method_declarationContext,0)


        def comment_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Comment_statementContext)
            else:
                return self.getTypedRuleContext(OParser.Comment_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.LfpContext)
            else:
                return self.getTypedRuleContext(OParser.LfpContext,i)


        def getRuleIndex(self):
            return OParser.RULE_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterDeclaration"):
                listener.enterDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDeclaration"):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = OParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1383
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMENT:
                self.state = 1378
                self.comment_statement()
                self.state = 1379
                self.lfp()
                self.state = 1385
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1391
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,93,self._ctx)
            if la_ == 1:
                self.state = 1386
                self.attribute_declaration()
                pass

            elif la_ == 2:
                self.state = 1387
                self.category_declaration()
                pass

            elif la_ == 3:
                self.state = 1388
                self.resource_declaration()
                pass

            elif la_ == 4:
                self.state = 1389
                self.enum_declaration()
                pass

            elif la_ == 5:
                self.state = 1390
                self.method_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Resource_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Resource_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_resource_declaration(self):
            return self.getTypedRuleContext(OParser.Native_resource_declarationContext,0)


        def getRuleIndex(self):
            return OParser.RULE_resource_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterResource_declaration"):
                listener.enterResource_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitResource_declaration"):
                listener.exitResource_declaration(self)




    def resource_declaration(self):

        localctx = OParser.Resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1393
            self.native_resource_declaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Enum_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Enum_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def enum_category_declaration(self):
            return self.getTypedRuleContext(OParser.Enum_category_declarationContext,0)


        def enum_native_declaration(self):
            return self.getTypedRuleContext(OParser.Enum_native_declarationContext,0)


        def getRuleIndex(self):
            return OParser.RULE_enum_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterEnum_declaration"):
                listener.enterEnum_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEnum_declaration"):
                listener.exitEnum_declaration(self)




    def enum_declaration(self):

        localctx = OParser.Enum_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_enum_declaration)
        try:
            self.state = 1397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,94,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1395
                self.enum_category_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1396
                self.enum_native_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_symbol(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Native_symbolContext)
            else:
                return self.getTypedRuleContext(OParser.Native_symbolContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.LfpContext)
            else:
                return self.getTypedRuleContext(OParser.LfpContext,i)


        def getRuleIndex(self):
            return OParser.RULE_native_symbol_list

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_symbol_list"):
                listener.enterNative_symbol_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_symbol_list"):
                listener.exitNative_symbol_list(self)




    def native_symbol_list(self):

        localctx = OParser.Native_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_native_symbol_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1399
            self.native_symbol()
            self.state = 1405
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.SYMBOL_IDENTIFIER:
                self.state = 1400
                self.lfp()
                self.state = 1401
                self.native_symbol()
                self.state = 1407
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Category_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def category_symbol(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Category_symbolContext)
            else:
                return self.getTypedRuleContext(OParser.Category_symbolContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.LfpContext)
            else:
                return self.getTypedRuleContext(OParser.LfpContext,i)


        def getRuleIndex(self):
            return OParser.RULE_category_symbol_list

        def enterRule(self, listener):
            if hasattr(listener, "enterCategory_symbol_list"):
                listener.enterCategory_symbol_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategory_symbol_list"):
                listener.exitCategory_symbol_list(self)




    def category_symbol_list(self):

        localctx = OParser.Category_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_category_symbol_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1408
            self.category_symbol()
            self.state = 1414
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.SYMBOL_IDENTIFIER:
                self.state = 1409
                self.lfp()
                self.state = 1410
                self.category_symbol()
                self.state = 1416
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def symbol_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Symbol_identifierContext)
            else:
                return self.getTypedRuleContext(OParser.Symbol_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(OParser.COMMA)
            else:
                return self.getToken(OParser.COMMA, i)

        def getRuleIndex(self):
            return OParser.RULE_symbol_list

        def enterRule(self, listener):
            if hasattr(listener, "enterSymbol_list"):
                listener.enterSymbol_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSymbol_list"):
                listener.exitSymbol_list(self)




    def symbol_list(self):

        localctx = OParser.Symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_symbol_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1417
            self.symbol_identifier()
            self.state = 1422
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1418
                self.match(OParser.COMMA)
                self.state = 1419
                self.symbol_identifier()
                self.state = 1424
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_constraintContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Attribute_constraintContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_attribute_constraint

     
        def copyFrom(self, ctx):
            super(OParser.Attribute_constraintContext, self).copyFrom(ctx)



    class MatchingSetContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a OParser.Attribute_constraintContext)
            super(OParser.MatchingSetContext, self).__init__(parser)
            self.source = None # Set_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(OParser.IN, 0)
        def set_literal(self):
            return self.getTypedRuleContext(OParser.Set_literalContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMatchingSet"):
                listener.enterMatchingSet(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingSet"):
                listener.exitMatchingSet(self)


    class MatchingPatternContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a OParser.Attribute_constraintContext)
            super(OParser.MatchingPatternContext, self).__init__(parser)
            self.text = None # Token
            self.copyFrom(ctx)

        def MATCHING(self):
            return self.getToken(OParser.MATCHING, 0)
        def TEXT_LITERAL(self):
            return self.getToken(OParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterMatchingPattern"):
                listener.enterMatchingPattern(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingPattern"):
                listener.exitMatchingPattern(self)


    class MatchingListContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a OParser.Attribute_constraintContext)
            super(OParser.MatchingListContext, self).__init__(parser)
            self.source = None # List_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(OParser.IN, 0)
        def list_literal(self):
            return self.getTypedRuleContext(OParser.List_literalContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMatchingList"):
                listener.enterMatchingList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingList"):
                listener.exitMatchingList(self)


    class MatchingRangeContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a OParser.Attribute_constraintContext)
            super(OParser.MatchingRangeContext, self).__init__(parser)
            self.source = None # Range_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(OParser.IN, 0)
        def range_literal(self):
            return self.getTypedRuleContext(OParser.Range_literalContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMatchingRange"):
                listener.enterMatchingRange(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingRange"):
                listener.exitMatchingRange(self)


    class MatchingExpressionContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a OParser.Attribute_constraintContext)
            super(OParser.MatchingExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def MATCHING(self):
            return self.getToken(OParser.MATCHING, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMatchingExpression"):
                listener.enterMatchingExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingExpression"):
                listener.exitMatchingExpression(self)



    def attribute_constraint(self):

        localctx = OParser.Attribute_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_attribute_constraint)
        try:
            self.state = 1435
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,98,self._ctx)
            if la_ == 1:
                localctx = OParser.MatchingListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1425
                self.match(OParser.IN)
                self.state = 1426
                localctx.source = self.list_literal()
                pass

            elif la_ == 2:
                localctx = OParser.MatchingSetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1427
                self.match(OParser.IN)
                self.state = 1428
                localctx.source = self.set_literal()
                pass

            elif la_ == 3:
                localctx = OParser.MatchingRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1429
                self.match(OParser.IN)
                self.state = 1430
                localctx.source = self.range_literal()
                pass

            elif la_ == 4:
                localctx = OParser.MatchingPatternContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1431
                self.match(OParser.MATCHING)
                self.state = 1432
                localctx.text = self.match(OParser.TEXT_LITERAL)
                pass

            elif la_ == 5:
                localctx = OParser.MatchingExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1433
                self.match(OParser.MATCHING)
                self.state = 1434
                localctx.exp = self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class List_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.List_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)

        def MUTABLE(self):
            return self.getToken(OParser.MUTABLE, 0)

        def expression_list(self):
            return self.getTypedRuleContext(OParser.Expression_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_list_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterList_literal"):
                listener.enterList_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitList_literal"):
                listener.exitList_literal(self)




    def list_literal(self):

        localctx = OParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1438
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.MUTABLE:
                self.state = 1437
                self.match(OParser.MUTABLE)


            self.state = 1440
            self.match(OParser.LBRAK)
            self.state = 1442
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.LTGT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (OParser.EXECUTE - 95)) | (1 << (OParser.FETCH - 95)) | (1 << (OParser.FILTERED - 95)) | (1 << (OParser.MUTABLE - 95)) | (1 << (OParser.NULL - 95)) | (1 << (OParser.READ - 95)) | (1 << (OParser.SELF - 95)) | (1 << (OParser.SORTED - 95)) | (1 << (OParser.THIS - 95)) | (1 << (OParser.BOOLEAN_LITERAL - 95)) | (1 << (OParser.CHAR_LITERAL - 95)) | (1 << (OParser.MIN_INTEGER - 95)) | (1 << (OParser.MAX_INTEGER - 95)) | (1 << (OParser.SYMBOL_IDENTIFIER - 95)))) != 0) or ((((_la - 159)) & ~0x3f) == 0 and ((1 << (_la - 159)) & ((1 << (OParser.TYPE_IDENTIFIER - 159)) | (1 << (OParser.VARIABLE_IDENTIFIER - 159)) | (1 << (OParser.TEXT_LITERAL - 159)) | (1 << (OParser.UUID_LITERAL - 159)) | (1 << (OParser.INTEGER_LITERAL - 159)) | (1 << (OParser.HEXA_LITERAL - 159)) | (1 << (OParser.DECIMAL_LITERAL - 159)) | (1 << (OParser.DATETIME_LITERAL - 159)) | (1 << (OParser.TIME_LITERAL - 159)) | (1 << (OParser.DATE_LITERAL - 159)) | (1 << (OParser.PERIOD_LITERAL - 159)) | (1 << (OParser.VERSION_LITERAL - 159)))) != 0):
                self.state = 1441
                self.expression_list()


            self.state = 1444
            self.match(OParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Set_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Set_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(OParser.LT, 0)

        def GT(self):
            return self.getToken(OParser.GT, 0)

        def MUTABLE(self):
            return self.getToken(OParser.MUTABLE, 0)

        def expression_list(self):
            return self.getTypedRuleContext(OParser.Expression_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_set_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterSet_literal"):
                listener.enterSet_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSet_literal"):
                listener.exitSet_literal(self)




    def set_literal(self):

        localctx = OParser.Set_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_set_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1447
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.MUTABLE:
                self.state = 1446
                self.match(OParser.MUTABLE)


            self.state = 1449
            self.match(OParser.LT)
            self.state = 1451
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.LTGT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (OParser.EXECUTE - 95)) | (1 << (OParser.FETCH - 95)) | (1 << (OParser.FILTERED - 95)) | (1 << (OParser.MUTABLE - 95)) | (1 << (OParser.NULL - 95)) | (1 << (OParser.READ - 95)) | (1 << (OParser.SELF - 95)) | (1 << (OParser.SORTED - 95)) | (1 << (OParser.THIS - 95)) | (1 << (OParser.BOOLEAN_LITERAL - 95)) | (1 << (OParser.CHAR_LITERAL - 95)) | (1 << (OParser.MIN_INTEGER - 95)) | (1 << (OParser.MAX_INTEGER - 95)) | (1 << (OParser.SYMBOL_IDENTIFIER - 95)))) != 0) or ((((_la - 159)) & ~0x3f) == 0 and ((1 << (_la - 159)) & ((1 << (OParser.TYPE_IDENTIFIER - 159)) | (1 << (OParser.VARIABLE_IDENTIFIER - 159)) | (1 << (OParser.TEXT_LITERAL - 159)) | (1 << (OParser.UUID_LITERAL - 159)) | (1 << (OParser.INTEGER_LITERAL - 159)) | (1 << (OParser.HEXA_LITERAL - 159)) | (1 << (OParser.DECIMAL_LITERAL - 159)) | (1 << (OParser.DATETIME_LITERAL - 159)) | (1 << (OParser.TIME_LITERAL - 159)) | (1 << (OParser.DATE_LITERAL - 159)) | (1 << (OParser.PERIOD_LITERAL - 159)) | (1 << (OParser.VERSION_LITERAL - 159)))) != 0):
                self.state = 1450
                self.expression_list()


            self.state = 1453
            self.match(OParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Expression_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(OParser.COMMA)
            else:
                return self.getToken(OParser.COMMA, i)

        def getRuleIndex(self):
            return OParser.RULE_expression_list

        def enterRule(self, listener):
            if hasattr(listener, "enterExpression_list"):
                listener.enterExpression_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExpression_list"):
                listener.exitExpression_list(self)




    def expression_list(self):

        localctx = OParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1455
            self.expression(0)
            self.state = 1460
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1456
                self.match(OParser.COMMA)
                self.state = 1457
                self.expression(0)
                self.state = 1462
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Range_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Range_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.low = None # ExpressionContext
            self.high = None # ExpressionContext

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)

        def RANGE(self):
            return self.getToken(OParser.RANGE, 0)

        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def getRuleIndex(self):
            return OParser.RULE_range_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterRange_literal"):
                listener.enterRange_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRange_literal"):
                listener.exitRange_literal(self)




    def range_literal(self):

        localctx = OParser.Range_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_range_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1463
            self.match(OParser.LBRAK)
            self.state = 1464
            localctx.low = self.expression(0)
            self.state = 1465
            self.match(OParser.RANGE)
            self.state = 1466
            localctx.high = self.expression(0)
            self.state = 1467
            self.match(OParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypedefContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.TypedefContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_typedef

     
        def copyFrom(self, ctx):
            super(OParser.TypedefContext, self).copyFrom(ctx)


    class IteratorTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a OParser.TypedefContext)
            super(OParser.IteratorTypeContext, self).__init__(parser)
            self.i = None # TypedefContext
            self.copyFrom(ctx)

        def ITERATOR(self):
            return self.getToken(OParser.ITERATOR, 0)
        def LT(self):
            return self.getToken(OParser.LT, 0)
        def GT(self):
            return self.getToken(OParser.GT, 0)
        def typedef(self):
            return self.getTypedRuleContext(OParser.TypedefContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIteratorType"):
                listener.enterIteratorType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIteratorType"):
                listener.exitIteratorType(self)


    class SetTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a OParser.TypedefContext)
            super(OParser.SetTypeContext, self).__init__(parser)
            self.s = None # TypedefContext
            self.copyFrom(ctx)

        def LTGT(self):
            return self.getToken(OParser.LTGT, 0)
        def typedef(self):
            return self.getTypedRuleContext(OParser.TypedefContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSetType"):
                listener.enterSetType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSetType"):
                listener.exitSetType(self)


    class ListTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a OParser.TypedefContext)
            super(OParser.ListTypeContext, self).__init__(parser)
            self.l = None # TypedefContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)
        def typedef(self):
            return self.getTypedRuleContext(OParser.TypedefContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterListType"):
                listener.enterListType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitListType"):
                listener.exitListType(self)


    class DictTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a OParser.TypedefContext)
            super(OParser.DictTypeContext, self).__init__(parser)
            self.d = None # TypedefContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)
        def typedef(self):
            return self.getTypedRuleContext(OParser.TypedefContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterDictType"):
                listener.enterDictType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDictType"):
                listener.exitDictType(self)


    class CursorTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a OParser.TypedefContext)
            super(OParser.CursorTypeContext, self).__init__(parser)
            self.c = None # TypedefContext
            self.copyFrom(ctx)

        def CURSOR(self):
            return self.getToken(OParser.CURSOR, 0)
        def LT(self):
            return self.getToken(OParser.LT, 0)
        def GT(self):
            return self.getToken(OParser.GT, 0)
        def typedef(self):
            return self.getTypedRuleContext(OParser.TypedefContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCursorType"):
                listener.enterCursorType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCursorType"):
                listener.exitCursorType(self)


    class PrimaryTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a OParser.TypedefContext)
            super(OParser.PrimaryTypeContext, self).__init__(parser)
            self.p = None # Primary_typeContext
            self.copyFrom(ctx)

        def primary_type(self):
            return self.getTypedRuleContext(OParser.Primary_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPrimaryType"):
                listener.enterPrimaryType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPrimaryType"):
                listener.exitPrimaryType(self)



    def typedef(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.TypedefContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 158
        self.enterRecursionRule(localctx, 158, self.RULE_typedef, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1481
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID, OParser.TYPE_IDENTIFIER]:
                localctx = OParser.PrimaryTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1470
                localctx.p = self.primary_type()
                pass
            elif token in [OParser.CURSOR]:
                localctx = OParser.CursorTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1471
                self.match(OParser.CURSOR)
                self.state = 1472
                self.match(OParser.LT)
                self.state = 1473
                localctx.c = self.typedef(0)
                self.state = 1474
                self.match(OParser.GT)
                pass
            elif token in [OParser.ITERATOR]:
                localctx = OParser.IteratorTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1476
                self.match(OParser.ITERATOR)
                self.state = 1477
                self.match(OParser.LT)
                self.state = 1478
                localctx.i = self.typedef(0)
                self.state = 1479
                self.match(OParser.GT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 1493
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,106,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1491
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,105,self._ctx)
                    if la_ == 1:
                        localctx = OParser.SetTypeContext(self, OParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.s = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1483
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 1484
                        self.match(OParser.LTGT)
                        pass

                    elif la_ == 2:
                        localctx = OParser.ListTypeContext(self, OParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1485
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 1486
                        self.match(OParser.LBRAK)
                        self.state = 1487
                        self.match(OParser.RBRAK)
                        pass

                    elif la_ == 3:
                        localctx = OParser.DictTypeContext(self, OParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.d = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1488
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1489
                        self.match(OParser.LCURL)
                        self.state = 1490
                        self.match(OParser.RCURL)
                        pass

             
                self.state = 1495
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,106,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Primary_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Primary_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_primary_type

     
        def copyFrom(self, ctx):
            super(OParser.Primary_typeContext, self).copyFrom(ctx)



    class NativeTypeContext(Primary_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Primary_typeContext)
            super(OParser.NativeTypeContext, self).__init__(parser)
            self.n = None # Native_typeContext
            self.copyFrom(ctx)

        def native_type(self):
            return self.getTypedRuleContext(OParser.Native_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNativeType"):
                listener.enterNativeType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNativeType"):
                listener.exitNativeType(self)


    class CategoryTypeContext(Primary_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Primary_typeContext)
            super(OParser.CategoryTypeContext, self).__init__(parser)
            self.c = None # Category_typeContext
            self.copyFrom(ctx)

        def category_type(self):
            return self.getTypedRuleContext(OParser.Category_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCategoryType"):
                listener.enterCategoryType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategoryType"):
                listener.exitCategoryType(self)



    def primary_type(self):

        localctx = OParser.Primary_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_primary_type)
        try:
            self.state = 1498
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID]:
                localctx = OParser.NativeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1496
                localctx.n = self.native_type()
                pass
            elif token in [OParser.TYPE_IDENTIFIER]:
                localctx = OParser.CategoryTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1497
                localctx.c = self.category_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_native_type

     
        def copyFrom(self, ctx):
            super(OParser.Native_typeContext, self).copyFrom(ctx)



    class PeriodTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.PeriodTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PERIOD(self):
            return self.getToken(OParser.PERIOD, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPeriodType"):
                listener.enterPeriodType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPeriodType"):
                listener.exitPeriodType(self)


    class BooleanTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.BooleanTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(OParser.BOOLEAN, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterBooleanType"):
                listener.enterBooleanType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBooleanType"):
                listener.exitBooleanType(self)


    class DocumentTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.DocumentTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOCUMENT(self):
            return self.getToken(OParser.DOCUMENT, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDocumentType"):
                listener.enterDocumentType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDocumentType"):
                listener.exitDocumentType(self)


    class CharacterTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.CharacterTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHARACTER(self):
            return self.getToken(OParser.CHARACTER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCharacterType"):
                listener.enterCharacterType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCharacterType"):
                listener.exitCharacterType(self)


    class VersionTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.VersionTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def VERSION(self):
            return self.getToken(OParser.VERSION, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterVersionType"):
                listener.enterVersionType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVersionType"):
                listener.exitVersionType(self)


    class TextTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.TextTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT(self):
            return self.getToken(OParser.TEXT, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterTextType"):
                listener.enterTextType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTextType"):
                listener.exitTextType(self)


    class ImageTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.ImageTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def IMAGE(self):
            return self.getToken(OParser.IMAGE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterImageType"):
                listener.enterImageType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitImageType"):
                listener.exitImageType(self)


    class TimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.TimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TIME(self):
            return self.getToken(OParser.TIME, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterTimeType"):
                listener.enterTimeType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTimeType"):
                listener.exitTimeType(self)


    class IntegerTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.IntegerTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(OParser.INTEGER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterIntegerType"):
                listener.enterIntegerType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIntegerType"):
                listener.exitIntegerType(self)


    class DateTimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.DateTimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATETIME(self):
            return self.getToken(OParser.DATETIME, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDateTimeType"):
                listener.enterDateTimeType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDateTimeType"):
                listener.exitDateTimeType(self)


    class BlobTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.BlobTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BLOB(self):
            return self.getToken(OParser.BLOB, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterBlobType"):
                listener.enterBlobType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBlobType"):
                listener.exitBlobType(self)


    class UUIDTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.UUIDTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def UUID(self):
            return self.getToken(OParser.UUID, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterUUIDType"):
                listener.enterUUIDType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitUUIDType"):
                listener.exitUUIDType(self)


    class DecimalTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.DecimalTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL(self):
            return self.getToken(OParser.DECIMAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDecimalType"):
                listener.enterDecimalType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDecimalType"):
                listener.exitDecimalType(self)


    class CodeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.CodeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(OParser.CODE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCodeType"):
                listener.enterCodeType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCodeType"):
                listener.exitCodeType(self)


    class DateTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_typeContext)
            super(OParser.DateTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATE(self):
            return self.getToken(OParser.DATE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDateType"):
                listener.enterDateType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDateType"):
                listener.exitDateType(self)



    def native_type(self):

        localctx = OParser.Native_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_native_type)
        try:
            self.state = 1515
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.BOOLEAN]:
                localctx = OParser.BooleanTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1500
                self.match(OParser.BOOLEAN)
                pass
            elif token in [OParser.CHARACTER]:
                localctx = OParser.CharacterTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1501
                self.match(OParser.CHARACTER)
                pass
            elif token in [OParser.TEXT]:
                localctx = OParser.TextTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1502
                self.match(OParser.TEXT)
                pass
            elif token in [OParser.IMAGE]:
                localctx = OParser.ImageTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1503
                self.match(OParser.IMAGE)
                pass
            elif token in [OParser.INTEGER]:
                localctx = OParser.IntegerTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1504
                self.match(OParser.INTEGER)
                pass
            elif token in [OParser.DECIMAL]:
                localctx = OParser.DecimalTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1505
                self.match(OParser.DECIMAL)
                pass
            elif token in [OParser.DOCUMENT]:
                localctx = OParser.DocumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1506
                self.match(OParser.DOCUMENT)
                pass
            elif token in [OParser.DATE]:
                localctx = OParser.DateTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1507
                self.match(OParser.DATE)
                pass
            elif token in [OParser.DATETIME]:
                localctx = OParser.DateTimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1508
                self.match(OParser.DATETIME)
                pass
            elif token in [OParser.TIME]:
                localctx = OParser.TimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1509
                self.match(OParser.TIME)
                pass
            elif token in [OParser.PERIOD]:
                localctx = OParser.PeriodTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1510
                self.match(OParser.PERIOD)
                pass
            elif token in [OParser.VERSION]:
                localctx = OParser.VersionTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1511
                self.match(OParser.VERSION)
                pass
            elif token in [OParser.CODE]:
                localctx = OParser.CodeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1512
                self.match(OParser.CODE)
                pass
            elif token in [OParser.BLOB]:
                localctx = OParser.BlobTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1513
                self.match(OParser.BLOB)
                pass
            elif token in [OParser.UUID]:
                localctx = OParser.UUIDTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 1514
                self.match(OParser.UUID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Category_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def TYPE_IDENTIFIER(self):
            return self.getToken(OParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_category_type

        def enterRule(self, listener):
            if hasattr(listener, "enterCategory_type"):
                listener.enterCategory_type(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategory_type"):
                listener.exitCategory_type(self)




    def category_type(self):

        localctx = OParser.Category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_category_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1517
            localctx.t1 = self.match(OParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Mutable_category_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Mutable_category_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def category_type(self):
            return self.getTypedRuleContext(OParser.Category_typeContext,0)


        def MUTABLE(self):
            return self.getToken(OParser.MUTABLE, 0)

        def getRuleIndex(self):
            return OParser.RULE_mutable_category_type

        def enterRule(self, listener):
            if hasattr(listener, "enterMutable_category_type"):
                listener.enterMutable_category_type(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMutable_category_type"):
                listener.exitMutable_category_type(self)




    def mutable_category_type(self):

        localctx = OParser.Mutable_category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_mutable_category_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1520
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.MUTABLE:
                self.state = 1519
                self.match(OParser.MUTABLE)


            self.state = 1522
            self.category_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Code_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Code_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def CODE(self):
            return self.getToken(OParser.CODE, 0)

        def getRuleIndex(self):
            return OParser.RULE_code_type

        def enterRule(self, listener):
            if hasattr(listener, "enterCode_type"):
                listener.enterCode_type(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCode_type"):
                listener.exitCode_type(self)




    def code_type(self):

        localctx = OParser.Code_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_code_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1524
            localctx.t1 = self.match(OParser.CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_category_declaration

     
        def copyFrom(self, ctx):
            super(OParser.Category_declarationContext, self).copyFrom(ctx)



    class ConcreteCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a OParser.Category_declarationContext)
            super(OParser.ConcreteCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Concrete_category_declarationContext
            self.copyFrom(ctx)

        def concrete_category_declaration(self):
            return self.getTypedRuleContext(OParser.Concrete_category_declarationContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterConcreteCategoryDeclaration"):
                listener.enterConcreteCategoryDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConcreteCategoryDeclaration"):
                listener.exitConcreteCategoryDeclaration(self)


    class NativeCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a OParser.Category_declarationContext)
            super(OParser.NativeCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Native_category_declarationContext
            self.copyFrom(ctx)

        def native_category_declaration(self):
            return self.getTypedRuleContext(OParser.Native_category_declarationContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNativeCategoryDeclaration"):
                listener.enterNativeCategoryDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNativeCategoryDeclaration"):
                listener.exitNativeCategoryDeclaration(self)


    class SingletonCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a OParser.Category_declarationContext)
            super(OParser.SingletonCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Singleton_category_declarationContext
            self.copyFrom(ctx)

        def singleton_category_declaration(self):
            return self.getTypedRuleContext(OParser.Singleton_category_declarationContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSingletonCategoryDeclaration"):
                listener.enterSingletonCategoryDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSingletonCategoryDeclaration"):
                listener.exitSingletonCategoryDeclaration(self)



    def category_declaration(self):

        localctx = OParser.Category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_category_declaration)
        try:
            self.state = 1529
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,110,self._ctx)
            if la_ == 1:
                localctx = OParser.ConcreteCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1526
                localctx.decl = self.concrete_category_declaration()
                pass

            elif la_ == 2:
                localctx = OParser.NativeCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1527
                localctx.decl = self.native_category_declaration()
                pass

            elif la_ == 3:
                localctx = OParser.SingletonCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1528
                localctx.decl = self.singleton_category_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_identifier_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Type_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def type_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Type_identifierContext)
            else:
                return self.getTypedRuleContext(OParser.Type_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(OParser.COMMA)
            else:
                return self.getToken(OParser.COMMA, i)

        def getRuleIndex(self):
            return OParser.RULE_type_identifier_list

        def enterRule(self, listener):
            if hasattr(listener, "enterType_identifier_list"):
                listener.enterType_identifier_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitType_identifier_list"):
                listener.exitType_identifier_list(self)




    def type_identifier_list(self):

        localctx = OParser.Type_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_type_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1531
            self.type_identifier()
            self.state = 1536
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1532
                self.match(OParser.COMMA)
                self.state = 1533
                self.type_identifier()
                self.state = 1538
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Method_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def getRuleIndex(self):
            return OParser.RULE_method_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterMethod_identifier"):
                listener.enterMethod_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethod_identifier"):
                listener.exitMethod_identifier(self)




    def method_identifier(self):

        localctx = OParser.Method_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_method_identifier)
        try:
            self.state = 1541
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.VARIABLE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1539
                self.variable_identifier()
                pass
            elif token in [OParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1540
                self.type_identifier()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.IdentifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_identifier

     
        def copyFrom(self, ctx):
            super(OParser.IdentifierContext, self).copyFrom(ctx)



    class TypeIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a OParser.IdentifierContext)
            super(OParser.TypeIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(OParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterTypeIdentifier"):
                listener.enterTypeIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTypeIdentifier"):
                listener.exitTypeIdentifier(self)


    class SymbolIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a OParser.IdentifierContext)
            super(OParser.SymbolIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def symbol_identifier(self):
            return self.getTypedRuleContext(OParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSymbolIdentifier"):
                listener.enterSymbolIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSymbolIdentifier"):
                listener.exitSymbolIdentifier(self)


    class VariableIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a OParser.IdentifierContext)
            super(OParser.VariableIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterVariableIdentifier"):
                listener.enterVariableIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVariableIdentifier"):
                listener.exitVariableIdentifier(self)



    def identifier(self):

        localctx = OParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_identifier)
        try:
            self.state = 1546
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.VARIABLE_IDENTIFIER]:
                localctx = OParser.VariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1543
                self.variable_identifier()
                pass
            elif token in [OParser.TYPE_IDENTIFIER]:
                localctx = OParser.TypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1544
                self.type_identifier()
                pass
            elif token in [OParser.SYMBOL_IDENTIFIER]:
                localctx = OParser.SymbolIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1545
                self.symbol_identifier()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Variable_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Variable_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_variable_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterVariable_identifier"):
                listener.enterVariable_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVariable_identifier"):
                listener.exitVariable_identifier(self)




    def variable_identifier(self):

        localctx = OParser.Variable_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_variable_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1548
            self.match(OParser.VARIABLE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Attribute_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def STORABLE(self):
            return self.getToken(OParser.STORABLE, 0)

        def getRuleIndex(self):
            return OParser.RULE_attribute_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterAttribute_identifier"):
                listener.enterAttribute_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAttribute_identifier"):
                listener.exitAttribute_identifier(self)




    def attribute_identifier(self):

        localctx = OParser.Attribute_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_attribute_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1550
            _la = self._input.LA(1)
            if not(_la==OParser.STORABLE or _la==OParser.VARIABLE_IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Type_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TYPE_IDENTIFIER(self):
            return self.getToken(OParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_type_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterType_identifier"):
                listener.enterType_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitType_identifier"):
                listener.exitType_identifier(self)




    def type_identifier(self):

        localctx = OParser.Type_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_type_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1552
            self.match(OParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Symbol_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Symbol_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(OParser.SYMBOL_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_symbol_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterSymbol_identifier"):
                listener.enterSymbol_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSymbol_identifier"):
                listener.exitSymbol_identifier(self)




    def symbol_identifier(self):

        localctx = OParser.Symbol_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_symbol_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1554
            self.match(OParser.SYMBOL_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(OParser.ArgumentContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(OParser.COMMA)
            else:
                return self.getToken(OParser.COMMA, i)

        def getRuleIndex(self):
            return OParser.RULE_argument_list

        def enterRule(self, listener):
            if hasattr(listener, "enterArgument_list"):
                listener.enterArgument_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgument_list"):
                listener.exitArgument_list(self)




    def argument_list(self):

        localctx = OParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1556
            self.argument()
            self.state = 1561
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1557
                self.match(OParser.COMMA)
                self.state = 1558
                self.argument()
                self.state = 1563
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.ArgumentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_argument

     
        def copyFrom(self, ctx):
            super(OParser.ArgumentContext, self).copyFrom(ctx)



    class OperatorArgumentContext(ArgumentContext):

        def __init__(self, parser, ctx): # actually a OParser.ArgumentContext)
            super(OParser.OperatorArgumentContext, self).__init__(parser)
            self.arg = None # Operator_argumentContext
            self.copyFrom(ctx)

        def operator_argument(self):
            return self.getTypedRuleContext(OParser.Operator_argumentContext,0)

        def MUTABLE(self):
            return self.getToken(OParser.MUTABLE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorArgument"):
                listener.enterOperatorArgument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorArgument"):
                listener.exitOperatorArgument(self)


    class CodeArgumentContext(ArgumentContext):

        def __init__(self, parser, ctx): # actually a OParser.ArgumentContext)
            super(OParser.CodeArgumentContext, self).__init__(parser)
            self.arg = None # Code_argumentContext
            self.copyFrom(ctx)

        def code_argument(self):
            return self.getTypedRuleContext(OParser.Code_argumentContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCodeArgument"):
                listener.enterCodeArgument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCodeArgument"):
                listener.exitCodeArgument(self)



    def argument(self):

        localctx = OParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.state = 1569
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,116,self._ctx)
            if la_ == 1:
                localctx = OParser.CodeArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1564
                localctx.arg = self.code_argument()
                pass

            elif la_ == 2:
                localctx = OParser.OperatorArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1566
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==OParser.MUTABLE:
                    self.state = 1565
                    self.match(OParser.MUTABLE)


                self.state = 1568
                localctx.arg = self.operator_argument()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Operator_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Operator_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def named_argument(self):
            return self.getTypedRuleContext(OParser.Named_argumentContext,0)


        def typed_argument(self):
            return self.getTypedRuleContext(OParser.Typed_argumentContext,0)


        def getRuleIndex(self):
            return OParser.RULE_operator_argument

        def enterRule(self, listener):
            if hasattr(listener, "enterOperator_argument"):
                listener.enterOperator_argument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperator_argument"):
                listener.exitOperator_argument(self)




    def operator_argument(self):

        localctx = OParser.Operator_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_operator_argument)
        try:
            self.state = 1573
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.VARIABLE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1571
                self.named_argument()
                pass
            elif token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID, OParser.ITERATOR, OParser.CURSOR, OParser.ANY, OParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1572
                self.typed_argument()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Named_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Named_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def EQ(self):
            return self.getToken(OParser.EQ, 0)

        def literal_expression(self):
            return self.getTypedRuleContext(OParser.Literal_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_named_argument

        def enterRule(self, listener):
            if hasattr(listener, "enterNamed_argument"):
                listener.enterNamed_argument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNamed_argument"):
                listener.exitNamed_argument(self)




    def named_argument(self):

        localctx = OParser.Named_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_named_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1575
            self.variable_identifier()
            self.state = 1578
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.EQ:
                self.state = 1576
                self.match(OParser.EQ)
                self.state = 1577
                self.literal_expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Code_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Code_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext

        def code_type(self):
            return self.getTypedRuleContext(OParser.Code_typeContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def getRuleIndex(self):
            return OParser.RULE_code_argument

        def enterRule(self, listener):
            if hasattr(listener, "enterCode_argument"):
                listener.enterCode_argument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCode_argument"):
                listener.exitCode_argument(self)




    def code_argument(self):

        localctx = OParser.Code_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_code_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1580
            self.code_type()
            self.state = 1581
            localctx.name = self.variable_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_or_any_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Category_or_any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def typedef(self):
            return self.getTypedRuleContext(OParser.TypedefContext,0)


        def any_type(self):
            return self.getTypedRuleContext(OParser.Any_typeContext,0)


        def getRuleIndex(self):
            return OParser.RULE_category_or_any_type

        def enterRule(self, listener):
            if hasattr(listener, "enterCategory_or_any_type"):
                listener.enterCategory_or_any_type(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategory_or_any_type"):
                listener.exitCategory_or_any_type(self)




    def category_or_any_type(self):

        localctx = OParser.Category_or_any_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_category_or_any_type)
        try:
            self.state = 1585
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID, OParser.ITERATOR, OParser.CURSOR, OParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1583
                self.typedef(0)
                pass
            elif token in [OParser.ANY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1584
                self.any_type(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Any_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_any_type

     
        def copyFrom(self, ctx):
            super(OParser.Any_typeContext, self).copyFrom(ctx)


    class AnyListTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Any_typeContext)
            super(OParser.AnyListTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def any_type(self):
            return self.getTypedRuleContext(OParser.Any_typeContext,0)

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAnyListType"):
                listener.enterAnyListType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAnyListType"):
                listener.exitAnyListType(self)


    class AnyTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Any_typeContext)
            super(OParser.AnyTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ANY(self):
            return self.getToken(OParser.ANY, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAnyType"):
                listener.enterAnyType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAnyType"):
                listener.exitAnyType(self)


    class AnyDictTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a OParser.Any_typeContext)
            super(OParser.AnyDictTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def any_type(self):
            return self.getTypedRuleContext(OParser.Any_typeContext,0)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAnyDictType"):
                listener.enterAnyDictType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAnyDictType"):
                listener.exitAnyDictType(self)



    def any_type(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Any_typeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 198
        self.enterRecursionRule(localctx, 198, self.RULE_any_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.AnyTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1588
            self.match(OParser.ANY)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1598
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,121,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1596
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,120,self._ctx)
                    if la_ == 1:
                        localctx = OParser.AnyListTypeContext(self, OParser.Any_typeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1590
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1591
                        self.match(OParser.LBRAK)
                        self.state = 1592
                        self.match(OParser.RBRAK)
                        pass

                    elif la_ == 2:
                        localctx = OParser.AnyDictTypeContext(self, OParser.Any_typeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1593
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1594
                        self.match(OParser.LCURL)
                        self.state = 1595
                        self.match(OParser.RCURL)
                        pass

             
                self.state = 1600
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,121,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Member_method_declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Member_method_declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def member_method_declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Member_method_declarationContext)
            else:
                return self.getTypedRuleContext(OParser.Member_method_declarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.LfpContext)
            else:
                return self.getTypedRuleContext(OParser.LfpContext,i)


        def getRuleIndex(self):
            return OParser.RULE_member_method_declaration_list

        def enterRule(self, listener):
            if hasattr(listener, "enterMember_method_declaration_list"):
                listener.enterMember_method_declaration_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMember_method_declaration_list"):
                listener.exitMember_method_declaration_list(self)




    def member_method_declaration_list(self):

        localctx = OParser.Member_method_declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_member_method_declaration_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1601
            self.member_method_declaration()
            self.state = 1607
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ABSTRACT - 46)) | (1 << (OParser.GETTER - 46)))) != 0) or ((((_la - 112)) & ~0x3f) == 0 and ((1 << (_la - 112)) & ((1 << (OParser.METHOD - 112)) | (1 << (OParser.OPERATOR - 112)) | (1 << (OParser.SETTER - 112)) | (1 << (OParser.TYPE_IDENTIFIER - 112)))) != 0):
                self.state = 1602
                self.lfp()
                self.state = 1603
                self.member_method_declaration()
                self.state = 1609
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def setter_method_declaration(self):
            return self.getTypedRuleContext(OParser.Setter_method_declarationContext,0)


        def getter_method_declaration(self):
            return self.getTypedRuleContext(OParser.Getter_method_declarationContext,0)


        def concrete_method_declaration(self):
            return self.getTypedRuleContext(OParser.Concrete_method_declarationContext,0)


        def abstract_method_declaration(self):
            return self.getTypedRuleContext(OParser.Abstract_method_declarationContext,0)


        def operator_method_declaration(self):
            return self.getTypedRuleContext(OParser.Operator_method_declarationContext,0)


        def getRuleIndex(self):
            return OParser.RULE_member_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterMember_method_declaration"):
                listener.enterMember_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMember_method_declaration"):
                listener.exitMember_method_declaration(self)




    def member_method_declaration(self):

        localctx = OParser.Member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_member_method_declaration)
        try:
            self.state = 1615
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,123,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1610
                self.setter_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1611
                self.getter_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1612
                self.concrete_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1613
                self.abstract_method_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1614
                self.operator_method_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_member_method_declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_member_method_declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_member_method_declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Native_member_method_declarationContext)
            else:
                return self.getTypedRuleContext(OParser.Native_member_method_declarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.LfpContext)
            else:
                return self.getTypedRuleContext(OParser.LfpContext,i)


        def getRuleIndex(self):
            return OParser.RULE_native_member_method_declaration_list

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_member_method_declaration_list"):
                listener.enterNative_member_method_declaration_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_member_method_declaration_list"):
                listener.exitNative_member_method_declaration_list(self)




    def native_member_method_declaration_list(self):

        localctx = OParser.Native_member_method_declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_native_member_method_declaration_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1617
            self.native_member_method_declaration()
            self.state = 1623
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ANY - 46)) | (1 << (OParser.GETTER - 46)))) != 0) or ((((_la - 112)) & ~0x3f) == 0 and ((1 << (_la - 112)) & ((1 << (OParser.METHOD - 112)) | (1 << (OParser.NATIVE - 112)) | (1 << (OParser.SETTER - 112)) | (1 << (OParser.TYPE_IDENTIFIER - 112)))) != 0):
                self.state = 1618
                self.lfp()
                self.state = 1619
                self.native_member_method_declaration()
                self.state = 1625
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_getter_declaration(self):
            return self.getTypedRuleContext(OParser.Native_getter_declarationContext,0)


        def native_setter_declaration(self):
            return self.getTypedRuleContext(OParser.Native_setter_declarationContext,0)


        def native_method_declaration(self):
            return self.getTypedRuleContext(OParser.Native_method_declarationContext,0)


        def getRuleIndex(self):
            return OParser.RULE_native_member_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_member_method_declaration"):
                listener.enterNative_member_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_member_method_declaration"):
                listener.exitNative_member_method_declaration(self)




    def native_member_method_declaration(self):

        localctx = OParser.Native_member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 206, self.RULE_native_member_method_declaration)
        try:
            self.state = 1629
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,125,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1626
                self.native_getter_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1627
                self.native_setter_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1628
                self.native_method_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_category_bindingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_native_category_binding

     
        def copyFrom(self, ctx):
            super(OParser.Native_category_bindingContext, self).copyFrom(ctx)



    class Python2CategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_category_bindingContext)
            super(OParser.Python2CategoryBindingContext, self).__init__(parser)
            self.binding = None # Python_category_bindingContext
            self.copyFrom(ctx)

        def PYTHON2(self):
            return self.getToken(OParser.PYTHON2, 0)
        def python_category_binding(self):
            return self.getTypedRuleContext(OParser.Python_category_bindingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPython2CategoryBinding"):
                listener.enterPython2CategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython2CategoryBinding"):
                listener.exitPython2CategoryBinding(self)


    class Python3CategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_category_bindingContext)
            super(OParser.Python3CategoryBindingContext, self).__init__(parser)
            self.binding = None # Python_category_bindingContext
            self.copyFrom(ctx)

        def PYTHON3(self):
            return self.getToken(OParser.PYTHON3, 0)
        def python_category_binding(self):
            return self.getTypedRuleContext(OParser.Python_category_bindingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPython3CategoryBinding"):
                listener.enterPython3CategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython3CategoryBinding"):
                listener.exitPython3CategoryBinding(self)


    class JavaCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_category_bindingContext)
            super(OParser.JavaCategoryBindingContext, self).__init__(parser)
            self.binding = None # Java_class_identifier_expressionContext
            self.copyFrom(ctx)

        def JAVA(self):
            return self.getToken(OParser.JAVA, 0)
        def java_class_identifier_expression(self):
            return self.getTypedRuleContext(OParser.Java_class_identifier_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaCategoryBinding"):
                listener.enterJavaCategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaCategoryBinding"):
                listener.exitJavaCategoryBinding(self)


    class CSharpCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_category_bindingContext)
            super(OParser.CSharpCategoryBindingContext, self).__init__(parser)
            self.binding = None # Csharp_identifier_expressionContext
            self.copyFrom(ctx)

        def CSHARP(self):
            return self.getToken(OParser.CSHARP, 0)
        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_identifier_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpCategoryBinding"):
                listener.enterCSharpCategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpCategoryBinding"):
                listener.exitCSharpCategoryBinding(self)


    class JavaScriptCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_category_bindingContext)
            super(OParser.JavaScriptCategoryBindingContext, self).__init__(parser)
            self.binding = None # Javascript_category_bindingContext
            self.copyFrom(ctx)

        def JAVASCRIPT(self):
            return self.getToken(OParser.JAVASCRIPT, 0)
        def javascript_category_binding(self):
            return self.getTypedRuleContext(OParser.Javascript_category_bindingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaScriptCategoryBinding"):
                listener.enterJavaScriptCategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptCategoryBinding"):
                listener.exitJavaScriptCategoryBinding(self)



    def native_category_binding(self):

        localctx = OParser.Native_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_native_category_binding)
        try:
            self.state = 1641
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.JAVA]:
                localctx = OParser.JavaCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1631
                self.match(OParser.JAVA)
                self.state = 1632
                localctx.binding = self.java_class_identifier_expression(0)
                pass
            elif token in [OParser.CSHARP]:
                localctx = OParser.CSharpCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1633
                self.match(OParser.CSHARP)
                self.state = 1634
                localctx.binding = self.csharp_identifier_expression(0)
                pass
            elif token in [OParser.PYTHON2]:
                localctx = OParser.Python2CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1635
                self.match(OParser.PYTHON2)
                self.state = 1636
                localctx.binding = self.python_category_binding()
                pass
            elif token in [OParser.PYTHON3]:
                localctx = OParser.Python3CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1637
                self.match(OParser.PYTHON3)
                self.state = 1638
                localctx.binding = self.python_category_binding()
                pass
            elif token in [OParser.JAVASCRIPT]:
                localctx = OParser.JavaScriptCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1639
                self.match(OParser.JAVASCRIPT)
                self.state = 1640
                localctx.binding = self.javascript_category_binding()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_category_bindingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(OParser.IdentifierContext,0)


        def python_module(self):
            return self.getTypedRuleContext(OParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return OParser.RULE_python_category_binding

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_category_binding"):
                listener.enterPython_category_binding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_category_binding"):
                listener.exitPython_category_binding(self)




    def python_category_binding(self):

        localctx = OParser.Python_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_python_category_binding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1643
            self.identifier()
            self.state = 1645
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.FROM:
                self.state = 1644
                self.python_module()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_moduleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_moduleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(OParser.FROM, 0)

        def module_token(self):
            return self.getTypedRuleContext(OParser.Module_tokenContext,0)


        def COLON(self):
            return self.getToken(OParser.COLON, 0)

        def identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(OParser.IdentifierContext,i)


        def DOT(self, i=None):
            if i is None:
                return self.getTokens(OParser.DOT)
            else:
                return self.getToken(OParser.DOT, i)

        def getRuleIndex(self):
            return OParser.RULE_python_module

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_module"):
                listener.enterPython_module(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_module"):
                listener.exitPython_module(self)




    def python_module(self):

        localctx = OParser.Python_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_python_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1647
            self.match(OParser.FROM)
            self.state = 1648
            self.module_token()
            self.state = 1649
            self.match(OParser.COLON)
            self.state = 1650
            self.identifier()
            self.state = 1655
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.DOT:
                self.state = 1651
                self.match(OParser.DOT)
                self.state = 1652
                self.identifier()
                self.state = 1657
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_category_bindingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(OParser.IdentifierContext,0)


        def javascript_module(self):
            return self.getTypedRuleContext(OParser.Javascript_moduleContext,0)


        def getRuleIndex(self):
            return OParser.RULE_javascript_category_binding

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_category_binding"):
                listener.enterJavascript_category_binding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_category_binding"):
                listener.exitJavascript_category_binding(self)




    def javascript_category_binding(self):

        localctx = OParser.Javascript_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_javascript_category_binding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1658
            self.identifier()
            self.state = 1660
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.FROM:
                self.state = 1659
                self.javascript_module()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_moduleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_moduleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(OParser.FROM, 0)

        def module_token(self):
            return self.getTypedRuleContext(OParser.Module_tokenContext,0)


        def COLON(self):
            return self.getToken(OParser.COLON, 0)

        def javascript_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Javascript_identifierContext)
            else:
                return self.getTypedRuleContext(OParser.Javascript_identifierContext,i)


        def SLASH(self, i=None):
            if i is None:
                return self.getTokens(OParser.SLASH)
            else:
                return self.getToken(OParser.SLASH, i)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)

        def getRuleIndex(self):
            return OParser.RULE_javascript_module

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_module"):
                listener.enterJavascript_module(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_module"):
                listener.exitJavascript_module(self)




    def javascript_module(self):

        localctx = OParser.Javascript_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_javascript_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1662
            self.match(OParser.FROM)
            self.state = 1663
            self.module_token()
            self.state = 1664
            self.match(OParser.COLON)
            self.state = 1666
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.SLASH:
                self.state = 1665
                self.match(OParser.SLASH)


            self.state = 1668
            self.javascript_identifier()
            self.state = 1673
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.SLASH:
                self.state = 1669
                self.match(OParser.SLASH)
                self.state = 1670
                self.javascript_identifier()
                self.state = 1675
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1678
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.DOT:
                self.state = 1676
                self.match(OParser.DOT)
                self.state = 1677
                self.javascript_identifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Variable_identifier_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Variable_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(OParser.Variable_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(OParser.COMMA)
            else:
                return self.getToken(OParser.COMMA, i)

        def getRuleIndex(self):
            return OParser.RULE_variable_identifier_list

        def enterRule(self, listener):
            if hasattr(listener, "enterVariable_identifier_list"):
                listener.enterVariable_identifier_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVariable_identifier_list"):
                listener.exitVariable_identifier_list(self)




    def variable_identifier_list(self):

        localctx = OParser.Variable_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_variable_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1680
            self.variable_identifier()
            self.state = 1685
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1681
                self.match(OParser.COMMA)
                self.state = 1682
                self.variable_identifier()
                self.state = 1687
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_identifier_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Attribute_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def attribute_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Attribute_identifierContext)
            else:
                return self.getTypedRuleContext(OParser.Attribute_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(OParser.COMMA)
            else:
                return self.getToken(OParser.COMMA, i)

        def getRuleIndex(self):
            return OParser.RULE_attribute_identifier_list

        def enterRule(self, listener):
            if hasattr(listener, "enterAttribute_identifier_list"):
                listener.enterAttribute_identifier_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAttribute_identifier_list"):
                listener.exitAttribute_identifier_list(self)




    def attribute_identifier_list(self):

        localctx = OParser.Attribute_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 220, self.RULE_attribute_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1688
            self.attribute_identifier()
            self.state = 1693
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1689
                self.match(OParser.COMMA)
                self.state = 1690
                self.attribute_identifier()
                self.state = 1695
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def abstract_method_declaration(self):
            return self.getTypedRuleContext(OParser.Abstract_method_declarationContext,0)


        def concrete_method_declaration(self):
            return self.getTypedRuleContext(OParser.Concrete_method_declarationContext,0)


        def native_method_declaration(self):
            return self.getTypedRuleContext(OParser.Native_method_declarationContext,0)


        def test_method_declaration(self):
            return self.getTypedRuleContext(OParser.Test_method_declarationContext,0)


        def getRuleIndex(self):
            return OParser.RULE_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterMethod_declaration"):
                listener.enterMethod_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethod_declaration"):
                listener.exitMethod_declaration(self)




    def method_declaration(self):

        localctx = OParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 222, self.RULE_method_declaration)
        try:
            self.state = 1700
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,135,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1696
                self.abstract_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1697
                self.concrete_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1698
                self.native_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1699
                self.test_method_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Comment_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Comment_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(OParser.COMMENT, 0)

        def getRuleIndex(self):
            return OParser.RULE_comment_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterComment_statement"):
                listener.enterComment_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitComment_statement"):
                listener.exitComment_statement(self)




    def comment_statement(self):

        localctx = OParser.Comment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 224, self.RULE_comment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1702
            self.match(OParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Native_statementContext)
            else:
                return self.getTypedRuleContext(OParser.Native_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.LfpContext)
            else:
                return self.getTypedRuleContext(OParser.LfpContext,i)


        def getRuleIndex(self):
            return OParser.RULE_native_statement_list

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_statement_list"):
                listener.enterNative_statement_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_statement_list"):
                listener.exitNative_statement_list(self)




    def native_statement_list(self):

        localctx = OParser.Native_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 226, self.RULE_native_statement_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1704
            self.native_statement()
            self.state = 1710
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.JAVA) | (1 << OParser.CSHARP) | (1 << OParser.PYTHON2) | (1 << OParser.PYTHON3) | (1 << OParser.JAVASCRIPT))) != 0):
                self.state = 1705
                self.lfp()
                self.state = 1706
                self.native_statement()
                self.state = 1712
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_native_statement

     
        def copyFrom(self, ctx):
            super(OParser.Native_statementContext, self).copyFrom(ctx)



    class CSharpNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_statementContext)
            super(OParser.CSharpNativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CSHARP(self):
            return self.getToken(OParser.CSHARP, 0)
        def csharp_statement(self):
            return self.getTypedRuleContext(OParser.Csharp_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpNativeStatement"):
                listener.enterCSharpNativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpNativeStatement"):
                listener.exitCSharpNativeStatement(self)


    class JavaNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_statementContext)
            super(OParser.JavaNativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def JAVA(self):
            return self.getToken(OParser.JAVA, 0)
        def java_statement(self):
            return self.getTypedRuleContext(OParser.Java_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaNativeStatement"):
                listener.enterJavaNativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaNativeStatement"):
                listener.exitJavaNativeStatement(self)


    class JavaScriptNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_statementContext)
            super(OParser.JavaScriptNativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def JAVASCRIPT(self):
            return self.getToken(OParser.JAVASCRIPT, 0)
        def javascript_native_statement(self):
            return self.getTypedRuleContext(OParser.Javascript_native_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaScriptNativeStatement"):
                listener.enterJavaScriptNativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptNativeStatement"):
                listener.exitJavaScriptNativeStatement(self)


    class Python2NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_statementContext)
            super(OParser.Python2NativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PYTHON2(self):
            return self.getToken(OParser.PYTHON2, 0)
        def python_native_statement(self):
            return self.getTypedRuleContext(OParser.Python_native_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPython2NativeStatement"):
                listener.enterPython2NativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython2NativeStatement"):
                listener.exitPython2NativeStatement(self)


    class Python3NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Native_statementContext)
            super(OParser.Python3NativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PYTHON3(self):
            return self.getToken(OParser.PYTHON3, 0)
        def python_native_statement(self):
            return self.getTypedRuleContext(OParser.Python_native_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPython3NativeStatement"):
                listener.enterPython3NativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython3NativeStatement"):
                listener.exitPython3NativeStatement(self)



    def native_statement(self):

        localctx = OParser.Native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 228, self.RULE_native_statement)
        try:
            self.state = 1723
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.JAVA]:
                localctx = OParser.JavaNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1713
                self.match(OParser.JAVA)
                self.state = 1714
                self.java_statement()
                pass
            elif token in [OParser.CSHARP]:
                localctx = OParser.CSharpNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1715
                self.match(OParser.CSHARP)
                self.state = 1716
                self.csharp_statement()
                pass
            elif token in [OParser.PYTHON2]:
                localctx = OParser.Python2NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1717
                self.match(OParser.PYTHON2)
                self.state = 1718
                self.python_native_statement()
                pass
            elif token in [OParser.PYTHON3]:
                localctx = OParser.Python3NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1719
                self.match(OParser.PYTHON3)
                self.state = 1720
                self.python_native_statement()
                pass
            elif token in [OParser.JAVASCRIPT]:
                localctx = OParser.JavaScriptNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1721
                self.match(OParser.JAVASCRIPT)
                self.state = 1722
                self.javascript_native_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_native_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def python_statement(self):
            return self.getTypedRuleContext(OParser.Python_statementContext,0)


        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def python_module(self):
            return self.getTypedRuleContext(OParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return OParser.RULE_python_native_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_native_statement"):
                listener.enterPython_native_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_native_statement"):
                listener.exitPython_native_statement(self)




    def python_native_statement(self):

        localctx = OParser.Python_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 230, self.RULE_python_native_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1725
            self.python_statement()
            self.state = 1727
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.SEMI:
                self.state = 1726
                self.match(OParser.SEMI)


            self.state = 1730
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.FROM:
                self.state = 1729
                self.python_module()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_native_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def javascript_statement(self):
            return self.getTypedRuleContext(OParser.Javascript_statementContext,0)


        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)

        def javascript_module(self):
            return self.getTypedRuleContext(OParser.Javascript_moduleContext,0)


        def getRuleIndex(self):
            return OParser.RULE_javascript_native_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_native_statement"):
                listener.enterJavascript_native_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_native_statement"):
                listener.exitJavascript_native_statement(self)




    def javascript_native_statement(self):

        localctx = OParser.Javascript_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_javascript_native_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1732
            self.javascript_statement()
            self.state = 1734
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.SEMI:
                self.state = 1733
                self.match(OParser.SEMI)


            self.state = 1737
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.FROM:
                self.state = 1736
                self.javascript_module()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.StatementContext)
            else:
                return self.getTypedRuleContext(OParser.StatementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.LfpContext)
            else:
                return self.getTypedRuleContext(OParser.LfpContext,i)


        def getRuleIndex(self):
            return OParser.RULE_statement_list

        def enterRule(self, listener):
            if hasattr(listener, "enterStatement_list"):
                listener.enterStatement_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStatement_list"):
                listener.exitStatement_list(self)




    def statement_list(self):

        localctx = OParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_statement_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1739
            self.statement()
            self.state = 1745
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                self.state = 1740
                self.lfp()
                self.state = 1741
                self.statement()
                self.state = 1747
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assertion_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Assertion_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assertion(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.AssertionContext)
            else:
                return self.getTypedRuleContext(OParser.AssertionContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.LfpContext)
            else:
                return self.getTypedRuleContext(OParser.LfpContext,i)


        def getRuleIndex(self):
            return OParser.RULE_assertion_list

        def enterRule(self, listener):
            if hasattr(listener, "enterAssertion_list"):
                listener.enterAssertion_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssertion_list"):
                listener.exitAssertion_list(self)




    def assertion_list(self):

        localctx = OParser.Assertion_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_assertion_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1748
            self.assertion()
            self.state = 1754
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.LTGT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (OParser.EXECUTE - 95)) | (1 << (OParser.FETCH - 95)) | (1 << (OParser.FILTERED - 95)) | (1 << (OParser.MUTABLE - 95)) | (1 << (OParser.NULL - 95)) | (1 << (OParser.READ - 95)) | (1 << (OParser.SELF - 95)) | (1 << (OParser.SORTED - 95)) | (1 << (OParser.THIS - 95)) | (1 << (OParser.BOOLEAN_LITERAL - 95)) | (1 << (OParser.CHAR_LITERAL - 95)) | (1 << (OParser.MIN_INTEGER - 95)) | (1 << (OParser.MAX_INTEGER - 95)) | (1 << (OParser.SYMBOL_IDENTIFIER - 95)))) != 0) or ((((_la - 159)) & ~0x3f) == 0 and ((1 << (_la - 159)) & ((1 << (OParser.TYPE_IDENTIFIER - 159)) | (1 << (OParser.VARIABLE_IDENTIFIER - 159)) | (1 << (OParser.TEXT_LITERAL - 159)) | (1 << (OParser.UUID_LITERAL - 159)) | (1 << (OParser.INTEGER_LITERAL - 159)) | (1 << (OParser.HEXA_LITERAL - 159)) | (1 << (OParser.DECIMAL_LITERAL - 159)) | (1 << (OParser.DATETIME_LITERAL - 159)) | (1 << (OParser.TIME_LITERAL - 159)) | (1 << (OParser.DATE_LITERAL - 159)) | (1 << (OParser.PERIOD_LITERAL - 159)) | (1 << (OParser.VERSION_LITERAL - 159)))) != 0):
                self.state = 1749
                self.lfp()
                self.state = 1750
                self.assertion()
                self.state = 1756
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Switch_case_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Switch_case_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def switch_case_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Switch_case_statementContext)
            else:
                return self.getTypedRuleContext(OParser.Switch_case_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.LfpContext)
            else:
                return self.getTypedRuleContext(OParser.LfpContext,i)


        def getRuleIndex(self):
            return OParser.RULE_switch_case_statement_list

        def enterRule(self, listener):
            if hasattr(listener, "enterSwitch_case_statement_list"):
                listener.enterSwitch_case_statement_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSwitch_case_statement_list"):
                listener.exitSwitch_case_statement_list(self)




    def switch_case_statement_list(self):

        localctx = OParser.Switch_case_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_switch_case_statement_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1757
            self.switch_case_statement()
            self.state = 1763
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.CASE:
                self.state = 1758
                self.lfp()
                self.state = 1759
                self.switch_case_statement()
                self.state = 1765
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Catch_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Catch_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def catch_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Catch_statementContext)
            else:
                return self.getTypedRuleContext(OParser.Catch_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.LfpContext)
            else:
                return self.getTypedRuleContext(OParser.LfpContext,i)


        def getRuleIndex(self):
            return OParser.RULE_catch_statement_list

        def enterRule(self, listener):
            if hasattr(listener, "enterCatch_statement_list"):
                listener.enterCatch_statement_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCatch_statement_list"):
                listener.exitCatch_statement_list(self)




    def catch_statement_list(self):

        localctx = OParser.Catch_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_catch_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1766
            self.catch_statement()
            self.state = 1772
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,145,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1767
                    self.lfp()
                    self.state = 1768
                    self.catch_statement() 
                self.state = 1774
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,145,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_collectionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Literal_collectionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_literal_collection

     
        def copyFrom(self, ctx):
            super(OParser.Literal_collectionContext, self).copyFrom(ctx)



    class LiteralListLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a OParser.Literal_collectionContext)
            super(OParser.LiteralListLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(OParser.Literal_list_literalContext,0)

        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterLiteralListLiteral"):
                listener.enterLiteralListLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteralListLiteral"):
                listener.exitLiteralListLiteral(self)


    class LiteralRangeLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a OParser.Literal_collectionContext)
            super(OParser.LiteralRangeLiteralContext, self).__init__(parser)
            self.low = None # Atomic_literalContext
            self.high = None # Atomic_literalContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)
        def RANGE(self):
            return self.getToken(OParser.RANGE, 0)
        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)
        def atomic_literal(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Atomic_literalContext)
            else:
                return self.getTypedRuleContext(OParser.Atomic_literalContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterLiteralRangeLiteral"):
                listener.enterLiteralRangeLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteralRangeLiteral"):
                listener.exitLiteralRangeLiteral(self)


    class LiteralSetLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a OParser.Literal_collectionContext)
            super(OParser.LiteralSetLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(OParser.LT, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(OParser.Literal_list_literalContext,0)

        def GT(self):
            return self.getToken(OParser.GT, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterLiteralSetLiteral"):
                listener.enterLiteralSetLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteralSetLiteral"):
                listener.exitLiteralSetLiteral(self)



    def literal_collection(self):

        localctx = OParser.Literal_collectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_literal_collection)
        try:
            self.state = 1789
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,146,self._ctx)
            if la_ == 1:
                localctx = OParser.LiteralRangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1775
                self.match(OParser.LBRAK)
                self.state = 1776
                localctx.low = self.atomic_literal()
                self.state = 1777
                self.match(OParser.RANGE)
                self.state = 1778
                localctx.high = self.atomic_literal()
                self.state = 1779
                self.match(OParser.RBRAK)
                pass

            elif la_ == 2:
                localctx = OParser.LiteralListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1781
                self.match(OParser.LBRAK)
                self.state = 1782
                self.literal_list_literal()
                self.state = 1783
                self.match(OParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = OParser.LiteralSetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1785
                self.match(OParser.LT)
                self.state = 1786
                self.literal_list_literal()
                self.state = 1787
                self.match(OParser.GT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Atomic_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Atomic_literalContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_atomic_literal

     
        def copyFrom(self, ctx):
            super(OParser.Atomic_literalContext, self).copyFrom(ctx)



    class MinIntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.MinIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def MIN_INTEGER(self):
            return self.getToken(OParser.MIN_INTEGER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterMinIntegerLiteral"):
                listener.enterMinIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMinIntegerLiteral"):
                listener.exitMinIntegerLiteral(self)


    class DateLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.DateLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATE_LITERAL(self):
            return self.getToken(OParser.DATE_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDateLiteral"):
                listener.enterDateLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDateLiteral"):
                listener.exitDateLiteral(self)


    class BooleanLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.BooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(OParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterBooleanLiteral"):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBooleanLiteral"):
                listener.exitBooleanLiteral(self)


    class VersionLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.VersionLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def VERSION_LITERAL(self):
            return self.getToken(OParser.VERSION_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterVersionLiteral"):
                listener.enterVersionLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVersionLiteral"):
                listener.exitVersionLiteral(self)


    class HexadecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.HexadecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def HEXA_LITERAL(self):
            return self.getToken(OParser.HEXA_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterHexadecimalLiteral"):
                listener.enterHexadecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHexadecimalLiteral"):
                listener.exitHexadecimalLiteral(self)


    class UUIDLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.UUIDLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def UUID_LITERAL(self):
            return self.getToken(OParser.UUID_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterUUIDLiteral"):
                listener.enterUUIDLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitUUIDLiteral"):
                listener.exitUUIDLiteral(self)


    class MaxIntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.MaxIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def MAX_INTEGER(self):
            return self.getToken(OParser.MAX_INTEGER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterMaxIntegerLiteral"):
                listener.enterMaxIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMaxIntegerLiteral"):
                listener.exitMaxIntegerLiteral(self)


    class DateTimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.DateTimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATETIME_LITERAL(self):
            return self.getToken(OParser.DATETIME_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDateTimeLiteral"):
                listener.enterDateTimeLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDateTimeLiteral"):
                listener.exitDateTimeLiteral(self)


    class PeriodLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.PeriodLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def PERIOD_LITERAL(self):
            return self.getToken(OParser.PERIOD_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPeriodLiteral"):
                listener.enterPeriodLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPeriodLiteral"):
                listener.exitPeriodLiteral(self)


    class DecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.DecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(OParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDecimalLiteral"):
                listener.enterDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDecimalLiteral"):
                listener.exitDecimalLiteral(self)


    class TextLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.TextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(OParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterTextLiteral"):
                listener.enterTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTextLiteral"):
                listener.exitTextLiteral(self)


    class NullLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.NullLiteralContext, self).__init__(parser)
            self.n = None # Null_literalContext
            self.copyFrom(ctx)

        def null_literal(self):
            return self.getTypedRuleContext(OParser.Null_literalContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNullLiteral"):
                listener.enterNullLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNullLiteral"):
                listener.exitNullLiteral(self)


    class IntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.IntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(OParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterIntegerLiteral"):
                listener.enterIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIntegerLiteral"):
                listener.exitIntegerLiteral(self)


    class TimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.TimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TIME_LITERAL(self):
            return self.getToken(OParser.TIME_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterTimeLiteral"):
                listener.enterTimeLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTimeLiteral"):
                listener.exitTimeLiteral(self)


    class CharacterLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a OParser.Atomic_literalContext)
            super(OParser.CharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(OParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCharacterLiteral"):
                listener.enterCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCharacterLiteral"):
                listener.exitCharacterLiteral(self)



    def atomic_literal(self):

        localctx = OParser.Atomic_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_atomic_literal)
        try:
            self.state = 1806
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.MIN_INTEGER]:
                localctx = OParser.MinIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1791
                localctx.t = self.match(OParser.MIN_INTEGER)
                pass
            elif token in [OParser.MAX_INTEGER]:
                localctx = OParser.MaxIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1792
                localctx.t = self.match(OParser.MAX_INTEGER)
                pass
            elif token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.IntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1793
                localctx.t = self.match(OParser.INTEGER_LITERAL)
                pass
            elif token in [OParser.HEXA_LITERAL]:
                localctx = OParser.HexadecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1794
                localctx.t = self.match(OParser.HEXA_LITERAL)
                pass
            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.CharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1795
                localctx.t = self.match(OParser.CHAR_LITERAL)
                pass
            elif token in [OParser.DATE_LITERAL]:
                localctx = OParser.DateLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1796
                localctx.t = self.match(OParser.DATE_LITERAL)
                pass
            elif token in [OParser.TIME_LITERAL]:
                localctx = OParser.TimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1797
                localctx.t = self.match(OParser.TIME_LITERAL)
                pass
            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.TextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1798
                localctx.t = self.match(OParser.TEXT_LITERAL)
                pass
            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.DecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1799
                localctx.t = self.match(OParser.DECIMAL_LITERAL)
                pass
            elif token in [OParser.DATETIME_LITERAL]:
                localctx = OParser.DateTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1800
                localctx.t = self.match(OParser.DATETIME_LITERAL)
                pass
            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.BooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1801
                localctx.t = self.match(OParser.BOOLEAN_LITERAL)
                pass
            elif token in [OParser.PERIOD_LITERAL]:
                localctx = OParser.PeriodLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1802
                localctx.t = self.match(OParser.PERIOD_LITERAL)
                pass
            elif token in [OParser.VERSION_LITERAL]:
                localctx = OParser.VersionLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1803
                localctx.t = self.match(OParser.VERSION_LITERAL)
                pass
            elif token in [OParser.UUID_LITERAL]:
                localctx = OParser.UUIDLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1804
                localctx.t = self.match(OParser.UUID_LITERAL)
                pass
            elif token in [OParser.NULL]:
                localctx = OParser.NullLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 1805
                localctx.n = self.null_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_list_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Literal_list_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def atomic_literal(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Atomic_literalContext)
            else:
                return self.getTypedRuleContext(OParser.Atomic_literalContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(OParser.COMMA)
            else:
                return self.getToken(OParser.COMMA, i)

        def getRuleIndex(self):
            return OParser.RULE_literal_list_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterLiteral_list_literal"):
                listener.enterLiteral_list_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteral_list_literal"):
                listener.exitLiteral_list_literal(self)




    def literal_list_literal(self):

        localctx = OParser.Literal_list_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_literal_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1808
            self.atomic_literal()
            self.state = 1813
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1809
                self.match(OParser.COMMA)
                self.state = 1810
                self.atomic_literal()
                self.state = 1815
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Selectable_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Selectable_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_selectable_expression

     
        def copyFrom(self, ctx):
            super(OParser.Selectable_expressionContext, self).copyFrom(ctx)



    class ThisExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Selectable_expressionContext)
            super(OParser.ThisExpressionContext, self).__init__(parser)
            self.exp = None # This_expressionContext
            self.copyFrom(ctx)

        def this_expression(self):
            return self.getTypedRuleContext(OParser.This_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterThisExpression"):
                listener.enterThisExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitThisExpression"):
                listener.exitThisExpression(self)


    class ParenthesisExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Selectable_expressionContext)
            super(OParser.ParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Parenthesis_expressionContext
            self.copyFrom(ctx)

        def parenthesis_expression(self):
            return self.getTypedRuleContext(OParser.Parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterParenthesisExpression"):
                listener.enterParenthesisExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitParenthesisExpression"):
                listener.exitParenthesisExpression(self)


    class LiteralExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Selectable_expressionContext)
            super(OParser.LiteralExpressionContext, self).__init__(parser)
            self.exp = None # Literal_expressionContext
            self.copyFrom(ctx)

        def literal_expression(self):
            return self.getTypedRuleContext(OParser.Literal_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterLiteralExpression"):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteralExpression"):
                listener.exitLiteralExpression(self)


    class IdentifierExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Selectable_expressionContext)
            super(OParser.IdentifierExpressionContext, self).__init__(parser)
            self.exp = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(OParser.IdentifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIdentifierExpression"):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIdentifierExpression"):
                listener.exitIdentifierExpression(self)



    def selectable_expression(self):

        localctx = OParser.Selectable_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_selectable_expression)
        try:
            self.state = 1820
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,149,self._ctx)
            if la_ == 1:
                localctx = OParser.ParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1816
                localctx.exp = self.parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = OParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1817
                localctx.exp = self.literal_expression()
                pass

            elif la_ == 3:
                localctx = OParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1818
                localctx.exp = self.identifier()
                pass

            elif la_ == 4:
                localctx = OParser.ThisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1819
                localctx.exp = self.this_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class This_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.This_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SELF(self):
            return self.getToken(OParser.SELF, 0)

        def THIS(self):
            return self.getToken(OParser.THIS, 0)

        def getRuleIndex(self):
            return OParser.RULE_this_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterThis_expression"):
                listener.enterThis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitThis_expression"):
                listener.exitThis_expression(self)




    def this_expression(self):

        localctx = OParser.This_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_this_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1822
            _la = self._input.LA(1)
            if not(_la==OParser.SELF or _la==OParser.THIS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def getRuleIndex(self):
            return OParser.RULE_parenthesis_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterParenthesis_expression"):
                listener.enterParenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitParenthesis_expression"):
                listener.exitParenthesis_expression(self)




    def parenthesis_expression(self):

        localctx = OParser.Parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 252, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1824
            self.match(OParser.LPAR)
            self.state = 1825
            self.expression(0)
            self.state = 1826
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def atomic_literal(self):
            return self.getTypedRuleContext(OParser.Atomic_literalContext,0)


        def collection_literal(self):
            return self.getTypedRuleContext(OParser.Collection_literalContext,0)


        def getRuleIndex(self):
            return OParser.RULE_literal_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterLiteral_expression"):
                listener.enterLiteral_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteral_expression"):
                listener.exitLiteral_expression(self)




    def literal_expression(self):

        localctx = OParser.Literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 254, self.RULE_literal_expression)
        try:
            self.state = 1830
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.NULL, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.MIN_INTEGER, OParser.MAX_INTEGER, OParser.TEXT_LITERAL, OParser.UUID_LITERAL, OParser.INTEGER_LITERAL, OParser.HEXA_LITERAL, OParser.DECIMAL_LITERAL, OParser.DATETIME_LITERAL, OParser.TIME_LITERAL, OParser.DATE_LITERAL, OParser.PERIOD_LITERAL, OParser.VERSION_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1828
                self.atomic_literal()
                pass
            elif token in [OParser.LPAR, OParser.LBRAK, OParser.LCURL, OParser.LT, OParser.MUTABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1829
                self.collection_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Collection_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Collection_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def range_literal(self):
            return self.getTypedRuleContext(OParser.Range_literalContext,0)


        def list_literal(self):
            return self.getTypedRuleContext(OParser.List_literalContext,0)


        def set_literal(self):
            return self.getTypedRuleContext(OParser.Set_literalContext,0)


        def dict_literal(self):
            return self.getTypedRuleContext(OParser.Dict_literalContext,0)


        def tuple_literal(self):
            return self.getTypedRuleContext(OParser.Tuple_literalContext,0)


        def getRuleIndex(self):
            return OParser.RULE_collection_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterCollection_literal"):
                listener.enterCollection_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCollection_literal"):
                listener.exitCollection_literal(self)




    def collection_literal(self):

        localctx = OParser.Collection_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_collection_literal)
        try:
            self.state = 1837
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,151,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1832
                self.range_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1833
                self.list_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1834
                self.set_literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1835
                self.dict_literal()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1836
                self.tuple_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Tuple_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Tuple_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def MUTABLE(self):
            return self.getToken(OParser.MUTABLE, 0)

        def expression_tuple(self):
            return self.getTypedRuleContext(OParser.Expression_tupleContext,0)


        def getRuleIndex(self):
            return OParser.RULE_tuple_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterTuple_literal"):
                listener.enterTuple_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTuple_literal"):
                listener.exitTuple_literal(self)




    def tuple_literal(self):

        localctx = OParser.Tuple_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_tuple_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1840
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.MUTABLE:
                self.state = 1839
                self.match(OParser.MUTABLE)


            self.state = 1842
            self.match(OParser.LPAR)
            self.state = 1844
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.LTGT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (OParser.EXECUTE - 95)) | (1 << (OParser.FETCH - 95)) | (1 << (OParser.FILTERED - 95)) | (1 << (OParser.MUTABLE - 95)) | (1 << (OParser.NULL - 95)) | (1 << (OParser.READ - 95)) | (1 << (OParser.SELF - 95)) | (1 << (OParser.SORTED - 95)) | (1 << (OParser.THIS - 95)) | (1 << (OParser.BOOLEAN_LITERAL - 95)) | (1 << (OParser.CHAR_LITERAL - 95)) | (1 << (OParser.MIN_INTEGER - 95)) | (1 << (OParser.MAX_INTEGER - 95)) | (1 << (OParser.SYMBOL_IDENTIFIER - 95)))) != 0) or ((((_la - 159)) & ~0x3f) == 0 and ((1 << (_la - 159)) & ((1 << (OParser.TYPE_IDENTIFIER - 159)) | (1 << (OParser.VARIABLE_IDENTIFIER - 159)) | (1 << (OParser.TEXT_LITERAL - 159)) | (1 << (OParser.UUID_LITERAL - 159)) | (1 << (OParser.INTEGER_LITERAL - 159)) | (1 << (OParser.HEXA_LITERAL - 159)) | (1 << (OParser.DECIMAL_LITERAL - 159)) | (1 << (OParser.DATETIME_LITERAL - 159)) | (1 << (OParser.TIME_LITERAL - 159)) | (1 << (OParser.DATE_LITERAL - 159)) | (1 << (OParser.PERIOD_LITERAL - 159)) | (1 << (OParser.VERSION_LITERAL - 159)))) != 0):
                self.state = 1843
                self.expression_tuple()


            self.state = 1846
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dict_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Dict_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)

        def MUTABLE(self):
            return self.getToken(OParser.MUTABLE, 0)

        def dict_entry_list(self):
            return self.getTypedRuleContext(OParser.Dict_entry_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_dict_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterDict_literal"):
                listener.enterDict_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDict_literal"):
                listener.exitDict_literal(self)




    def dict_literal(self):

        localctx = OParser.Dict_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_dict_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1849
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.MUTABLE:
                self.state = 1848
                self.match(OParser.MUTABLE)


            self.state = 1851
            self.match(OParser.LCURL)
            self.state = 1853
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.LTGT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (OParser.EXECUTE - 95)) | (1 << (OParser.FETCH - 95)) | (1 << (OParser.FILTERED - 95)) | (1 << (OParser.MUTABLE - 95)) | (1 << (OParser.NULL - 95)) | (1 << (OParser.READ - 95)) | (1 << (OParser.SELF - 95)) | (1 << (OParser.SORTED - 95)) | (1 << (OParser.THIS - 95)) | (1 << (OParser.BOOLEAN_LITERAL - 95)) | (1 << (OParser.CHAR_LITERAL - 95)) | (1 << (OParser.MIN_INTEGER - 95)) | (1 << (OParser.MAX_INTEGER - 95)) | (1 << (OParser.SYMBOL_IDENTIFIER - 95)))) != 0) or ((((_la - 159)) & ~0x3f) == 0 and ((1 << (_la - 159)) & ((1 << (OParser.TYPE_IDENTIFIER - 159)) | (1 << (OParser.VARIABLE_IDENTIFIER - 159)) | (1 << (OParser.TEXT_LITERAL - 159)) | (1 << (OParser.UUID_LITERAL - 159)) | (1 << (OParser.INTEGER_LITERAL - 159)) | (1 << (OParser.HEXA_LITERAL - 159)) | (1 << (OParser.DECIMAL_LITERAL - 159)) | (1 << (OParser.DATETIME_LITERAL - 159)) | (1 << (OParser.TIME_LITERAL - 159)) | (1 << (OParser.DATE_LITERAL - 159)) | (1 << (OParser.PERIOD_LITERAL - 159)) | (1 << (OParser.VERSION_LITERAL - 159)))) != 0):
                self.state = 1852
                self.dict_entry_list()


            self.state = 1855
            self.match(OParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_tupleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Expression_tupleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(OParser.COMMA)
            else:
                return self.getToken(OParser.COMMA, i)

        def getRuleIndex(self):
            return OParser.RULE_expression_tuple

        def enterRule(self, listener):
            if hasattr(listener, "enterExpression_tuple"):
                listener.enterExpression_tuple(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExpression_tuple"):
                listener.exitExpression_tuple(self)




    def expression_tuple(self):

        localctx = OParser.Expression_tupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 262, self.RULE_expression_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1857
            self.expression(0)
            self.state = 1858
            self.match(OParser.COMMA)
            self.state = 1867
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.LTGT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (OParser.EXECUTE - 95)) | (1 << (OParser.FETCH - 95)) | (1 << (OParser.FILTERED - 95)) | (1 << (OParser.MUTABLE - 95)) | (1 << (OParser.NULL - 95)) | (1 << (OParser.READ - 95)) | (1 << (OParser.SELF - 95)) | (1 << (OParser.SORTED - 95)) | (1 << (OParser.THIS - 95)) | (1 << (OParser.BOOLEAN_LITERAL - 95)) | (1 << (OParser.CHAR_LITERAL - 95)) | (1 << (OParser.MIN_INTEGER - 95)) | (1 << (OParser.MAX_INTEGER - 95)) | (1 << (OParser.SYMBOL_IDENTIFIER - 95)))) != 0) or ((((_la - 159)) & ~0x3f) == 0 and ((1 << (_la - 159)) & ((1 << (OParser.TYPE_IDENTIFIER - 159)) | (1 << (OParser.VARIABLE_IDENTIFIER - 159)) | (1 << (OParser.TEXT_LITERAL - 159)) | (1 << (OParser.UUID_LITERAL - 159)) | (1 << (OParser.INTEGER_LITERAL - 159)) | (1 << (OParser.HEXA_LITERAL - 159)) | (1 << (OParser.DECIMAL_LITERAL - 159)) | (1 << (OParser.DATETIME_LITERAL - 159)) | (1 << (OParser.TIME_LITERAL - 159)) | (1 << (OParser.DATE_LITERAL - 159)) | (1 << (OParser.PERIOD_LITERAL - 159)) | (1 << (OParser.VERSION_LITERAL - 159)))) != 0):
                self.state = 1859
                self.expression(0)
                self.state = 1864
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==OParser.COMMA:
                    self.state = 1860
                    self.match(OParser.COMMA)
                    self.state = 1861
                    self.expression(0)
                    self.state = 1866
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dict_entry_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Dict_entry_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def dict_entry(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Dict_entryContext)
            else:
                return self.getTypedRuleContext(OParser.Dict_entryContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(OParser.COMMA)
            else:
                return self.getToken(OParser.COMMA, i)

        def getRuleIndex(self):
            return OParser.RULE_dict_entry_list

        def enterRule(self, listener):
            if hasattr(listener, "enterDict_entry_list"):
                listener.enterDict_entry_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDict_entry_list"):
                listener.exitDict_entry_list(self)




    def dict_entry_list(self):

        localctx = OParser.Dict_entry_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_dict_entry_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1869
            self.dict_entry()
            self.state = 1874
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1870
                self.match(OParser.COMMA)
                self.state = 1871
                self.dict_entry()
                self.state = 1876
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dict_entryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Dict_entryContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.key = None # ExpressionContext
            self.value = None # ExpressionContext

        def COLON(self):
            return self.getToken(OParser.COLON, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def getRuleIndex(self):
            return OParser.RULE_dict_entry

        def enterRule(self, listener):
            if hasattr(listener, "enterDict_entry"):
                listener.enterDict_entry(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDict_entry"):
                listener.exitDict_entry(self)




    def dict_entry(self):

        localctx = OParser.Dict_entryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_dict_entry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1877
            localctx.key = self.expression(0)
            self.state = 1878
            self.match(OParser.COLON)
            self.state = 1879
            localctx.value = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Slice_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Slice_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_slice_arguments

     
        def copyFrom(self, ctx):
            super(OParser.Slice_argumentsContext, self).copyFrom(ctx)



    class SliceFirstAndLastContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a OParser.Slice_argumentsContext)
            super(OParser.SliceFirstAndLastContext, self).__init__(parser)
            self.first = None # ExpressionContext
            self.last = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(OParser.COLON, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterSliceFirstAndLast"):
                listener.enterSliceFirstAndLast(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSliceFirstAndLast"):
                listener.exitSliceFirstAndLast(self)


    class SliceLastOnlyContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a OParser.Slice_argumentsContext)
            super(OParser.SliceLastOnlyContext, self).__init__(parser)
            self.last = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(OParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSliceLastOnly"):
                listener.enterSliceLastOnly(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSliceLastOnly"):
                listener.exitSliceLastOnly(self)


    class SliceFirstOnlyContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a OParser.Slice_argumentsContext)
            super(OParser.SliceFirstOnlyContext, self).__init__(parser)
            self.first = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(OParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSliceFirstOnly"):
                listener.enterSliceFirstOnly(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSliceFirstOnly"):
                listener.exitSliceFirstOnly(self)



    def slice_arguments(self):

        localctx = OParser.Slice_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_slice_arguments)
        try:
            self.state = 1890
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,159,self._ctx)
            if la_ == 1:
                localctx = OParser.SliceFirstAndLastContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1881
                localctx.first = self.expression(0)
                self.state = 1882
                self.match(OParser.COLON)
                self.state = 1883
                localctx.last = self.expression(0)
                pass

            elif la_ == 2:
                localctx = OParser.SliceFirstOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1885
                localctx.first = self.expression(0)
                self.state = 1886
                self.match(OParser.COLON)
                pass

            elif la_ == 3:
                localctx = OParser.SliceLastOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1888
                self.match(OParser.COLON)
                self.state = 1889
                localctx.last = self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_variable_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Assign_variable_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def assign(self):
            return self.getTypedRuleContext(OParser.AssignContext,0)


        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_assign_variable_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterAssign_variable_statement"):
                listener.enterAssign_variable_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign_variable_statement"):
                listener.exitAssign_variable_statement(self)




    def assign_variable_statement(self):

        localctx = OParser.Assign_variable_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_assign_variable_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1892
            self.variable_identifier()
            self.state = 1893
            self.assign()
            self.state = 1894
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assignable_instanceContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Assignable_instanceContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_assignable_instance

     
        def copyFrom(self, ctx):
            super(OParser.Assignable_instanceContext, self).copyFrom(ctx)


    class ChildInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a OParser.Assignable_instanceContext)
            super(OParser.ChildInstanceContext, self).__init__(parser)
            self.copyFrom(ctx)

        def assignable_instance(self):
            return self.getTypedRuleContext(OParser.Assignable_instanceContext,0)

        def child_instance(self):
            return self.getTypedRuleContext(OParser.Child_instanceContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterChildInstance"):
                listener.enterChildInstance(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitChildInstance"):
                listener.exitChildInstance(self)


    class RootInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a OParser.Assignable_instanceContext)
            super(OParser.RootInstanceContext, self).__init__(parser)
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterRootInstance"):
                listener.enterRootInstance(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRootInstance"):
                listener.exitRootInstance(self)



    def assignable_instance(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Assignable_instanceContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 272
        self.enterRecursionRule(localctx, 272, self.RULE_assignable_instance, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.RootInstanceContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1897
            self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1903
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,160,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.ChildInstanceContext(self, OParser.Assignable_instanceContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignable_instance)
                    self.state = 1899
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1900
                    self.child_instance() 
                self.state = 1905
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,160,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Is_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Is_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_is_expression

     
        def copyFrom(self, ctx):
            super(OParser.Is_expressionContext, self).copyFrom(ctx)



    class IsATypeExpressionContext(Is_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Is_expressionContext)
            super(OParser.IsATypeExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)
        def category_or_any_type(self):
            return self.getTypedRuleContext(OParser.Category_or_any_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIsATypeExpression"):
                listener.enterIsATypeExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsATypeExpression"):
                listener.exitIsATypeExpression(self)


    class IsOtherExpressionContext(Is_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Is_expressionContext)
            super(OParser.IsOtherExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIsOtherExpression"):
                listener.enterIsOtherExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsOtherExpression"):
                listener.exitIsOtherExpression(self)



    def is_expression(self):

        localctx = OParser.Is_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 274, self.RULE_is_expression)
        try:
            self.state = 1910
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,161,self._ctx)
            if la_ == 1:
                localctx = OParser.IsATypeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1906
                if not self.willBeAOrAn():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willBeAOrAn()")
                self.state = 1907
                self.match(OParser.VARIABLE_IDENTIFIER)
                self.state = 1908
                self.category_or_any_type()
                pass

            elif la_ == 2:
                localctx = OParser.IsOtherExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1909
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Read_all_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Read_all_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # ExpressionContext

        def READ(self):
            return self.getToken(OParser.READ, 0)

        def ALL(self):
            return self.getToken(OParser.ALL, 0)

        def FROM(self):
            return self.getToken(OParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_read_all_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterRead_all_expression"):
                listener.enterRead_all_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRead_all_expression"):
                listener.exitRead_all_expression(self)




    def read_all_expression(self):

        localctx = OParser.Read_all_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_read_all_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1912
            self.match(OParser.READ)
            self.state = 1913
            self.match(OParser.ALL)
            self.state = 1914
            self.match(OParser.FROM)
            self.state = 1915
            localctx.source = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Read_one_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Read_one_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # ExpressionContext

        def READ(self):
            return self.getToken(OParser.READ, 0)

        def ONE(self):
            return self.getToken(OParser.ONE, 0)

        def FROM(self):
            return self.getToken(OParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_read_one_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterRead_one_expression"):
                listener.enterRead_one_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRead_one_expression"):
                listener.exitRead_one_expression(self)




    def read_one_expression(self):

        localctx = OParser.Read_one_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 278, self.RULE_read_one_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1917
            self.match(OParser.READ)
            self.state = 1918
            self.match(OParser.ONE)
            self.state = 1919
            self.match(OParser.FROM)
            self.state = 1920
            localctx.source = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Order_by_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Order_by_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def order_by(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Order_byContext)
            else:
                return self.getTypedRuleContext(OParser.Order_byContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(OParser.COMMA)
            else:
                return self.getToken(OParser.COMMA, i)

        def getRuleIndex(self):
            return OParser.RULE_order_by_list

        def enterRule(self, listener):
            if hasattr(listener, "enterOrder_by_list"):
                listener.enterOrder_by_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOrder_by_list"):
                listener.exitOrder_by_list(self)




    def order_by_list(self):

        localctx = OParser.Order_by_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_order_by_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1922
            self.order_by()
            self.state = 1927
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1923
                self.match(OParser.COMMA)
                self.state = 1924
                self.order_by()
                self.state = 1929
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Order_byContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Order_byContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(OParser.Variable_identifierContext,i)


        def DOT(self, i=None):
            if i is None:
                return self.getTokens(OParser.DOT)
            else:
                return self.getToken(OParser.DOT, i)

        def ASC(self):
            return self.getToken(OParser.ASC, 0)

        def DESC(self):
            return self.getToken(OParser.DESC, 0)

        def getRuleIndex(self):
            return OParser.RULE_order_by

        def enterRule(self, listener):
            if hasattr(listener, "enterOrder_by"):
                listener.enterOrder_by(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOrder_by"):
                listener.exitOrder_by(self)




    def order_by(self):

        localctx = OParser.Order_byContext(self, self._ctx, self.state)
        self.enterRule(localctx, 282, self.RULE_order_by)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1930
            self.variable_identifier()
            self.state = 1935
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.DOT:
                self.state = 1931
                self.match(OParser.DOT)
                self.state = 1932
                self.variable_identifier()
                self.state = 1937
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1939
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.ASC or _la==OParser.DESC:
                self.state = 1938
                _la = self._input.LA(1)
                if not(_la==OParser.ASC or _la==OParser.DESC):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.OperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_operator

     
        def copyFrom(self, ctx):
            super(OParser.OperatorContext, self).copyFrom(ctx)



    class OperatorPlusContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a OParser.OperatorContext)
            super(OParser.OperatorPlusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PLUS(self):
            return self.getToken(OParser.PLUS, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorPlus"):
                listener.enterOperatorPlus(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorPlus"):
                listener.exitOperatorPlus(self)


    class OperatorDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a OParser.OperatorContext)
            super(OParser.OperatorDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def divide(self):
            return self.getTypedRuleContext(OParser.DivideContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorDivide"):
                listener.enterOperatorDivide(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorDivide"):
                listener.exitOperatorDivide(self)


    class OperatorIDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a OParser.OperatorContext)
            super(OParser.OperatorIDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def idivide(self):
            return self.getTypedRuleContext(OParser.IdivideContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorIDivide"):
                listener.enterOperatorIDivide(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorIDivide"):
                listener.exitOperatorIDivide(self)


    class OperatorMultiplyContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a OParser.OperatorContext)
            super(OParser.OperatorMultiplyContext, self).__init__(parser)
            self.copyFrom(ctx)

        def multiply(self):
            return self.getTypedRuleContext(OParser.MultiplyContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorMultiply"):
                listener.enterOperatorMultiply(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorMultiply"):
                listener.exitOperatorMultiply(self)


    class OperatorMinusContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a OParser.OperatorContext)
            super(OParser.OperatorMinusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(OParser.MINUS, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorMinus"):
                listener.enterOperatorMinus(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorMinus"):
                listener.exitOperatorMinus(self)


    class OperatorModuloContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a OParser.OperatorContext)
            super(OParser.OperatorModuloContext, self).__init__(parser)
            self.copyFrom(ctx)

        def modulo(self):
            return self.getTypedRuleContext(OParser.ModuloContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorModulo"):
                listener.enterOperatorModulo(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorModulo"):
                listener.exitOperatorModulo(self)



    def operator(self):

        localctx = OParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_operator)
        try:
            self.state = 1947
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.PLUS]:
                localctx = OParser.OperatorPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1941
                self.match(OParser.PLUS)
                pass
            elif token in [OParser.MINUS]:
                localctx = OParser.OperatorMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1942
                self.match(OParser.MINUS)
                pass
            elif token in [OParser.STAR]:
                localctx = OParser.OperatorMultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1943
                self.multiply()
                pass
            elif token in [OParser.SLASH]:
                localctx = OParser.OperatorDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1944
                self.divide()
                pass
            elif token in [OParser.BSLASH]:
                localctx = OParser.OperatorIDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1945
                self.idivide()
                pass
            elif token in [OParser.PERCENT, OParser.MODULO]:
                localctx = OParser.OperatorModuloContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1946
                self.modulo()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class KeywordContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.KeywordContext, self).__init__(parent, invokingState)
            self.parser = parser

        def JAVA(self):
            return self.getToken(OParser.JAVA, 0)

        def CSHARP(self):
            return self.getToken(OParser.CSHARP, 0)

        def PYTHON2(self):
            return self.getToken(OParser.PYTHON2, 0)

        def PYTHON3(self):
            return self.getToken(OParser.PYTHON3, 0)

        def JAVASCRIPT(self):
            return self.getToken(OParser.JAVASCRIPT, 0)

        def SWIFT(self):
            return self.getToken(OParser.SWIFT, 0)

        def BOOLEAN(self):
            return self.getToken(OParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(OParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(OParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(OParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(OParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(OParser.DATE, 0)

        def TIME(self):
            return self.getToken(OParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(OParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(OParser.PERIOD, 0)

        def VERSION(self):
            return self.getToken(OParser.VERSION, 0)

        def METHOD_T(self):
            return self.getToken(OParser.METHOD_T, 0)

        def CODE(self):
            return self.getToken(OParser.CODE, 0)

        def DOCUMENT(self):
            return self.getToken(OParser.DOCUMENT, 0)

        def BLOB(self):
            return self.getToken(OParser.BLOB, 0)

        def IMAGE(self):
            return self.getToken(OParser.IMAGE, 0)

        def UUID(self):
            return self.getToken(OParser.UUID, 0)

        def ITERATOR(self):
            return self.getToken(OParser.ITERATOR, 0)

        def CURSOR(self):
            return self.getToken(OParser.CURSOR, 0)

        def ABSTRACT(self):
            return self.getToken(OParser.ABSTRACT, 0)

        def ALL(self):
            return self.getToken(OParser.ALL, 0)

        def ALWAYS(self):
            return self.getToken(OParser.ALWAYS, 0)

        def AND(self):
            return self.getToken(OParser.AND, 0)

        def ANY(self):
            return self.getToken(OParser.ANY, 0)

        def AS(self):
            return self.getToken(OParser.AS, 0)

        def ASC(self):
            return self.getToken(OParser.ASC, 0)

        def ATTR(self):
            return self.getToken(OParser.ATTR, 0)

        def ATTRIBUTE(self):
            return self.getToken(OParser.ATTRIBUTE, 0)

        def ATTRIBUTES(self):
            return self.getToken(OParser.ATTRIBUTES, 0)

        def BINDINGS(self):
            return self.getToken(OParser.BINDINGS, 0)

        def BREAK(self):
            return self.getToken(OParser.BREAK, 0)

        def BY(self):
            return self.getToken(OParser.BY, 0)

        def CASE(self):
            return self.getToken(OParser.CASE, 0)

        def CATCH(self):
            return self.getToken(OParser.CATCH, 0)

        def CATEGORY(self):
            return self.getToken(OParser.CATEGORY, 0)

        def CLASS(self):
            return self.getToken(OParser.CLASS, 0)

        def CLOSE(self):
            return self.getToken(OParser.CLOSE, 0)

        def CONTAINS(self):
            return self.getToken(OParser.CONTAINS, 0)

        def DEF(self):
            return self.getToken(OParser.DEF, 0)

        def DEFAULT(self):
            return self.getToken(OParser.DEFAULT, 0)

        def DEFINE(self):
            return self.getToken(OParser.DEFINE, 0)

        def DELETE(self):
            return self.getToken(OParser.DELETE, 0)

        def DESC(self):
            return self.getToken(OParser.DESC, 0)

        def DO(self):
            return self.getToken(OParser.DO, 0)

        def DOING(self):
            return self.getToken(OParser.DOING, 0)

        def EACH(self):
            return self.getToken(OParser.EACH, 0)

        def ELSE(self):
            return self.getToken(OParser.ELSE, 0)

        def ENUM(self):
            return self.getToken(OParser.ENUM, 0)

        def ENUMERATED(self):
            return self.getToken(OParser.ENUMERATED, 0)

        def EXCEPT(self):
            return self.getToken(OParser.EXCEPT, 0)

        def EXECUTE(self):
            return self.getToken(OParser.EXECUTE, 0)

        def EXPECTING(self):
            return self.getToken(OParser.EXPECTING, 0)

        def EXTENDS(self):
            return self.getToken(OParser.EXTENDS, 0)

        def FETCH(self):
            return self.getToken(OParser.FETCH, 0)

        def FILTERED(self):
            return self.getToken(OParser.FILTERED, 0)

        def FINALLY(self):
            return self.getToken(OParser.FINALLY, 0)

        def FLUSH(self):
            return self.getToken(OParser.FLUSH, 0)

        def FOR(self):
            return self.getToken(OParser.FOR, 0)

        def FROM(self):
            return self.getToken(OParser.FROM, 0)

        def GETTER(self):
            return self.getToken(OParser.GETTER, 0)

        def HAS(self):
            return self.getToken(OParser.HAS, 0)

        def IF(self):
            return self.getToken(OParser.IF, 0)

        def IN(self):
            return self.getToken(OParser.IN, 0)

        def INDEX(self):
            return self.getToken(OParser.INDEX, 0)

        def INVOKE(self):
            return self.getToken(OParser.INVOKE, 0)

        def IS(self):
            return self.getToken(OParser.IS, 0)

        def MATCHING(self):
            return self.getToken(OParser.MATCHING, 0)

        def METHOD(self):
            return self.getToken(OParser.METHOD, 0)

        def METHODS(self):
            return self.getToken(OParser.METHODS, 0)

        def MODULO(self):
            return self.getToken(OParser.MODULO, 0)

        def MUTABLE(self):
            return self.getToken(OParser.MUTABLE, 0)

        def NATIVE(self):
            return self.getToken(OParser.NATIVE, 0)

        def NONE(self):
            return self.getToken(OParser.NONE, 0)

        def NOT(self):
            return self.getToken(OParser.NOT, 0)

        def NOTHING(self):
            return self.getToken(OParser.NOTHING, 0)

        def NULL(self):
            return self.getToken(OParser.NULL, 0)

        def ON(self):
            return self.getToken(OParser.ON, 0)

        def ONE(self):
            return self.getToken(OParser.ONE, 0)

        def OPEN(self):
            return self.getToken(OParser.OPEN, 0)

        def OPERATOR(self):
            return self.getToken(OParser.OPERATOR, 0)

        def OR(self):
            return self.getToken(OParser.OR, 0)

        def ORDER(self):
            return self.getToken(OParser.ORDER, 0)

        def OTHERWISE(self):
            return self.getToken(OParser.OTHERWISE, 0)

        def PASS(self):
            return self.getToken(OParser.PASS, 0)

        def RAISE(self):
            return self.getToken(OParser.RAISE, 0)

        def READ(self):
            return self.getToken(OParser.READ, 0)

        def RECEIVING(self):
            return self.getToken(OParser.RECEIVING, 0)

        def RESOURCE(self):
            return self.getToken(OParser.RESOURCE, 0)

        def RETURN(self):
            return self.getToken(OParser.RETURN, 0)

        def RETURNING(self):
            return self.getToken(OParser.RETURNING, 0)

        def ROWS(self):
            return self.getToken(OParser.ROWS, 0)

        def SELF(self):
            return self.getToken(OParser.SELF, 0)

        def SETTER(self):
            return self.getToken(OParser.SETTER, 0)

        def SINGLETON(self):
            return self.getToken(OParser.SINGLETON, 0)

        def SORTED(self):
            return self.getToken(OParser.SORTED, 0)

        def STORABLE(self):
            return self.getToken(OParser.STORABLE, 0)

        def STORE(self):
            return self.getToken(OParser.STORE, 0)

        def SWITCH(self):
            return self.getToken(OParser.SWITCH, 0)

        def TEST(self):
            return self.getToken(OParser.TEST, 0)

        def THIS(self):
            return self.getToken(OParser.THIS, 0)

        def THROW(self):
            return self.getToken(OParser.THROW, 0)

        def TO(self):
            return self.getToken(OParser.TO, 0)

        def TRY(self):
            return self.getToken(OParser.TRY, 0)

        def VERIFYING(self):
            return self.getToken(OParser.VERIFYING, 0)

        def WITH(self):
            return self.getToken(OParser.WITH, 0)

        def WHEN(self):
            return self.getToken(OParser.WHEN, 0)

        def WHERE(self):
            return self.getToken(OParser.WHERE, 0)

        def WHILE(self):
            return self.getToken(OParser.WHILE, 0)

        def WRITE(self):
            return self.getToken(OParser.WRITE, 0)

        def getRuleIndex(self):
            return OParser.RULE_keyword

        def enterRule(self, listener):
            if hasattr(listener, "enterKeyword"):
                listener.enterKeyword(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitKeyword"):
                listener.exitKeyword(self)




    def keyword(self):

        localctx = OParser.KeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 286, self.RULE_keyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1949
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.JAVA) | (1 << OParser.CSHARP) | (1 << OParser.PYTHON2) | (1 << OParser.PYTHON3) | (1 << OParser.JAVASCRIPT) | (1 << OParser.SWIFT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.METHOD_T) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.ABSTRACT - 64)) | (1 << (OParser.ALL - 64)) | (1 << (OParser.ALWAYS - 64)) | (1 << (OParser.AND - 64)) | (1 << (OParser.ANY - 64)) | (1 << (OParser.AS - 64)) | (1 << (OParser.ASC - 64)) | (1 << (OParser.ATTR - 64)) | (1 << (OParser.ATTRIBUTE - 64)) | (1 << (OParser.ATTRIBUTES - 64)) | (1 << (OParser.BINDINGS - 64)) | (1 << (OParser.BREAK - 64)) | (1 << (OParser.BY - 64)) | (1 << (OParser.CASE - 64)) | (1 << (OParser.CATCH - 64)) | (1 << (OParser.CATEGORY - 64)) | (1 << (OParser.CLASS - 64)) | (1 << (OParser.CLOSE - 64)) | (1 << (OParser.CONTAINS - 64)) | (1 << (OParser.DEF - 64)) | (1 << (OParser.DEFAULT - 64)) | (1 << (OParser.DEFINE - 64)) | (1 << (OParser.DELETE - 64)) | (1 << (OParser.DESC - 64)) | (1 << (OParser.DO - 64)) | (1 << (OParser.DOING - 64)) | (1 << (OParser.EACH - 64)) | (1 << (OParser.ELSE - 64)) | (1 << (OParser.ENUM - 64)) | (1 << (OParser.ENUMERATED - 64)) | (1 << (OParser.EXCEPT - 64)) | (1 << (OParser.EXECUTE - 64)) | (1 << (OParser.EXPECTING - 64)) | (1 << (OParser.EXTENDS - 64)) | (1 << (OParser.FETCH - 64)) | (1 << (OParser.FILTERED - 64)) | (1 << (OParser.FINALLY - 64)) | (1 << (OParser.FLUSH - 64)) | (1 << (OParser.FOR - 64)) | (1 << (OParser.FROM - 64)) | (1 << (OParser.GETTER - 64)) | (1 << (OParser.HAS - 64)) | (1 << (OParser.IF - 64)) | (1 << (OParser.IN - 64)) | (1 << (OParser.INDEX - 64)) | (1 << (OParser.INVOKE - 64)) | (1 << (OParser.IS - 64)) | (1 << (OParser.MATCHING - 64)) | (1 << (OParser.METHOD - 64)) | (1 << (OParser.METHODS - 64)) | (1 << (OParser.MODULO - 64)) | (1 << (OParser.MUTABLE - 64)) | (1 << (OParser.NATIVE - 64)) | (1 << (OParser.NONE - 64)) | (1 << (OParser.NOT - 64)) | (1 << (OParser.NOTHING - 64)) | (1 << (OParser.NULL - 64)) | (1 << (OParser.ON - 64)) | (1 << (OParser.ONE - 64)) | (1 << (OParser.OPEN - 64)) | (1 << (OParser.OPERATOR - 64)) | (1 << (OParser.OR - 64)) | (1 << (OParser.ORDER - 64)) | (1 << (OParser.OTHERWISE - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (OParser.PASS - 128)) | (1 << (OParser.RAISE - 128)) | (1 << (OParser.READ - 128)) | (1 << (OParser.RECEIVING - 128)) | (1 << (OParser.RESOURCE - 128)) | (1 << (OParser.RETURN - 128)) | (1 << (OParser.RETURNING - 128)) | (1 << (OParser.ROWS - 128)) | (1 << (OParser.SELF - 128)) | (1 << (OParser.SETTER - 128)) | (1 << (OParser.SINGLETON - 128)) | (1 << (OParser.SORTED - 128)) | (1 << (OParser.STORABLE - 128)) | (1 << (OParser.STORE - 128)) | (1 << (OParser.SWITCH - 128)) | (1 << (OParser.TEST - 128)) | (1 << (OParser.THIS - 128)) | (1 << (OParser.THROW - 128)) | (1 << (OParser.TO - 128)) | (1 << (OParser.TRY - 128)) | (1 << (OParser.VERIFYING - 128)) | (1 << (OParser.WITH - 128)) | (1 << (OParser.WHEN - 128)) | (1 << (OParser.WHERE - 128)) | (1 << (OParser.WHILE - 128)) | (1 << (OParser.WRITE - 128)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class New_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.New_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_new_token

        def enterRule(self, listener):
            if hasattr(listener, "enterNew_token"):
                listener.enterNew_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNew_token"):
                listener.exitNew_token(self)




    def new_token(self):

        localctx = OParser.New_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 288, self.RULE_new_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1951
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1952
            if not self.isText(localctx.i1,"new"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.isText($i1,\"new\")")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Key_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Key_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_key_token

        def enterRule(self, listener):
            if hasattr(listener, "enterKey_token"):
                listener.enterKey_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitKey_token"):
                listener.exitKey_token(self)




    def key_token(self):

        localctx = OParser.Key_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_key_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1954
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1955
            if not self.isText(localctx.i1,"key"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.isText($i1,\"key\")")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Module_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Module_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_module_token

        def enterRule(self, listener):
            if hasattr(listener, "enterModule_token"):
                listener.enterModule_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitModule_token"):
                listener.exitModule_token(self)




    def module_token(self):

        localctx = OParser.Module_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 292, self.RULE_module_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1957
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1958
            if not self.isText(localctx.i1,"module"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.isText($i1,\"module\")")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Value_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Value_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_value_token

        def enterRule(self, listener):
            if hasattr(listener, "enterValue_token"):
                listener.enterValue_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitValue_token"):
                listener.exitValue_token(self)




    def value_token(self):

        localctx = OParser.Value_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_value_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1960
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1961
            if not self.isText(localctx.i1,"value"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.isText($i1,\"value\")")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Symbols_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Symbols_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return OParser.RULE_symbols_token

        def enterRule(self, listener):
            if hasattr(listener, "enterSymbols_token"):
                listener.enterSymbols_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSymbols_token"):
                listener.exitSymbols_token(self)




    def symbols_token(self):

        localctx = OParser.Symbols_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 296, self.RULE_symbols_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1963
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1964
            if not self.isText(localctx.i1,"symbols"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.isText($i1,\"symbols\")")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.AssignContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(OParser.EQ, 0)

        def getRuleIndex(self):
            return OParser.RULE_assign

        def enterRule(self, listener):
            if hasattr(listener, "enterAssign"):
                listener.enterAssign(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign"):
                listener.exitAssign(self)




    def assign(self):

        localctx = OParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1966
            self.match(OParser.EQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MultiplyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.MultiplyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(OParser.STAR, 0)

        def getRuleIndex(self):
            return OParser.RULE_multiply

        def enterRule(self, listener):
            if hasattr(listener, "enterMultiply"):
                listener.enterMultiply(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMultiply"):
                listener.exitMultiply(self)




    def multiply(self):

        localctx = OParser.MultiplyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 300, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1968
            self.match(OParser.STAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DivideContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.DivideContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self):
            return self.getToken(OParser.SLASH, 0)

        def getRuleIndex(self):
            return OParser.RULE_divide

        def enterRule(self, listener):
            if hasattr(listener, "enterDivide"):
                listener.enterDivide(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDivide"):
                listener.exitDivide(self)




    def divide(self):

        localctx = OParser.DivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_divide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1970
            self.match(OParser.SLASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdivideContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.IdivideContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BSLASH(self):
            return self.getToken(OParser.BSLASH, 0)

        def getRuleIndex(self):
            return OParser.RULE_idivide

        def enterRule(self, listener):
            if hasattr(listener, "enterIdivide"):
                listener.enterIdivide(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIdivide"):
                listener.exitIdivide(self)




    def idivide(self):

        localctx = OParser.IdivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_idivide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1972
            self.match(OParser.BSLASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModuloContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.ModuloContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PERCENT(self):
            return self.getToken(OParser.PERCENT, 0)

        def MODULO(self):
            return self.getToken(OParser.MODULO, 0)

        def getRuleIndex(self):
            return OParser.RULE_modulo

        def enterRule(self, listener):
            if hasattr(listener, "enterModulo"):
                listener.enterModulo(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitModulo"):
                listener.exitModulo(self)




    def modulo(self):

        localctx = OParser.ModuloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 306, self.RULE_modulo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1974
            _la = self._input.LA(1)
            if not(_la==OParser.PERCENT or _la==OParser.MODULO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LfsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.LfsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_lfs

        def enterRule(self, listener):
            if hasattr(listener, "enterLfs"):
                listener.enterLfs(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLfs"):
                listener.exitLfs(self)




    def lfs(self):

        localctx = OParser.LfsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 308, self.RULE_lfs)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LfpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.LfpContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_lfp

        def enterRule(self, listener):
            if hasattr(listener, "enterLfp"):
                listener.enterLfp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLfp"):
                listener.exitLfp(self)




    def lfp(self):

        localctx = OParser.LfpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 310, self.RULE_lfp)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_javascript_statement

     
        def copyFrom(self, ctx):
            super(OParser.Javascript_statementContext, self).copyFrom(ctx)



    class JavascriptStatementContext(Javascript_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_statementContext)
            super(OParser.JavascriptStatementContext, self).__init__(parser)
            self.exp = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)
        def javascript_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptStatement"):
                listener.enterJavascriptStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptStatement"):
                listener.exitJavascriptStatement(self)


    class JavascriptReturnStatementContext(Javascript_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_statementContext)
            super(OParser.JavascriptReturnStatementContext, self).__init__(parser)
            self.exp = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(OParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)
        def javascript_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptReturnStatement"):
                listener.enterJavascriptReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptReturnStatement"):
                listener.exitJavascriptReturnStatement(self)



    def javascript_statement(self):

        localctx = OParser.Javascript_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 312, self.RULE_javascript_statement)
        try:
            self.state = 1987
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.RETURN]:
                localctx = OParser.JavascriptReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1980
                self.match(OParser.RETURN)
                self.state = 1981
                localctx.exp = self.javascript_expression(0)
                self.state = 1982
                self.match(OParser.SEMI)
                pass
            elif token in [OParser.LPAR, OParser.LBRAK, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.UUID, OParser.NONE, OParser.NULL, OParser.READ, OParser.SELF, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER, OParser.TEXT_LITERAL, OParser.INTEGER_LITERAL, OParser.DECIMAL_LITERAL]:
                localctx = OParser.JavascriptStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1984
                localctx.exp = self.javascript_expression(0)
                self.state = 1985
                self.match(OParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_javascript_expression

     
        def copyFrom(self, ctx):
            super(OParser.Javascript_expressionContext, self).copyFrom(ctx)


    class JavascriptSelectorExpressionContext(Javascript_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_expressionContext)
            super(OParser.JavascriptSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Javascript_expressionContext
            self.child = None # Javascript_selector_expressionContext
            self.copyFrom(ctx)

        def javascript_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_expressionContext,0)

        def javascript_selector_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_selector_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptSelectorExpression"):
                listener.enterJavascriptSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptSelectorExpression"):
                listener.exitJavascriptSelectorExpression(self)


    class JavascriptPrimaryExpressionContext(Javascript_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_expressionContext)
            super(OParser.JavascriptPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_primary_expressionContext
            self.copyFrom(ctx)

        def javascript_primary_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_primary_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptPrimaryExpression"):
                listener.enterJavascriptPrimaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptPrimaryExpression"):
                listener.exitJavascriptPrimaryExpression(self)



    def javascript_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Javascript_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 314
        self.enterRecursionRule(localctx, 314, self.RULE_javascript_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavascriptPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1990
            localctx.exp = self.javascript_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1996
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,167,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavascriptSelectorExpressionContext(self, OParser.Javascript_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_expression)
                    self.state = 1992
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1993
                    localctx.child = self.javascript_selector_expression() 
                self.state = 1998
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,167,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Javascript_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def javascript_this_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_this_expressionContext,0)


        def javascript_new_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_new_expressionContext,0)


        def javascript_parenthesis_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_parenthesis_expressionContext,0)


        def javascript_identifier_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_identifier_expressionContext,0)


        def javascript_literal_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_literal_expressionContext,0)


        def javascript_method_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_method_expressionContext,0)


        def javascript_item_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_item_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_javascript_primary_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_primary_expression"):
                listener.enterJavascript_primary_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_primary_expression"):
                listener.exitJavascript_primary_expression(self)




    def javascript_primary_expression(self):

        localctx = OParser.Javascript_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 316, self.RULE_javascript_primary_expression)
        try:
            self.state = 2006
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,168,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1999
                self.javascript_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2000
                self.javascript_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2001
                self.javascript_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2002
                self.javascript_identifier_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2003
                self.javascript_literal_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2004
                self.javascript_method_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 2005
                self.javascript_item_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_this_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(OParser.This_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_javascript_this_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_this_expression"):
                listener.enterJavascript_this_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_this_expression"):
                listener.exitJavascript_this_expression(self)




    def javascript_this_expression(self):

        localctx = OParser.Javascript_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 318, self.RULE_javascript_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2008
            self.this_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_new_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(OParser.New_tokenContext,0)


        def javascript_method_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_method_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_javascript_new_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_new_expression"):
                listener.enterJavascript_new_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_new_expression"):
                listener.exitJavascript_new_expression(self)




    def javascript_new_expression(self):

        localctx = OParser.Javascript_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 320, self.RULE_javascript_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2010
            self.new_token()
            self.state = 2011
            self.javascript_method_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_selector_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_javascript_selector_expression

     
        def copyFrom(self, ctx):
            super(OParser.Javascript_selector_expressionContext, self).copyFrom(ctx)



    class JavaScriptMemberExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_selector_expressionContext)
            super(OParser.JavaScriptMemberExpressionContext, self).__init__(parser)
            self.name = None # Javascript_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def javascript_identifier(self):
            return self.getTypedRuleContext(OParser.Javascript_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaScriptMemberExpression"):
                listener.enterJavaScriptMemberExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptMemberExpression"):
                listener.exitJavaScriptMemberExpression(self)


    class JavaScriptItemExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_selector_expressionContext)
            super(OParser.JavaScriptItemExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_item_expressionContext
            self.copyFrom(ctx)

        def javascript_item_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_item_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaScriptItemExpression"):
                listener.enterJavaScriptItemExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptItemExpression"):
                listener.exitJavaScriptItemExpression(self)


    class JavaScriptMethodExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_selector_expressionContext)
            super(OParser.JavaScriptMethodExpressionContext, self).__init__(parser)
            self.method = None # Javascript_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def javascript_method_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaScriptMethodExpression"):
                listener.enterJavaScriptMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptMethodExpression"):
                listener.exitJavaScriptMethodExpression(self)



    def javascript_selector_expression(self):

        localctx = OParser.Javascript_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 322, self.RULE_javascript_selector_expression)
        try:
            self.state = 2018
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,169,self._ctx)
            if la_ == 1:
                localctx = OParser.JavaScriptMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2013
                self.match(OParser.DOT)
                self.state = 2014
                localctx.method = self.javascript_method_expression()
                pass

            elif la_ == 2:
                localctx = OParser.JavaScriptMemberExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2015
                self.match(OParser.DOT)
                self.state = 2016
                localctx.name = self.javascript_identifier()
                pass

            elif la_ == 3:
                localctx = OParser.JavaScriptItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2017
                localctx.exp = self.javascript_item_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_method_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Javascript_identifierContext
            self.args = None # Javascript_argumentsContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def javascript_identifier(self):
            return self.getTypedRuleContext(OParser.Javascript_identifierContext,0)


        def javascript_arguments(self):
            return self.getTypedRuleContext(OParser.Javascript_argumentsContext,0)


        def getRuleIndex(self):
            return OParser.RULE_javascript_method_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_method_expression"):
                listener.enterJavascript_method_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_method_expression"):
                listener.exitJavascript_method_expression(self)




    def javascript_method_expression(self):

        localctx = OParser.Javascript_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 324, self.RULE_javascript_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2020
            localctx.name = self.javascript_identifier()
            self.state = 2021
            self.match(OParser.LPAR)
            self.state = 2023
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.UUID))) != 0) or ((((_la - 117)) & ~0x3f) == 0 and ((1 << (_la - 117)) & ((1 << (OParser.NONE - 117)) | (1 << (OParser.NULL - 117)) | (1 << (OParser.READ - 117)) | (1 << (OParser.SELF - 117)) | (1 << (OParser.TEST - 117)) | (1 << (OParser.THIS - 117)) | (1 << (OParser.WRITE - 117)) | (1 << (OParser.BOOLEAN_LITERAL - 117)) | (1 << (OParser.CHAR_LITERAL - 117)) | (1 << (OParser.SYMBOL_IDENTIFIER - 117)) | (1 << (OParser.TYPE_IDENTIFIER - 117)) | (1 << (OParser.VARIABLE_IDENTIFIER - 117)) | (1 << (OParser.DOLLAR_IDENTIFIER - 117)) | (1 << (OParser.TEXT_LITERAL - 117)) | (1 << (OParser.INTEGER_LITERAL - 117)) | (1 << (OParser.DECIMAL_LITERAL - 117)))) != 0):
                self.state = 2022
                localctx.args = self.javascript_arguments(0)


            self.state = 2025
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_javascript_arguments

     
        def copyFrom(self, ctx):
            super(OParser.Javascript_argumentsContext, self).copyFrom(ctx)


    class JavascriptArgumentListContext(Javascript_argumentsContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_argumentsContext)
            super(OParser.JavascriptArgumentListContext, self).__init__(parser)
            self.item = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def javascript_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptArgumentList"):
                listener.enterJavascriptArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptArgumentList"):
                listener.exitJavascriptArgumentList(self)


    class JavascriptArgumentListItemContext(Javascript_argumentsContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_argumentsContext)
            super(OParser.JavascriptArgumentListItemContext, self).__init__(parser)
            self.items = None # Javascript_argumentsContext
            self.item = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def javascript_arguments(self):
            return self.getTypedRuleContext(OParser.Javascript_argumentsContext,0)

        def javascript_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptArgumentListItem"):
                listener.enterJavascriptArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptArgumentListItem"):
                listener.exitJavascriptArgumentListItem(self)



    def javascript_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Javascript_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 326
        self.enterRecursionRule(localctx, 326, self.RULE_javascript_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavascriptArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2028
            localctx.item = self.javascript_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2035
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,171,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavascriptArgumentListItemContext(self, OParser.Javascript_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_arguments)
                    self.state = 2030
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2031
                    self.match(OParser.COMMA)
                    self.state = 2032
                    localctx.item = self.javascript_expression(0) 
                self.state = 2037
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,171,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Javascript_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Javascript_expressionContext

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)

        def javascript_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_javascript_item_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_item_expression"):
                listener.enterJavascript_item_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_item_expression"):
                listener.exitJavascript_item_expression(self)




    def javascript_item_expression(self):

        localctx = OParser.Javascript_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 328, self.RULE_javascript_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2038
            self.match(OParser.LBRAK)
            self.state = 2039
            localctx.exp = self.javascript_expression(0)
            self.state = 2040
            self.match(OParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Javascript_expressionContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def javascript_expression(self):
            return self.getTypedRuleContext(OParser.Javascript_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_javascript_parenthesis_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_parenthesis_expression"):
                listener.enterJavascript_parenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_parenthesis_expression"):
                listener.exitJavascript_parenthesis_expression(self)




    def javascript_parenthesis_expression(self):

        localctx = OParser.Javascript_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 330, self.RULE_javascript_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2042
            self.match(OParser.LPAR)
            self.state = 2043
            localctx.exp = self.javascript_expression(0)
            self.state = 2044
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Javascript_identifierContext

        def javascript_identifier(self):
            return self.getTypedRuleContext(OParser.Javascript_identifierContext,0)


        def getRuleIndex(self):
            return OParser.RULE_javascript_identifier_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_identifier_expression"):
                listener.enterJavascript_identifier_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_identifier_expression"):
                listener.exitJavascript_identifier_expression(self)




    def javascript_identifier_expression(self):

        localctx = OParser.Javascript_identifier_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 332, self.RULE_javascript_identifier_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2046
            localctx.name = self.javascript_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_javascript_literal_expression

     
        def copyFrom(self, ctx):
            super(OParser.Javascript_literal_expressionContext, self).copyFrom(ctx)



    class JavascriptIntegerLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_literal_expressionContext)
            super(OParser.JavascriptIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(OParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptIntegerLiteral"):
                listener.enterJavascriptIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptIntegerLiteral"):
                listener.exitJavascriptIntegerLiteral(self)


    class JavascriptBooleanLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_literal_expressionContext)
            super(OParser.JavascriptBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(OParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptBooleanLiteral"):
                listener.enterJavascriptBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptBooleanLiteral"):
                listener.exitJavascriptBooleanLiteral(self)


    class JavascriptCharacterLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_literal_expressionContext)
            super(OParser.JavascriptCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(OParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptCharacterLiteral"):
                listener.enterJavascriptCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptCharacterLiteral"):
                listener.exitJavascriptCharacterLiteral(self)


    class JavascriptTextLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_literal_expressionContext)
            super(OParser.JavascriptTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(OParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptTextLiteral"):
                listener.enterJavascriptTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptTextLiteral"):
                listener.exitJavascriptTextLiteral(self)


    class JavascriptDecimalLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Javascript_literal_expressionContext)
            super(OParser.JavascriptDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(OParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptDecimalLiteral"):
                listener.enterJavascriptDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptDecimalLiteral"):
                listener.exitJavascriptDecimalLiteral(self)



    def javascript_literal_expression(self):

        localctx = OParser.Javascript_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 334, self.RULE_javascript_literal_expression)
        try:
            self.state = 2053
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.JavascriptIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2048
                localctx.t = self.match(OParser.INTEGER_LITERAL)
                pass
            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.JavascriptDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2049
                localctx.t = self.match(OParser.DECIMAL_LITERAL)
                pass
            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.JavascriptTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2050
                localctx.t = self.match(OParser.TEXT_LITERAL)
                pass
            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.JavascriptBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2051
                localctx.t = self.match(OParser.BOOLEAN_LITERAL)
                pass
            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.JavascriptCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2052
                localctx.t = self.match(OParser.CHAR_LITERAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Javascript_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(OParser.SYMBOL_IDENTIFIER, 0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(OParser.DOLLAR_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(OParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(OParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(OParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(OParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(OParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(OParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(OParser.DATE, 0)

        def TIME(self):
            return self.getToken(OParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(OParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(OParser.PERIOD, 0)

        def VERSION(self):
            return self.getToken(OParser.VERSION, 0)

        def UUID(self):
            return self.getToken(OParser.UUID, 0)

        def READ(self):
            return self.getToken(OParser.READ, 0)

        def WRITE(self):
            return self.getToken(OParser.WRITE, 0)

        def TEST(self):
            return self.getToken(OParser.TEST, 0)

        def SELF(self):
            return self.getToken(OParser.SELF, 0)

        def NONE(self):
            return self.getToken(OParser.NONE, 0)

        def NULL(self):
            return self.getToken(OParser.NULL, 0)

        def getRuleIndex(self):
            return OParser.RULE_javascript_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_identifier"):
                listener.enterJavascript_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_identifier"):
                listener.exitJavascript_identifier(self)




    def javascript_identifier(self):

        localctx = OParser.Javascript_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 336, self.RULE_javascript_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2055
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.UUID))) != 0) or ((((_la - 117)) & ~0x3f) == 0 and ((1 << (_la - 117)) & ((1 << (OParser.NONE - 117)) | (1 << (OParser.NULL - 117)) | (1 << (OParser.READ - 117)) | (1 << (OParser.SELF - 117)) | (1 << (OParser.TEST - 117)) | (1 << (OParser.WRITE - 117)) | (1 << (OParser.SYMBOL_IDENTIFIER - 117)) | (1 << (OParser.TYPE_IDENTIFIER - 117)) | (1 << (OParser.VARIABLE_IDENTIFIER - 117)) | (1 << (OParser.DOLLAR_IDENTIFIER - 117)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_python_statement

     
        def copyFrom(self, ctx):
            super(OParser.Python_statementContext, self).copyFrom(ctx)



    class PythonStatementContext(Python_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_statementContext)
            super(OParser.PythonStatementContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(OParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonStatement"):
                listener.enterPythonStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonStatement"):
                listener.exitPythonStatement(self)


    class PythonReturnStatementContext(Python_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_statementContext)
            super(OParser.PythonReturnStatementContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(OParser.RETURN, 0)
        def python_expression(self):
            return self.getTypedRuleContext(OParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonReturnStatement"):
                listener.enterPythonReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonReturnStatement"):
                listener.exitPythonReturnStatement(self)



    def python_statement(self):

        localctx = OParser.Python_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 338, self.RULE_python_statement)
        try:
            self.state = 2060
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.RETURN]:
                localctx = OParser.PythonReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2057
                self.match(OParser.RETURN)
                self.state = 2058
                localctx.exp = self.python_expression(0)
                pass
            elif token in [OParser.LPAR, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.UUID, OParser.NONE, OParser.NULL, OParser.READ, OParser.SELF, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER, OParser.TEXT_LITERAL, OParser.INTEGER_LITERAL, OParser.DECIMAL_LITERAL]:
                localctx = OParser.PythonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2059
                localctx.exp = self.python_expression(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_python_expression

     
        def copyFrom(self, ctx):
            super(OParser.Python_expressionContext, self).copyFrom(ctx)


    class PythonSelectorExpressionContext(Python_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_expressionContext)
            super(OParser.PythonSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Python_expressionContext
            self.child = None # Python_selector_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(OParser.Python_expressionContext,0)

        def python_selector_expression(self):
            return self.getTypedRuleContext(OParser.Python_selector_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonSelectorExpression"):
                listener.enterPythonSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonSelectorExpression"):
                listener.exitPythonSelectorExpression(self)


    class PythonPrimaryExpressionContext(Python_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_expressionContext)
            super(OParser.PythonPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Python_primary_expressionContext
            self.copyFrom(ctx)

        def python_primary_expression(self):
            return self.getTypedRuleContext(OParser.Python_primary_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonPrimaryExpression"):
                listener.enterPythonPrimaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonPrimaryExpression"):
                listener.exitPythonPrimaryExpression(self)



    def python_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Python_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 340
        self.enterRecursionRule(localctx, 340, self.RULE_python_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.PythonPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2063
            localctx.exp = self.python_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2069
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,174,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.PythonSelectorExpressionContext(self, OParser.Python_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_expression)
                    self.state = 2065
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2066
                    localctx.child = self.python_selector_expression() 
                self.state = 2071
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,174,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_python_primary_expression

     
        def copyFrom(self, ctx):
            super(OParser.Python_primary_expressionContext, self).copyFrom(ctx)



    class PythonParenthesisExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_primary_expressionContext)
            super(OParser.PythonParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Python_parenthesis_expressionContext
            self.copyFrom(ctx)

        def python_parenthesis_expression(self):
            return self.getTypedRuleContext(OParser.Python_parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonParenthesisExpression"):
                listener.enterPythonParenthesisExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonParenthesisExpression"):
                listener.exitPythonParenthesisExpression(self)


    class PythonIdentifierExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_primary_expressionContext)
            super(OParser.PythonIdentifierExpressionContext, self).__init__(parser)
            self.exp = None # Python_identifier_expressionContext
            self.copyFrom(ctx)

        def python_identifier_expression(self):
            return self.getTypedRuleContext(OParser.Python_identifier_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonIdentifierExpression"):
                listener.enterPythonIdentifierExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonIdentifierExpression"):
                listener.exitPythonIdentifierExpression(self)


    class PythonSelfExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_primary_expressionContext)
            super(OParser.PythonSelfExpressionContext, self).__init__(parser)
            self.exp = None # Python_self_expressionContext
            self.copyFrom(ctx)

        def python_self_expression(self):
            return self.getTypedRuleContext(OParser.Python_self_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonSelfExpression"):
                listener.enterPythonSelfExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonSelfExpression"):
                listener.exitPythonSelfExpression(self)


    class PythonLiteralExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_primary_expressionContext)
            super(OParser.PythonLiteralExpressionContext, self).__init__(parser)
            self.exp = None # Python_literal_expressionContext
            self.copyFrom(ctx)

        def python_literal_expression(self):
            return self.getTypedRuleContext(OParser.Python_literal_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonLiteralExpression"):
                listener.enterPythonLiteralExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonLiteralExpression"):
                listener.exitPythonLiteralExpression(self)


    class PythonGlobalMethodExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_primary_expressionContext)
            super(OParser.PythonGlobalMethodExpressionContext, self).__init__(parser)
            self.exp = None # Python_method_expressionContext
            self.copyFrom(ctx)

        def python_method_expression(self):
            return self.getTypedRuleContext(OParser.Python_method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonGlobalMethodExpression"):
                listener.enterPythonGlobalMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonGlobalMethodExpression"):
                listener.exitPythonGlobalMethodExpression(self)



    def python_primary_expression(self):

        localctx = OParser.Python_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 342, self.RULE_python_primary_expression)
        try:
            self.state = 2077
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,175,self._ctx)
            if la_ == 1:
                localctx = OParser.PythonSelfExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2072
                localctx.exp = self.python_self_expression()
                pass

            elif la_ == 2:
                localctx = OParser.PythonParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2073
                localctx.exp = self.python_parenthesis_expression()
                pass

            elif la_ == 3:
                localctx = OParser.PythonIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2074
                localctx.exp = self.python_identifier_expression(0)
                pass

            elif la_ == 4:
                localctx = OParser.PythonLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2075
                localctx.exp = self.python_literal_expression()
                pass

            elif la_ == 5:
                localctx = OParser.PythonGlobalMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2076
                localctx.exp = self.python_method_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_self_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_self_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(OParser.This_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_python_self_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_self_expression"):
                listener.enterPython_self_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_self_expression"):
                listener.exitPython_self_expression(self)




    def python_self_expression(self):

        localctx = OParser.Python_self_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 344, self.RULE_python_self_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2079
            self.this_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_selector_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_python_selector_expression

     
        def copyFrom(self, ctx):
            super(OParser.Python_selector_expressionContext, self).copyFrom(ctx)



    class PythonMethodExpressionContext(Python_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_selector_expressionContext)
            super(OParser.PythonMethodExpressionContext, self).__init__(parser)
            self.exp = None # Python_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def python_method_expression(self):
            return self.getTypedRuleContext(OParser.Python_method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonMethodExpression"):
                listener.enterPythonMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonMethodExpression"):
                listener.exitPythonMethodExpression(self)


    class PythonItemExpressionContext(Python_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_selector_expressionContext)
            super(OParser.PythonItemExpressionContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)
        def python_expression(self):
            return self.getTypedRuleContext(OParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonItemExpression"):
                listener.enterPythonItemExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonItemExpression"):
                listener.exitPythonItemExpression(self)



    def python_selector_expression(self):

        localctx = OParser.Python_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 346, self.RULE_python_selector_expression)
        try:
            self.state = 2087
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.PythonMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2081
                self.match(OParser.DOT)
                self.state = 2082
                localctx.exp = self.python_method_expression()
                pass
            elif token in [OParser.LBRAK]:
                localctx = OParser.PythonItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2083
                self.match(OParser.LBRAK)
                self.state = 2084
                localctx.exp = self.python_expression(0)
                self.state = 2085
                self.match(OParser.RBRAK)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_method_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Python_identifierContext
            self.args = None # Python_argument_listContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def python_identifier(self):
            return self.getTypedRuleContext(OParser.Python_identifierContext,0)


        def python_argument_list(self):
            return self.getTypedRuleContext(OParser.Python_argument_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_python_method_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_method_expression"):
                listener.enterPython_method_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_method_expression"):
                listener.exitPython_method_expression(self)




    def python_method_expression(self):

        localctx = OParser.Python_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 348, self.RULE_python_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2089
            localctx.name = self.python_identifier()
            self.state = 2090
            self.match(OParser.LPAR)
            self.state = 2092
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.UUID))) != 0) or ((((_la - 117)) & ~0x3f) == 0 and ((1 << (_la - 117)) & ((1 << (OParser.NONE - 117)) | (1 << (OParser.NULL - 117)) | (1 << (OParser.READ - 117)) | (1 << (OParser.SELF - 117)) | (1 << (OParser.TEST - 117)) | (1 << (OParser.THIS - 117)) | (1 << (OParser.WRITE - 117)) | (1 << (OParser.BOOLEAN_LITERAL - 117)) | (1 << (OParser.CHAR_LITERAL - 117)) | (1 << (OParser.SYMBOL_IDENTIFIER - 117)) | (1 << (OParser.TYPE_IDENTIFIER - 117)) | (1 << (OParser.VARIABLE_IDENTIFIER - 117)) | (1 << (OParser.DOLLAR_IDENTIFIER - 117)) | (1 << (OParser.TEXT_LITERAL - 117)) | (1 << (OParser.INTEGER_LITERAL - 117)) | (1 << (OParser.DECIMAL_LITERAL - 117)))) != 0):
                self.state = 2091
                localctx.args = self.python_argument_list()


            self.state = 2094
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_python_argument_list

     
        def copyFrom(self, ctx):
            super(OParser.Python_argument_listContext, self).copyFrom(ctx)



    class PythonOrdinalOnlyArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_argument_listContext)
            super(OParser.PythonOrdinalOnlyArgumentListContext, self).__init__(parser)
            self.ordinal = None # Python_ordinal_argument_listContext
            self.copyFrom(ctx)

        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(OParser.Python_ordinal_argument_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonOrdinalOnlyArgumentList"):
                listener.enterPythonOrdinalOnlyArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonOrdinalOnlyArgumentList"):
                listener.exitPythonOrdinalOnlyArgumentList(self)


    class PythonNamedOnlyArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_argument_listContext)
            super(OParser.PythonNamedOnlyArgumentListContext, self).__init__(parser)
            self.named = None # Python_named_argument_listContext
            self.copyFrom(ctx)

        def python_named_argument_list(self):
            return self.getTypedRuleContext(OParser.Python_named_argument_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonNamedOnlyArgumentList"):
                listener.enterPythonNamedOnlyArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonNamedOnlyArgumentList"):
                listener.exitPythonNamedOnlyArgumentList(self)


    class PythonArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_argument_listContext)
            super(OParser.PythonArgumentListContext, self).__init__(parser)
            self.ordinal = None # Python_ordinal_argument_listContext
            self.named = None # Python_named_argument_listContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(OParser.Python_ordinal_argument_listContext,0)

        def python_named_argument_list(self):
            return self.getTypedRuleContext(OParser.Python_named_argument_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonArgumentList"):
                listener.enterPythonArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonArgumentList"):
                listener.exitPythonArgumentList(self)



    def python_argument_list(self):

        localctx = OParser.Python_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 350, self.RULE_python_argument_list)
        try:
            self.state = 2102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,178,self._ctx)
            if la_ == 1:
                localctx = OParser.PythonOrdinalOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2096
                localctx.ordinal = self.python_ordinal_argument_list(0)
                pass

            elif la_ == 2:
                localctx = OParser.PythonNamedOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2097
                localctx.named = self.python_named_argument_list(0)
                pass

            elif la_ == 3:
                localctx = OParser.PythonArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2098
                localctx.ordinal = self.python_ordinal_argument_list(0)
                self.state = 2099
                self.match(OParser.COMMA)
                self.state = 2100
                localctx.named = self.python_named_argument_list(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_ordinal_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_ordinal_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_python_ordinal_argument_list

     
        def copyFrom(self, ctx):
            super(OParser.Python_ordinal_argument_listContext, self).copyFrom(ctx)


    class PythonOrdinalArgumentListContext(Python_ordinal_argument_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_ordinal_argument_listContext)
            super(OParser.PythonOrdinalArgumentListContext, self).__init__(parser)
            self.item = None # Python_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(OParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonOrdinalArgumentList"):
                listener.enterPythonOrdinalArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonOrdinalArgumentList"):
                listener.exitPythonOrdinalArgumentList(self)


    class PythonOrdinalArgumentListItemContext(Python_ordinal_argument_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_ordinal_argument_listContext)
            super(OParser.PythonOrdinalArgumentListItemContext, self).__init__(parser)
            self.items = None # Python_ordinal_argument_listContext
            self.item = None # Python_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(OParser.Python_ordinal_argument_listContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(OParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonOrdinalArgumentListItem"):
                listener.enterPythonOrdinalArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonOrdinalArgumentListItem"):
                listener.exitPythonOrdinalArgumentListItem(self)



    def python_ordinal_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Python_ordinal_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 352
        self.enterRecursionRule(localctx, 352, self.RULE_python_ordinal_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.PythonOrdinalArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2105
            localctx.item = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2112
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,179,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.PythonOrdinalArgumentListItemContext(self, OParser.Python_ordinal_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_ordinal_argument_list)
                    self.state = 2107
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2108
                    self.match(OParser.COMMA)
                    self.state = 2109
                    localctx.item = self.python_expression(0) 
                self.state = 2114
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,179,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_named_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_named_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_python_named_argument_list

     
        def copyFrom(self, ctx):
            super(OParser.Python_named_argument_listContext, self).copyFrom(ctx)


    class PythonNamedArgumentListContext(Python_named_argument_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_named_argument_listContext)
            super(OParser.PythonNamedArgumentListContext, self).__init__(parser)
            self.name = None # Python_identifierContext
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def EQ(self):
            return self.getToken(OParser.EQ, 0)
        def python_identifier(self):
            return self.getTypedRuleContext(OParser.Python_identifierContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(OParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonNamedArgumentList"):
                listener.enterPythonNamedArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonNamedArgumentList"):
                listener.exitPythonNamedArgumentList(self)


    class PythonNamedArgumentListItemContext(Python_named_argument_listContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_named_argument_listContext)
            super(OParser.PythonNamedArgumentListItemContext, self).__init__(parser)
            self.items = None # Python_named_argument_listContext
            self.name = None # Python_identifierContext
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def EQ(self):
            return self.getToken(OParser.EQ, 0)
        def python_named_argument_list(self):
            return self.getTypedRuleContext(OParser.Python_named_argument_listContext,0)

        def python_identifier(self):
            return self.getTypedRuleContext(OParser.Python_identifierContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(OParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonNamedArgumentListItem"):
                listener.enterPythonNamedArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonNamedArgumentListItem"):
                listener.exitPythonNamedArgumentListItem(self)



    def python_named_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Python_named_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 354
        self.enterRecursionRule(localctx, 354, self.RULE_python_named_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.PythonNamedArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2116
            localctx.name = self.python_identifier()
            self.state = 2117
            self.match(OParser.EQ)
            self.state = 2118
            localctx.exp = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2128
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,180,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.PythonNamedArgumentListItemContext(self, OParser.Python_named_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_named_argument_list)
                    self.state = 2120
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2121
                    self.match(OParser.COMMA)
                    self.state = 2122
                    localctx.name = self.python_identifier()
                    self.state = 2123
                    self.match(OParser.EQ)
                    self.state = 2124
                    localctx.exp = self.python_expression(0) 
                self.state = 2130
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,180,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Python_expressionContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def python_expression(self):
            return self.getTypedRuleContext(OParser.Python_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_python_parenthesis_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_parenthesis_expression"):
                listener.enterPython_parenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_parenthesis_expression"):
                listener.exitPython_parenthesis_expression(self)




    def python_parenthesis_expression(self):

        localctx = OParser.Python_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 356, self.RULE_python_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2131
            self.match(OParser.LPAR)
            self.state = 2132
            localctx.exp = self.python_expression(0)
            self.state = 2133
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_python_identifier_expression

     
        def copyFrom(self, ctx):
            super(OParser.Python_identifier_expressionContext, self).copyFrom(ctx)


    class PythonChildIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_identifier_expressionContext)
            super(OParser.PythonChildIdentifierContext, self).__init__(parser)
            self.parent = None # Python_identifier_expressionContext
            self.name = None # Python_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def python_identifier_expression(self):
            return self.getTypedRuleContext(OParser.Python_identifier_expressionContext,0)

        def python_identifier(self):
            return self.getTypedRuleContext(OParser.Python_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonChildIdentifier"):
                listener.enterPythonChildIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonChildIdentifier"):
                listener.exitPythonChildIdentifier(self)


    class PythonPromptoIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_identifier_expressionContext)
            super(OParser.PythonPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(OParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonPromptoIdentifier"):
                listener.enterPythonPromptoIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonPromptoIdentifier"):
                listener.exitPythonPromptoIdentifier(self)


    class PythonIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_identifier_expressionContext)
            super(OParser.PythonIdentifierContext, self).__init__(parser)
            self.name = None # Python_identifierContext
            self.copyFrom(ctx)

        def python_identifier(self):
            return self.getTypedRuleContext(OParser.Python_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonIdentifier"):
                listener.enterPythonIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonIdentifier"):
                listener.exitPythonIdentifier(self)



    def python_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Python_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 358
        self.enterRecursionRule(localctx, 358, self.RULE_python_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.DOLLAR_IDENTIFIER]:
                localctx = OParser.PythonPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2136
                self.match(OParser.DOLLAR_IDENTIFIER)
                pass
            elif token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.UUID, OParser.NONE, OParser.NULL, OParser.READ, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER]:
                localctx = OParser.PythonIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2137
                localctx.name = self.python_identifier()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,182,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.PythonChildIdentifierContext(self, OParser.Python_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_identifier_expression)
                    self.state = 2140
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2141
                    self.match(OParser.DOT)
                    self.state = 2142
                    localctx.name = self.python_identifier() 
                self.state = 2147
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,182,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_python_literal_expression

     
        def copyFrom(self, ctx):
            super(OParser.Python_literal_expressionContext, self).copyFrom(ctx)



    class PythonIntegerLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_literal_expressionContext)
            super(OParser.PythonIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(OParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonIntegerLiteral"):
                listener.enterPythonIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonIntegerLiteral"):
                listener.exitPythonIntegerLiteral(self)


    class PythonBooleanLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_literal_expressionContext)
            super(OParser.PythonBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(OParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonBooleanLiteral"):
                listener.enterPythonBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonBooleanLiteral"):
                listener.exitPythonBooleanLiteral(self)


    class PythonCharacterLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_literal_expressionContext)
            super(OParser.PythonCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(OParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonCharacterLiteral"):
                listener.enterPythonCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonCharacterLiteral"):
                listener.exitPythonCharacterLiteral(self)


    class PythonTextLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_literal_expressionContext)
            super(OParser.PythonTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(OParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonTextLiteral"):
                listener.enterPythonTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonTextLiteral"):
                listener.exitPythonTextLiteral(self)


    class PythonDecimalLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Python_literal_expressionContext)
            super(OParser.PythonDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(OParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonDecimalLiteral"):
                listener.enterPythonDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonDecimalLiteral"):
                listener.exitPythonDecimalLiteral(self)



    def python_literal_expression(self):

        localctx = OParser.Python_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 360, self.RULE_python_literal_expression)
        try:
            self.state = 2153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.PythonIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2148
                localctx.t = self.match(OParser.INTEGER_LITERAL)
                pass
            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.PythonDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2149
                localctx.t = self.match(OParser.DECIMAL_LITERAL)
                pass
            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.PythonTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2150
                localctx.t = self.match(OParser.TEXT_LITERAL)
                pass
            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.PythonBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2151
                localctx.t = self.match(OParser.BOOLEAN_LITERAL)
                pass
            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.PythonCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2152
                localctx.t = self.match(OParser.CHAR_LITERAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Python_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(OParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(OParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(OParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(OParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(OParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(OParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(OParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(OParser.DATE, 0)

        def TIME(self):
            return self.getToken(OParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(OParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(OParser.PERIOD, 0)

        def VERSION(self):
            return self.getToken(OParser.VERSION, 0)

        def UUID(self):
            return self.getToken(OParser.UUID, 0)

        def READ(self):
            return self.getToken(OParser.READ, 0)

        def WRITE(self):
            return self.getToken(OParser.WRITE, 0)

        def TEST(self):
            return self.getToken(OParser.TEST, 0)

        def THIS(self):
            return self.getToken(OParser.THIS, 0)

        def NONE(self):
            return self.getToken(OParser.NONE, 0)

        def NULL(self):
            return self.getToken(OParser.NULL, 0)

        def getRuleIndex(self):
            return OParser.RULE_python_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_identifier"):
                listener.enterPython_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_identifier"):
                listener.exitPython_identifier(self)




    def python_identifier(self):

        localctx = OParser.Python_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 362, self.RULE_python_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2155
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.UUID))) != 0) or ((((_la - 117)) & ~0x3f) == 0 and ((1 << (_la - 117)) & ((1 << (OParser.NONE - 117)) | (1 << (OParser.NULL - 117)) | (1 << (OParser.READ - 117)) | (1 << (OParser.TEST - 117)) | (1 << (OParser.THIS - 117)) | (1 << (OParser.WRITE - 117)) | (1 << (OParser.SYMBOL_IDENTIFIER - 117)) | (1 << (OParser.TYPE_IDENTIFIER - 117)) | (1 << (OParser.VARIABLE_IDENTIFIER - 117)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_java_statement

     
        def copyFrom(self, ctx):
            super(OParser.Java_statementContext, self).copyFrom(ctx)



    class JavaReturnStatementContext(Java_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_statementContext)
            super(OParser.JavaReturnStatementContext, self).__init__(parser)
            self.exp = None # Java_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(OParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)
        def java_expression(self):
            return self.getTypedRuleContext(OParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaReturnStatement"):
                listener.enterJavaReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaReturnStatement"):
                listener.exitJavaReturnStatement(self)


    class JavaStatementContext(Java_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_statementContext)
            super(OParser.JavaStatementContext, self).__init__(parser)
            self.exp = None # Java_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)
        def java_expression(self):
            return self.getTypedRuleContext(OParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaStatement"):
                listener.enterJavaStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaStatement"):
                listener.exitJavaStatement(self)



    def java_statement(self):

        localctx = OParser.Java_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 364, self.RULE_java_statement)
        try:
            self.state = 2164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.RETURN]:
                localctx = OParser.JavaReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2157
                self.match(OParser.RETURN)
                self.state = 2158
                localctx.exp = self.java_expression(0)
                self.state = 2159
                self.match(OParser.SEMI)
                pass
            elif token in [OParser.LPAR, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.UUID, OParser.NONE, OParser.NULL, OParser.READ, OParser.SELF, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.NATIVE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER, OParser.TEXT_LITERAL, OParser.INTEGER_LITERAL, OParser.DECIMAL_LITERAL]:
                localctx = OParser.JavaStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2161
                localctx.exp = self.java_expression(0)
                self.state = 2162
                self.match(OParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_java_expression

     
        def copyFrom(self, ctx):
            super(OParser.Java_expressionContext, self).copyFrom(ctx)


    class JavaSelectorExpressionContext(Java_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_expressionContext)
            super(OParser.JavaSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Java_expressionContext
            self.child = None # Java_selector_expressionContext
            self.copyFrom(ctx)

        def java_expression(self):
            return self.getTypedRuleContext(OParser.Java_expressionContext,0)

        def java_selector_expression(self):
            return self.getTypedRuleContext(OParser.Java_selector_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaSelectorExpression"):
                listener.enterJavaSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaSelectorExpression"):
                listener.exitJavaSelectorExpression(self)


    class JavaPrimaryExpressionContext(Java_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_expressionContext)
            super(OParser.JavaPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Java_primary_expressionContext
            self.copyFrom(ctx)

        def java_primary_expression(self):
            return self.getTypedRuleContext(OParser.Java_primary_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaPrimaryExpression"):
                listener.enterJavaPrimaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaPrimaryExpression"):
                listener.exitJavaPrimaryExpression(self)



    def java_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Java_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 366
        self.enterRecursionRule(localctx, 366, self.RULE_java_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavaPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2167
            localctx.exp = self.java_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2173
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,185,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavaSelectorExpressionContext(self, OParser.Java_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_expression)
                    self.state = 2169
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2170
                    localctx.child = self.java_selector_expression() 
                self.state = 2175
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,185,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def java_this_expression(self):
            return self.getTypedRuleContext(OParser.Java_this_expressionContext,0)


        def java_new_expression(self):
            return self.getTypedRuleContext(OParser.Java_new_expressionContext,0)


        def java_parenthesis_expression(self):
            return self.getTypedRuleContext(OParser.Java_parenthesis_expressionContext,0)


        def java_identifier_expression(self):
            return self.getTypedRuleContext(OParser.Java_identifier_expressionContext,0)


        def java_literal_expression(self):
            return self.getTypedRuleContext(OParser.Java_literal_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_java_primary_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_primary_expression"):
                listener.enterJava_primary_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_primary_expression"):
                listener.exitJava_primary_expression(self)




    def java_primary_expression(self):

        localctx = OParser.Java_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 368, self.RULE_java_primary_expression)
        try:
            self.state = 2181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,186,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2176
                self.java_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2177
                self.java_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2178
                self.java_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2179
                self.java_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2180
                self.java_literal_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_this_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(OParser.This_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_java_this_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_this_expression"):
                listener.enterJava_this_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_this_expression"):
                listener.exitJava_this_expression(self)




    def java_this_expression(self):

        localctx = OParser.Java_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 370, self.RULE_java_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2183
            self.this_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_new_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(OParser.New_tokenContext,0)


        def java_method_expression(self):
            return self.getTypedRuleContext(OParser.Java_method_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_java_new_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_new_expression"):
                listener.enterJava_new_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_new_expression"):
                listener.exitJava_new_expression(self)




    def java_new_expression(self):

        localctx = OParser.Java_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 372, self.RULE_java_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2185
            self.new_token()
            self.state = 2186
            self.java_method_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_selector_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_java_selector_expression

     
        def copyFrom(self, ctx):
            super(OParser.Java_selector_expressionContext, self).copyFrom(ctx)



    class JavaItemExpressionContext(Java_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_selector_expressionContext)
            super(OParser.JavaItemExpressionContext, self).__init__(parser)
            self.exp = None # Java_item_expressionContext
            self.copyFrom(ctx)

        def java_item_expression(self):
            return self.getTypedRuleContext(OParser.Java_item_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaItemExpression"):
                listener.enterJavaItemExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaItemExpression"):
                listener.exitJavaItemExpression(self)


    class JavaMethodExpressionContext(Java_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_selector_expressionContext)
            super(OParser.JavaMethodExpressionContext, self).__init__(parser)
            self.exp = None # Java_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def java_method_expression(self):
            return self.getTypedRuleContext(OParser.Java_method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaMethodExpression"):
                listener.enterJavaMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaMethodExpression"):
                listener.exitJavaMethodExpression(self)



    def java_selector_expression(self):

        localctx = OParser.Java_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 374, self.RULE_java_selector_expression)
        try:
            self.state = 2191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.JavaMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2188
                self.match(OParser.DOT)
                self.state = 2189
                localctx.exp = self.java_method_expression()
                pass
            elif token in [OParser.LBRAK]:
                localctx = OParser.JavaItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2190
                localctx.exp = self.java_item_expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_method_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Java_identifierContext
            self.args = None # Java_argumentsContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def java_identifier(self):
            return self.getTypedRuleContext(OParser.Java_identifierContext,0)


        def java_arguments(self):
            return self.getTypedRuleContext(OParser.Java_argumentsContext,0)


        def getRuleIndex(self):
            return OParser.RULE_java_method_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_method_expression"):
                listener.enterJava_method_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_method_expression"):
                listener.exitJava_method_expression(self)




    def java_method_expression(self):

        localctx = OParser.Java_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 376, self.RULE_java_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2193
            localctx.name = self.java_identifier()
            self.state = 2194
            self.match(OParser.LPAR)
            self.state = 2196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.UUID))) != 0) or ((((_la - 117)) & ~0x3f) == 0 and ((1 << (_la - 117)) & ((1 << (OParser.NONE - 117)) | (1 << (OParser.NULL - 117)) | (1 << (OParser.READ - 117)) | (1 << (OParser.SELF - 117)) | (1 << (OParser.TEST - 117)) | (1 << (OParser.THIS - 117)) | (1 << (OParser.WRITE - 117)) | (1 << (OParser.BOOLEAN_LITERAL - 117)) | (1 << (OParser.CHAR_LITERAL - 117)) | (1 << (OParser.SYMBOL_IDENTIFIER - 117)) | (1 << (OParser.TYPE_IDENTIFIER - 117)) | (1 << (OParser.VARIABLE_IDENTIFIER - 117)) | (1 << (OParser.NATIVE_IDENTIFIER - 117)) | (1 << (OParser.DOLLAR_IDENTIFIER - 117)) | (1 << (OParser.TEXT_LITERAL - 117)) | (1 << (OParser.INTEGER_LITERAL - 117)) | (1 << (OParser.DECIMAL_LITERAL - 117)))) != 0):
                self.state = 2195
                localctx.args = self.java_arguments(0)


            self.state = 2198
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_java_arguments

     
        def copyFrom(self, ctx):
            super(OParser.Java_argumentsContext, self).copyFrom(ctx)


    class JavaArgumentListItemContext(Java_argumentsContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_argumentsContext)
            super(OParser.JavaArgumentListItemContext, self).__init__(parser)
            self.items = None # Java_argumentsContext
            self.item = None # Java_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def java_arguments(self):
            return self.getTypedRuleContext(OParser.Java_argumentsContext,0)

        def java_expression(self):
            return self.getTypedRuleContext(OParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaArgumentListItem"):
                listener.enterJavaArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaArgumentListItem"):
                listener.exitJavaArgumentListItem(self)


    class JavaArgumentListContext(Java_argumentsContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_argumentsContext)
            super(OParser.JavaArgumentListContext, self).__init__(parser)
            self.item = None # Java_expressionContext
            self.copyFrom(ctx)

        def java_expression(self):
            return self.getTypedRuleContext(OParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaArgumentList"):
                listener.enterJavaArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaArgumentList"):
                listener.exitJavaArgumentList(self)



    def java_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Java_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 378
        self.enterRecursionRule(localctx, 378, self.RULE_java_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavaArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2201
            localctx.item = self.java_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2208
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,189,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavaArgumentListItemContext(self, OParser.Java_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_arguments)
                    self.state = 2203
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2204
                    self.match(OParser.COMMA)
                    self.state = 2205
                    localctx.item = self.java_expression(0) 
                self.state = 2210
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,189,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Java_expressionContext

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)

        def java_expression(self):
            return self.getTypedRuleContext(OParser.Java_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_java_item_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_item_expression"):
                listener.enterJava_item_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_item_expression"):
                listener.exitJava_item_expression(self)




    def java_item_expression(self):

        localctx = OParser.Java_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 380, self.RULE_java_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2211
            self.match(OParser.LBRAK)
            self.state = 2212
            localctx.exp = self.java_expression(0)
            self.state = 2213
            self.match(OParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Java_expressionContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def java_expression(self):
            return self.getTypedRuleContext(OParser.Java_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_java_parenthesis_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_parenthesis_expression"):
                listener.enterJava_parenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_parenthesis_expression"):
                listener.exitJava_parenthesis_expression(self)




    def java_parenthesis_expression(self):

        localctx = OParser.Java_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 382, self.RULE_java_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2215
            self.match(OParser.LPAR)
            self.state = 2216
            localctx.exp = self.java_expression(0)
            self.state = 2217
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_java_identifier_expression

     
        def copyFrom(self, ctx):
            super(OParser.Java_identifier_expressionContext, self).copyFrom(ctx)


    class JavaIdentifierContext(Java_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_identifier_expressionContext)
            super(OParser.JavaIdentifierContext, self).__init__(parser)
            self.name = None # Java_identifierContext
            self.copyFrom(ctx)

        def java_identifier(self):
            return self.getTypedRuleContext(OParser.Java_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaIdentifier"):
                listener.enterJavaIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaIdentifier"):
                listener.exitJavaIdentifier(self)


    class JavaChildIdentifierContext(Java_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_identifier_expressionContext)
            super(OParser.JavaChildIdentifierContext, self).__init__(parser)
            self.parent = None # Java_identifier_expressionContext
            self.name = None # Java_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def java_identifier_expression(self):
            return self.getTypedRuleContext(OParser.Java_identifier_expressionContext,0)

        def java_identifier(self):
            return self.getTypedRuleContext(OParser.Java_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaChildIdentifier"):
                listener.enterJavaChildIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaChildIdentifier"):
                listener.exitJavaChildIdentifier(self)



    def java_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Java_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 384
        self.enterRecursionRule(localctx, 384, self.RULE_java_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavaIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2220
            localctx.name = self.java_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2227
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,190,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavaChildIdentifierContext(self, OParser.Java_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_identifier_expression)
                    self.state = 2222
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2223
                    self.match(OParser.DOT)
                    self.state = 2224
                    localctx.name = self.java_identifier() 
                self.state = 2229
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,190,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_class_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_class_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_java_class_identifier_expression

     
        def copyFrom(self, ctx):
            super(OParser.Java_class_identifier_expressionContext, self).copyFrom(ctx)


    class JavaClassIdentifierContext(Java_class_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_class_identifier_expressionContext)
            super(OParser.JavaClassIdentifierContext, self).__init__(parser)
            self.klass = None # Java_identifier_expressionContext
            self.copyFrom(ctx)

        def java_identifier_expression(self):
            return self.getTypedRuleContext(OParser.Java_identifier_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaClassIdentifier"):
                listener.enterJavaClassIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaClassIdentifier"):
                listener.exitJavaClassIdentifier(self)


    class JavaChildClassIdentifierContext(Java_class_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_class_identifier_expressionContext)
            super(OParser.JavaChildClassIdentifierContext, self).__init__(parser)
            self.parent = None # Java_class_identifier_expressionContext
            self.name = None # Token
            self.copyFrom(ctx)

        def java_class_identifier_expression(self):
            return self.getTypedRuleContext(OParser.Java_class_identifier_expressionContext,0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(OParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaChildClassIdentifier"):
                listener.enterJavaChildClassIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaChildClassIdentifier"):
                listener.exitJavaChildClassIdentifier(self)



    def java_class_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Java_class_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 386
        self.enterRecursionRule(localctx, 386, self.RULE_java_class_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavaClassIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2231
            localctx.klass = self.java_identifier_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2237
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,191,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavaChildClassIdentifierContext(self, OParser.Java_class_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_class_identifier_expression)
                    self.state = 2233
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2234
                    localctx.name = self.match(OParser.DOLLAR_IDENTIFIER) 
                self.state = 2239
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,191,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_java_literal_expression

     
        def copyFrom(self, ctx):
            super(OParser.Java_literal_expressionContext, self).copyFrom(ctx)



    class JavaBooleanLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_literal_expressionContext)
            super(OParser.JavaBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(OParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaBooleanLiteral"):
                listener.enterJavaBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaBooleanLiteral"):
                listener.exitJavaBooleanLiteral(self)


    class JavaCharacterLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_literal_expressionContext)
            super(OParser.JavaCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(OParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaCharacterLiteral"):
                listener.enterJavaCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaCharacterLiteral"):
                listener.exitJavaCharacterLiteral(self)


    class JavaIntegerLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_literal_expressionContext)
            super(OParser.JavaIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(OParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaIntegerLiteral"):
                listener.enterJavaIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaIntegerLiteral"):
                listener.exitJavaIntegerLiteral(self)


    class JavaTextLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_literal_expressionContext)
            super(OParser.JavaTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(OParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaTextLiteral"):
                listener.enterJavaTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaTextLiteral"):
                listener.exitJavaTextLiteral(self)


    class JavaDecimalLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Java_literal_expressionContext)
            super(OParser.JavaDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(OParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaDecimalLiteral"):
                listener.enterJavaDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaDecimalLiteral"):
                listener.exitJavaDecimalLiteral(self)



    def java_literal_expression(self):

        localctx = OParser.Java_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 388, self.RULE_java_literal_expression)
        try:
            self.state = 2245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.JavaIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2240
                localctx.t = self.match(OParser.INTEGER_LITERAL)
                pass
            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.JavaDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2241
                localctx.t = self.match(OParser.DECIMAL_LITERAL)
                pass
            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.JavaTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2242
                localctx.t = self.match(OParser.TEXT_LITERAL)
                pass
            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.JavaBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2243
                localctx.t = self.match(OParser.BOOLEAN_LITERAL)
                pass
            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.JavaCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2244
                localctx.t = self.match(OParser.CHAR_LITERAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Java_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(OParser.SYMBOL_IDENTIFIER, 0)

        def NATIVE_IDENTIFIER(self):
            return self.getToken(OParser.NATIVE_IDENTIFIER, 0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(OParser.DOLLAR_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(OParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(OParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(OParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(OParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(OParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(OParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(OParser.DATE, 0)

        def TIME(self):
            return self.getToken(OParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(OParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(OParser.PERIOD, 0)

        def VERSION(self):
            return self.getToken(OParser.VERSION, 0)

        def UUID(self):
            return self.getToken(OParser.UUID, 0)

        def READ(self):
            return self.getToken(OParser.READ, 0)

        def WRITE(self):
            return self.getToken(OParser.WRITE, 0)

        def TEST(self):
            return self.getToken(OParser.TEST, 0)

        def SELF(self):
            return self.getToken(OParser.SELF, 0)

        def NONE(self):
            return self.getToken(OParser.NONE, 0)

        def NULL(self):
            return self.getToken(OParser.NULL, 0)

        def getRuleIndex(self):
            return OParser.RULE_java_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_identifier"):
                listener.enterJava_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_identifier"):
                listener.exitJava_identifier(self)




    def java_identifier(self):

        localctx = OParser.Java_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 390, self.RULE_java_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2247
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.UUID))) != 0) or ((((_la - 117)) & ~0x3f) == 0 and ((1 << (_la - 117)) & ((1 << (OParser.NONE - 117)) | (1 << (OParser.NULL - 117)) | (1 << (OParser.READ - 117)) | (1 << (OParser.SELF - 117)) | (1 << (OParser.TEST - 117)) | (1 << (OParser.WRITE - 117)) | (1 << (OParser.SYMBOL_IDENTIFIER - 117)) | (1 << (OParser.TYPE_IDENTIFIER - 117)) | (1 << (OParser.VARIABLE_IDENTIFIER - 117)) | (1 << (OParser.NATIVE_IDENTIFIER - 117)) | (1 << (OParser.DOLLAR_IDENTIFIER - 117)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_csharp_statement

     
        def copyFrom(self, ctx):
            super(OParser.Csharp_statementContext, self).copyFrom(ctx)



    class CSharpReturnStatementContext(Csharp_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_statementContext)
            super(OParser.CSharpReturnStatementContext, self).__init__(parser)
            self.exp = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(OParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)
        def csharp_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpReturnStatement"):
                listener.enterCSharpReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpReturnStatement"):
                listener.exitCSharpReturnStatement(self)


    class CSharpStatementContext(Csharp_statementContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_statementContext)
            super(OParser.CSharpStatementContext, self).__init__(parser)
            self.exp = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(OParser.SEMI, 0)
        def csharp_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpStatement"):
                listener.enterCSharpStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpStatement"):
                listener.exitCSharpStatement(self)



    def csharp_statement(self):

        localctx = OParser.Csharp_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 392, self.RULE_csharp_statement)
        try:
            self.state = 2256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.RETURN]:
                localctx = OParser.CSharpReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2249
                self.match(OParser.RETURN)
                self.state = 2250
                localctx.exp = self.csharp_expression(0)
                self.state = 2251
                self.match(OParser.SEMI)
                pass
            elif token in [OParser.LPAR, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.UUID, OParser.NONE, OParser.NULL, OParser.READ, OParser.SELF, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER, OParser.TEXT_LITERAL, OParser.INTEGER_LITERAL, OParser.DECIMAL_LITERAL]:
                localctx = OParser.CSharpStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2253
                localctx.exp = self.csharp_expression(0)
                self.state = 2254
                self.match(OParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_csharp_expression

     
        def copyFrom(self, ctx):
            super(OParser.Csharp_expressionContext, self).copyFrom(ctx)


    class CSharpSelectorExpressionContext(Csharp_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_expressionContext)
            super(OParser.CSharpSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Csharp_expressionContext
            self.child = None # Csharp_selector_expressionContext
            self.copyFrom(ctx)

        def csharp_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_expressionContext,0)

        def csharp_selector_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_selector_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpSelectorExpression"):
                listener.enterCSharpSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpSelectorExpression"):
                listener.exitCSharpSelectorExpression(self)


    class CSharpPrimaryExpressionContext(Csharp_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_expressionContext)
            super(OParser.CSharpPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_primary_expressionContext
            self.copyFrom(ctx)

        def csharp_primary_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_primary_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpPrimaryExpression"):
                listener.enterCSharpPrimaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpPrimaryExpression"):
                listener.exitCSharpPrimaryExpression(self)



    def csharp_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Csharp_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 394
        self.enterRecursionRule(localctx, 394, self.RULE_csharp_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.CSharpPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2259
            localctx.exp = self.csharp_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2265
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,194,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.CSharpSelectorExpressionContext(self, OParser.Csharp_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_expression)
                    self.state = 2261
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2262
                    localctx.child = self.csharp_selector_expression() 
                self.state = 2267
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,194,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def csharp_this_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_this_expressionContext,0)


        def csharp_new_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_new_expressionContext,0)


        def csharp_parenthesis_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_parenthesis_expressionContext,0)


        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_identifier_expressionContext,0)


        def csharp_literal_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_literal_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_csharp_primary_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_primary_expression"):
                listener.enterCsharp_primary_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_primary_expression"):
                listener.exitCsharp_primary_expression(self)




    def csharp_primary_expression(self):

        localctx = OParser.Csharp_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 396, self.RULE_csharp_primary_expression)
        try:
            self.state = 2273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,195,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2268
                self.csharp_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2269
                self.csharp_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2270
                self.csharp_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2271
                self.csharp_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2272
                self.csharp_literal_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_this_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(OParser.This_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_csharp_this_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_this_expression"):
                listener.enterCsharp_this_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_this_expression"):
                listener.exitCsharp_this_expression(self)




    def csharp_this_expression(self):

        localctx = OParser.Csharp_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 398, self.RULE_csharp_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2275
            self.this_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_new_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(OParser.New_tokenContext,0)


        def csharp_method_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_method_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_csharp_new_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_new_expression"):
                listener.enterCsharp_new_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_new_expression"):
                listener.exitCsharp_new_expression(self)




    def csharp_new_expression(self):

        localctx = OParser.Csharp_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 400, self.RULE_csharp_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2277
            self.new_token()
            self.state = 2278
            self.csharp_method_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_selector_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_csharp_selector_expression

     
        def copyFrom(self, ctx):
            super(OParser.Csharp_selector_expressionContext, self).copyFrom(ctx)



    class CSharpMethodExpressionContext(Csharp_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_selector_expressionContext)
            super(OParser.CSharpMethodExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def csharp_method_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpMethodExpression"):
                listener.enterCSharpMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpMethodExpression"):
                listener.exitCSharpMethodExpression(self)


    class CSharpItemExpressionContext(Csharp_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_selector_expressionContext)
            super(OParser.CSharpItemExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_item_expressionContext
            self.copyFrom(ctx)

        def csharp_item_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_item_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpItemExpression"):
                listener.enterCSharpItemExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpItemExpression"):
                listener.exitCSharpItemExpression(self)



    def csharp_selector_expression(self):

        localctx = OParser.Csharp_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 402, self.RULE_csharp_selector_expression)
        try:
            self.state = 2283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.CSharpMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2280
                self.match(OParser.DOT)
                self.state = 2281
                localctx.exp = self.csharp_method_expression()
                pass
            elif token in [OParser.LBRAK]:
                localctx = OParser.CSharpItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2282
                localctx.exp = self.csharp_item_expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_method_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Csharp_identifierContext
            self.args = None # Csharp_argumentsContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def csharp_identifier(self):
            return self.getTypedRuleContext(OParser.Csharp_identifierContext,0)


        def csharp_arguments(self):
            return self.getTypedRuleContext(OParser.Csharp_argumentsContext,0)


        def getRuleIndex(self):
            return OParser.RULE_csharp_method_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_method_expression"):
                listener.enterCsharp_method_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_method_expression"):
                listener.exitCsharp_method_expression(self)




    def csharp_method_expression(self):

        localctx = OParser.Csharp_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 404, self.RULE_csharp_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2285
            localctx.name = self.csharp_identifier()
            self.state = 2286
            self.match(OParser.LPAR)
            self.state = 2288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.UUID))) != 0) or ((((_la - 117)) & ~0x3f) == 0 and ((1 << (_la - 117)) & ((1 << (OParser.NONE - 117)) | (1 << (OParser.NULL - 117)) | (1 << (OParser.READ - 117)) | (1 << (OParser.SELF - 117)) | (1 << (OParser.TEST - 117)) | (1 << (OParser.THIS - 117)) | (1 << (OParser.WRITE - 117)) | (1 << (OParser.BOOLEAN_LITERAL - 117)) | (1 << (OParser.CHAR_LITERAL - 117)) | (1 << (OParser.SYMBOL_IDENTIFIER - 117)) | (1 << (OParser.TYPE_IDENTIFIER - 117)) | (1 << (OParser.VARIABLE_IDENTIFIER - 117)) | (1 << (OParser.DOLLAR_IDENTIFIER - 117)) | (1 << (OParser.TEXT_LITERAL - 117)) | (1 << (OParser.INTEGER_LITERAL - 117)) | (1 << (OParser.DECIMAL_LITERAL - 117)))) != 0):
                self.state = 2287
                localctx.args = self.csharp_arguments(0)


            self.state = 2290
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_csharp_arguments

     
        def copyFrom(self, ctx):
            super(OParser.Csharp_argumentsContext, self).copyFrom(ctx)


    class CSharpArgumentListContext(Csharp_argumentsContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_argumentsContext)
            super(OParser.CSharpArgumentListContext, self).__init__(parser)
            self.item = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def csharp_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpArgumentList"):
                listener.enterCSharpArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpArgumentList"):
                listener.exitCSharpArgumentList(self)


    class CSharpArgumentListItemContext(Csharp_argumentsContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_argumentsContext)
            super(OParser.CSharpArgumentListItemContext, self).__init__(parser)
            self.items = None # Csharp_argumentsContext
            self.item = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(OParser.COMMA, 0)
        def csharp_arguments(self):
            return self.getTypedRuleContext(OParser.Csharp_argumentsContext,0)

        def csharp_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpArgumentListItem"):
                listener.enterCSharpArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpArgumentListItem"):
                listener.exitCSharpArgumentListItem(self)



    def csharp_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Csharp_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 406
        self.enterRecursionRule(localctx, 406, self.RULE_csharp_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.CSharpArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2293
            localctx.item = self.csharp_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2300
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,198,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.CSharpArgumentListItemContext(self, OParser.Csharp_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_arguments)
                    self.state = 2295
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2296
                    self.match(OParser.COMMA)
                    self.state = 2297
                    localctx.item = self.csharp_expression(0) 
                self.state = 2302
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,198,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Csharp_expressionContext

        def LBRAK(self):
            return self.getToken(OParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(OParser.RBRAK, 0)

        def csharp_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_csharp_item_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_item_expression"):
                listener.enterCsharp_item_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_item_expression"):
                listener.exitCsharp_item_expression(self)




    def csharp_item_expression(self):

        localctx = OParser.Csharp_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 408, self.RULE_csharp_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2303
            self.match(OParser.LBRAK)
            self.state = 2304
            localctx.exp = self.csharp_expression(0)
            self.state = 2305
            self.match(OParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Csharp_expressionContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def csharp_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_expressionContext,0)


        def getRuleIndex(self):
            return OParser.RULE_csharp_parenthesis_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_parenthesis_expression"):
                listener.enterCsharp_parenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_parenthesis_expression"):
                listener.exitCsharp_parenthesis_expression(self)




    def csharp_parenthesis_expression(self):

        localctx = OParser.Csharp_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 410, self.RULE_csharp_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2307
            self.match(OParser.LPAR)
            self.state = 2308
            localctx.exp = self.csharp_expression(0)
            self.state = 2309
            self.match(OParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_csharp_identifier_expression

     
        def copyFrom(self, ctx):
            super(OParser.Csharp_identifier_expressionContext, self).copyFrom(ctx)


    class CSharpIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_identifier_expressionContext)
            super(OParser.CSharpIdentifierContext, self).__init__(parser)
            self.name = None # Csharp_identifierContext
            self.copyFrom(ctx)

        def csharp_identifier(self):
            return self.getTypedRuleContext(OParser.Csharp_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpIdentifier"):
                listener.enterCSharpIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpIdentifier"):
                listener.exitCSharpIdentifier(self)


    class CSharpChildIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_identifier_expressionContext)
            super(OParser.CSharpChildIdentifierContext, self).__init__(parser)
            self.parent = None # Csharp_identifier_expressionContext
            self.name = None # Csharp_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(OParser.DOT, 0)
        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(OParser.Csharp_identifier_expressionContext,0)

        def csharp_identifier(self):
            return self.getTypedRuleContext(OParser.Csharp_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpChildIdentifier"):
                listener.enterCSharpChildIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpChildIdentifier"):
                listener.exitCSharpChildIdentifier(self)


    class CSharpPromptoIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_identifier_expressionContext)
            super(OParser.CSharpPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(OParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpPromptoIdentifier"):
                listener.enterCSharpPromptoIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpPromptoIdentifier"):
                listener.exitCSharpPromptoIdentifier(self)



    def csharp_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OParser.Csharp_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 412
        self.enterRecursionRule(localctx, 412, self.RULE_csharp_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2314
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.DOLLAR_IDENTIFIER]:
                localctx = OParser.CSharpPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2312
                self.match(OParser.DOLLAR_IDENTIFIER)
                pass
            elif token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.UUID, OParser.NONE, OParser.NULL, OParser.READ, OParser.SELF, OParser.TEST, OParser.WRITE, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER]:
                localctx = OParser.CSharpIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2313
                localctx.name = self.csharp_identifier()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2321
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,200,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.CSharpChildIdentifierContext(self, OParser.Csharp_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_identifier_expression)
                    self.state = 2316
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2317
                    self.match(OParser.DOT)
                    self.state = 2318
                    localctx.name = self.csharp_identifier() 
                self.state = 2323
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,200,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_csharp_literal_expression

     
        def copyFrom(self, ctx):
            super(OParser.Csharp_literal_expressionContext, self).copyFrom(ctx)



    class CSharpBooleanLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_literal_expressionContext)
            super(OParser.CSharpBooleanLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(OParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpBooleanLiteral"):
                listener.enterCSharpBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpBooleanLiteral"):
                listener.exitCSharpBooleanLiteral(self)


    class CSharpIntegerLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_literal_expressionContext)
            super(OParser.CSharpIntegerLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(OParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpIntegerLiteral"):
                listener.enterCSharpIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpIntegerLiteral"):
                listener.exitCSharpIntegerLiteral(self)


    class CSharpDecimalLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_literal_expressionContext)
            super(OParser.CSharpDecimalLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(OParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpDecimalLiteral"):
                listener.enterCSharpDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpDecimalLiteral"):
                listener.exitCSharpDecimalLiteral(self)


    class CSharpCharacterLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_literal_expressionContext)
            super(OParser.CSharpCharacterLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(OParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpCharacterLiteral"):
                listener.enterCSharpCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpCharacterLiteral"):
                listener.exitCSharpCharacterLiteral(self)


    class CSharpTextLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a OParser.Csharp_literal_expressionContext)
            super(OParser.CSharpTextLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(OParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpTextLiteral"):
                listener.enterCSharpTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpTextLiteral"):
                listener.exitCSharpTextLiteral(self)



    def csharp_literal_expression(self):

        localctx = OParser.Csharp_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 414, self.RULE_csharp_literal_expression)
        try:
            self.state = 2329
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.CSharpIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2324
                self.match(OParser.INTEGER_LITERAL)
                pass
            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.CSharpDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2325
                self.match(OParser.DECIMAL_LITERAL)
                pass
            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.CSharpTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2326
                self.match(OParser.TEXT_LITERAL)
                pass
            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.CSharpBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2327
                self.match(OParser.BOOLEAN_LITERAL)
                pass
            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.CSharpCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2328
                self.match(OParser.CHAR_LITERAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Csharp_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(OParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(OParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(OParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(OParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(OParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(OParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(OParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(OParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(OParser.DATE, 0)

        def TIME(self):
            return self.getToken(OParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(OParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(OParser.PERIOD, 0)

        def VERSION(self):
            return self.getToken(OParser.VERSION, 0)

        def UUID(self):
            return self.getToken(OParser.UUID, 0)

        def READ(self):
            return self.getToken(OParser.READ, 0)

        def WRITE(self):
            return self.getToken(OParser.WRITE, 0)

        def TEST(self):
            return self.getToken(OParser.TEST, 0)

        def SELF(self):
            return self.getToken(OParser.SELF, 0)

        def NONE(self):
            return self.getToken(OParser.NONE, 0)

        def NULL(self):
            return self.getToken(OParser.NULL, 0)

        def getRuleIndex(self):
            return OParser.RULE_csharp_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_identifier"):
                listener.enterCsharp_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_identifier"):
                listener.exitCsharp_identifier(self)




    def csharp_identifier(self):

        localctx = OParser.Csharp_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 416, self.RULE_csharp_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2331
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.UUID))) != 0) or ((((_la - 117)) & ~0x3f) == 0 and ((1 << (_la - 117)) & ((1 << (OParser.NONE - 117)) | (1 << (OParser.NULL - 117)) | (1 << (OParser.READ - 117)) | (1 << (OParser.SELF - 117)) | (1 << (OParser.TEST - 117)) | (1 << (OParser.WRITE - 117)) | (1 << (OParser.SYMBOL_IDENTIFIER - 117)) | (1 << (OParser.TYPE_IDENTIFIER - 117)) | (1 << (OParser.VARIABLE_IDENTIFIER - 117)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def jsx_element(self):
            return self.getTypedRuleContext(OParser.Jsx_elementContext,0)


        def jsx_fragment(self):
            return self.getTypedRuleContext(OParser.Jsx_fragmentContext,0)


        def getRuleIndex(self):
            return OParser.RULE_jsx_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_expression"):
                listener.enterJsx_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_expression"):
                listener.exitJsx_expression(self)




    def jsx_expression(self):

        localctx = OParser.Jsx_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 418, self.RULE_jsx_expression)
        try:
            self.state = 2335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,202,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2333
                self.jsx_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2334
                self.jsx_fragment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_elementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_elementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_jsx_element

     
        def copyFrom(self, ctx):
            super(OParser.Jsx_elementContext, self).copyFrom(ctx)



    class JsxSelfClosingContext(Jsx_elementContext):

        def __init__(self, parser, ctx): # actually a OParser.Jsx_elementContext)
            super(OParser.JsxSelfClosingContext, self).__init__(parser)
            self.jsx = None # Jsx_self_closingContext
            self.copyFrom(ctx)

        def jsx_self_closing(self):
            return self.getTypedRuleContext(OParser.Jsx_self_closingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJsxSelfClosing"):
                listener.enterJsxSelfClosing(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxSelfClosing"):
                listener.exitJsxSelfClosing(self)


    class JsxElementContext(Jsx_elementContext):

        def __init__(self, parser, ctx): # actually a OParser.Jsx_elementContext)
            super(OParser.JsxElementContext, self).__init__(parser)
            self.jsx = None # Jsx_openingContext
            self.children_ = None # Jsx_childrenContext
            self.copyFrom(ctx)

        def jsx_closing(self):
            return self.getTypedRuleContext(OParser.Jsx_closingContext,0)

        def jsx_opening(self):
            return self.getTypedRuleContext(OParser.Jsx_openingContext,0)

        def jsx_children(self):
            return self.getTypedRuleContext(OParser.Jsx_childrenContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJsxElement"):
                listener.enterJsxElement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxElement"):
                listener.exitJsxElement(self)



    def jsx_element(self):

        localctx = OParser.Jsx_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 420, self.RULE_jsx_element)
        try:
            self.state = 2344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,204,self._ctx)
            if la_ == 1:
                localctx = OParser.JsxSelfClosingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2337
                localctx.jsx = self.jsx_self_closing()
                pass

            elif la_ == 2:
                localctx = OParser.JsxElementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2338
                localctx.jsx = self.jsx_opening()
                self.state = 2340
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,203,self._ctx)
                if la_ == 1:
                    self.state = 2339
                    localctx.children_ = self.jsx_children()


                self.state = 2342
                self.jsx_closing()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_fragmentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_fragmentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.children_ = None # Jsx_childrenContext

        def jsx_fragment_start(self):
            return self.getTypedRuleContext(OParser.Jsx_fragment_startContext,0)


        def jsx_fragment_end(self):
            return self.getTypedRuleContext(OParser.Jsx_fragment_endContext,0)


        def jsx_children(self):
            return self.getTypedRuleContext(OParser.Jsx_childrenContext,0)


        def getRuleIndex(self):
            return OParser.RULE_jsx_fragment

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_fragment"):
                listener.enterJsx_fragment(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_fragment"):
                listener.exitJsx_fragment(self)




    def jsx_fragment(self):

        localctx = OParser.Jsx_fragmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 422, self.RULE_jsx_fragment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2346
            self.jsx_fragment_start()
            self.state = 2348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,205,self._ctx)
            if la_ == 1:
                self.state = 2347
                localctx.children_ = self.jsx_children()


            self.state = 2350
            self.jsx_fragment_end()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_fragment_startContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_fragment_startContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(OParser.LT, 0)

        def GT(self):
            return self.getToken(OParser.GT, 0)

        def LTGT(self):
            return self.getToken(OParser.LTGT, 0)

        def getRuleIndex(self):
            return OParser.RULE_jsx_fragment_start

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_fragment_start"):
                listener.enterJsx_fragment_start(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_fragment_start"):
                listener.exitJsx_fragment_start(self)




    def jsx_fragment_start(self):

        localctx = OParser.Jsx_fragment_startContext(self, self._ctx, self.state)
        self.enterRule(localctx, 424, self.RULE_jsx_fragment_start)
        try:
            self.state = 2355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.LT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2352
                self.match(OParser.LT)
                self.state = 2353
                self.match(OParser.GT)
                pass
            elif token in [OParser.LTGT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2354
                self.match(OParser.LTGT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_fragment_endContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_fragment_endContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(OParser.LT, 0)

        def SLASH(self):
            return self.getToken(OParser.SLASH, 0)

        def GT(self):
            return self.getToken(OParser.GT, 0)

        def getRuleIndex(self):
            return OParser.RULE_jsx_fragment_end

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_fragment_end"):
                listener.enterJsx_fragment_end(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_fragment_end"):
                listener.exitJsx_fragment_end(self)




    def jsx_fragment_end(self):

        localctx = OParser.Jsx_fragment_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 426, self.RULE_jsx_fragment_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2357
            self.match(OParser.LT)
            self.state = 2358
            self.match(OParser.SLASH)
            self.state = 2359
            self.match(OParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_self_closingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_self_closingContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Jsx_element_nameContext
            self.attributes = None # Jsx_attributeContext

        def LT(self):
            return self.getToken(OParser.LT, 0)

        def SLASH(self):
            return self.getToken(OParser.SLASH, 0)

        def GT(self):
            return self.getToken(OParser.GT, 0)

        def jsx_element_name(self):
            return self.getTypedRuleContext(OParser.Jsx_element_nameContext,0)


        def jsx_attribute(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Jsx_attributeContext)
            else:
                return self.getTypedRuleContext(OParser.Jsx_attributeContext,i)


        def getRuleIndex(self):
            return OParser.RULE_jsx_self_closing

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_self_closing"):
                listener.enterJsx_self_closing(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_self_closing"):
                listener.exitJsx_self_closing(self)




    def jsx_self_closing(self):

        localctx = OParser.Jsx_self_closingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 428, self.RULE_jsx_self_closing)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2361
            self.match(OParser.LT)
            self.state = 2362
            localctx.name = self.jsx_element_name()
            self.state = 2366
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.JAVA) | (1 << OParser.CSHARP) | (1 << OParser.PYTHON2) | (1 << OParser.PYTHON3) | (1 << OParser.JAVASCRIPT) | (1 << OParser.SWIFT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.METHOD_T) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.ABSTRACT - 64)) | (1 << (OParser.ALL - 64)) | (1 << (OParser.ALWAYS - 64)) | (1 << (OParser.AND - 64)) | (1 << (OParser.ANY - 64)) | (1 << (OParser.AS - 64)) | (1 << (OParser.ASC - 64)) | (1 << (OParser.ATTR - 64)) | (1 << (OParser.ATTRIBUTE - 64)) | (1 << (OParser.ATTRIBUTES - 64)) | (1 << (OParser.BINDINGS - 64)) | (1 << (OParser.BREAK - 64)) | (1 << (OParser.BY - 64)) | (1 << (OParser.CASE - 64)) | (1 << (OParser.CATCH - 64)) | (1 << (OParser.CATEGORY - 64)) | (1 << (OParser.CLASS - 64)) | (1 << (OParser.CLOSE - 64)) | (1 << (OParser.CONTAINS - 64)) | (1 << (OParser.DEF - 64)) | (1 << (OParser.DEFAULT - 64)) | (1 << (OParser.DEFINE - 64)) | (1 << (OParser.DELETE - 64)) | (1 << (OParser.DESC - 64)) | (1 << (OParser.DO - 64)) | (1 << (OParser.DOING - 64)) | (1 << (OParser.EACH - 64)) | (1 << (OParser.ELSE - 64)) | (1 << (OParser.ENUM - 64)) | (1 << (OParser.ENUMERATED - 64)) | (1 << (OParser.EXCEPT - 64)) | (1 << (OParser.EXECUTE - 64)) | (1 << (OParser.EXPECTING - 64)) | (1 << (OParser.EXTENDS - 64)) | (1 << (OParser.FETCH - 64)) | (1 << (OParser.FILTERED - 64)) | (1 << (OParser.FINALLY - 64)) | (1 << (OParser.FLUSH - 64)) | (1 << (OParser.FOR - 64)) | (1 << (OParser.FROM - 64)) | (1 << (OParser.GETTER - 64)) | (1 << (OParser.HAS - 64)) | (1 << (OParser.IF - 64)) | (1 << (OParser.IN - 64)) | (1 << (OParser.INDEX - 64)) | (1 << (OParser.INVOKE - 64)) | (1 << (OParser.IS - 64)) | (1 << (OParser.MATCHING - 64)) | (1 << (OParser.METHOD - 64)) | (1 << (OParser.METHODS - 64)) | (1 << (OParser.MODULO - 64)) | (1 << (OParser.MUTABLE - 64)) | (1 << (OParser.NATIVE - 64)) | (1 << (OParser.NONE - 64)) | (1 << (OParser.NOT - 64)) | (1 << (OParser.NOTHING - 64)) | (1 << (OParser.NULL - 64)) | (1 << (OParser.ON - 64)) | (1 << (OParser.ONE - 64)) | (1 << (OParser.OPEN - 64)) | (1 << (OParser.OPERATOR - 64)) | (1 << (OParser.OR - 64)) | (1 << (OParser.ORDER - 64)) | (1 << (OParser.OTHERWISE - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (OParser.PASS - 128)) | (1 << (OParser.RAISE - 128)) | (1 << (OParser.READ - 128)) | (1 << (OParser.RECEIVING - 128)) | (1 << (OParser.RESOURCE - 128)) | (1 << (OParser.RETURN - 128)) | (1 << (OParser.RETURNING - 128)) | (1 << (OParser.ROWS - 128)) | (1 << (OParser.SELF - 128)) | (1 << (OParser.SETTER - 128)) | (1 << (OParser.SINGLETON - 128)) | (1 << (OParser.SORTED - 128)) | (1 << (OParser.STORABLE - 128)) | (1 << (OParser.STORE - 128)) | (1 << (OParser.SWITCH - 128)) | (1 << (OParser.TEST - 128)) | (1 << (OParser.THIS - 128)) | (1 << (OParser.THROW - 128)) | (1 << (OParser.TO - 128)) | (1 << (OParser.TRY - 128)) | (1 << (OParser.VERIFYING - 128)) | (1 << (OParser.WITH - 128)) | (1 << (OParser.WHEN - 128)) | (1 << (OParser.WHERE - 128)) | (1 << (OParser.WHILE - 128)) | (1 << (OParser.WRITE - 128)) | (1 << (OParser.SYMBOL_IDENTIFIER - 128)) | (1 << (OParser.TYPE_IDENTIFIER - 128)) | (1 << (OParser.VARIABLE_IDENTIFIER - 128)))) != 0):
                self.state = 2363
                localctx.attributes = self.jsx_attribute()
                self.state = 2368
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2369
            self.match(OParser.SLASH)
            self.state = 2370
            self.match(OParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_openingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_openingContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Jsx_element_nameContext
            self.attributes = None # Jsx_attributeContext

        def LT(self):
            return self.getToken(OParser.LT, 0)

        def GT(self):
            return self.getToken(OParser.GT, 0)

        def jsx_element_name(self):
            return self.getTypedRuleContext(OParser.Jsx_element_nameContext,0)


        def jsx_attribute(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Jsx_attributeContext)
            else:
                return self.getTypedRuleContext(OParser.Jsx_attributeContext,i)


        def getRuleIndex(self):
            return OParser.RULE_jsx_opening

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_opening"):
                listener.enterJsx_opening(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_opening"):
                listener.exitJsx_opening(self)




    def jsx_opening(self):

        localctx = OParser.Jsx_openingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 430, self.RULE_jsx_opening)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2372
            self.match(OParser.LT)
            self.state = 2373
            localctx.name = self.jsx_element_name()
            self.state = 2377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.JAVA) | (1 << OParser.CSHARP) | (1 << OParser.PYTHON2) | (1 << OParser.PYTHON3) | (1 << OParser.JAVASCRIPT) | (1 << OParser.SWIFT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.METHOD_T) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.ABSTRACT - 64)) | (1 << (OParser.ALL - 64)) | (1 << (OParser.ALWAYS - 64)) | (1 << (OParser.AND - 64)) | (1 << (OParser.ANY - 64)) | (1 << (OParser.AS - 64)) | (1 << (OParser.ASC - 64)) | (1 << (OParser.ATTR - 64)) | (1 << (OParser.ATTRIBUTE - 64)) | (1 << (OParser.ATTRIBUTES - 64)) | (1 << (OParser.BINDINGS - 64)) | (1 << (OParser.BREAK - 64)) | (1 << (OParser.BY - 64)) | (1 << (OParser.CASE - 64)) | (1 << (OParser.CATCH - 64)) | (1 << (OParser.CATEGORY - 64)) | (1 << (OParser.CLASS - 64)) | (1 << (OParser.CLOSE - 64)) | (1 << (OParser.CONTAINS - 64)) | (1 << (OParser.DEF - 64)) | (1 << (OParser.DEFAULT - 64)) | (1 << (OParser.DEFINE - 64)) | (1 << (OParser.DELETE - 64)) | (1 << (OParser.DESC - 64)) | (1 << (OParser.DO - 64)) | (1 << (OParser.DOING - 64)) | (1 << (OParser.EACH - 64)) | (1 << (OParser.ELSE - 64)) | (1 << (OParser.ENUM - 64)) | (1 << (OParser.ENUMERATED - 64)) | (1 << (OParser.EXCEPT - 64)) | (1 << (OParser.EXECUTE - 64)) | (1 << (OParser.EXPECTING - 64)) | (1 << (OParser.EXTENDS - 64)) | (1 << (OParser.FETCH - 64)) | (1 << (OParser.FILTERED - 64)) | (1 << (OParser.FINALLY - 64)) | (1 << (OParser.FLUSH - 64)) | (1 << (OParser.FOR - 64)) | (1 << (OParser.FROM - 64)) | (1 << (OParser.GETTER - 64)) | (1 << (OParser.HAS - 64)) | (1 << (OParser.IF - 64)) | (1 << (OParser.IN - 64)) | (1 << (OParser.INDEX - 64)) | (1 << (OParser.INVOKE - 64)) | (1 << (OParser.IS - 64)) | (1 << (OParser.MATCHING - 64)) | (1 << (OParser.METHOD - 64)) | (1 << (OParser.METHODS - 64)) | (1 << (OParser.MODULO - 64)) | (1 << (OParser.MUTABLE - 64)) | (1 << (OParser.NATIVE - 64)) | (1 << (OParser.NONE - 64)) | (1 << (OParser.NOT - 64)) | (1 << (OParser.NOTHING - 64)) | (1 << (OParser.NULL - 64)) | (1 << (OParser.ON - 64)) | (1 << (OParser.ONE - 64)) | (1 << (OParser.OPEN - 64)) | (1 << (OParser.OPERATOR - 64)) | (1 << (OParser.OR - 64)) | (1 << (OParser.ORDER - 64)) | (1 << (OParser.OTHERWISE - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (OParser.PASS - 128)) | (1 << (OParser.RAISE - 128)) | (1 << (OParser.READ - 128)) | (1 << (OParser.RECEIVING - 128)) | (1 << (OParser.RESOURCE - 128)) | (1 << (OParser.RETURN - 128)) | (1 << (OParser.RETURNING - 128)) | (1 << (OParser.ROWS - 128)) | (1 << (OParser.SELF - 128)) | (1 << (OParser.SETTER - 128)) | (1 << (OParser.SINGLETON - 128)) | (1 << (OParser.SORTED - 128)) | (1 << (OParser.STORABLE - 128)) | (1 << (OParser.STORE - 128)) | (1 << (OParser.SWITCH - 128)) | (1 << (OParser.TEST - 128)) | (1 << (OParser.THIS - 128)) | (1 << (OParser.THROW - 128)) | (1 << (OParser.TO - 128)) | (1 << (OParser.TRY - 128)) | (1 << (OParser.VERIFYING - 128)) | (1 << (OParser.WITH - 128)) | (1 << (OParser.WHEN - 128)) | (1 << (OParser.WHERE - 128)) | (1 << (OParser.WHILE - 128)) | (1 << (OParser.WRITE - 128)) | (1 << (OParser.SYMBOL_IDENTIFIER - 128)) | (1 << (OParser.TYPE_IDENTIFIER - 128)) | (1 << (OParser.VARIABLE_IDENTIFIER - 128)))) != 0):
                self.state = 2374
                localctx.attributes = self.jsx_attribute()
                self.state = 2379
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2380
            self.match(OParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_closingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_closingContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Jsx_element_nameContext

        def LT(self):
            return self.getToken(OParser.LT, 0)

        def SLASH(self):
            return self.getToken(OParser.SLASH, 0)

        def GT(self):
            return self.getToken(OParser.GT, 0)

        def jsx_element_name(self):
            return self.getTypedRuleContext(OParser.Jsx_element_nameContext,0)


        def getRuleIndex(self):
            return OParser.RULE_jsx_closing

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_closing"):
                listener.enterJsx_closing(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_closing"):
                listener.exitJsx_closing(self)




    def jsx_closing(self):

        localctx = OParser.Jsx_closingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 432, self.RULE_jsx_closing)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2382
            self.match(OParser.LT)
            self.state = 2383
            self.match(OParser.SLASH)
            self.state = 2384
            localctx.name = self.jsx_element_name()
            self.state = 2385
            self.match(OParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_element_nameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_element_nameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def jsx_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Jsx_identifierContext)
            else:
                return self.getTypedRuleContext(OParser.Jsx_identifierContext,i)


        def DOT(self, i=None):
            if i is None:
                return self.getTokens(OParser.DOT)
            else:
                return self.getToken(OParser.DOT, i)

        def getRuleIndex(self):
            return OParser.RULE_jsx_element_name

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_element_name"):
                listener.enterJsx_element_name(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_element_name"):
                listener.exitJsx_element_name(self)




    def jsx_element_name(self):

        localctx = OParser.Jsx_element_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 434, self.RULE_jsx_element_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2387
            self.jsx_identifier()
            self.state = 2392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.DOT:
                self.state = 2388
                self.match(OParser.DOT)
                self.state = 2389
                self.jsx_identifier()
                self.state = 2394
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier_or_keyword(self):
            return self.getTypedRuleContext(OParser.Identifier_or_keywordContext,0)


        def jsx_hyphen_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Jsx_hyphen_identifierContext)
            else:
                return self.getTypedRuleContext(OParser.Jsx_hyphen_identifierContext,i)


        def getRuleIndex(self):
            return OParser.RULE_jsx_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_identifier"):
                listener.enterJsx_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_identifier"):
                listener.exitJsx_identifier(self)




    def jsx_identifier(self):

        localctx = OParser.Jsx_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 436, self.RULE_jsx_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2395
            self.identifier_or_keyword()
            self.state = 2399
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,210,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2396
                    self.jsx_hyphen_identifier() 
                self.state = 2401
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,210,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_hyphen_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_hyphen_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(OParser.MINUS, 0)

        def hyphen_identifier(self):
            return self.getTypedRuleContext(OParser.Hyphen_identifierContext,0)


        def getRuleIndex(self):
            return OParser.RULE_jsx_hyphen_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_hyphen_identifier"):
                listener.enterJsx_hyphen_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_hyphen_identifier"):
                listener.exitJsx_hyphen_identifier(self)




    def jsx_hyphen_identifier(self):

        localctx = OParser.Jsx_hyphen_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 438, self.RULE_jsx_hyphen_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2402
            if not self.wasNotWhiteSpace():
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.wasNotWhiteSpace()")
            self.state = 2403
            self.match(OParser.MINUS)
            self.state = 2404
            self.hyphen_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Hyphen_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Hyphen_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier_or_keyword(self):
            return self.getTypedRuleContext(OParser.Identifier_or_keywordContext,0)


        def getRuleIndex(self):
            return OParser.RULE_hyphen_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterHyphen_identifier"):
                listener.enterHyphen_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHyphen_identifier"):
                listener.exitHyphen_identifier(self)




    def hyphen_identifier(self):

        localctx = OParser.Hyphen_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 440, self.RULE_hyphen_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2406
            if not self.wasNotWhiteSpace():
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.wasNotWhiteSpace()")
            self.state = 2407
            self.identifier_or_keyword()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Identifier_or_keywordContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Identifier_or_keywordContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(OParser.IdentifierContext,0)


        def keyword(self):
            return self.getTypedRuleContext(OParser.KeywordContext,0)


        def getRuleIndex(self):
            return OParser.RULE_identifier_or_keyword

        def enterRule(self, listener):
            if hasattr(listener, "enterIdentifier_or_keyword"):
                listener.enterIdentifier_or_keyword(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIdentifier_or_keyword"):
                listener.exitIdentifier_or_keyword(self)




    def identifier_or_keyword(self):

        localctx = OParser.Identifier_or_keywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 442, self.RULE_identifier_or_keyword)
        try:
            self.state = 2411
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2409
                self.identifier()
                pass
            elif token in [OParser.JAVA, OParser.CSHARP, OParser.PYTHON2, OParser.PYTHON3, OParser.JAVASCRIPT, OParser.SWIFT, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.METHOD_T, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID, OParser.ITERATOR, OParser.CURSOR, OParser.ABSTRACT, OParser.ALL, OParser.ALWAYS, OParser.AND, OParser.ANY, OParser.AS, OParser.ASC, OParser.ATTR, OParser.ATTRIBUTE, OParser.ATTRIBUTES, OParser.BINDINGS, OParser.BREAK, OParser.BY, OParser.CASE, OParser.CATCH, OParser.CATEGORY, OParser.CLASS, OParser.CLOSE, OParser.CONTAINS, OParser.DEF, OParser.DEFAULT, OParser.DEFINE, OParser.DELETE, OParser.DESC, OParser.DO, OParser.DOING, OParser.EACH, OParser.ELSE, OParser.ENUM, OParser.ENUMERATED, OParser.EXCEPT, OParser.EXECUTE, OParser.EXPECTING, OParser.EXTENDS, OParser.FETCH, OParser.FILTERED, OParser.FINALLY, OParser.FLUSH, OParser.FOR, OParser.FROM, OParser.GETTER, OParser.HAS, OParser.IF, OParser.IN, OParser.INDEX, OParser.INVOKE, OParser.IS, OParser.MATCHING, OParser.METHOD, OParser.METHODS, OParser.MODULO, OParser.MUTABLE, OParser.NATIVE, OParser.NONE, OParser.NOT, OParser.NOTHING, OParser.NULL, OParser.ON, OParser.ONE, OParser.OPEN, OParser.OPERATOR, OParser.OR, OParser.ORDER, OParser.OTHERWISE, OParser.PASS, OParser.RAISE, OParser.READ, OParser.RECEIVING, OParser.RESOURCE, OParser.RETURN, OParser.RETURNING, OParser.ROWS, OParser.SELF, OParser.SETTER, OParser.SINGLETON, OParser.SORTED, OParser.STORABLE, OParser.STORE, OParser.SWITCH, OParser.TEST, OParser.THIS, OParser.THROW, OParser.TO, OParser.TRY, OParser.VERIFYING, OParser.WITH, OParser.WHEN, OParser.WHERE, OParser.WHILE, OParser.WRITE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2410
                self.keyword()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_attributeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_attributeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Jsx_identifierContext
            self.value = None # Jsx_attribute_valueContext

        def jsx_identifier(self):
            return self.getTypedRuleContext(OParser.Jsx_identifierContext,0)


        def EQ(self):
            return self.getToken(OParser.EQ, 0)

        def jsx_attribute_value(self):
            return self.getTypedRuleContext(OParser.Jsx_attribute_valueContext,0)


        def getRuleIndex(self):
            return OParser.RULE_jsx_attribute

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_attribute"):
                listener.enterJsx_attribute(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_attribute"):
                listener.exitJsx_attribute(self)




    def jsx_attribute(self):

        localctx = OParser.Jsx_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 444, self.RULE_jsx_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2413
            localctx.name = self.jsx_identifier()
            self.state = 2416
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.EQ:
                self.state = 2414
                self.match(OParser.EQ)
                self.state = 2415
                localctx.value = self.jsx_attribute_value()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_attribute_valueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_attribute_valueContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_jsx_attribute_value

     
        def copyFrom(self, ctx):
            super(OParser.Jsx_attribute_valueContext, self).copyFrom(ctx)



    class JsxValueContext(Jsx_attribute_valueContext):

        def __init__(self, parser, ctx): # actually a OParser.Jsx_attribute_valueContext)
            super(OParser.JsxValueContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJsxValue"):
                listener.enterJsxValue(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxValue"):
                listener.exitJsxValue(self)


    class JsxLiteralContext(Jsx_attribute_valueContext):

        def __init__(self, parser, ctx): # actually a OParser.Jsx_attribute_valueContext)
            super(OParser.JsxLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(OParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJsxLiteral"):
                listener.enterJsxLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxLiteral"):
                listener.exitJsxLiteral(self)



    def jsx_attribute_value(self):

        localctx = OParser.Jsx_attribute_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 446, self.RULE_jsx_attribute_value)
        try:
            self.state = 2423
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.TEXT_LITERAL]:
                localctx = OParser.JsxLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2418
                self.match(OParser.TEXT_LITERAL)
                pass
            elif token in [OParser.LCURL]:
                localctx = OParser.JsxValueContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2419
                self.match(OParser.LCURL)
                self.state = 2420
                localctx.exp = self.expression(0)
                self.state = 2421
                self.match(OParser.RCURL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_childrenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_childrenContext, self).__init__(parent, invokingState)
            self.parser = parser

        def jsx_child(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(OParser.Jsx_childContext)
            else:
                return self.getTypedRuleContext(OParser.Jsx_childContext,i)


        def getRuleIndex(self):
            return OParser.RULE_jsx_children

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_children"):
                listener.enterJsx_children(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_children"):
                listener.exitJsx_children(self)




    def jsx_children(self):

        localctx = OParser.Jsx_childrenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 448, self.RULE_jsx_children)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2426 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 2425
                    self.jsx_child()

                else:
                    raise NoViableAltException(self)
                self.state = 2428 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,214,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_childContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_childContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OParser.RULE_jsx_child

     
        def copyFrom(self, ctx):
            super(OParser.Jsx_childContext, self).copyFrom(ctx)



    class JsxTextContext(Jsx_childContext):

        def __init__(self, parser, ctx): # actually a OParser.Jsx_childContext)
            super(OParser.JsxTextContext, self).__init__(parser)
            self.text = None # Jsx_textContext
            self.copyFrom(ctx)

        def jsx_text(self):
            return self.getTypedRuleContext(OParser.Jsx_textContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJsxText"):
                listener.enterJsxText(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxText"):
                listener.exitJsxText(self)


    class JsxChildContext(Jsx_childContext):

        def __init__(self, parser, ctx): # actually a OParser.Jsx_childContext)
            super(OParser.JsxChildContext, self).__init__(parser)
            self.jsx = None # Jsx_elementContext
            self.copyFrom(ctx)

        def jsx_element(self):
            return self.getTypedRuleContext(OParser.Jsx_elementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJsxChild"):
                listener.enterJsxChild(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxChild"):
                listener.exitJsxChild(self)


    class JsxCodeContext(Jsx_childContext):

        def __init__(self, parser, ctx): # actually a OParser.Jsx_childContext)
            super(OParser.JsxCodeContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(OParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(OParser.RCURL, 0)
        def expression(self):
            return self.getTypedRuleContext(OParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJsxCode"):
                listener.enterJsxCode(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxCode"):
                listener.exitJsxCode(self)



    def jsx_child(self):

        localctx = OParser.Jsx_childContext(self, self._ctx, self.state)
        self.enterRule(localctx, 450, self.RULE_jsx_child)
        self._la = 0 # Token type
        try:
            self.state = 2437
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.SPACE, OParser.WS, OParser.LF, OParser.COMMENT, OParser.JAVA, OParser.CSHARP, OParser.PYTHON2, OParser.PYTHON3, OParser.JAVASCRIPT, OParser.SWIFT, OParser.COLON, OParser.SEMI, OParser.COMMA, OParser.RANGE, OParser.DOT, OParser.LPAR, OParser.RPAR, OParser.LBRAK, OParser.RBRAK, OParser.QMARK, OParser.XMARK, OParser.AMP, OParser.AMP2, OParser.PIPE, OParser.PIPE2, OParser.PLUS, OParser.MINUS, OParser.STAR, OParser.SLASH, OParser.BSLASH, OParser.PERCENT, OParser.GTE, OParser.LTE, OParser.LTGT, OParser.EQ, OParser.XEQ, OParser.EQ2, OParser.TEQ, OParser.TILDE, OParser.LARROW, OParser.RARROW, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.METHOD_T, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID, OParser.ITERATOR, OParser.CURSOR, OParser.ABSTRACT, OParser.ALL, OParser.ALWAYS, OParser.AND, OParser.ANY, OParser.AS, OParser.ASC, OParser.ATTR, OParser.ATTRIBUTE, OParser.ATTRIBUTES, OParser.BINDINGS, OParser.BREAK, OParser.BY, OParser.CASE, OParser.CATCH, OParser.CATEGORY, OParser.CLASS, OParser.CLOSE, OParser.CONTAINS, OParser.DEF, OParser.DEFAULT, OParser.DEFINE, OParser.DELETE, OParser.DESC, OParser.DO, OParser.DOING, OParser.EACH, OParser.ELSE, OParser.ENUM, OParser.ENUMERATED, OParser.EXCEPT, OParser.EXECUTE, OParser.EXPECTING, OParser.EXTENDS, OParser.FETCH, OParser.FILTERED, OParser.FINALLY, OParser.FLUSH, OParser.FOR, OParser.FROM, OParser.GETTER, OParser.HAS, OParser.IF, OParser.IN, OParser.INDEX, OParser.INVOKE, OParser.IS, OParser.MATCHING, OParser.METHOD, OParser.METHODS, OParser.MODULO, OParser.MUTABLE, OParser.NATIVE, OParser.NONE, OParser.NOT, OParser.NOTHING, OParser.NULL, OParser.ON, OParser.ONE, OParser.OPEN, OParser.OPERATOR, OParser.OR, OParser.ORDER, OParser.OTHERWISE, OParser.PASS, OParser.RAISE, OParser.READ, OParser.RECEIVING, OParser.RESOURCE, OParser.RETURN, OParser.RETURNING, OParser.ROWS, OParser.SELF, OParser.SETTER, OParser.SINGLETON, OParser.SORTED, OParser.STORABLE, OParser.STORE, OParser.SWITCH, OParser.TEST, OParser.THIS, OParser.THROW, OParser.TO, OParser.TRY, OParser.VERIFYING, OParser.WITH, OParser.WHEN, OParser.WHERE, OParser.WHILE, OParser.WRITE, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.MIN_INTEGER, OParser.MAX_INTEGER, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.NATIVE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER, OParser.TEXT_LITERAL, OParser.UUID_LITERAL, OParser.INTEGER_LITERAL, OParser.HEXA_LITERAL, OParser.DECIMAL_LITERAL, OParser.DATETIME_LITERAL, OParser.TIME_LITERAL, OParser.DATE_LITERAL, OParser.PERIOD_LITERAL, OParser.VERSION_LITERAL]:
                localctx = OParser.JsxTextContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2430
                localctx.text = self.jsx_text()
                pass
            elif token in [OParser.LT]:
                localctx = OParser.JsxChildContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2431
                localctx.jsx = self.jsx_element()
                pass
            elif token in [OParser.LCURL]:
                localctx = OParser.JsxCodeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2432
                self.match(OParser.LCURL)
                self.state = 2434
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.LTGT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (OParser.EXECUTE - 95)) | (1 << (OParser.FETCH - 95)) | (1 << (OParser.FILTERED - 95)) | (1 << (OParser.MUTABLE - 95)) | (1 << (OParser.NULL - 95)) | (1 << (OParser.READ - 95)) | (1 << (OParser.SELF - 95)) | (1 << (OParser.SORTED - 95)) | (1 << (OParser.THIS - 95)) | (1 << (OParser.BOOLEAN_LITERAL - 95)) | (1 << (OParser.CHAR_LITERAL - 95)) | (1 << (OParser.MIN_INTEGER - 95)) | (1 << (OParser.MAX_INTEGER - 95)) | (1 << (OParser.SYMBOL_IDENTIFIER - 95)))) != 0) or ((((_la - 159)) & ~0x3f) == 0 and ((1 << (_la - 159)) & ((1 << (OParser.TYPE_IDENTIFIER - 159)) | (1 << (OParser.VARIABLE_IDENTIFIER - 159)) | (1 << (OParser.TEXT_LITERAL - 159)) | (1 << (OParser.UUID_LITERAL - 159)) | (1 << (OParser.INTEGER_LITERAL - 159)) | (1 << (OParser.HEXA_LITERAL - 159)) | (1 << (OParser.DECIMAL_LITERAL - 159)) | (1 << (OParser.DATETIME_LITERAL - 159)) | (1 << (OParser.TIME_LITERAL - 159)) | (1 << (OParser.DATE_LITERAL - 159)) | (1 << (OParser.PERIOD_LITERAL - 159)) | (1 << (OParser.VERSION_LITERAL - 159)))) != 0):
                    self.state = 2433
                    localctx.exp = self.expression(0)


                self.state = 2436
                self.match(OParser.RCURL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_textContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(OParser.Jsx_textContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LCURL(self, i=None):
            if i is None:
                return self.getTokens(OParser.LCURL)
            else:
                return self.getToken(OParser.LCURL, i)

        def RCURL(self, i=None):
            if i is None:
                return self.getTokens(OParser.RCURL)
            else:
                return self.getToken(OParser.RCURL, i)

        def LT(self, i=None):
            if i is None:
                return self.getTokens(OParser.LT)
            else:
                return self.getToken(OParser.LT, i)

        def GT(self, i=None):
            if i is None:
                return self.getTokens(OParser.GT)
            else:
                return self.getToken(OParser.GT, i)

        def getRuleIndex(self):
            return OParser.RULE_jsx_text

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_text"):
                listener.enterJsx_text(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_text"):
                listener.exitJsx_text(self)




    def jsx_text(self):

        localctx = OParser.Jsx_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 452, self.RULE_jsx_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2440 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 2439
                    _la = self._input.LA(1)
                    if _la <= 0 or (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LCURL) | (1 << OParser.RCURL) | (1 << OParser.GT) | (1 << OParser.LT))) != 0):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 2442 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,217,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.derived_list_sempred
        self._predicates[17] = self.native_category_binding_list_sempred
        self._predicates[36] = self.else_if_statement_list_sempred
        self._predicates[44] = self.callable_parent_sempred
        self._predicates[46] = self.expression_sempred
        self._predicates[47] = self.an_expression_sempred
        self._predicates[49] = self.instance_expression_sempred
        self._predicates[59] = self.copy_from_sempred
        self._predicates[60] = self.argument_assignment_list_sempred
        self._predicates[79] = self.typedef_sempred
        self._predicates[99] = self.any_type_sempred
        self._predicates[136] = self.assignable_instance_sempred
        self._predicates[137] = self.is_expression_sempred
        self._predicates[144] = self.new_token_sempred
        self._predicates[145] = self.key_token_sempred
        self._predicates[146] = self.module_token_sempred
        self._predicates[147] = self.value_token_sempred
        self._predicates[148] = self.symbols_token_sempred
        self._predicates[157] = self.javascript_expression_sempred
        self._predicates[163] = self.javascript_arguments_sempred
        self._predicates[170] = self.python_expression_sempred
        self._predicates[176] = self.python_ordinal_argument_list_sempred
        self._predicates[177] = self.python_named_argument_list_sempred
        self._predicates[179] = self.python_identifier_expression_sempred
        self._predicates[183] = self.java_expression_sempred
        self._predicates[189] = self.java_arguments_sempred
        self._predicates[192] = self.java_identifier_expression_sempred
        self._predicates[193] = self.java_class_identifier_expression_sempred
        self._predicates[197] = self.csharp_expression_sempred
        self._predicates[203] = self.csharp_arguments_sempred
        self._predicates[206] = self.csharp_identifier_expression_sempred
        self._predicates[219] = self.jsx_hyphen_identifier_sempred
        self._predicates[220] = self.hyphen_identifier_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def derived_list_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def native_category_binding_list_sempred(self, localctx, predIndex):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def else_if_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def callable_parent_sempred(self, localctx, predIndex):
            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx, predIndex):
            if predIndex == 4:
                return self.precpred(self._ctx, 34)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 33)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 32)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 31)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 30)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 25)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 23:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 24:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 25:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 26:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 27:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 28:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 29:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 30:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 31:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 32:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 33:
                return self.precpred(self._ctx, 1)
         

    def an_expression_sempred(self, localctx, predIndex):
            if predIndex == 34:
                return self.willBeAOrAn()
         

    def instance_expression_sempred(self, localctx, predIndex):
            if predIndex == 35:
                return self.precpred(self._ctx, 1)
         

    def copy_from_sempred(self, localctx, predIndex):
            if predIndex == 36:
                return self.willNotBe(self.equalToken())
         

    def argument_assignment_list_sempred(self, localctx, predIndex):
            if predIndex == 37:
                return self.willNotBe(self.equalToken())
         

            if predIndex == 38:
                return self.precpred(self._ctx, 1)
         

    def typedef_sempred(self, localctx, predIndex):
            if predIndex == 39:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 40:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 41:
                return self.precpred(self._ctx, 3)
         

    def any_type_sempred(self, localctx, predIndex):
            if predIndex == 42:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 43:
                return self.precpred(self._ctx, 1)
         

    def assignable_instance_sempred(self, localctx, predIndex):
            if predIndex == 44:
                return self.precpred(self._ctx, 1)
         

    def is_expression_sempred(self, localctx, predIndex):
            if predIndex == 45:
                return self.willBeAOrAn()
         

    def new_token_sempred(self, localctx, predIndex):
            if predIndex == 46:
                return self.isText(localctx.i1,"new")
         

    def key_token_sempred(self, localctx, predIndex):
            if predIndex == 47:
                return self.isText(localctx.i1,"key")
         

    def module_token_sempred(self, localctx, predIndex):
            if predIndex == 48:
                return self.isText(localctx.i1,"module")
         

    def value_token_sempred(self, localctx, predIndex):
            if predIndex == 49:
                return self.isText(localctx.i1,"value")
         

    def symbols_token_sempred(self, localctx, predIndex):
            if predIndex == 50:
                return self.isText(localctx.i1,"symbols")
         

    def javascript_expression_sempred(self, localctx, predIndex):
            if predIndex == 51:
                return self.precpred(self._ctx, 1)
         

    def javascript_arguments_sempred(self, localctx, predIndex):
            if predIndex == 52:
                return self.precpred(self._ctx, 1)
         

    def python_expression_sempred(self, localctx, predIndex):
            if predIndex == 53:
                return self.precpred(self._ctx, 1)
         

    def python_ordinal_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 54:
                return self.precpred(self._ctx, 1)
         

    def python_named_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 55:
                return self.precpred(self._ctx, 1)
         

    def python_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 56:
                return self.precpred(self._ctx, 1)
         

    def java_expression_sempred(self, localctx, predIndex):
            if predIndex == 57:
                return self.precpred(self._ctx, 1)
         

    def java_arguments_sempred(self, localctx, predIndex):
            if predIndex == 58:
                return self.precpred(self._ctx, 1)
         

    def java_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 59:
                return self.precpred(self._ctx, 1)
         

    def java_class_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 60:
                return self.precpred(self._ctx, 1)
         

    def csharp_expression_sempred(self, localctx, predIndex):
            if predIndex == 61:
                return self.precpred(self._ctx, 1)
         

    def csharp_arguments_sempred(self, localctx, predIndex):
            if predIndex == 62:
                return self.precpred(self._ctx, 1)
         

    def csharp_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 63:
                return self.precpred(self._ctx, 1)
         

    def jsx_hyphen_identifier_sempred(self, localctx, predIndex):
            if predIndex == 64:
                return self.wasNotWhiteSpace()
         

    def hyphen_identifier_sempred(self, localctx, predIndex):
            if predIndex == 65:
                return self.wasNotWhiteSpace()
         




