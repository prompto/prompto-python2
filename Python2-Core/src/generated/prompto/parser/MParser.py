# Generated from MParser.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

from .AbstractParser import AbstractParser

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\u00b4\u09e8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
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
        buf.write(u"\4\u00e4\t\u00e4\4\u00e5\t\u00e5\4\u00e6\t\u00e6\4\u00e7")
        buf.write(u"\t\u00e7\4\u00e8\t\u00e8\4\u00e9\t\u00e9\4\u00ea\t\u00ea")
        buf.write(u"\4\u00eb\t\u00eb\4\u00ec\t\u00ec\3\2\3\2\3\2\3\2\3\2")
        buf.write(u"\3\2\5\2\u01df\n\2\3\2\5\2\u01e2\n\2\3\2\3\2\3\2\3\2")
        buf.write(u"\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write(u"\3\4\3\4\3\4\3\5\3\5\3\5\5\5\u01fb\n\5\3\5\3\5\3\6\5")
        buf.write(u"\6\u0200\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write(u"\3\6\3\6\5\6\u020e\n\6\3\6\3\6\3\6\3\6\5\6\u0214\n\6")
        buf.write(u"\5\6\u0216\n\6\5\6\u0218\n\6\3\6\3\6\3\7\3\7\3\7\5\7")
        buf.write(u"\u021f\n\7\3\7\3\7\3\b\3\b\3\b\3\b\5\b\u0227\n\b\3\b")
        buf.write(u"\3\b\3\b\3\b\3\b\5\b\u022e\n\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write(u"\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\5\n\u023f\n\n")
        buf.write(u"\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u024a\n\n\3")
        buf.write(u"\n\3\n\3\n\3\n\3\n\5\n\u0251\n\n\3\n\3\n\3\13\3\13\3")
        buf.write(u"\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u025e\n\13\3\13")
        buf.write(u"\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u026c")
        buf.write(u"\n\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write(u"\3\16\3\16\3\16\3\16\3\17\3\17\3\17\5\17\u0280\n\17\3")
        buf.write(u"\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write(u"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\5")
        buf.write(u"\21\u0297\n\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write(u"\3\22\5\22\u02a2\n\22\3\22\3\22\3\22\3\22\3\22\5\22\u02a9")
        buf.write(u"\n\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u02b2\n")
        buf.write(u"\22\3\22\3\22\3\23\5\23\u02b7\n\23\3\23\3\23\3\23\3\23")
        buf.write(u"\3\23\5\23\u02be\n\23\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write(u"\23\5\23\u02c7\n\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write(u"\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\7")
        buf.write(u"\25\u02da\n\25\f\25\16\25\u02dd\13\25\3\26\3\26\3\26")
        buf.write(u"\3\26\3\26\5\26\u02e4\n\26\3\26\3\26\3\26\5\26\u02e9")
        buf.write(u"\n\26\3\27\3\27\3\27\3\27\5\27\u02ef\n\27\3\27\3\27\3")
        buf.write(u"\27\5\27\u02f4\n\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write(u"\5\30\u02fd\n\30\3\30\3\30\3\30\5\30\u0302\n\30\3\30")
        buf.write(u"\3\30\3\30\5\30\u0307\n\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write(u"\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write(u"\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u031f\n\31\3\32\3")
        buf.write(u"\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u032a\n\33")
        buf.write(u"\3\33\3\33\5\33\u032e\n\33\3\34\3\34\3\34\3\34\3\34\3")
        buf.write(u"\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write(u"\3\34\3\34\3\34\5\34\u0343\n\34\3\35\3\35\3\35\3\35\3")
        buf.write(u"\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write(u"\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u035d")
        buf.write(u"\n\36\3\37\3\37\3\37\5\37\u0362\n\37\3\37\3\37\3 \3 ")
        buf.write(u"\3 \3 \3 \5 \u036b\n \3!\3!\3!\3!\3!\7!\u0372\n!\f!\16")
        buf.write(u"!\u0375\13!\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u037d\n\"\3#")
        buf.write(u"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3")
        buf.write(u"%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u039a\n%\3%\3%\3&\3&\3&")
        buf.write(u"\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u03ad\n&\3\'")
        buf.write(u"\3\'\3\'\3\'\5\'\u03b3\n\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write(u"\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(u"*\3*\3*\3*\3*\3*\3*\3*\3*\5*\u03d5\n*\3*\3*\3*\3*\3*")
        buf.write(u"\3*\3*\5*\u03de\n*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write(u"+\3+\3+\3+\3+\3+\3+\3+\7+\u03f3\n+\f+\16+\u03f6\13+\3")
        buf.write(u",\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\5-\u0403\n-\3-\3-\3-")
        buf.write(u"\3-\3-\3-\3-\5-\u040c\n-\3-\3-\3-\3-\3-\3-\3-\5-\u0415")
        buf.write(u"\n-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(u".\3.\3.\3.\3.\5.\u042c\n.\3/\3/\3\60\3\60\5\60\u0432")
        buf.write(u"\n\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write(u"\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write(u"\5\61\u0448\n\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write(u"\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write(u"\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write(u"\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write(u"\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write(u"\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write(u"\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write(u"\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write(u"\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write(u"\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write(u"\3\61\3\61\3\61\3\61\3\61\3\61\3\61\7\61\u04b7\n\61\f")
        buf.write(u"\61\16\61\u04ba\13\61\3\62\3\62\3\63\3\63\3\63\3\63\3")
        buf.write(u"\63\7\63\u04c3\n\63\f\63\16\63\u04c6\13\63\3\64\3\64")
        buf.write(u"\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u04d0\n\64\3\65\3")
        buf.write(u"\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write(u"\3\65\5\65\u04df\n\65\3\66\3\66\3\66\5\66\u04e4\n\66")
        buf.write(u"\3\66\3\66\3\67\3\67\3\67\5\67\u04eb\n\67\3\67\3\67\3")
        buf.write(u"8\38\38\38\38\58\u04f4\n8\38\38\38\38\38\58\u04fb\n8")
        buf.write(u"\38\38\58\u04ff\n8\39\39\39\39\39\3:\3:\3:\3:\3:\5:\u050b")
        buf.write(u"\n:\3:\3:\3:\7:\u0510\n:\f:\16:\u0513\13:\3;\3;\3;\3")
        buf.write(u";\5;\u0519\n;\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3>\3>")
        buf.write(u"\3>\5>\u0529\n>\3>\3>\3>\3>\3>\3>\3>\3>\3>\5>\u0534\n")
        buf.write(u">\3>\3>\5>\u0538\n>\3>\3>\3>\5>\u053d\n>\3>\3>\3>\5>")
        buf.write(u"\u0542\n>\5>\u0544\n>\3?\3?\5?\u0548\n?\3?\3?\3?\3?\3")
        buf.write(u"?\3?\3?\5?\u0551\n?\3?\3?\3@\3@\3@\3@\3A\3A\3A\3A\3A")
        buf.write(u"\3A\3A\3A\5A\u0561\nA\3B\3B\3B\3B\3C\7C\u0568\nC\fC\16")
        buf.write(u"C\u056b\13C\3D\6D\u056e\nD\rD\16D\u056f\3E\6E\u0573\n")
        buf.write(u"E\rE\16E\u0574\3E\3E\3F\7F\u057a\nF\fF\16F\u057d\13F")
        buf.write(u"\3F\3F\3G\3G\3H\5H\u0584\nH\3H\3H\3H\3I\3I\3I\3I\7I\u058d")
        buf.write(u"\nI\fI\16I\u0590\13I\3J\3J\3J\7J\u0595\nJ\fJ\16J\u0598")
        buf.write(u"\13J\3J\3J\3J\3J\3J\3J\5J\u05a0\nJ\3K\3K\3L\3L\5L\u05a6")
        buf.write(u"\nL\3M\3M\3M\3M\7M\u05ac\nM\fM\16M\u05af\13M\3N\3N\3")
        buf.write(u"N\3N\7N\u05b5\nN\fN\16N\u05b8\13N\3O\3O\3O\7O\u05bd\n")
        buf.write(u"O\fO\16O\u05c0\13O\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\5P\u05cc")
        buf.write(u"\nP\3Q\5Q\u05cf\nQ\3Q\3Q\5Q\u05d3\nQ\3Q\3Q\3R\5R\u05d8")
        buf.write(u"\nR\3R\3R\5R\u05dc\nR\3R\3R\3S\3S\3S\7S\u05e3\nS\fS\16")
        buf.write(u"S\u05e6\13S\3T\3T\3T\3T\3T\3T\3U\3U\3U\3U\3U\3U\3U\3")
        buf.write(u"U\3U\3U\3U\3U\5U\u05fa\nU\3U\3U\3U\3U\3U\3U\3U\3U\7U")
        buf.write(u"\u0604\nU\fU\16U\u0607\13U\3V\3V\5V\u060b\nV\3W\3W\3")
        buf.write(u"W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\5W\u061d\nW")
        buf.write(u"\3X\3X\3Y\5Y\u0622\nY\3Y\3Y\3Z\3Z\3[\3[\3[\5[\u062b\n")
        buf.write(u"[\3\\\3\\\5\\\u062f\n\\\3]\3]\3]\7]\u0634\n]\f]\16]\u0637")
        buf.write(u"\13]\3^\3^\5^\u063b\n^\3_\3_\5_\u063f\n_\3`\3`\3`\3`")
        buf.write(u"\3a\3a\3a\3b\3b\3b\5b\u064b\nb\3c\3c\3d\3d\3e\3e\3f\3")
        buf.write(u"f\3g\3g\3g\7g\u0658\ng\fg\16g\u065b\13g\3h\3h\5h\u065f")
        buf.write(u"\nh\3h\5h\u0662\nh\3i\3i\5i\u0666\ni\3j\3j\3j\5j\u066b")
        buf.write(u"\nj\3k\3k\3k\3l\3l\5l\u0672\nl\3m\3m\3m\3m\3m\3m\3m\3")
        buf.write(u"m\3m\7m\u067d\nm\fm\16m\u0680\13m\3n\3n\3n\3n\7n\u0686")
        buf.write(u"\nn\fn\16n\u0689\13n\3o\3o\3o\3o\3o\5o\u0690\no\3p\3")
        buf.write(u"p\3p\3p\7p\u0696\np\fp\16p\u0699\13p\3q\3q\3q\5q\u069e")
        buf.write(u"\nq\3r\3r\3r\3r\3r\3r\3r\3r\3r\3r\5r\u06aa\nr\3s\3s\5")
        buf.write(u"s\u06ae\ns\3t\3t\3t\3t\3t\3t\7t\u06b6\nt\ft\16t\u06b9")
        buf.write(u"\13t\3u\3u\5u\u06bd\nu\3v\3v\3v\3v\5v\u06c3\nv\3v\3v")
        buf.write(u"\3v\7v\u06c8\nv\fv\16v\u06cb\13v\3v\3v\5v\u06cf\nv\3")
        buf.write(u"w\3w\3w\7w\u06d4\nw\fw\16w\u06d7\13w\3x\3x\3x\7x\u06dc")
        buf.write(u"\nx\fx\16x\u06df\13x\3y\3y\3y\3y\5y\u06e5\ny\3z\3z\3")
        buf.write(u"{\3{\3{\3{\7{\u06ed\n{\f{\16{\u06f0\13{\3|\3|\3|\3|\3")
        buf.write(u"|\3|\3|\3|\3|\3|\5|\u06fc\n|\3}\3}\5}\u0700\n}\3}\5}")
        buf.write(u"\u0703\n}\3~\3~\5~\u0707\n~\3~\5~\u070a\n~\3\177\3\177")
        buf.write(u"\3\177\3\177\7\177\u0710\n\177\f\177\16\177\u0713\13")
        buf.write(u"\177\3\u0080\3\u0080\3\u0080\3\u0080\7\u0080\u0719\n")
        buf.write(u"\u0080\f\u0080\16\u0080\u071c\13\u0080\3\u0081\3\u0081")
        buf.write(u"\3\u0081\3\u0081\7\u0081\u0722\n\u0081\f\u0081\16\u0081")
        buf.write(u"\u0725\13\u0081\3\u0082\3\u0082\3\u0082\3\u0082\7\u0082")
        buf.write(u"\u072b\n\u0082\f\u0082\16\u0082\u072e\13\u0082\3\u0083")
        buf.write(u"\3\u0083\3\u0083\3\u0083\3\u0083\3\u0083\3\u0083\3\u0083")
        buf.write(u"\3\u0083\3\u0083\3\u0083\3\u0083\3\u0083\3\u0083\5\u0083")
        buf.write(u"\u073e\n\u0083\3\u0084\3\u0084\3\u0084\3\u0084\3\u0084")
        buf.write(u"\3\u0084\3\u0084\3\u0084\3\u0084\3\u0084\3\u0084\3\u0084")
        buf.write(u"\3\u0084\3\u0084\3\u0084\5\u0084\u074f\n\u0084\3\u0085")
        buf.write(u"\3\u0085\3\u0085\7\u0085\u0754\n\u0085\f\u0085\16\u0085")
        buf.write(u"\u0757\13\u0085\3\u0086\3\u0086\3\u0086\3\u0086\5\u0086")
        buf.write(u"\u075d\n\u0086\3\u0087\3\u0087\3\u0088\3\u0088\3\u0088")
        buf.write(u"\3\u0088\3\u0089\3\u0089\5\u0089\u0767\n\u0089\3\u008a")
        buf.write(u"\3\u008a\3\u008a\3\u008a\3\u008a\5\u008a\u076e\n\u008a")
        buf.write(u"\3\u008b\5\u008b\u0771\n\u008b\3\u008b\3\u008b\5\u008b")
        buf.write(u"\u0775\n\u008b\3\u008b\3\u008b\3\u008c\5\u008c\u077a")
        buf.write(u"\n\u008c\3\u008c\3\u008c\5\u008c\u077e\n\u008c\3\u008c")
        buf.write(u"\3\u008c\3\u008d\3\u008d\3\u008d\3\u008d\3\u008d\7\u008d")
        buf.write(u"\u0787\n\u008d\f\u008d\16\u008d\u078a\13\u008d\5\u008d")
        buf.write(u"\u078c\n\u008d\3\u008e\3\u008e\3\u008e\7\u008e\u0791")
        buf.write(u"\n\u008e\f\u008e\16\u008e\u0794\13\u008e\3\u008f\3\u008f")
        buf.write(u"\3\u008f\3\u008f\3\u0090\3\u0090\3\u0090\3\u0090\3\u0090")
        buf.write(u"\3\u0090\3\u0090\3\u0090\3\u0090\5\u0090\u07a3\n\u0090")
        buf.write(u"\3\u0091\3\u0091\3\u0091\3\u0091\3\u0092\3\u0092\3\u0092")
        buf.write(u"\3\u0092\3\u0092\7\u0092\u07ae\n\u0092\f\u0092\16\u0092")
        buf.write(u"\u07b1\13\u0092\3\u0093\3\u0093\3\u0093\3\u0093\5\u0093")
        buf.write(u"\u07b7\n\u0093\3\u0094\3\u0094\3\u0094\3\u0094\3\u0094")
        buf.write(u"\3\u0095\3\u0095\3\u0095\3\u0095\3\u0095\3\u0096\3\u0096")
        buf.write(u"\3\u0096\7\u0096\u07c6\n\u0096\f\u0096\16\u0096\u07c9")
        buf.write(u"\13\u0096\3\u0097\3\u0097\3\u0097\7\u0097\u07ce\n\u0097")
        buf.write(u"\f\u0097\16\u0097\u07d1\13\u0097\3\u0097\5\u0097\u07d4")
        buf.write(u"\n\u0097\3\u0098\3\u0098\3\u0098\3\u0098\3\u0098\3\u0098")
        buf.write(u"\5\u0098\u07dc\n\u0098\3\u0099\3\u0099\3\u009a\3\u009a")
        buf.write(u"\3\u009a\3\u009b\3\u009b\3\u009b\3\u009c\3\u009c\3\u009c")
        buf.write(u"\3\u009d\3\u009d\3\u009d\3\u009e\3\u009e\3\u009e\3\u009f")
        buf.write(u"\3\u009f\3\u00a0\3\u00a0\3\u00a1\3\u00a1\3\u00a2\3\u00a2")
        buf.write(u"\3\u00a3\3\u00a3\3\u00a4\3\u00a4\3\u00a4\3\u00a4\3\u00a4")
        buf.write(u"\3\u00a4\3\u00a4\5\u00a4\u0800\n\u00a4\3\u00a5\3\u00a5")
        buf.write(u"\3\u00a5\3\u00a5\3\u00a5\7\u00a5\u0807\n\u00a5\f\u00a5")
        buf.write(u"\16\u00a5\u080a\13\u00a5\3\u00a6\3\u00a6\3\u00a6\3\u00a6")
        buf.write(u"\3\u00a6\3\u00a6\3\u00a6\5\u00a6\u0813\n\u00a6\3\u00a7")
        buf.write(u"\3\u00a7\3\u00a8\3\u00a8\3\u00a8\3\u00a9\3\u00a9\3\u00a9")
        buf.write(u"\3\u00a9\3\u00a9\5\u00a9\u081f\n\u00a9\3\u00aa\3\u00aa")
        buf.write(u"\3\u00aa\5\u00aa\u0824\n\u00aa\3\u00aa\3\u00aa\3\u00ab")
        buf.write(u"\3\u00ab\3\u00ab\3\u00ab\3\u00ab\3\u00ab\7\u00ab\u082e")
        buf.write(u"\n\u00ab\f\u00ab\16\u00ab\u0831\13\u00ab\3\u00ac\3\u00ac")
        buf.write(u"\3\u00ac\3\u00ac\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ae")
        buf.write(u"\3\u00ae\3\u00af\3\u00af\3\u00af\3\u00af\3\u00af\5\u00af")
        buf.write(u"\u0842\n\u00af\3\u00b0\3\u00b0\3\u00b1\3\u00b1\3\u00b1")
        buf.write(u"\5\u00b1\u0849\n\u00b1\3\u00b2\3\u00b2\3\u00b2\3\u00b2")
        buf.write(u"\3\u00b2\7\u00b2\u0850\n\u00b2\f\u00b2\16\u00b2\u0853")
        buf.write(u"\13\u00b2\3\u00b3\3\u00b3\3\u00b3\3\u00b3\3\u00b3\5\u00b3")
        buf.write(u"\u085a\n\u00b3\3\u00b4\3\u00b4\3\u00b5\3\u00b5\3\u00b5")
        buf.write(u"\3\u00b5\3\u00b5\3\u00b5\5\u00b5\u0864\n\u00b5\3\u00b6")
        buf.write(u"\3\u00b6\3\u00b6\5\u00b6\u0869\n\u00b6\3\u00b6\3\u00b6")
        buf.write(u"\3\u00b7\3\u00b7\3\u00b7\3\u00b7\3\u00b7\3\u00b7\5\u00b7")
        buf.write(u"\u0873\n\u00b7\3\u00b8\3\u00b8\3\u00b8\3\u00b8\3\u00b8")
        buf.write(u"\3\u00b8\7\u00b8\u087b\n\u00b8\f\u00b8\16\u00b8\u087e")
        buf.write(u"\13\u00b8\3\u00b9\3\u00b9\3\u00b9\3\u00b9\3\u00b9\3\u00b9")
        buf.write(u"\3\u00b9\3\u00b9\3\u00b9\3\u00b9\3\u00b9\7\u00b9\u088b")
        buf.write(u"\n\u00b9\f\u00b9\16\u00b9\u088e\13\u00b9\3\u00ba\3\u00ba")
        buf.write(u"\3\u00ba\3\u00ba\3\u00bb\3\u00bb\3\u00bb\5\u00bb\u0897")
        buf.write(u"\n\u00bb\3\u00bb\3\u00bb\3\u00bb\7\u00bb\u089c\n\u00bb")
        buf.write(u"\f\u00bb\16\u00bb\u089f\13\u00bb\3\u00bc\3\u00bc\3\u00bc")
        buf.write(u"\3\u00bc\3\u00bc\5\u00bc\u08a6\n\u00bc\3\u00bd\3\u00bd")
        buf.write(u"\3\u00be\3\u00be\3\u00be\3\u00be\3\u00be\3\u00be\3\u00be")
        buf.write(u"\5\u00be\u08b1\n\u00be\3\u00bf\3\u00bf\3\u00bf\3\u00bf")
        buf.write(u"\3\u00bf\7\u00bf\u08b8\n\u00bf\f\u00bf\16\u00bf\u08bb")
        buf.write(u"\13\u00bf\3\u00c0\3\u00c0\3\u00c0\3\u00c0\3\u00c0\5\u00c0")
        buf.write(u"\u08c2\n\u00c0\3\u00c1\3\u00c1\3\u00c2\3\u00c2\3\u00c2")
        buf.write(u"\3\u00c3\3\u00c3\3\u00c3\5\u00c3\u08cc\n\u00c3\3\u00c4")
        buf.write(u"\3\u00c4\3\u00c4\5\u00c4\u08d1\n\u00c4\3\u00c4\3\u00c4")
        buf.write(u"\3\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c5\7\u00c5")
        buf.write(u"\u08db\n\u00c5\f\u00c5\16\u00c5\u08de\13\u00c5\3\u00c6")
        buf.write(u"\3\u00c6\3\u00c6\3\u00c6\3\u00c7\3\u00c7\3\u00c7\3\u00c7")
        buf.write(u"\3\u00c8\3\u00c8\3\u00c8\3\u00c8\3\u00c8\3\u00c8\7\u00c8")
        buf.write(u"\u08ee\n\u00c8\f\u00c8\16\u00c8\u08f1\13\u00c8\3\u00c9")
        buf.write(u"\3\u00c9\3\u00c9\3\u00c9\3\u00c9\7\u00c9\u08f8\n\u00c9")
        buf.write(u"\f\u00c9\16\u00c9\u08fb\13\u00c9\3\u00ca\3\u00ca\3\u00ca")
        buf.write(u"\3\u00ca\3\u00ca\5\u00ca\u0902\n\u00ca\3\u00cb\3\u00cb")
        buf.write(u"\3\u00cc\3\u00cc\3\u00cc\3\u00cc\3\u00cc\3\u00cc\3\u00cc")
        buf.write(u"\5\u00cc\u090d\n\u00cc\3\u00cd\3\u00cd\3\u00cd\3\u00cd")
        buf.write(u"\3\u00cd\7\u00cd\u0914\n\u00cd\f\u00cd\16\u00cd\u0917")
        buf.write(u"\13\u00cd\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\5\u00ce")
        buf.write(u"\u091e\n\u00ce\3\u00cf\3\u00cf\3\u00d0\3\u00d0\3\u00d0")
        buf.write(u"\3\u00d1\3\u00d1\3\u00d1\5\u00d1\u0928\n\u00d1\3\u00d2")
        buf.write(u"\3\u00d2\3\u00d2\5\u00d2\u092d\n\u00d2\3\u00d2\3\u00d2")
        buf.write(u"\3\u00d3\3\u00d3\3\u00d3\3\u00d3\3\u00d3\3\u00d3\7\u00d3")
        buf.write(u"\u0937\n\u00d3\f\u00d3\16\u00d3\u093a\13\u00d3\3\u00d4")
        buf.write(u"\3\u00d4\3\u00d4\3\u00d4\3\u00d5\3\u00d5\3\u00d5\3\u00d5")
        buf.write(u"\3\u00d6\3\u00d6\3\u00d6\5\u00d6\u0947\n\u00d6\3\u00d6")
        buf.write(u"\3\u00d6\3\u00d6\7\u00d6\u094c\n\u00d6\f\u00d6\16\u00d6")
        buf.write(u"\u094f\13\u00d6\3\u00d7\3\u00d7\3\u00d7\3\u00d7\3\u00d7")
        buf.write(u"\5\u00d7\u0956\n\u00d7\3\u00d8\3\u00d8\3\u00d9\3\u00d9")
        buf.write(u"\5\u00d9\u095c\n\u00d9\3\u00da\3\u00da\3\u00da\5\u00da")
        buf.write(u"\u0961\n\u00da\3\u00da\3\u00da\5\u00da\u0965\n\u00da")
        buf.write(u"\3\u00db\3\u00db\5\u00db\u0969\n\u00db\3\u00db\3\u00db")
        buf.write(u"\3\u00dc\3\u00dc\3\u00dc\5\u00dc\u0970\n\u00dc\3\u00dd")
        buf.write(u"\3\u00dd\3\u00dd\3\u00dd\3\u00de\3\u00de\3\u00de\7\u00de")
        buf.write(u"\u0979\n\u00de\f\u00de\16\u00de\u097c\13\u00de\3\u00de")
        buf.write(u"\3\u00de\3\u00de\3\u00df\3\u00df\3\u00df\7\u00df\u0984")
        buf.write(u"\n\u00df\f\u00df\16\u00df\u0987\13\u00df\3\u00df\3\u00df")
        buf.write(u"\3\u00e0\3\u00e0\3\u00e0\3\u00e0\3\u00e0\3\u00e1\3\u00e1")
        buf.write(u"\3\u00e1\7\u00e1\u0993\n\u00e1\f\u00e1\16\u00e1\u0996")
        buf.write(u"\13\u00e1\3\u00e2\3\u00e2\7\u00e2\u099a\n\u00e2\f\u00e2")
        buf.write(u"\16\u00e2\u099d\13\u00e2\3\u00e3\3\u00e3\3\u00e3\5\u00e3")
        buf.write(u"\u09a2\n\u00e3\3\u00e4\3\u00e4\3\u00e4\3\u00e4\3\u00e4")
        buf.write(u"\5\u00e4\u09a9\n\u00e4\3\u00e5\6\u00e5\u09ac\n\u00e5")
        buf.write(u"\r\u00e5\16\u00e5\u09ad\3\u00e6\3\u00e6\3\u00e6\3\u00e6")
        buf.write(u"\5\u00e6\u09b4\n\u00e6\3\u00e6\5\u00e6\u09b7\n\u00e6")
        buf.write(u"\3\u00e7\6\u00e7\u09ba\n\u00e7\r\u00e7\16\u00e7\u09bb")
        buf.write(u"\3\u00e8\3\u00e8\6\u00e8\u09c0\n\u00e8\r\u00e8\16\u00e8")
        buf.write(u"\u09c1\3\u00e8\3\u00e8\3\u00e9\3\u00e9\3\u00e9\3\u00e9")
        buf.write(u"\3\u00e9\3\u00ea\3\u00ea\3\u00ea\3\u00ea\5\u00ea\u09cf")
        buf.write(u"\n\u00ea\3\u00ea\3\u00ea\6\u00ea\u09d3\n\u00ea\r\u00ea")
        buf.write(u"\16\u00ea\u09d4\7\u00ea\u09d7\n\u00ea\f\u00ea\16\u00ea")
        buf.write(u"\u09da\13\u00ea\3\u00eb\3\u00eb\3\u00eb\3\u00eb\3\u00eb")
        buf.write(u"\5\u00eb\u09e1\n\u00eb\3\u00ec\6\u00ec\u09e4\n\u00ec")
        buf.write(u"\r\u00ec\16\u00ec\u09e5\3\u00ec\2\31(@T`dr\u00a8\u00d8")
        buf.write(u"\u0122\u0148\u0154\u0162\u016e\u0170\u0174\u017c\u0188")
        buf.write(u"\u018e\u0190\u0198\u01a4\u01aa\u01d2\u00ed\2\4\6\b\n")
        buf.write(u"\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:")
        buf.write(u"<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084")
        buf.write(u"\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096")
        buf.write(u"\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4\u00a6\u00a8")
        buf.write(u"\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4\u00b6\u00b8\u00ba")
        buf.write(u"\u00bc\u00be\u00c0\u00c2\u00c4\u00c6\u00c8\u00ca\u00cc")
        buf.write(u"\u00ce\u00d0\u00d2\u00d4\u00d6\u00d8\u00da\u00dc\u00de")
        buf.write(u"\u00e0\u00e2\u00e4\u00e6\u00e8\u00ea\u00ec\u00ee\u00f0")
        buf.write(u"\u00f2\u00f4\u00f6\u00f8\u00fa\u00fc\u00fe\u0100\u0102")
        buf.write(u"\u0104\u0106\u0108\u010a\u010c\u010e\u0110\u0112\u0114")
        buf.write(u"\u0116\u0118\u011a\u011c\u011e\u0120\u0122\u0124\u0126")
        buf.write(u"\u0128\u012a\u012c\u012e\u0130\u0132\u0134\u0136\u0138")
        buf.write(u"\u013a\u013c\u013e\u0140\u0142\u0144\u0146\u0148\u014a")
        buf.write(u"\u014c\u014e\u0150\u0152\u0154\u0156\u0158\u015a\u015c")
        buf.write(u"\u015e\u0160\u0162\u0164\u0166\u0168\u016a\u016c\u016e")
        buf.write(u"\u0170\u0172\u0174\u0176\u0178\u017a\u017c\u017e\u0180")
        buf.write(u"\u0182\u0184\u0186\u0188\u018a\u018c\u018e\u0190\u0192")
        buf.write(u"\u0194\u0196\u0198\u019a\u019c\u019e\u01a0\u01a2\u01a4")
        buf.write(u"\u01a6\u01a8\u01aa\u01ac\u01ae\u01b0\u01b2\u01b4\u01b6")
        buf.write(u"\u01b8\u01ba\u01bc\u01be\u01c0\u01c2\u01c4\u01c6\u01c8")
        buf.write(u"\u01ca\u01cc\u01ce\u01d0\u01d2\u01d4\u01d6\2\17\3\2V")
        buf.write(u"W\3\2\"#\4\2\u0093\u0093\u00a8\u00a8\4\2\u008f\u008f")
        buf.write(u"\u0097\u0097\4\2MM^^\4\2\13\20\64\u00a1\4\2\'\'yy\r\2")
        buf.write(u"\64=CCFF||\177\177\u0089\u0089\u008f\u008f\u0096\u0096")
        buf.write(u"\u00a1\u00a1\u00a6\u00a8\u00aa\u00aa\13\2\64=CCFF||\177")
        buf.write(u"\177\u0089\u0089\u0096\u0097\u00a1\u00a1\u00a6\u00a8")
        buf.write(u"\f\2\64=CCFF||\177\177\u0089\u0089\u008f\u008f\u0096")
        buf.write(u"\u0096\u00a1\u00a1\u00a6\u00aa\f\2\64=CCFF||\177\177")
        buf.write(u"\u0089\u0089\u008f\u008f\u0096\u0096\u00a1\u00a1\u00a6")
        buf.write(u"\u00a8\5\2\32\33((**\5\2\t\t\21\22\32\33\2\u0a69\2\u01d8")
        buf.write(u"\3\2\2\2\4\u01e9\3\2\2\2\6\u01f3\3\2\2\2\b\u01f7\3\2")
        buf.write(u"\2\2\n\u01ff\3\2\2\2\f\u021b\3\2\2\2\16\u0222\3\2\2\2")
        buf.write(u"\20\u0231\3\2\2\2\22\u023e\3\2\2\2\24\u0254\3\2\2\2\26")
        buf.write(u"\u0261\3\2\2\2\30\u0263\3\2\2\2\32\u0272\3\2\2\2\34\u027c")
        buf.write(u"\3\2\2\2\36\u0289\3\2\2\2 \u0293\3\2\2\2\"\u02a1\3\2")
        buf.write(u"\2\2$\u02b6\3\2\2\2&\u02ca\3\2\2\2(\u02d2\3\2\2\2*\u02de")
        buf.write(u"\3\2\2\2,\u02ea\3\2\2\2.\u02fa\3\2\2\2\60\u030d\3\2\2")
        buf.write(u"\2\62\u0320\3\2\2\2\64\u0322\3\2\2\2\66\u0342\3\2\2\2")
        buf.write(u"8\u0344\3\2\2\2:\u035c\3\2\2\2<\u035e\3\2\2\2>\u036a")
        buf.write(u"\3\2\2\2@\u036c\3\2\2\2B\u037c\3\2\2\2D\u037e\3\2\2\2")
        buf.write(u"F\u0385\3\2\2\2H\u038c\3\2\2\2J\u03ac\3\2\2\2L\u03ae")
        buf.write(u"\3\2\2\2N\u03bb\3\2\2\2P\u03c4\3\2\2\2R\u03cb\3\2\2\2")
        buf.write(u"T\u03df\3\2\2\2V\u03f7\3\2\2\2X\u03fa\3\2\2\2Z\u042b")
        buf.write(u"\3\2\2\2\\\u042d\3\2\2\2^\u042f\3\2\2\2`\u0447\3\2\2")
        buf.write(u"\2b\u04bb\3\2\2\2d\u04bd\3\2\2\2f\u04cf\3\2\2\2h\u04de")
        buf.write(u"\3\2\2\2j\u04e0\3\2\2\2l\u04e7\3\2\2\2n\u04fe\3\2\2\2")
        buf.write(u"p\u0500\3\2\2\2r\u050a\3\2\2\2t\u0514\3\2\2\2v\u051a")
        buf.write(u"\3\2\2\2x\u051f\3\2\2\2z\u0543\3\2\2\2|\u0545\3\2\2\2")
        buf.write(u"~\u0554\3\2\2\2\u0080\u0560\3\2\2\2\u0082\u0562\3\2\2")
        buf.write(u"\2\u0084\u0569\3\2\2\2\u0086\u056d\3\2\2\2\u0088\u0572")
        buf.write(u"\3\2\2\2\u008a\u057b\3\2\2\2\u008c\u0580\3\2\2\2\u008e")
        buf.write(u"\u0583\3\2\2\2\u0090\u0588\3\2\2\2\u0092\u0596\3\2\2")
        buf.write(u"\2\u0094\u05a1\3\2\2\2\u0096\u05a5\3\2\2\2\u0098\u05a7")
        buf.write(u"\3\2\2\2\u009a\u05b0\3\2\2\2\u009c\u05b9\3\2\2\2\u009e")
        buf.write(u"\u05cb\3\2\2\2\u00a0\u05ce\3\2\2\2\u00a2\u05d7\3\2\2")
        buf.write(u"\2\u00a4\u05df\3\2\2\2\u00a6\u05e7\3\2\2\2\u00a8\u05f9")
        buf.write(u"\3\2\2\2\u00aa\u060a\3\2\2\2\u00ac\u061c\3\2\2\2\u00ae")
        buf.write(u"\u061e\3\2\2\2\u00b0\u0621\3\2\2\2\u00b2\u0625\3\2\2")
        buf.write(u"\2\u00b4\u062a\3\2\2\2\u00b6\u062e\3\2\2\2\u00b8\u0630")
        buf.write(u"\3\2\2\2\u00ba\u063a\3\2\2\2\u00bc\u063e\3\2\2\2\u00be")
        buf.write(u"\u0640\3\2\2\2\u00c0\u0644\3\2\2\2\u00c2\u064a\3\2\2")
        buf.write(u"\2\u00c4\u064c\3\2\2\2\u00c6\u064e\3\2\2\2\u00c8\u0650")
        buf.write(u"\3\2\2\2\u00ca\u0652\3\2\2\2\u00cc\u0654\3\2\2\2\u00ce")
        buf.write(u"\u0661\3\2\2\2\u00d0\u0665\3\2\2\2\u00d2\u0667\3\2\2")
        buf.write(u"\2\u00d4\u066c\3\2\2\2\u00d6\u0671\3\2\2\2\u00d8\u0673")
        buf.write(u"\3\2\2\2\u00da\u0681\3\2\2\2\u00dc\u068f\3\2\2\2\u00de")
        buf.write(u"\u0691\3\2\2\2\u00e0\u069d\3\2\2\2\u00e2\u06a9\3\2\2")
        buf.write(u"\2\u00e4\u06ab\3\2\2\2\u00e6\u06af\3\2\2\2\u00e8\u06ba")
        buf.write(u"\3\2\2\2\u00ea\u06be\3\2\2\2\u00ec\u06d0\3\2\2\2\u00ee")
        buf.write(u"\u06d8\3\2\2\2\u00f0\u06e4\3\2\2\2\u00f2\u06e6\3\2\2")
        buf.write(u"\2\u00f4\u06e8\3\2\2\2\u00f6\u06fb\3\2\2\2\u00f8\u06fd")
        buf.write(u"\3\2\2\2\u00fa\u0704\3\2\2\2\u00fc\u070b\3\2\2\2\u00fe")
        buf.write(u"\u0714\3\2\2\2\u0100\u071d\3\2\2\2\u0102\u0726\3\2\2")
        buf.write(u"\2\u0104\u073d\3\2\2\2\u0106\u074e\3\2\2\2\u0108\u0750")
        buf.write(u"\3\2\2\2\u010a\u075c\3\2\2\2\u010c\u075e\3\2\2\2\u010e")
        buf.write(u"\u0760\3\2\2\2\u0110\u0766\3\2\2\2\u0112\u076d\3\2\2")
        buf.write(u"\2\u0114\u0770\3\2\2\2\u0116\u0779\3\2\2\2\u0118\u0781")
        buf.write(u"\3\2\2\2\u011a\u078d\3\2\2\2\u011c\u0795\3\2\2\2\u011e")
        buf.write(u"\u07a2\3\2\2\2\u0120\u07a4\3\2\2\2\u0122\u07a8\3\2\2")
        buf.write(u"\2\u0124\u07b6\3\2\2\2\u0126\u07b8\3\2\2\2\u0128\u07bd")
        buf.write(u"\3\2\2\2\u012a\u07c2\3\2\2\2\u012c\u07ca\3\2\2\2\u012e")
        buf.write(u"\u07db\3\2\2\2\u0130\u07dd\3\2\2\2\u0132\u07df\3\2\2")
        buf.write(u"\2\u0134\u07e2\3\2\2\2\u0136\u07e5\3\2\2\2\u0138\u07e8")
        buf.write(u"\3\2\2\2\u013a\u07eb\3\2\2\2\u013c\u07ee\3\2\2\2\u013e")
        buf.write(u"\u07f0\3\2\2\2\u0140\u07f2\3\2\2\2\u0142\u07f4\3\2\2")
        buf.write(u"\2\u0144\u07f6\3\2\2\2\u0146\u07ff\3\2\2\2\u0148\u0801")
        buf.write(u"\3\2\2\2\u014a\u0812\3\2\2\2\u014c\u0814\3\2\2\2\u014e")
        buf.write(u"\u0816\3\2\2\2\u0150\u081e\3\2\2\2\u0152\u0820\3\2\2")
        buf.write(u"\2\u0154\u0827\3\2\2\2\u0156\u0832\3\2\2\2\u0158\u0836")
        buf.write(u"\3\2\2\2\u015a\u083a\3\2\2\2\u015c\u0841\3\2\2\2\u015e")
        buf.write(u"\u0843\3\2\2\2\u0160\u0848\3\2\2\2\u0162\u084a\3\2\2")
        buf.write(u"\2\u0164\u0859\3\2\2\2\u0166\u085b\3\2\2\2\u0168\u0863")
        buf.write(u"\3\2\2\2\u016a\u0865\3\2\2\2\u016c\u0872\3\2\2\2\u016e")
        buf.write(u"\u0874\3\2\2\2\u0170\u087f\3\2\2\2\u0172\u088f\3\2\2")
        buf.write(u"\2\u0174\u0896\3\2\2\2\u0176\u08a5\3\2\2\2\u0178\u08a7")
        buf.write(u"\3\2\2\2\u017a\u08b0\3\2\2\2\u017c\u08b2\3\2\2\2\u017e")
        buf.write(u"\u08c1\3\2\2\2\u0180\u08c3\3\2\2\2\u0182\u08c5\3\2\2")
        buf.write(u"\2\u0184\u08cb\3\2\2\2\u0186\u08cd\3\2\2\2\u0188\u08d4")
        buf.write(u"\3\2\2\2\u018a\u08df\3\2\2\2\u018c\u08e3\3\2\2\2\u018e")
        buf.write(u"\u08e7\3\2\2\2\u0190\u08f2\3\2\2\2\u0192\u0901\3\2\2")
        buf.write(u"\2\u0194\u0903\3\2\2\2\u0196\u090c\3\2\2\2\u0198\u090e")
        buf.write(u"\3\2\2\2\u019a\u091d\3\2\2\2\u019c\u091f\3\2\2\2\u019e")
        buf.write(u"\u0921\3\2\2\2\u01a0\u0927\3\2\2\2\u01a2\u0929\3\2\2")
        buf.write(u"\2\u01a4\u0930\3\2\2\2\u01a6\u093b\3\2\2\2\u01a8\u093f")
        buf.write(u"\3\2\2\2\u01aa\u0946\3\2\2\2\u01ac\u0955\3\2\2\2\u01ae")
        buf.write(u"\u0957\3\2\2\2\u01b0\u095b\3\2\2\2\u01b2\u0964\3\2\2")
        buf.write(u"\2\u01b4\u0966\3\2\2\2\u01b6\u096f\3\2\2\2\u01b8\u0971")
        buf.write(u"\3\2\2\2\u01ba\u0975\3\2\2\2\u01bc\u0980\3\2\2\2\u01be")
        buf.write(u"\u098a\3\2\2\2\u01c0\u098f\3\2\2\2\u01c2\u0997\3\2\2")
        buf.write(u"\2\u01c4\u099e\3\2\2\2\u01c6\u09a8\3\2\2\2\u01c8\u09ab")
        buf.write(u"\3\2\2\2\u01ca\u09b6\3\2\2\2\u01cc\u09b9\3\2\2\2\u01ce")
        buf.write(u"\u09bd\3\2\2\2\u01d0\u09c5\3\2\2\2\u01d2\u09ce\3\2\2")
        buf.write(u"\2\u01d4\u09e0\3\2\2\2\u01d6\u09e3\3\2\2\2\u01d8\u01d9")
        buf.write(u"\7c\2\2\u01d9\u01da\5\u00c8e\2\u01da\u01e1\7\26\2\2\u01db")
        buf.write(u"\u01de\5\u00c8e\2\u01dc\u01dd\7\23\2\2\u01dd\u01df\5")
        buf.write(u"\u00eex\2\u01de\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df")
        buf.write(u"\u01e2\3\2\2\2\u01e0\u01e2\5\u00eex\2\u01e1\u01db\3\2")
        buf.write(u"\2\2\u01e1\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u01e4")
        buf.write(u"\7\27\2\2\u01e4\u01e5\7\21\2\2\u01e5\u01e6\5\u0088E\2")
        buf.write(u"\u01e6\u01e7\5\u009aN\2\u01e7\u01e8\5\u008aF\2\u01e8")
        buf.write(u"\3\3\2\2\2\u01e9\u01ea\7c\2\2\u01ea\u01eb\5\u00c8e\2")
        buf.write(u"\u01eb\u01ec\7\26\2\2\u01ec\u01ed\5\u00acW\2\u01ed\u01ee")
        buf.write(u"\7\27\2\2\u01ee\u01ef\7\21\2\2\u01ef\u01f0\5\u0088E\2")
        buf.write(u"\u01f0\u01f1\5\u0098M\2\u01f1\u01f2\5\u008aF\2\u01f2")
        buf.write(u"\5\3\2\2\2\u01f3\u01f4\5\u00caf\2\u01f4\u01f5\7-\2\2")
        buf.write(u"\u01f5\u01f6\5`\61\2\u01f6\7\3\2\2\2\u01f7\u01f8\5\u00ca")
        buf.write(u"f\2\u01f8\u01fa\7\26\2\2\u01f9\u01fb\5r:\2\u01fa\u01f9")
        buf.write(u"\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc")
        buf.write(u"\u01fd\7\27\2\2\u01fd\t\3\2\2\2\u01fe\u0200\7\u0093\2")
        buf.write(u"\2\u01ff\u01fe\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0201")
        buf.write(u"\3\2\2\2\u0201\u0202\7N\2\2\u0202\u0203\5\u00c6d\2\u0203")
        buf.write(u"\u0204\7\26\2\2\u0204\u0205\5\u00a8U\2\u0205\u0206\7")
        buf.write(u"\27\2\2\u0206\u0207\7\21\2\2\u0207\u0217\5\u0088E\2\u0208")
        buf.write(u"\u0218\7\u0087\2\2\u0209\u020d\5\u009eP\2\u020a\u020b")
        buf.write(u"\5\u0086D\2\u020b\u020c\5\f\7\2\u020c\u020e\3\2\2\2\u020d")
        buf.write(u"\u020a\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u0216\3\2\2")
        buf.write(u"\2\u020f\u0213\5\f\7\2\u0210\u0211\5\u0086D\2\u0211\u0212")
        buf.write(u"\5\u009eP\2\u0212\u0214\3\2\2\2\u0213\u0210\3\2\2\2\u0213")
        buf.write(u"\u0214\3\2\2\2\u0214\u0216\3\2\2\2\u0215\u0209\3\2\2")
        buf.write(u"\2\u0215\u020f\3\2\2\2\u0216\u0218\3\2\2\2\u0217\u0208")
        buf.write(u"\3\2\2\2\u0217\u0215\3\2\2\2\u0218\u0219\3\2\2\2\u0219")
        buf.write(u"\u021a\5\u008aF\2\u021a\13\3\2\2\2\u021b\u021c\7s\2\2")
        buf.write(u"\u021c\u021e\7\26\2\2\u021d\u021f\5\u00ecw\2\u021e\u021d")
        buf.write(u"\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u0220\3\2\2\2\u0220")
        buf.write(u"\u0221\7\27\2\2\u0221\r\3\2\2\2\u0222\u0223\7\u009c\2")
        buf.write(u"\2\u0223\u0224\5\u00c8e\2\u0224\u0226\7\26\2\2\u0225")
        buf.write(u"\u0227\5\u00c8e\2\u0226\u0225\3\2\2\2\u0226\u0227\3\2")
        buf.write(u"\2\2\u0227\u0228\3\2\2\2\u0228\u0229\7\27\2\2\u0229\u022a")
        buf.write(u"\7\21\2\2\u022a\u022d\5\u0088E\2\u022b\u022e\5\u00da")
        buf.write(u"n\2\u022c\u022e\7\u0087\2\2\u022d\u022b\3\2\2\2\u022d")
        buf.write(u"\u022c\3\2\2\2\u022e\u022f\3\2\2\2\u022f\u0230\5\u008a")
        buf.write(u"F\2\u0230\17\3\2\2\2\u0231\u0232\7{\2\2\u0232\u0233\7")
        buf.write(u"\u009c\2\2\u0233\u0234\5\u00c8e\2\u0234\u0235\7\26\2")
        buf.write(u"\2\u0235\u0236\7\27\2\2\u0236\u0237\7\21\2\2\u0237\u0238")
        buf.write(u"\5\u0088E\2\u0238\u0239\5&\24\2\u0239\u023a\5\u0086D")
        buf.write(u"\2\u023a\u023b\5\u00dep\2\u023b\u023c\5\u008aF\2\u023c")
        buf.write(u"\21\3\2\2\2\u023d\u023f\7\u0093\2\2\u023e\u023d\3\2\2")
        buf.write(u"\2\u023e\u023f\3\2\2\2\u023f\u0240\3\2\2\2\u0240\u0241")
        buf.write(u"\t\2\2\2\u0241\u0242\5\u00c8e\2\u0242\u0249\7\26\2\2")
        buf.write(u"\u0243\u024a\5\26\f\2\u0244\u024a\5\u00eex\2\u0245\u0246")
        buf.write(u"\5\26\f\2\u0246\u0247\7\23\2\2\u0247\u0248\5\u00eex\2")
        buf.write(u"\u0248\u024a\3\2\2\2\u0249\u0243\3\2\2\2\u0249\u0244")
        buf.write(u"\3\2\2\2\u0249\u0245\3\2\2\2\u024a\u024b\3\2\2\2\u024b")
        buf.write(u"\u024c\7\27\2\2\u024c\u024d\7\21\2\2\u024d\u0250\5\u0088")
        buf.write(u"E\2\u024e\u0251\5\u00dan\2\u024f\u0251\7\u0087\2\2\u0250")
        buf.write(u"\u024e\3\2\2\2\u0250\u024f\3\2\2\2\u0251\u0252\3\2\2")
        buf.write(u"\2\u0252\u0253\5\u008aF\2\u0253\23\3\2\2\2\u0254\u0255")
        buf.write(u"\7\u0091\2\2\u0255\u0256\5\u00c8e\2\u0256\u0257\7\26")
        buf.write(u"\2\2\u0257\u0258\5\u00eex\2\u0258\u0259\7\27\2\2\u0259")
        buf.write(u"\u025a\7\21\2\2\u025a\u025d\5\u0088E\2\u025b\u025e\5")
        buf.write(u"\u00dan\2\u025c\u025e\7\u0087\2\2\u025d\u025b\3\2\2\2")
        buf.write(u"\u025d\u025c\3\2\2\2\u025e\u025f\3\2\2\2\u025f\u0260")
        buf.write(u"\5\u008aF\2\u0260\25\3\2\2\2\u0261\u0262\5\u00b8]\2\u0262")
        buf.write(u"\27\3\2\2\2\u0263\u0264\7Z\2\2\u0264\u0265\7\u0083\2")
        buf.write(u"\2\u0265\u0266\5\u012e\u0098\2\u0266\u0267\7\26\2\2\u0267")
        buf.write(u"\u0268\5\u00d0i\2\u0268\u026b\7\27\2\2\u0269\u026a\7")
        buf.write(u"\63\2\2\u026a\u026c\5\u00a8U\2\u026b\u0269\3\2\2\2\u026b")
        buf.write(u"\u026c\3\2\2\2\u026c\u026d\3\2\2\2\u026d\u026e\7\21\2")
        buf.write(u"\2\u026e\u026f\5\u0088E\2\u026f\u0270\5\u00fc\177\2\u0270")
        buf.write(u"\u0271\5\u008aF\2\u0271\31\3\2\2\2\u0272\u0273\7Z\2\2")
        buf.write(u"\u0273\u0274\5\u00c4c\2\u0274\u0275\7\u0090\2\2\u0275")
        buf.write(u"\u0276\7\26\2\2\u0276\u0277\7\27\2\2\u0277\u0278\7\21")
        buf.write(u"\2\2\u0278\u0279\5\u0088E\2\u0279\u027a\5\u00fc\177\2")
        buf.write(u"\u027a\u027b\5\u008aF\2\u027b\33\3\2\2\2\u027c\u027d")
        buf.write(u"\7Z\2\2\u027d\u027f\5\u00c4c\2\u027e\u0280\7{\2\2\u027f")
        buf.write(u"\u027e\3\2\2\2\u027f\u0280\3\2\2\2\u0280\u0281\3\2\2")
        buf.write(u"\2\u0281\u0282\7\u0090\2\2\u0282\u0283\7\26\2\2\u0283")
        buf.write(u"\u0284\7\27\2\2\u0284\u0285\7\21\2\2\u0285\u0286\5\u0088")
        buf.write(u"E\2\u0286\u0287\5\u00f4{\2\u0287\u0288\5\u008aF\2\u0288")
        buf.write(u"\35\3\2\2\2\u0289\u028a\7Z\2\2\u028a\u028b\5\u00c4c\2")
        buf.write(u"\u028b\u028c\7o\2\2\u028c\u028d\7\26\2\2\u028d\u028e")
        buf.write(u"\7\27\2\2\u028e\u028f\7\21\2\2\u028f\u0290\5\u0088E\2")
        buf.write(u"\u0290\u0291\5\u00fc\177\2\u0291\u0292\5\u008aF\2\u0292")
        buf.write(u"\37\3\2\2\2\u0293\u0294\7Z\2\2\u0294\u0296\5\u00c4c\2")
        buf.write(u"\u0295\u0297\7{\2\2\u0296\u0295\3\2\2\2\u0296\u0297\3")
        buf.write(u"\2\2\2\u0297\u0298\3\2\2\2\u0298\u0299\7o\2\2\u0299\u029a")
        buf.write(u"\7\26\2\2\u029a\u029b\7\27\2\2\u029b\u029c\7\21\2\2\u029c")
        buf.write(u"\u029d\5\u0088E\2\u029d\u029e\5\u00f4{\2\u029e\u029f")
        buf.write(u"\5\u008aF\2\u029f!\3\2\2\2\u02a0\u02a2\7\u0093\2\2\u02a1")
        buf.write(u"\u02a0\3\2\2\2\u02a1\u02a2\3\2\2\2\u02a2\u02a3\3\2\2")
        buf.write(u"\2\u02a3\u02a4\7{\2\2\u02a4\u02a5\t\2\2\2\u02a5\u02a6")
        buf.write(u"\5\u00c8e\2\u02a6\u02a8\7\26\2\2\u02a7\u02a9\5\u00ee")
        buf.write(u"x\2\u02a8\u02a7\3\2\2\2\u02a8\u02a9\3\2\2\2\u02a9\u02aa")
        buf.write(u"\3\2\2\2\u02aa\u02ab\7\27\2\2\u02ab\u02ac\7\21\2\2\u02ac")
        buf.write(u"\u02ad\5\u0088E\2\u02ad\u02b1\5&\24\2\u02ae\u02af\5\u0086")
        buf.write(u"D\2\u02af\u02b0\5\u00dep\2\u02b0\u02b2\3\2\2\2\u02b1")
        buf.write(u"\u02ae\3\2\2\2\u02b1\u02b2\3\2\2\2\u02b2\u02b3\3\2\2")
        buf.write(u"\2\u02b3\u02b4\5\u008aF\2\u02b4#\3\2\2\2\u02b5\u02b7")
        buf.write(u"\7\u0093\2\2\u02b6\u02b5\3\2\2\2\u02b6\u02b7\3\2\2\2")
        buf.write(u"\u02b7\u02b8\3\2\2\2\u02b8\u02b9\7{\2\2\u02b9\u02ba\7")
        buf.write(u"\u008b\2\2\u02ba\u02bb\5\u00c8e\2\u02bb\u02bd\7\26\2")
        buf.write(u"\2\u02bc\u02be\5\u00eex\2\u02bd\u02bc\3\2\2\2\u02bd\u02be")
        buf.write(u"\3\2\2\2\u02be\u02bf\3\2\2\2\u02bf\u02c0\7\27\2\2\u02c0")
        buf.write(u"\u02c1\7\21\2\2\u02c1\u02c2\5\u0088E\2\u02c2\u02c6\5")
        buf.write(u"&\24\2\u02c3\u02c4\5\u0086D\2\u02c4\u02c5\5\u00dep\2")
        buf.write(u"\u02c5\u02c7\3\2\2\2\u02c6\u02c3\3\2\2\2\u02c6\u02c7")
        buf.write(u"\3\2\2\2\u02c7\u02c8\3\2\2\2\u02c8\u02c9\5\u008aF\2\u02c9")
        buf.write(u"%\3\2\2\2\u02ca\u02cb\7Z\2\2\u02cb\u02cc\t\2\2\2\u02cc")
        buf.write(u"\u02cd\7Q\2\2\u02cd\u02ce\7\21\2\2\u02ce\u02cf\5\u0088")
        buf.write(u"E\2\u02cf\u02d0\5(\25\2\u02d0\u02d1\5\u008aF\2\u02d1")
        buf.write(u"\'\3\2\2\2\u02d2\u02d3\b\25\1\2\u02d3\u02d4\5\u00e2r")
        buf.write(u"\2\u02d4\u02db\3\2\2\2\u02d5\u02d6\f\3\2\2\u02d6\u02d7")
        buf.write(u"\5\u0086D\2\u02d7\u02d8\5\u00e2r\2\u02d8\u02da\3\2\2")
        buf.write(u"\2\u02d9\u02d5\3\2\2\2\u02da\u02dd\3\2\2\2\u02db\u02d9")
        buf.write(u"\3\2\2\2\u02db\u02dc\3\2\2\2\u02dc)\3\2\2\2\u02dd\u02db")
        buf.write(u"\3\2\2\2\u02de\u02df\7G\2\2\u02df\u02e0\7Z\2\2\u02e0")
        buf.write(u"\u02e1\5\u00ba^\2\u02e1\u02e3\7\26\2\2\u02e2\u02e4\5")
        buf.write(u"\u00ccg\2\u02e3\u02e2\3\2\2\2\u02e3\u02e4\3\2\2\2\u02e4")
        buf.write(u"\u02e5\3\2\2\2\u02e5\u02e8\7\27\2\2\u02e6\u02e7\7\63")
        buf.write(u"\2\2\u02e7\u02e9\5\u00a8U\2\u02e8\u02e6\3\2\2\2\u02e8")
        buf.write(u"\u02e9\3\2\2\2\u02e9+\3\2\2\2\u02ea\u02eb\7Z\2\2\u02eb")
        buf.write(u"\u02ec\5\u00ba^\2\u02ec\u02ee\7\26\2\2\u02ed\u02ef\5")
        buf.write(u"\u00ccg\2\u02ee\u02ed\3\2\2\2\u02ee\u02ef\3\2\2\2\u02ef")
        buf.write(u"\u02f0\3\2\2\2\u02f0\u02f3\7\27\2\2\u02f1\u02f2\7\63")
        buf.write(u"\2\2\u02f2\u02f4\5\u00a8U\2\u02f3\u02f1\3\2\2\2\u02f3")
        buf.write(u"\u02f4\3\2\2\2\u02f4\u02f5\3\2\2\2\u02f5\u02f6\7\21\2")
        buf.write(u"\2\u02f6\u02f7\5\u0088E\2\u02f7\u02f8\5\u00fc\177\2\u02f8")
        buf.write(u"\u02f9\5\u008aF\2\u02f9-\3\2\2\2\u02fa\u02fc\7Z\2\2\u02fb")
        buf.write(u"\u02fd\7{\2\2\u02fc\u02fb\3\2\2\2\u02fc\u02fd\3\2\2\2")
        buf.write(u"\u02fd\u02fe\3\2\2\2\u02fe\u02ff\5\u00ba^\2\u02ff\u0301")
        buf.write(u"\7\26\2\2\u0300\u0302\5\u00ccg\2\u0301\u0300\3\2\2\2")
        buf.write(u"\u0301\u0302\3\2\2\2\u0302\u0303\3\2\2\2\u0303\u0306")
        buf.write(u"\7\27\2\2\u0304\u0305\7\63\2\2\u0305\u0307\5\u00d6l\2")
        buf.write(u"\u0306\u0304\3\2\2\2\u0306\u0307\3\2\2\2\u0307\u0308")
        buf.write(u"\3\2\2\2\u0308\u0309\7\21\2\2\u0309\u030a\5\u0088E\2")
        buf.write(u"\u030a\u030b\5\u00f4{\2\u030b\u030c\5\u008aF\2\u030c")
        buf.write(u"/\3\2\2\2\u030d\u030e\7Z\2\2\u030e\u030f\7\u0096\2\2")
        buf.write(u"\u030f\u0310\7\u00ab\2\2\u0310\u0311\7\26\2\2\u0311\u0312")
        buf.write(u"\7\27\2\2\u0312\u0313\7\21\2\2\u0313\u0314\5\u0088E\2")
        buf.write(u"\u0314\u0315\5\u00fc\177\2\u0315\u0316\5\u008aF\2\u0316")
        buf.write(u"\u0317\5\u0086D\2\u0317\u0318\7\u009b\2\2\u0318\u031e")
        buf.write(u"\7\21\2\2\u0319\u031a\5\u0088E\2\u031a\u031b\5\u00fe")
        buf.write(u"\u0080\2\u031b\u031c\5\u008aF\2\u031c\u031f\3\2\2\2\u031d")
        buf.write(u"\u031f\5\u00caf\2\u031e\u0319\3\2\2\2\u031e\u031d\3\2")
        buf.write(u"\2\2\u031f\61\3\2\2\2\u0320\u0321\5`\61\2\u0321\63\3")
        buf.write(u"\2\2\2\u0322\u0323\5\u00c4c\2\u0323\u0324\7\21\2\2\u0324")
        buf.write(u"\u0329\5\u00d6l\2\u0325\u0326\7\26\2\2\u0326\u0327\5")
        buf.write(u"\u00eex\2\u0327\u0328\7\27\2\2\u0328\u032a\3\2\2\2\u0329")
        buf.write(u"\u0325\3\2\2\2\u0329\u032a\3\2\2\2\u032a\u032d\3\2\2")
        buf.write(u"\2\u032b\u032c\7-\2\2\u032c\u032e\5\u0110\u0089\2\u032d")
        buf.write(u"\u032b\3\2\2\2\u032d\u032e\3\2\2\2\u032e\65\3\2\2\2\u032f")
        buf.write(u"\u0343\5<\37\2\u0330\u0343\5~@\2\u0331\u0343\5\u0082")
        buf.write(u"B\2\u0332\u0343\5:\36\2\u0333\u0343\58\35\2\u0334\u0343")
        buf.write(u"\5\\/\2\u0335\u0343\5^\60\2\u0336\u0343\5R*\2\u0337\u0343")
        buf.write(u"\5H%\2\u0338\u0343\5L\'\2\u0339\u0343\5P)\2\u033a\u0343")
        buf.write(u"\5N(\2\u033b\u0343\5V,\2\u033c\u0343\5X-\2\u033d\u0343")
        buf.write(u"\5v<\2\u033e\u0343\5D#\2\u033f\u0343\5F$\2\u0340\u0343")
        buf.write(u"\5,\27\2\u0341\u0343\5\u00f2z\2\u0342\u032f\3\2\2\2\u0342")
        buf.write(u"\u0330\3\2\2\2\u0342\u0331\3\2\2\2\u0342\u0332\3\2\2")
        buf.write(u"\2\u0342\u0333\3\2\2\2\u0342\u0334\3\2\2\2\u0342\u0335")
        buf.write(u"\3\2\2\2\u0342\u0336\3\2\2\2\u0342\u0337\3\2\2\2\u0342")
        buf.write(u"\u0338\3\2\2\2\u0342\u0339\3\2\2\2\u0342\u033a\3\2\2")
        buf.write(u"\2\u0342\u033b\3\2\2\2\u0342\u033c\3\2\2\2\u0342\u033d")
        buf.write(u"\3\2\2\2\u0342\u033e\3\2\2\2\u0342\u033f\3\2\2\2\u0342")
        buf.write(u"\u0340\3\2\2\2\u0342\u0341\3\2\2\2\u0343\67\3\2\2\2\u0344")
        buf.write(u"\u0345\7l\2\2\u0345\u0346\7\26\2\2\u0346\u0347\7\27\2")
        buf.write(u"\2\u03479\3\2\2\2\u0348\u0349\7]\2\2\u0349\u034a\7\26")
        buf.write(u"\2\2\u034a\u034b\5\u00a4S\2\u034b\u034c\7\27\2\2\u034c")
        buf.write(u"\u035d\3\2\2\2\u034d\u034e\7\u0094\2\2\u034e\u034f\7")
        buf.write(u"\26\2\2\u034f\u0350\5\u00a4S\2\u0350\u0351\7\27\2\2\u0351")
        buf.write(u"\u035d\3\2\2\2\u0352\u0353\7]\2\2\u0353\u0354\7\26\2")
        buf.write(u"\2\u0354\u0355\5\u00a4S\2\u0355\u0356\7\27\2\2\u0356")
        buf.write(u"\u0357\7J\2\2\u0357\u0358\7\u0094\2\2\u0358\u0359\7\26")
        buf.write(u"\2\2\u0359\u035a\5\u00a4S\2\u035a\u035b\7\27\2\2\u035b")
        buf.write(u"\u035d\3\2\2\2\u035c\u0348\3\2\2\2\u035c\u034d\3\2\2")
        buf.write(u"\2\u035c\u0352\3\2\2\2\u035d;\3\2\2\2\u035e\u035f\5>")
        buf.write(u" \2\u035f\u0361\7\26\2\2\u0360\u0362\5r:\2\u0361\u0360")
        buf.write(u"\3\2\2\2\u0361\u0362\3\2\2\2\u0362\u0363\3\2\2\2\u0363")
        buf.write(u"\u0364\7\27\2\2\u0364=\3\2\2\2\u0365\u036b\5\u00ba^\2")
        buf.write(u"\u0366\u0367\5@!\2\u0367\u0368\7\25\2\2\u0368\u0369\5")
        buf.write(u"\u00ba^\2\u0369\u036b\3\2\2\2\u036a\u0365\3\2\2\2\u036a")
        buf.write(u"\u0366\3\2\2\2\u036b?\3\2\2\2\u036c\u036d\b!\1\2\u036d")
        buf.write(u"\u036e\5\u00c2b\2\u036e\u0373\3\2\2\2\u036f\u0370\f\3")
        buf.write(u"\2\2\u0370\u0372\5B\"\2\u0371\u036f\3\2\2\2\u0372\u0375")
        buf.write(u"\3\2\2\2\u0373\u0371\3\2\2\2\u0373\u0374\3\2\2\2\u0374")
        buf.write(u"A\3\2\2\2\u0375\u0373\3\2\2\2\u0376\u0377\7\25\2\2\u0377")
        buf.write(u"\u037d\5\u00c4c\2\u0378\u0379\7\30\2\2\u0379\u037a\5")
        buf.write(u"`\61\2\u037a\u037b\7\31\2\2\u037b\u037d\3\2\2\2\u037c")
        buf.write(u"\u0376\3\2\2\2\u037c\u0378\3\2\2\2\u037dC\3\2\2\2\u037e")
        buf.write(u"\u037f\7\u009d\2\2\u037f\u0380\5\u0120\u0091\2\u0380")
        buf.write(u"\u0381\7\21\2\2\u0381\u0382\5\u0088E\2\u0382\u0383\5")
        buf.write(u"\u00fc\177\2\u0383\u0384\5\u008aF\2\u0384E\3\2\2\2\u0385")
        buf.write(u"\u0386\7\u009d\2\2\u0386\u0387\5\u00c8e\2\u0387\u0388")
        buf.write(u"\7\21\2\2\u0388\u0389\5\u0088E\2\u0389\u038a\5\u00fc")
        buf.write(u"\177\2\u038a\u038b\5\u008aF\2\u038bG\3\2\2\2\u038c\u038d")
        buf.write(u"\7\u0095\2\2\u038d\u038e\7\u0080\2\2\u038e\u038f\5`\61")
        buf.write(u"\2\u038f\u0390\7\21\2\2\u0390\u0391\5\u0088E\2\u0391")
        buf.write(u"\u0399\5\u0100\u0081\2\u0392\u0393\5\u0086D\2\u0393\u0394")
        buf.write(u"\7\u0086\2\2\u0394\u0395\7\21\2\2\u0395\u0396\5\u0088")
        buf.write(u"E\2\u0396\u0397\5\u00fc\177\2\u0397\u0398\5\u008aF\2")
        buf.write(u"\u0398\u039a\3\2\2\2\u0399\u0392\3\2\2\2\u0399\u039a")
        buf.write(u"\3\2\2\2\u039a\u039b\3\2\2\2\u039b\u039c\5\u008aF\2\u039c")
        buf.write(u"I\3\2\2\2\u039d\u039e\7\u009e\2\2\u039e\u039f\5\u0106")
        buf.write(u"\u0084\2\u039f\u03a0\7\21\2\2\u03a0\u03a1\5\u0088E\2")
        buf.write(u"\u03a1\u03a2\5\u00fc\177\2\u03a2\u03a3\5\u008aF\2\u03a3")
        buf.write(u"\u03ad\3\2\2\2\u03a4\u03a5\7\u009e\2\2\u03a5\u03a6\7")
        buf.write(u"r\2\2\u03a6\u03a7\5\u0104\u0083\2\u03a7\u03a8\7\21\2")
        buf.write(u"\2\u03a8\u03a9\5\u0088E\2\u03a9\u03aa\5\u00fc\177\2\u03aa")
        buf.write(u"\u03ab\5\u008aF\2\u03ab\u03ad\3\2\2\2\u03ac\u039d\3\2")
        buf.write(u"\2\2\u03ac\u03a4\3\2\2\2\u03adK\3\2\2\2\u03ae\u03af\7")
        buf.write(u"m\2\2\u03af\u03b2\5\u00c4c\2\u03b0\u03b1\7\23\2\2\u03b1")
        buf.write(u"\u03b3\5\u00c4c\2\u03b2\u03b0\3\2\2\2\u03b2\u03b3\3\2")
        buf.write(u"\2\2\u03b3\u03b4\3\2\2\2\u03b4\u03b5\7r\2\2\u03b5\u03b6")
        buf.write(u"\5`\61\2\u03b6\u03b7\7\21\2\2\u03b7\u03b8\5\u0088E\2")
        buf.write(u"\u03b8\u03b9\5\u00fc\177\2\u03b9\u03ba\5\u008aF\2\u03ba")
        buf.write(u"M\3\2\2\2\u03bb\u03bc\7_\2\2\u03bc\u03bd\7\21\2\2\u03bd")
        buf.write(u"\u03be\5\u0088E\2\u03be\u03bf\5\u00fc\177\2\u03bf\u03c0")
        buf.write(u"\5\u008aF\2\u03c0\u03c1\5\u0086D\2\u03c1\u03c2\7\u00a0")
        buf.write(u"\2\2\u03c2\u03c3\5`\61\2\u03c3O\3\2\2\2\u03c4\u03c5\7")
        buf.write(u"\u00a0\2\2\u03c5\u03c6\5`\61\2\u03c6\u03c7\7\21\2\2\u03c7")
        buf.write(u"\u03c8\5\u0088E\2\u03c8\u03c9\5\u00fc\177\2\u03c9\u03ca")
        buf.write(u"\5\u008aF\2\u03caQ\3\2\2\2\u03cb\u03cc\7q\2\2\u03cc\u03cd")
        buf.write(u"\5`\61\2\u03cd\u03ce\7\21\2\2\u03ce\u03cf\5\u0088E\2")
        buf.write(u"\u03cf\u03d0\5\u00fc\177\2\u03d0\u03d4\5\u008aF\2\u03d1")
        buf.write(u"\u03d2\5\u0086D\2\u03d2\u03d3\5T+\2\u03d3\u03d5\3\2\2")
        buf.write(u"\2\u03d4\u03d1\3\2\2\2\u03d4\u03d5\3\2\2\2\u03d5\u03dd")
        buf.write(u"\3\2\2\2\u03d6\u03d7\5\u0086D\2\u03d7\u03d8\7b\2\2\u03d8")
        buf.write(u"\u03d9\7\21\2\2\u03d9\u03da\5\u0088E\2\u03da\u03db\5")
        buf.write(u"\u00fc\177\2\u03db\u03dc\5\u008aF\2\u03dc\u03de\3\2\2")
        buf.write(u"\2\u03dd\u03d6\3\2\2\2\u03dd\u03de\3\2\2\2\u03deS\3\2")
        buf.write(u"\2\2\u03df\u03e0\b+\1\2\u03e0\u03e1\7b\2\2\u03e1\u03e2")
        buf.write(u"\7q\2\2\u03e2\u03e3\5`\61\2\u03e3\u03e4\7\21\2\2\u03e4")
        buf.write(u"\u03e5\5\u0088E\2\u03e5\u03e6\5\u00fc\177\2\u03e6\u03e7")
        buf.write(u"\5\u008aF\2\u03e7\u03f4\3\2\2\2\u03e8\u03e9\f\3\2\2\u03e9")
        buf.write(u"\u03ea\5\u0086D\2\u03ea\u03eb\7b\2\2\u03eb\u03ec\7q\2")
        buf.write(u"\2\u03ec\u03ed\5`\61\2\u03ed\u03ee\7\21\2\2\u03ee\u03ef")
        buf.write(u"\5\u0088E\2\u03ef\u03f0\5\u00fc\177\2\u03f0\u03f1\5\u008a")
        buf.write(u"F\2\u03f1\u03f3\3\2\2\2\u03f2\u03e8\3\2\2\2\u03f3\u03f6")
        buf.write(u"\3\2\2\2\u03f4\u03f2\3\2\2\2\u03f4\u03f5\3\2\2\2\u03f5")
        buf.write(u"U\3\2\2\2\u03f6\u03f4\3\2\2\2\u03f7\u03f8\7\u0088\2\2")
        buf.write(u"\u03f8\u03f9\5`\61\2\u03f9W\3\2\2\2\u03fa\u03fb\7\u009a")
        buf.write(u"\2\2\u03fb\u03fc\5\u00c4c\2\u03fc\u03fd\7\21\2\2\u03fd")
        buf.write(u"\u03fe\5\u0088E\2\u03fe\u03ff\5\u00fc\177\2\u03ff\u0400")
        buf.write(u"\5\u008aF\2\u0400\u0402\5\u0084C\2\u0401\u0403\5\u0102")
        buf.write(u"\u0082\2\u0402\u0401\3\2\2\2\u0402\u0403\3\2\2\2\u0403")
        buf.write(u"\u040b\3\2\2\2\u0404\u0405\7e\2\2\u0405\u0406\7\21\2")
        buf.write(u"\2\u0406\u0407\5\u0088E\2\u0407\u0408\5\u00fc\177\2\u0408")
        buf.write(u"\u0409\5\u008aF\2\u0409\u040a\5\u0084C\2\u040a\u040c")
        buf.write(u"\3\2\2\2\u040b\u0404\3\2\2\2\u040b\u040c\3\2\2\2\u040c")
        buf.write(u"\u0414\3\2\2\2\u040d\u040e\7k\2\2\u040e\u040f\7\21\2")
        buf.write(u"\2\u040f\u0410\5\u0088E\2\u0410\u0411\5\u00fc\177\2\u0411")
        buf.write(u"\u0412\5\u008aF\2\u0412\u0413\5\u0084C\2\u0413\u0415")
        buf.write(u"\3\2\2\2\u0414\u040d\3\2\2\2\u0414\u0415\3\2\2\2\u0415")
        buf.write(u"\u0416\3\2\2\2\u0416\u0417\5\u0084C\2\u0417Y\3\2\2\2")
        buf.write(u"\u0418\u0419\7e\2\2\u0419\u041a\5\u00caf\2\u041a\u041b")
        buf.write(u"\7\21\2\2\u041b\u041c\5\u0088E\2\u041c\u041d\5\u00fc")
        buf.write(u"\177\2\u041d\u041e\5\u008aF\2\u041e\u041f\5\u0084C\2")
        buf.write(u"\u041f\u042c\3\2\2\2\u0420\u0421\7e\2\2\u0421\u0422\7")
        buf.write(u"r\2\2\u0422\u0423\7\30\2\2\u0423\u0424\5\u009cO\2\u0424")
        buf.write(u"\u0425\7\31\2\2\u0425\u0426\7\21\2\2\u0426\u0427\5\u0088")
        buf.write(u"E\2\u0427\u0428\5\u00fc\177\2\u0428\u0429\5\u008aF\2")
        buf.write(u"\u0429\u042a\5\u0084C\2\u042a\u042c\3\2\2\2\u042b\u0418")
        buf.write(u"\3\2\2\2\u042b\u0420\3\2\2\2\u042c[\3\2\2\2\u042d\u042e")
        buf.write(u"\7R\2\2\u042e]\3\2\2\2\u042f\u0431\7\u008c\2\2\u0430")
        buf.write(u"\u0432\5`\61\2\u0431\u0430\3\2\2\2\u0431\u0432\3\2\2")
        buf.write(u"\2\u0432_\3\2\2\2\u0433\u0434\b\61\1\2\u0434\u0448\5")
        buf.write(u"\u01ce\u00e8\2\u0435\u0448\5\u01b0\u00d9\2\u0436\u0448")
        buf.write(u"\5d\63\2\u0437\u0448\5f\64\2\u0438\u0439\7#\2\2\u0439")
        buf.write(u"\u0448\5`\61$\u043a\u043b\7}\2\2\u043b\u0448\5`\61#\u043c")
        buf.write(u"\u043d\7?\2\2\u043d\u043e\7\26\2\2\u043e\u043f\5`\61")
        buf.write(u"\2\u043f\u0440\7\27\2\2\u0440\u0448\3\2\2\2\u0441\u0442")
        buf.write(u"\7f\2\2\u0442\u0443\7\26\2\2\u0443\u0444\5\u00c4c\2\u0444")
        buf.write(u"\u0445\7\27\2\2\u0445\u0448\3\2\2\2\u0446\u0448\5b\62")
        buf.write(u"\2\u0447\u0433\3\2\2\2\u0447\u0435\3\2\2\2\u0447\u0436")
        buf.write(u"\3\2\2\2\u0447\u0437\3\2\2\2\u0447\u0438\3\2\2\2\u0447")
        buf.write(u"\u043a\3\2\2\2\u0447\u043c\3\2\2\2\u0447\u0441\3\2\2")
        buf.write(u"\2\u0447\u0446\3\2\2\2\u0448\u04b8\3\2\2\2\u0449\u044a")
        buf.write(u"\f\"\2\2\u044a\u044b\5\u013e\u00a0\2\u044b\u044c\5`\61")
        buf.write(u"#\u044c\u04b7\3\2\2\2\u044d\u044e\f!\2\2\u044e\u044f")
        buf.write(u"\5\u0140\u00a1\2\u044f\u0450\5`\61\"\u0450\u04b7\3\2")
        buf.write(u"\2\2\u0451\u0452\f \2\2\u0452\u0453\5\u0144\u00a3\2\u0453")
        buf.write(u"\u0454\5`\61!\u0454\u04b7\3\2\2\2\u0455\u0456\f\37\2")
        buf.write(u"\2\u0456\u0457\5\u0142\u00a2\2\u0457\u0458\5`\61 \u0458")
        buf.write(u"\u04b7\3\2\2\2\u0459\u045a\f\36\2\2\u045a\u045b\t\3\2")
        buf.write(u"\2\u045b\u04b7\5`\61\37\u045c\u045d\f\34\2\2\u045d\u045e")
        buf.write(u"\7*\2\2\u045e\u04b7\5`\61\35\u045f\u0460\f\33\2\2\u0460")
        buf.write(u"\u0461\7+\2\2\u0461\u04b7\5`\61\34\u0462\u0463\f\32\2")
        buf.write(u"\2\u0463\u0464\7(\2\2\u0464\u04b7\5`\61\33\u0465\u0466")
        buf.write(u"\f\31\2\2\u0466\u0467\7)\2\2\u0467\u04b7\5`\61\32\u0468")
        buf.write(u"\u0469\f\26\2\2\u0469\u046a\7/\2\2\u046a\u04b7\5`\61")
        buf.write(u"\27\u046b\u046c\f\25\2\2\u046c\u046d\7.\2\2\u046d\u04b7")
        buf.write(u"\5`\61\26\u046e\u046f\f\24\2\2\u046f\u0470\7\60\2\2\u0470")
        buf.write(u"\u04b7\5`\61\25\u0471\u0472\f\23\2\2\u0472\u0473\7Y\2")
        buf.write(u"\2\u0473\u04b7\5`\61\24\u0474\u0475\f\22\2\2\u0475\u0476")
        buf.write(u"\7r\2\2\u0476\u04b7\5`\61\23\u0477\u0478\f\21\2\2\u0478")
        buf.write(u"\u0479\7p\2\2\u0479\u04b7\5`\61\22\u047a\u047b\f\20\2")
        buf.write(u"\2\u047b\u047c\7p\2\2\u047c\u047d\7H\2\2\u047d\u04b7")
        buf.write(u"\5`\61\21\u047e\u047f\f\17\2\2\u047f\u0480\7p\2\2\u0480")
        buf.write(u"\u0481\7K\2\2\u0481\u04b7\5`\61\20\u0482\u0483\f\16\2")
        buf.write(u"\2\u0483\u0484\7}\2\2\u0484\u0485\7Y\2\2\u0485\u04b7")
        buf.write(u"\5`\61\17\u0486\u0487\f\r\2\2\u0487\u0488\7}\2\2\u0488")
        buf.write(u"\u0489\7r\2\2\u0489\u04b7\5`\61\16\u048a\u048b\f\f\2")
        buf.write(u"\2\u048b\u048c\7}\2\2\u048c\u048d\7p\2\2\u048d\u04b7")
        buf.write(u"\5`\61\r\u048e\u048f\f\13\2\2\u048f\u0490\7}\2\2\u0490")
        buf.write(u"\u0491\7p\2\2\u0491\u0492\7H\2\2\u0492\u04b7\5`\61\f")
        buf.write(u"\u0493\u0494\f\n\2\2\u0494\u0495\7}\2\2\u0495\u0496\7")
        buf.write(u"p\2\2\u0496\u0497\7K\2\2\u0497\u04b7\5`\61\13\u0498\u0499")
        buf.write(u"\f\t\2\2\u0499\u049a\7\u0084\2\2\u049a\u04b7\5`\61\n")
        buf.write(u"\u049b\u049c\f\b\2\2\u049c\u049d\7J\2\2\u049d\u04b7\5")
        buf.write(u"`\61\t\u049e\u049f\f\7\2\2\u049f\u04a0\7q\2\2\u04a0\u04a1")
        buf.write(u"\5`\61\2\u04a1\u04a2\7b\2\2\u04a2\u04a3\5`\61\b\u04a3")
        buf.write(u"\u04b7\3\2\2\2\u04a4\u04a5\f\3\2\2\u04a5\u04a6\7m\2\2")
        buf.write(u"\u04a6\u04a7\5\u00c4c\2\u04a7\u04a8\7r\2\2\u04a8\u04a9")
        buf.write(u"\5`\61\4\u04a9\u04b7\3\2\2\2\u04aa\u04ab\f&\2\2\u04ab")
        buf.write(u"\u04b7\5x=\2\u04ac\u04ad\f\35\2\2\u04ad\u04ae\7L\2\2")
        buf.write(u"\u04ae\u04b7\5\u00d6l\2\u04af\u04b0\f\30\2\2\u04b0\u04b1")
        buf.write(u"\7u\2\2\u04b1\u04b2\7}\2\2\u04b2\u04b7\5\u0124\u0093")
        buf.write(u"\2\u04b3\u04b4\f\27\2\2\u04b4\u04b5\7u\2\2\u04b5\u04b7")
        buf.write(u"\5\u0124\u0093\2\u04b6\u0449\3\2\2\2\u04b6\u044d\3\2")
        buf.write(u"\2\2\u04b6\u0451\3\2\2\2\u04b6\u0455\3\2\2\2\u04b6\u0459")
        buf.write(u"\3\2\2\2\u04b6\u045c\3\2\2\2\u04b6\u045f\3\2\2\2\u04b6")
        buf.write(u"\u0462\3\2\2\2\u04b6\u0465\3\2\2\2\u04b6\u0468\3\2\2")
        buf.write(u"\2\u04b6\u046b\3\2\2\2\u04b6\u046e\3\2\2\2\u04b6\u0471")
        buf.write(u"\3\2\2\2\u04b6\u0474\3\2\2\2\u04b6\u0477\3\2\2\2\u04b6")
        buf.write(u"\u047a\3\2\2\2\u04b6\u047e\3\2\2\2\u04b6\u0482\3\2\2")
        buf.write(u"\2\u04b6\u0486\3\2\2\2\u04b6\u048a\3\2\2\2\u04b6\u048e")
        buf.write(u"\3\2\2\2\u04b6\u0493\3\2\2\2\u04b6\u0498\3\2\2\2\u04b6")
        buf.write(u"\u049b\3\2\2\2\u04b6\u049e\3\2\2\2\u04b6\u04a4\3\2\2")
        buf.write(u"\2\u04b6\u04aa\3\2\2\2\u04b6\u04ac\3\2\2\2\u04b6\u04af")
        buf.write(u"\3\2\2\2\u04b6\u04b3\3\2\2\2\u04b7\u04ba\3\2\2\2\u04b8")
        buf.write(u"\u04b6\3\2\2\2\u04b8\u04b9\3\2\2\2\u04b9a\3\2\2\2\u04ba")
        buf.write(u"\u04b8\3\2\2\2\u04bb\u04bc\5\u00c8e\2\u04bcc\3\2\2\2")
        buf.write(u"\u04bd\u04be\b\63\1\2\u04be\u04bf\5\u010a\u0086\2\u04bf")
        buf.write(u"\u04c4\3\2\2\2\u04c0\u04c1\f\3\2\2\u04c1\u04c3\5h\65")
        buf.write(u"\2\u04c2\u04c0\3\2\2\2\u04c3\u04c6\3\2\2\2\u04c4\u04c2")
        buf.write(u"\3\2\2\2\u04c4\u04c5\3\2\2\2\u04c5e\3\2\2\2\u04c6\u04c4")
        buf.write(u"\3\2\2\2\u04c7\u04d0\5j\66\2\u04c8\u04d0\5l\67\2\u04c9")
        buf.write(u"\u04d0\5z>\2\u04ca\u04d0\5\u0126\u0094\2\u04cb\u04d0")
        buf.write(u"\5\u0128\u0095\2\u04cc\u04d0\5|?\2\u04cd\u04d0\5<\37")
        buf.write(u"\2\u04ce\u04d0\5n8\2\u04cf\u04c7\3\2\2\2\u04cf\u04c8")
        buf.write(u"\3\2\2\2\u04cf\u04c9\3\2\2\2\u04cf\u04ca\3\2\2\2\u04cf")
        buf.write(u"\u04cb\3\2\2\2\u04cf\u04cc\3\2\2\2\u04cf\u04cd\3\2\2")
        buf.write(u"\2\u04cf\u04ce\3\2\2\2\u04d0g\3\2\2\2\u04d1\u04d2\6\65")
        buf.write(u"$\3\u04d2\u04d3\7\25\2\2\u04d3\u04df\5\u00c4c\2\u04d4")
        buf.write(u"\u04d5\6\65%\3\u04d5\u04d6\7\30\2\2\u04d6\u04d7\5\u011e")
        buf.write(u"\u0090\2\u04d7\u04d8\7\31\2\2\u04d8\u04df\3\2\2\2\u04d9")
        buf.write(u"\u04da\6\65&\3\u04da\u04db\7\30\2\2\u04db\u04dc\5`\61")
        buf.write(u"\2\u04dc\u04dd\7\31\2\2\u04dd\u04df\3\2\2\2\u04de\u04d1")
        buf.write(u"\3\2\2\2\u04de\u04d4\3\2\2\2\u04de\u04d9\3\2\2\2\u04df")
        buf.write(u"i\3\2\2\2\u04e0\u04e1\7A\2\2\u04e1\u04e3\7\26\2\2\u04e2")
        buf.write(u"\u04e4\5`\61\2\u04e3\u04e2\3\2\2\2\u04e3\u04e4\3\2\2")
        buf.write(u"\2\u04e4\u04e5\3\2\2\2\u04e5\u04e6\7\27\2\2\u04e6k\3")
        buf.write(u"\2\2\2\u04e7\u04e8\7@\2\2\u04e8\u04ea\7\26\2\2\u04e9")
        buf.write(u"\u04eb\5`\61\2\u04ea\u04e9\3\2\2\2\u04ea\u04eb\3\2\2")
        buf.write(u"\2\u04eb\u04ec\3\2\2\2\u04ec\u04ed\7\27\2\2\u04edm\3")
        buf.write(u"\2\2\2\u04ee\u04ef\5\u00b0Y\2\u04ef\u04f0\7\26\2\2\u04f0")
        buf.write(u"\u04f3\5p9\2\u04f1\u04f2\7\23\2\2\u04f2\u04f4\5r:\2\u04f3")
        buf.write(u"\u04f1\3\2\2\2\u04f3\u04f4\3\2\2\2\u04f4\u04f5\3\2\2")
        buf.write(u"\2\u04f5\u04f6\7\27\2\2\u04f6\u04ff\3\2\2\2\u04f7\u04f8")
        buf.write(u"\5\u00b0Y\2\u04f8\u04fa\7\26\2\2\u04f9\u04fb\5r:\2\u04fa")
        buf.write(u"\u04f9\3\2\2\2\u04fa\u04fb\3\2\2\2\u04fb\u04fc\3\2\2")
        buf.write(u"\2\u04fc\u04fd\7\27\2\2\u04fd\u04ff\3\2\2\2\u04fe\u04ee")
        buf.write(u"\3\2\2\2\u04fe\u04f7\3\2\2\2\u04ffo\3\2\2\2\u0500\u0501")
        buf.write(u"\7n\2\2\u0501\u0502\5\u013c\u009f\2\u0502\u0503\5`\61")
        buf.write(u"\2\u0503\u0504\69\'\3\u0504q\3\2\2\2\u0505\u0506\b:\1")
        buf.write(u"\2\u0506\u0507\5`\61\2\u0507\u0508\6:(\3\u0508\u050b")
        buf.write(u"\3\2\2\2\u0509\u050b\5t;\2\u050a\u0505\3\2\2\2\u050a")
        buf.write(u"\u0509\3\2\2\2\u050b\u0511\3\2\2\2\u050c\u050d\f\3\2")
        buf.write(u"\2\u050d\u050e\7\23\2\2\u050e\u0510\5t;\2\u050f\u050c")
        buf.write(u"\3\2\2\2\u0510\u0513\3\2\2\2\u0511\u050f\3\2\2\2\u0511")
        buf.write(u"\u0512\3\2\2\2\u0512s\3\2\2\2\u0513\u0511\3\2\2\2\u0514")
        buf.write(u"\u0518\5\u00c4c\2\u0515\u0516\5\u013c\u009f\2\u0516\u0517")
        buf.write(u"\5`\61\2\u0517\u0519\3\2\2\2\u0518\u0515\3\2\2\2\u0518")
        buf.write(u"\u0519\3\2\2\2\u0519u\3\2\2\2\u051a\u051b\7\u00a1\2\2")
        buf.write(u"\u051b\u051c\5`\61\2\u051c\u051d\7\u0099\2\2\u051d\u051e")
        buf.write(u"\5`\61\2\u051ew\3\2\2\2\u051f\u0520\7j\2\2\u0520\u0521")
        buf.write(u"\7\u009d\2\2\u0521\u0522\5\u00c4c\2\u0522\u0523\7\u009f")
        buf.write(u"\2\2\u0523\u0524\5`\61\2\u0524y\3\2\2\2\u0525\u0526\7")
        buf.write(u"i\2\2\u0526\u0528\7\u0081\2\2\u0527\u0529\5\u00b0Y\2")
        buf.write(u"\u0528\u0527\3\2\2\2\u0528\u0529\3\2\2\2\u0529\u052a")
        buf.write(u"\3\2\2\2\u052a\u052b\7\u009f\2\2\u052b\u0544\5`\61\2")
        buf.write(u"\u052c\u0533\7i\2\2\u052d\u0534\7H\2\2\u052e\u052f\7")
        buf.write(u"\u008e\2\2\u052f\u0530\5`\61\2\u0530\u0531\7\u0099\2")
        buf.write(u"\2\u0531\u0532\5`\61\2\u0532\u0534\3\2\2\2\u0533\u052d")
        buf.write(u"\3\2\2\2\u0533\u052e\3\2\2\2\u0534\u0535\3\2\2\2\u0535")
        buf.write(u"\u0537\7\26\2\2\u0536\u0538\5\u00b0Y\2\u0537\u0536\3")
        buf.write(u"\2\2\2\u0537\u0538\3\2\2\2\u0538\u0539\3\2\2\2\u0539")
        buf.write(u"\u053c\7\27\2\2\u053a\u053b\7\u009f\2\2\u053b\u053d\5")
        buf.write(u"`\61\2\u053c\u053a\3\2\2\2\u053c\u053d\3\2\2\2\u053d")
        buf.write(u"\u0541\3\2\2\2\u053e\u053f\7\u0085\2\2\u053f\u0540\7")
        buf.write(u"S\2\2\u0540\u0542\5\u012a\u0096\2\u0541\u053e\3\2\2\2")
        buf.write(u"\u0541\u0542\3\2\2\2\u0542\u0544\3\2\2\2\u0543\u0525")
        buf.write(u"\3\2\2\2\u0543\u052c\3\2\2\2\u0544{\3\2\2\2\u0545\u0547")
        buf.write(u"\7\u0092\2\2\u0546\u0548\7^\2\2\u0547\u0546\3\2\2\2\u0547")
        buf.write(u"\u0548\3\2\2\2\u0548\u0549\3\2\2\2\u0549\u054a\7\26\2")
        buf.write(u"\2\u054a\u0550\5d\63\2\u054b\u054c\7\23\2\2\u054c\u054d")
        buf.write(u"\5\u0134\u009b\2\u054d\u054e\7-\2\2\u054e\u054f\5d\63")
        buf.write(u"\2\u054f\u0551\3\2\2\2\u0550\u054b\3\2\2\2\u0550\u0551")
        buf.write(u"\3\2\2\2\u0551\u0552\3\2\2\2\u0552\u0553\7\27\2\2\u0553")
        buf.write(u"}\3\2\2\2\u0554\u0555\5\u0122\u0092\2\u0555\u0556\5\u013c")
        buf.write(u"\u009f\2\u0556\u0557\5`\61\2\u0557\177\3\2\2\2\u0558")
        buf.write(u"\u0559\6A*\3\u0559\u055a\7\25\2\2\u055a\u0561\5\u00c4")
        buf.write(u"c\2\u055b\u055c\6A+\3\u055c\u055d\7\30\2\2\u055d\u055e")
        buf.write(u"\5`\61\2\u055e\u055f\7\31\2\2\u055f\u0561\3\2\2\2\u0560")
        buf.write(u"\u0558\3\2\2\2\u0560\u055b\3\2\2\2\u0561\u0081\3\2\2")
        buf.write(u"\2\u0562\u0563\5\u00ecw\2\u0563\u0564\5\u013c\u009f\2")
        buf.write(u"\u0564\u0565\5`\61\2\u0565\u0083\3\2\2\2\u0566\u0568")
        buf.write(u"\7\7\2\2\u0567\u0566\3\2\2\2\u0568\u056b\3\2\2\2\u0569")
        buf.write(u"\u0567\3\2\2\2\u0569\u056a\3\2\2\2\u056a\u0085\3\2\2")
        buf.write(u"\2\u056b\u0569\3\2\2\2\u056c\u056e\7\7\2\2\u056d\u056c")
        buf.write(u"\3\2\2\2\u056e\u056f\3\2\2\2\u056f\u056d\3\2\2\2\u056f")
        buf.write(u"\u0570\3\2\2\2\u0570\u0087\3\2\2\2\u0571\u0573\7\7\2")
        buf.write(u"\2\u0572\u0571\3\2\2\2\u0573\u0574\3\2\2\2\u0574\u0572")
        buf.write(u"\3\2\2\2\u0574\u0575\3\2\2\2\u0575\u0576\3\2\2\2\u0576")
        buf.write(u"\u0577\7\3\2\2\u0577\u0089\3\2\2\2\u0578\u057a\7\7\2")
        buf.write(u"\2\u0579\u0578\3\2\2\2\u057a\u057d\3\2\2\2\u057b\u0579")
        buf.write(u"\3\2\2\2\u057b\u057c\3\2\2\2\u057c\u057e\3\2\2\2\u057d")
        buf.write(u"\u057b\3\2\2\2\u057e\u057f\7\4\2\2\u057f\u008b\3\2\2")
        buf.write(u"\2\u0580\u0581\7|\2\2\u0581\u008d\3\2\2\2\u0582\u0584")
        buf.write(u"\5\u0090I\2\u0583\u0582\3\2\2\2\u0583\u0584\3\2\2\2\u0584")
        buf.write(u"\u0585\3\2\2\2\u0585\u0586\5\u0084C\2\u0586\u0587\7\2")
        buf.write(u"\2\3\u0587\u008f\3\2\2\2\u0588\u058e\5\u0092J\2\u0589")
        buf.write(u"\u058a\5\u0086D\2\u058a\u058b\5\u0092J\2\u058b\u058d")
        buf.write(u"\3\2\2\2\u058c\u0589\3\2\2\2\u058d\u0590\3\2\2\2\u058e")
        buf.write(u"\u058c\3\2\2\2\u058e\u058f\3\2\2\2\u058f\u0091\3\2\2")
        buf.write(u"\2\u0590\u058e\3\2\2\2\u0591\u0592\5\u00f2z\2\u0592\u0593")
        buf.write(u"\5\u0086D\2\u0593\u0595\3\2\2\2\u0594\u0591\3\2\2\2\u0595")
        buf.write(u"\u0598\3\2\2\2\u0596\u0594\3\2\2\2\u0596\u0597\3\2\2")
        buf.write(u"\2\u0597\u059f\3\2\2\2\u0598\u0596\3\2\2\2\u0599\u05a0")
        buf.write(u"\5\n\6\2\u059a\u05a0\5\u00b4[\2\u059b\u05a0\5\u0094K")
        buf.write(u"\2\u059c\u05a0\5\u0096L\2\u059d\u05a0\5\u00b6\\\2\u059e")
        buf.write(u"\u05a0\5\u00f0y\2\u059f\u0599\3\2\2\2\u059f\u059a\3\2")
        buf.write(u"\2\2\u059f\u059b\3\2\2\2\u059f\u059c\3\2\2\2\u059f\u059d")
        buf.write(u"\3\2\2\2\u059f\u059e\3\2\2\2\u05a0\u0093\3\2\2\2\u05a1")
        buf.write(u"\u05a2\5$\23\2\u05a2\u0095\3\2\2\2\u05a3\u05a6\5\2\2")
        buf.write(u"\2\u05a4\u05a6\5\4\3\2\u05a5\u05a3\3\2\2\2\u05a5\u05a4")
        buf.write(u"\3\2\2\2\u05a6\u0097\3\2\2\2\u05a7\u05ad\5\6\4\2\u05a8")
        buf.write(u"\u05a9\5\u0086D\2\u05a9\u05aa\5\6\4\2\u05aa\u05ac\3\2")
        buf.write(u"\2\2\u05ab\u05a8\3\2\2\2\u05ac\u05af\3\2\2\2\u05ad\u05ab")
        buf.write(u"\3\2\2\2\u05ad\u05ae\3\2\2\2\u05ae\u0099\3\2\2\2\u05af")
        buf.write(u"\u05ad\3\2\2\2\u05b0\u05b6\5\b\5\2\u05b1\u05b2\5\u0086")
        buf.write(u"D\2\u05b2\u05b3\5\b\5\2\u05b3\u05b5\3\2\2\2\u05b4\u05b1")
        buf.write(u"\3\2\2\2\u05b5\u05b8\3\2\2\2\u05b6\u05b4\3\2\2\2\u05b6")
        buf.write(u"\u05b7\3\2\2\2\u05b7\u009b\3\2\2\2\u05b8\u05b6\3\2\2")
        buf.write(u"\2\u05b9\u05be\5\u00caf\2\u05ba\u05bb\7\23\2\2\u05bb")
        buf.write(u"\u05bd\5\u00caf\2\u05bc\u05ba\3\2\2\2\u05bd\u05c0\3\2")
        buf.write(u"\2\2\u05be\u05bc\3\2\2\2\u05be\u05bf\3\2\2\2\u05bf\u009d")
        buf.write(u"\3\2\2\2\u05c0\u05be\3\2\2\2\u05c1\u05c2\7r\2\2\u05c2")
        buf.write(u"\u05cc\5\u00a0Q\2\u05c3\u05c4\7r\2\2\u05c4\u05cc\5\u00a2")
        buf.write(u"R\2\u05c5\u05c6\7r\2\2\u05c6\u05cc\5\u00a6T\2\u05c7\u05c8")
        buf.write(u"\7v\2\2\u05c8\u05cc\7\u00ab\2\2\u05c9\u05ca\7v\2\2\u05ca")
        buf.write(u"\u05cc\5`\61\2\u05cb\u05c1\3\2\2\2\u05cb\u05c3\3\2\2")
        buf.write(u"\2\u05cb\u05c5\3\2\2\2\u05cb\u05c7\3\2\2\2\u05cb\u05c9")
        buf.write(u"\3\2\2\2\u05cc\u009f\3\2\2\2\u05cd\u05cf\7z\2\2\u05ce")
        buf.write(u"\u05cd\3\2\2\2\u05ce\u05cf\3\2\2\2\u05cf\u05d0\3\2\2")
        buf.write(u"\2\u05d0\u05d2\7\30\2\2\u05d1\u05d3\5\u00a4S\2\u05d2")
        buf.write(u"\u05d1\3\2\2\2\u05d2\u05d3\3\2\2\2\u05d3\u05d4\3\2\2")
        buf.write(u"\2\u05d4\u05d5\7\31\2\2\u05d5\u00a1\3\2\2\2\u05d6\u05d8")
        buf.write(u"\7z\2\2\u05d7\u05d6\3\2\2\2\u05d7\u05d8\3\2\2\2\u05d8")
        buf.write(u"\u05d9\3\2\2\2\u05d9\u05db\7*\2\2\u05da\u05dc\5\u00a4")
        buf.write(u"S\2\u05db\u05da\3\2\2\2\u05db\u05dc\3\2\2\2\u05dc\u05dd")
        buf.write(u"\3\2\2\2\u05dd\u05de\7(\2\2\u05de\u00a3\3\2\2\2\u05df")
        buf.write(u"\u05e4\5`\61\2\u05e0\u05e1\7\23\2\2\u05e1\u05e3\5`\61")
        buf.write(u"\2\u05e2\u05e0\3\2\2\2\u05e3\u05e6\3\2\2\2\u05e4\u05e2")
        buf.write(u"\3\2\2\2\u05e4\u05e5\3\2\2\2\u05e5\u00a5\3\2\2\2\u05e6")
        buf.write(u"\u05e4\3\2\2\2\u05e7\u05e8\7\30\2\2\u05e8\u05e9\5`\61")
        buf.write(u"\2\u05e9\u05ea\7\24\2\2\u05ea\u05eb\5`\61\2\u05eb\u05ec")
        buf.write(u"\7\31\2\2\u05ec\u00a7\3\2\2\2\u05ed\u05ee\bU\1\2\u05ee")
        buf.write(u"\u05fa\5\u00aaV\2\u05ef\u05f0\7E\2\2\u05f0\u05f1\7*\2")
        buf.write(u"\2\u05f1\u05f2\5\u00a8U\2\u05f2\u05f3\7(\2\2\u05f3\u05fa")
        buf.write(u"\3\2\2\2\u05f4\u05f5\7D\2\2\u05f5\u05f6\7*\2\2\u05f6")
        buf.write(u"\u05f7\5\u00a8U\2\u05f7\u05f8\7(\2\2\u05f8\u05fa\3\2")
        buf.write(u"\2\2\u05f9\u05ed\3\2\2\2\u05f9\u05ef\3\2\2\2\u05f9\u05f4")
        buf.write(u"\3\2\2\2\u05fa\u0605\3\2\2\2\u05fb\u05fc\f\7\2\2\u05fc")
        buf.write(u"\u0604\7,\2\2\u05fd\u05fe\f\6\2\2\u05fe\u05ff\7\30\2")
        buf.write(u"\2\u05ff\u0604\7\31\2\2\u0600\u0601\f\5\2\2\u0601\u0602")
        buf.write(u"\7\32\2\2\u0602\u0604\7\33\2\2\u0603\u05fb\3\2\2\2\u0603")
        buf.write(u"\u05fd\3\2\2\2\u0603\u0600\3\2\2\2\u0604\u0607\3\2\2")
        buf.write(u"\2\u0605\u0603\3\2\2\2\u0605\u0606\3\2\2\2\u0606\u00a9")
        buf.write(u"\3\2\2\2\u0607\u0605\3\2\2\2\u0608\u060b\5\u00acW\2\u0609")
        buf.write(u"\u060b\5\u00aeX\2\u060a\u0608\3\2\2\2\u060a\u0609\3\2")
        buf.write(u"\2\2\u060b\u00ab\3\2\2\2\u060c\u061d\7\64\2\2\u060d\u061d")
        buf.write(u"\7\65\2\2\u060e\u061d\7\66\2\2\u060f\u061d\7B\2\2\u0610")
        buf.write(u"\u061d\7\67\2\2\u0611\u061d\78\2\2\u0612\u061d\7@\2\2")
        buf.write(u"\u0613\u061d\79\2\2\u0614\u061d\7;\2\2\u0615\u061d\7")
        buf.write(u":\2\2\u0616\u061d\7<\2\2\u0617\u061d\7=\2\2\u0618\u061d")
        buf.write(u"\7?\2\2\u0619\u061d\7A\2\2\u061a\u061d\7C\2\2\u061b\u061d")
        buf.write(u"\7F\2\2\u061c\u060c\3\2\2\2\u061c\u060d\3\2\2\2\u061c")
        buf.write(u"\u060e\3\2\2\2\u061c\u060f\3\2\2\2\u061c\u0610\3\2\2")
        buf.write(u"\2\u061c\u0611\3\2\2\2\u061c\u0612\3\2\2\2\u061c\u0613")
        buf.write(u"\3\2\2\2\u061c\u0614\3\2\2\2\u061c\u0615\3\2\2\2\u061c")
        buf.write(u"\u0616\3\2\2\2\u061c\u0617\3\2\2\2\u061c\u0618\3\2\2")
        buf.write(u"\2\u061c\u0619\3\2\2\2\u061c\u061a\3\2\2\2\u061c\u061b")
        buf.write(u"\3\2\2\2\u061d\u00ad\3\2\2\2\u061e\u061f\7\u00a7\2\2")
        buf.write(u"\u061f\u00af\3\2\2\2\u0620\u0622\7z\2\2\u0621\u0620\3")
        buf.write(u"\2\2\2\u0621\u0622\3\2\2\2\u0622\u0623\3\2\2\2\u0623")
        buf.write(u"\u0624\5\u00aeX\2\u0624\u00b1\3\2\2\2\u0625\u0626\7?")
        buf.write(u"\2\2\u0626\u00b3\3\2\2\2\u0627\u062b\5\22\n\2\u0628\u062b")
        buf.write(u"\5\"\22\2\u0629\u062b\5\24\13\2\u062a\u0627\3\2\2\2\u062a")
        buf.write(u"\u0628\3\2\2\2\u062a\u0629\3\2\2\2\u062b\u00b5\3\2\2")
        buf.write(u"\2\u062c\u062f\5\16\b\2\u062d\u062f\5\20\t\2\u062e\u062c")
        buf.write(u"\3\2\2\2\u062e\u062d\3\2\2\2\u062f\u00b7\3\2\2\2\u0630")
        buf.write(u"\u0635\5\u00c8e\2\u0631\u0632\7\23\2\2\u0632\u0634\5")
        buf.write(u"\u00c8e\2\u0633\u0631\3\2\2\2\u0634\u0637\3\2\2\2\u0635")
        buf.write(u"\u0633\3\2\2\2\u0635\u0636\3\2\2\2\u0636\u00b9\3\2\2")
        buf.write(u"\2\u0637\u0635\3\2\2\2\u0638\u063b\5\u00c4c\2\u0639\u063b")
        buf.write(u"\5\u00c8e\2\u063a\u0638\3\2\2\2\u063a\u0639\3\2\2\2\u063b")
        buf.write(u"\u00bb\3\2\2\2\u063c\u063f\5\u00c2b\2\u063d\u063f\5\u0130")
        buf.write(u"\u0099\2\u063e\u063c\3\2\2\2\u063e\u063d\3\2\2\2\u063f")
        buf.write(u"\u00bd\3\2\2\2\u0640\u0641\6`/\3\u0641\u0642\7#\2\2\u0642")
        buf.write(u"\u0643\5\u00c0a\2\u0643\u00bf\3\2\2\2\u0644\u0645\6a")
        buf.write(u"\60\3\u0645\u0646\5\u00bc_\2\u0646\u00c1\3\2\2\2\u0647")
        buf.write(u"\u064b\5\u00c4c\2\u0648\u064b\5\u00c8e\2\u0649\u064b")
        buf.write(u"\5\u00caf\2\u064a\u0647\3\2\2\2\u064a\u0648\3\2\2\2\u064a")
        buf.write(u"\u0649\3\2\2\2\u064b\u00c3\3\2\2\2\u064c\u064d\7\u00a8")
        buf.write(u"\2\2\u064d\u00c5\3\2\2\2\u064e\u064f\t\4\2\2\u064f\u00c7")
        buf.write(u"\3\2\2\2\u0650\u0651\7\u00a7\2\2\u0651\u00c9\3\2\2\2")
        buf.write(u"\u0652\u0653\7\u00a6\2\2\u0653\u00cb\3\2\2\2\u0654\u0659")
        buf.write(u"\5\u00ceh\2\u0655\u0656\7\23\2\2\u0656\u0658\5\u00ce")
        buf.write(u"h\2\u0657\u0655\3\2\2\2\u0658\u065b\3\2\2\2\u0659\u0657")
        buf.write(u"\3\2\2\2\u0659\u065a\3\2\2\2\u065a\u00cd\3\2\2\2\u065b")
        buf.write(u"\u0659\3\2\2\2\u065c\u0662\5\u00d4k\2\u065d\u065f\7z")
        buf.write(u"\2\2\u065e\u065d\3\2\2\2\u065e\u065f\3\2\2\2\u065f\u0660")
        buf.write(u"\3\2\2\2\u0660\u0662\5\u00d0i\2\u0661\u065c\3\2\2\2\u0661")
        buf.write(u"\u065e\3\2\2\2\u0662\u00cf\3\2\2\2\u0663\u0666\5\u00d2")
        buf.write(u"j\2\u0664\u0666\5\64\33\2\u0665\u0663\3\2\2\2\u0665\u0664")
        buf.write(u"\3\2\2\2\u0666\u00d1\3\2\2\2\u0667\u066a\5\u00c4c\2\u0668")
        buf.write(u"\u0669\7-\2\2\u0669\u066b\5\u0110\u0089\2\u066a\u0668")
        buf.write(u"\3\2\2\2\u066a\u066b\3\2\2\2\u066b\u00d3\3\2\2\2\u066c")
        buf.write(u"\u066d\5\u00b2Z\2\u066d\u066e\5\u00c4c\2\u066e\u00d5")
        buf.write(u"\3\2\2\2\u066f\u0672\5\u00a8U\2\u0670\u0672\5\u00d8m")
        buf.write(u"\2\u0671\u066f\3\2\2\2\u0671\u0670\3\2\2\2\u0672\u00d7")
        buf.write(u"\3\2\2\2\u0673\u0674\bm\1\2\u0674\u0675\7K\2\2\u0675")
        buf.write(u"\u067e\3\2\2\2\u0676\u0677\f\4\2\2\u0677\u0678\7\30\2")
        buf.write(u"\2\u0678\u067d\7\31\2\2\u0679\u067a\f\3\2\2\u067a\u067b")
        buf.write(u"\7\32\2\2\u067b\u067d\7\33\2\2\u067c\u0676\3\2\2\2\u067c")
        buf.write(u"\u0679\3\2\2\2\u067d\u0680\3\2\2\2\u067e\u067c\3\2\2")
        buf.write(u"\2\u067e\u067f\3\2\2\2\u067f\u00d9\3\2\2\2\u0680\u067e")
        buf.write(u"\3\2\2\2\u0681\u0687\5\u00dco\2\u0682\u0683\5\u0086D")
        buf.write(u"\2\u0683\u0684\5\u00dco\2\u0684\u0686\3\2\2\2\u0685\u0682")
        buf.write(u"\3\2\2\2\u0686\u0689\3\2\2\2\u0687\u0685\3\2\2\2\u0687")
        buf.write(u"\u0688\3\2\2\2\u0688\u00db\3\2\2\2\u0689\u0687\3\2\2")
        buf.write(u"\2\u068a\u0690\5\32\16\2\u068b\u0690\5\36\20\2\u068c")
        buf.write(u"\u0690\5,\27\2\u068d\u0690\5*\26\2\u068e\u0690\5\30\r")
        buf.write(u"\2\u068f\u068a\3\2\2\2\u068f\u068b\3\2\2\2\u068f\u068c")
        buf.write(u"\3\2\2\2\u068f\u068d\3\2\2\2\u068f\u068e\3\2\2\2\u0690")
        buf.write(u"\u00dd\3\2\2\2\u0691\u0697\5\u00e0q\2\u0692\u0693\5\u0086")
        buf.write(u"D\2\u0693\u0694\5\u00e0q\2\u0694\u0696\3\2\2\2\u0695")
        buf.write(u"\u0692\3\2\2\2\u0696\u0699\3\2\2\2\u0697\u0695\3\2\2")
        buf.write(u"\2\u0697\u0698\3\2\2\2\u0698\u00df\3\2\2\2\u0699\u0697")
        buf.write(u"\3\2\2\2\u069a\u069e\5 \21\2\u069b\u069e\5\34\17\2\u069c")
        buf.write(u"\u069e\5.\30\2\u069d\u069a\3\2\2\2\u069d\u069b\3\2\2")
        buf.write(u"\2\u069d\u069c\3\2\2\2\u069e\u00e1\3\2\2\2\u069f\u06a0")
        buf.write(u"\7\13\2\2\u06a0\u06aa\5\u0190\u00c9\2\u06a1\u06a2\7\f")
        buf.write(u"\2\2\u06a2\u06aa\5\u01aa\u00d6\2\u06a3\u06a4\7\r\2\2")
        buf.write(u"\u06a4\u06aa\5\u00e4s\2\u06a5\u06a6\7\16\2\2\u06a6\u06aa")
        buf.write(u"\5\u00e4s\2\u06a7\u06a8\7\17\2\2\u06a8\u06aa\5\u00e8")
        buf.write(u"u\2\u06a9\u069f\3\2\2\2\u06a9\u06a1\3\2\2\2\u06a9\u06a3")
        buf.write(u"\3\2\2\2\u06a9\u06a5\3\2\2\2\u06a9\u06a7\3\2\2\2\u06aa")
        buf.write(u"\u00e3\3\2\2\2\u06ab\u06ad\5\u00c2b\2\u06ac\u06ae\5\u00e6")
        buf.write(u"t\2\u06ad\u06ac\3\2\2\2\u06ad\u06ae\3\2\2\2\u06ae\u00e5")
        buf.write(u"\3\2\2\2\u06af\u06b0\7n\2\2\u06b0\u06b1\5\u0136\u009c")
        buf.write(u"\2\u06b1\u06b2\7\21\2\2\u06b2\u06b7\5\u00c2b\2\u06b3")
        buf.write(u"\u06b4\7\25\2\2\u06b4\u06b6\5\u00c2b\2\u06b5\u06b3\3")
        buf.write(u"\2\2\2\u06b6\u06b9\3\2\2\2\u06b7\u06b5\3\2\2\2\u06b7")
        buf.write(u"\u06b8\3\2\2\2\u06b8\u00e7\3\2\2\2\u06b9\u06b7\3\2\2")
        buf.write(u"\2\u06ba\u06bc\5\u00c2b\2\u06bb\u06bd\5\u00eav\2\u06bc")
        buf.write(u"\u06bb\3\2\2\2\u06bc\u06bd\3\2\2\2\u06bd\u00e9\3\2\2")
        buf.write(u"\2\u06be\u06bf\7n\2\2\u06bf\u06c0\5\u0136\u009c\2\u06c0")
        buf.write(u"\u06c2\7\21\2\2\u06c1\u06c3\7%\2\2\u06c2\u06c1\3\2\2")
        buf.write(u"\2\u06c2\u06c3\3\2\2\2\u06c3\u06c4\3\2\2\2\u06c4\u06c9")
        buf.write(u"\5\u015e\u00b0\2\u06c5\u06c6\7%\2\2\u06c6\u06c8\5\u015e")
        buf.write(u"\u00b0\2\u06c7\u06c5\3\2\2\2\u06c8\u06cb\3\2\2\2\u06c9")
        buf.write(u"\u06c7\3\2\2\2\u06c9\u06ca\3\2\2\2\u06ca\u06ce\3\2\2")
        buf.write(u"\2\u06cb\u06c9\3\2\2\2\u06cc\u06cd\7\25\2\2\u06cd\u06cf")
        buf.write(u"\5\u015e\u00b0\2\u06ce\u06cc\3\2\2\2\u06ce\u06cf\3\2")
        buf.write(u"\2\2\u06cf\u00eb\3\2\2\2\u06d0\u06d5\5\u00c4c\2\u06d1")
        buf.write(u"\u06d2\7\23\2\2\u06d2\u06d4\5\u00c4c\2\u06d3\u06d1\3")
        buf.write(u"\2\2\2\u06d4\u06d7\3\2\2\2\u06d5\u06d3\3\2\2\2\u06d5")
        buf.write(u"\u06d6\3\2\2\2\u06d6\u00ed\3\2\2\2\u06d7\u06d5\3\2\2")
        buf.write(u"\2\u06d8\u06dd\5\u00c6d\2\u06d9\u06da\7\23\2\2\u06da")
        buf.write(u"\u06dc\5\u00c6d\2\u06db\u06d9\3\2\2\2\u06dc\u06df\3\2")
        buf.write(u"\2\2\u06dd\u06db\3\2\2\2\u06dd\u06de\3\2\2\2\u06de\u00ef")
        buf.write(u"\3\2\2\2\u06df\u06dd\3\2\2\2\u06e0\u06e5\5*\26\2\u06e1")
        buf.write(u"\u06e5\5,\27\2\u06e2\u06e5\5.\30\2\u06e3\u06e5\5\60\31")
        buf.write(u"\2\u06e4\u06e0\3\2\2\2\u06e4\u06e1\3\2\2\2\u06e4\u06e2")
        buf.write(u"\3\2\2\2\u06e4\u06e3\3\2\2\2\u06e5\u00f1\3\2\2\2\u06e6")
        buf.write(u"\u06e7\7\n\2\2\u06e7\u00f3\3\2\2\2\u06e8\u06ee\5\u00f6")
        buf.write(u"|\2\u06e9\u06ea\5\u0086D\2\u06ea\u06eb\5\u00f6|\2\u06eb")
        buf.write(u"\u06ed\3\2\2\2\u06ec\u06e9\3\2\2\2\u06ed\u06f0\3\2\2")
        buf.write(u"\2\u06ee\u06ec\3\2\2\2\u06ee\u06ef\3\2\2\2\u06ef\u00f5")
        buf.write(u"\3\2\2\2\u06f0\u06ee\3\2\2\2\u06f1\u06f2\7\13\2\2\u06f2")
        buf.write(u"\u06fc\5\u017a\u00be\2\u06f3\u06f4\7\f\2\2\u06f4\u06fc")
        buf.write(u"\5\u0196\u00cc\2\u06f5\u06f6\7\r\2\2\u06f6\u06fc\5\u00f8")
        buf.write(u"}\2\u06f7\u06f8\7\16\2\2\u06f8\u06fc\5\u00f8}\2\u06f9")
        buf.write(u"\u06fa\7\17\2\2\u06fa\u06fc\5\u00fa~\2\u06fb\u06f1\3")
        buf.write(u"\2\2\2\u06fb\u06f3\3\2\2\2\u06fb\u06f5\3\2\2\2\u06fb")
        buf.write(u"\u06f7\3\2\2\2\u06fb\u06f9\3\2\2\2\u06fc\u00f7\3\2\2")
        buf.write(u"\2\u06fd\u06ff\5\u0160\u00b1\2\u06fe\u0700\7\22\2\2\u06ff")
        buf.write(u"\u06fe\3\2\2\2\u06ff\u0700\3\2\2\2\u0700\u0702\3\2\2")
        buf.write(u"\2\u0701\u0703\5\u00e6t\2\u0702\u0701\3\2\2\2\u0702\u0703")
        buf.write(u"\3\2\2\2\u0703\u00f9\3\2\2\2\u0704\u0706\5\u0146\u00a4")
        buf.write(u"\2\u0705\u0707\7\22\2\2\u0706\u0705\3\2\2\2\u0706\u0707")
        buf.write(u"\3\2\2\2\u0707\u0709\3\2\2\2\u0708\u070a\5\u00eav\2\u0709")
        buf.write(u"\u0708\3\2\2\2\u0709\u070a\3\2\2\2\u070a\u00fb\3\2\2")
        buf.write(u"\2\u070b\u0711\5\66\34\2\u070c\u070d\5\u0086D\2\u070d")
        buf.write(u"\u070e\5\66\34\2\u070e\u0710\3\2\2\2\u070f\u070c\3\2")
        buf.write(u"\2\2\u0710\u0713\3\2\2\2\u0711\u070f\3\2\2\2\u0711\u0712")
        buf.write(u"\3\2\2\2\u0712\u00fd\3\2\2\2\u0713\u0711\3\2\2\2\u0714")
        buf.write(u"\u071a\5\62\32\2\u0715\u0716\5\u0086D\2\u0716\u0717\5")
        buf.write(u"\62\32\2\u0717\u0719\3\2\2\2\u0718\u0715\3\2\2\2\u0719")
        buf.write(u"\u071c\3\2\2\2\u071a\u0718\3\2\2\2\u071a\u071b\3\2\2")
        buf.write(u"\2\u071b\u00ff\3\2\2\2\u071c\u071a\3\2\2\2\u071d\u0723")
        buf.write(u"\5J&\2\u071e\u071f\5\u0086D\2\u071f\u0720\5J&\2\u0720")
        buf.write(u"\u0722\3\2\2\2\u0721\u071e\3\2\2\2\u0722\u0725\3\2\2")
        buf.write(u"\2\u0723\u0721\3\2\2\2\u0723\u0724\3\2\2\2\u0724\u0101")
        buf.write(u"\3\2\2\2\u0725\u0723\3\2\2\2\u0726\u072c\5Z.\2\u0727")
        buf.write(u"\u0728\5\u0086D\2\u0728\u0729\5Z.\2\u0729\u072b\3\2\2")
        buf.write(u"\2\u072a\u0727\3\2\2\2\u072b\u072e\3\2\2\2\u072c\u072a")
        buf.write(u"\3\2\2\2\u072c\u072d\3\2\2\2\u072d\u0103\3\2\2\2\u072e")
        buf.write(u"\u072c\3\2\2\2\u072f\u0730\7\30\2\2\u0730\u0731\5\u0106")
        buf.write(u"\u0084\2\u0731\u0732\7\24\2\2\u0732\u0733\5\u0106\u0084")
        buf.write(u"\2\u0733\u0734\7\31\2\2\u0734\u073e\3\2\2\2\u0735\u0736")
        buf.write(u"\7\30\2\2\u0736\u0737\5\u0108\u0085\2\u0737\u0738\7\31")
        buf.write(u"\2\2\u0738\u073e\3\2\2\2\u0739\u073a\7*\2\2\u073a\u073b")
        buf.write(u"\5\u0108\u0085\2\u073b\u073c\7(\2\2\u073c\u073e\3\2\2")
        buf.write(u"\2\u073d\u072f\3\2\2\2\u073d\u0735\3\2\2\2\u073d\u0739")
        buf.write(u"\3\2\2\2\u073e\u0105\3\2\2\2\u073f\u074f\7\u00a4\2\2")
        buf.write(u"\u0740\u074f\7\u00a5\2\2\u0741\u074f\7\u00ad\2\2\u0742")
        buf.write(u"\u074f\7\u00ae\2\2\u0743\u074f\7\u00a3\2\2\u0744\u074f")
        buf.write(u"\7\u00b2\2\2\u0745\u074f\7\u00b1\2\2\u0746\u074f\7\u00ab")
        buf.write(u"\2\2\u0747\u074f\7\u00af\2\2\u0748\u074f\7\u00b0\2\2")
        buf.write(u"\u0749\u074f\7\u00a2\2\2\u074a\u074f\7\u00b3\2\2\u074b")
        buf.write(u"\u074f\7\u00b4\2\2\u074c\u074f\7\u00ac\2\2\u074d\u074f")
        buf.write(u"\5\u008cG\2\u074e\u073f\3\2\2\2\u074e\u0740\3\2\2\2\u074e")
        buf.write(u"\u0741\3\2\2\2\u074e\u0742\3\2\2\2\u074e\u0743\3\2\2")
        buf.write(u"\2\u074e\u0744\3\2\2\2\u074e\u0745\3\2\2\2\u074e\u0746")
        buf.write(u"\3\2\2\2\u074e\u0747\3\2\2\2\u074e\u0748\3\2\2\2\u074e")
        buf.write(u"\u0749\3\2\2\2\u074e\u074a\3\2\2\2\u074e\u074b\3\2\2")
        buf.write(u"\2\u074e\u074c\3\2\2\2\u074e\u074d\3\2\2\2\u074f\u0107")
        buf.write(u"\3\2\2\2\u0750\u0755\5\u0106\u0084\2\u0751\u0752\7\23")
        buf.write(u"\2\2\u0752\u0754\5\u0106\u0084\2\u0753\u0751\3\2\2\2")
        buf.write(u"\u0754\u0757\3\2\2\2\u0755\u0753\3\2\2\2\u0755\u0756")
        buf.write(u"\3\2\2\2\u0756\u0109\3\2\2\2\u0757\u0755\3\2\2\2\u0758")
        buf.write(u"\u075d\5\u010e\u0088\2\u0759\u075d\5\u0110\u0089\2\u075a")
        buf.write(u"\u075d\5\u00c2b\2\u075b\u075d\5\u010c\u0087\2\u075c\u0758")
        buf.write(u"\3\2\2\2\u075c\u0759\3\2\2\2\u075c\u075a\3\2\2\2\u075c")
        buf.write(u"\u075b\3\2\2\2\u075d\u010b\3\2\2\2\u075e\u075f\t\5\2")
        buf.write(u"\2\u075f\u010d\3\2\2\2\u0760\u0761\7\26\2\2\u0761\u0762")
        buf.write(u"\5`\61\2\u0762\u0763\7\27\2\2\u0763\u010f\3\2\2\2\u0764")
        buf.write(u"\u0767\5\u0106\u0084\2\u0765\u0767\5\u0112\u008a\2\u0766")
        buf.write(u"\u0764\3\2\2\2\u0766\u0765\3\2\2\2\u0767\u0111\3\2\2")
        buf.write(u"\2\u0768\u076e\5\u00a6T\2\u0769\u076e\5\u00a0Q\2\u076a")
        buf.write(u"\u076e\5\u00a2R\2\u076b\u076e\5\u0116\u008c\2\u076c\u076e")
        buf.write(u"\5\u0114\u008b\2\u076d\u0768\3\2\2\2\u076d\u0769\3\2")
        buf.write(u"\2\2\u076d\u076a\3\2\2\2\u076d\u076b\3\2\2\2\u076d\u076c")
        buf.write(u"\3\2\2\2\u076e\u0113\3\2\2\2\u076f\u0771\7z\2\2\u0770")
        buf.write(u"\u076f\3\2\2\2\u0770\u0771\3\2\2\2\u0771\u0772\3\2\2")
        buf.write(u"\2\u0772\u0774\7\26\2\2\u0773\u0775\5\u0118\u008d\2\u0774")
        buf.write(u"\u0773\3\2\2\2\u0774\u0775\3\2\2\2\u0775\u0776\3\2\2")
        buf.write(u"\2\u0776\u0777\7\27\2\2\u0777\u0115\3\2\2\2\u0778\u077a")
        buf.write(u"\7z\2\2\u0779\u0778\3\2\2\2\u0779\u077a\3\2\2\2\u077a")
        buf.write(u"\u077b\3\2\2\2\u077b\u077d\7\32\2\2\u077c\u077e\5\u011a")
        buf.write(u"\u008e\2\u077d\u077c\3\2\2\2\u077d\u077e\3\2\2\2\u077e")
        buf.write(u"\u077f\3\2\2\2\u077f\u0780\7\33\2\2\u0780\u0117\3\2\2")
        buf.write(u"\2\u0781\u0782\5`\61\2\u0782\u078b\7\23\2\2\u0783\u0788")
        buf.write(u"\5`\61\2\u0784\u0785\7\23\2\2\u0785\u0787\5`\61\2\u0786")
        buf.write(u"\u0784\3\2\2\2\u0787\u078a\3\2\2\2\u0788\u0786\3\2\2")
        buf.write(u"\2\u0788\u0789\3\2\2\2\u0789\u078c\3\2\2\2\u078a\u0788")
        buf.write(u"\3\2\2\2\u078b\u0783\3\2\2\2\u078b\u078c\3\2\2\2\u078c")
        buf.write(u"\u0119\3\2\2\2\u078d\u0792\5\u011c\u008f\2\u078e\u078f")
        buf.write(u"\7\23\2\2\u078f\u0791\5\u011c\u008f\2\u0790\u078e\3\2")
        buf.write(u"\2\2\u0791\u0794\3\2\2\2\u0792\u0790\3\2\2\2\u0792\u0793")
        buf.write(u"\3\2\2\2\u0793\u011b\3\2\2\2\u0794\u0792\3\2\2\2\u0795")
        buf.write(u"\u0796\5`\61\2\u0796\u0797\7\21\2\2\u0797\u0798\5`\61")
        buf.write(u"\2\u0798\u011d\3\2\2\2\u0799\u079a\5`\61\2\u079a\u079b")
        buf.write(u"\7\21\2\2\u079b\u079c\5`\61\2\u079c\u07a3\3\2\2\2\u079d")
        buf.write(u"\u079e\5`\61\2\u079e\u079f\7\21\2\2\u079f\u07a3\3\2\2")
        buf.write(u"\2\u07a0\u07a1\7\21\2\2\u07a1\u07a3\5`\61\2\u07a2\u0799")
        buf.write(u"\3\2\2\2\u07a2\u079d\3\2\2\2\u07a2\u07a0\3\2\2\2\u07a3")
        buf.write(u"\u011f\3\2\2\2\u07a4\u07a5\5\u00c4c\2\u07a5\u07a6\5\u013c")
        buf.write(u"\u009f\2\u07a6\u07a7\5`\61\2\u07a7\u0121\3\2\2\2\u07a8")
        buf.write(u"\u07a9\b\u0092\1\2\u07a9\u07aa\5\u00c4c\2\u07aa\u07af")
        buf.write(u"\3\2\2\2\u07ab\u07ac\f\3\2\2\u07ac\u07ae\5\u0080A\2\u07ad")
        buf.write(u"\u07ab\3\2\2\2\u07ae\u07b1\3\2\2\2\u07af\u07ad\3\2\2")
        buf.write(u"\2\u07af\u07b0\3\2\2\2\u07b0\u0123\3\2\2\2\u07b1\u07af")
        buf.write(u"\3\2\2\2\u07b2\u07b3\6\u0093\64\3\u07b3\u07b4\7\u00a8")
        buf.write(u"\2\2\u07b4\u07b7\5\u00d6l\2\u07b5\u07b7\5`\61\2\u07b6")
        buf.write(u"\u07b2\3\2\2\2\u07b6\u07b5\3\2\2\2\u07b7\u0125\3\2\2")
        buf.write(u"\2\u07b8\u07b9\7\u0089\2\2\u07b9\u07ba\7H\2\2\u07ba\u07bb")
        buf.write(u"\7n\2\2\u07bb\u07bc\5`\61\2\u07bc\u0127\3\2\2\2\u07bd")
        buf.write(u"\u07be\7\u0089\2\2\u07be\u07bf\7\u0081\2\2\u07bf\u07c0")
        buf.write(u"\7n\2\2\u07c0\u07c1\5`\61\2\u07c1\u0129\3\2\2\2\u07c2")
        buf.write(u"\u07c7\5\u012c\u0097\2\u07c3\u07c4\7\23\2\2\u07c4\u07c6")
        buf.write(u"\5\u012c\u0097\2\u07c5\u07c3\3\2\2\2\u07c6\u07c9\3\2")
        buf.write(u"\2\2\u07c7\u07c5\3\2\2\2\u07c7\u07c8\3\2\2\2\u07c8\u012b")
        buf.write(u"\3\2\2\2\u07c9\u07c7\3\2\2\2\u07ca\u07cf\5\u00c4c\2\u07cb")
        buf.write(u"\u07cc\7\25\2\2\u07cc\u07ce\5\u00c4c\2\u07cd\u07cb\3")
        buf.write(u"\2\2\2\u07ce\u07d1\3\2\2\2\u07cf\u07cd\3\2\2\2\u07cf")
        buf.write(u"\u07d0\3\2\2\2\u07d0\u07d3\3\2\2\2\u07d1\u07cf\3\2\2")
        buf.write(u"\2\u07d2\u07d4\t\6\2\2\u07d3\u07d2\3\2\2\2\u07d3\u07d4")
        buf.write(u"\3\2\2\2\u07d4\u012d\3\2\2\2\u07d5\u07dc\7\"\2\2\u07d6")
        buf.write(u"\u07dc\7#\2\2\u07d7\u07dc\5\u013e\u00a0\2\u07d8\u07dc")
        buf.write(u"\5\u0140\u00a1\2\u07d9\u07dc\5\u0142\u00a2\2\u07da\u07dc")
        buf.write(u"\5\u0144\u00a3\2\u07db\u07d5\3\2\2\2\u07db\u07d6\3\2")
        buf.write(u"\2\2\u07db\u07d7\3\2\2\2\u07db\u07d8\3\2\2\2\u07db\u07d9")
        buf.write(u"\3\2\2\2\u07db\u07da\3\2\2\2\u07dc\u012f\3\2\2\2\u07dd")
        buf.write(u"\u07de\t\7\2\2\u07de\u0131\3\2\2\2\u07df\u07e0\7\u00a8")
        buf.write(u"\2\2\u07e0\u07e1\6\u009a\65\3\u07e1\u0133\3\2\2\2\u07e2")
        buf.write(u"\u07e3\7\u00a8\2\2\u07e3\u07e4\6\u009b\66\3\u07e4\u0135")
        buf.write(u"\3\2\2\2\u07e5\u07e6\7\u00a8\2\2\u07e6\u07e7\6\u009c")
        buf.write(u"\67\3\u07e7\u0137\3\2\2\2\u07e8\u07e9\7\u00a8\2\2\u07e9")
        buf.write(u"\u07ea\6\u009d8\3\u07ea\u0139\3\2\2\2\u07eb\u07ec\7\u00a8")
        buf.write(u"\2\2\u07ec\u07ed\6\u009e9\3\u07ed\u013b\3\2\2\2\u07ee")
        buf.write(u"\u07ef\7-\2\2\u07ef\u013d\3\2\2\2\u07f0\u07f1\7$\2\2")
        buf.write(u"\u07f1\u013f\3\2\2\2\u07f2\u07f3\7%\2\2\u07f3\u0141\3")
        buf.write(u"\2\2\2\u07f4\u07f5\7&\2\2\u07f5\u0143\3\2\2\2\u07f6\u07f7")
        buf.write(u"\t\b\2\2\u07f7\u0145\3\2\2\2\u07f8\u07f9\7\u008c\2\2")
        buf.write(u"\u07f9\u07fa\5\u0148\u00a5\2\u07fa\u07fb\7\22\2\2\u07fb")
        buf.write(u"\u0800\3\2\2\2\u07fc\u07fd\5\u0148\u00a5\2\u07fd\u07fe")
        buf.write(u"\7\22\2\2\u07fe\u0800\3\2\2\2\u07ff\u07f8\3\2\2\2\u07ff")
        buf.write(u"\u07fc\3\2\2\2\u0800\u0147\3\2\2\2\u0801\u0802\b\u00a5")
        buf.write(u"\1\2\u0802\u0803\5\u014a\u00a6\2\u0803\u0808\3\2\2\2")
        buf.write(u"\u0804\u0805\f\3\2\2\u0805\u0807\5\u0150\u00a9\2\u0806")
        buf.write(u"\u0804\3\2\2\2\u0807\u080a\3\2\2\2\u0808\u0806\3\2\2")
        buf.write(u"\2\u0808\u0809\3\2\2\2\u0809\u0149\3\2\2\2\u080a\u0808")
        buf.write(u"\3\2\2\2\u080b\u0813\5\u014c\u00a7\2\u080c\u0813\5\u014e")
        buf.write(u"\u00a8\2\u080d\u0813\5\u0158\u00ad\2\u080e\u0813\5\u015a")
        buf.write(u"\u00ae\2\u080f\u0813\5\u015c\u00af\2\u0810\u0813\5\u0152")
        buf.write(u"\u00aa\2\u0811\u0813\5\u0156\u00ac\2\u0812\u080b\3\2")
        buf.write(u"\2\2\u0812\u080c\3\2\2\2\u0812\u080d\3\2\2\2\u0812\u080e")
        buf.write(u"\3\2\2\2\u0812\u080f\3\2\2\2\u0812\u0810\3\2\2\2\u0812")
        buf.write(u"\u0811\3\2\2\2\u0813\u014b\3\2\2\2\u0814\u0815\5\u010c")
        buf.write(u"\u0087\2\u0815\u014d\3\2\2\2\u0816\u0817\5\u0132\u009a")
        buf.write(u"\2\u0817\u0818\5\u0152\u00aa\2\u0818\u014f\3\2\2\2\u0819")
        buf.write(u"\u081a\7\25\2\2\u081a\u081f\5\u0152\u00aa\2\u081b\u081c")
        buf.write(u"\7\25\2\2\u081c\u081f\5\u015e\u00b0\2\u081d\u081f\5\u0156")
        buf.write(u"\u00ac\2\u081e\u0819\3\2\2\2\u081e\u081b\3\2\2\2\u081e")
        buf.write(u"\u081d\3\2\2\2\u081f\u0151\3\2\2\2\u0820\u0821\5\u015e")
        buf.write(u"\u00b0\2\u0821\u0823\7\26\2\2\u0822\u0824\5\u0154\u00ab")
        buf.write(u"\2\u0823\u0822\3\2\2\2\u0823\u0824\3\2\2\2\u0824\u0825")
        buf.write(u"\3\2\2\2\u0825\u0826\7\27\2\2\u0826\u0153\3\2\2\2\u0827")
        buf.write(u"\u0828\b\u00ab\1\2\u0828\u0829\5\u0148\u00a5\2\u0829")
        buf.write(u"\u082f\3\2\2\2\u082a\u082b\f\3\2\2\u082b\u082c\7\23\2")
        buf.write(u"\2\u082c\u082e\5\u0148\u00a5\2\u082d\u082a\3\2\2\2\u082e")
        buf.write(u"\u0831\3\2\2\2\u082f\u082d\3\2\2\2\u082f\u0830\3\2\2")
        buf.write(u"\2\u0830\u0155\3\2\2\2\u0831\u082f\3\2\2\2\u0832\u0833")
        buf.write(u"\7\30\2\2\u0833\u0834\5\u0148\u00a5\2\u0834\u0835\7\31")
        buf.write(u"\2\2\u0835\u0157\3\2\2\2\u0836\u0837\7\26\2\2\u0837\u0838")
        buf.write(u"\5\u0148\u00a5\2\u0838\u0839\7\27\2\2\u0839\u0159\3\2")
        buf.write(u"\2\2\u083a\u083b\5\u015e\u00b0\2\u083b\u015b\3\2\2\2")
        buf.write(u"\u083c\u0842\7\u00ad\2\2\u083d\u0842\7\u00af\2\2\u083e")
        buf.write(u"\u0842\7\u00ab\2\2\u083f\u0842\7\u00a2\2\2\u0840\u0842")
        buf.write(u"\7\u00a3\2\2\u0841\u083c\3\2\2\2\u0841\u083d\3\2\2\2")
        buf.write(u"\u0841\u083e\3\2\2\2\u0841\u083f\3\2\2\2\u0841\u0840")
        buf.write(u"\3\2\2\2\u0842\u015d\3\2\2\2\u0843\u0844\t\t\2\2\u0844")
        buf.write(u"\u015f\3\2\2\2\u0845\u0846\7\u008c\2\2\u0846\u0849\5")
        buf.write(u"\u0162\u00b2\2\u0847\u0849\5\u0162\u00b2\2\u0848\u0845")
        buf.write(u"\3\2\2\2\u0848\u0847\3\2\2\2\u0849\u0161\3\2\2\2\u084a")
        buf.write(u"\u084b\b\u00b2\1\2\u084b\u084c\5\u0164\u00b3\2\u084c")
        buf.write(u"\u0851\3\2\2\2\u084d\u084e\f\3\2\2\u084e\u0850\5\u0168")
        buf.write(u"\u00b5\2\u084f\u084d\3\2\2\2\u0850\u0853\3\2\2\2\u0851")
        buf.write(u"\u084f\3\2\2\2\u0851\u0852\3\2\2\2\u0852\u0163\3\2\2")
        buf.write(u"\2\u0853\u0851\3\2\2\2\u0854\u085a\5\u0166\u00b4\2\u0855")
        buf.write(u"\u085a\5\u0172\u00ba\2\u0856\u085a\5\u0174\u00bb\2\u0857")
        buf.write(u"\u085a\5\u0176\u00bc\2\u0858\u085a\5\u016a\u00b6\2\u0859")
        buf.write(u"\u0854\3\2\2\2\u0859\u0855\3\2\2\2\u0859\u0856\3\2\2")
        buf.write(u"\2\u0859\u0857\3\2\2\2\u0859\u0858\3\2\2\2\u085a\u0165")
        buf.write(u"\3\2\2\2\u085b\u085c\5\u010c\u0087\2\u085c\u0167\3\2")
        buf.write(u"\2\2\u085d\u085e\7\25\2\2\u085e\u0864\5\u016a\u00b6\2")
        buf.write(u"\u085f\u0860\7\30\2\2\u0860\u0861\5\u0162\u00b2\2\u0861")
        buf.write(u"\u0862\7\31\2\2\u0862\u0864\3\2\2\2\u0863\u085d\3\2\2")
        buf.write(u"\2\u0863\u085f\3\2\2\2\u0864\u0169\3\2\2\2\u0865\u0866")
        buf.write(u"\5\u0178\u00bd\2\u0866\u0868\7\26\2\2\u0867\u0869\5\u016c")
        buf.write(u"\u00b7\2\u0868\u0867\3\2\2\2\u0868\u0869\3\2\2\2\u0869")
        buf.write(u"\u086a\3\2\2\2\u086a\u086b\7\27\2\2\u086b\u016b\3\2\2")
        buf.write(u"\2\u086c\u0873\5\u016e\u00b8\2\u086d\u0873\5\u0170\u00b9")
        buf.write(u"\2\u086e\u086f\5\u016e\u00b8\2\u086f\u0870\7\23\2\2\u0870")
        buf.write(u"\u0871\5\u0170\u00b9\2\u0871\u0873\3\2\2\2\u0872\u086c")
        buf.write(u"\3\2\2\2\u0872\u086d\3\2\2\2\u0872\u086e\3\2\2\2\u0873")
        buf.write(u"\u016d\3\2\2\2\u0874\u0875\b\u00b8\1\2\u0875\u0876\5")
        buf.write(u"\u0162\u00b2\2\u0876\u087c\3\2\2\2\u0877\u0878\f\3\2")
        buf.write(u"\2\u0878\u0879\7\23\2\2\u0879\u087b\5\u0162\u00b2\2\u087a")
        buf.write(u"\u0877\3\2\2\2\u087b\u087e\3\2\2\2\u087c\u087a\3\2\2")
        buf.write(u"\2\u087c\u087d\3\2\2\2\u087d\u016f\3\2\2\2\u087e\u087c")
        buf.write(u"\3\2\2\2\u087f\u0880\b\u00b9\1\2\u0880\u0881\5\u0178")
        buf.write(u"\u00bd\2\u0881\u0882\7-\2\2\u0882\u0883\5\u0162\u00b2")
        buf.write(u"\2\u0883\u088c\3\2\2\2\u0884\u0885\f\3\2\2\u0885\u0886")
        buf.write(u"\7\23\2\2\u0886\u0887\5\u0178\u00bd\2\u0887\u0888\7-")
        buf.write(u"\2\2\u0888\u0889\5\u0162\u00b2\2\u0889\u088b\3\2\2\2")
        buf.write(u"\u088a\u0884\3\2\2\2\u088b\u088e\3\2\2\2\u088c\u088a")
        buf.write(u"\3\2\2\2\u088c\u088d\3\2\2\2\u088d\u0171\3\2\2\2\u088e")
        buf.write(u"\u088c\3\2\2\2\u088f\u0890\7\26\2\2\u0890\u0891\5\u0162")
        buf.write(u"\u00b2\2\u0891\u0892\7\27\2\2\u0892\u0173\3\2\2\2\u0893")
        buf.write(u"\u0894\b\u00bb\1\2\u0894\u0897\7\u00aa\2\2\u0895\u0897")
        buf.write(u"\5\u0178\u00bd\2\u0896\u0893\3\2\2\2\u0896\u0895\3\2")
        buf.write(u"\2\2\u0897\u089d\3\2\2\2\u0898\u0899\f\3\2\2\u0899\u089a")
        buf.write(u"\7\25\2\2\u089a\u089c\5\u0178\u00bd\2\u089b\u0898\3\2")
        buf.write(u"\2\2\u089c\u089f\3\2\2\2\u089d\u089b\3\2\2\2\u089d\u089e")
        buf.write(u"\3\2\2\2\u089e\u0175\3\2\2\2\u089f\u089d\3\2\2\2\u08a0")
        buf.write(u"\u08a6\7\u00ad\2\2\u08a1\u08a6\7\u00af\2\2\u08a2\u08a6")
        buf.write(u"\7\u00ab\2\2\u08a3\u08a6\7\u00a2\2\2\u08a4\u08a6\7\u00a3")
        buf.write(u"\2\2\u08a5\u08a0\3\2\2\2\u08a5\u08a1\3\2\2\2\u08a5\u08a2")
        buf.write(u"\3\2\2\2\u08a5\u08a3\3\2\2\2\u08a5\u08a4\3\2\2\2\u08a6")
        buf.write(u"\u0177\3\2\2\2\u08a7\u08a8\t\n\2\2\u08a8\u0179\3\2\2")
        buf.write(u"\2\u08a9\u08aa\7\u008c\2\2\u08aa\u08ab\5\u017c\u00bf")
        buf.write(u"\2\u08ab\u08ac\7\22\2\2\u08ac\u08b1\3\2\2\2\u08ad\u08ae")
        buf.write(u"\5\u017c\u00bf\2\u08ae\u08af\7\22\2\2\u08af\u08b1\3\2")
        buf.write(u"\2\2\u08b0\u08a9\3\2\2\2\u08b0\u08ad\3\2\2\2\u08b1\u017b")
        buf.write(u"\3\2\2\2\u08b2\u08b3\b\u00bf\1\2\u08b3\u08b4\5\u017e")
        buf.write(u"\u00c0\2\u08b4\u08b9\3\2\2\2\u08b5\u08b6\f\3\2\2\u08b6")
        buf.write(u"\u08b8\5\u0184\u00c3\2\u08b7\u08b5\3\2\2\2\u08b8\u08bb")
        buf.write(u"\3\2\2\2\u08b9\u08b7\3\2\2\2\u08b9\u08ba\3\2\2\2\u08ba")
        buf.write(u"\u017d\3\2\2\2\u08bb\u08b9\3\2\2\2\u08bc\u08c2\5\u0180")
        buf.write(u"\u00c1\2\u08bd\u08c2\5\u0182\u00c2\2\u08be\u08c2\5\u018c")
        buf.write(u"\u00c7\2\u08bf\u08c2\5\u018e\u00c8\2\u08c0\u08c2\5\u0192")
        buf.write(u"\u00ca\2\u08c1\u08bc\3\2\2\2\u08c1\u08bd\3\2\2\2\u08c1")
        buf.write(u"\u08be\3\2\2\2\u08c1\u08bf\3\2\2\2\u08c1\u08c0\3\2\2")
        buf.write(u"\2\u08c2\u017f\3\2\2\2\u08c3\u08c4\5\u010c\u0087\2\u08c4")
        buf.write(u"\u0181\3\2\2\2\u08c5\u08c6\5\u0132\u009a\2\u08c6\u08c7")
        buf.write(u"\5\u0186\u00c4\2\u08c7\u0183\3\2\2\2\u08c8\u08c9\7\25")
        buf.write(u"\2\2\u08c9\u08cc\5\u0186\u00c4\2\u08ca\u08cc\5\u018a")
        buf.write(u"\u00c6\2\u08cb\u08c8\3\2\2\2\u08cb\u08ca\3\2\2\2\u08cc")
        buf.write(u"\u0185\3\2\2\2\u08cd\u08ce\5\u0194\u00cb\2\u08ce\u08d0")
        buf.write(u"\7\26\2\2\u08cf\u08d1\5\u0188\u00c5\2\u08d0\u08cf\3\2")
        buf.write(u"\2\2\u08d0\u08d1\3\2\2\2\u08d1\u08d2\3\2\2\2\u08d2\u08d3")
        buf.write(u"\7\27\2\2\u08d3\u0187\3\2\2\2\u08d4\u08d5\b\u00c5\1\2")
        buf.write(u"\u08d5\u08d6\5\u017c\u00bf\2\u08d6\u08dc\3\2\2\2\u08d7")
        buf.write(u"\u08d8\f\3\2\2\u08d8\u08d9\7\23\2\2\u08d9\u08db\5\u017c")
        buf.write(u"\u00bf\2\u08da\u08d7\3\2\2\2\u08db\u08de\3\2\2\2\u08dc")
        buf.write(u"\u08da\3\2\2\2\u08dc\u08dd\3\2\2\2\u08dd\u0189\3\2\2")
        buf.write(u"\2\u08de\u08dc\3\2\2\2\u08df\u08e0\7\30\2\2\u08e0\u08e1")
        buf.write(u"\5\u017c\u00bf\2\u08e1\u08e2\7\31\2\2\u08e2\u018b\3\2")
        buf.write(u"\2\2\u08e3\u08e4\7\26\2\2\u08e4\u08e5\5\u017c\u00bf\2")
        buf.write(u"\u08e5\u08e6\7\27\2\2\u08e6\u018d\3\2\2\2\u08e7\u08e8")
        buf.write(u"\b\u00c8\1\2\u08e8\u08e9\5\u0194\u00cb\2\u08e9\u08ef")
        buf.write(u"\3\2\2\2\u08ea\u08eb\f\3\2\2\u08eb\u08ec\7\25\2\2\u08ec")
        buf.write(u"\u08ee\5\u0194\u00cb\2\u08ed\u08ea\3\2\2\2\u08ee\u08f1")
        buf.write(u"\3\2\2\2\u08ef\u08ed\3\2\2\2\u08ef\u08f0\3\2\2\2\u08f0")
        buf.write(u"\u018f\3\2\2\2\u08f1\u08ef\3\2\2\2\u08f2\u08f3\b\u00c9")
        buf.write(u"\1\2\u08f3\u08f4\5\u018e\u00c8\2\u08f4\u08f9\3\2\2\2")
        buf.write(u"\u08f5\u08f6\f\3\2\2\u08f6\u08f8\7\u00aa\2\2\u08f7\u08f5")
        buf.write(u"\3\2\2\2\u08f8\u08fb\3\2\2\2\u08f9\u08f7\3\2\2\2\u08f9")
        buf.write(u"\u08fa\3\2\2\2\u08fa\u0191\3\2\2\2\u08fb\u08f9\3\2\2")
        buf.write(u"\2\u08fc\u0902\7\u00ad\2\2\u08fd\u0902\7\u00af\2\2\u08fe")
        buf.write(u"\u0902\7\u00ab\2\2\u08ff\u0902\7\u00a2\2\2\u0900\u0902")
        buf.write(u"\7\u00a3\2\2\u0901\u08fc\3\2\2\2\u0901\u08fd\3\2\2\2")
        buf.write(u"\u0901\u08fe\3\2\2\2\u0901\u08ff\3\2\2\2\u0901\u0900")
        buf.write(u"\3\2\2\2\u0902\u0193\3\2\2\2\u0903\u0904\t\13\2\2\u0904")
        buf.write(u"\u0195\3\2\2\2\u0905\u0906\7\u008c\2\2\u0906\u0907\5")
        buf.write(u"\u0198\u00cd\2\u0907\u0908\7\22\2\2\u0908\u090d\3\2\2")
        buf.write(u"\2\u0909\u090a\5\u0198\u00cd\2\u090a\u090b\7\22\2\2\u090b")
        buf.write(u"\u090d\3\2\2\2\u090c\u0905\3\2\2\2\u090c\u0909\3\2\2")
        buf.write(u"\2\u090d\u0197\3\2\2\2\u090e\u090f\b\u00cd\1\2\u090f")
        buf.write(u"\u0910\5\u019a\u00ce\2\u0910\u0915\3\2\2\2\u0911\u0912")
        buf.write(u"\f\3\2\2\u0912\u0914\5\u01a0\u00d1\2\u0913\u0911\3\2")
        buf.write(u"\2\2\u0914\u0917\3\2\2\2\u0915\u0913\3\2\2\2\u0915\u0916")
        buf.write(u"\3\2\2\2\u0916\u0199\3\2\2\2\u0917\u0915\3\2\2\2\u0918")
        buf.write(u"\u091e\5\u019c\u00cf\2\u0919\u091e\5\u019e\u00d0\2\u091a")
        buf.write(u"\u091e\5\u01a8\u00d5\2\u091b\u091e\5\u01aa\u00d6\2\u091c")
        buf.write(u"\u091e\5\u01ac\u00d7\2\u091d\u0918\3\2\2\2\u091d\u0919")
        buf.write(u"\3\2\2\2\u091d\u091a\3\2\2\2\u091d\u091b\3\2\2\2\u091d")
        buf.write(u"\u091c\3\2\2\2\u091e\u019b\3\2\2\2\u091f\u0920\5\u010c")
        buf.write(u"\u0087\2\u0920\u019d\3\2\2\2\u0921\u0922\5\u0132\u009a")
        buf.write(u"\2\u0922\u0923\5\u01a2\u00d2\2\u0923\u019f\3\2\2\2\u0924")
        buf.write(u"\u0925\7\25\2\2\u0925\u0928\5\u01a2\u00d2\2\u0926\u0928")
        buf.write(u"\5\u01a6\u00d4\2\u0927\u0924\3\2\2\2\u0927\u0926\3\2")
        buf.write(u"\2\2\u0928\u01a1\3\2\2\2\u0929\u092a\5\u01ae\u00d8\2")
        buf.write(u"\u092a\u092c\7\26\2\2\u092b\u092d\5\u01a4\u00d3\2\u092c")
        buf.write(u"\u092b\3\2\2\2\u092c\u092d\3\2\2\2\u092d\u092e\3\2\2")
        buf.write(u"\2\u092e\u092f\7\27\2\2\u092f\u01a3\3\2\2\2\u0930\u0931")
        buf.write(u"\b\u00d3\1\2\u0931\u0932\5\u0198\u00cd\2\u0932\u0938")
        buf.write(u"\3\2\2\2\u0933\u0934\f\3\2\2\u0934\u0935\7\23\2\2\u0935")
        buf.write(u"\u0937\5\u0198\u00cd\2\u0936\u0933\3\2\2\2\u0937\u093a")
        buf.write(u"\3\2\2\2\u0938\u0936\3\2\2\2\u0938\u0939\3\2\2\2\u0939")
        buf.write(u"\u01a5\3\2\2\2\u093a\u0938\3\2\2\2\u093b\u093c\7\30\2")
        buf.write(u"\2\u093c\u093d\5\u0198\u00cd\2\u093d\u093e\7\31\2\2\u093e")
        buf.write(u"\u01a7\3\2\2\2\u093f\u0940\7\26\2\2\u0940\u0941\5\u0198")
        buf.write(u"\u00cd\2\u0941\u0942\7\27\2\2\u0942\u01a9\3\2\2\2\u0943")
        buf.write(u"\u0944\b\u00d6\1\2\u0944\u0947\7\u00aa\2\2\u0945\u0947")
        buf.write(u"\5\u01ae\u00d8\2\u0946\u0943\3\2\2\2\u0946\u0945\3\2")
        buf.write(u"\2\2\u0947\u094d\3\2\2\2\u0948\u0949\f\3\2\2\u0949\u094a")
        buf.write(u"\7\25\2\2\u094a\u094c\5\u01ae\u00d8\2\u094b\u0948\3\2")
        buf.write(u"\2\2\u094c\u094f\3\2\2\2\u094d\u094b\3\2\2\2\u094d\u094e")
        buf.write(u"\3\2\2\2\u094e\u01ab\3\2\2\2\u094f\u094d\3\2\2\2\u0950")
        buf.write(u"\u0956\7\u00ad\2\2\u0951\u0956\7\u00af\2\2\u0952\u0956")
        buf.write(u"\7\u00ab\2\2\u0953\u0956\7\u00a2\2\2\u0954\u0956\7\u00a3")
        buf.write(u"\2\2\u0955\u0950\3\2\2\2\u0955\u0951\3\2\2\2\u0955\u0952")
        buf.write(u"\3\2\2\2\u0955\u0953\3\2\2\2\u0955\u0954\3\2\2\2\u0956")
        buf.write(u"\u01ad\3\2\2\2\u0957\u0958\t\f\2\2\u0958\u01af\3\2\2")
        buf.write(u"\2\u0959\u095c\5\u01b2\u00da\2\u095a\u095c\5\u01b4\u00db")
        buf.write(u"\2\u095b\u0959\3\2\2\2\u095b\u095a\3\2\2\2\u095c\u01b1")
        buf.write(u"\3\2\2\2\u095d\u0965\5\u01ba\u00de\2\u095e\u0960\5\u01bc")
        buf.write(u"\u00df\2\u095f\u0961\5\u01c8\u00e5\2\u0960\u095f\3\2")
        buf.write(u"\2\2\u0960\u0961\3\2\2\2\u0961\u0962\3\2\2\2\u0962\u0963")
        buf.write(u"\5\u01be\u00e0\2\u0963\u0965\3\2\2\2\u0964\u095d\3\2")
        buf.write(u"\2\2\u0964\u095e\3\2\2\2\u0965\u01b3\3\2\2\2\u0966\u0968")
        buf.write(u"\5\u01b6\u00dc\2\u0967\u0969\5\u01c8\u00e5\2\u0968\u0967")
        buf.write(u"\3\2\2\2\u0968\u0969\3\2\2\2\u0969\u096a\3\2\2\2\u096a")
        buf.write(u"\u096b\5\u01b8\u00dd\2\u096b\u01b5\3\2\2\2\u096c\u096d")
        buf.write(u"\7*\2\2\u096d\u0970\7(\2\2\u096e\u0970\7,\2\2\u096f\u096c")
        buf.write(u"\3\2\2\2\u096f\u096e\3\2\2\2\u0970\u01b7\3\2\2\2\u0971")
        buf.write(u"\u0972\7*\2\2\u0972\u0973\7%\2\2\u0973\u0974\7(\2\2\u0974")
        buf.write(u"\u01b9\3\2\2\2\u0975\u0976\7*\2\2\u0976\u097a\5\u01c0")
        buf.write(u"\u00e1\2\u0977\u0979\5\u01c4\u00e3\2\u0978\u0977\3\2")
        buf.write(u"\2\2\u0979\u097c\3\2\2\2\u097a\u0978\3\2\2\2\u097a\u097b")
        buf.write(u"\3\2\2\2\u097b\u097d\3\2\2\2\u097c\u097a\3\2\2\2\u097d")
        buf.write(u"\u097e\7%\2\2\u097e\u097f\7(\2\2\u097f\u01bb\3\2\2\2")
        buf.write(u"\u0980\u0981\7*\2\2\u0981\u0985\5\u01c0\u00e1\2\u0982")
        buf.write(u"\u0984\5\u01c4\u00e3\2\u0983\u0982\3\2\2\2\u0984\u0987")
        buf.write(u"\3\2\2\2\u0985\u0983\3\2\2\2\u0985\u0986\3\2\2\2\u0986")
        buf.write(u"\u0988\3\2\2\2\u0987\u0985\3\2\2\2\u0988\u0989\7(\2\2")
        buf.write(u"\u0989\u01bd\3\2\2\2\u098a\u098b\7*\2\2\u098b\u098c\7")
        buf.write(u"%\2\2\u098c\u098d\5\u01c0\u00e1\2\u098d\u098e\7(\2\2")
        buf.write(u"\u098e\u01bf\3\2\2\2\u098f\u0994\5\u01c2\u00e2\2\u0990")
        buf.write(u"\u0991\7\25\2\2\u0991\u0993\5\u01c2\u00e2\2\u0992\u0990")
        buf.write(u"\3\2\2\2\u0993\u0996\3\2\2\2\u0994\u0992\3\2\2\2\u0994")
        buf.write(u"\u0995\3\2\2\2\u0995\u01c1\3\2\2\2\u0996\u0994\3\2\2")
        buf.write(u"\2\u0997\u099b\5\u00bc_\2\u0998\u099a\5\u00be`\2\u0999")
        buf.write(u"\u0998\3\2\2\2\u099a\u099d\3\2\2\2\u099b\u0999\3\2\2")
        buf.write(u"\2\u099b\u099c\3\2\2\2\u099c\u01c3\3\2\2\2\u099d\u099b")
        buf.write(u"\3\2\2\2\u099e\u09a1\5\u01c2\u00e2\2\u099f\u09a0\7-\2")
        buf.write(u"\2\u09a0\u09a2\5\u01c6\u00e4\2\u09a1\u099f\3\2\2\2\u09a1")
        buf.write(u"\u09a2\3\2\2\2\u09a2\u01c5\3\2\2\2\u09a3\u09a9\7\u00ab")
        buf.write(u"\2\2\u09a4\u09a5\7\32\2\2\u09a5\u09a6\5`\61\2\u09a6\u09a7")
        buf.write(u"\7\33\2\2\u09a7\u09a9\3\2\2\2\u09a8\u09a3\3\2\2\2\u09a8")
        buf.write(u"\u09a4\3\2\2\2\u09a9\u01c7\3\2\2\2\u09aa\u09ac\5\u01ca")
        buf.write(u"\u00e6\2\u09ab\u09aa\3\2\2\2\u09ac\u09ad\3\2\2\2\u09ad")
        buf.write(u"\u09ab\3\2\2\2\u09ad\u09ae\3\2\2\2\u09ae\u01c9\3\2\2")
        buf.write(u"\2\u09af\u09b7\5\u01cc\u00e7\2\u09b0\u09b7\5\u01b2\u00da")
        buf.write(u"\2\u09b1\u09b3\7\32\2\2\u09b2\u09b4\5`\61\2\u09b3\u09b2")
        buf.write(u"\3\2\2\2\u09b3\u09b4\3\2\2\2\u09b4\u09b5\3\2\2\2\u09b5")
        buf.write(u"\u09b7\7\33\2\2\u09b6\u09af\3\2\2\2\u09b6\u09b0\3\2\2")
        buf.write(u"\2\u09b6\u09b1\3\2\2\2\u09b7\u01cb\3\2\2\2\u09b8\u09ba")
        buf.write(u"\n\r\2\2\u09b9\u09b8\3\2\2\2\u09ba\u09bb\3\2\2\2\u09bb")
        buf.write(u"\u09b9\3\2\2\2\u09bb\u09bc\3\2\2\2\u09bc\u01cd\3\2\2")
        buf.write(u"\2\u09bd\u09bf\7\32\2\2\u09be\u09c0\5\u01d0\u00e9\2\u09bf")
        buf.write(u"\u09be\3\2\2\2\u09c0\u09c1\3\2\2\2\u09c1\u09bf\3\2\2")
        buf.write(u"\2\u09c1\u09c2\3\2\2\2\u09c2\u09c3\3\2\2\2\u09c3\u09c4")
        buf.write(u"\7\33\2\2\u09c4\u01cf\3\2\2\2\u09c5\u09c6\5\u01d2\u00ea")
        buf.write(u"\2\u09c6\u09c7\7\21\2\2\u09c7\u09c8\5\u01d4\u00eb\2\u09c8")
        buf.write(u"\u09c9\7\22\2\2\u09c9\u01d1\3\2\2\2\u09ca\u09cb\b\u00ea")
        buf.write(u"\1\2\u09cb\u09cf\5\u00bc_\2\u09cc\u09cd\7#\2\2\u09cd")
        buf.write(u"\u09cf\5\u00c0a\2\u09ce\u09ca\3\2\2\2\u09ce\u09cc\3\2")
        buf.write(u"\2\2\u09cf\u09d8\3\2\2\2\u09d0\u09d2\f\3\2\2\u09d1\u09d3")
        buf.write(u"\5\u00be`\2\u09d2\u09d1\3\2\2\2\u09d3\u09d4\3\2\2\2\u09d4")
        buf.write(u"\u09d2\3\2\2\2\u09d4\u09d5\3\2\2\2\u09d5\u09d7\3\2\2")
        buf.write(u"\2\u09d6\u09d0\3\2\2\2\u09d7\u09da\3\2\2\2\u09d8\u09d6")
        buf.write(u"\3\2\2\2\u09d8\u09d9\3\2\2\2\u09d9\u01d3\3\2\2\2\u09da")
        buf.write(u"\u09d8\3\2\2\2\u09db\u09dc\7\32\2\2\u09dc\u09dd\5`\61")
        buf.write(u"\2\u09dd\u09de\7\33\2\2\u09de\u09e1\3\2\2\2\u09df\u09e1")
        buf.write(u"\5\u01d6\u00ec\2\u09e0\u09db\3\2\2\2\u09e0\u09df\3\2")
        buf.write(u"\2\2\u09e1\u01d5\3\2\2\2\u09e2\u09e4\n\16\2\2\u09e3\u09e2")
        buf.write(u"\3\2\2\2\u09e4\u09e5\3\2\2\2\u09e5\u09e3\3\2\2\2\u09e5")
        buf.write(u"\u09e6\3\2\2\2\u09e6\u01d7\3\2\2\2\u00d8\u01de\u01e1")
        buf.write(u"\u01fa\u01ff\u020d\u0213\u0215\u0217\u021e\u0226\u022d")
        buf.write(u"\u023e\u0249\u0250\u025d\u026b\u027f\u0296\u02a1\u02a8")
        buf.write(u"\u02b1\u02b6\u02bd\u02c6\u02db\u02e3\u02e8\u02ee\u02f3")
        buf.write(u"\u02fc\u0301\u0306\u031e\u0329\u032d\u0342\u035c\u0361")
        buf.write(u"\u036a\u0373\u037c\u0399\u03ac\u03b2\u03d4\u03dd\u03f4")
        buf.write(u"\u0402\u040b\u0414\u042b\u0431\u0447\u04b6\u04b8\u04c4")
        buf.write(u"\u04cf\u04de\u04e3\u04ea\u04f3\u04fa\u04fe\u050a\u0511")
        buf.write(u"\u0518\u0528\u0533\u0537\u053c\u0541\u0543\u0547\u0550")
        buf.write(u"\u0560\u0569\u056f\u0574\u057b\u0583\u058e\u0596\u059f")
        buf.write(u"\u05a5\u05ad\u05b6\u05be\u05cb\u05ce\u05d2\u05d7\u05db")
        buf.write(u"\u05e4\u05f9\u0603\u0605\u060a\u061c\u0621\u062a\u062e")
        buf.write(u"\u0635\u063a\u063e\u064a\u0659\u065e\u0661\u0665\u066a")
        buf.write(u"\u0671\u067c\u067e\u0687\u068f\u0697\u069d\u06a9\u06ad")
        buf.write(u"\u06b7\u06bc\u06c2\u06c9\u06ce\u06d5\u06dd\u06e4\u06ee")
        buf.write(u"\u06fb\u06ff\u0702\u0706\u0709\u0711\u071a\u0723\u072c")
        buf.write(u"\u073d\u074e\u0755\u075c\u0766\u076d\u0770\u0774\u0779")
        buf.write(u"\u077d\u0788\u078b\u0792\u07a2\u07af\u07b6\u07c7\u07cf")
        buf.write(u"\u07d3\u07db\u07ff\u0808\u0812\u081e\u0823\u082f\u0841")
        buf.write(u"\u0848\u0851\u0859\u0863\u0868\u0872\u087c\u088c\u0896")
        buf.write(u"\u089d\u08a5\u08b0\u08b9\u08c1\u08cb\u08d0\u08dc\u08ef")
        buf.write(u"\u08f9\u0901\u090c\u0915\u091d\u0927\u092c\u0938\u0946")
        buf.write(u"\u094d\u0955\u095b\u0960\u0964\u0968\u096f\u097a\u0985")
        buf.write(u"\u0994\u099b\u09a1\u09a8\u09ad\u09b3\u09b6\u09bb\u09c1")
        buf.write(u"\u09ce\u09d4\u09d8\u09e0\u09e5")
        return buf.getvalue()


class MParser ( AbstractParser ):

    grammarFileName = "MParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"'\t'", u"' '", u"<INVALID>", 
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
                     u"'Cursor'", u"'Html'", u"'abstract'", u"'all'", u"'always'", 
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
                     u"'widget'", u"'with'", u"'when'", u"'where'", u"'while'", 
                     u"'write'", u"<INVALID>", u"<INVALID>", u"'MIN_INTEGER'", 
                     u"'MAX_INTEGER'" ]

    symbolicNames = [ u"<INVALID>", u"INDENT", u"DEDENT", u"LF_TAB", u"LF_MORE", 
                      u"LF", u"TAB", u"WS", u"COMMENT", u"JAVA", u"CSHARP", 
                      u"PYTHON2", u"PYTHON3", u"JAVASCRIPT", u"SWIFT", u"COLON", 
                      u"SEMI", u"COMMA", u"RANGE", u"DOT", u"LPAR", u"RPAR", 
                      u"LBRAK", u"RBRAK", u"LCURL", u"RCURL", u"QMARK", 
                      u"XMARK", u"AMP", u"AMP2", u"PIPE", u"PIPE2", u"PLUS", 
                      u"MINUS", u"STAR", u"SLASH", u"BSLASH", u"PERCENT", 
                      u"GT", u"GTE", u"LT", u"LTE", u"LTGT", u"EQ", u"XEQ", 
                      u"EQ2", u"TEQ", u"TILDE", u"LARROW", u"RARROW", u"BOOLEAN", 
                      u"CHARACTER", u"TEXT", u"INTEGER", u"DECIMAL", u"DATE", 
                      u"TIME", u"DATETIME", u"PERIOD", u"VERSION", u"METHOD_T", 
                      u"CODE", u"DOCUMENT", u"BLOB", u"IMAGE", u"UUID", 
                      u"ITERATOR", u"CURSOR", u"HTML", u"ABSTRACT", u"ALL", 
                      u"ALWAYS", u"AND", u"ANY", u"AS", u"ASC", u"ATTR", 
                      u"ATTRIBUTE", u"ATTRIBUTES", u"BINDINGS", u"BREAK", 
                      u"BY", u"CASE", u"CATCH", u"CATEGORY", u"CLASS", u"CLOSE", 
                      u"CONTAINS", u"DEF", u"DEFAULT", u"DEFINE", u"DELETE", 
                      u"DESC", u"DO", u"DOING", u"EACH", u"ELSE", u"ENUM", 
                      u"ENUMERATED", u"EXCEPT", u"EXECUTE", u"EXPECTING", 
                      u"EXTENDS", u"FETCH", u"FILTERED", u"FINALLY", u"FLUSH", 
                      u"FOR", u"FROM", u"GETTER", u"HAS", u"IF", u"IN", 
                      u"INDEX", u"INVOKE", u"IS", u"MATCHING", u"METHOD", 
                      u"METHODS", u"MODULO", u"MUTABLE", u"NATIVE", u"NONE", 
                      u"NOT", u"NOTHING", u"NULL", u"ON", u"ONE", u"OPEN", 
                      u"OPERATOR", u"OR", u"ORDER", u"OTHERWISE", u"PASS", 
                      u"RAISE", u"READ", u"RECEIVING", u"RESOURCE", u"RETURN", 
                      u"RETURNING", u"ROWS", u"SELF", u"SETTER", u"SINGLETON", 
                      u"SORTED", u"STORABLE", u"STORE", u"SWITCH", u"TEST", 
                      u"THIS", u"THROW", u"TO", u"TRY", u"VERIFYING", u"WIDGET", 
                      u"WITH", u"WHEN", u"WHERE", u"WHILE", u"WRITE", u"BOOLEAN_LITERAL", 
                      u"CHAR_LITERAL", u"MIN_INTEGER", u"MAX_INTEGER", u"SYMBOL_IDENTIFIER", 
                      u"TYPE_IDENTIFIER", u"VARIABLE_IDENTIFIER", u"NATIVE_IDENTIFIER", 
                      u"DOLLAR_IDENTIFIER", u"TEXT_LITERAL", u"UUID_LITERAL", 
                      u"INTEGER_LITERAL", u"HEXA_LITERAL", u"DECIMAL_LITERAL", 
                      u"DATETIME_LITERAL", u"TIME_LITERAL", u"DATE_LITERAL", 
                      u"PERIOD_LITERAL", u"VERSION_LITERAL" ]

    RULE_enum_category_declaration = 0
    RULE_enum_native_declaration = 1
    RULE_native_symbol = 2
    RULE_category_symbol = 3
    RULE_attribute_declaration = 4
    RULE_index_clause = 5
    RULE_concrete_widget_declaration = 6
    RULE_native_widget_declaration = 7
    RULE_concrete_category_declaration = 8
    RULE_singleton_category_declaration = 9
    RULE_derived_list = 10
    RULE_operator_method_declaration = 11
    RULE_setter_method_declaration = 12
    RULE_native_setter_declaration = 13
    RULE_getter_method_declaration = 14
    RULE_native_getter_declaration = 15
    RULE_native_category_declaration = 16
    RULE_native_resource_declaration = 17
    RULE_native_category_bindings = 18
    RULE_native_category_binding_list = 19
    RULE_abstract_method_declaration = 20
    RULE_concrete_method_declaration = 21
    RULE_native_method_declaration = 22
    RULE_test_method_declaration = 23
    RULE_assertion = 24
    RULE_typed_argument = 25
    RULE_statement = 26
    RULE_flush_statement = 27
    RULE_store_statement = 28
    RULE_method_call = 29
    RULE_method_selector = 30
    RULE_callable_parent = 31
    RULE_callable_selector = 32
    RULE_with_resource_statement = 33
    RULE_with_singleton_statement = 34
    RULE_switch_statement = 35
    RULE_switch_case_statement = 36
    RULE_for_each_statement = 37
    RULE_do_while_statement = 38
    RULE_while_statement = 39
    RULE_if_statement = 40
    RULE_else_if_statement_list = 41
    RULE_raise_statement = 42
    RULE_try_statement = 43
    RULE_catch_statement = 44
    RULE_break_statement = 45
    RULE_return_statement = 46
    RULE_expression = 47
    RULE_closure_expression = 48
    RULE_instance_expression = 49
    RULE_method_expression = 50
    RULE_instance_selector = 51
    RULE_blob_expression = 52
    RULE_document_expression = 53
    RULE_constructor_expression = 54
    RULE_copy_from = 55
    RULE_argument_assignment_list = 56
    RULE_argument_assignment = 57
    RULE_write_statement = 58
    RULE_filtered_list_suffix = 59
    RULE_fetch_store_expression = 60
    RULE_sorted_expression = 61
    RULE_assign_instance_statement = 62
    RULE_child_instance = 63
    RULE_assign_tuple_statement = 64
    RULE_lfs = 65
    RULE_lfp = 66
    RULE_indent = 67
    RULE_dedent = 68
    RULE_null_literal = 69
    RULE_declaration_list = 70
    RULE_declarations = 71
    RULE_declaration = 72
    RULE_resource_declaration = 73
    RULE_enum_declaration = 74
    RULE_native_symbol_list = 75
    RULE_category_symbol_list = 76
    RULE_symbol_list = 77
    RULE_attribute_constraint = 78
    RULE_list_literal = 79
    RULE_set_literal = 80
    RULE_expression_list = 81
    RULE_range_literal = 82
    RULE_typedef = 83
    RULE_primary_type = 84
    RULE_native_type = 85
    RULE_category_type = 86
    RULE_mutable_category_type = 87
    RULE_code_type = 88
    RULE_category_declaration = 89
    RULE_widget_declaration = 90
    RULE_type_identifier_list = 91
    RULE_method_identifier = 92
    RULE_identifier_or_keyword = 93
    RULE_nospace_hyphen_identifier_or_keyword = 94
    RULE_nospace_identifier_or_keyword = 95
    RULE_identifier = 96
    RULE_variable_identifier = 97
    RULE_attribute_identifier = 98
    RULE_type_identifier = 99
    RULE_symbol_identifier = 100
    RULE_argument_list = 101
    RULE_argument = 102
    RULE_operator_argument = 103
    RULE_named_argument = 104
    RULE_code_argument = 105
    RULE_category_or_any_type = 106
    RULE_any_type = 107
    RULE_member_method_declaration_list = 108
    RULE_member_method_declaration = 109
    RULE_native_member_method_declaration_list = 110
    RULE_native_member_method_declaration = 111
    RULE_native_category_binding = 112
    RULE_python_category_binding = 113
    RULE_python_module = 114
    RULE_javascript_category_binding = 115
    RULE_javascript_module = 116
    RULE_variable_identifier_list = 117
    RULE_attribute_identifier_list = 118
    RULE_method_declaration = 119
    RULE_comment_statement = 120
    RULE_native_statement_list = 121
    RULE_native_statement = 122
    RULE_python_native_statement = 123
    RULE_javascript_native_statement = 124
    RULE_statement_list = 125
    RULE_assertion_list = 126
    RULE_switch_case_statement_list = 127
    RULE_catch_statement_list = 128
    RULE_literal_collection = 129
    RULE_atomic_literal = 130
    RULE_literal_list_literal = 131
    RULE_selectable_expression = 132
    RULE_this_expression = 133
    RULE_parenthesis_expression = 134
    RULE_literal_expression = 135
    RULE_collection_literal = 136
    RULE_tuple_literal = 137
    RULE_dict_literal = 138
    RULE_expression_tuple = 139
    RULE_dict_entry_list = 140
    RULE_dict_entry = 141
    RULE_slice_arguments = 142
    RULE_assign_variable_statement = 143
    RULE_assignable_instance = 144
    RULE_is_expression = 145
    RULE_read_all_expression = 146
    RULE_read_one_expression = 147
    RULE_order_by_list = 148
    RULE_order_by = 149
    RULE_operator = 150
    RULE_keyword = 151
    RULE_new_token = 152
    RULE_key_token = 153
    RULE_module_token = 154
    RULE_value_token = 155
    RULE_symbols_token = 156
    RULE_assign = 157
    RULE_multiply = 158
    RULE_divide = 159
    RULE_idivide = 160
    RULE_modulo = 161
    RULE_javascript_statement = 162
    RULE_javascript_expression = 163
    RULE_javascript_primary_expression = 164
    RULE_javascript_this_expression = 165
    RULE_javascript_new_expression = 166
    RULE_javascript_selector_expression = 167
    RULE_javascript_method_expression = 168
    RULE_javascript_arguments = 169
    RULE_javascript_item_expression = 170
    RULE_javascript_parenthesis_expression = 171
    RULE_javascript_identifier_expression = 172
    RULE_javascript_literal_expression = 173
    RULE_javascript_identifier = 174
    RULE_python_statement = 175
    RULE_python_expression = 176
    RULE_python_primary_expression = 177
    RULE_python_self_expression = 178
    RULE_python_selector_expression = 179
    RULE_python_method_expression = 180
    RULE_python_argument_list = 181
    RULE_python_ordinal_argument_list = 182
    RULE_python_named_argument_list = 183
    RULE_python_parenthesis_expression = 184
    RULE_python_identifier_expression = 185
    RULE_python_literal_expression = 186
    RULE_python_identifier = 187
    RULE_java_statement = 188
    RULE_java_expression = 189
    RULE_java_primary_expression = 190
    RULE_java_this_expression = 191
    RULE_java_new_expression = 192
    RULE_java_selector_expression = 193
    RULE_java_method_expression = 194
    RULE_java_arguments = 195
    RULE_java_item_expression = 196
    RULE_java_parenthesis_expression = 197
    RULE_java_identifier_expression = 198
    RULE_java_class_identifier_expression = 199
    RULE_java_literal_expression = 200
    RULE_java_identifier = 201
    RULE_csharp_statement = 202
    RULE_csharp_expression = 203
    RULE_csharp_primary_expression = 204
    RULE_csharp_this_expression = 205
    RULE_csharp_new_expression = 206
    RULE_csharp_selector_expression = 207
    RULE_csharp_method_expression = 208
    RULE_csharp_arguments = 209
    RULE_csharp_item_expression = 210
    RULE_csharp_parenthesis_expression = 211
    RULE_csharp_identifier_expression = 212
    RULE_csharp_literal_expression = 213
    RULE_csharp_identifier = 214
    RULE_jsx_expression = 215
    RULE_jsx_element = 216
    RULE_jsx_fragment = 217
    RULE_jsx_fragment_start = 218
    RULE_jsx_fragment_end = 219
    RULE_jsx_self_closing = 220
    RULE_jsx_opening = 221
    RULE_jsx_closing = 222
    RULE_jsx_element_name = 223
    RULE_jsx_identifier = 224
    RULE_jsx_attribute = 225
    RULE_jsx_attribute_value = 226
    RULE_jsx_children = 227
    RULE_jsx_child = 228
    RULE_jsx_text = 229
    RULE_css_expression = 230
    RULE_css_field = 231
    RULE_css_identifier = 232
    RULE_css_value = 233
    RULE_css_text = 234

    ruleNames =  [ u"enum_category_declaration", u"enum_native_declaration", 
                   u"native_symbol", u"category_symbol", u"attribute_declaration", 
                   u"index_clause", u"concrete_widget_declaration", u"native_widget_declaration", 
                   u"concrete_category_declaration", u"singleton_category_declaration", 
                   u"derived_list", u"operator_method_declaration", u"setter_method_declaration", 
                   u"native_setter_declaration", u"getter_method_declaration", 
                   u"native_getter_declaration", u"native_category_declaration", 
                   u"native_resource_declaration", u"native_category_bindings", 
                   u"native_category_binding_list", u"abstract_method_declaration", 
                   u"concrete_method_declaration", u"native_method_declaration", 
                   u"test_method_declaration", u"assertion", u"typed_argument", 
                   u"statement", u"flush_statement", u"store_statement", 
                   u"method_call", u"method_selector", u"callable_parent", 
                   u"callable_selector", u"with_resource_statement", u"with_singleton_statement", 
                   u"switch_statement", u"switch_case_statement", u"for_each_statement", 
                   u"do_while_statement", u"while_statement", u"if_statement", 
                   u"else_if_statement_list", u"raise_statement", u"try_statement", 
                   u"catch_statement", u"break_statement", u"return_statement", 
                   u"expression", u"closure_expression", u"instance_expression", 
                   u"method_expression", u"instance_selector", u"blob_expression", 
                   u"document_expression", u"constructor_expression", u"copy_from", 
                   u"argument_assignment_list", u"argument_assignment", 
                   u"write_statement", u"filtered_list_suffix", u"fetch_store_expression", 
                   u"sorted_expression", u"assign_instance_statement", u"child_instance", 
                   u"assign_tuple_statement", u"lfs", u"lfp", u"indent", 
                   u"dedent", u"null_literal", u"declaration_list", u"declarations", 
                   u"declaration", u"resource_declaration", u"enum_declaration", 
                   u"native_symbol_list", u"category_symbol_list", u"symbol_list", 
                   u"attribute_constraint", u"list_literal", u"set_literal", 
                   u"expression_list", u"range_literal", u"typedef", u"primary_type", 
                   u"native_type", u"category_type", u"mutable_category_type", 
                   u"code_type", u"category_declaration", u"widget_declaration", 
                   u"type_identifier_list", u"method_identifier", u"identifier_or_keyword", 
                   u"nospace_hyphen_identifier_or_keyword", u"nospace_identifier_or_keyword", 
                   u"identifier", u"variable_identifier", u"attribute_identifier", 
                   u"type_identifier", u"symbol_identifier", u"argument_list", 
                   u"argument", u"operator_argument", u"named_argument", 
                   u"code_argument", u"category_or_any_type", u"any_type", 
                   u"member_method_declaration_list", u"member_method_declaration", 
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
                   u"idivide", u"modulo", u"javascript_statement", u"javascript_expression", 
                   u"javascript_primary_expression", u"javascript_this_expression", 
                   u"javascript_new_expression", u"javascript_selector_expression", 
                   u"javascript_method_expression", u"javascript_arguments", 
                   u"javascript_item_expression", u"javascript_parenthesis_expression", 
                   u"javascript_identifier_expression", u"javascript_literal_expression", 
                   u"javascript_identifier", u"python_statement", u"python_expression", 
                   u"python_primary_expression", u"python_self_expression", 
                   u"python_selector_expression", u"python_method_expression", 
                   u"python_argument_list", u"python_ordinal_argument_list", 
                   u"python_named_argument_list", u"python_parenthesis_expression", 
                   u"python_identifier_expression", u"python_literal_expression", 
                   u"python_identifier", u"java_statement", u"java_expression", 
                   u"java_primary_expression", u"java_this_expression", 
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
                   u"jsx_attribute", u"jsx_attribute_value", u"jsx_children", 
                   u"jsx_child", u"jsx_text", u"css_expression", u"css_field", 
                   u"css_identifier", u"css_value", u"css_text" ]

    EOF = Token.EOF
    INDENT=1
    DEDENT=2
    LF_TAB=3
    LF_MORE=4
    LF=5
    TAB=6
    WS=7
    COMMENT=8
    JAVA=9
    CSHARP=10
    PYTHON2=11
    PYTHON3=12
    JAVASCRIPT=13
    SWIFT=14
    COLON=15
    SEMI=16
    COMMA=17
    RANGE=18
    DOT=19
    LPAR=20
    RPAR=21
    LBRAK=22
    RBRAK=23
    LCURL=24
    RCURL=25
    QMARK=26
    XMARK=27
    AMP=28
    AMP2=29
    PIPE=30
    PIPE2=31
    PLUS=32
    MINUS=33
    STAR=34
    SLASH=35
    BSLASH=36
    PERCENT=37
    GT=38
    GTE=39
    LT=40
    LTE=41
    LTGT=42
    EQ=43
    XEQ=44
    EQ2=45
    TEQ=46
    TILDE=47
    LARROW=48
    RARROW=49
    BOOLEAN=50
    CHARACTER=51
    TEXT=52
    INTEGER=53
    DECIMAL=54
    DATE=55
    TIME=56
    DATETIME=57
    PERIOD=58
    VERSION=59
    METHOD_T=60
    CODE=61
    DOCUMENT=62
    BLOB=63
    IMAGE=64
    UUID=65
    ITERATOR=66
    CURSOR=67
    HTML=68
    ABSTRACT=69
    ALL=70
    ALWAYS=71
    AND=72
    ANY=73
    AS=74
    ASC=75
    ATTR=76
    ATTRIBUTE=77
    ATTRIBUTES=78
    BINDINGS=79
    BREAK=80
    BY=81
    CASE=82
    CATCH=83
    CATEGORY=84
    CLASS=85
    CLOSE=86
    CONTAINS=87
    DEF=88
    DEFAULT=89
    DEFINE=90
    DELETE=91
    DESC=92
    DO=93
    DOING=94
    EACH=95
    ELSE=96
    ENUM=97
    ENUMERATED=98
    EXCEPT=99
    EXECUTE=100
    EXPECTING=101
    EXTENDS=102
    FETCH=103
    FILTERED=104
    FINALLY=105
    FLUSH=106
    FOR=107
    FROM=108
    GETTER=109
    HAS=110
    IF=111
    IN=112
    INDEX=113
    INVOKE=114
    IS=115
    MATCHING=116
    METHOD=117
    METHODS=118
    MODULO=119
    MUTABLE=120
    NATIVE=121
    NONE=122
    NOT=123
    NOTHING=124
    NULL=125
    ON=126
    ONE=127
    OPEN=128
    OPERATOR=129
    OR=130
    ORDER=131
    OTHERWISE=132
    PASS=133
    RAISE=134
    READ=135
    RECEIVING=136
    RESOURCE=137
    RETURN=138
    RETURNING=139
    ROWS=140
    SELF=141
    SETTER=142
    SINGLETON=143
    SORTED=144
    STORABLE=145
    STORE=146
    SWITCH=147
    TEST=148
    THIS=149
    THROW=150
    TO=151
    TRY=152
    VERIFYING=153
    WIDGET=154
    WITH=155
    WHEN=156
    WHERE=157
    WHILE=158
    WRITE=159
    BOOLEAN_LITERAL=160
    CHAR_LITERAL=161
    MIN_INTEGER=162
    MAX_INTEGER=163
    SYMBOL_IDENTIFIER=164
    TYPE_IDENTIFIER=165
    VARIABLE_IDENTIFIER=166
    NATIVE_IDENTIFIER=167
    DOLLAR_IDENTIFIER=168
    TEXT_LITERAL=169
    UUID_LITERAL=170
    INTEGER_LITERAL=171
    HEXA_LITERAL=172
    DECIMAL_LITERAL=173
    DATETIME_LITERAL=174
    TIME_LITERAL=175
    DATE_LITERAL=176
    PERIOD_LITERAL=177
    VERSION_LITERAL=178

    def __init__(self, input, output=sys.stdout):
        super(MParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Enum_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Enum_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.derived = None # Type_identifierContext
            self.attrs = None # Attribute_identifier_listContext
            self.symbols = None # Category_symbol_listContext

        def ENUM(self):
            return self.getToken(MParser.ENUM, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def type_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Type_identifierContext)
            else:
                return self.getTypedRuleContext(MParser.Type_identifierContext,i)


        def category_symbol_list(self):
            return self.getTypedRuleContext(MParser.Category_symbol_listContext,0)


        def attribute_identifier_list(self):
            return self.getTypedRuleContext(MParser.Attribute_identifier_listContext,0)


        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)

        def getRuleIndex(self):
            return MParser.RULE_enum_category_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterEnum_category_declaration"):
                listener.enterEnum_category_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEnum_category_declaration"):
                listener.exitEnum_category_declaration(self)




    def enum_category_declaration(self):

        localctx = MParser.Enum_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_enum_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.match(MParser.ENUM)
            self.state = 471
            localctx.name = self.type_identifier()
            self.state = 472
            self.match(MParser.LPAR)
            self.state = 479
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.TYPE_IDENTIFIER]:
                self.state = 473
                localctx.derived = self.type_identifier()
                self.state = 476
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MParser.COMMA:
                    self.state = 474
                    self.match(MParser.COMMA)
                    self.state = 475
                    localctx.attrs = self.attribute_identifier_list()


                pass
            elif token in [MParser.STORABLE, MParser.VARIABLE_IDENTIFIER]:
                self.state = 478
                localctx.attrs = self.attribute_identifier_list()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 481
            self.match(MParser.RPAR)
            self.state = 482
            self.match(MParser.COLON)
            self.state = 483
            self.indent()
            self.state = 484
            localctx.symbols = self.category_symbol_list()
            self.state = 485
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Enum_native_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Enum_native_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.typ = None # Native_typeContext
            self.symbols = None # Native_symbol_listContext

        def ENUM(self):
            return self.getToken(MParser.ENUM, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(MParser.Type_identifierContext,0)


        def native_type(self):
            return self.getTypedRuleContext(MParser.Native_typeContext,0)


        def native_symbol_list(self):
            return self.getTypedRuleContext(MParser.Native_symbol_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_enum_native_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterEnum_native_declaration"):
                listener.enterEnum_native_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEnum_native_declaration"):
                listener.exitEnum_native_declaration(self)




    def enum_native_declaration(self):

        localctx = MParser.Enum_native_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_enum_native_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.match(MParser.ENUM)
            self.state = 488
            localctx.name = self.type_identifier()
            self.state = 489
            self.match(MParser.LPAR)
            self.state = 490
            localctx.typ = self.native_type()
            self.state = 491
            self.match(MParser.RPAR)
            self.state = 492
            self.match(MParser.COLON)
            self.state = 493
            self.indent()
            self.state = 494
            localctx.symbols = self.native_symbol_list()
            self.state = 495
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_symbolContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Native_symbolContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Symbol_identifierContext
            self.exp = None # ExpressionContext

        def EQ(self):
            return self.getToken(MParser.EQ, 0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(MParser.Symbol_identifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_native_symbol

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_symbol"):
                listener.enterNative_symbol(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_symbol"):
                listener.exitNative_symbol(self)




    def native_symbol(self):

        localctx = MParser.Native_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_native_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            localctx.name = self.symbol_identifier()
            self.state = 498
            self.match(MParser.EQ)
            self.state = 499
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_symbolContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Category_symbolContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Symbol_identifierContext
            self.args = None # Argument_assignment_listContext

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(MParser.Symbol_identifierContext,0)


        def argument_assignment_list(self):
            return self.getTypedRuleContext(MParser.Argument_assignment_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_category_symbol

        def enterRule(self, listener):
            if hasattr(listener, "enterCategory_symbol"):
                listener.enterCategory_symbol(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategory_symbol"):
                listener.exitCategory_symbol(self)




    def category_symbol(self):

        localctx = MParser.Category_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_category_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            localctx.name = self.symbol_identifier()
            self.state = 502
            self.match(MParser.LPAR)
            self.state = 504
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.LTGT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 100)) & ~0x3f) == 0 and ((1 << (_la - 100)) & ((1 << (MParser.EXECUTE - 100)) | (1 << (MParser.FETCH - 100)) | (1 << (MParser.MUTABLE - 100)) | (1 << (MParser.NONE - 100)) | (1 << (MParser.NOT - 100)) | (1 << (MParser.READ - 100)) | (1 << (MParser.SELF - 100)) | (1 << (MParser.SORTED - 100)) | (1 << (MParser.THIS - 100)) | (1 << (MParser.BOOLEAN_LITERAL - 100)) | (1 << (MParser.CHAR_LITERAL - 100)) | (1 << (MParser.MIN_INTEGER - 100)) | (1 << (MParser.MAX_INTEGER - 100)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (MParser.SYMBOL_IDENTIFIER - 164)) | (1 << (MParser.TYPE_IDENTIFIER - 164)) | (1 << (MParser.VARIABLE_IDENTIFIER - 164)) | (1 << (MParser.TEXT_LITERAL - 164)) | (1 << (MParser.UUID_LITERAL - 164)) | (1 << (MParser.INTEGER_LITERAL - 164)) | (1 << (MParser.HEXA_LITERAL - 164)) | (1 << (MParser.DECIMAL_LITERAL - 164)) | (1 << (MParser.DATETIME_LITERAL - 164)) | (1 << (MParser.TIME_LITERAL - 164)) | (1 << (MParser.DATE_LITERAL - 164)) | (1 << (MParser.PERIOD_LITERAL - 164)) | (1 << (MParser.VERSION_LITERAL - 164)))) != 0):
                self.state = 503
                localctx.args = self.argument_assignment_list(0)


            self.state = 506
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Attribute_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Attribute_identifierContext
            self.typ = None # TypedefContext
            self.match = None # Attribute_constraintContext
            self.indices = None # Index_clauseContext

        def ATTR(self):
            return self.getToken(MParser.ATTR, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def attribute_identifier(self):
            return self.getTypedRuleContext(MParser.Attribute_identifierContext,0)


        def typedef(self):
            return self.getTypedRuleContext(MParser.TypedefContext,0)


        def PASS(self):
            return self.getToken(MParser.PASS, 0)

        def STORABLE(self):
            return self.getToken(MParser.STORABLE, 0)

        def attribute_constraint(self):
            return self.getTypedRuleContext(MParser.Attribute_constraintContext,0)


        def index_clause(self):
            return self.getTypedRuleContext(MParser.Index_clauseContext,0)


        def lfp(self):
            return self.getTypedRuleContext(MParser.LfpContext,0)


        def getRuleIndex(self):
            return MParser.RULE_attribute_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterAttribute_declaration"):
                listener.enterAttribute_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAttribute_declaration"):
                listener.exitAttribute_declaration(self)




    def attribute_declaration(self):

        localctx = MParser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.STORABLE:
                self.state = 508
                self.match(MParser.STORABLE)


            self.state = 511
            self.match(MParser.ATTR)
            self.state = 512
            localctx.name = self.attribute_identifier()
            self.state = 513
            self.match(MParser.LPAR)
            self.state = 514
            localctx.typ = self.typedef(0)
            self.state = 515
            self.match(MParser.RPAR)
            self.state = 516
            self.match(MParser.COLON)
            self.state = 517
            self.indent()
            self.state = 533
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.PASS]:
                self.state = 518
                self.match(MParser.PASS)
                pass
            elif token in [MParser.IN, MParser.INDEX, MParser.MATCHING]:
                self.state = 531
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MParser.IN, MParser.MATCHING]:
                    self.state = 519
                    localctx.match = self.attribute_constraint()
                    self.state = 523
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        self.state = 520
                        self.lfp()
                        self.state = 521
                        localctx.indices = self.index_clause()


                    pass
                elif token in [MParser.INDEX]:
                    self.state = 525
                    localctx.indices = self.index_clause()
                    self.state = 529
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        self.state = 526
                        self.lfp()
                        self.state = 527
                        localctx.match = self.attribute_constraint()


                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 535
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Index_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Index_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.indices = None # Variable_identifier_listContext

        def INDEX(self):
            return self.getToken(MParser.INDEX, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def variable_identifier_list(self):
            return self.getTypedRuleContext(MParser.Variable_identifier_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_index_clause

        def enterRule(self, listener):
            if hasattr(listener, "enterIndex_clause"):
                listener.enterIndex_clause(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIndex_clause"):
                listener.exitIndex_clause(self)




    def index_clause(self):

        localctx = MParser.Index_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_index_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            self.match(MParser.INDEX)
            self.state = 538
            self.match(MParser.LPAR)
            self.state = 540
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.VARIABLE_IDENTIFIER:
                self.state = 539
                localctx.indices = self.variable_identifier_list()


            self.state = 542
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Concrete_widget_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Concrete_widget_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.derived = None # Type_identifierContext
            self.methods = None # Member_method_declaration_listContext

        def WIDGET(self):
            return self.getToken(MParser.WIDGET, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def type_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Type_identifierContext)
            else:
                return self.getTypedRuleContext(MParser.Type_identifierContext,i)


        def PASS(self):
            return self.getToken(MParser.PASS, 0)

        def member_method_declaration_list(self):
            return self.getTypedRuleContext(MParser.Member_method_declaration_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_concrete_widget_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterConcrete_widget_declaration"):
                listener.enterConcrete_widget_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConcrete_widget_declaration"):
                listener.exitConcrete_widget_declaration(self)




    def concrete_widget_declaration(self):

        localctx = MParser.Concrete_widget_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_concrete_widget_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self.match(MParser.WIDGET)
            self.state = 545
            localctx.name = self.type_identifier()
            self.state = 546
            self.match(MParser.LPAR)
            self.state = 548
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.TYPE_IDENTIFIER:
                self.state = 547
                localctx.derived = self.type_identifier()


            self.state = 550
            self.match(MParser.RPAR)
            self.state = 551
            self.match(MParser.COLON)
            self.state = 552
            self.indent()
            self.state = 555
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.ABSTRACT, MParser.DEF]:
                self.state = 553
                localctx.methods = self.member_method_declaration_list()
                pass
            elif token in [MParser.PASS]:
                self.state = 554
                self.match(MParser.PASS)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 557
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_widget_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Native_widget_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.bindings = None # Native_category_bindingsContext
            self.methods = None # Native_member_method_declaration_listContext

        def NATIVE(self):
            return self.getToken(MParser.NATIVE, 0)

        def WIDGET(self):
            return self.getToken(MParser.WIDGET, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def lfp(self):
            return self.getTypedRuleContext(MParser.LfpContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(MParser.Type_identifierContext,0)


        def native_category_bindings(self):
            return self.getTypedRuleContext(MParser.Native_category_bindingsContext,0)


        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(MParser.Native_member_method_declaration_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_native_widget_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_widget_declaration"):
                listener.enterNative_widget_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_widget_declaration"):
                listener.exitNative_widget_declaration(self)




    def native_widget_declaration(self):

        localctx = MParser.Native_widget_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_native_widget_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self.match(MParser.NATIVE)
            self.state = 560
            self.match(MParser.WIDGET)
            self.state = 561
            localctx.name = self.type_identifier()
            self.state = 562
            self.match(MParser.LPAR)
            self.state = 563
            self.match(MParser.RPAR)
            self.state = 564
            self.match(MParser.COLON)
            self.state = 565
            self.indent()
            self.state = 566
            localctx.bindings = self.native_category_bindings()
            self.state = 567
            self.lfp()
            self.state = 568
            localctx.methods = self.native_member_method_declaration_list()
            self.state = 569
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Concrete_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Concrete_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.derived = None # Derived_listContext
            self.attrs = None # Attribute_identifier_listContext
            self.methods = None # Member_method_declaration_listContext

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def CLASS(self):
            return self.getToken(MParser.CLASS, 0)

        def CATEGORY(self):
            return self.getToken(MParser.CATEGORY, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(MParser.Type_identifierContext,0)


        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)

        def PASS(self):
            return self.getToken(MParser.PASS, 0)

        def STORABLE(self):
            return self.getToken(MParser.STORABLE, 0)

        def derived_list(self):
            return self.getTypedRuleContext(MParser.Derived_listContext,0)


        def attribute_identifier_list(self):
            return self.getTypedRuleContext(MParser.Attribute_identifier_listContext,0)


        def member_method_declaration_list(self):
            return self.getTypedRuleContext(MParser.Member_method_declaration_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_concrete_category_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterConcrete_category_declaration"):
                listener.enterConcrete_category_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConcrete_category_declaration"):
                listener.exitConcrete_category_declaration(self)




    def concrete_category_declaration(self):

        localctx = MParser.Concrete_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_concrete_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.STORABLE:
                self.state = 571
                self.match(MParser.STORABLE)


            self.state = 574
            _la = self._input.LA(1)
            if not(_la==MParser.CATEGORY or _la==MParser.CLASS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 575
            localctx.name = self.type_identifier()
            self.state = 576
            self.match(MParser.LPAR)
            self.state = 583
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 577
                localctx.derived = self.derived_list()
                pass

            elif la_ == 2:
                self.state = 578
                localctx.attrs = self.attribute_identifier_list()
                pass

            elif la_ == 3:
                self.state = 579
                localctx.derived = self.derived_list()
                self.state = 580
                self.match(MParser.COMMA)
                self.state = 581
                localctx.attrs = self.attribute_identifier_list()
                pass


            self.state = 585
            self.match(MParser.RPAR)
            self.state = 586
            self.match(MParser.COLON)
            self.state = 587
            self.indent()
            self.state = 590
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.ABSTRACT, MParser.DEF]:
                self.state = 588
                localctx.methods = self.member_method_declaration_list()
                pass
            elif token in [MParser.PASS]:
                self.state = 589
                self.match(MParser.PASS)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 592
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Singleton_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Singleton_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_identifier_listContext
            self.methods = None # Member_method_declaration_listContext

        def SINGLETON(self):
            return self.getToken(MParser.SINGLETON, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(MParser.Type_identifierContext,0)


        def attribute_identifier_list(self):
            return self.getTypedRuleContext(MParser.Attribute_identifier_listContext,0)


        def PASS(self):
            return self.getToken(MParser.PASS, 0)

        def member_method_declaration_list(self):
            return self.getTypedRuleContext(MParser.Member_method_declaration_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_singleton_category_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterSingleton_category_declaration"):
                listener.enterSingleton_category_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSingleton_category_declaration"):
                listener.exitSingleton_category_declaration(self)




    def singleton_category_declaration(self):

        localctx = MParser.Singleton_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_singleton_category_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self.match(MParser.SINGLETON)
            self.state = 595
            localctx.name = self.type_identifier()
            self.state = 596
            self.match(MParser.LPAR)
            self.state = 597
            localctx.attrs = self.attribute_identifier_list()
            self.state = 598
            self.match(MParser.RPAR)
            self.state = 599
            self.match(MParser.COLON)
            self.state = 600
            self.indent()
            self.state = 603
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.ABSTRACT, MParser.DEF]:
                self.state = 601
                localctx.methods = self.member_method_declaration_list()
                pass
            elif token in [MParser.PASS]:
                self.state = 602
                self.match(MParser.PASS)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 605
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Derived_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Derived_listContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Type_identifier_listContext

        def type_identifier_list(self):
            return self.getTypedRuleContext(MParser.Type_identifier_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_derived_list

        def enterRule(self, listener):
            if hasattr(listener, "enterDerived_list"):
                listener.enterDerived_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDerived_list"):
                listener.exitDerived_list(self)




    def derived_list(self):

        localctx = MParser.Derived_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_derived_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            localctx.items = self.type_identifier_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Operator_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Operator_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.op = None # OperatorContext
            self.arg = None # Operator_argumentContext
            self.typ = None # TypedefContext
            self.stmts = None # Statement_listContext

        def DEF(self):
            return self.getToken(MParser.DEF, 0)

        def OPERATOR(self):
            return self.getToken(MParser.OPERATOR, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def operator(self):
            return self.getTypedRuleContext(MParser.OperatorContext,0)


        def operator_argument(self):
            return self.getTypedRuleContext(MParser.Operator_argumentContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def RARROW(self):
            return self.getToken(MParser.RARROW, 0)

        def typedef(self):
            return self.getTypedRuleContext(MParser.TypedefContext,0)


        def getRuleIndex(self):
            return MParser.RULE_operator_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterOperator_method_declaration"):
                listener.enterOperator_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperator_method_declaration"):
                listener.exitOperator_method_declaration(self)




    def operator_method_declaration(self):

        localctx = MParser.Operator_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_operator_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 609
            self.match(MParser.DEF)
            self.state = 610
            self.match(MParser.OPERATOR)
            self.state = 611
            localctx.op = self.operator()
            self.state = 612
            self.match(MParser.LPAR)
            self.state = 613
            localctx.arg = self.operator_argument()
            self.state = 614
            self.match(MParser.RPAR)
            self.state = 617
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.RARROW:
                self.state = 615
                self.match(MParser.RARROW)
                self.state = 616
                localctx.typ = self.typedef(0)


            self.state = 619
            self.match(MParser.COLON)
            self.state = 620
            self.indent()
            self.state = 621
            localctx.stmts = self.statement_list()
            self.state = 622
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Setter_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Setter_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext

        def DEF(self):
            return self.getToken(MParser.DEF, 0)

        def SETTER(self):
            return self.getToken(MParser.SETTER, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_setter_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterSetter_method_declaration"):
                listener.enterSetter_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSetter_method_declaration"):
                listener.exitSetter_method_declaration(self)




    def setter_method_declaration(self):

        localctx = MParser.Setter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_setter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 624
            self.match(MParser.DEF)
            self.state = 625
            localctx.name = self.variable_identifier()
            self.state = 626
            self.match(MParser.SETTER)
            self.state = 627
            self.match(MParser.LPAR)
            self.state = 628
            self.match(MParser.RPAR)
            self.state = 629
            self.match(MParser.COLON)
            self.state = 630
            self.indent()
            self.state = 631
            localctx.stmts = self.statement_list()
            self.state = 632
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_setter_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Native_setter_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Native_statement_listContext

        def DEF(self):
            return self.getToken(MParser.DEF, 0)

        def SETTER(self):
            return self.getToken(MParser.SETTER, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def native_statement_list(self):
            return self.getTypedRuleContext(MParser.Native_statement_listContext,0)


        def NATIVE(self):
            return self.getToken(MParser.NATIVE, 0)

        def getRuleIndex(self):
            return MParser.RULE_native_setter_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_setter_declaration"):
                listener.enterNative_setter_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_setter_declaration"):
                listener.exitNative_setter_declaration(self)




    def native_setter_declaration(self):

        localctx = MParser.Native_setter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_native_setter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 634
            self.match(MParser.DEF)
            self.state = 635
            localctx.name = self.variable_identifier()
            self.state = 637
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.NATIVE:
                self.state = 636
                self.match(MParser.NATIVE)


            self.state = 639
            self.match(MParser.SETTER)
            self.state = 640
            self.match(MParser.LPAR)
            self.state = 641
            self.match(MParser.RPAR)
            self.state = 642
            self.match(MParser.COLON)
            self.state = 643
            self.indent()
            self.state = 644
            localctx.stmts = self.native_statement_list()
            self.state = 645
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Getter_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Getter_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext

        def DEF(self):
            return self.getToken(MParser.DEF, 0)

        def GETTER(self):
            return self.getToken(MParser.GETTER, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_getter_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterGetter_method_declaration"):
                listener.enterGetter_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitGetter_method_declaration"):
                listener.exitGetter_method_declaration(self)




    def getter_method_declaration(self):

        localctx = MParser.Getter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_getter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 647
            self.match(MParser.DEF)
            self.state = 648
            localctx.name = self.variable_identifier()
            self.state = 649
            self.match(MParser.GETTER)
            self.state = 650
            self.match(MParser.LPAR)
            self.state = 651
            self.match(MParser.RPAR)
            self.state = 652
            self.match(MParser.COLON)
            self.state = 653
            self.indent()
            self.state = 654
            localctx.stmts = self.statement_list()
            self.state = 655
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_getter_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Native_getter_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Native_statement_listContext

        def DEF(self):
            return self.getToken(MParser.DEF, 0)

        def GETTER(self):
            return self.getToken(MParser.GETTER, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def native_statement_list(self):
            return self.getTypedRuleContext(MParser.Native_statement_listContext,0)


        def NATIVE(self):
            return self.getToken(MParser.NATIVE, 0)

        def getRuleIndex(self):
            return MParser.RULE_native_getter_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_getter_declaration"):
                listener.enterNative_getter_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_getter_declaration"):
                listener.exitNative_getter_declaration(self)




    def native_getter_declaration(self):

        localctx = MParser.Native_getter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_native_getter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 657
            self.match(MParser.DEF)
            self.state = 658
            localctx.name = self.variable_identifier()
            self.state = 660
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.NATIVE:
                self.state = 659
                self.match(MParser.NATIVE)


            self.state = 662
            self.match(MParser.GETTER)
            self.state = 663
            self.match(MParser.LPAR)
            self.state = 664
            self.match(MParser.RPAR)
            self.state = 665
            self.match(MParser.COLON)
            self.state = 666
            self.indent()
            self.state = 667
            localctx.stmts = self.native_statement_list()
            self.state = 668
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Native_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_identifier_listContext
            self.bindings = None # Native_category_bindingsContext
            self.methods = None # Native_member_method_declaration_listContext

        def NATIVE(self):
            return self.getToken(MParser.NATIVE, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def CLASS(self):
            return self.getToken(MParser.CLASS, 0)

        def CATEGORY(self):
            return self.getToken(MParser.CATEGORY, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(MParser.Type_identifierContext,0)


        def native_category_bindings(self):
            return self.getTypedRuleContext(MParser.Native_category_bindingsContext,0)


        def STORABLE(self):
            return self.getToken(MParser.STORABLE, 0)

        def lfp(self):
            return self.getTypedRuleContext(MParser.LfpContext,0)


        def attribute_identifier_list(self):
            return self.getTypedRuleContext(MParser.Attribute_identifier_listContext,0)


        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(MParser.Native_member_method_declaration_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_native_category_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_category_declaration"):
                listener.enterNative_category_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_category_declaration"):
                listener.exitNative_category_declaration(self)




    def native_category_declaration(self):

        localctx = MParser.Native_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_native_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 671
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.STORABLE:
                self.state = 670
                self.match(MParser.STORABLE)


            self.state = 673
            self.match(MParser.NATIVE)
            self.state = 674
            _la = self._input.LA(1)
            if not(_la==MParser.CATEGORY or _la==MParser.CLASS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 675
            localctx.name = self.type_identifier()
            self.state = 676
            self.match(MParser.LPAR)
            self.state = 678
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.STORABLE or _la==MParser.VARIABLE_IDENTIFIER:
                self.state = 677
                localctx.attrs = self.attribute_identifier_list()


            self.state = 680
            self.match(MParser.RPAR)
            self.state = 681
            self.match(MParser.COLON)
            self.state = 682
            self.indent()
            self.state = 683
            localctx.bindings = self.native_category_bindings()
            self.state = 687
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 684
                self.lfp()
                self.state = 685
                localctx.methods = self.native_member_method_declaration_list()


            self.state = 689
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_resource_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Native_resource_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_identifier_listContext
            self.bindings = None # Native_category_bindingsContext
            self.methods = None # Native_member_method_declaration_listContext

        def NATIVE(self):
            return self.getToken(MParser.NATIVE, 0)

        def RESOURCE(self):
            return self.getToken(MParser.RESOURCE, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(MParser.Type_identifierContext,0)


        def native_category_bindings(self):
            return self.getTypedRuleContext(MParser.Native_category_bindingsContext,0)


        def STORABLE(self):
            return self.getToken(MParser.STORABLE, 0)

        def lfp(self):
            return self.getTypedRuleContext(MParser.LfpContext,0)


        def attribute_identifier_list(self):
            return self.getTypedRuleContext(MParser.Attribute_identifier_listContext,0)


        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(MParser.Native_member_method_declaration_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_native_resource_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_resource_declaration"):
                listener.enterNative_resource_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_resource_declaration"):
                listener.exitNative_resource_declaration(self)




    def native_resource_declaration(self):

        localctx = MParser.Native_resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_native_resource_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 692
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.STORABLE:
                self.state = 691
                self.match(MParser.STORABLE)


            self.state = 694
            self.match(MParser.NATIVE)
            self.state = 695
            self.match(MParser.RESOURCE)
            self.state = 696
            localctx.name = self.type_identifier()
            self.state = 697
            self.match(MParser.LPAR)
            self.state = 699
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.STORABLE or _la==MParser.VARIABLE_IDENTIFIER:
                self.state = 698
                localctx.attrs = self.attribute_identifier_list()


            self.state = 701
            self.match(MParser.RPAR)
            self.state = 702
            self.match(MParser.COLON)
            self.state = 703
            self.indent()
            self.state = 704
            localctx.bindings = self.native_category_bindings()
            self.state = 708
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 705
                self.lfp()
                self.state = 706
                localctx.methods = self.native_member_method_declaration_list()


            self.state = 710
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_category_bindingsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Native_category_bindingsContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Native_category_binding_listContext

        def DEF(self):
            return self.getToken(MParser.DEF, 0)

        def BINDINGS(self):
            return self.getToken(MParser.BINDINGS, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def CLASS(self):
            return self.getToken(MParser.CLASS, 0)

        def CATEGORY(self):
            return self.getToken(MParser.CATEGORY, 0)

        def native_category_binding_list(self):
            return self.getTypedRuleContext(MParser.Native_category_binding_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_native_category_bindings

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_category_bindings"):
                listener.enterNative_category_bindings(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_category_bindings"):
                listener.exitNative_category_bindings(self)




    def native_category_bindings(self):

        localctx = MParser.Native_category_bindingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_native_category_bindings)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 712
            self.match(MParser.DEF)
            self.state = 713
            _la = self._input.LA(1)
            if not(_la==MParser.CATEGORY or _la==MParser.CLASS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 714
            self.match(MParser.BINDINGS)
            self.state = 715
            self.match(MParser.COLON)
            self.state = 716
            self.indent()
            self.state = 717
            localctx.items = self.native_category_binding_list(0)
            self.state = 718
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_category_binding_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Native_category_binding_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_native_category_binding_list

     
        def copyFrom(self, ctx):
            super(MParser.Native_category_binding_listContext, self).copyFrom(ctx)


    class NativeCategoryBindingListItemContext(Native_category_binding_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_category_binding_listContext)
            super(MParser.NativeCategoryBindingListItemContext, self).__init__(parser)
            self.items = None # Native_category_binding_listContext
            self.item = None # Native_category_bindingContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(MParser.LfpContext,0)

        def native_category_binding_list(self):
            return self.getTypedRuleContext(MParser.Native_category_binding_listContext,0)

        def native_category_binding(self):
            return self.getTypedRuleContext(MParser.Native_category_bindingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNativeCategoryBindingListItem"):
                listener.enterNativeCategoryBindingListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNativeCategoryBindingListItem"):
                listener.exitNativeCategoryBindingListItem(self)


    class NativeCategoryBindingListContext(Native_category_binding_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_category_binding_listContext)
            super(MParser.NativeCategoryBindingListContext, self).__init__(parser)
            self.item = None # Native_category_bindingContext
            self.copyFrom(ctx)

        def native_category_binding(self):
            return self.getTypedRuleContext(MParser.Native_category_bindingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNativeCategoryBindingList"):
                listener.enterNativeCategoryBindingList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNativeCategoryBindingList"):
                listener.exitNativeCategoryBindingList(self)



    def native_category_binding_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Native_category_binding_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_native_category_binding_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.NativeCategoryBindingListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 721
            localctx.item = self.native_category_binding()
            self._ctx.stop = self._input.LT(-1)
            self.state = 729
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.NativeCategoryBindingListItemContext(self, MParser.Native_category_binding_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_category_binding_list)
                    self.state = 723
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 724
                    self.lfp()
                    self.state = 725
                    localctx.item = self.native_category_binding() 
                self.state = 731
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Abstract_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Abstract_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Argument_listContext
            self.typ = None # TypedefContext

        def ABSTRACT(self):
            return self.getToken(MParser.ABSTRACT, 0)

        def DEF(self):
            return self.getToken(MParser.DEF, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def method_identifier(self):
            return self.getTypedRuleContext(MParser.Method_identifierContext,0)


        def RARROW(self):
            return self.getToken(MParser.RARROW, 0)

        def argument_list(self):
            return self.getTypedRuleContext(MParser.Argument_listContext,0)


        def typedef(self):
            return self.getTypedRuleContext(MParser.TypedefContext,0)


        def getRuleIndex(self):
            return MParser.RULE_abstract_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterAbstract_method_declaration"):
                listener.enterAbstract_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAbstract_method_declaration"):
                listener.exitAbstract_method_declaration(self)




    def abstract_method_declaration(self):

        localctx = MParser.Abstract_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_abstract_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 732
            self.match(MParser.ABSTRACT)
            self.state = 733
            self.match(MParser.DEF)
            self.state = 734
            localctx.name = self.method_identifier()
            self.state = 735
            self.match(MParser.LPAR)
            self.state = 737
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.CODE or _la==MParser.MUTABLE or _la==MParser.VARIABLE_IDENTIFIER:
                self.state = 736
                localctx.args = self.argument_list()


            self.state = 739
            self.match(MParser.RPAR)
            self.state = 742
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.RARROW:
                self.state = 740
                self.match(MParser.RARROW)
                self.state = 741
                localctx.typ = self.typedef(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Concrete_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Concrete_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Argument_listContext
            self.typ = None # TypedefContext
            self.stmts = None # Statement_listContext

        def DEF(self):
            return self.getToken(MParser.DEF, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def method_identifier(self):
            return self.getTypedRuleContext(MParser.Method_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def RARROW(self):
            return self.getToken(MParser.RARROW, 0)

        def argument_list(self):
            return self.getTypedRuleContext(MParser.Argument_listContext,0)


        def typedef(self):
            return self.getTypedRuleContext(MParser.TypedefContext,0)


        def getRuleIndex(self):
            return MParser.RULE_concrete_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterConcrete_method_declaration"):
                listener.enterConcrete_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConcrete_method_declaration"):
                listener.exitConcrete_method_declaration(self)




    def concrete_method_declaration(self):

        localctx = MParser.Concrete_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_concrete_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 744
            self.match(MParser.DEF)
            self.state = 745
            localctx.name = self.method_identifier()
            self.state = 746
            self.match(MParser.LPAR)
            self.state = 748
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.CODE or _la==MParser.MUTABLE or _la==MParser.VARIABLE_IDENTIFIER:
                self.state = 747
                localctx.args = self.argument_list()


            self.state = 750
            self.match(MParser.RPAR)
            self.state = 753
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.RARROW:
                self.state = 751
                self.match(MParser.RARROW)
                self.state = 752
                localctx.typ = self.typedef(0)


            self.state = 755
            self.match(MParser.COLON)
            self.state = 756
            self.indent()
            self.state = 757
            localctx.stmts = self.statement_list()
            self.state = 758
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Native_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Argument_listContext
            self.typ = None # Category_or_any_typeContext
            self.stmts = None # Native_statement_listContext

        def DEF(self):
            return self.getToken(MParser.DEF, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def method_identifier(self):
            return self.getTypedRuleContext(MParser.Method_identifierContext,0)


        def native_statement_list(self):
            return self.getTypedRuleContext(MParser.Native_statement_listContext,0)


        def NATIVE(self):
            return self.getToken(MParser.NATIVE, 0)

        def RARROW(self):
            return self.getToken(MParser.RARROW, 0)

        def argument_list(self):
            return self.getTypedRuleContext(MParser.Argument_listContext,0)


        def category_or_any_type(self):
            return self.getTypedRuleContext(MParser.Category_or_any_typeContext,0)


        def getRuleIndex(self):
            return MParser.RULE_native_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_method_declaration"):
                listener.enterNative_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_method_declaration"):
                listener.exitNative_method_declaration(self)




    def native_method_declaration(self):

        localctx = MParser.Native_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_native_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 760
            self.match(MParser.DEF)
            self.state = 762
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.NATIVE:
                self.state = 761
                self.match(MParser.NATIVE)


            self.state = 764
            localctx.name = self.method_identifier()
            self.state = 765
            self.match(MParser.LPAR)
            self.state = 767
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.CODE or _la==MParser.MUTABLE or _la==MParser.VARIABLE_IDENTIFIER:
                self.state = 766
                localctx.args = self.argument_list()


            self.state = 769
            self.match(MParser.RPAR)
            self.state = 772
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.RARROW:
                self.state = 770
                self.match(MParser.RARROW)
                self.state = 771
                localctx.typ = self.category_or_any_type()


            self.state = 774
            self.match(MParser.COLON)
            self.state = 775
            self.indent()
            self.state = 776
            localctx.stmts = self.native_statement_list()
            self.state = 777
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Test_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Test_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.stmts = None # Statement_listContext
            self.exps = None # Assertion_listContext
            self.error = None # Symbol_identifierContext

        def DEF(self):
            return self.getToken(MParser.DEF, 0)

        def TEST(self):
            return self.getToken(MParser.TEST, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(MParser.COLON)
            else:
                return self.getToken(MParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.IndentContext)
            else:
                return self.getTypedRuleContext(MParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.DedentContext)
            else:
                return self.getTypedRuleContext(MParser.DedentContext,i)


        def lfp(self):
            return self.getTypedRuleContext(MParser.LfpContext,0)


        def VERIFYING(self):
            return self.getToken(MParser.VERIFYING, 0)

        def TEXT_LITERAL(self):
            return self.getToken(MParser.TEXT_LITERAL, 0)

        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def assertion_list(self):
            return self.getTypedRuleContext(MParser.Assertion_listContext,0)


        def symbol_identifier(self):
            return self.getTypedRuleContext(MParser.Symbol_identifierContext,0)


        def getRuleIndex(self):
            return MParser.RULE_test_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterTest_method_declaration"):
                listener.enterTest_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTest_method_declaration"):
                listener.exitTest_method_declaration(self)




    def test_method_declaration(self):

        localctx = MParser.Test_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_test_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 779
            self.match(MParser.DEF)
            self.state = 780
            self.match(MParser.TEST)
            self.state = 781
            localctx.name = self.match(MParser.TEXT_LITERAL)
            self.state = 782
            self.match(MParser.LPAR)
            self.state = 783
            self.match(MParser.RPAR)
            self.state = 784
            self.match(MParser.COLON)
            self.state = 785
            self.indent()
            self.state = 786
            localctx.stmts = self.statement_list()
            self.state = 787
            self.dedent()
            self.state = 788
            self.lfp()
            self.state = 789
            self.match(MParser.VERIFYING)
            self.state = 790
            self.match(MParser.COLON)
            self.state = 796
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.LF]:
                self.state = 791
                self.indent()
                self.state = 792
                localctx.exps = self.assertion_list()
                self.state = 793
                self.dedent()
                pass
            elif token in [MParser.SYMBOL_IDENTIFIER]:
                self.state = 795
                localctx.error = self.symbol_identifier()
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
            super(MParser.AssertionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_assertion

        def enterRule(self, listener):
            if hasattr(listener, "enterAssertion"):
                listener.enterAssertion(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssertion"):
                listener.exitAssertion(self)




    def assertion(self):

        localctx = MParser.AssertionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_assertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 798
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Typed_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Typed_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.typ = None # Category_or_any_typeContext
            self.attrs = None # Attribute_identifier_listContext
            self.value = None # Literal_expressionContext

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def category_or_any_type(self):
            return self.getTypedRuleContext(MParser.Category_or_any_typeContext,0)


        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def EQ(self):
            return self.getToken(MParser.EQ, 0)

        def attribute_identifier_list(self):
            return self.getTypedRuleContext(MParser.Attribute_identifier_listContext,0)


        def literal_expression(self):
            return self.getTypedRuleContext(MParser.Literal_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_typed_argument

        def enterRule(self, listener):
            if hasattr(listener, "enterTyped_argument"):
                listener.enterTyped_argument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTyped_argument"):
                listener.exitTyped_argument(self)




    def typed_argument(self):

        localctx = MParser.Typed_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_typed_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 800
            localctx.name = self.variable_identifier()
            self.state = 801
            self.match(MParser.COLON)
            self.state = 802
            localctx.typ = self.category_or_any_type()
            self.state = 807
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.LPAR:
                self.state = 803
                self.match(MParser.LPAR)
                self.state = 804
                localctx.attrs = self.attribute_identifier_list()
                self.state = 805
                self.match(MParser.RPAR)


            self.state = 811
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.EQ:
                self.state = 809
                self.match(MParser.EQ)
                self.state = 810
                localctx.value = self.literal_expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_statement

     
        def copyFrom(self, ctx):
            super(MParser.StatementContext, self).copyFrom(ctx)



    class CommentStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.CommentStatementContext, self).__init__(parser)
            self.decl = None # Comment_statementContext
            self.copyFrom(ctx)

        def comment_statement(self):
            return self.getTypedRuleContext(MParser.Comment_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCommentStatement"):
                listener.enterCommentStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCommentStatement"):
                listener.exitCommentStatement(self)


    class StoreStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.StoreStatementContext, self).__init__(parser)
            self.stmt = None # Store_statementContext
            self.copyFrom(ctx)

        def store_statement(self):
            return self.getTypedRuleContext(MParser.Store_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterStoreStatement"):
                listener.enterStoreStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStoreStatement"):
                listener.exitStoreStatement(self)


    class WithSingletonStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.WithSingletonStatementContext, self).__init__(parser)
            self.stmt = None # With_singleton_statementContext
            self.copyFrom(ctx)

        def with_singleton_statement(self):
            return self.getTypedRuleContext(MParser.With_singleton_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterWithSingletonStatement"):
                listener.enterWithSingletonStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWithSingletonStatement"):
                listener.exitWithSingletonStatement(self)


    class WriteStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.WriteStatementContext, self).__init__(parser)
            self.stmt = None # Write_statementContext
            self.copyFrom(ctx)

        def write_statement(self):
            return self.getTypedRuleContext(MParser.Write_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterWriteStatement"):
                listener.enterWriteStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWriteStatement"):
                listener.exitWriteStatement(self)


    class WhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.WhileStatementContext, self).__init__(parser)
            self.stmt = None # While_statementContext
            self.copyFrom(ctx)

        def while_statement(self):
            return self.getTypedRuleContext(MParser.While_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterWhileStatement"):
                listener.enterWhileStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWhileStatement"):
                listener.exitWhileStatement(self)


    class WithResourceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.WithResourceStatementContext, self).__init__(parser)
            self.stmt = None # With_resource_statementContext
            self.copyFrom(ctx)

        def with_resource_statement(self):
            return self.getTypedRuleContext(MParser.With_resource_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterWithResourceStatement"):
                listener.enterWithResourceStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWithResourceStatement"):
                listener.exitWithResourceStatement(self)


    class RaiseStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.RaiseStatementContext, self).__init__(parser)
            self.stmt = None # Raise_statementContext
            self.copyFrom(ctx)

        def raise_statement(self):
            return self.getTypedRuleContext(MParser.Raise_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterRaiseStatement"):
                listener.enterRaiseStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRaiseStatement"):
                listener.exitRaiseStatement(self)


    class BreakStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.BreakStatementContext, self).__init__(parser)
            self.stmt = None # Break_statementContext
            self.copyFrom(ctx)

        def break_statement(self):
            return self.getTypedRuleContext(MParser.Break_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterBreakStatement"):
                listener.enterBreakStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBreakStatement"):
                listener.exitBreakStatement(self)


    class AssignInstanceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.AssignInstanceStatementContext, self).__init__(parser)
            self.stmt = None # Assign_instance_statementContext
            self.copyFrom(ctx)

        def assign_instance_statement(self):
            return self.getTypedRuleContext(MParser.Assign_instance_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterAssignInstanceStatement"):
                listener.enterAssignInstanceStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssignInstanceStatement"):
                listener.exitAssignInstanceStatement(self)


    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.IfStatementContext, self).__init__(parser)
            self.stmt = None # If_statementContext
            self.copyFrom(ctx)

        def if_statement(self):
            return self.getTypedRuleContext(MParser.If_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIfStatement"):
                listener.enterIfStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIfStatement"):
                listener.exitIfStatement(self)


    class SwitchStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.SwitchStatementContext, self).__init__(parser)
            self.stmt = None # Switch_statementContext
            self.copyFrom(ctx)

        def switch_statement(self):
            return self.getTypedRuleContext(MParser.Switch_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSwitchStatement"):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSwitchStatement"):
                listener.exitSwitchStatement(self)


    class TryStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.TryStatementContext, self).__init__(parser)
            self.stmt = None # Try_statementContext
            self.copyFrom(ctx)

        def try_statement(self):
            return self.getTypedRuleContext(MParser.Try_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterTryStatement"):
                listener.enterTryStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTryStatement"):
                listener.exitTryStatement(self)


    class MethodCallStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.MethodCallStatementContext, self).__init__(parser)
            self.stmt = None # Method_callContext
            self.copyFrom(ctx)

        def method_call(self):
            return self.getTypedRuleContext(MParser.Method_callContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMethodCallStatement"):
                listener.enterMethodCallStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethodCallStatement"):
                listener.exitMethodCallStatement(self)


    class ReturnStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.ReturnStatementContext, self).__init__(parser)
            self.stmt = None # Return_statementContext
            self.copyFrom(ctx)

        def return_statement(self):
            return self.getTypedRuleContext(MParser.Return_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterReturnStatement"):
                listener.enterReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitReturnStatement"):
                listener.exitReturnStatement(self)


    class AssignTupleStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.AssignTupleStatementContext, self).__init__(parser)
            self.stmt = None # Assign_tuple_statementContext
            self.copyFrom(ctx)

        def assign_tuple_statement(self):
            return self.getTypedRuleContext(MParser.Assign_tuple_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterAssignTupleStatement"):
                listener.enterAssignTupleStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssignTupleStatement"):
                listener.exitAssignTupleStatement(self)


    class ClosureStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.ClosureStatementContext, self).__init__(parser)
            self.decl = None # Concrete_method_declarationContext
            self.copyFrom(ctx)

        def concrete_method_declaration(self):
            return self.getTypedRuleContext(MParser.Concrete_method_declarationContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterClosureStatement"):
                listener.enterClosureStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitClosureStatement"):
                listener.exitClosureStatement(self)


    class FlushStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.FlushStatementContext, self).__init__(parser)
            self.stmt = None # Flush_statementContext
            self.copyFrom(ctx)

        def flush_statement(self):
            return self.getTypedRuleContext(MParser.Flush_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterFlushStatement"):
                listener.enterFlushStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFlushStatement"):
                listener.exitFlushStatement(self)


    class DoWhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.DoWhileStatementContext, self).__init__(parser)
            self.stmt = None # Do_while_statementContext
            self.copyFrom(ctx)

        def do_while_statement(self):
            return self.getTypedRuleContext(MParser.Do_while_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterDoWhileStatement"):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDoWhileStatement"):
                listener.exitDoWhileStatement(self)


    class ForEachStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.ForEachStatementContext, self).__init__(parser)
            self.stmt = None # For_each_statementContext
            self.copyFrom(ctx)

        def for_each_statement(self):
            return self.getTypedRuleContext(MParser.For_each_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterForEachStatement"):
                listener.enterForEachStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitForEachStatement"):
                listener.exitForEachStatement(self)



    def statement(self):

        localctx = MParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_statement)
        try:
            self.state = 832
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                localctx = MParser.MethodCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 813
                localctx.stmt = self.method_call()
                pass

            elif la_ == 2:
                localctx = MParser.AssignInstanceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 814
                localctx.stmt = self.assign_instance_statement()
                pass

            elif la_ == 3:
                localctx = MParser.AssignTupleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 815
                localctx.stmt = self.assign_tuple_statement()
                pass

            elif la_ == 4:
                localctx = MParser.StoreStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 816
                localctx.stmt = self.store_statement()
                pass

            elif la_ == 5:
                localctx = MParser.FlushStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 817
                localctx.stmt = self.flush_statement()
                pass

            elif la_ == 6:
                localctx = MParser.BreakStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 818
                localctx.stmt = self.break_statement()
                pass

            elif la_ == 7:
                localctx = MParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 819
                localctx.stmt = self.return_statement()
                pass

            elif la_ == 8:
                localctx = MParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 820
                localctx.stmt = self.if_statement()
                pass

            elif la_ == 9:
                localctx = MParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 821
                localctx.stmt = self.switch_statement()
                pass

            elif la_ == 10:
                localctx = MParser.ForEachStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 822
                localctx.stmt = self.for_each_statement()
                pass

            elif la_ == 11:
                localctx = MParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 823
                localctx.stmt = self.while_statement()
                pass

            elif la_ == 12:
                localctx = MParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 824
                localctx.stmt = self.do_while_statement()
                pass

            elif la_ == 13:
                localctx = MParser.RaiseStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 825
                localctx.stmt = self.raise_statement()
                pass

            elif la_ == 14:
                localctx = MParser.TryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 826
                localctx.stmt = self.try_statement()
                pass

            elif la_ == 15:
                localctx = MParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 827
                localctx.stmt = self.write_statement()
                pass

            elif la_ == 16:
                localctx = MParser.WithResourceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 828
                localctx.stmt = self.with_resource_statement()
                pass

            elif la_ == 17:
                localctx = MParser.WithSingletonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 829
                localctx.stmt = self.with_singleton_statement()
                pass

            elif la_ == 18:
                localctx = MParser.ClosureStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 830
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 19:
                localctx = MParser.CommentStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 19)
                self.state = 831
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
            super(MParser.Flush_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FLUSH(self):
            return self.getToken(MParser.FLUSH, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def getRuleIndex(self):
            return MParser.RULE_flush_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterFlush_statement"):
                listener.enterFlush_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFlush_statement"):
                listener.exitFlush_statement(self)




    def flush_statement(self):

        localctx = MParser.Flush_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_flush_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 834
            self.match(MParser.FLUSH)
            self.state = 835
            self.match(MParser.LPAR)
            self.state = 836
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Store_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Store_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.to_del = None # Expression_listContext
            self.to_add = None # Expression_listContext

        def DELETE(self):
            return self.getToken(MParser.DELETE, 0)

        def LPAR(self, i=None):
            if i is None:
                return self.getTokens(MParser.LPAR)
            else:
                return self.getToken(MParser.LPAR, i)

        def RPAR(self, i=None):
            if i is None:
                return self.getTokens(MParser.RPAR)
            else:
                return self.getToken(MParser.RPAR, i)

        def expression_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Expression_listContext)
            else:
                return self.getTypedRuleContext(MParser.Expression_listContext,i)


        def STORE(self):
            return self.getToken(MParser.STORE, 0)

        def AND(self):
            return self.getToken(MParser.AND, 0)

        def getRuleIndex(self):
            return MParser.RULE_store_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterStore_statement"):
                listener.enterStore_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStore_statement"):
                listener.exitStore_statement(self)




    def store_statement(self):

        localctx = MParser.Store_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_store_statement)
        try:
            self.state = 858
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 838
                self.match(MParser.DELETE)
                self.state = 839
                self.match(MParser.LPAR)
                self.state = 840
                localctx.to_del = self.expression_list()
                self.state = 841
                self.match(MParser.RPAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 843
                self.match(MParser.STORE)
                self.state = 844
                self.match(MParser.LPAR)
                self.state = 845
                localctx.to_add = self.expression_list()
                self.state = 846
                self.match(MParser.RPAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 848
                self.match(MParser.DELETE)
                self.state = 849
                self.match(MParser.LPAR)
                self.state = 850
                localctx.to_del = self.expression_list()
                self.state = 851
                self.match(MParser.RPAR)
                self.state = 852
                self.match(MParser.AND)
                self.state = 853
                self.match(MParser.STORE)
                self.state = 854
                self.match(MParser.LPAR)
                self.state = 855
                localctx.to_add = self.expression_list()
                self.state = 856
                self.match(MParser.RPAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_callContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Method_callContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.method = None # Method_selectorContext
            self.args = None # Argument_assignment_listContext

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def method_selector(self):
            return self.getTypedRuleContext(MParser.Method_selectorContext,0)


        def argument_assignment_list(self):
            return self.getTypedRuleContext(MParser.Argument_assignment_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_method_call

        def enterRule(self, listener):
            if hasattr(listener, "enterMethod_call"):
                listener.enterMethod_call(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethod_call"):
                listener.exitMethod_call(self)




    def method_call(self):

        localctx = MParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 860
            localctx.method = self.method_selector()
            self.state = 861
            self.match(MParser.LPAR)
            self.state = 863
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.LTGT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 100)) & ~0x3f) == 0 and ((1 << (_la - 100)) & ((1 << (MParser.EXECUTE - 100)) | (1 << (MParser.FETCH - 100)) | (1 << (MParser.MUTABLE - 100)) | (1 << (MParser.NONE - 100)) | (1 << (MParser.NOT - 100)) | (1 << (MParser.READ - 100)) | (1 << (MParser.SELF - 100)) | (1 << (MParser.SORTED - 100)) | (1 << (MParser.THIS - 100)) | (1 << (MParser.BOOLEAN_LITERAL - 100)) | (1 << (MParser.CHAR_LITERAL - 100)) | (1 << (MParser.MIN_INTEGER - 100)) | (1 << (MParser.MAX_INTEGER - 100)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (MParser.SYMBOL_IDENTIFIER - 164)) | (1 << (MParser.TYPE_IDENTIFIER - 164)) | (1 << (MParser.VARIABLE_IDENTIFIER - 164)) | (1 << (MParser.TEXT_LITERAL - 164)) | (1 << (MParser.UUID_LITERAL - 164)) | (1 << (MParser.INTEGER_LITERAL - 164)) | (1 << (MParser.HEXA_LITERAL - 164)) | (1 << (MParser.DECIMAL_LITERAL - 164)) | (1 << (MParser.DATETIME_LITERAL - 164)) | (1 << (MParser.TIME_LITERAL - 164)) | (1 << (MParser.DATE_LITERAL - 164)) | (1 << (MParser.PERIOD_LITERAL - 164)) | (1 << (MParser.VERSION_LITERAL - 164)))) != 0):
                self.state = 862
                localctx.args = self.argument_assignment_list(0)


            self.state = 865
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Method_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_method_selector

     
        def copyFrom(self, ctx):
            super(MParser.Method_selectorContext, self).copyFrom(ctx)



    class MethodParentContext(Method_selectorContext):

        def __init__(self, parser, ctx): # actually a MParser.Method_selectorContext)
            super(MParser.MethodParentContext, self).__init__(parser)
            self.parent = None # Callable_parentContext
            self.name = None # Method_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def callable_parent(self):
            return self.getTypedRuleContext(MParser.Callable_parentContext,0)

        def method_identifier(self):
            return self.getTypedRuleContext(MParser.Method_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMethodParent"):
                listener.enterMethodParent(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethodParent"):
                listener.exitMethodParent(self)


    class MethodNameContext(Method_selectorContext):

        def __init__(self, parser, ctx): # actually a MParser.Method_selectorContext)
            super(MParser.MethodNameContext, self).__init__(parser)
            self.name = None # Method_identifierContext
            self.copyFrom(ctx)

        def method_identifier(self):
            return self.getTypedRuleContext(MParser.Method_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMethodName"):
                listener.enterMethodName(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethodName"):
                listener.exitMethodName(self)



    def method_selector(self):

        localctx = MParser.Method_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_method_selector)
        try:
            self.state = 872
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                localctx = MParser.MethodNameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 867
                localctx.name = self.method_identifier()
                pass

            elif la_ == 2:
                localctx = MParser.MethodParentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 868
                localctx.parent = self.callable_parent(0)
                self.state = 869
                self.match(MParser.DOT)
                self.state = 870
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
            super(MParser.Callable_parentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_callable_parent

     
        def copyFrom(self, ctx):
            super(MParser.Callable_parentContext, self).copyFrom(ctx)


    class CallableSelectorContext(Callable_parentContext):

        def __init__(self, parser, ctx): # actually a MParser.Callable_parentContext)
            super(MParser.CallableSelectorContext, self).__init__(parser)
            self.parent = None # Callable_parentContext
            self.select = None # Callable_selectorContext
            self.copyFrom(ctx)

        def callable_parent(self):
            return self.getTypedRuleContext(MParser.Callable_parentContext,0)

        def callable_selector(self):
            return self.getTypedRuleContext(MParser.Callable_selectorContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCallableSelector"):
                listener.enterCallableSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCallableSelector"):
                listener.exitCallableSelector(self)


    class CallableRootContext(Callable_parentContext):

        def __init__(self, parser, ctx): # actually a MParser.Callable_parentContext)
            super(MParser.CallableRootContext, self).__init__(parser)
            self.name = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(MParser.IdentifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCallableRoot"):
                listener.enterCallableRoot(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCallableRoot"):
                listener.exitCallableRoot(self)



    def callable_parent(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Callable_parentContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_callable_parent, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.CallableRootContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 875
            localctx.name = self.identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 881
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.CallableSelectorContext(self, MParser.Callable_parentContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_callable_parent)
                    self.state = 877
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 878
                    localctx.select = self.callable_selector() 
                self.state = 883
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Callable_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Callable_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_callable_selector

     
        def copyFrom(self, ctx):
            super(MParser.Callable_selectorContext, self).copyFrom(ctx)



    class CallableItemSelectorContext(Callable_selectorContext):

        def __init__(self, parser, ctx): # actually a MParser.Callable_selectorContext)
            super(MParser.CallableItemSelectorContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCallableItemSelector"):
                listener.enterCallableItemSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCallableItemSelector"):
                listener.exitCallableItemSelector(self)


    class CallableMemberSelectorContext(Callable_selectorContext):

        def __init__(self, parser, ctx): # actually a MParser.Callable_selectorContext)
            super(MParser.CallableMemberSelectorContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCallableMemberSelector"):
                listener.enterCallableMemberSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCallableMemberSelector"):
                listener.exitCallableMemberSelector(self)



    def callable_selector(self):

        localctx = MParser.Callable_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_callable_selector)
        try:
            self.state = 890
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.DOT]:
                localctx = MParser.CallableMemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 884
                self.match(MParser.DOT)
                self.state = 885
                localctx.name = self.variable_identifier()
                pass
            elif token in [MParser.LBRAK]:
                localctx = MParser.CallableItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 886
                self.match(MParser.LBRAK)
                self.state = 887
                localctx.exp = self.expression(0)
                self.state = 888
                self.match(MParser.RBRAK)
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

    class With_resource_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.With_resource_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmt = None # Assign_variable_statementContext
            self.stmts = None # Statement_listContext

        def WITH(self):
            return self.getToken(MParser.WITH, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def assign_variable_statement(self):
            return self.getTypedRuleContext(MParser.Assign_variable_statementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_with_resource_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterWith_resource_statement"):
                listener.enterWith_resource_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWith_resource_statement"):
                listener.exitWith_resource_statement(self)




    def with_resource_statement(self):

        localctx = MParser.With_resource_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_with_resource_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 892
            self.match(MParser.WITH)
            self.state = 893
            localctx.stmt = self.assign_variable_statement()
            self.state = 894
            self.match(MParser.COLON)
            self.state = 895
            self.indent()
            self.state = 896
            localctx.stmts = self.statement_list()
            self.state = 897
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class With_singleton_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.With_singleton_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # Type_identifierContext
            self.stmts = None # Statement_listContext

        def WITH(self):
            return self.getToken(MParser.WITH, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(MParser.Type_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_with_singleton_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterWith_singleton_statement"):
                listener.enterWith_singleton_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWith_singleton_statement"):
                listener.exitWith_singleton_statement(self)




    def with_singleton_statement(self):

        localctx = MParser.With_singleton_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_with_singleton_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 899
            self.match(MParser.WITH)
            self.state = 900
            localctx.typ = self.type_identifier()
            self.state = 901
            self.match(MParser.COLON)
            self.state = 902
            self.indent()
            self.state = 903
            localctx.stmts = self.statement_list()
            self.state = 904
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Switch_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Switch_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.cases = None # Switch_case_statement_listContext
            self.stmts = None # Statement_listContext

        def SWITCH(self):
            return self.getToken(MParser.SWITCH, 0)

        def ON(self):
            return self.getToken(MParser.ON, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(MParser.COLON)
            else:
                return self.getToken(MParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.IndentContext)
            else:
                return self.getTypedRuleContext(MParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.DedentContext)
            else:
                return self.getTypedRuleContext(MParser.DedentContext,i)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def switch_case_statement_list(self):
            return self.getTypedRuleContext(MParser.Switch_case_statement_listContext,0)


        def lfp(self):
            return self.getTypedRuleContext(MParser.LfpContext,0)


        def OTHERWISE(self):
            return self.getToken(MParser.OTHERWISE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_switch_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterSwitch_statement"):
                listener.enterSwitch_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSwitch_statement"):
                listener.exitSwitch_statement(self)




    def switch_statement(self):

        localctx = MParser.Switch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_switch_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 906
            self.match(MParser.SWITCH)
            self.state = 907
            self.match(MParser.ON)
            self.state = 908
            localctx.exp = self.expression(0)
            self.state = 909
            self.match(MParser.COLON)
            self.state = 910
            self.indent()
            self.state = 911
            localctx.cases = self.switch_case_statement_list()
            self.state = 919
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 912
                self.lfp()
                self.state = 913
                self.match(MParser.OTHERWISE)
                self.state = 914
                self.match(MParser.COLON)
                self.state = 915
                self.indent()
                self.state = 916
                localctx.stmts = self.statement_list()
                self.state = 917
                self.dedent()


            self.state = 921
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Switch_case_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Switch_case_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_switch_case_statement

     
        def copyFrom(self, ctx):
            super(MParser.Switch_case_statementContext, self).copyFrom(ctx)



    class AtomicSwitchCaseContext(Switch_case_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Switch_case_statementContext)
            super(MParser.AtomicSwitchCaseContext, self).__init__(parser)
            self.exp = None # Atomic_literalContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def WHEN(self):
            return self.getToken(MParser.WHEN, 0)
        def COLON(self):
            return self.getToken(MParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)

        def atomic_literal(self):
            return self.getTypedRuleContext(MParser.Atomic_literalContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterAtomicSwitchCase"):
                listener.enterAtomicSwitchCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAtomicSwitchCase"):
                listener.exitAtomicSwitchCase(self)


    class CollectionSwitchCaseContext(Switch_case_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Switch_case_statementContext)
            super(MParser.CollectionSwitchCaseContext, self).__init__(parser)
            self.exp = None # Literal_collectionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def WHEN(self):
            return self.getToken(MParser.WHEN, 0)
        def IN(self):
            return self.getToken(MParser.IN, 0)
        def COLON(self):
            return self.getToken(MParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)

        def literal_collection(self):
            return self.getTypedRuleContext(MParser.Literal_collectionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCollectionSwitchCase"):
                listener.enterCollectionSwitchCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCollectionSwitchCase"):
                listener.exitCollectionSwitchCase(self)



    def switch_case_statement(self):

        localctx = MParser.Switch_case_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_switch_case_statement)
        try:
            self.state = 938
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                localctx = MParser.AtomicSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 923
                self.match(MParser.WHEN)
                self.state = 924
                localctx.exp = self.atomic_literal()
                self.state = 925
                self.match(MParser.COLON)
                self.state = 926
                self.indent()
                self.state = 927
                localctx.stmts = self.statement_list()
                self.state = 928
                self.dedent()
                pass

            elif la_ == 2:
                localctx = MParser.CollectionSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 930
                self.match(MParser.WHEN)
                self.state = 931
                self.match(MParser.IN)
                self.state = 932
                localctx.exp = self.literal_collection()
                self.state = 933
                self.match(MParser.COLON)
                self.state = 934
                self.indent()
                self.state = 935
                localctx.stmts = self.statement_list()
                self.state = 936
                self.dedent()
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
            super(MParser.For_each_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name1 = None # Variable_identifierContext
            self.name2 = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.stmts = None # Statement_listContext

        def FOR(self):
            return self.getToken(MParser.FOR, 0)

        def IN(self):
            return self.getToken(MParser.IN, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(MParser.Variable_identifierContext,i)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)

        def getRuleIndex(self):
            return MParser.RULE_for_each_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterFor_each_statement"):
                listener.enterFor_each_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFor_each_statement"):
                listener.exitFor_each_statement(self)




    def for_each_statement(self):

        localctx = MParser.For_each_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_for_each_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 940
            self.match(MParser.FOR)
            self.state = 941
            localctx.name1 = self.variable_identifier()
            self.state = 944
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.COMMA:
                self.state = 942
                self.match(MParser.COMMA)
                self.state = 943
                localctx.name2 = self.variable_identifier()


            self.state = 946
            self.match(MParser.IN)
            self.state = 947
            localctx.source = self.expression(0)
            self.state = 948
            self.match(MParser.COLON)
            self.state = 949
            self.indent()
            self.state = 950
            localctx.stmts = self.statement_list()
            self.state = 951
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Do_while_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Do_while_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmts = None # Statement_listContext
            self.exp = None # ExpressionContext

        def DO(self):
            return self.getToken(MParser.DO, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def lfp(self):
            return self.getTypedRuleContext(MParser.LfpContext,0)


        def WHILE(self):
            return self.getToken(MParser.WHILE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_do_while_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterDo_while_statement"):
                listener.enterDo_while_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDo_while_statement"):
                listener.exitDo_while_statement(self)




    def do_while_statement(self):

        localctx = MParser.Do_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_do_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 953
            self.match(MParser.DO)
            self.state = 954
            self.match(MParser.COLON)
            self.state = 955
            self.indent()
            self.state = 956
            localctx.stmts = self.statement_list()
            self.state = 957
            self.dedent()
            self.state = 958
            self.lfp()
            self.state = 959
            self.match(MParser.WHILE)
            self.state = 960
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class While_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.While_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext

        def WHILE(self):
            return self.getToken(MParser.WHILE, 0)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_while_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterWhile_statement"):
                listener.enterWhile_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWhile_statement"):
                listener.exitWhile_statement(self)




    def while_statement(self):

        localctx = MParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 962
            self.match(MParser.WHILE)
            self.state = 963
            localctx.exp = self.expression(0)
            self.state = 964
            self.match(MParser.COLON)
            self.state = 965
            self.indent()
            self.state = 966
            localctx.stmts = self.statement_list()
            self.state = 967
            self.dedent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.If_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.elseIfs = None # Else_if_statement_listContext
            self.elseStmts = None # Statement_listContext

        def IF(self):
            return self.getToken(MParser.IF, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(MParser.COLON)
            else:
                return self.getToken(MParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.IndentContext)
            else:
                return self.getTypedRuleContext(MParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.DedentContext)
            else:
                return self.getTypedRuleContext(MParser.DedentContext,i)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def statement_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(MParser.Statement_listContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def ELSE(self):
            return self.getToken(MParser.ELSE, 0)

        def else_if_statement_list(self):
            return self.getTypedRuleContext(MParser.Else_if_statement_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_if_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterIf_statement"):
                listener.enterIf_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIf_statement"):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = MParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 969
            self.match(MParser.IF)
            self.state = 970
            localctx.exp = self.expression(0)
            self.state = 971
            self.match(MParser.COLON)
            self.state = 972
            self.indent()
            self.state = 973
            localctx.stmts = self.statement_list()
            self.state = 974
            self.dedent()
            self.state = 978
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 975
                self.lfp()
                self.state = 976
                localctx.elseIfs = self.else_if_statement_list(0)


            self.state = 987
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 980
                self.lfp()
                self.state = 981
                self.match(MParser.ELSE)
                self.state = 982
                self.match(MParser.COLON)
                self.state = 983
                self.indent()
                self.state = 984
                localctx.elseStmts = self.statement_list()
                self.state = 985
                self.dedent()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Else_if_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Else_if_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_else_if_statement_list

     
        def copyFrom(self, ctx):
            super(MParser.Else_if_statement_listContext, self).copyFrom(ctx)


    class ElseIfStatementListContext(Else_if_statement_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Else_if_statement_listContext)
            super(MParser.ElseIfStatementListContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def ELSE(self):
            return self.getToken(MParser.ELSE, 0)
        def IF(self):
            return self.getToken(MParser.IF, 0)
        def COLON(self):
            return self.getToken(MParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterElseIfStatementList"):
                listener.enterElseIfStatementList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitElseIfStatementList"):
                listener.exitElseIfStatementList(self)


    class ElseIfStatementListItemContext(Else_if_statement_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Else_if_statement_listContext)
            super(MParser.ElseIfStatementListItemContext, self).__init__(parser)
            self.items = None # Else_if_statement_listContext
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(MParser.LfpContext,0)

        def ELSE(self):
            return self.getToken(MParser.ELSE, 0)
        def IF(self):
            return self.getToken(MParser.IF, 0)
        def COLON(self):
            return self.getToken(MParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)

        def else_if_statement_list(self):
            return self.getTypedRuleContext(MParser.Else_if_statement_listContext,0)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterElseIfStatementListItem"):
                listener.enterElseIfStatementListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitElseIfStatementListItem"):
                listener.exitElseIfStatementListItem(self)



    def else_if_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Else_if_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_else_if_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.ElseIfStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 990
            self.match(MParser.ELSE)
            self.state = 991
            self.match(MParser.IF)
            self.state = 992
            localctx.exp = self.expression(0)
            self.state = 993
            self.match(MParser.COLON)
            self.state = 994
            self.indent()
            self.state = 995
            localctx.stmts = self.statement_list()
            self.state = 996
            self.dedent()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1010
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.ElseIfStatementListItemContext(self, MParser.Else_if_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_else_if_statement_list)
                    self.state = 998
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 999
                    self.lfp()
                    self.state = 1000
                    self.match(MParser.ELSE)
                    self.state = 1001
                    self.match(MParser.IF)
                    self.state = 1002
                    localctx.exp = self.expression(0)
                    self.state = 1003
                    self.match(MParser.COLON)
                    self.state = 1004
                    self.indent()
                    self.state = 1005
                    localctx.stmts = self.statement_list()
                    self.state = 1006
                    self.dedent() 
                self.state = 1012
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Raise_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Raise_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def RAISE(self):
            return self.getToken(MParser.RAISE, 0)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_raise_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterRaise_statement"):
                listener.enterRaise_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRaise_statement"):
                listener.exitRaise_statement(self)




    def raise_statement(self):

        localctx = MParser.Raise_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_raise_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1013
            self.match(MParser.RAISE)
            self.state = 1014
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Try_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Try_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext
            self.handlers = None # Catch_statement_listContext
            self.anyStmts = None # Statement_listContext
            self.finalStmts = None # Statement_listContext

        def TRY(self):
            return self.getToken(MParser.TRY, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(MParser.COLON)
            else:
                return self.getToken(MParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.IndentContext)
            else:
                return self.getTypedRuleContext(MParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.DedentContext)
            else:
                return self.getTypedRuleContext(MParser.DedentContext,i)


        def lfs(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfsContext)
            else:
                return self.getTypedRuleContext(MParser.LfsContext,i)


        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def statement_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(MParser.Statement_listContext,i)


        def EXCEPT(self):
            return self.getToken(MParser.EXCEPT, 0)

        def FINALLY(self):
            return self.getToken(MParser.FINALLY, 0)

        def catch_statement_list(self):
            return self.getTypedRuleContext(MParser.Catch_statement_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_try_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterTry_statement"):
                listener.enterTry_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTry_statement"):
                listener.exitTry_statement(self)




    def try_statement(self):

        localctx = MParser.Try_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_try_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1016
            self.match(MParser.TRY)
            self.state = 1017
            localctx.name = self.variable_identifier()
            self.state = 1018
            self.match(MParser.COLON)
            self.state = 1019
            self.indent()
            self.state = 1020
            localctx.stmts = self.statement_list()
            self.state = 1021
            self.dedent()
            self.state = 1022
            self.lfs()
            self.state = 1024
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.state = 1023
                localctx.handlers = self.catch_statement_list()


            self.state = 1033
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.EXCEPT:
                self.state = 1026
                self.match(MParser.EXCEPT)
                self.state = 1027
                self.match(MParser.COLON)
                self.state = 1028
                self.indent()
                self.state = 1029
                localctx.anyStmts = self.statement_list()
                self.state = 1030
                self.dedent()
                self.state = 1031
                self.lfs()


            self.state = 1042
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.FINALLY:
                self.state = 1035
                self.match(MParser.FINALLY)
                self.state = 1036
                self.match(MParser.COLON)
                self.state = 1037
                self.indent()
                self.state = 1038
                localctx.finalStmts = self.statement_list()
                self.state = 1039
                self.dedent()
                self.state = 1040
                self.lfs()


            self.state = 1044
            self.lfs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Catch_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Catch_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_catch_statement

     
        def copyFrom(self, ctx):
            super(MParser.Catch_statementContext, self).copyFrom(ctx)



    class CatchAtomicStatementContext(Catch_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Catch_statementContext)
            super(MParser.CatchAtomicStatementContext, self).__init__(parser)
            self.name = None # Symbol_identifierContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def EXCEPT(self):
            return self.getToken(MParser.EXCEPT, 0)
        def COLON(self):
            return self.getToken(MParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)

        def lfs(self):
            return self.getTypedRuleContext(MParser.LfsContext,0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(MParser.Symbol_identifierContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCatchAtomicStatement"):
                listener.enterCatchAtomicStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCatchAtomicStatement"):
                listener.exitCatchAtomicStatement(self)


    class CatchCollectionStatementContext(Catch_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Catch_statementContext)
            super(MParser.CatchCollectionStatementContext, self).__init__(parser)
            self.exp = None # Symbol_listContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def EXCEPT(self):
            return self.getToken(MParser.EXCEPT, 0)
        def IN(self):
            return self.getToken(MParser.IN, 0)
        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)
        def COLON(self):
            return self.getToken(MParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(MParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(MParser.DedentContext,0)

        def lfs(self):
            return self.getTypedRuleContext(MParser.LfsContext,0)

        def symbol_list(self):
            return self.getTypedRuleContext(MParser.Symbol_listContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(MParser.Statement_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCatchCollectionStatement"):
                listener.enterCatchCollectionStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCatchCollectionStatement"):
                listener.exitCatchCollectionStatement(self)



    def catch_statement(self):

        localctx = MParser.Catch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_catch_statement)
        try:
            self.state = 1065
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                localctx = MParser.CatchAtomicStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1046
                self.match(MParser.EXCEPT)
                self.state = 1047
                localctx.name = self.symbol_identifier()
                self.state = 1048
                self.match(MParser.COLON)
                self.state = 1049
                self.indent()
                self.state = 1050
                localctx.stmts = self.statement_list()
                self.state = 1051
                self.dedent()
                self.state = 1052
                self.lfs()
                pass

            elif la_ == 2:
                localctx = MParser.CatchCollectionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1054
                self.match(MParser.EXCEPT)
                self.state = 1055
                self.match(MParser.IN)
                self.state = 1056
                self.match(MParser.LBRAK)
                self.state = 1057
                localctx.exp = self.symbol_list()
                self.state = 1058
                self.match(MParser.RBRAK)
                self.state = 1059
                self.match(MParser.COLON)
                self.state = 1060
                self.indent()
                self.state = 1061
                localctx.stmts = self.statement_list()
                self.state = 1062
                self.dedent()
                self.state = 1063
                self.lfs()
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
            super(MParser.Break_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MParser.BREAK, 0)

        def getRuleIndex(self):
            return MParser.RULE_break_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterBreak_statement"):
                listener.enterBreak_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBreak_statement"):
                listener.exitBreak_statement(self)




    def break_statement(self):

        localctx = MParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1067
            self.match(MParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Return_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def RETURN(self):
            return self.getToken(MParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_return_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterReturn_statement"):
                listener.enterReturn_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitReturn_statement"):
                listener.exitReturn_statement(self)




    def return_statement(self):

        localctx = MParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1069
            self.match(MParser.RETURN)
            self.state = 1071
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.LTGT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 100)) & ~0x3f) == 0 and ((1 << (_la - 100)) & ((1 << (MParser.EXECUTE - 100)) | (1 << (MParser.FETCH - 100)) | (1 << (MParser.MUTABLE - 100)) | (1 << (MParser.NONE - 100)) | (1 << (MParser.NOT - 100)) | (1 << (MParser.READ - 100)) | (1 << (MParser.SELF - 100)) | (1 << (MParser.SORTED - 100)) | (1 << (MParser.THIS - 100)) | (1 << (MParser.BOOLEAN_LITERAL - 100)) | (1 << (MParser.CHAR_LITERAL - 100)) | (1 << (MParser.MIN_INTEGER - 100)) | (1 << (MParser.MAX_INTEGER - 100)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (MParser.SYMBOL_IDENTIFIER - 164)) | (1 << (MParser.TYPE_IDENTIFIER - 164)) | (1 << (MParser.VARIABLE_IDENTIFIER - 164)) | (1 << (MParser.TEXT_LITERAL - 164)) | (1 << (MParser.UUID_LITERAL - 164)) | (1 << (MParser.INTEGER_LITERAL - 164)) | (1 << (MParser.HEXA_LITERAL - 164)) | (1 << (MParser.DECIMAL_LITERAL - 164)) | (1 << (MParser.DATETIME_LITERAL - 164)) | (1 << (MParser.TIME_LITERAL - 164)) | (1 << (MParser.DATE_LITERAL - 164)) | (1 << (MParser.PERIOD_LITERAL - 164)) | (1 << (MParser.VERSION_LITERAL - 164)))) != 0):
                self.state = 1070
                localctx.exp = self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.ExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_expression

     
        def copyFrom(self, ctx):
            super(MParser.ExpressionContext, self).copyFrom(ctx)


    class IntDivideExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.IntDivideExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def idivide(self):
            return self.getTypedRuleContext(MParser.IdivideContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterIntDivideExpression"):
                listener.enterIntDivideExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIntDivideExpression"):
                listener.exitIntDivideExpression(self)


    class HasAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.HasAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def HAS(self):
            return self.getToken(MParser.HAS, 0)
        def ANY(self):
            return self.getToken(MParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterHasAnyExpression"):
                listener.enterHasAnyExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHasAnyExpression"):
                listener.exitHasAnyExpression(self)


    class HasExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.HasExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def HAS(self):
            return self.getToken(MParser.HAS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterHasExpression"):
                listener.enterHasExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHasExpression"):
                listener.exitHasExpression(self)


    class TernaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.TernaryExpressionContext, self).__init__(parser)
            self.ifTrue = None # ExpressionContext
            self.test = None # ExpressionContext
            self.ifFalse = None # ExpressionContext
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(MParser.IF, 0)
        def ELSE(self):
            return self.getToken(MParser.ELSE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterTernaryExpression"):
                listener.enterTernaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTernaryExpression"):
                listener.exitTernaryExpression(self)


    class NotEqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.NotEqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def XEQ(self):
            return self.getToken(MParser.XEQ, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotEqualsExpression"):
                listener.enterNotEqualsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotEqualsExpression"):
                listener.exitNotEqualsExpression(self)


    class InExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.InExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(MParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterInExpression"):
                listener.enterInExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitInExpression"):
                listener.exitInExpression(self)


    class JsxExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.JsxExpressionContext, self).__init__(parser)
            self.exp = None # Jsx_expressionContext
            self.copyFrom(ctx)

        def jsx_expression(self):
            return self.getTypedRuleContext(MParser.Jsx_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJsxExpression"):
                listener.enterJsxExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxExpression"):
                listener.exitJsxExpression(self)


    class NotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.NotExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotExpression"):
                listener.enterNotExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotExpression"):
                listener.exitNotExpression(self)


    class GreaterThanExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.GreaterThanExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def GT(self):
            return self.getToken(MParser.GT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterGreaterThanExpression"):
                listener.enterGreaterThanExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitGreaterThanExpression"):
                listener.exitGreaterThanExpression(self)


    class OrExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.OrExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def OR(self):
            return self.getToken(MParser.OR, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterOrExpression"):
                listener.enterOrExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOrExpression"):
                listener.exitOrExpression(self)


    class CodeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.CodeExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(MParser.CODE, 0)
        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCodeExpression"):
                listener.enterCodeExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCodeExpression"):
                listener.exitCodeExpression(self)


    class LessThanOrEqualExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.LessThanOrEqualExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LTE(self):
            return self.getToken(MParser.LTE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterLessThanOrEqualExpression"):
                listener.enterLessThanOrEqualExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLessThanOrEqualExpression"):
                listener.exitLessThanOrEqualExpression(self)


    class NotHasAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.NotHasAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MParser.NOT, 0)
        def HAS(self):
            return self.getToken(MParser.HAS, 0)
        def ANY(self):
            return self.getToken(MParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotHasAnyExpression"):
                listener.enterNotHasAnyExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotHasAnyExpression"):
                listener.exitNotHasAnyExpression(self)


    class AndExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.AndExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def AND(self):
            return self.getToken(MParser.AND, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterAndExpression"):
                listener.enterAndExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAndExpression"):
                listener.exitAndExpression(self)


    class NotHasExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.NotHasExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MParser.NOT, 0)
        def HAS(self):
            return self.getToken(MParser.HAS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotHasExpression"):
                listener.enterNotHasExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotHasExpression"):
                listener.exitNotHasExpression(self)


    class ClosureExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.ClosureExpressionContext, self).__init__(parser)
            self.exp = None # Closure_expressionContext
            self.copyFrom(ctx)

        def closure_expression(self):
            return self.getTypedRuleContext(MParser.Closure_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterClosureExpression"):
                listener.enterClosureExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitClosureExpression"):
                listener.exitClosureExpression(self)


    class NotHasAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.NotHasAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MParser.NOT, 0)
        def HAS(self):
            return self.getToken(MParser.HAS, 0)
        def ALL(self):
            return self.getToken(MParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotHasAllExpression"):
                listener.enterNotHasAllExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotHasAllExpression"):
                listener.exitNotHasAllExpression(self)


    class ContainsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.ContainsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(MParser.CONTAINS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterContainsExpression"):
                listener.enterContainsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitContainsExpression"):
                listener.exitContainsExpression(self)


    class FilteredListExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.FilteredListExpressionContext, self).__init__(parser)
            self.src = None # ExpressionContext
            self.copyFrom(ctx)

        def filtered_list_suffix(self):
            return self.getTypedRuleContext(MParser.Filtered_list_suffixContext,0)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterFilteredListExpression"):
                listener.enterFilteredListExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFilteredListExpression"):
                listener.exitFilteredListExpression(self)


    class NotContainsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.NotContainsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(MParser.CONTAINS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotContainsExpression"):
                listener.enterNotContainsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotContainsExpression"):
                listener.exitNotContainsExpression(self)


    class MultiplyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.MultiplyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def multiply(self):
            return self.getTypedRuleContext(MParser.MultiplyContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterMultiplyExpression"):
                listener.enterMultiplyExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMultiplyExpression"):
                listener.exitMultiplyExpression(self)


    class RoughlyEqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.RoughlyEqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def TEQ(self):
            return self.getToken(MParser.TEQ, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterRoughlyEqualsExpression"):
                listener.enterRoughlyEqualsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRoughlyEqualsExpression"):
                listener.exitRoughlyEqualsExpression(self)


    class ExecuteExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.ExecuteExpressionContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def EXECUTE(self):
            return self.getToken(MParser.EXECUTE, 0)
        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterExecuteExpression"):
                listener.enterExecuteExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExecuteExpression"):
                listener.exitExecuteExpression(self)


    class MethodExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.MethodExpressionContext, self).__init__(parser)
            self.exp = None # Method_expressionContext
            self.copyFrom(ctx)

        def method_expression(self):
            return self.getTypedRuleContext(MParser.Method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMethodExpression"):
                listener.enterMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethodExpression"):
                listener.exitMethodExpression(self)


    class GreaterThanOrEqualExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.GreaterThanOrEqualExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def GTE(self):
            return self.getToken(MParser.GTE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterGreaterThanOrEqualExpression"):
                listener.enterGreaterThanOrEqualExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitGreaterThanOrEqualExpression"):
                listener.exitGreaterThanOrEqualExpression(self)


    class NotInExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.NotInExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MParser.NOT, 0)
        def IN(self):
            return self.getToken(MParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotInExpression"):
                listener.enterNotInExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotInExpression"):
                listener.exitNotInExpression(self)


    class IteratorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.IteratorExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.name = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(MParser.FOR, 0)
        def IN(self):
            return self.getToken(MParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)

        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIteratorExpression"):
                listener.enterIteratorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIteratorExpression"):
                listener.exitIteratorExpression(self)


    class IsNotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.IsNotExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Is_expressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(MParser.IS, 0)
        def NOT(self):
            return self.getToken(MParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)

        def is_expression(self):
            return self.getTypedRuleContext(MParser.Is_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIsNotExpression"):
                listener.enterIsNotExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsNotExpression"):
                listener.exitIsNotExpression(self)


    class DivideExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.DivideExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def divide(self):
            return self.getTypedRuleContext(MParser.DivideContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterDivideExpression"):
                listener.enterDivideExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDivideExpression"):
                listener.exitDivideExpression(self)


    class IsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.IsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Is_expressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(MParser.IS, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)

        def is_expression(self):
            return self.getTypedRuleContext(MParser.Is_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIsExpression"):
                listener.enterIsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsExpression"):
                listener.exitIsExpression(self)


    class MinusExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.MinusExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(MParser.MINUS, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMinusExpression"):
                listener.enterMinusExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMinusExpression"):
                listener.exitMinusExpression(self)


    class AddExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.AddExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.op = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(MParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(MParser.MINUS, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAddExpression"):
                listener.enterAddExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAddExpression"):
                listener.exitAddExpression(self)


    class HasAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.HasAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def HAS(self):
            return self.getToken(MParser.HAS, 0)
        def ALL(self):
            return self.getToken(MParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterHasAllExpression"):
                listener.enterHasAllExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHasAllExpression"):
                listener.exitHasAllExpression(self)


    class InstanceExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.InstanceExpressionContext, self).__init__(parser)
            self.exp = None # Instance_expressionContext
            self.copyFrom(ctx)

        def instance_expression(self):
            return self.getTypedRuleContext(MParser.Instance_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterInstanceExpression"):
                listener.enterInstanceExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitInstanceExpression"):
                listener.exitInstanceExpression(self)


    class CssExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.CssExpressionContext, self).__init__(parser)
            self.exp = None # Css_expressionContext
            self.copyFrom(ctx)

        def css_expression(self):
            return self.getTypedRuleContext(MParser.Css_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCssExpression"):
                listener.enterCssExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCssExpression"):
                listener.exitCssExpression(self)


    class CastExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.CastExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Category_or_any_typeContext
            self.copyFrom(ctx)

        def AS(self):
            return self.getToken(MParser.AS, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)

        def category_or_any_type(self):
            return self.getTypedRuleContext(MParser.Category_or_any_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCastExpression"):
                listener.enterCastExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCastExpression"):
                listener.exitCastExpression(self)


    class ModuloExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.ModuloExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def modulo(self):
            return self.getTypedRuleContext(MParser.ModuloContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterModuloExpression"):
                listener.enterModuloExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitModuloExpression"):
                listener.exitModuloExpression(self)


    class LessThanExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.LessThanExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(MParser.LT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterLessThanExpression"):
                listener.enterLessThanExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLessThanExpression"):
                listener.exitLessThanExpression(self)


    class EqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.EqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def EQ2(self):
            return self.getToken(MParser.EQ2, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterEqualsExpression"):
                listener.enterEqualsExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEqualsExpression"):
                listener.exitEqualsExpression(self)



    def expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1093
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                localctx = MParser.CssExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1074
                localctx.exp = self.css_expression()
                pass

            elif la_ == 2:
                localctx = MParser.JsxExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1075
                localctx.exp = self.jsx_expression()
                pass

            elif la_ == 3:
                localctx = MParser.InstanceExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1076
                localctx.exp = self.instance_expression(0)
                pass

            elif la_ == 4:
                localctx = MParser.MethodExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1077
                localctx.exp = self.method_expression()
                pass

            elif la_ == 5:
                localctx = MParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1078
                self.match(MParser.MINUS)
                self.state = 1079
                localctx.exp = self.expression(34)
                pass

            elif la_ == 6:
                localctx = MParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1080
                self.match(MParser.NOT)
                self.state = 1081
                localctx.exp = self.expression(33)
                pass

            elif la_ == 7:
                localctx = MParser.CodeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1082
                self.match(MParser.CODE)
                self.state = 1083
                self.match(MParser.LPAR)
                self.state = 1084
                localctx.exp = self.expression(0)
                self.state = 1085
                self.match(MParser.RPAR)
                pass

            elif la_ == 8:
                localctx = MParser.ExecuteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1087
                self.match(MParser.EXECUTE)
                self.state = 1088
                self.match(MParser.LPAR)
                self.state = 1089
                localctx.name = self.variable_identifier()
                self.state = 1090
                self.match(MParser.RPAR)
                pass

            elif la_ == 9:
                localctx = MParser.ClosureExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1092
                localctx.exp = self.closure_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1206
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,54,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1204
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                    if la_ == 1:
                        localctx = MParser.MultiplyExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1095
                        if not self.precpred(self._ctx, 32):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 32)")
                        self.state = 1096
                        self.multiply()
                        self.state = 1097
                        localctx.right = self.expression(33)
                        pass

                    elif la_ == 2:
                        localctx = MParser.DivideExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1099
                        if not self.precpred(self._ctx, 31):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 31)")
                        self.state = 1100
                        self.divide()
                        self.state = 1101
                        localctx.right = self.expression(32)
                        pass

                    elif la_ == 3:
                        localctx = MParser.ModuloExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1103
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 1104
                        self.modulo()
                        self.state = 1105
                        localctx.right = self.expression(31)
                        pass

                    elif la_ == 4:
                        localctx = MParser.IntDivideExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1107
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 1108
                        self.idivide()
                        self.state = 1109
                        localctx.right = self.expression(30)
                        pass

                    elif la_ == 5:
                        localctx = MParser.AddExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1111
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 1112
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==MParser.PLUS or _la==MParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 1113
                        localctx.right = self.expression(29)
                        pass

                    elif la_ == 6:
                        localctx = MParser.LessThanExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1114
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 1115
                        self.match(MParser.LT)
                        self.state = 1116
                        localctx.right = self.expression(27)
                        pass

                    elif la_ == 7:
                        localctx = MParser.LessThanOrEqualExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1117
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 1118
                        self.match(MParser.LTE)
                        self.state = 1119
                        localctx.right = self.expression(26)
                        pass

                    elif la_ == 8:
                        localctx = MParser.GreaterThanExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1120
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 1121
                        self.match(MParser.GT)
                        self.state = 1122
                        localctx.right = self.expression(25)
                        pass

                    elif la_ == 9:
                        localctx = MParser.GreaterThanOrEqualExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1123
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 1124
                        self.match(MParser.GTE)
                        self.state = 1125
                        localctx.right = self.expression(24)
                        pass

                    elif la_ == 10:
                        localctx = MParser.EqualsExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1126
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 1127
                        self.match(MParser.EQ2)
                        self.state = 1128
                        localctx.right = self.expression(21)
                        pass

                    elif la_ == 11:
                        localctx = MParser.NotEqualsExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1129
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 1130
                        self.match(MParser.XEQ)
                        self.state = 1131
                        localctx.right = self.expression(20)
                        pass

                    elif la_ == 12:
                        localctx = MParser.RoughlyEqualsExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1132
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 1133
                        self.match(MParser.TEQ)
                        self.state = 1134
                        localctx.right = self.expression(19)
                        pass

                    elif la_ == 13:
                        localctx = MParser.ContainsExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1135
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 1136
                        self.match(MParser.CONTAINS)
                        self.state = 1137
                        localctx.right = self.expression(18)
                        pass

                    elif la_ == 14:
                        localctx = MParser.InExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1138
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 1139
                        self.match(MParser.IN)
                        self.state = 1140
                        localctx.right = self.expression(17)
                        pass

                    elif la_ == 15:
                        localctx = MParser.HasExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1141
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 1142
                        self.match(MParser.HAS)
                        self.state = 1143
                        localctx.right = self.expression(16)
                        pass

                    elif la_ == 16:
                        localctx = MParser.HasAllExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1144
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 1145
                        self.match(MParser.HAS)
                        self.state = 1146
                        self.match(MParser.ALL)
                        self.state = 1147
                        localctx.right = self.expression(15)
                        pass

                    elif la_ == 17:
                        localctx = MParser.HasAnyExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1148
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 1149
                        self.match(MParser.HAS)
                        self.state = 1150
                        self.match(MParser.ANY)
                        self.state = 1151
                        localctx.right = self.expression(14)
                        pass

                    elif la_ == 18:
                        localctx = MParser.NotContainsExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1152
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 1153
                        self.match(MParser.NOT)
                        self.state = 1154
                        self.match(MParser.CONTAINS)
                        self.state = 1155
                        localctx.right = self.expression(13)
                        pass

                    elif la_ == 19:
                        localctx = MParser.NotInExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1156
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 1157
                        self.match(MParser.NOT)
                        self.state = 1158
                        self.match(MParser.IN)
                        self.state = 1159
                        localctx.right = self.expression(12)
                        pass

                    elif la_ == 20:
                        localctx = MParser.NotHasExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1160
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 1161
                        self.match(MParser.NOT)
                        self.state = 1162
                        self.match(MParser.HAS)
                        self.state = 1163
                        localctx.right = self.expression(11)
                        pass

                    elif la_ == 21:
                        localctx = MParser.NotHasAllExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1164
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 1165
                        self.match(MParser.NOT)
                        self.state = 1166
                        self.match(MParser.HAS)
                        self.state = 1167
                        self.match(MParser.ALL)
                        self.state = 1168
                        localctx.right = self.expression(10)
                        pass

                    elif la_ == 22:
                        localctx = MParser.NotHasAnyExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1169
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 1170
                        self.match(MParser.NOT)
                        self.state = 1171
                        self.match(MParser.HAS)
                        self.state = 1172
                        self.match(MParser.ANY)
                        self.state = 1173
                        localctx.right = self.expression(9)
                        pass

                    elif la_ == 23:
                        localctx = MParser.OrExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1174
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 1175
                        self.match(MParser.OR)
                        self.state = 1176
                        localctx.right = self.expression(8)
                        pass

                    elif la_ == 24:
                        localctx = MParser.AndExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1177
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 1178
                        self.match(MParser.AND)
                        self.state = 1179
                        localctx.right = self.expression(7)
                        pass

                    elif la_ == 25:
                        localctx = MParser.TernaryExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.ifTrue = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1180
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 1181
                        self.match(MParser.IF)
                        self.state = 1182
                        localctx.test = self.expression(0)
                        self.state = 1183
                        self.match(MParser.ELSE)
                        self.state = 1184
                        localctx.ifFalse = self.expression(6)
                        pass

                    elif la_ == 26:
                        localctx = MParser.IteratorExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.exp = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1186
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1187
                        self.match(MParser.FOR)
                        self.state = 1188
                        localctx.name = self.variable_identifier()
                        self.state = 1189
                        self.match(MParser.IN)
                        self.state = 1190
                        localctx.source = self.expression(2)
                        pass

                    elif la_ == 27:
                        localctx = MParser.FilteredListExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.src = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1192
                        if not self.precpred(self._ctx, 36):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 36)")
                        self.state = 1193
                        self.filtered_list_suffix()
                        pass

                    elif la_ == 28:
                        localctx = MParser.CastExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1194
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 1195
                        self.match(MParser.AS)
                        self.state = 1196
                        localctx.right = self.category_or_any_type()
                        pass

                    elif la_ == 29:
                        localctx = MParser.IsNotExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1197
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 1198
                        self.match(MParser.IS)
                        self.state = 1199
                        self.match(MParser.NOT)
                        self.state = 1200
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 30:
                        localctx = MParser.IsExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1201
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 1202
                        self.match(MParser.IS)
                        self.state = 1203
                        localctx.right = self.is_expression()
                        pass

             
                self.state = 1208
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,54,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Closure_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Closure_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext

        def type_identifier(self):
            return self.getTypedRuleContext(MParser.Type_identifierContext,0)


        def getRuleIndex(self):
            return MParser.RULE_closure_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterClosure_expression"):
                listener.enterClosure_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitClosure_expression"):
                listener.exitClosure_expression(self)




    def closure_expression(self):

        localctx = MParser.Closure_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_closure_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1209
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
            super(MParser.Instance_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_instance_expression

     
        def copyFrom(self, ctx):
            super(MParser.Instance_expressionContext, self).copyFrom(ctx)


    class SelectorExpressionContext(Instance_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Instance_expressionContext)
            super(MParser.SelectorExpressionContext, self).__init__(parser)
            self.parent = None # Instance_expressionContext
            self.selector = None # Instance_selectorContext
            self.copyFrom(ctx)

        def instance_expression(self):
            return self.getTypedRuleContext(MParser.Instance_expressionContext,0)

        def instance_selector(self):
            return self.getTypedRuleContext(MParser.Instance_selectorContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSelectorExpression"):
                listener.enterSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSelectorExpression"):
                listener.exitSelectorExpression(self)


    class SelectableExpressionContext(Instance_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Instance_expressionContext)
            super(MParser.SelectableExpressionContext, self).__init__(parser)
            self.parent = None # Selectable_expressionContext
            self.copyFrom(ctx)

        def selectable_expression(self):
            return self.getTypedRuleContext(MParser.Selectable_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSelectableExpression"):
                listener.enterSelectableExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSelectableExpression"):
                listener.exitSelectableExpression(self)



    def instance_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Instance_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_instance_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.SelectableExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1212
            localctx.parent = self.selectable_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1218
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.SelectorExpressionContext(self, MParser.Instance_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_expression)
                    self.state = 1214
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1215
                    localctx.selector = self.instance_selector() 
                self.state = 1220
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Method_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def blob_expression(self):
            return self.getTypedRuleContext(MParser.Blob_expressionContext,0)


        def document_expression(self):
            return self.getTypedRuleContext(MParser.Document_expressionContext,0)


        def fetch_store_expression(self):
            return self.getTypedRuleContext(MParser.Fetch_store_expressionContext,0)


        def read_all_expression(self):
            return self.getTypedRuleContext(MParser.Read_all_expressionContext,0)


        def read_one_expression(self):
            return self.getTypedRuleContext(MParser.Read_one_expressionContext,0)


        def sorted_expression(self):
            return self.getTypedRuleContext(MParser.Sorted_expressionContext,0)


        def method_call(self):
            return self.getTypedRuleContext(MParser.Method_callContext,0)


        def constructor_expression(self):
            return self.getTypedRuleContext(MParser.Constructor_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_method_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterMethod_expression"):
                listener.enterMethod_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethod_expression"):
                listener.exitMethod_expression(self)




    def method_expression(self):

        localctx = MParser.Method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_method_expression)
        try:
            self.state = 1229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1221
                self.blob_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1222
                self.document_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1223
                self.fetch_store_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1224
                self.read_all_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1225
                self.read_one_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1226
                self.sorted_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1227
                self.method_call()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1228
                self.constructor_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Instance_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Instance_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_instance_selector

     
        def copyFrom(self, ctx):
            super(MParser.Instance_selectorContext, self).copyFrom(ctx)



    class SliceSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a MParser.Instance_selectorContext)
            super(MParser.SliceSelectorContext, self).__init__(parser)
            self.xslice = None # Slice_argumentsContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)
        def slice_arguments(self):
            return self.getTypedRuleContext(MParser.Slice_argumentsContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSliceSelector"):
                listener.enterSliceSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSliceSelector"):
                listener.exitSliceSelector(self)


    class MemberSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a MParser.Instance_selectorContext)
            super(MParser.MemberSelectorContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMemberSelector"):
                listener.enterMemberSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMemberSelector"):
                listener.exitMemberSelector(self)


    class ItemSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a MParser.Instance_selectorContext)
            super(MParser.ItemSelectorContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterItemSelector"):
                listener.enterItemSelector(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitItemSelector"):
                listener.exitItemSelector(self)



    def instance_selector(self):

        localctx = MParser.Instance_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_instance_selector)
        try:
            self.state = 1244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                localctx = MParser.MemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1231
                if not self.wasNot(MParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(MParser.WS)")
                self.state = 1232
                self.match(MParser.DOT)
                self.state = 1233
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = MParser.SliceSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1234
                if not self.wasNot(MParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(MParser.WS)")
                self.state = 1235
                self.match(MParser.LBRAK)
                self.state = 1236
                localctx.xslice = self.slice_arguments()
                self.state = 1237
                self.match(MParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = MParser.ItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1239
                if not self.wasNot(MParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(MParser.WS)")
                self.state = 1240
                self.match(MParser.LBRAK)
                self.state = 1241
                localctx.exp = self.expression(0)
                self.state = 1242
                self.match(MParser.RBRAK)
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
            super(MParser.Blob_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BLOB(self):
            return self.getToken(MParser.BLOB, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_blob_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterBlob_expression"):
                listener.enterBlob_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBlob_expression"):
                listener.exitBlob_expression(self)




    def blob_expression(self):

        localctx = MParser.Blob_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_blob_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1246
            self.match(MParser.BLOB)
            self.state = 1247
            self.match(MParser.LPAR)
            self.state = 1249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.LTGT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 100)) & ~0x3f) == 0 and ((1 << (_la - 100)) & ((1 << (MParser.EXECUTE - 100)) | (1 << (MParser.FETCH - 100)) | (1 << (MParser.MUTABLE - 100)) | (1 << (MParser.NONE - 100)) | (1 << (MParser.NOT - 100)) | (1 << (MParser.READ - 100)) | (1 << (MParser.SELF - 100)) | (1 << (MParser.SORTED - 100)) | (1 << (MParser.THIS - 100)) | (1 << (MParser.BOOLEAN_LITERAL - 100)) | (1 << (MParser.CHAR_LITERAL - 100)) | (1 << (MParser.MIN_INTEGER - 100)) | (1 << (MParser.MAX_INTEGER - 100)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (MParser.SYMBOL_IDENTIFIER - 164)) | (1 << (MParser.TYPE_IDENTIFIER - 164)) | (1 << (MParser.VARIABLE_IDENTIFIER - 164)) | (1 << (MParser.TEXT_LITERAL - 164)) | (1 << (MParser.UUID_LITERAL - 164)) | (1 << (MParser.INTEGER_LITERAL - 164)) | (1 << (MParser.HEXA_LITERAL - 164)) | (1 << (MParser.DECIMAL_LITERAL - 164)) | (1 << (MParser.DATETIME_LITERAL - 164)) | (1 << (MParser.TIME_LITERAL - 164)) | (1 << (MParser.DATE_LITERAL - 164)) | (1 << (MParser.PERIOD_LITERAL - 164)) | (1 << (MParser.VERSION_LITERAL - 164)))) != 0):
                self.state = 1248
                self.expression(0)


            self.state = 1251
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Document_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Document_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DOCUMENT(self):
            return self.getToken(MParser.DOCUMENT, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_document_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterDocument_expression"):
                listener.enterDocument_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDocument_expression"):
                listener.exitDocument_expression(self)




    def document_expression(self):

        localctx = MParser.Document_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_document_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1253
            self.match(MParser.DOCUMENT)
            self.state = 1254
            self.match(MParser.LPAR)
            self.state = 1256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.LTGT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 100)) & ~0x3f) == 0 and ((1 << (_la - 100)) & ((1 << (MParser.EXECUTE - 100)) | (1 << (MParser.FETCH - 100)) | (1 << (MParser.MUTABLE - 100)) | (1 << (MParser.NONE - 100)) | (1 << (MParser.NOT - 100)) | (1 << (MParser.READ - 100)) | (1 << (MParser.SELF - 100)) | (1 << (MParser.SORTED - 100)) | (1 << (MParser.THIS - 100)) | (1 << (MParser.BOOLEAN_LITERAL - 100)) | (1 << (MParser.CHAR_LITERAL - 100)) | (1 << (MParser.MIN_INTEGER - 100)) | (1 << (MParser.MAX_INTEGER - 100)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (MParser.SYMBOL_IDENTIFIER - 164)) | (1 << (MParser.TYPE_IDENTIFIER - 164)) | (1 << (MParser.VARIABLE_IDENTIFIER - 164)) | (1 << (MParser.TEXT_LITERAL - 164)) | (1 << (MParser.UUID_LITERAL - 164)) | (1 << (MParser.INTEGER_LITERAL - 164)) | (1 << (MParser.HEXA_LITERAL - 164)) | (1 << (MParser.DECIMAL_LITERAL - 164)) | (1 << (MParser.DATETIME_LITERAL - 164)) | (1 << (MParser.TIME_LITERAL - 164)) | (1 << (MParser.DATE_LITERAL - 164)) | (1 << (MParser.PERIOD_LITERAL - 164)) | (1 << (MParser.VERSION_LITERAL - 164)))) != 0):
                self.state = 1255
                self.expression(0)


            self.state = 1258
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Constructor_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Constructor_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_constructor_expression

     
        def copyFrom(self, ctx):
            super(MParser.Constructor_expressionContext, self).copyFrom(ctx)



    class ConstructorFromContext(Constructor_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Constructor_expressionContext)
            super(MParser.ConstructorFromContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.copyExp = None # Copy_fromContext
            self.args = None # Argument_assignment_listContext
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)
        def mutable_category_type(self):
            return self.getTypedRuleContext(MParser.Mutable_category_typeContext,0)

        def copy_from(self):
            return self.getTypedRuleContext(MParser.Copy_fromContext,0)

        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)
        def argument_assignment_list(self):
            return self.getTypedRuleContext(MParser.Argument_assignment_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterConstructorFrom"):
                listener.enterConstructorFrom(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConstructorFrom"):
                listener.exitConstructorFrom(self)


    class ConstructorNoFromContext(Constructor_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Constructor_expressionContext)
            super(MParser.ConstructorNoFromContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.args = None # Argument_assignment_listContext
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)
        def mutable_category_type(self):
            return self.getTypedRuleContext(MParser.Mutable_category_typeContext,0)

        def argument_assignment_list(self):
            return self.getTypedRuleContext(MParser.Argument_assignment_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterConstructorNoFrom"):
                listener.enterConstructorNoFrom(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConstructorNoFrom"):
                listener.exitConstructorNoFrom(self)



    def constructor_expression(self):

        localctx = MParser.Constructor_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_constructor_expression)
        self._la = 0 # Token type
        try:
            self.state = 1276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                localctx = MParser.ConstructorFromContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1260
                localctx.typ = self.mutable_category_type()
                self.state = 1261
                self.match(MParser.LPAR)
                self.state = 1262
                localctx.copyExp = self.copy_from()
                self.state = 1265
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MParser.COMMA:
                    self.state = 1263
                    self.match(MParser.COMMA)
                    self.state = 1264
                    localctx.args = self.argument_assignment_list(0)


                self.state = 1267
                self.match(MParser.RPAR)
                pass

            elif la_ == 2:
                localctx = MParser.ConstructorNoFromContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1269
                localctx.typ = self.mutable_category_type()
                self.state = 1270
                self.match(MParser.LPAR)
                self.state = 1272
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.LTGT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 100)) & ~0x3f) == 0 and ((1 << (_la - 100)) & ((1 << (MParser.EXECUTE - 100)) | (1 << (MParser.FETCH - 100)) | (1 << (MParser.MUTABLE - 100)) | (1 << (MParser.NONE - 100)) | (1 << (MParser.NOT - 100)) | (1 << (MParser.READ - 100)) | (1 << (MParser.SELF - 100)) | (1 << (MParser.SORTED - 100)) | (1 << (MParser.THIS - 100)) | (1 << (MParser.BOOLEAN_LITERAL - 100)) | (1 << (MParser.CHAR_LITERAL - 100)) | (1 << (MParser.MIN_INTEGER - 100)) | (1 << (MParser.MAX_INTEGER - 100)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (MParser.SYMBOL_IDENTIFIER - 164)) | (1 << (MParser.TYPE_IDENTIFIER - 164)) | (1 << (MParser.VARIABLE_IDENTIFIER - 164)) | (1 << (MParser.TEXT_LITERAL - 164)) | (1 << (MParser.UUID_LITERAL - 164)) | (1 << (MParser.INTEGER_LITERAL - 164)) | (1 << (MParser.HEXA_LITERAL - 164)) | (1 << (MParser.DECIMAL_LITERAL - 164)) | (1 << (MParser.DATETIME_LITERAL - 164)) | (1 << (MParser.TIME_LITERAL - 164)) | (1 << (MParser.DATE_LITERAL - 164)) | (1 << (MParser.PERIOD_LITERAL - 164)) | (1 << (MParser.VERSION_LITERAL - 164)))) != 0):
                    self.state = 1271
                    localctx.args = self.argument_assignment_list(0)


                self.state = 1274
                self.match(MParser.RPAR)
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
            super(MParser.Copy_fromContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def FROM(self):
            return self.getToken(MParser.FROM, 0)

        def assign(self):
            return self.getTypedRuleContext(MParser.AssignContext,0)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_copy_from

        def enterRule(self, listener):
            if hasattr(listener, "enterCopy_from"):
                listener.enterCopy_from(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCopy_from"):
                listener.exitCopy_from(self)




    def copy_from(self):

        localctx = MParser.Copy_fromContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_copy_from)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1278
            self.match(MParser.FROM)
            self.state = 1279
            self.assign()
            self.state = 1280
            localctx.exp = self.expression(0)
            self.state = 1281
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
            super(MParser.Argument_assignment_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_argument_assignment_list

     
        def copyFrom(self, ctx):
            super(MParser.Argument_assignment_listContext, self).copyFrom(ctx)


    class ExpressionAssignmentListContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Argument_assignment_listContext)
            super(MParser.ExpressionAssignmentListContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterExpressionAssignmentList"):
                listener.enterExpressionAssignmentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExpressionAssignmentList"):
                listener.exitExpressionAssignmentList(self)


    class ArgumentAssignmentListContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Argument_assignment_listContext)
            super(MParser.ArgumentAssignmentListContext, self).__init__(parser)
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def argument_assignment(self):
            return self.getTypedRuleContext(MParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterArgumentAssignmentList"):
                listener.enterArgumentAssignmentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgumentAssignmentList"):
                listener.exitArgumentAssignmentList(self)


    class ArgumentAssignmentListItemContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Argument_assignment_listContext)
            super(MParser.ArgumentAssignmentListItemContext, self).__init__(parser)
            self.items = None # Argument_assignment_listContext
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)
        def argument_assignment_list(self):
            return self.getTypedRuleContext(MParser.Argument_assignment_listContext,0)

        def argument_assignment(self):
            return self.getTypedRuleContext(MParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterArgumentAssignmentListItem"):
                listener.enterArgumentAssignmentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgumentAssignmentListItem"):
                listener.exitArgumentAssignmentListItem(self)



    def argument_assignment_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Argument_assignment_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_argument_assignment_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                localctx = MParser.ExpressionAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1284
                localctx.exp = self.expression(0)
                self.state = 1285
                if not self.willNotBe(self.equalToken()):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willNotBe($parser.equalToken())")
                pass

            elif la_ == 2:
                localctx = MParser.ArgumentAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1287
                localctx.item = self.argument_assignment()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1295
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.ArgumentAssignmentListItemContext(self, MParser.Argument_assignment_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_assignment_list)
                    self.state = 1290
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1291
                    self.match(MParser.COMMA)
                    self.state = 1292
                    localctx.item = self.argument_assignment() 
                self.state = 1297
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Argument_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Argument_assignmentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.exp = None # ExpressionContext

        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def assign(self):
            return self.getTypedRuleContext(MParser.AssignContext,0)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_argument_assignment

        def enterRule(self, listener):
            if hasattr(listener, "enterArgument_assignment"):
                listener.enterArgument_assignment(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgument_assignment"):
                listener.exitArgument_assignment(self)




    def argument_assignment(self):

        localctx = MParser.Argument_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_argument_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1298
            localctx.name = self.variable_identifier()
            self.state = 1302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.state = 1299
                self.assign()
                self.state = 1300
                localctx.exp = self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Write_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Write_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.what = None # ExpressionContext
            self.target = None # ExpressionContext

        def WRITE(self):
            return self.getToken(MParser.WRITE, 0)

        def TO(self):
            return self.getToken(MParser.TO, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MParser.RULE_write_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterWrite_statement"):
                listener.enterWrite_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWrite_statement"):
                listener.exitWrite_statement(self)




    def write_statement(self):

        localctx = MParser.Write_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_write_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1304
            self.match(MParser.WRITE)
            self.state = 1305
            localctx.what = self.expression(0)
            self.state = 1306
            self.match(MParser.TO)
            self.state = 1307
            localctx.target = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Filtered_list_suffixContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Filtered_list_suffixContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.predicate = None # ExpressionContext

        def FILTERED(self):
            return self.getToken(MParser.FILTERED, 0)

        def WITH(self):
            return self.getToken(MParser.WITH, 0)

        def WHERE(self):
            return self.getToken(MParser.WHERE, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_filtered_list_suffix

        def enterRule(self, listener):
            if hasattr(listener, "enterFiltered_list_suffix"):
                listener.enterFiltered_list_suffix(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFiltered_list_suffix"):
                listener.exitFiltered_list_suffix(self)




    def filtered_list_suffix(self):

        localctx = MParser.Filtered_list_suffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_filtered_list_suffix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1309
            self.match(MParser.FILTERED)
            self.state = 1310
            self.match(MParser.WITH)
            self.state = 1311
            localctx.name = self.variable_identifier()
            self.state = 1312
            self.match(MParser.WHERE)
            self.state = 1313
            localctx.predicate = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fetch_store_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Fetch_store_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_fetch_store_expression

     
        def copyFrom(self, ctx):
            super(MParser.Fetch_store_expressionContext, self).copyFrom(ctx)



    class FetchOneContext(Fetch_store_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Fetch_store_expressionContext)
            super(MParser.FetchOneContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.predicate = None # ExpressionContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(MParser.FETCH, 0)
        def ONE(self):
            return self.getToken(MParser.ONE, 0)
        def WHERE(self):
            return self.getToken(MParser.WHERE, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)

        def mutable_category_type(self):
            return self.getTypedRuleContext(MParser.Mutable_category_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterFetchOne"):
                listener.enterFetchOne(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFetchOne"):
                listener.exitFetchOne(self)


    class FetchManyContext(Fetch_store_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Fetch_store_expressionContext)
            super(MParser.FetchManyContext, self).__init__(parser)
            self.xstart = None # ExpressionContext
            self.xstop = None # ExpressionContext
            self.typ = None # Mutable_category_typeContext
            self.predicate = None # ExpressionContext
            self.orderby = None # Order_by_listContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(MParser.FETCH, 0)
        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)
        def ALL(self):
            return self.getToken(MParser.ALL, 0)
        def ROWS(self):
            return self.getToken(MParser.ROWS, 0)
        def TO(self):
            return self.getToken(MParser.TO, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)

        def WHERE(self):
            return self.getToken(MParser.WHERE, 0)
        def ORDER(self):
            return self.getToken(MParser.ORDER, 0)
        def BY(self):
            return self.getToken(MParser.BY, 0)
        def mutable_category_type(self):
            return self.getTypedRuleContext(MParser.Mutable_category_typeContext,0)

        def order_by_list(self):
            return self.getTypedRuleContext(MParser.Order_by_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterFetchMany"):
                listener.enterFetchMany(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFetchMany"):
                listener.exitFetchMany(self)



    def fetch_store_expression(self):

        localctx = MParser.Fetch_store_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_fetch_store_expression)
        self._la = 0 # Token type
        try:
            self.state = 1345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                localctx = MParser.FetchOneContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1315
                self.match(MParser.FETCH)
                self.state = 1316
                self.match(MParser.ONE)
                self.state = 1318
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MParser.MUTABLE or _la==MParser.TYPE_IDENTIFIER:
                    self.state = 1317
                    localctx.typ = self.mutable_category_type()


                self.state = 1320
                self.match(MParser.WHERE)
                self.state = 1321
                localctx.predicate = self.expression(0)
                pass

            elif la_ == 2:
                localctx = MParser.FetchManyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1322
                self.match(MParser.FETCH)
                self.state = 1329
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MParser.ALL]:
                    self.state = 1323
                    self.match(MParser.ALL)
                    pass
                elif token in [MParser.ROWS]:
                    self.state = 1324
                    self.match(MParser.ROWS)
                    self.state = 1325
                    localctx.xstart = self.expression(0)
                    self.state = 1326
                    self.match(MParser.TO)
                    self.state = 1327
                    localctx.xstop = self.expression(0)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1331
                self.match(MParser.LPAR)
                self.state = 1333
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MParser.MUTABLE or _la==MParser.TYPE_IDENTIFIER:
                    self.state = 1332
                    localctx.typ = self.mutable_category_type()


                self.state = 1335
                self.match(MParser.RPAR)
                self.state = 1338
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
                if la_ == 1:
                    self.state = 1336
                    self.match(MParser.WHERE)
                    self.state = 1337
                    localctx.predicate = self.expression(0)


                self.state = 1343
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
                if la_ == 1:
                    self.state = 1340
                    self.match(MParser.ORDER)
                    self.state = 1341
                    self.match(MParser.BY)
                    self.state = 1342
                    localctx.orderby = self.order_by_list()


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
            super(MParser.Sorted_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # Instance_expressionContext
            self.key = None # Instance_expressionContext

        def SORTED(self):
            return self.getToken(MParser.SORTED, 0)

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def instance_expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Instance_expressionContext)
            else:
                return self.getTypedRuleContext(MParser.Instance_expressionContext,i)


        def DESC(self):
            return self.getToken(MParser.DESC, 0)

        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)

        def key_token(self):
            return self.getTypedRuleContext(MParser.Key_tokenContext,0)


        def EQ(self):
            return self.getToken(MParser.EQ, 0)

        def getRuleIndex(self):
            return MParser.RULE_sorted_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterSorted_expression"):
                listener.enterSorted_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSorted_expression"):
                listener.exitSorted_expression(self)




    def sorted_expression(self):

        localctx = MParser.Sorted_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_sorted_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1347
            self.match(MParser.SORTED)
            self.state = 1349
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.DESC:
                self.state = 1348
                self.match(MParser.DESC)


            self.state = 1351
            self.match(MParser.LPAR)
            self.state = 1352
            localctx.source = self.instance_expression(0)
            self.state = 1358
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.COMMA:
                self.state = 1353
                self.match(MParser.COMMA)
                self.state = 1354
                self.key_token()
                self.state = 1355
                self.match(MParser.EQ)
                self.state = 1356
                localctx.key = self.instance_expression(0)


            self.state = 1360
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_instance_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Assign_instance_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.inst = None # Assignable_instanceContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(MParser.AssignContext,0)


        def assignable_instance(self):
            return self.getTypedRuleContext(MParser.Assignable_instanceContext,0)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_assign_instance_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterAssign_instance_statement"):
                listener.enterAssign_instance_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign_instance_statement"):
                listener.exitAssign_instance_statement(self)




    def assign_instance_statement(self):

        localctx = MParser.Assign_instance_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_assign_instance_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1362
            localctx.inst = self.assignable_instance(0)
            self.state = 1363
            self.assign()
            self.state = 1364
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Child_instanceContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Child_instanceContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_child_instance

     
        def copyFrom(self, ctx):
            super(MParser.Child_instanceContext, self).copyFrom(ctx)



    class MemberInstanceContext(Child_instanceContext):

        def __init__(self, parser, ctx): # actually a MParser.Child_instanceContext)
            super(MParser.MemberInstanceContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMemberInstance"):
                listener.enterMemberInstance(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMemberInstance"):
                listener.exitMemberInstance(self)


    class ItemInstanceContext(Child_instanceContext):

        def __init__(self, parser, ctx): # actually a MParser.Child_instanceContext)
            super(MParser.ItemInstanceContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterItemInstance"):
                listener.enterItemInstance(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitItemInstance"):
                listener.exitItemInstance(self)



    def child_instance(self):

        localctx = MParser.Child_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_child_instance)
        try:
            self.state = 1374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,74,self._ctx)
            if la_ == 1:
                localctx = MParser.MemberInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1366
                if not self.wasNot(MParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(MParser.WS)")
                self.state = 1367
                self.match(MParser.DOT)
                self.state = 1368
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = MParser.ItemInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1369
                if not self.wasNot(MParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(MParser.WS)")
                self.state = 1370
                self.match(MParser.LBRAK)
                self.state = 1371
                localctx.exp = self.expression(0)
                self.state = 1372
                self.match(MParser.RBRAK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_tuple_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Assign_tuple_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Variable_identifier_listContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(MParser.AssignContext,0)


        def variable_identifier_list(self):
            return self.getTypedRuleContext(MParser.Variable_identifier_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_assign_tuple_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterAssign_tuple_statement"):
                listener.enterAssign_tuple_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign_tuple_statement"):
                listener.exitAssign_tuple_statement(self)




    def assign_tuple_statement(self):

        localctx = MParser.Assign_tuple_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_assign_tuple_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1376
            localctx.items = self.variable_identifier_list()
            self.state = 1377
            self.assign()
            self.state = 1378
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LfsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.LfsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LF(self, i=None):
            if i is None:
                return self.getTokens(MParser.LF)
            else:
                return self.getToken(MParser.LF, i)

        def getRuleIndex(self):
            return MParser.RULE_lfs

        def enterRule(self, listener):
            if hasattr(listener, "enterLfs"):
                listener.enterLfs(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLfs"):
                listener.exitLfs(self)




    def lfs(self):

        localctx = MParser.LfsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_lfs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1383
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,75,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1380
                    self.match(MParser.LF) 
                self.state = 1385
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,75,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LfpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.LfpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LF(self, i=None):
            if i is None:
                return self.getTokens(MParser.LF)
            else:
                return self.getToken(MParser.LF, i)

        def getRuleIndex(self):
            return MParser.RULE_lfp

        def enterRule(self, listener):
            if hasattr(listener, "enterLfp"):
                listener.enterLfp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLfp"):
                listener.exitLfp(self)




    def lfp(self):

        localctx = MParser.LfpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_lfp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1387 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1386
                self.match(MParser.LF)
                self.state = 1389 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MParser.LF):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IndentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.IndentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(MParser.INDENT, 0)

        def LF(self, i=None):
            if i is None:
                return self.getTokens(MParser.LF)
            else:
                return self.getToken(MParser.LF, i)

        def getRuleIndex(self):
            return MParser.RULE_indent

        def enterRule(self, listener):
            if hasattr(listener, "enterIndent"):
                listener.enterIndent(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIndent"):
                listener.exitIndent(self)




    def indent(self):

        localctx = MParser.IndentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_indent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1392 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1391
                self.match(MParser.LF)
                self.state = 1394 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MParser.LF):
                    break

            self.state = 1396
            self.match(MParser.INDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DedentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.DedentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DEDENT(self):
            return self.getToken(MParser.DEDENT, 0)

        def LF(self, i=None):
            if i is None:
                return self.getTokens(MParser.LF)
            else:
                return self.getToken(MParser.LF, i)

        def getRuleIndex(self):
            return MParser.RULE_dedent

        def enterRule(self, listener):
            if hasattr(listener, "enterDedent"):
                listener.enterDedent(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDedent"):
                listener.exitDedent(self)




    def dedent(self):

        localctx = MParser.DedentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_dedent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1401
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.LF:
                self.state = 1398
                self.match(MParser.LF)
                self.state = 1403
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1404
            self.match(MParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Null_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Null_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NONE(self):
            return self.getToken(MParser.NONE, 0)

        def getRuleIndex(self):
            return MParser.RULE_null_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterNull_literal"):
                listener.enterNull_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNull_literal"):
                listener.exitNull_literal(self)




    def null_literal(self):

        localctx = MParser.Null_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1406
            self.match(MParser.NONE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_declaration_list

     
        def copyFrom(self, ctx):
            super(MParser.Declaration_listContext, self).copyFrom(ctx)



    class FullDeclarationListContext(Declaration_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Declaration_listContext)
            super(MParser.FullDeclarationListContext, self).__init__(parser)
            self.copyFrom(ctx)

        def lfs(self):
            return self.getTypedRuleContext(MParser.LfsContext,0)

        def EOF(self):
            return self.getToken(MParser.EOF, 0)
        def declarations(self):
            return self.getTypedRuleContext(MParser.DeclarationsContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterFullDeclarationList"):
                listener.enterFullDeclarationList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFullDeclarationList"):
                listener.exitFullDeclarationList(self)



    def declaration_list(self):

        localctx = MParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            localctx = MParser.FullDeclarationListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 1409
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.COMMENT or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (MParser.ABSTRACT - 69)) | (1 << (MParser.ATTR - 69)) | (1 << (MParser.CATEGORY - 69)) | (1 << (MParser.CLASS - 69)) | (1 << (MParser.DEF - 69)) | (1 << (MParser.ENUM - 69)) | (1 << (MParser.NATIVE - 69)))) != 0) or ((((_la - 143)) & ~0x3f) == 0 and ((1 << (_la - 143)) & ((1 << (MParser.SINGLETON - 143)) | (1 << (MParser.STORABLE - 143)) | (1 << (MParser.WIDGET - 143)))) != 0):
                self.state = 1408
                self.declarations()


            self.state = 1411
            self.lfs()
            self.state = 1412
            self.match(MParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.DeclarationsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(MParser.DeclarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def getRuleIndex(self):
            return MParser.RULE_declarations

        def enterRule(self, listener):
            if hasattr(listener, "enterDeclarations"):
                listener.enterDeclarations(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDeclarations"):
                listener.exitDeclarations(self)




    def declarations(self):

        localctx = MParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_declarations)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1414
            self.declaration()
            self.state = 1420
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,80,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1415
                    self.lfp()
                    self.state = 1416
                    self.declaration() 
                self.state = 1422
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,80,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.DeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def attribute_declaration(self):
            return self.getTypedRuleContext(MParser.Attribute_declarationContext,0)


        def category_declaration(self):
            return self.getTypedRuleContext(MParser.Category_declarationContext,0)


        def resource_declaration(self):
            return self.getTypedRuleContext(MParser.Resource_declarationContext,0)


        def enum_declaration(self):
            return self.getTypedRuleContext(MParser.Enum_declarationContext,0)


        def widget_declaration(self):
            return self.getTypedRuleContext(MParser.Widget_declarationContext,0)


        def method_declaration(self):
            return self.getTypedRuleContext(MParser.Method_declarationContext,0)


        def comment_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Comment_statementContext)
            else:
                return self.getTypedRuleContext(MParser.Comment_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def getRuleIndex(self):
            return MParser.RULE_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterDeclaration"):
                listener.enterDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDeclaration"):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = MParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1428
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMENT:
                self.state = 1423
                self.comment_statement()
                self.state = 1424
                self.lfp()
                self.state = 1430
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1437
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                self.state = 1431
                self.attribute_declaration()
                pass

            elif la_ == 2:
                self.state = 1432
                self.category_declaration()
                pass

            elif la_ == 3:
                self.state = 1433
                self.resource_declaration()
                pass

            elif la_ == 4:
                self.state = 1434
                self.enum_declaration()
                pass

            elif la_ == 5:
                self.state = 1435
                self.widget_declaration()
                pass

            elif la_ == 6:
                self.state = 1436
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
            super(MParser.Resource_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_resource_declaration(self):
            return self.getTypedRuleContext(MParser.Native_resource_declarationContext,0)


        def getRuleIndex(self):
            return MParser.RULE_resource_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterResource_declaration"):
                listener.enterResource_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitResource_declaration"):
                listener.exitResource_declaration(self)




    def resource_declaration(self):

        localctx = MParser.Resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1439
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
            super(MParser.Enum_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def enum_category_declaration(self):
            return self.getTypedRuleContext(MParser.Enum_category_declarationContext,0)


        def enum_native_declaration(self):
            return self.getTypedRuleContext(MParser.Enum_native_declarationContext,0)


        def getRuleIndex(self):
            return MParser.RULE_enum_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterEnum_declaration"):
                listener.enterEnum_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEnum_declaration"):
                listener.exitEnum_declaration(self)




    def enum_declaration(self):

        localctx = MParser.Enum_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_enum_declaration)
        try:
            self.state = 1443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,83,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1441
                self.enum_category_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1442
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
            super(MParser.Native_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_symbol(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Native_symbolContext)
            else:
                return self.getTypedRuleContext(MParser.Native_symbolContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def getRuleIndex(self):
            return MParser.RULE_native_symbol_list

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_symbol_list"):
                listener.enterNative_symbol_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_symbol_list"):
                listener.exitNative_symbol_list(self)




    def native_symbol_list(self):

        localctx = MParser.Native_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_native_symbol_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1445
            self.native_symbol()
            self.state = 1451
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,84,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1446
                    self.lfp()
                    self.state = 1447
                    self.native_symbol() 
                self.state = 1453
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,84,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Category_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def category_symbol(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Category_symbolContext)
            else:
                return self.getTypedRuleContext(MParser.Category_symbolContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def getRuleIndex(self):
            return MParser.RULE_category_symbol_list

        def enterRule(self, listener):
            if hasattr(listener, "enterCategory_symbol_list"):
                listener.enterCategory_symbol_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategory_symbol_list"):
                listener.exitCategory_symbol_list(self)




    def category_symbol_list(self):

        localctx = MParser.Category_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_category_symbol_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1454
            self.category_symbol()
            self.state = 1460
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,85,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1455
                    self.lfp()
                    self.state = 1456
                    self.category_symbol() 
                self.state = 1462
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,85,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def symbol_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Symbol_identifierContext)
            else:
                return self.getTypedRuleContext(MParser.Symbol_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(MParser.COMMA)
            else:
                return self.getToken(MParser.COMMA, i)

        def getRuleIndex(self):
            return MParser.RULE_symbol_list

        def enterRule(self, listener):
            if hasattr(listener, "enterSymbol_list"):
                listener.enterSymbol_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSymbol_list"):
                listener.exitSymbol_list(self)




    def symbol_list(self):

        localctx = MParser.Symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_symbol_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1463
            self.symbol_identifier()
            self.state = 1468
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMA:
                self.state = 1464
                self.match(MParser.COMMA)
                self.state = 1465
                self.symbol_identifier()
                self.state = 1470
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
            super(MParser.Attribute_constraintContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_attribute_constraint

     
        def copyFrom(self, ctx):
            super(MParser.Attribute_constraintContext, self).copyFrom(ctx)



    class MatchingSetContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a MParser.Attribute_constraintContext)
            super(MParser.MatchingSetContext, self).__init__(parser)
            self.source = None # Set_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(MParser.IN, 0)
        def set_literal(self):
            return self.getTypedRuleContext(MParser.Set_literalContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMatchingSet"):
                listener.enterMatchingSet(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingSet"):
                listener.exitMatchingSet(self)


    class MatchingPatternContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a MParser.Attribute_constraintContext)
            super(MParser.MatchingPatternContext, self).__init__(parser)
            self.text = None # Token
            self.copyFrom(ctx)

        def MATCHING(self):
            return self.getToken(MParser.MATCHING, 0)
        def TEXT_LITERAL(self):
            return self.getToken(MParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterMatchingPattern"):
                listener.enterMatchingPattern(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingPattern"):
                listener.exitMatchingPattern(self)


    class MatchingListContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a MParser.Attribute_constraintContext)
            super(MParser.MatchingListContext, self).__init__(parser)
            self.source = None # List_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(MParser.IN, 0)
        def list_literal(self):
            return self.getTypedRuleContext(MParser.List_literalContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMatchingList"):
                listener.enterMatchingList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingList"):
                listener.exitMatchingList(self)


    class MatchingRangeContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a MParser.Attribute_constraintContext)
            super(MParser.MatchingRangeContext, self).__init__(parser)
            self.source = None # Range_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(MParser.IN, 0)
        def range_literal(self):
            return self.getTypedRuleContext(MParser.Range_literalContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMatchingRange"):
                listener.enterMatchingRange(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingRange"):
                listener.exitMatchingRange(self)


    class MatchingExpressionContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a MParser.Attribute_constraintContext)
            super(MParser.MatchingExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def MATCHING(self):
            return self.getToken(MParser.MATCHING, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterMatchingExpression"):
                listener.enterMatchingExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMatchingExpression"):
                listener.exitMatchingExpression(self)



    def attribute_constraint(self):

        localctx = MParser.Attribute_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_attribute_constraint)
        try:
            self.state = 1481
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,87,self._ctx)
            if la_ == 1:
                localctx = MParser.MatchingListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1471
                self.match(MParser.IN)
                self.state = 1472
                localctx.source = self.list_literal()
                pass

            elif la_ == 2:
                localctx = MParser.MatchingSetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1473
                self.match(MParser.IN)
                self.state = 1474
                localctx.source = self.set_literal()
                pass

            elif la_ == 3:
                localctx = MParser.MatchingRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1475
                self.match(MParser.IN)
                self.state = 1476
                localctx.source = self.range_literal()
                pass

            elif la_ == 4:
                localctx = MParser.MatchingPatternContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1477
                self.match(MParser.MATCHING)
                self.state = 1478
                localctx.text = self.match(MParser.TEXT_LITERAL)
                pass

            elif la_ == 5:
                localctx = MParser.MatchingExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1479
                self.match(MParser.MATCHING)
                self.state = 1480
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
            super(MParser.List_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)

        def MUTABLE(self):
            return self.getToken(MParser.MUTABLE, 0)

        def expression_list(self):
            return self.getTypedRuleContext(MParser.Expression_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_list_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterList_literal"):
                listener.enterList_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitList_literal"):
                listener.exitList_literal(self)




    def list_literal(self):

        localctx = MParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1484
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.MUTABLE:
                self.state = 1483
                self.match(MParser.MUTABLE)


            self.state = 1486
            self.match(MParser.LBRAK)
            self.state = 1488
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.LTGT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 100)) & ~0x3f) == 0 and ((1 << (_la - 100)) & ((1 << (MParser.EXECUTE - 100)) | (1 << (MParser.FETCH - 100)) | (1 << (MParser.MUTABLE - 100)) | (1 << (MParser.NONE - 100)) | (1 << (MParser.NOT - 100)) | (1 << (MParser.READ - 100)) | (1 << (MParser.SELF - 100)) | (1 << (MParser.SORTED - 100)) | (1 << (MParser.THIS - 100)) | (1 << (MParser.BOOLEAN_LITERAL - 100)) | (1 << (MParser.CHAR_LITERAL - 100)) | (1 << (MParser.MIN_INTEGER - 100)) | (1 << (MParser.MAX_INTEGER - 100)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (MParser.SYMBOL_IDENTIFIER - 164)) | (1 << (MParser.TYPE_IDENTIFIER - 164)) | (1 << (MParser.VARIABLE_IDENTIFIER - 164)) | (1 << (MParser.TEXT_LITERAL - 164)) | (1 << (MParser.UUID_LITERAL - 164)) | (1 << (MParser.INTEGER_LITERAL - 164)) | (1 << (MParser.HEXA_LITERAL - 164)) | (1 << (MParser.DECIMAL_LITERAL - 164)) | (1 << (MParser.DATETIME_LITERAL - 164)) | (1 << (MParser.TIME_LITERAL - 164)) | (1 << (MParser.DATE_LITERAL - 164)) | (1 << (MParser.PERIOD_LITERAL - 164)) | (1 << (MParser.VERSION_LITERAL - 164)))) != 0):
                self.state = 1487
                self.expression_list()


            self.state = 1490
            self.match(MParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Set_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Set_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(MParser.LT, 0)

        def GT(self):
            return self.getToken(MParser.GT, 0)

        def MUTABLE(self):
            return self.getToken(MParser.MUTABLE, 0)

        def expression_list(self):
            return self.getTypedRuleContext(MParser.Expression_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_set_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterSet_literal"):
                listener.enterSet_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSet_literal"):
                listener.exitSet_literal(self)




    def set_literal(self):

        localctx = MParser.Set_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_set_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1493
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.MUTABLE:
                self.state = 1492
                self.match(MParser.MUTABLE)


            self.state = 1495
            self.match(MParser.LT)
            self.state = 1497
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.LTGT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 100)) & ~0x3f) == 0 and ((1 << (_la - 100)) & ((1 << (MParser.EXECUTE - 100)) | (1 << (MParser.FETCH - 100)) | (1 << (MParser.MUTABLE - 100)) | (1 << (MParser.NONE - 100)) | (1 << (MParser.NOT - 100)) | (1 << (MParser.READ - 100)) | (1 << (MParser.SELF - 100)) | (1 << (MParser.SORTED - 100)) | (1 << (MParser.THIS - 100)) | (1 << (MParser.BOOLEAN_LITERAL - 100)) | (1 << (MParser.CHAR_LITERAL - 100)) | (1 << (MParser.MIN_INTEGER - 100)) | (1 << (MParser.MAX_INTEGER - 100)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (MParser.SYMBOL_IDENTIFIER - 164)) | (1 << (MParser.TYPE_IDENTIFIER - 164)) | (1 << (MParser.VARIABLE_IDENTIFIER - 164)) | (1 << (MParser.TEXT_LITERAL - 164)) | (1 << (MParser.UUID_LITERAL - 164)) | (1 << (MParser.INTEGER_LITERAL - 164)) | (1 << (MParser.HEXA_LITERAL - 164)) | (1 << (MParser.DECIMAL_LITERAL - 164)) | (1 << (MParser.DATETIME_LITERAL - 164)) | (1 << (MParser.TIME_LITERAL - 164)) | (1 << (MParser.DATE_LITERAL - 164)) | (1 << (MParser.PERIOD_LITERAL - 164)) | (1 << (MParser.VERSION_LITERAL - 164)))) != 0):
                self.state = 1496
                self.expression_list()


            self.state = 1499
            self.match(MParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Expression_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(MParser.COMMA)
            else:
                return self.getToken(MParser.COMMA, i)

        def getRuleIndex(self):
            return MParser.RULE_expression_list

        def enterRule(self, listener):
            if hasattr(listener, "enterExpression_list"):
                listener.enterExpression_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExpression_list"):
                listener.exitExpression_list(self)




    def expression_list(self):

        localctx = MParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1501
            self.expression(0)
            self.state = 1506
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMA:
                self.state = 1502
                self.match(MParser.COMMA)
                self.state = 1503
                self.expression(0)
                self.state = 1508
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
            super(MParser.Range_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.low = None # ExpressionContext
            self.high = None # ExpressionContext

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)

        def RANGE(self):
            return self.getToken(MParser.RANGE, 0)

        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MParser.RULE_range_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterRange_literal"):
                listener.enterRange_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRange_literal"):
                listener.exitRange_literal(self)




    def range_literal(self):

        localctx = MParser.Range_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_range_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1509
            self.match(MParser.LBRAK)
            self.state = 1510
            localctx.low = self.expression(0)
            self.state = 1511
            self.match(MParser.RANGE)
            self.state = 1512
            localctx.high = self.expression(0)
            self.state = 1513
            self.match(MParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypedefContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.TypedefContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_typedef

     
        def copyFrom(self, ctx):
            super(MParser.TypedefContext, self).copyFrom(ctx)


    class IteratorTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a MParser.TypedefContext)
            super(MParser.IteratorTypeContext, self).__init__(parser)
            self.i = None # TypedefContext
            self.copyFrom(ctx)

        def ITERATOR(self):
            return self.getToken(MParser.ITERATOR, 0)
        def LT(self):
            return self.getToken(MParser.LT, 0)
        def GT(self):
            return self.getToken(MParser.GT, 0)
        def typedef(self):
            return self.getTypedRuleContext(MParser.TypedefContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIteratorType"):
                listener.enterIteratorType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIteratorType"):
                listener.exitIteratorType(self)


    class SetTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a MParser.TypedefContext)
            super(MParser.SetTypeContext, self).__init__(parser)
            self.s = None # TypedefContext
            self.copyFrom(ctx)

        def LTGT(self):
            return self.getToken(MParser.LTGT, 0)
        def typedef(self):
            return self.getTypedRuleContext(MParser.TypedefContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSetType"):
                listener.enterSetType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSetType"):
                listener.exitSetType(self)


    class ListTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a MParser.TypedefContext)
            super(MParser.ListTypeContext, self).__init__(parser)
            self.l = None # TypedefContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)
        def typedef(self):
            return self.getTypedRuleContext(MParser.TypedefContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterListType"):
                listener.enterListType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitListType"):
                listener.exitListType(self)


    class DictTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a MParser.TypedefContext)
            super(MParser.DictTypeContext, self).__init__(parser)
            self.d = None # TypedefContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(MParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(MParser.RCURL, 0)
        def typedef(self):
            return self.getTypedRuleContext(MParser.TypedefContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterDictType"):
                listener.enterDictType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDictType"):
                listener.exitDictType(self)


    class CursorTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a MParser.TypedefContext)
            super(MParser.CursorTypeContext, self).__init__(parser)
            self.c = None # TypedefContext
            self.copyFrom(ctx)

        def CURSOR(self):
            return self.getToken(MParser.CURSOR, 0)
        def LT(self):
            return self.getToken(MParser.LT, 0)
        def GT(self):
            return self.getToken(MParser.GT, 0)
        def typedef(self):
            return self.getTypedRuleContext(MParser.TypedefContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCursorType"):
                listener.enterCursorType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCursorType"):
                listener.exitCursorType(self)


    class PrimaryTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a MParser.TypedefContext)
            super(MParser.PrimaryTypeContext, self).__init__(parser)
            self.p = None # Primary_typeContext
            self.copyFrom(ctx)

        def primary_type(self):
            return self.getTypedRuleContext(MParser.Primary_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPrimaryType"):
                listener.enterPrimaryType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPrimaryType"):
                listener.exitPrimaryType(self)



    def typedef(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.TypedefContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 166
        self.enterRecursionRule(localctx, 166, self.RULE_typedef, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1527
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.VERSION, MParser.CODE, MParser.DOCUMENT, MParser.BLOB, MParser.IMAGE, MParser.UUID, MParser.HTML, MParser.TYPE_IDENTIFIER]:
                localctx = MParser.PrimaryTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1516
                localctx.p = self.primary_type()
                pass
            elif token in [MParser.CURSOR]:
                localctx = MParser.CursorTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1517
                self.match(MParser.CURSOR)
                self.state = 1518
                self.match(MParser.LT)
                self.state = 1519
                localctx.c = self.typedef(0)
                self.state = 1520
                self.match(MParser.GT)
                pass
            elif token in [MParser.ITERATOR]:
                localctx = MParser.IteratorTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1522
                self.match(MParser.ITERATOR)
                self.state = 1523
                self.match(MParser.LT)
                self.state = 1524
                localctx.i = self.typedef(0)
                self.state = 1525
                self.match(MParser.GT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 1539
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,95,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1537
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,94,self._ctx)
                    if la_ == 1:
                        localctx = MParser.SetTypeContext(self, MParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.s = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1529
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 1530
                        self.match(MParser.LTGT)
                        pass

                    elif la_ == 2:
                        localctx = MParser.ListTypeContext(self, MParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1531
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 1532
                        self.match(MParser.LBRAK)
                        self.state = 1533
                        self.match(MParser.RBRAK)
                        pass

                    elif la_ == 3:
                        localctx = MParser.DictTypeContext(self, MParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.d = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1534
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1535
                        self.match(MParser.LCURL)
                        self.state = 1536
                        self.match(MParser.RCURL)
                        pass

             
                self.state = 1541
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,95,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Primary_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Primary_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_primary_type

     
        def copyFrom(self, ctx):
            super(MParser.Primary_typeContext, self).copyFrom(ctx)



    class NativeTypeContext(Primary_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Primary_typeContext)
            super(MParser.NativeTypeContext, self).__init__(parser)
            self.n = None # Native_typeContext
            self.copyFrom(ctx)

        def native_type(self):
            return self.getTypedRuleContext(MParser.Native_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNativeType"):
                listener.enterNativeType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNativeType"):
                listener.exitNativeType(self)


    class CategoryTypeContext(Primary_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Primary_typeContext)
            super(MParser.CategoryTypeContext, self).__init__(parser)
            self.c = None # Category_typeContext
            self.copyFrom(ctx)

        def category_type(self):
            return self.getTypedRuleContext(MParser.Category_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCategoryType"):
                listener.enterCategoryType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategoryType"):
                listener.exitCategoryType(self)



    def primary_type(self):

        localctx = MParser.Primary_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_primary_type)
        try:
            self.state = 1544
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.VERSION, MParser.CODE, MParser.DOCUMENT, MParser.BLOB, MParser.IMAGE, MParser.UUID, MParser.HTML]:
                localctx = MParser.NativeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1542
                localctx.n = self.native_type()
                pass
            elif token in [MParser.TYPE_IDENTIFIER]:
                localctx = MParser.CategoryTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1543
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
            super(MParser.Native_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_native_type

     
        def copyFrom(self, ctx):
            super(MParser.Native_typeContext, self).copyFrom(ctx)



    class PeriodTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.PeriodTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PERIOD(self):
            return self.getToken(MParser.PERIOD, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPeriodType"):
                listener.enterPeriodType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPeriodType"):
                listener.exitPeriodType(self)


    class HtmlTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.HtmlTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def HTML(self):
            return self.getToken(MParser.HTML, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterHtmlType"):
                listener.enterHtmlType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHtmlType"):
                listener.exitHtmlType(self)


    class BooleanTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.BooleanTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(MParser.BOOLEAN, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterBooleanType"):
                listener.enterBooleanType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBooleanType"):
                listener.exitBooleanType(self)


    class DocumentTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.DocumentTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOCUMENT(self):
            return self.getToken(MParser.DOCUMENT, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDocumentType"):
                listener.enterDocumentType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDocumentType"):
                listener.exitDocumentType(self)


    class CharacterTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.CharacterTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHARACTER(self):
            return self.getToken(MParser.CHARACTER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCharacterType"):
                listener.enterCharacterType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCharacterType"):
                listener.exitCharacterType(self)


    class VersionTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.VersionTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def VERSION(self):
            return self.getToken(MParser.VERSION, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterVersionType"):
                listener.enterVersionType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVersionType"):
                listener.exitVersionType(self)


    class TextTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.TextTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT(self):
            return self.getToken(MParser.TEXT, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterTextType"):
                listener.enterTextType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTextType"):
                listener.exitTextType(self)


    class ImageTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.ImageTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def IMAGE(self):
            return self.getToken(MParser.IMAGE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterImageType"):
                listener.enterImageType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitImageType"):
                listener.exitImageType(self)


    class TimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.TimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TIME(self):
            return self.getToken(MParser.TIME, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterTimeType"):
                listener.enterTimeType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTimeType"):
                listener.exitTimeType(self)


    class IntegerTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.IntegerTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(MParser.INTEGER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterIntegerType"):
                listener.enterIntegerType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIntegerType"):
                listener.exitIntegerType(self)


    class DateTimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.DateTimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATETIME(self):
            return self.getToken(MParser.DATETIME, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDateTimeType"):
                listener.enterDateTimeType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDateTimeType"):
                listener.exitDateTimeType(self)


    class BlobTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.BlobTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BLOB(self):
            return self.getToken(MParser.BLOB, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterBlobType"):
                listener.enterBlobType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBlobType"):
                listener.exitBlobType(self)


    class UUIDTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.UUIDTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def UUID(self):
            return self.getToken(MParser.UUID, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterUUIDType"):
                listener.enterUUIDType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitUUIDType"):
                listener.exitUUIDType(self)


    class DecimalTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.DecimalTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL(self):
            return self.getToken(MParser.DECIMAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDecimalType"):
                listener.enterDecimalType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDecimalType"):
                listener.exitDecimalType(self)


    class CodeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.CodeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(MParser.CODE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCodeType"):
                listener.enterCodeType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCodeType"):
                listener.exitCodeType(self)


    class DateTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.DateTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATE(self):
            return self.getToken(MParser.DATE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDateType"):
                listener.enterDateType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDateType"):
                listener.exitDateType(self)



    def native_type(self):

        localctx = MParser.Native_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_native_type)
        try:
            self.state = 1562
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.BOOLEAN]:
                localctx = MParser.BooleanTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1546
                self.match(MParser.BOOLEAN)
                pass
            elif token in [MParser.CHARACTER]:
                localctx = MParser.CharacterTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1547
                self.match(MParser.CHARACTER)
                pass
            elif token in [MParser.TEXT]:
                localctx = MParser.TextTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1548
                self.match(MParser.TEXT)
                pass
            elif token in [MParser.IMAGE]:
                localctx = MParser.ImageTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1549
                self.match(MParser.IMAGE)
                pass
            elif token in [MParser.INTEGER]:
                localctx = MParser.IntegerTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1550
                self.match(MParser.INTEGER)
                pass
            elif token in [MParser.DECIMAL]:
                localctx = MParser.DecimalTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1551
                self.match(MParser.DECIMAL)
                pass
            elif token in [MParser.DOCUMENT]:
                localctx = MParser.DocumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1552
                self.match(MParser.DOCUMENT)
                pass
            elif token in [MParser.DATE]:
                localctx = MParser.DateTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1553
                self.match(MParser.DATE)
                pass
            elif token in [MParser.DATETIME]:
                localctx = MParser.DateTimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1554
                self.match(MParser.DATETIME)
                pass
            elif token in [MParser.TIME]:
                localctx = MParser.TimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1555
                self.match(MParser.TIME)
                pass
            elif token in [MParser.PERIOD]:
                localctx = MParser.PeriodTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1556
                self.match(MParser.PERIOD)
                pass
            elif token in [MParser.VERSION]:
                localctx = MParser.VersionTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1557
                self.match(MParser.VERSION)
                pass
            elif token in [MParser.CODE]:
                localctx = MParser.CodeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1558
                self.match(MParser.CODE)
                pass
            elif token in [MParser.BLOB]:
                localctx = MParser.BlobTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1559
                self.match(MParser.BLOB)
                pass
            elif token in [MParser.UUID]:
                localctx = MParser.UUIDTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 1560
                self.match(MParser.UUID)
                pass
            elif token in [MParser.HTML]:
                localctx = MParser.HtmlTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 1561
                self.match(MParser.HTML)
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
            super(MParser.Category_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def TYPE_IDENTIFIER(self):
            return self.getToken(MParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MParser.RULE_category_type

        def enterRule(self, listener):
            if hasattr(listener, "enterCategory_type"):
                listener.enterCategory_type(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategory_type"):
                listener.exitCategory_type(self)




    def category_type(self):

        localctx = MParser.Category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_category_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1564
            localctx.t1 = self.match(MParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Mutable_category_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Mutable_category_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def category_type(self):
            return self.getTypedRuleContext(MParser.Category_typeContext,0)


        def MUTABLE(self):
            return self.getToken(MParser.MUTABLE, 0)

        def getRuleIndex(self):
            return MParser.RULE_mutable_category_type

        def enterRule(self, listener):
            if hasattr(listener, "enterMutable_category_type"):
                listener.enterMutable_category_type(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMutable_category_type"):
                listener.exitMutable_category_type(self)




    def mutable_category_type(self):

        localctx = MParser.Mutable_category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_mutable_category_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1567
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.MUTABLE:
                self.state = 1566
                self.match(MParser.MUTABLE)


            self.state = 1569
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
            super(MParser.Code_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def CODE(self):
            return self.getToken(MParser.CODE, 0)

        def getRuleIndex(self):
            return MParser.RULE_code_type

        def enterRule(self, listener):
            if hasattr(listener, "enterCode_type"):
                listener.enterCode_type(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCode_type"):
                listener.exitCode_type(self)




    def code_type(self):

        localctx = MParser.Code_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_code_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1571
            localctx.t1 = self.match(MParser.CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_category_declaration

     
        def copyFrom(self, ctx):
            super(MParser.Category_declarationContext, self).copyFrom(ctx)



    class ConcreteCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a MParser.Category_declarationContext)
            super(MParser.ConcreteCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Concrete_category_declarationContext
            self.copyFrom(ctx)

        def concrete_category_declaration(self):
            return self.getTypedRuleContext(MParser.Concrete_category_declarationContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterConcreteCategoryDeclaration"):
                listener.enterConcreteCategoryDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConcreteCategoryDeclaration"):
                listener.exitConcreteCategoryDeclaration(self)


    class NativeCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a MParser.Category_declarationContext)
            super(MParser.NativeCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Native_category_declarationContext
            self.copyFrom(ctx)

        def native_category_declaration(self):
            return self.getTypedRuleContext(MParser.Native_category_declarationContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNativeCategoryDeclaration"):
                listener.enterNativeCategoryDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNativeCategoryDeclaration"):
                listener.exitNativeCategoryDeclaration(self)


    class SingletonCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a MParser.Category_declarationContext)
            super(MParser.SingletonCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Singleton_category_declarationContext
            self.copyFrom(ctx)

        def singleton_category_declaration(self):
            return self.getTypedRuleContext(MParser.Singleton_category_declarationContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSingletonCategoryDeclaration"):
                listener.enterSingletonCategoryDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSingletonCategoryDeclaration"):
                listener.exitSingletonCategoryDeclaration(self)



    def category_declaration(self):

        localctx = MParser.Category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_category_declaration)
        try:
            self.state = 1576
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,99,self._ctx)
            if la_ == 1:
                localctx = MParser.ConcreteCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1573
                localctx.decl = self.concrete_category_declaration()
                pass

            elif la_ == 2:
                localctx = MParser.NativeCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1574
                localctx.decl = self.native_category_declaration()
                pass

            elif la_ == 3:
                localctx = MParser.SingletonCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1575
                localctx.decl = self.singleton_category_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Widget_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Widget_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_widget_declaration

     
        def copyFrom(self, ctx):
            super(MParser.Widget_declarationContext, self).copyFrom(ctx)



    class ConcreteWidgetDeclarationContext(Widget_declarationContext):

        def __init__(self, parser, ctx): # actually a MParser.Widget_declarationContext)
            super(MParser.ConcreteWidgetDeclarationContext, self).__init__(parser)
            self.decl = None # Concrete_widget_declarationContext
            self.copyFrom(ctx)

        def concrete_widget_declaration(self):
            return self.getTypedRuleContext(MParser.Concrete_widget_declarationContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterConcreteWidgetDeclaration"):
                listener.enterConcreteWidgetDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConcreteWidgetDeclaration"):
                listener.exitConcreteWidgetDeclaration(self)


    class NativeWidgetDeclarationContext(Widget_declarationContext):

        def __init__(self, parser, ctx): # actually a MParser.Widget_declarationContext)
            super(MParser.NativeWidgetDeclarationContext, self).__init__(parser)
            self.decl = None # Native_widget_declarationContext
            self.copyFrom(ctx)

        def native_widget_declaration(self):
            return self.getTypedRuleContext(MParser.Native_widget_declarationContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNativeWidgetDeclaration"):
                listener.enterNativeWidgetDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNativeWidgetDeclaration"):
                listener.exitNativeWidgetDeclaration(self)



    def widget_declaration(self):

        localctx = MParser.Widget_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_widget_declaration)
        try:
            self.state = 1580
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.WIDGET]:
                localctx = MParser.ConcreteWidgetDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1578
                localctx.decl = self.concrete_widget_declaration()
                pass
            elif token in [MParser.NATIVE]:
                localctx = MParser.NativeWidgetDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1579
                localctx.decl = self.native_widget_declaration()
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

    class Type_identifier_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Type_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def type_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Type_identifierContext)
            else:
                return self.getTypedRuleContext(MParser.Type_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(MParser.COMMA)
            else:
                return self.getToken(MParser.COMMA, i)

        def getRuleIndex(self):
            return MParser.RULE_type_identifier_list

        def enterRule(self, listener):
            if hasattr(listener, "enterType_identifier_list"):
                listener.enterType_identifier_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitType_identifier_list"):
                listener.exitType_identifier_list(self)




    def type_identifier_list(self):

        localctx = MParser.Type_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_type_identifier_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1582
            self.type_identifier()
            self.state = 1587
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,101,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1583
                    self.match(MParser.COMMA)
                    self.state = 1584
                    self.type_identifier() 
                self.state = 1589
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,101,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Method_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(MParser.Type_identifierContext,0)


        def getRuleIndex(self):
            return MParser.RULE_method_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterMethod_identifier"):
                listener.enterMethod_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethod_identifier"):
                listener.exitMethod_identifier(self)




    def method_identifier(self):

        localctx = MParser.Method_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_method_identifier)
        try:
            self.state = 1592
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.VARIABLE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1590
                self.variable_identifier()
                pass
            elif token in [MParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1591
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

    class Identifier_or_keywordContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Identifier_or_keywordContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MParser.IdentifierContext,0)


        def keyword(self):
            return self.getTypedRuleContext(MParser.KeywordContext,0)


        def getRuleIndex(self):
            return MParser.RULE_identifier_or_keyword

        def enterRule(self, listener):
            if hasattr(listener, "enterIdentifier_or_keyword"):
                listener.enterIdentifier_or_keyword(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIdentifier_or_keyword"):
                listener.exitIdentifier_or_keyword(self)




    def identifier_or_keyword(self):

        localctx = MParser.Identifier_or_keywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_identifier_or_keyword)
        try:
            self.state = 1596
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.SYMBOL_IDENTIFIER, MParser.TYPE_IDENTIFIER, MParser.VARIABLE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1594
                self.identifier()
                pass
            elif token in [MParser.JAVA, MParser.CSHARP, MParser.PYTHON2, MParser.PYTHON3, MParser.JAVASCRIPT, MParser.SWIFT, MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.VERSION, MParser.METHOD_T, MParser.CODE, MParser.DOCUMENT, MParser.BLOB, MParser.IMAGE, MParser.UUID, MParser.ITERATOR, MParser.CURSOR, MParser.HTML, MParser.ABSTRACT, MParser.ALL, MParser.ALWAYS, MParser.AND, MParser.ANY, MParser.AS, MParser.ASC, MParser.ATTR, MParser.ATTRIBUTE, MParser.ATTRIBUTES, MParser.BINDINGS, MParser.BREAK, MParser.BY, MParser.CASE, MParser.CATCH, MParser.CATEGORY, MParser.CLASS, MParser.CLOSE, MParser.CONTAINS, MParser.DEF, MParser.DEFAULT, MParser.DEFINE, MParser.DELETE, MParser.DESC, MParser.DO, MParser.DOING, MParser.EACH, MParser.ELSE, MParser.ENUM, MParser.ENUMERATED, MParser.EXCEPT, MParser.EXECUTE, MParser.EXPECTING, MParser.EXTENDS, MParser.FETCH, MParser.FILTERED, MParser.FINALLY, MParser.FLUSH, MParser.FOR, MParser.FROM, MParser.GETTER, MParser.HAS, MParser.IF, MParser.IN, MParser.INDEX, MParser.INVOKE, MParser.IS, MParser.MATCHING, MParser.METHOD, MParser.METHODS, MParser.MODULO, MParser.MUTABLE, MParser.NATIVE, MParser.NONE, MParser.NOT, MParser.NOTHING, MParser.NULL, MParser.ON, MParser.ONE, MParser.OPEN, MParser.OPERATOR, MParser.OR, MParser.ORDER, MParser.OTHERWISE, MParser.PASS, MParser.RAISE, MParser.READ, MParser.RECEIVING, MParser.RESOURCE, MParser.RETURN, MParser.RETURNING, MParser.ROWS, MParser.SELF, MParser.SETTER, MParser.SINGLETON, MParser.SORTED, MParser.STORABLE, MParser.STORE, MParser.SWITCH, MParser.TEST, MParser.THIS, MParser.THROW, MParser.TO, MParser.TRY, MParser.VERIFYING, MParser.WIDGET, MParser.WITH, MParser.WHEN, MParser.WHERE, MParser.WHILE, MParser.WRITE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1595
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

    class Nospace_hyphen_identifier_or_keywordContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Nospace_hyphen_identifier_or_keywordContext, self).__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(MParser.MINUS, 0)

        def nospace_identifier_or_keyword(self):
            return self.getTypedRuleContext(MParser.Nospace_identifier_or_keywordContext,0)


        def getRuleIndex(self):
            return MParser.RULE_nospace_hyphen_identifier_or_keyword

        def enterRule(self, listener):
            if hasattr(listener, "enterNospace_hyphen_identifier_or_keyword"):
                listener.enterNospace_hyphen_identifier_or_keyword(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNospace_hyphen_identifier_or_keyword"):
                listener.exitNospace_hyphen_identifier_or_keyword(self)




    def nospace_hyphen_identifier_or_keyword(self):

        localctx = MParser.Nospace_hyphen_identifier_or_keywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_nospace_hyphen_identifier_or_keyword)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1598
            if not self.wasNotWhiteSpace():
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.wasNotWhiteSpace()")
            self.state = 1599
            self.match(MParser.MINUS)
            self.state = 1600
            self.nospace_identifier_or_keyword()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Nospace_identifier_or_keywordContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Nospace_identifier_or_keywordContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier_or_keyword(self):
            return self.getTypedRuleContext(MParser.Identifier_or_keywordContext,0)


        def getRuleIndex(self):
            return MParser.RULE_nospace_identifier_or_keyword

        def enterRule(self, listener):
            if hasattr(listener, "enterNospace_identifier_or_keyword"):
                listener.enterNospace_identifier_or_keyword(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNospace_identifier_or_keyword"):
                listener.exitNospace_identifier_or_keyword(self)




    def nospace_identifier_or_keyword(self):

        localctx = MParser.Nospace_identifier_or_keywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_nospace_identifier_or_keyword)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1602
            if not self.wasNotWhiteSpace():
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.wasNotWhiteSpace()")
            self.state = 1603
            self.identifier_or_keyword()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.IdentifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_identifier

     
        def copyFrom(self, ctx):
            super(MParser.IdentifierContext, self).copyFrom(ctx)



    class TypeIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a MParser.IdentifierContext)
            super(MParser.TypeIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(MParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterTypeIdentifier"):
                listener.enterTypeIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTypeIdentifier"):
                listener.exitTypeIdentifier(self)


    class SymbolIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a MParser.IdentifierContext)
            super(MParser.SymbolIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def symbol_identifier(self):
            return self.getTypedRuleContext(MParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSymbolIdentifier"):
                listener.enterSymbolIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSymbolIdentifier"):
                listener.exitSymbolIdentifier(self)


    class VariableIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a MParser.IdentifierContext)
            super(MParser.VariableIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterVariableIdentifier"):
                listener.enterVariableIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVariableIdentifier"):
                listener.exitVariableIdentifier(self)



    def identifier(self):

        localctx = MParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_identifier)
        try:
            self.state = 1608
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.VARIABLE_IDENTIFIER]:
                localctx = MParser.VariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1605
                self.variable_identifier()
                pass
            elif token in [MParser.TYPE_IDENTIFIER]:
                localctx = MParser.TypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1606
                self.type_identifier()
                pass
            elif token in [MParser.SYMBOL_IDENTIFIER]:
                localctx = MParser.SymbolIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1607
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
            super(MParser.Variable_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MParser.RULE_variable_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterVariable_identifier"):
                listener.enterVariable_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVariable_identifier"):
                listener.exitVariable_identifier(self)




    def variable_identifier(self):

        localctx = MParser.Variable_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_variable_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1610
            self.match(MParser.VARIABLE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Attribute_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)

        def STORABLE(self):
            return self.getToken(MParser.STORABLE, 0)

        def getRuleIndex(self):
            return MParser.RULE_attribute_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterAttribute_identifier"):
                listener.enterAttribute_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAttribute_identifier"):
                listener.exitAttribute_identifier(self)




    def attribute_identifier(self):

        localctx = MParser.Attribute_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_attribute_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1612
            _la = self._input.LA(1)
            if not(_la==MParser.STORABLE or _la==MParser.VARIABLE_IDENTIFIER):
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
            super(MParser.Type_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TYPE_IDENTIFIER(self):
            return self.getToken(MParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MParser.RULE_type_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterType_identifier"):
                listener.enterType_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitType_identifier"):
                listener.exitType_identifier(self)




    def type_identifier(self):

        localctx = MParser.Type_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_type_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1614
            self.match(MParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Symbol_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Symbol_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(MParser.SYMBOL_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MParser.RULE_symbol_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterSymbol_identifier"):
                listener.enterSymbol_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSymbol_identifier"):
                listener.exitSymbol_identifier(self)




    def symbol_identifier(self):

        localctx = MParser.Symbol_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_symbol_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1616
            self.match(MParser.SYMBOL_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(MParser.ArgumentContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(MParser.COMMA)
            else:
                return self.getToken(MParser.COMMA, i)

        def getRuleIndex(self):
            return MParser.RULE_argument_list

        def enterRule(self, listener):
            if hasattr(listener, "enterArgument_list"):
                listener.enterArgument_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArgument_list"):
                listener.exitArgument_list(self)




    def argument_list(self):

        localctx = MParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1618
            self.argument()
            self.state = 1623
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMA:
                self.state = 1619
                self.match(MParser.COMMA)
                self.state = 1620
                self.argument()
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

    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.ArgumentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_argument

     
        def copyFrom(self, ctx):
            super(MParser.ArgumentContext, self).copyFrom(ctx)



    class OperatorArgumentContext(ArgumentContext):

        def __init__(self, parser, ctx): # actually a MParser.ArgumentContext)
            super(MParser.OperatorArgumentContext, self).__init__(parser)
            self.arg = None # Operator_argumentContext
            self.copyFrom(ctx)

        def operator_argument(self):
            return self.getTypedRuleContext(MParser.Operator_argumentContext,0)

        def MUTABLE(self):
            return self.getToken(MParser.MUTABLE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorArgument"):
                listener.enterOperatorArgument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorArgument"):
                listener.exitOperatorArgument(self)


    class CodeArgumentContext(ArgumentContext):

        def __init__(self, parser, ctx): # actually a MParser.ArgumentContext)
            super(MParser.CodeArgumentContext, self).__init__(parser)
            self.arg = None # Code_argumentContext
            self.copyFrom(ctx)

        def code_argument(self):
            return self.getTypedRuleContext(MParser.Code_argumentContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCodeArgument"):
                listener.enterCodeArgument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCodeArgument"):
                listener.exitCodeArgument(self)



    def argument(self):

        localctx = MParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.state = 1631
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.CODE]:
                localctx = MParser.CodeArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1626
                localctx.arg = self.code_argument()
                pass
            elif token in [MParser.MUTABLE, MParser.VARIABLE_IDENTIFIER]:
                localctx = MParser.OperatorArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1628
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MParser.MUTABLE:
                    self.state = 1627
                    self.match(MParser.MUTABLE)


                self.state = 1630
                localctx.arg = self.operator_argument()
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

    class Operator_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Operator_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def named_argument(self):
            return self.getTypedRuleContext(MParser.Named_argumentContext,0)


        def typed_argument(self):
            return self.getTypedRuleContext(MParser.Typed_argumentContext,0)


        def getRuleIndex(self):
            return MParser.RULE_operator_argument

        def enterRule(self, listener):
            if hasattr(listener, "enterOperator_argument"):
                listener.enterOperator_argument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperator_argument"):
                listener.exitOperator_argument(self)




    def operator_argument(self):

        localctx = MParser.Operator_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 206, self.RULE_operator_argument)
        try:
            self.state = 1635
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,108,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1633
                self.named_argument()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1634
                self.typed_argument()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Named_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Named_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def EQ(self):
            return self.getToken(MParser.EQ, 0)

        def literal_expression(self):
            return self.getTypedRuleContext(MParser.Literal_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_named_argument

        def enterRule(self, listener):
            if hasattr(listener, "enterNamed_argument"):
                listener.enterNamed_argument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNamed_argument"):
                listener.exitNamed_argument(self)




    def named_argument(self):

        localctx = MParser.Named_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_named_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1637
            self.variable_identifier()
            self.state = 1640
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.EQ:
                self.state = 1638
                self.match(MParser.EQ)
                self.state = 1639
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
            super(MParser.Code_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext

        def code_type(self):
            return self.getTypedRuleContext(MParser.Code_typeContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def getRuleIndex(self):
            return MParser.RULE_code_argument

        def enterRule(self, listener):
            if hasattr(listener, "enterCode_argument"):
                listener.enterCode_argument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCode_argument"):
                listener.exitCode_argument(self)




    def code_argument(self):

        localctx = MParser.Code_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_code_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1642
            self.code_type()
            self.state = 1643
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
            super(MParser.Category_or_any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def typedef(self):
            return self.getTypedRuleContext(MParser.TypedefContext,0)


        def any_type(self):
            return self.getTypedRuleContext(MParser.Any_typeContext,0)


        def getRuleIndex(self):
            return MParser.RULE_category_or_any_type

        def enterRule(self, listener):
            if hasattr(listener, "enterCategory_or_any_type"):
                listener.enterCategory_or_any_type(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCategory_or_any_type"):
                listener.exitCategory_or_any_type(self)




    def category_or_any_type(self):

        localctx = MParser.Category_or_any_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_category_or_any_type)
        try:
            self.state = 1647
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.VERSION, MParser.CODE, MParser.DOCUMENT, MParser.BLOB, MParser.IMAGE, MParser.UUID, MParser.ITERATOR, MParser.CURSOR, MParser.HTML, MParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1645
                self.typedef(0)
                pass
            elif token in [MParser.ANY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1646
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
            super(MParser.Any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_any_type

     
        def copyFrom(self, ctx):
            super(MParser.Any_typeContext, self).copyFrom(ctx)


    class AnyListTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Any_typeContext)
            super(MParser.AnyListTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def any_type(self):
            return self.getTypedRuleContext(MParser.Any_typeContext,0)

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAnyListType"):
                listener.enterAnyListType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAnyListType"):
                listener.exitAnyListType(self)


    class AnyTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Any_typeContext)
            super(MParser.AnyTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ANY(self):
            return self.getToken(MParser.ANY, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAnyType"):
                listener.enterAnyType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAnyType"):
                listener.exitAnyType(self)


    class AnyDictTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Any_typeContext)
            super(MParser.AnyDictTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def any_type(self):
            return self.getTypedRuleContext(MParser.Any_typeContext,0)

        def LCURL(self):
            return self.getToken(MParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(MParser.RCURL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAnyDictType"):
                listener.enterAnyDictType(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAnyDictType"):
                listener.exitAnyDictType(self)



    def any_type(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Any_typeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 214
        self.enterRecursionRule(localctx, 214, self.RULE_any_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.AnyTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1650
            self.match(MParser.ANY)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1660
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,112,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1658
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,111,self._ctx)
                    if la_ == 1:
                        localctx = MParser.AnyListTypeContext(self, MParser.Any_typeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1652
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1653
                        self.match(MParser.LBRAK)
                        self.state = 1654
                        self.match(MParser.RBRAK)
                        pass

                    elif la_ == 2:
                        localctx = MParser.AnyDictTypeContext(self, MParser.Any_typeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1655
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1656
                        self.match(MParser.LCURL)
                        self.state = 1657
                        self.match(MParser.RCURL)
                        pass

             
                self.state = 1662
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,112,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Member_method_declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Member_method_declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def member_method_declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Member_method_declarationContext)
            else:
                return self.getTypedRuleContext(MParser.Member_method_declarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def getRuleIndex(self):
            return MParser.RULE_member_method_declaration_list

        def enterRule(self, listener):
            if hasattr(listener, "enterMember_method_declaration_list"):
                listener.enterMember_method_declaration_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMember_method_declaration_list"):
                listener.exitMember_method_declaration_list(self)




    def member_method_declaration_list(self):

        localctx = MParser.Member_method_declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_member_method_declaration_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1663
            self.member_method_declaration()
            self.state = 1669
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,113,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1664
                    self.lfp()
                    self.state = 1665
                    self.member_method_declaration() 
                self.state = 1671
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,113,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def setter_method_declaration(self):
            return self.getTypedRuleContext(MParser.Setter_method_declarationContext,0)


        def getter_method_declaration(self):
            return self.getTypedRuleContext(MParser.Getter_method_declarationContext,0)


        def concrete_method_declaration(self):
            return self.getTypedRuleContext(MParser.Concrete_method_declarationContext,0)


        def abstract_method_declaration(self):
            return self.getTypedRuleContext(MParser.Abstract_method_declarationContext,0)


        def operator_method_declaration(self):
            return self.getTypedRuleContext(MParser.Operator_method_declarationContext,0)


        def getRuleIndex(self):
            return MParser.RULE_member_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterMember_method_declaration"):
                listener.enterMember_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMember_method_declaration"):
                listener.exitMember_method_declaration(self)




    def member_method_declaration(self):

        localctx = MParser.Member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_member_method_declaration)
        try:
            self.state = 1677
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,114,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1672
                self.setter_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1673
                self.getter_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1674
                self.concrete_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1675
                self.abstract_method_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1676
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
            super(MParser.Native_member_method_declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_member_method_declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Native_member_method_declarationContext)
            else:
                return self.getTypedRuleContext(MParser.Native_member_method_declarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def getRuleIndex(self):
            return MParser.RULE_native_member_method_declaration_list

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_member_method_declaration_list"):
                listener.enterNative_member_method_declaration_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_member_method_declaration_list"):
                listener.exitNative_member_method_declaration_list(self)




    def native_member_method_declaration_list(self):

        localctx = MParser.Native_member_method_declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 220, self.RULE_native_member_method_declaration_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1679
            self.native_member_method_declaration()
            self.state = 1685
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,115,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1680
                    self.lfp()
                    self.state = 1681
                    self.native_member_method_declaration() 
                self.state = 1687
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,115,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Native_member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_getter_declaration(self):
            return self.getTypedRuleContext(MParser.Native_getter_declarationContext,0)


        def native_setter_declaration(self):
            return self.getTypedRuleContext(MParser.Native_setter_declarationContext,0)


        def native_method_declaration(self):
            return self.getTypedRuleContext(MParser.Native_method_declarationContext,0)


        def getRuleIndex(self):
            return MParser.RULE_native_member_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_member_method_declaration"):
                listener.enterNative_member_method_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_member_method_declaration"):
                listener.exitNative_member_method_declaration(self)




    def native_member_method_declaration(self):

        localctx = MParser.Native_member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 222, self.RULE_native_member_method_declaration)
        try:
            self.state = 1691
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,116,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1688
                self.native_getter_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1689
                self.native_setter_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1690
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
            super(MParser.Native_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_native_category_binding

     
        def copyFrom(self, ctx):
            super(MParser.Native_category_bindingContext, self).copyFrom(ctx)



    class Python2CategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_category_bindingContext)
            super(MParser.Python2CategoryBindingContext, self).__init__(parser)
            self.binding = None # Python_category_bindingContext
            self.copyFrom(ctx)

        def PYTHON2(self):
            return self.getToken(MParser.PYTHON2, 0)
        def python_category_binding(self):
            return self.getTypedRuleContext(MParser.Python_category_bindingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPython2CategoryBinding"):
                listener.enterPython2CategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython2CategoryBinding"):
                listener.exitPython2CategoryBinding(self)


    class Python3CategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_category_bindingContext)
            super(MParser.Python3CategoryBindingContext, self).__init__(parser)
            self.binding = None # Python_category_bindingContext
            self.copyFrom(ctx)

        def PYTHON3(self):
            return self.getToken(MParser.PYTHON3, 0)
        def python_category_binding(self):
            return self.getTypedRuleContext(MParser.Python_category_bindingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPython3CategoryBinding"):
                listener.enterPython3CategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython3CategoryBinding"):
                listener.exitPython3CategoryBinding(self)


    class JavaCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_category_bindingContext)
            super(MParser.JavaCategoryBindingContext, self).__init__(parser)
            self.binding = None # Java_class_identifier_expressionContext
            self.copyFrom(ctx)

        def JAVA(self):
            return self.getToken(MParser.JAVA, 0)
        def java_class_identifier_expression(self):
            return self.getTypedRuleContext(MParser.Java_class_identifier_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaCategoryBinding"):
                listener.enterJavaCategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaCategoryBinding"):
                listener.exitJavaCategoryBinding(self)


    class CSharpCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_category_bindingContext)
            super(MParser.CSharpCategoryBindingContext, self).__init__(parser)
            self.binding = None # Csharp_identifier_expressionContext
            self.copyFrom(ctx)

        def CSHARP(self):
            return self.getToken(MParser.CSHARP, 0)
        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_identifier_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpCategoryBinding"):
                listener.enterCSharpCategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpCategoryBinding"):
                listener.exitCSharpCategoryBinding(self)


    class JavaScriptCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_category_bindingContext)
            super(MParser.JavaScriptCategoryBindingContext, self).__init__(parser)
            self.binding = None # Javascript_category_bindingContext
            self.copyFrom(ctx)

        def JAVASCRIPT(self):
            return self.getToken(MParser.JAVASCRIPT, 0)
        def javascript_category_binding(self):
            return self.getTypedRuleContext(MParser.Javascript_category_bindingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaScriptCategoryBinding"):
                listener.enterJavaScriptCategoryBinding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptCategoryBinding"):
                listener.exitJavaScriptCategoryBinding(self)



    def native_category_binding(self):

        localctx = MParser.Native_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 224, self.RULE_native_category_binding)
        try:
            self.state = 1703
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.JAVA]:
                localctx = MParser.JavaCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1693
                self.match(MParser.JAVA)
                self.state = 1694
                localctx.binding = self.java_class_identifier_expression(0)
                pass
            elif token in [MParser.CSHARP]:
                localctx = MParser.CSharpCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1695
                self.match(MParser.CSHARP)
                self.state = 1696
                localctx.binding = self.csharp_identifier_expression(0)
                pass
            elif token in [MParser.PYTHON2]:
                localctx = MParser.Python2CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1697
                self.match(MParser.PYTHON2)
                self.state = 1698
                localctx.binding = self.python_category_binding()
                pass
            elif token in [MParser.PYTHON3]:
                localctx = MParser.Python3CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1699
                self.match(MParser.PYTHON3)
                self.state = 1700
                localctx.binding = self.python_category_binding()
                pass
            elif token in [MParser.JAVASCRIPT]:
                localctx = MParser.JavaScriptCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1701
                self.match(MParser.JAVASCRIPT)
                self.state = 1702
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
            super(MParser.Python_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MParser.IdentifierContext,0)


        def python_module(self):
            return self.getTypedRuleContext(MParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return MParser.RULE_python_category_binding

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_category_binding"):
                listener.enterPython_category_binding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_category_binding"):
                listener.exitPython_category_binding(self)




    def python_category_binding(self):

        localctx = MParser.Python_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 226, self.RULE_python_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1705
            self.identifier()
            self.state = 1707
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,118,self._ctx)
            if la_ == 1:
                self.state = 1706
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
            super(MParser.Python_moduleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(MParser.FROM, 0)

        def module_token(self):
            return self.getTypedRuleContext(MParser.Module_tokenContext,0)


        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(MParser.IdentifierContext,i)


        def DOT(self, i=None):
            if i is None:
                return self.getTokens(MParser.DOT)
            else:
                return self.getToken(MParser.DOT, i)

        def getRuleIndex(self):
            return MParser.RULE_python_module

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_module"):
                listener.enterPython_module(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_module"):
                listener.exitPython_module(self)




    def python_module(self):

        localctx = MParser.Python_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 228, self.RULE_python_module)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1709
            self.match(MParser.FROM)
            self.state = 1710
            self.module_token()
            self.state = 1711
            self.match(MParser.COLON)
            self.state = 1712
            self.identifier()
            self.state = 1717
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,119,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1713
                    self.match(MParser.DOT)
                    self.state = 1714
                    self.identifier() 
                self.state = 1719
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,119,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_category_bindingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Javascript_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MParser.IdentifierContext,0)


        def javascript_module(self):
            return self.getTypedRuleContext(MParser.Javascript_moduleContext,0)


        def getRuleIndex(self):
            return MParser.RULE_javascript_category_binding

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_category_binding"):
                listener.enterJavascript_category_binding(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_category_binding"):
                listener.exitJavascript_category_binding(self)




    def javascript_category_binding(self):

        localctx = MParser.Javascript_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 230, self.RULE_javascript_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1720
            self.identifier()
            self.state = 1722
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,120,self._ctx)
            if la_ == 1:
                self.state = 1721
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
            super(MParser.Javascript_moduleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(MParser.FROM, 0)

        def module_token(self):
            return self.getTypedRuleContext(MParser.Module_tokenContext,0)


        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def javascript_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Javascript_identifierContext)
            else:
                return self.getTypedRuleContext(MParser.Javascript_identifierContext,i)


        def SLASH(self, i=None):
            if i is None:
                return self.getTokens(MParser.SLASH)
            else:
                return self.getToken(MParser.SLASH, i)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)

        def getRuleIndex(self):
            return MParser.RULE_javascript_module

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_module"):
                listener.enterJavascript_module(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_module"):
                listener.exitJavascript_module(self)




    def javascript_module(self):

        localctx = MParser.Javascript_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_javascript_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1724
            self.match(MParser.FROM)
            self.state = 1725
            self.module_token()
            self.state = 1726
            self.match(MParser.COLON)
            self.state = 1728
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.SLASH:
                self.state = 1727
                self.match(MParser.SLASH)


            self.state = 1730
            self.javascript_identifier()
            self.state = 1735
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,122,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1731
                    self.match(MParser.SLASH)
                    self.state = 1732
                    self.javascript_identifier() 
                self.state = 1737
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,122,self._ctx)

            self.state = 1740
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,123,self._ctx)
            if la_ == 1:
                self.state = 1738
                self.match(MParser.DOT)
                self.state = 1739
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
            super(MParser.Variable_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(MParser.Variable_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(MParser.COMMA)
            else:
                return self.getToken(MParser.COMMA, i)

        def getRuleIndex(self):
            return MParser.RULE_variable_identifier_list

        def enterRule(self, listener):
            if hasattr(listener, "enterVariable_identifier_list"):
                listener.enterVariable_identifier_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVariable_identifier_list"):
                listener.exitVariable_identifier_list(self)




    def variable_identifier_list(self):

        localctx = MParser.Variable_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_variable_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1742
            self.variable_identifier()
            self.state = 1747
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMA:
                self.state = 1743
                self.match(MParser.COMMA)
                self.state = 1744
                self.variable_identifier()
                self.state = 1749
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
            super(MParser.Attribute_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def attribute_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Attribute_identifierContext)
            else:
                return self.getTypedRuleContext(MParser.Attribute_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(MParser.COMMA)
            else:
                return self.getToken(MParser.COMMA, i)

        def getRuleIndex(self):
            return MParser.RULE_attribute_identifier_list

        def enterRule(self, listener):
            if hasattr(listener, "enterAttribute_identifier_list"):
                listener.enterAttribute_identifier_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAttribute_identifier_list"):
                listener.exitAttribute_identifier_list(self)




    def attribute_identifier_list(self):

        localctx = MParser.Attribute_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_attribute_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1750
            self.attribute_identifier()
            self.state = 1755
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMA:
                self.state = 1751
                self.match(MParser.COMMA)
                self.state = 1752
                self.attribute_identifier()
                self.state = 1757
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
            super(MParser.Method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def abstract_method_declaration(self):
            return self.getTypedRuleContext(MParser.Abstract_method_declarationContext,0)


        def concrete_method_declaration(self):
            return self.getTypedRuleContext(MParser.Concrete_method_declarationContext,0)


        def native_method_declaration(self):
            return self.getTypedRuleContext(MParser.Native_method_declarationContext,0)


        def test_method_declaration(self):
            return self.getTypedRuleContext(MParser.Test_method_declarationContext,0)


        def getRuleIndex(self):
            return MParser.RULE_method_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterMethod_declaration"):
                listener.enterMethod_declaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethod_declaration"):
                listener.exitMethod_declaration(self)




    def method_declaration(self):

        localctx = MParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_method_declaration)
        try:
            self.state = 1762
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,126,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1758
                self.abstract_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1759
                self.concrete_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1760
                self.native_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1761
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
            super(MParser.Comment_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(MParser.COMMENT, 0)

        def getRuleIndex(self):
            return MParser.RULE_comment_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterComment_statement"):
                listener.enterComment_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitComment_statement"):
                listener.exitComment_statement(self)




    def comment_statement(self):

        localctx = MParser.Comment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_comment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1764
            self.match(MParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Native_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Native_statementContext)
            else:
                return self.getTypedRuleContext(MParser.Native_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def getRuleIndex(self):
            return MParser.RULE_native_statement_list

        def enterRule(self, listener):
            if hasattr(listener, "enterNative_statement_list"):
                listener.enterNative_statement_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNative_statement_list"):
                listener.exitNative_statement_list(self)




    def native_statement_list(self):

        localctx = MParser.Native_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_native_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1766
            self.native_statement()
            self.state = 1772
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,127,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1767
                    self.lfp()
                    self.state = 1768
                    self.native_statement() 
                self.state = 1774
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,127,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_native_statement

     
        def copyFrom(self, ctx):
            super(MParser.Native_statementContext, self).copyFrom(ctx)



    class CSharpNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_statementContext)
            super(MParser.CSharpNativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CSHARP(self):
            return self.getToken(MParser.CSHARP, 0)
        def csharp_statement(self):
            return self.getTypedRuleContext(MParser.Csharp_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpNativeStatement"):
                listener.enterCSharpNativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpNativeStatement"):
                listener.exitCSharpNativeStatement(self)


    class JavaNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_statementContext)
            super(MParser.JavaNativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def JAVA(self):
            return self.getToken(MParser.JAVA, 0)
        def java_statement(self):
            return self.getTypedRuleContext(MParser.Java_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaNativeStatement"):
                listener.enterJavaNativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaNativeStatement"):
                listener.exitJavaNativeStatement(self)


    class JavaScriptNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_statementContext)
            super(MParser.JavaScriptNativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def JAVASCRIPT(self):
            return self.getToken(MParser.JAVASCRIPT, 0)
        def javascript_native_statement(self):
            return self.getTypedRuleContext(MParser.Javascript_native_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaScriptNativeStatement"):
                listener.enterJavaScriptNativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptNativeStatement"):
                listener.exitJavaScriptNativeStatement(self)


    class Python2NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_statementContext)
            super(MParser.Python2NativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PYTHON2(self):
            return self.getToken(MParser.PYTHON2, 0)
        def python_native_statement(self):
            return self.getTypedRuleContext(MParser.Python_native_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPython2NativeStatement"):
                listener.enterPython2NativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython2NativeStatement"):
                listener.exitPython2NativeStatement(self)


    class Python3NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_statementContext)
            super(MParser.Python3NativeStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PYTHON3(self):
            return self.getToken(MParser.PYTHON3, 0)
        def python_native_statement(self):
            return self.getTypedRuleContext(MParser.Python_native_statementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPython3NativeStatement"):
                listener.enterPython3NativeStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython3NativeStatement"):
                listener.exitPython3NativeStatement(self)



    def native_statement(self):

        localctx = MParser.Native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_native_statement)
        try:
            self.state = 1785
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.JAVA]:
                localctx = MParser.JavaNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1775
                self.match(MParser.JAVA)
                self.state = 1776
                self.java_statement()
                pass
            elif token in [MParser.CSHARP]:
                localctx = MParser.CSharpNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1777
                self.match(MParser.CSHARP)
                self.state = 1778
                self.csharp_statement()
                pass
            elif token in [MParser.PYTHON2]:
                localctx = MParser.Python2NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1779
                self.match(MParser.PYTHON2)
                self.state = 1780
                self.python_native_statement()
                pass
            elif token in [MParser.PYTHON3]:
                localctx = MParser.Python3NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1781
                self.match(MParser.PYTHON3)
                self.state = 1782
                self.python_native_statement()
                pass
            elif token in [MParser.JAVASCRIPT]:
                localctx = MParser.JavaScriptNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1783
                self.match(MParser.JAVASCRIPT)
                self.state = 1784
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
            super(MParser.Python_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def python_statement(self):
            return self.getTypedRuleContext(MParser.Python_statementContext,0)


        def SEMI(self):
            return self.getToken(MParser.SEMI, 0)

        def python_module(self):
            return self.getTypedRuleContext(MParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return MParser.RULE_python_native_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_native_statement"):
                listener.enterPython_native_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_native_statement"):
                listener.exitPython_native_statement(self)




    def python_native_statement(self):

        localctx = MParser.Python_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_python_native_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1787
            self.python_statement()
            self.state = 1789
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.SEMI:
                self.state = 1788
                self.match(MParser.SEMI)


            self.state = 1792
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.FROM:
                self.state = 1791
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
            super(MParser.Javascript_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def javascript_statement(self):
            return self.getTypedRuleContext(MParser.Javascript_statementContext,0)


        def SEMI(self):
            return self.getToken(MParser.SEMI, 0)

        def javascript_module(self):
            return self.getTypedRuleContext(MParser.Javascript_moduleContext,0)


        def getRuleIndex(self):
            return MParser.RULE_javascript_native_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_native_statement"):
                listener.enterJavascript_native_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_native_statement"):
                listener.exitJavascript_native_statement(self)




    def javascript_native_statement(self):

        localctx = MParser.Javascript_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_javascript_native_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1794
            self.javascript_statement()
            self.state = 1796
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.SEMI:
                self.state = 1795
                self.match(MParser.SEMI)


            self.state = 1799
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.FROM:
                self.state = 1798
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
            super(MParser.Statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.StatementContext)
            else:
                return self.getTypedRuleContext(MParser.StatementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def getRuleIndex(self):
            return MParser.RULE_statement_list

        def enterRule(self, listener):
            if hasattr(listener, "enterStatement_list"):
                listener.enterStatement_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStatement_list"):
                listener.exitStatement_list(self)




    def statement_list(self):

        localctx = MParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1801
            self.statement()
            self.state = 1807
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,133,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1802
                    self.lfp()
                    self.state = 1803
                    self.statement() 
                self.state = 1809
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,133,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assertion_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Assertion_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assertion(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.AssertionContext)
            else:
                return self.getTypedRuleContext(MParser.AssertionContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def getRuleIndex(self):
            return MParser.RULE_assertion_list

        def enterRule(self, listener):
            if hasattr(listener, "enterAssertion_list"):
                listener.enterAssertion_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssertion_list"):
                listener.exitAssertion_list(self)




    def assertion_list(self):

        localctx = MParser.Assertion_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 252, self.RULE_assertion_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1810
            self.assertion()
            self.state = 1816
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,134,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1811
                    self.lfp()
                    self.state = 1812
                    self.assertion() 
                self.state = 1818
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,134,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Switch_case_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Switch_case_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def switch_case_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Switch_case_statementContext)
            else:
                return self.getTypedRuleContext(MParser.Switch_case_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def getRuleIndex(self):
            return MParser.RULE_switch_case_statement_list

        def enterRule(self, listener):
            if hasattr(listener, "enterSwitch_case_statement_list"):
                listener.enterSwitch_case_statement_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSwitch_case_statement_list"):
                listener.exitSwitch_case_statement_list(self)




    def switch_case_statement_list(self):

        localctx = MParser.Switch_case_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 254, self.RULE_switch_case_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1819
            self.switch_case_statement()
            self.state = 1825
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,135,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1820
                    self.lfp()
                    self.state = 1821
                    self.switch_case_statement() 
                self.state = 1827
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,135,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Catch_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Catch_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def catch_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Catch_statementContext)
            else:
                return self.getTypedRuleContext(MParser.Catch_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.LfpContext)
            else:
                return self.getTypedRuleContext(MParser.LfpContext,i)


        def getRuleIndex(self):
            return MParser.RULE_catch_statement_list

        def enterRule(self, listener):
            if hasattr(listener, "enterCatch_statement_list"):
                listener.enterCatch_statement_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCatch_statement_list"):
                listener.exitCatch_statement_list(self)




    def catch_statement_list(self):

        localctx = MParser.Catch_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_catch_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1828
            self.catch_statement()
            self.state = 1834
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,136,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1829
                    self.lfp()
                    self.state = 1830
                    self.catch_statement() 
                self.state = 1836
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,136,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_collectionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Literal_collectionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_literal_collection

     
        def copyFrom(self, ctx):
            super(MParser.Literal_collectionContext, self).copyFrom(ctx)



    class LiteralListLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a MParser.Literal_collectionContext)
            super(MParser.LiteralListLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(MParser.Literal_list_literalContext,0)

        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterLiteralListLiteral"):
                listener.enterLiteralListLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteralListLiteral"):
                listener.exitLiteralListLiteral(self)


    class LiteralRangeLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a MParser.Literal_collectionContext)
            super(MParser.LiteralRangeLiteralContext, self).__init__(parser)
            self.low = None # Atomic_literalContext
            self.high = None # Atomic_literalContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)
        def RANGE(self):
            return self.getToken(MParser.RANGE, 0)
        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)
        def atomic_literal(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Atomic_literalContext)
            else:
                return self.getTypedRuleContext(MParser.Atomic_literalContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterLiteralRangeLiteral"):
                listener.enterLiteralRangeLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteralRangeLiteral"):
                listener.exitLiteralRangeLiteral(self)


    class LiteralSetLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a MParser.Literal_collectionContext)
            super(MParser.LiteralSetLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(MParser.LT, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(MParser.Literal_list_literalContext,0)

        def GT(self):
            return self.getToken(MParser.GT, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterLiteralSetLiteral"):
                listener.enterLiteralSetLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteralSetLiteral"):
                listener.exitLiteralSetLiteral(self)



    def literal_collection(self):

        localctx = MParser.Literal_collectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_literal_collection)
        try:
            self.state = 1851
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,137,self._ctx)
            if la_ == 1:
                localctx = MParser.LiteralRangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1837
                self.match(MParser.LBRAK)
                self.state = 1838
                localctx.low = self.atomic_literal()
                self.state = 1839
                self.match(MParser.RANGE)
                self.state = 1840
                localctx.high = self.atomic_literal()
                self.state = 1841
                self.match(MParser.RBRAK)
                pass

            elif la_ == 2:
                localctx = MParser.LiteralListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1843
                self.match(MParser.LBRAK)
                self.state = 1844
                self.literal_list_literal()
                self.state = 1845
                self.match(MParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = MParser.LiteralSetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1847
                self.match(MParser.LT)
                self.state = 1848
                self.literal_list_literal()
                self.state = 1849
                self.match(MParser.GT)
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
            super(MParser.Atomic_literalContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_atomic_literal

     
        def copyFrom(self, ctx):
            super(MParser.Atomic_literalContext, self).copyFrom(ctx)



    class MinIntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.MinIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def MIN_INTEGER(self):
            return self.getToken(MParser.MIN_INTEGER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterMinIntegerLiteral"):
                listener.enterMinIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMinIntegerLiteral"):
                listener.exitMinIntegerLiteral(self)


    class DateLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.DateLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATE_LITERAL(self):
            return self.getToken(MParser.DATE_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDateLiteral"):
                listener.enterDateLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDateLiteral"):
                listener.exitDateLiteral(self)


    class BooleanLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.BooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(MParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterBooleanLiteral"):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBooleanLiteral"):
                listener.exitBooleanLiteral(self)


    class VersionLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.VersionLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def VERSION_LITERAL(self):
            return self.getToken(MParser.VERSION_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterVersionLiteral"):
                listener.enterVersionLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVersionLiteral"):
                listener.exitVersionLiteral(self)


    class HexadecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.HexadecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def HEXA_LITERAL(self):
            return self.getToken(MParser.HEXA_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterHexadecimalLiteral"):
                listener.enterHexadecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHexadecimalLiteral"):
                listener.exitHexadecimalLiteral(self)


    class UUIDLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.UUIDLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def UUID_LITERAL(self):
            return self.getToken(MParser.UUID_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterUUIDLiteral"):
                listener.enterUUIDLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitUUIDLiteral"):
                listener.exitUUIDLiteral(self)


    class MaxIntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.MaxIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def MAX_INTEGER(self):
            return self.getToken(MParser.MAX_INTEGER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterMaxIntegerLiteral"):
                listener.enterMaxIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMaxIntegerLiteral"):
                listener.exitMaxIntegerLiteral(self)


    class DateTimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.DateTimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATETIME_LITERAL(self):
            return self.getToken(MParser.DATETIME_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDateTimeLiteral"):
                listener.enterDateTimeLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDateTimeLiteral"):
                listener.exitDateTimeLiteral(self)


    class PeriodLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.PeriodLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def PERIOD_LITERAL(self):
            return self.getToken(MParser.PERIOD_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPeriodLiteral"):
                listener.enterPeriodLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPeriodLiteral"):
                listener.exitPeriodLiteral(self)


    class DecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.DecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(MParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDecimalLiteral"):
                listener.enterDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDecimalLiteral"):
                listener.exitDecimalLiteral(self)


    class TextLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.TextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(MParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterTextLiteral"):
                listener.enterTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTextLiteral"):
                listener.exitTextLiteral(self)


    class NullLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.NullLiteralContext, self).__init__(parser)
            self.n = None # Null_literalContext
            self.copyFrom(ctx)

        def null_literal(self):
            return self.getTypedRuleContext(MParser.Null_literalContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNullLiteral"):
                listener.enterNullLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNullLiteral"):
                listener.exitNullLiteral(self)


    class IntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.IntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(MParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterIntegerLiteral"):
                listener.enterIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIntegerLiteral"):
                listener.exitIntegerLiteral(self)


    class TimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.TimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TIME_LITERAL(self):
            return self.getToken(MParser.TIME_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterTimeLiteral"):
                listener.enterTimeLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTimeLiteral"):
                listener.exitTimeLiteral(self)


    class CharacterLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.CharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(MParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCharacterLiteral"):
                listener.enterCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCharacterLiteral"):
                listener.exitCharacterLiteral(self)



    def atomic_literal(self):

        localctx = MParser.Atomic_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_atomic_literal)
        try:
            self.state = 1868
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.MIN_INTEGER]:
                localctx = MParser.MinIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1853
                localctx.t = self.match(MParser.MIN_INTEGER)
                pass
            elif token in [MParser.MAX_INTEGER]:
                localctx = MParser.MaxIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1854
                localctx.t = self.match(MParser.MAX_INTEGER)
                pass
            elif token in [MParser.INTEGER_LITERAL]:
                localctx = MParser.IntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1855
                localctx.t = self.match(MParser.INTEGER_LITERAL)
                pass
            elif token in [MParser.HEXA_LITERAL]:
                localctx = MParser.HexadecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1856
                localctx.t = self.match(MParser.HEXA_LITERAL)
                pass
            elif token in [MParser.CHAR_LITERAL]:
                localctx = MParser.CharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1857
                localctx.t = self.match(MParser.CHAR_LITERAL)
                pass
            elif token in [MParser.DATE_LITERAL]:
                localctx = MParser.DateLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1858
                localctx.t = self.match(MParser.DATE_LITERAL)
                pass
            elif token in [MParser.TIME_LITERAL]:
                localctx = MParser.TimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1859
                localctx.t = self.match(MParser.TIME_LITERAL)
                pass
            elif token in [MParser.TEXT_LITERAL]:
                localctx = MParser.TextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1860
                localctx.t = self.match(MParser.TEXT_LITERAL)
                pass
            elif token in [MParser.DECIMAL_LITERAL]:
                localctx = MParser.DecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1861
                localctx.t = self.match(MParser.DECIMAL_LITERAL)
                pass
            elif token in [MParser.DATETIME_LITERAL]:
                localctx = MParser.DateTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1862
                localctx.t = self.match(MParser.DATETIME_LITERAL)
                pass
            elif token in [MParser.BOOLEAN_LITERAL]:
                localctx = MParser.BooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1863
                localctx.t = self.match(MParser.BOOLEAN_LITERAL)
                pass
            elif token in [MParser.PERIOD_LITERAL]:
                localctx = MParser.PeriodLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1864
                localctx.t = self.match(MParser.PERIOD_LITERAL)
                pass
            elif token in [MParser.VERSION_LITERAL]:
                localctx = MParser.VersionLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1865
                localctx.t = self.match(MParser.VERSION_LITERAL)
                pass
            elif token in [MParser.UUID_LITERAL]:
                localctx = MParser.UUIDLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1866
                localctx.t = self.match(MParser.UUID_LITERAL)
                pass
            elif token in [MParser.NONE]:
                localctx = MParser.NullLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 1867
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
            super(MParser.Literal_list_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def atomic_literal(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Atomic_literalContext)
            else:
                return self.getTypedRuleContext(MParser.Atomic_literalContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(MParser.COMMA)
            else:
                return self.getToken(MParser.COMMA, i)

        def getRuleIndex(self):
            return MParser.RULE_literal_list_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterLiteral_list_literal"):
                listener.enterLiteral_list_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteral_list_literal"):
                listener.exitLiteral_list_literal(self)




    def literal_list_literal(self):

        localctx = MParser.Literal_list_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 262, self.RULE_literal_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1870
            self.atomic_literal()
            self.state = 1875
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMA:
                self.state = 1871
                self.match(MParser.COMMA)
                self.state = 1872
                self.atomic_literal()
                self.state = 1877
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
            super(MParser.Selectable_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_selectable_expression

     
        def copyFrom(self, ctx):
            super(MParser.Selectable_expressionContext, self).copyFrom(ctx)



    class ThisExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Selectable_expressionContext)
            super(MParser.ThisExpressionContext, self).__init__(parser)
            self.exp = None # This_expressionContext
            self.copyFrom(ctx)

        def this_expression(self):
            return self.getTypedRuleContext(MParser.This_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterThisExpression"):
                listener.enterThisExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitThisExpression"):
                listener.exitThisExpression(self)


    class ParenthesisExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Selectable_expressionContext)
            super(MParser.ParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Parenthesis_expressionContext
            self.copyFrom(ctx)

        def parenthesis_expression(self):
            return self.getTypedRuleContext(MParser.Parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterParenthesisExpression"):
                listener.enterParenthesisExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitParenthesisExpression"):
                listener.exitParenthesisExpression(self)


    class LiteralExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Selectable_expressionContext)
            super(MParser.LiteralExpressionContext, self).__init__(parser)
            self.exp = None # Literal_expressionContext
            self.copyFrom(ctx)

        def literal_expression(self):
            return self.getTypedRuleContext(MParser.Literal_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterLiteralExpression"):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteralExpression"):
                listener.exitLiteralExpression(self)


    class IdentifierExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Selectable_expressionContext)
            super(MParser.IdentifierExpressionContext, self).__init__(parser)
            self.exp = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(MParser.IdentifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIdentifierExpression"):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIdentifierExpression"):
                listener.exitIdentifierExpression(self)



    def selectable_expression(self):

        localctx = MParser.Selectable_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_selectable_expression)
        try:
            self.state = 1882
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,140,self._ctx)
            if la_ == 1:
                localctx = MParser.ParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1878
                localctx.exp = self.parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = MParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1879
                localctx.exp = self.literal_expression()
                pass

            elif la_ == 3:
                localctx = MParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1880
                localctx.exp = self.identifier()
                pass

            elif la_ == 4:
                localctx = MParser.ThisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1881
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
            super(MParser.This_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SELF(self):
            return self.getToken(MParser.SELF, 0)

        def THIS(self):
            return self.getToken(MParser.THIS, 0)

        def getRuleIndex(self):
            return MParser.RULE_this_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterThis_expression"):
                listener.enterThis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitThis_expression"):
                listener.exitThis_expression(self)




    def this_expression(self):

        localctx = MParser.This_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_this_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1884
            _la = self._input.LA(1)
            if not(_la==MParser.SELF or _la==MParser.THIS):
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
            super(MParser.Parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def getRuleIndex(self):
            return MParser.RULE_parenthesis_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterParenthesis_expression"):
                listener.enterParenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitParenthesis_expression"):
                listener.exitParenthesis_expression(self)




    def parenthesis_expression(self):

        localctx = MParser.Parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1886
            self.match(MParser.LPAR)
            self.state = 1887
            self.expression(0)
            self.state = 1888
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def atomic_literal(self):
            return self.getTypedRuleContext(MParser.Atomic_literalContext,0)


        def collection_literal(self):
            return self.getTypedRuleContext(MParser.Collection_literalContext,0)


        def getRuleIndex(self):
            return MParser.RULE_literal_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterLiteral_expression"):
                listener.enterLiteral_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteral_expression"):
                listener.exitLiteral_expression(self)




    def literal_expression(self):

        localctx = MParser.Literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_literal_expression)
        try:
            self.state = 1892
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.NONE, MParser.BOOLEAN_LITERAL, MParser.CHAR_LITERAL, MParser.MIN_INTEGER, MParser.MAX_INTEGER, MParser.TEXT_LITERAL, MParser.UUID_LITERAL, MParser.INTEGER_LITERAL, MParser.HEXA_LITERAL, MParser.DECIMAL_LITERAL, MParser.DATETIME_LITERAL, MParser.TIME_LITERAL, MParser.DATE_LITERAL, MParser.PERIOD_LITERAL, MParser.VERSION_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1890
                self.atomic_literal()
                pass
            elif token in [MParser.LPAR, MParser.LBRAK, MParser.LCURL, MParser.LT, MParser.MUTABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1891
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
            super(MParser.Collection_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def range_literal(self):
            return self.getTypedRuleContext(MParser.Range_literalContext,0)


        def list_literal(self):
            return self.getTypedRuleContext(MParser.List_literalContext,0)


        def set_literal(self):
            return self.getTypedRuleContext(MParser.Set_literalContext,0)


        def dict_literal(self):
            return self.getTypedRuleContext(MParser.Dict_literalContext,0)


        def tuple_literal(self):
            return self.getTypedRuleContext(MParser.Tuple_literalContext,0)


        def getRuleIndex(self):
            return MParser.RULE_collection_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterCollection_literal"):
                listener.enterCollection_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCollection_literal"):
                listener.exitCollection_literal(self)




    def collection_literal(self):

        localctx = MParser.Collection_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 272, self.RULE_collection_literal)
        try:
            self.state = 1899
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,142,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1894
                self.range_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1895
                self.list_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1896
                self.set_literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1897
                self.dict_literal()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1898
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
            super(MParser.Tuple_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def MUTABLE(self):
            return self.getToken(MParser.MUTABLE, 0)

        def expression_tuple(self):
            return self.getTypedRuleContext(MParser.Expression_tupleContext,0)


        def getRuleIndex(self):
            return MParser.RULE_tuple_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterTuple_literal"):
                listener.enterTuple_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTuple_literal"):
                listener.exitTuple_literal(self)




    def tuple_literal(self):

        localctx = MParser.Tuple_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 274, self.RULE_tuple_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1902
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.MUTABLE:
                self.state = 1901
                self.match(MParser.MUTABLE)


            self.state = 1904
            self.match(MParser.LPAR)
            self.state = 1906
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.LTGT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 100)) & ~0x3f) == 0 and ((1 << (_la - 100)) & ((1 << (MParser.EXECUTE - 100)) | (1 << (MParser.FETCH - 100)) | (1 << (MParser.MUTABLE - 100)) | (1 << (MParser.NONE - 100)) | (1 << (MParser.NOT - 100)) | (1 << (MParser.READ - 100)) | (1 << (MParser.SELF - 100)) | (1 << (MParser.SORTED - 100)) | (1 << (MParser.THIS - 100)) | (1 << (MParser.BOOLEAN_LITERAL - 100)) | (1 << (MParser.CHAR_LITERAL - 100)) | (1 << (MParser.MIN_INTEGER - 100)) | (1 << (MParser.MAX_INTEGER - 100)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (MParser.SYMBOL_IDENTIFIER - 164)) | (1 << (MParser.TYPE_IDENTIFIER - 164)) | (1 << (MParser.VARIABLE_IDENTIFIER - 164)) | (1 << (MParser.TEXT_LITERAL - 164)) | (1 << (MParser.UUID_LITERAL - 164)) | (1 << (MParser.INTEGER_LITERAL - 164)) | (1 << (MParser.HEXA_LITERAL - 164)) | (1 << (MParser.DECIMAL_LITERAL - 164)) | (1 << (MParser.DATETIME_LITERAL - 164)) | (1 << (MParser.TIME_LITERAL - 164)) | (1 << (MParser.DATE_LITERAL - 164)) | (1 << (MParser.PERIOD_LITERAL - 164)) | (1 << (MParser.VERSION_LITERAL - 164)))) != 0):
                self.state = 1905
                self.expression_tuple()


            self.state = 1908
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dict_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Dict_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LCURL(self):
            return self.getToken(MParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(MParser.RCURL, 0)

        def MUTABLE(self):
            return self.getToken(MParser.MUTABLE, 0)

        def dict_entry_list(self):
            return self.getTypedRuleContext(MParser.Dict_entry_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_dict_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterDict_literal"):
                listener.enterDict_literal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDict_literal"):
                listener.exitDict_literal(self)




    def dict_literal(self):

        localctx = MParser.Dict_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_dict_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1911
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.MUTABLE:
                self.state = 1910
                self.match(MParser.MUTABLE)


            self.state = 1913
            self.match(MParser.LCURL)
            self.state = 1915
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.LTGT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 100)) & ~0x3f) == 0 and ((1 << (_la - 100)) & ((1 << (MParser.EXECUTE - 100)) | (1 << (MParser.FETCH - 100)) | (1 << (MParser.MUTABLE - 100)) | (1 << (MParser.NONE - 100)) | (1 << (MParser.NOT - 100)) | (1 << (MParser.READ - 100)) | (1 << (MParser.SELF - 100)) | (1 << (MParser.SORTED - 100)) | (1 << (MParser.THIS - 100)) | (1 << (MParser.BOOLEAN_LITERAL - 100)) | (1 << (MParser.CHAR_LITERAL - 100)) | (1 << (MParser.MIN_INTEGER - 100)) | (1 << (MParser.MAX_INTEGER - 100)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (MParser.SYMBOL_IDENTIFIER - 164)) | (1 << (MParser.TYPE_IDENTIFIER - 164)) | (1 << (MParser.VARIABLE_IDENTIFIER - 164)) | (1 << (MParser.TEXT_LITERAL - 164)) | (1 << (MParser.UUID_LITERAL - 164)) | (1 << (MParser.INTEGER_LITERAL - 164)) | (1 << (MParser.HEXA_LITERAL - 164)) | (1 << (MParser.DECIMAL_LITERAL - 164)) | (1 << (MParser.DATETIME_LITERAL - 164)) | (1 << (MParser.TIME_LITERAL - 164)) | (1 << (MParser.DATE_LITERAL - 164)) | (1 << (MParser.PERIOD_LITERAL - 164)) | (1 << (MParser.VERSION_LITERAL - 164)))) != 0):
                self.state = 1914
                self.dict_entry_list()


            self.state = 1917
            self.match(MParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_tupleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Expression_tupleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(MParser.COMMA)
            else:
                return self.getToken(MParser.COMMA, i)

        def getRuleIndex(self):
            return MParser.RULE_expression_tuple

        def enterRule(self, listener):
            if hasattr(listener, "enterExpression_tuple"):
                listener.enterExpression_tuple(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExpression_tuple"):
                listener.exitExpression_tuple(self)




    def expression_tuple(self):

        localctx = MParser.Expression_tupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 278, self.RULE_expression_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1919
            self.expression(0)
            self.state = 1920
            self.match(MParser.COMMA)
            self.state = 1929
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.LTGT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 100)) & ~0x3f) == 0 and ((1 << (_la - 100)) & ((1 << (MParser.EXECUTE - 100)) | (1 << (MParser.FETCH - 100)) | (1 << (MParser.MUTABLE - 100)) | (1 << (MParser.NONE - 100)) | (1 << (MParser.NOT - 100)) | (1 << (MParser.READ - 100)) | (1 << (MParser.SELF - 100)) | (1 << (MParser.SORTED - 100)) | (1 << (MParser.THIS - 100)) | (1 << (MParser.BOOLEAN_LITERAL - 100)) | (1 << (MParser.CHAR_LITERAL - 100)) | (1 << (MParser.MIN_INTEGER - 100)) | (1 << (MParser.MAX_INTEGER - 100)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (MParser.SYMBOL_IDENTIFIER - 164)) | (1 << (MParser.TYPE_IDENTIFIER - 164)) | (1 << (MParser.VARIABLE_IDENTIFIER - 164)) | (1 << (MParser.TEXT_LITERAL - 164)) | (1 << (MParser.UUID_LITERAL - 164)) | (1 << (MParser.INTEGER_LITERAL - 164)) | (1 << (MParser.HEXA_LITERAL - 164)) | (1 << (MParser.DECIMAL_LITERAL - 164)) | (1 << (MParser.DATETIME_LITERAL - 164)) | (1 << (MParser.TIME_LITERAL - 164)) | (1 << (MParser.DATE_LITERAL - 164)) | (1 << (MParser.PERIOD_LITERAL - 164)) | (1 << (MParser.VERSION_LITERAL - 164)))) != 0):
                self.state = 1921
                self.expression(0)
                self.state = 1926
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MParser.COMMA:
                    self.state = 1922
                    self.match(MParser.COMMA)
                    self.state = 1923
                    self.expression(0)
                    self.state = 1928
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
            super(MParser.Dict_entry_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def dict_entry(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Dict_entryContext)
            else:
                return self.getTypedRuleContext(MParser.Dict_entryContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(MParser.COMMA)
            else:
                return self.getToken(MParser.COMMA, i)

        def getRuleIndex(self):
            return MParser.RULE_dict_entry_list

        def enterRule(self, listener):
            if hasattr(listener, "enterDict_entry_list"):
                listener.enterDict_entry_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDict_entry_list"):
                listener.exitDict_entry_list(self)




    def dict_entry_list(self):

        localctx = MParser.Dict_entry_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_dict_entry_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1931
            self.dict_entry()
            self.state = 1936
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMA:
                self.state = 1932
                self.match(MParser.COMMA)
                self.state = 1933
                self.dict_entry()
                self.state = 1938
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
            super(MParser.Dict_entryContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.key = None # ExpressionContext
            self.value = None # ExpressionContext

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MParser.RULE_dict_entry

        def enterRule(self, listener):
            if hasattr(listener, "enterDict_entry"):
                listener.enterDict_entry(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDict_entry"):
                listener.exitDict_entry(self)




    def dict_entry(self):

        localctx = MParser.Dict_entryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 282, self.RULE_dict_entry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1939
            localctx.key = self.expression(0)
            self.state = 1940
            self.match(MParser.COLON)
            self.state = 1941
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
            super(MParser.Slice_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_slice_arguments

     
        def copyFrom(self, ctx):
            super(MParser.Slice_argumentsContext, self).copyFrom(ctx)



    class SliceFirstAndLastContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a MParser.Slice_argumentsContext)
            super(MParser.SliceFirstAndLastContext, self).__init__(parser)
            self.first = None # ExpressionContext
            self.last = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterSliceFirstAndLast"):
                listener.enterSliceFirstAndLast(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSliceFirstAndLast"):
                listener.exitSliceFirstAndLast(self)


    class SliceLastOnlyContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a MParser.Slice_argumentsContext)
            super(MParser.SliceLastOnlyContext, self).__init__(parser)
            self.last = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSliceLastOnly"):
                listener.enterSliceLastOnly(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSliceLastOnly"):
                listener.exitSliceLastOnly(self)


    class SliceFirstOnlyContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a MParser.Slice_argumentsContext)
            super(MParser.SliceFirstOnlyContext, self).__init__(parser)
            self.first = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(MParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterSliceFirstOnly"):
                listener.enterSliceFirstOnly(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSliceFirstOnly"):
                listener.exitSliceFirstOnly(self)



    def slice_arguments(self):

        localctx = MParser.Slice_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_slice_arguments)
        try:
            self.state = 1952
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,150,self._ctx)
            if la_ == 1:
                localctx = MParser.SliceFirstAndLastContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1943
                localctx.first = self.expression(0)
                self.state = 1944
                self.match(MParser.COLON)
                self.state = 1945
                localctx.last = self.expression(0)
                pass

            elif la_ == 2:
                localctx = MParser.SliceFirstOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1947
                localctx.first = self.expression(0)
                self.state = 1948
                self.match(MParser.COLON)
                pass

            elif la_ == 3:
                localctx = MParser.SliceLastOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1950
                self.match(MParser.COLON)
                self.state = 1951
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
            super(MParser.Assign_variable_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def assign(self):
            return self.getTypedRuleContext(MParser.AssignContext,0)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_assign_variable_statement

        def enterRule(self, listener):
            if hasattr(listener, "enterAssign_variable_statement"):
                listener.enterAssign_variable_statement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign_variable_statement"):
                listener.exitAssign_variable_statement(self)




    def assign_variable_statement(self):

        localctx = MParser.Assign_variable_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 286, self.RULE_assign_variable_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1954
            self.variable_identifier()
            self.state = 1955
            self.assign()
            self.state = 1956
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
            super(MParser.Assignable_instanceContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_assignable_instance

     
        def copyFrom(self, ctx):
            super(MParser.Assignable_instanceContext, self).copyFrom(ctx)


    class ChildInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a MParser.Assignable_instanceContext)
            super(MParser.ChildInstanceContext, self).__init__(parser)
            self.copyFrom(ctx)

        def assignable_instance(self):
            return self.getTypedRuleContext(MParser.Assignable_instanceContext,0)

        def child_instance(self):
            return self.getTypedRuleContext(MParser.Child_instanceContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterChildInstance"):
                listener.enterChildInstance(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitChildInstance"):
                listener.exitChildInstance(self)


    class RootInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a MParser.Assignable_instanceContext)
            super(MParser.RootInstanceContext, self).__init__(parser)
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterRootInstance"):
                listener.enterRootInstance(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRootInstance"):
                listener.exitRootInstance(self)



    def assignable_instance(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Assignable_instanceContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 288
        self.enterRecursionRule(localctx, 288, self.RULE_assignable_instance, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.RootInstanceContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1959
            self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1965
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,151,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.ChildInstanceContext(self, MParser.Assignable_instanceContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignable_instance)
                    self.state = 1961
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1962
                    self.child_instance() 
                self.state = 1967
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,151,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Is_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Is_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_is_expression

     
        def copyFrom(self, ctx):
            super(MParser.Is_expressionContext, self).copyFrom(ctx)



    class IsATypeExpressionContext(Is_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Is_expressionContext)
            super(MParser.IsATypeExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)
        def category_or_any_type(self):
            return self.getTypedRuleContext(MParser.Category_or_any_typeContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIsATypeExpression"):
                listener.enterIsATypeExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsATypeExpression"):
                listener.exitIsATypeExpression(self)


    class IsOtherExpressionContext(Is_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Is_expressionContext)
            super(MParser.IsOtherExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterIsOtherExpression"):
                listener.enterIsOtherExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIsOtherExpression"):
                listener.exitIsOtherExpression(self)



    def is_expression(self):

        localctx = MParser.Is_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_is_expression)
        try:
            self.state = 1972
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,152,self._ctx)
            if la_ == 1:
                localctx = MParser.IsATypeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1968
                if not self.willBeAOrAn():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willBeAOrAn()")
                self.state = 1969
                self.match(MParser.VARIABLE_IDENTIFIER)
                self.state = 1970
                self.category_or_any_type()
                pass

            elif la_ == 2:
                localctx = MParser.IsOtherExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1971
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
            super(MParser.Read_all_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # ExpressionContext

        def READ(self):
            return self.getToken(MParser.READ, 0)

        def ALL(self):
            return self.getToken(MParser.ALL, 0)

        def FROM(self):
            return self.getToken(MParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_read_all_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterRead_all_expression"):
                listener.enterRead_all_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRead_all_expression"):
                listener.exitRead_all_expression(self)




    def read_all_expression(self):

        localctx = MParser.Read_all_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 292, self.RULE_read_all_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1974
            self.match(MParser.READ)
            self.state = 1975
            self.match(MParser.ALL)
            self.state = 1976
            self.match(MParser.FROM)
            self.state = 1977
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
            super(MParser.Read_one_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # ExpressionContext

        def READ(self):
            return self.getToken(MParser.READ, 0)

        def ONE(self):
            return self.getToken(MParser.ONE, 0)

        def FROM(self):
            return self.getToken(MParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_read_one_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterRead_one_expression"):
                listener.enterRead_one_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRead_one_expression"):
                listener.exitRead_one_expression(self)




    def read_one_expression(self):

        localctx = MParser.Read_one_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_read_one_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1979
            self.match(MParser.READ)
            self.state = 1980
            self.match(MParser.ONE)
            self.state = 1981
            self.match(MParser.FROM)
            self.state = 1982
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
            super(MParser.Order_by_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def order_by(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Order_byContext)
            else:
                return self.getTypedRuleContext(MParser.Order_byContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(MParser.COMMA)
            else:
                return self.getToken(MParser.COMMA, i)

        def getRuleIndex(self):
            return MParser.RULE_order_by_list

        def enterRule(self, listener):
            if hasattr(listener, "enterOrder_by_list"):
                listener.enterOrder_by_list(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOrder_by_list"):
                listener.exitOrder_by_list(self)




    def order_by_list(self):

        localctx = MParser.Order_by_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 296, self.RULE_order_by_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1984
            self.order_by()
            self.state = 1989
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,153,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1985
                    self.match(MParser.COMMA)
                    self.state = 1986
                    self.order_by() 
                self.state = 1991
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,153,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Order_byContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Order_byContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(MParser.Variable_identifierContext,i)


        def DOT(self, i=None):
            if i is None:
                return self.getTokens(MParser.DOT)
            else:
                return self.getToken(MParser.DOT, i)

        def ASC(self):
            return self.getToken(MParser.ASC, 0)

        def DESC(self):
            return self.getToken(MParser.DESC, 0)

        def getRuleIndex(self):
            return MParser.RULE_order_by

        def enterRule(self, listener):
            if hasattr(listener, "enterOrder_by"):
                listener.enterOrder_by(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOrder_by"):
                listener.exitOrder_by(self)




    def order_by(self):

        localctx = MParser.Order_byContext(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_order_by)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1992
            self.variable_identifier()
            self.state = 1997
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,154,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1993
                    self.match(MParser.DOT)
                    self.state = 1994
                    self.variable_identifier() 
                self.state = 1999
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,154,self._ctx)

            self.state = 2001
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,155,self._ctx)
            if la_ == 1:
                self.state = 2000
                _la = self._input.LA(1)
                if not(_la==MParser.ASC or _la==MParser.DESC):
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
            super(MParser.OperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_operator

     
        def copyFrom(self, ctx):
            super(MParser.OperatorContext, self).copyFrom(ctx)



    class OperatorPlusContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a MParser.OperatorContext)
            super(MParser.OperatorPlusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PLUS(self):
            return self.getToken(MParser.PLUS, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorPlus"):
                listener.enterOperatorPlus(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorPlus"):
                listener.exitOperatorPlus(self)


    class OperatorDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a MParser.OperatorContext)
            super(MParser.OperatorDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def divide(self):
            return self.getTypedRuleContext(MParser.DivideContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorDivide"):
                listener.enterOperatorDivide(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorDivide"):
                listener.exitOperatorDivide(self)


    class OperatorIDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a MParser.OperatorContext)
            super(MParser.OperatorIDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def idivide(self):
            return self.getTypedRuleContext(MParser.IdivideContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorIDivide"):
                listener.enterOperatorIDivide(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorIDivide"):
                listener.exitOperatorIDivide(self)


    class OperatorMultiplyContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a MParser.OperatorContext)
            super(MParser.OperatorMultiplyContext, self).__init__(parser)
            self.copyFrom(ctx)

        def multiply(self):
            return self.getTypedRuleContext(MParser.MultiplyContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorMultiply"):
                listener.enterOperatorMultiply(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorMultiply"):
                listener.exitOperatorMultiply(self)


    class OperatorMinusContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a MParser.OperatorContext)
            super(MParser.OperatorMinusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(MParser.MINUS, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorMinus"):
                listener.enterOperatorMinus(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorMinus"):
                listener.exitOperatorMinus(self)


    class OperatorModuloContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a MParser.OperatorContext)
            super(MParser.OperatorModuloContext, self).__init__(parser)
            self.copyFrom(ctx)

        def modulo(self):
            return self.getTypedRuleContext(MParser.ModuloContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterOperatorModulo"):
                listener.enterOperatorModulo(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperatorModulo"):
                listener.exitOperatorModulo(self)



    def operator(self):

        localctx = MParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 300, self.RULE_operator)
        try:
            self.state = 2009
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.PLUS]:
                localctx = MParser.OperatorPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2003
                self.match(MParser.PLUS)
                pass
            elif token in [MParser.MINUS]:
                localctx = MParser.OperatorMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2004
                self.match(MParser.MINUS)
                pass
            elif token in [MParser.STAR]:
                localctx = MParser.OperatorMultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2005
                self.multiply()
                pass
            elif token in [MParser.SLASH]:
                localctx = MParser.OperatorDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2006
                self.divide()
                pass
            elif token in [MParser.BSLASH]:
                localctx = MParser.OperatorIDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2007
                self.idivide()
                pass
            elif token in [MParser.PERCENT, MParser.MODULO]:
                localctx = MParser.OperatorModuloContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 2008
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
            super(MParser.KeywordContext, self).__init__(parent, invokingState)
            self.parser = parser

        def JAVA(self):
            return self.getToken(MParser.JAVA, 0)

        def CSHARP(self):
            return self.getToken(MParser.CSHARP, 0)

        def PYTHON2(self):
            return self.getToken(MParser.PYTHON2, 0)

        def PYTHON3(self):
            return self.getToken(MParser.PYTHON3, 0)

        def JAVASCRIPT(self):
            return self.getToken(MParser.JAVASCRIPT, 0)

        def SWIFT(self):
            return self.getToken(MParser.SWIFT, 0)

        def BOOLEAN(self):
            return self.getToken(MParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(MParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(MParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(MParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(MParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(MParser.DATE, 0)

        def TIME(self):
            return self.getToken(MParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(MParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(MParser.PERIOD, 0)

        def VERSION(self):
            return self.getToken(MParser.VERSION, 0)

        def METHOD_T(self):
            return self.getToken(MParser.METHOD_T, 0)

        def CODE(self):
            return self.getToken(MParser.CODE, 0)

        def DOCUMENT(self):
            return self.getToken(MParser.DOCUMENT, 0)

        def BLOB(self):
            return self.getToken(MParser.BLOB, 0)

        def IMAGE(self):
            return self.getToken(MParser.IMAGE, 0)

        def UUID(self):
            return self.getToken(MParser.UUID, 0)

        def ITERATOR(self):
            return self.getToken(MParser.ITERATOR, 0)

        def CURSOR(self):
            return self.getToken(MParser.CURSOR, 0)

        def HTML(self):
            return self.getToken(MParser.HTML, 0)

        def ABSTRACT(self):
            return self.getToken(MParser.ABSTRACT, 0)

        def ALL(self):
            return self.getToken(MParser.ALL, 0)

        def ALWAYS(self):
            return self.getToken(MParser.ALWAYS, 0)

        def AND(self):
            return self.getToken(MParser.AND, 0)

        def ANY(self):
            return self.getToken(MParser.ANY, 0)

        def AS(self):
            return self.getToken(MParser.AS, 0)

        def ASC(self):
            return self.getToken(MParser.ASC, 0)

        def ATTR(self):
            return self.getToken(MParser.ATTR, 0)

        def ATTRIBUTE(self):
            return self.getToken(MParser.ATTRIBUTE, 0)

        def ATTRIBUTES(self):
            return self.getToken(MParser.ATTRIBUTES, 0)

        def BINDINGS(self):
            return self.getToken(MParser.BINDINGS, 0)

        def BREAK(self):
            return self.getToken(MParser.BREAK, 0)

        def BY(self):
            return self.getToken(MParser.BY, 0)

        def CASE(self):
            return self.getToken(MParser.CASE, 0)

        def CATCH(self):
            return self.getToken(MParser.CATCH, 0)

        def CATEGORY(self):
            return self.getToken(MParser.CATEGORY, 0)

        def CLASS(self):
            return self.getToken(MParser.CLASS, 0)

        def CLOSE(self):
            return self.getToken(MParser.CLOSE, 0)

        def CONTAINS(self):
            return self.getToken(MParser.CONTAINS, 0)

        def DEF(self):
            return self.getToken(MParser.DEF, 0)

        def DEFAULT(self):
            return self.getToken(MParser.DEFAULT, 0)

        def DEFINE(self):
            return self.getToken(MParser.DEFINE, 0)

        def DELETE(self):
            return self.getToken(MParser.DELETE, 0)

        def DESC(self):
            return self.getToken(MParser.DESC, 0)

        def DO(self):
            return self.getToken(MParser.DO, 0)

        def DOING(self):
            return self.getToken(MParser.DOING, 0)

        def EACH(self):
            return self.getToken(MParser.EACH, 0)

        def ELSE(self):
            return self.getToken(MParser.ELSE, 0)

        def ENUM(self):
            return self.getToken(MParser.ENUM, 0)

        def ENUMERATED(self):
            return self.getToken(MParser.ENUMERATED, 0)

        def EXCEPT(self):
            return self.getToken(MParser.EXCEPT, 0)

        def EXECUTE(self):
            return self.getToken(MParser.EXECUTE, 0)

        def EXPECTING(self):
            return self.getToken(MParser.EXPECTING, 0)

        def EXTENDS(self):
            return self.getToken(MParser.EXTENDS, 0)

        def FETCH(self):
            return self.getToken(MParser.FETCH, 0)

        def FILTERED(self):
            return self.getToken(MParser.FILTERED, 0)

        def FINALLY(self):
            return self.getToken(MParser.FINALLY, 0)

        def FLUSH(self):
            return self.getToken(MParser.FLUSH, 0)

        def FOR(self):
            return self.getToken(MParser.FOR, 0)

        def FROM(self):
            return self.getToken(MParser.FROM, 0)

        def GETTER(self):
            return self.getToken(MParser.GETTER, 0)

        def HAS(self):
            return self.getToken(MParser.HAS, 0)

        def IF(self):
            return self.getToken(MParser.IF, 0)

        def IN(self):
            return self.getToken(MParser.IN, 0)

        def INDEX(self):
            return self.getToken(MParser.INDEX, 0)

        def INVOKE(self):
            return self.getToken(MParser.INVOKE, 0)

        def IS(self):
            return self.getToken(MParser.IS, 0)

        def MATCHING(self):
            return self.getToken(MParser.MATCHING, 0)

        def METHOD(self):
            return self.getToken(MParser.METHOD, 0)

        def METHODS(self):
            return self.getToken(MParser.METHODS, 0)

        def MODULO(self):
            return self.getToken(MParser.MODULO, 0)

        def MUTABLE(self):
            return self.getToken(MParser.MUTABLE, 0)

        def NATIVE(self):
            return self.getToken(MParser.NATIVE, 0)

        def NONE(self):
            return self.getToken(MParser.NONE, 0)

        def NOT(self):
            return self.getToken(MParser.NOT, 0)

        def NOTHING(self):
            return self.getToken(MParser.NOTHING, 0)

        def NULL(self):
            return self.getToken(MParser.NULL, 0)

        def ON(self):
            return self.getToken(MParser.ON, 0)

        def ONE(self):
            return self.getToken(MParser.ONE, 0)

        def OPEN(self):
            return self.getToken(MParser.OPEN, 0)

        def OPERATOR(self):
            return self.getToken(MParser.OPERATOR, 0)

        def OR(self):
            return self.getToken(MParser.OR, 0)

        def ORDER(self):
            return self.getToken(MParser.ORDER, 0)

        def OTHERWISE(self):
            return self.getToken(MParser.OTHERWISE, 0)

        def PASS(self):
            return self.getToken(MParser.PASS, 0)

        def RAISE(self):
            return self.getToken(MParser.RAISE, 0)

        def READ(self):
            return self.getToken(MParser.READ, 0)

        def RECEIVING(self):
            return self.getToken(MParser.RECEIVING, 0)

        def RESOURCE(self):
            return self.getToken(MParser.RESOURCE, 0)

        def RETURN(self):
            return self.getToken(MParser.RETURN, 0)

        def RETURNING(self):
            return self.getToken(MParser.RETURNING, 0)

        def ROWS(self):
            return self.getToken(MParser.ROWS, 0)

        def SELF(self):
            return self.getToken(MParser.SELF, 0)

        def SETTER(self):
            return self.getToken(MParser.SETTER, 0)

        def SINGLETON(self):
            return self.getToken(MParser.SINGLETON, 0)

        def SORTED(self):
            return self.getToken(MParser.SORTED, 0)

        def STORABLE(self):
            return self.getToken(MParser.STORABLE, 0)

        def STORE(self):
            return self.getToken(MParser.STORE, 0)

        def SWITCH(self):
            return self.getToken(MParser.SWITCH, 0)

        def TEST(self):
            return self.getToken(MParser.TEST, 0)

        def THIS(self):
            return self.getToken(MParser.THIS, 0)

        def THROW(self):
            return self.getToken(MParser.THROW, 0)

        def TO(self):
            return self.getToken(MParser.TO, 0)

        def TRY(self):
            return self.getToken(MParser.TRY, 0)

        def VERIFYING(self):
            return self.getToken(MParser.VERIFYING, 0)

        def WIDGET(self):
            return self.getToken(MParser.WIDGET, 0)

        def WITH(self):
            return self.getToken(MParser.WITH, 0)

        def WHEN(self):
            return self.getToken(MParser.WHEN, 0)

        def WHERE(self):
            return self.getToken(MParser.WHERE, 0)

        def WHILE(self):
            return self.getToken(MParser.WHILE, 0)

        def WRITE(self):
            return self.getToken(MParser.WRITE, 0)

        def getRuleIndex(self):
            return MParser.RULE_keyword

        def enterRule(self, listener):
            if hasattr(listener, "enterKeyword"):
                listener.enterKeyword(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitKeyword"):
                listener.exitKeyword(self)




    def keyword(self):

        localctx = MParser.KeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_keyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2011
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.JAVA) | (1 << MParser.CSHARP) | (1 << MParser.PYTHON2) | (1 << MParser.PYTHON3) | (1 << MParser.JAVASCRIPT) | (1 << MParser.SWIFT) | (1 << MParser.BOOLEAN) | (1 << MParser.CHARACTER) | (1 << MParser.TEXT) | (1 << MParser.INTEGER) | (1 << MParser.DECIMAL) | (1 << MParser.DATE) | (1 << MParser.TIME) | (1 << MParser.DATETIME) | (1 << MParser.PERIOD) | (1 << MParser.VERSION) | (1 << MParser.METHOD_T) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (MParser.IMAGE - 64)) | (1 << (MParser.UUID - 64)) | (1 << (MParser.ITERATOR - 64)) | (1 << (MParser.CURSOR - 64)) | (1 << (MParser.HTML - 64)) | (1 << (MParser.ABSTRACT - 64)) | (1 << (MParser.ALL - 64)) | (1 << (MParser.ALWAYS - 64)) | (1 << (MParser.AND - 64)) | (1 << (MParser.ANY - 64)) | (1 << (MParser.AS - 64)) | (1 << (MParser.ASC - 64)) | (1 << (MParser.ATTR - 64)) | (1 << (MParser.ATTRIBUTE - 64)) | (1 << (MParser.ATTRIBUTES - 64)) | (1 << (MParser.BINDINGS - 64)) | (1 << (MParser.BREAK - 64)) | (1 << (MParser.BY - 64)) | (1 << (MParser.CASE - 64)) | (1 << (MParser.CATCH - 64)) | (1 << (MParser.CATEGORY - 64)) | (1 << (MParser.CLASS - 64)) | (1 << (MParser.CLOSE - 64)) | (1 << (MParser.CONTAINS - 64)) | (1 << (MParser.DEF - 64)) | (1 << (MParser.DEFAULT - 64)) | (1 << (MParser.DEFINE - 64)) | (1 << (MParser.DELETE - 64)) | (1 << (MParser.DESC - 64)) | (1 << (MParser.DO - 64)) | (1 << (MParser.DOING - 64)) | (1 << (MParser.EACH - 64)) | (1 << (MParser.ELSE - 64)) | (1 << (MParser.ENUM - 64)) | (1 << (MParser.ENUMERATED - 64)) | (1 << (MParser.EXCEPT - 64)) | (1 << (MParser.EXECUTE - 64)) | (1 << (MParser.EXPECTING - 64)) | (1 << (MParser.EXTENDS - 64)) | (1 << (MParser.FETCH - 64)) | (1 << (MParser.FILTERED - 64)) | (1 << (MParser.FINALLY - 64)) | (1 << (MParser.FLUSH - 64)) | (1 << (MParser.FOR - 64)) | (1 << (MParser.FROM - 64)) | (1 << (MParser.GETTER - 64)) | (1 << (MParser.HAS - 64)) | (1 << (MParser.IF - 64)) | (1 << (MParser.IN - 64)) | (1 << (MParser.INDEX - 64)) | (1 << (MParser.INVOKE - 64)) | (1 << (MParser.IS - 64)) | (1 << (MParser.MATCHING - 64)) | (1 << (MParser.METHOD - 64)) | (1 << (MParser.METHODS - 64)) | (1 << (MParser.MODULO - 64)) | (1 << (MParser.MUTABLE - 64)) | (1 << (MParser.NATIVE - 64)) | (1 << (MParser.NONE - 64)) | (1 << (MParser.NOT - 64)) | (1 << (MParser.NOTHING - 64)) | (1 << (MParser.NULL - 64)) | (1 << (MParser.ON - 64)) | (1 << (MParser.ONE - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (MParser.OPEN - 128)) | (1 << (MParser.OPERATOR - 128)) | (1 << (MParser.OR - 128)) | (1 << (MParser.ORDER - 128)) | (1 << (MParser.OTHERWISE - 128)) | (1 << (MParser.PASS - 128)) | (1 << (MParser.RAISE - 128)) | (1 << (MParser.READ - 128)) | (1 << (MParser.RECEIVING - 128)) | (1 << (MParser.RESOURCE - 128)) | (1 << (MParser.RETURN - 128)) | (1 << (MParser.RETURNING - 128)) | (1 << (MParser.ROWS - 128)) | (1 << (MParser.SELF - 128)) | (1 << (MParser.SETTER - 128)) | (1 << (MParser.SINGLETON - 128)) | (1 << (MParser.SORTED - 128)) | (1 << (MParser.STORABLE - 128)) | (1 << (MParser.STORE - 128)) | (1 << (MParser.SWITCH - 128)) | (1 << (MParser.TEST - 128)) | (1 << (MParser.THIS - 128)) | (1 << (MParser.THROW - 128)) | (1 << (MParser.TO - 128)) | (1 << (MParser.TRY - 128)) | (1 << (MParser.VERIFYING - 128)) | (1 << (MParser.WIDGET - 128)) | (1 << (MParser.WITH - 128)) | (1 << (MParser.WHEN - 128)) | (1 << (MParser.WHERE - 128)) | (1 << (MParser.WHILE - 128)) | (1 << (MParser.WRITE - 128)))) != 0)):
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
            super(MParser.New_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MParser.RULE_new_token

        def enterRule(self, listener):
            if hasattr(listener, "enterNew_token"):
                listener.enterNew_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNew_token"):
                listener.exitNew_token(self)




    def new_token(self):

        localctx = MParser.New_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_new_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2013
            localctx.i1 = self.match(MParser.VARIABLE_IDENTIFIER)
            self.state = 2014
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
            super(MParser.Key_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MParser.RULE_key_token

        def enterRule(self, listener):
            if hasattr(listener, "enterKey_token"):
                listener.enterKey_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitKey_token"):
                listener.exitKey_token(self)




    def key_token(self):

        localctx = MParser.Key_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 306, self.RULE_key_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2016
            localctx.i1 = self.match(MParser.VARIABLE_IDENTIFIER)
            self.state = 2017
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
            super(MParser.Module_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MParser.RULE_module_token

        def enterRule(self, listener):
            if hasattr(listener, "enterModule_token"):
                listener.enterModule_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitModule_token"):
                listener.exitModule_token(self)




    def module_token(self):

        localctx = MParser.Module_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 308, self.RULE_module_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2019
            localctx.i1 = self.match(MParser.VARIABLE_IDENTIFIER)
            self.state = 2020
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
            super(MParser.Value_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MParser.RULE_value_token

        def enterRule(self, listener):
            if hasattr(listener, "enterValue_token"):
                listener.enterValue_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitValue_token"):
                listener.exitValue_token(self)




    def value_token(self):

        localctx = MParser.Value_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 310, self.RULE_value_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2022
            localctx.i1 = self.match(MParser.VARIABLE_IDENTIFIER)
            self.state = 2023
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
            super(MParser.Symbols_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MParser.RULE_symbols_token

        def enterRule(self, listener):
            if hasattr(listener, "enterSymbols_token"):
                listener.enterSymbols_token(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSymbols_token"):
                listener.exitSymbols_token(self)




    def symbols_token(self):

        localctx = MParser.Symbols_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 312, self.RULE_symbols_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2025
            localctx.i1 = self.match(MParser.VARIABLE_IDENTIFIER)
            self.state = 2026
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
            super(MParser.AssignContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(MParser.EQ, 0)

        def getRuleIndex(self):
            return MParser.RULE_assign

        def enterRule(self, listener):
            if hasattr(listener, "enterAssign"):
                listener.enterAssign(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign"):
                listener.exitAssign(self)




    def assign(self):

        localctx = MParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 314, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2028
            self.match(MParser.EQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MultiplyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.MultiplyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(MParser.STAR, 0)

        def getRuleIndex(self):
            return MParser.RULE_multiply

        def enterRule(self, listener):
            if hasattr(listener, "enterMultiply"):
                listener.enterMultiply(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMultiply"):
                listener.exitMultiply(self)




    def multiply(self):

        localctx = MParser.MultiplyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 316, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2030
            self.match(MParser.STAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DivideContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.DivideContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self):
            return self.getToken(MParser.SLASH, 0)

        def getRuleIndex(self):
            return MParser.RULE_divide

        def enterRule(self, listener):
            if hasattr(listener, "enterDivide"):
                listener.enterDivide(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDivide"):
                listener.exitDivide(self)




    def divide(self):

        localctx = MParser.DivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 318, self.RULE_divide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2032
            self.match(MParser.SLASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdivideContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.IdivideContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BSLASH(self):
            return self.getToken(MParser.BSLASH, 0)

        def getRuleIndex(self):
            return MParser.RULE_idivide

        def enterRule(self, listener):
            if hasattr(listener, "enterIdivide"):
                listener.enterIdivide(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIdivide"):
                listener.exitIdivide(self)




    def idivide(self):

        localctx = MParser.IdivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 320, self.RULE_idivide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2034
            self.match(MParser.BSLASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModuloContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.ModuloContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PERCENT(self):
            return self.getToken(MParser.PERCENT, 0)

        def MODULO(self):
            return self.getToken(MParser.MODULO, 0)

        def getRuleIndex(self):
            return MParser.RULE_modulo

        def enterRule(self, listener):
            if hasattr(listener, "enterModulo"):
                listener.enterModulo(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitModulo"):
                listener.exitModulo(self)




    def modulo(self):

        localctx = MParser.ModuloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 322, self.RULE_modulo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2036
            _la = self._input.LA(1)
            if not(_la==MParser.PERCENT or _la==MParser.MODULO):
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

    class Javascript_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Javascript_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_javascript_statement

     
        def copyFrom(self, ctx):
            super(MParser.Javascript_statementContext, self).copyFrom(ctx)



    class JavascriptStatementContext(Javascript_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_statementContext)
            super(MParser.JavascriptStatementContext, self).__init__(parser)
            self.exp = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(MParser.SEMI, 0)
        def javascript_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptStatement"):
                listener.enterJavascriptStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptStatement"):
                listener.exitJavascriptStatement(self)


    class JavascriptReturnStatementContext(Javascript_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_statementContext)
            super(MParser.JavascriptReturnStatementContext, self).__init__(parser)
            self.exp = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(MParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(MParser.SEMI, 0)
        def javascript_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptReturnStatement"):
                listener.enterJavascriptReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptReturnStatement"):
                listener.exitJavascriptReturnStatement(self)



    def javascript_statement(self):

        localctx = MParser.Javascript_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 324, self.RULE_javascript_statement)
        try:
            self.state = 2045
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.RETURN]:
                localctx = MParser.JavascriptReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2038
                self.match(MParser.RETURN)
                self.state = 2039
                localctx.exp = self.javascript_expression(0)
                self.state = 2040
                self.match(MParser.SEMI)
                pass
            elif token in [MParser.LPAR, MParser.LBRAK, MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.VERSION, MParser.UUID, MParser.HTML, MParser.NONE, MParser.NULL, MParser.READ, MParser.SELF, MParser.TEST, MParser.THIS, MParser.WRITE, MParser.BOOLEAN_LITERAL, MParser.CHAR_LITERAL, MParser.SYMBOL_IDENTIFIER, MParser.TYPE_IDENTIFIER, MParser.VARIABLE_IDENTIFIER, MParser.DOLLAR_IDENTIFIER, MParser.TEXT_LITERAL, MParser.INTEGER_LITERAL, MParser.DECIMAL_LITERAL]:
                localctx = MParser.JavascriptStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2042
                localctx.exp = self.javascript_expression(0)
                self.state = 2043
                self.match(MParser.SEMI)
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
            super(MParser.Javascript_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_javascript_expression

     
        def copyFrom(self, ctx):
            super(MParser.Javascript_expressionContext, self).copyFrom(ctx)


    class JavascriptSelectorExpressionContext(Javascript_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_expressionContext)
            super(MParser.JavascriptSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Javascript_expressionContext
            self.child = None # Javascript_selector_expressionContext
            self.copyFrom(ctx)

        def javascript_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_expressionContext,0)

        def javascript_selector_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_selector_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptSelectorExpression"):
                listener.enterJavascriptSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptSelectorExpression"):
                listener.exitJavascriptSelectorExpression(self)


    class JavascriptPrimaryExpressionContext(Javascript_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_expressionContext)
            super(MParser.JavascriptPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_primary_expressionContext
            self.copyFrom(ctx)

        def javascript_primary_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_primary_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptPrimaryExpression"):
                listener.enterJavascriptPrimaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptPrimaryExpression"):
                listener.exitJavascriptPrimaryExpression(self)



    def javascript_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Javascript_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 326
        self.enterRecursionRule(localctx, 326, self.RULE_javascript_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.JavascriptPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2048
            localctx.exp = self.javascript_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2054
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,158,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.JavascriptSelectorExpressionContext(self, MParser.Javascript_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_expression)
                    self.state = 2050
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2051
                    localctx.child = self.javascript_selector_expression() 
                self.state = 2056
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,158,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Javascript_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Javascript_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def javascript_this_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_this_expressionContext,0)


        def javascript_new_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_new_expressionContext,0)


        def javascript_parenthesis_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_parenthesis_expressionContext,0)


        def javascript_identifier_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_identifier_expressionContext,0)


        def javascript_literal_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_literal_expressionContext,0)


        def javascript_method_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_method_expressionContext,0)


        def javascript_item_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_item_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_javascript_primary_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_primary_expression"):
                listener.enterJavascript_primary_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_primary_expression"):
                listener.exitJavascript_primary_expression(self)




    def javascript_primary_expression(self):

        localctx = MParser.Javascript_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 328, self.RULE_javascript_primary_expression)
        try:
            self.state = 2064
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,159,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2057
                self.javascript_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2058
                self.javascript_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2059
                self.javascript_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2060
                self.javascript_identifier_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2061
                self.javascript_literal_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2062
                self.javascript_method_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 2063
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
            super(MParser.Javascript_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(MParser.This_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_javascript_this_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_this_expression"):
                listener.enterJavascript_this_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_this_expression"):
                listener.exitJavascript_this_expression(self)




    def javascript_this_expression(self):

        localctx = MParser.Javascript_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 330, self.RULE_javascript_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2066
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
            super(MParser.Javascript_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(MParser.New_tokenContext,0)


        def javascript_method_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_method_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_javascript_new_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_new_expression"):
                listener.enterJavascript_new_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_new_expression"):
                listener.exitJavascript_new_expression(self)




    def javascript_new_expression(self):

        localctx = MParser.Javascript_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 332, self.RULE_javascript_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2068
            self.new_token()
            self.state = 2069
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
            super(MParser.Javascript_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_javascript_selector_expression

     
        def copyFrom(self, ctx):
            super(MParser.Javascript_selector_expressionContext, self).copyFrom(ctx)



    class JavaScriptMemberExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_selector_expressionContext)
            super(MParser.JavaScriptMemberExpressionContext, self).__init__(parser)
            self.name = None # Javascript_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def javascript_identifier(self):
            return self.getTypedRuleContext(MParser.Javascript_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaScriptMemberExpression"):
                listener.enterJavaScriptMemberExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptMemberExpression"):
                listener.exitJavaScriptMemberExpression(self)


    class JavaScriptItemExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_selector_expressionContext)
            super(MParser.JavaScriptItemExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_item_expressionContext
            self.copyFrom(ctx)

        def javascript_item_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_item_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaScriptItemExpression"):
                listener.enterJavaScriptItemExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptItemExpression"):
                listener.exitJavaScriptItemExpression(self)


    class JavaScriptMethodExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_selector_expressionContext)
            super(MParser.JavaScriptMethodExpressionContext, self).__init__(parser)
            self.method = None # Javascript_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def javascript_method_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaScriptMethodExpression"):
                listener.enterJavaScriptMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaScriptMethodExpression"):
                listener.exitJavaScriptMethodExpression(self)



    def javascript_selector_expression(self):

        localctx = MParser.Javascript_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 334, self.RULE_javascript_selector_expression)
        try:
            self.state = 2076
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,160,self._ctx)
            if la_ == 1:
                localctx = MParser.JavaScriptMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2071
                self.match(MParser.DOT)
                self.state = 2072
                localctx.method = self.javascript_method_expression()
                pass

            elif la_ == 2:
                localctx = MParser.JavaScriptMemberExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2073
                self.match(MParser.DOT)
                self.state = 2074
                localctx.name = self.javascript_identifier()
                pass

            elif la_ == 3:
                localctx = MParser.JavaScriptItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2075
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
            super(MParser.Javascript_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Javascript_identifierContext
            self.args = None # Javascript_argumentsContext

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def javascript_identifier(self):
            return self.getTypedRuleContext(MParser.Javascript_identifierContext,0)


        def javascript_arguments(self):
            return self.getTypedRuleContext(MParser.Javascript_argumentsContext,0)


        def getRuleIndex(self):
            return MParser.RULE_javascript_method_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_method_expression"):
                listener.enterJavascript_method_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_method_expression"):
                listener.exitJavascript_method_expression(self)




    def javascript_method_expression(self):

        localctx = MParser.Javascript_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 336, self.RULE_javascript_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2078
            localctx.name = self.javascript_identifier()
            self.state = 2079
            self.match(MParser.LPAR)
            self.state = 2081
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & ((1 << (MParser.LPAR - 20)) | (1 << (MParser.LBRAK - 20)) | (1 << (MParser.BOOLEAN - 20)) | (1 << (MParser.CHARACTER - 20)) | (1 << (MParser.TEXT - 20)) | (1 << (MParser.INTEGER - 20)) | (1 << (MParser.DECIMAL - 20)) | (1 << (MParser.DATE - 20)) | (1 << (MParser.TIME - 20)) | (1 << (MParser.DATETIME - 20)) | (1 << (MParser.PERIOD - 20)) | (1 << (MParser.VERSION - 20)) | (1 << (MParser.UUID - 20)) | (1 << (MParser.HTML - 20)))) != 0) or ((((_la - 122)) & ~0x3f) == 0 and ((1 << (_la - 122)) & ((1 << (MParser.NONE - 122)) | (1 << (MParser.NULL - 122)) | (1 << (MParser.READ - 122)) | (1 << (MParser.SELF - 122)) | (1 << (MParser.TEST - 122)) | (1 << (MParser.THIS - 122)) | (1 << (MParser.WRITE - 122)) | (1 << (MParser.BOOLEAN_LITERAL - 122)) | (1 << (MParser.CHAR_LITERAL - 122)) | (1 << (MParser.SYMBOL_IDENTIFIER - 122)) | (1 << (MParser.TYPE_IDENTIFIER - 122)) | (1 << (MParser.VARIABLE_IDENTIFIER - 122)) | (1 << (MParser.DOLLAR_IDENTIFIER - 122)) | (1 << (MParser.TEXT_LITERAL - 122)) | (1 << (MParser.INTEGER_LITERAL - 122)) | (1 << (MParser.DECIMAL_LITERAL - 122)))) != 0):
                self.state = 2080
                localctx.args = self.javascript_arguments(0)


            self.state = 2083
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Javascript_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_javascript_arguments

     
        def copyFrom(self, ctx):
            super(MParser.Javascript_argumentsContext, self).copyFrom(ctx)


    class JavascriptArgumentListContext(Javascript_argumentsContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_argumentsContext)
            super(MParser.JavascriptArgumentListContext, self).__init__(parser)
            self.item = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def javascript_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptArgumentList"):
                listener.enterJavascriptArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptArgumentList"):
                listener.exitJavascriptArgumentList(self)


    class JavascriptArgumentListItemContext(Javascript_argumentsContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_argumentsContext)
            super(MParser.JavascriptArgumentListItemContext, self).__init__(parser)
            self.items = None # Javascript_argumentsContext
            self.item = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)
        def javascript_arguments(self):
            return self.getTypedRuleContext(MParser.Javascript_argumentsContext,0)

        def javascript_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptArgumentListItem"):
                listener.enterJavascriptArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptArgumentListItem"):
                listener.exitJavascriptArgumentListItem(self)



    def javascript_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Javascript_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 338
        self.enterRecursionRule(localctx, 338, self.RULE_javascript_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.JavascriptArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2086
            localctx.item = self.javascript_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2093
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,162,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.JavascriptArgumentListItemContext(self, MParser.Javascript_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_arguments)
                    self.state = 2088
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2089
                    self.match(MParser.COMMA)
                    self.state = 2090
                    localctx.item = self.javascript_expression(0) 
                self.state = 2095
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,162,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Javascript_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Javascript_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Javascript_expressionContext

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)

        def javascript_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_javascript_item_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_item_expression"):
                listener.enterJavascript_item_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_item_expression"):
                listener.exitJavascript_item_expression(self)




    def javascript_item_expression(self):

        localctx = MParser.Javascript_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 340, self.RULE_javascript_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2096
            self.match(MParser.LBRAK)
            self.state = 2097
            localctx.exp = self.javascript_expression(0)
            self.state = 2098
            self.match(MParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Javascript_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Javascript_expressionContext

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def javascript_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_javascript_parenthesis_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_parenthesis_expression"):
                listener.enterJavascript_parenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_parenthesis_expression"):
                listener.exitJavascript_parenthesis_expression(self)




    def javascript_parenthesis_expression(self):

        localctx = MParser.Javascript_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 342, self.RULE_javascript_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2100
            self.match(MParser.LPAR)
            self.state = 2101
            localctx.exp = self.javascript_expression(0)
            self.state = 2102
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Javascript_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Javascript_identifierContext

        def javascript_identifier(self):
            return self.getTypedRuleContext(MParser.Javascript_identifierContext,0)


        def getRuleIndex(self):
            return MParser.RULE_javascript_identifier_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_identifier_expression"):
                listener.enterJavascript_identifier_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_identifier_expression"):
                listener.exitJavascript_identifier_expression(self)




    def javascript_identifier_expression(self):

        localctx = MParser.Javascript_identifier_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 344, self.RULE_javascript_identifier_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2104
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
            super(MParser.Javascript_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_javascript_literal_expression

     
        def copyFrom(self, ctx):
            super(MParser.Javascript_literal_expressionContext, self).copyFrom(ctx)



    class JavascriptIntegerLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_literal_expressionContext)
            super(MParser.JavascriptIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(MParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptIntegerLiteral"):
                listener.enterJavascriptIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptIntegerLiteral"):
                listener.exitJavascriptIntegerLiteral(self)


    class JavascriptBooleanLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_literal_expressionContext)
            super(MParser.JavascriptBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(MParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptBooleanLiteral"):
                listener.enterJavascriptBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptBooleanLiteral"):
                listener.exitJavascriptBooleanLiteral(self)


    class JavascriptCharacterLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_literal_expressionContext)
            super(MParser.JavascriptCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(MParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptCharacterLiteral"):
                listener.enterJavascriptCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptCharacterLiteral"):
                listener.exitJavascriptCharacterLiteral(self)


    class JavascriptTextLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_literal_expressionContext)
            super(MParser.JavascriptTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(MParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptTextLiteral"):
                listener.enterJavascriptTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptTextLiteral"):
                listener.exitJavascriptTextLiteral(self)


    class JavascriptDecimalLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_literal_expressionContext)
            super(MParser.JavascriptDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(MParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascriptDecimalLiteral"):
                listener.enterJavascriptDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascriptDecimalLiteral"):
                listener.exitJavascriptDecimalLiteral(self)



    def javascript_literal_expression(self):

        localctx = MParser.Javascript_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 346, self.RULE_javascript_literal_expression)
        try:
            self.state = 2111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.INTEGER_LITERAL]:
                localctx = MParser.JavascriptIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2106
                localctx.t = self.match(MParser.INTEGER_LITERAL)
                pass
            elif token in [MParser.DECIMAL_LITERAL]:
                localctx = MParser.JavascriptDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2107
                localctx.t = self.match(MParser.DECIMAL_LITERAL)
                pass
            elif token in [MParser.TEXT_LITERAL]:
                localctx = MParser.JavascriptTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2108
                localctx.t = self.match(MParser.TEXT_LITERAL)
                pass
            elif token in [MParser.BOOLEAN_LITERAL]:
                localctx = MParser.JavascriptBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2109
                localctx.t = self.match(MParser.BOOLEAN_LITERAL)
                pass
            elif token in [MParser.CHAR_LITERAL]:
                localctx = MParser.JavascriptCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2110
                localctx.t = self.match(MParser.CHAR_LITERAL)
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
            super(MParser.Javascript_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(MParser.SYMBOL_IDENTIFIER, 0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(MParser.DOLLAR_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(MParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(MParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(MParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(MParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(MParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(MParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(MParser.DATE, 0)

        def TIME(self):
            return self.getToken(MParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(MParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(MParser.PERIOD, 0)

        def VERSION(self):
            return self.getToken(MParser.VERSION, 0)

        def UUID(self):
            return self.getToken(MParser.UUID, 0)

        def HTML(self):
            return self.getToken(MParser.HTML, 0)

        def READ(self):
            return self.getToken(MParser.READ, 0)

        def WRITE(self):
            return self.getToken(MParser.WRITE, 0)

        def TEST(self):
            return self.getToken(MParser.TEST, 0)

        def SELF(self):
            return self.getToken(MParser.SELF, 0)

        def NONE(self):
            return self.getToken(MParser.NONE, 0)

        def NULL(self):
            return self.getToken(MParser.NULL, 0)

        def getRuleIndex(self):
            return MParser.RULE_javascript_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterJavascript_identifier"):
                listener.enterJavascript_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavascript_identifier"):
                listener.exitJavascript_identifier(self)




    def javascript_identifier(self):

        localctx = MParser.Javascript_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 348, self.RULE_javascript_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2113
            _la = self._input.LA(1)
            if not(((((_la - 50)) & ~0x3f) == 0 and ((1 << (_la - 50)) & ((1 << (MParser.BOOLEAN - 50)) | (1 << (MParser.CHARACTER - 50)) | (1 << (MParser.TEXT - 50)) | (1 << (MParser.INTEGER - 50)) | (1 << (MParser.DECIMAL - 50)) | (1 << (MParser.DATE - 50)) | (1 << (MParser.TIME - 50)) | (1 << (MParser.DATETIME - 50)) | (1 << (MParser.PERIOD - 50)) | (1 << (MParser.VERSION - 50)) | (1 << (MParser.UUID - 50)) | (1 << (MParser.HTML - 50)))) != 0) or ((((_la - 122)) & ~0x3f) == 0 and ((1 << (_la - 122)) & ((1 << (MParser.NONE - 122)) | (1 << (MParser.NULL - 122)) | (1 << (MParser.READ - 122)) | (1 << (MParser.SELF - 122)) | (1 << (MParser.TEST - 122)) | (1 << (MParser.WRITE - 122)) | (1 << (MParser.SYMBOL_IDENTIFIER - 122)) | (1 << (MParser.TYPE_IDENTIFIER - 122)) | (1 << (MParser.VARIABLE_IDENTIFIER - 122)) | (1 << (MParser.DOLLAR_IDENTIFIER - 122)))) != 0)):
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
            super(MParser.Python_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_python_statement

     
        def copyFrom(self, ctx):
            super(MParser.Python_statementContext, self).copyFrom(ctx)



    class PythonStatementContext(Python_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_statementContext)
            super(MParser.PythonStatementContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(MParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonStatement"):
                listener.enterPythonStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonStatement"):
                listener.exitPythonStatement(self)


    class PythonReturnStatementContext(Python_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_statementContext)
            super(MParser.PythonReturnStatementContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(MParser.RETURN, 0)
        def python_expression(self):
            return self.getTypedRuleContext(MParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonReturnStatement"):
                listener.enterPythonReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonReturnStatement"):
                listener.exitPythonReturnStatement(self)



    def python_statement(self):

        localctx = MParser.Python_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 350, self.RULE_python_statement)
        try:
            self.state = 2118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.RETURN]:
                localctx = MParser.PythonReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2115
                self.match(MParser.RETURN)
                self.state = 2116
                localctx.exp = self.python_expression(0)
                pass
            elif token in [MParser.LPAR, MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.VERSION, MParser.UUID, MParser.HTML, MParser.NONE, MParser.NULL, MParser.READ, MParser.SELF, MParser.TEST, MParser.THIS, MParser.WRITE, MParser.BOOLEAN_LITERAL, MParser.CHAR_LITERAL, MParser.SYMBOL_IDENTIFIER, MParser.TYPE_IDENTIFIER, MParser.VARIABLE_IDENTIFIER, MParser.DOLLAR_IDENTIFIER, MParser.TEXT_LITERAL, MParser.INTEGER_LITERAL, MParser.DECIMAL_LITERAL]:
                localctx = MParser.PythonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2117
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
            super(MParser.Python_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_python_expression

     
        def copyFrom(self, ctx):
            super(MParser.Python_expressionContext, self).copyFrom(ctx)


    class PythonSelectorExpressionContext(Python_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_expressionContext)
            super(MParser.PythonSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Python_expressionContext
            self.child = None # Python_selector_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(MParser.Python_expressionContext,0)

        def python_selector_expression(self):
            return self.getTypedRuleContext(MParser.Python_selector_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonSelectorExpression"):
                listener.enterPythonSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonSelectorExpression"):
                listener.exitPythonSelectorExpression(self)


    class PythonPrimaryExpressionContext(Python_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_expressionContext)
            super(MParser.PythonPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Python_primary_expressionContext
            self.copyFrom(ctx)

        def python_primary_expression(self):
            return self.getTypedRuleContext(MParser.Python_primary_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonPrimaryExpression"):
                listener.enterPythonPrimaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonPrimaryExpression"):
                listener.exitPythonPrimaryExpression(self)



    def python_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Python_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 352
        self.enterRecursionRule(localctx, 352, self.RULE_python_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.PythonPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2121
            localctx.exp = self.python_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2127
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,165,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.PythonSelectorExpressionContext(self, MParser.Python_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_expression)
                    self.state = 2123
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2124
                    localctx.child = self.python_selector_expression() 
                self.state = 2129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,165,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Python_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_python_primary_expression

     
        def copyFrom(self, ctx):
            super(MParser.Python_primary_expressionContext, self).copyFrom(ctx)



    class PythonParenthesisExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_primary_expressionContext)
            super(MParser.PythonParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Python_parenthesis_expressionContext
            self.copyFrom(ctx)

        def python_parenthesis_expression(self):
            return self.getTypedRuleContext(MParser.Python_parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonParenthesisExpression"):
                listener.enterPythonParenthesisExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonParenthesisExpression"):
                listener.exitPythonParenthesisExpression(self)


    class PythonIdentifierExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_primary_expressionContext)
            super(MParser.PythonIdentifierExpressionContext, self).__init__(parser)
            self.exp = None # Python_identifier_expressionContext
            self.copyFrom(ctx)

        def python_identifier_expression(self):
            return self.getTypedRuleContext(MParser.Python_identifier_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonIdentifierExpression"):
                listener.enterPythonIdentifierExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonIdentifierExpression"):
                listener.exitPythonIdentifierExpression(self)


    class PythonSelfExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_primary_expressionContext)
            super(MParser.PythonSelfExpressionContext, self).__init__(parser)
            self.exp = None # Python_self_expressionContext
            self.copyFrom(ctx)

        def python_self_expression(self):
            return self.getTypedRuleContext(MParser.Python_self_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonSelfExpression"):
                listener.enterPythonSelfExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonSelfExpression"):
                listener.exitPythonSelfExpression(self)


    class PythonLiteralExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_primary_expressionContext)
            super(MParser.PythonLiteralExpressionContext, self).__init__(parser)
            self.exp = None # Python_literal_expressionContext
            self.copyFrom(ctx)

        def python_literal_expression(self):
            return self.getTypedRuleContext(MParser.Python_literal_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonLiteralExpression"):
                listener.enterPythonLiteralExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonLiteralExpression"):
                listener.exitPythonLiteralExpression(self)


    class PythonGlobalMethodExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_primary_expressionContext)
            super(MParser.PythonGlobalMethodExpressionContext, self).__init__(parser)
            self.exp = None # Python_method_expressionContext
            self.copyFrom(ctx)

        def python_method_expression(self):
            return self.getTypedRuleContext(MParser.Python_method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonGlobalMethodExpression"):
                listener.enterPythonGlobalMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonGlobalMethodExpression"):
                listener.exitPythonGlobalMethodExpression(self)



    def python_primary_expression(self):

        localctx = MParser.Python_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 354, self.RULE_python_primary_expression)
        try:
            self.state = 2135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,166,self._ctx)
            if la_ == 1:
                localctx = MParser.PythonSelfExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2130
                localctx.exp = self.python_self_expression()
                pass

            elif la_ == 2:
                localctx = MParser.PythonParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2131
                localctx.exp = self.python_parenthesis_expression()
                pass

            elif la_ == 3:
                localctx = MParser.PythonIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2132
                localctx.exp = self.python_identifier_expression(0)
                pass

            elif la_ == 4:
                localctx = MParser.PythonLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2133
                localctx.exp = self.python_literal_expression()
                pass

            elif la_ == 5:
                localctx = MParser.PythonGlobalMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2134
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
            super(MParser.Python_self_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(MParser.This_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_python_self_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_self_expression"):
                listener.enterPython_self_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_self_expression"):
                listener.exitPython_self_expression(self)




    def python_self_expression(self):

        localctx = MParser.Python_self_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 356, self.RULE_python_self_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2137
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
            super(MParser.Python_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_python_selector_expression

     
        def copyFrom(self, ctx):
            super(MParser.Python_selector_expressionContext, self).copyFrom(ctx)



    class PythonMethodExpressionContext(Python_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_selector_expressionContext)
            super(MParser.PythonMethodExpressionContext, self).__init__(parser)
            self.exp = None # Python_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def python_method_expression(self):
            return self.getTypedRuleContext(MParser.Python_method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonMethodExpression"):
                listener.enterPythonMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonMethodExpression"):
                listener.exitPythonMethodExpression(self)


    class PythonItemExpressionContext(Python_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_selector_expressionContext)
            super(MParser.PythonItemExpressionContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)
        def python_expression(self):
            return self.getTypedRuleContext(MParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonItemExpression"):
                listener.enterPythonItemExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonItemExpression"):
                listener.exitPythonItemExpression(self)



    def python_selector_expression(self):

        localctx = MParser.Python_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 358, self.RULE_python_selector_expression)
        try:
            self.state = 2145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.DOT]:
                localctx = MParser.PythonMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2139
                self.match(MParser.DOT)
                self.state = 2140
                localctx.exp = self.python_method_expression()
                pass
            elif token in [MParser.LBRAK]:
                localctx = MParser.PythonItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2141
                self.match(MParser.LBRAK)
                self.state = 2142
                localctx.exp = self.python_expression(0)
                self.state = 2143
                self.match(MParser.RBRAK)
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
            super(MParser.Python_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Python_identifierContext
            self.args = None # Python_argument_listContext

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def python_identifier(self):
            return self.getTypedRuleContext(MParser.Python_identifierContext,0)


        def python_argument_list(self):
            return self.getTypedRuleContext(MParser.Python_argument_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_python_method_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_method_expression"):
                listener.enterPython_method_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_method_expression"):
                listener.exitPython_method_expression(self)




    def python_method_expression(self):

        localctx = MParser.Python_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 360, self.RULE_python_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2147
            localctx.name = self.python_identifier()
            self.state = 2148
            self.match(MParser.LPAR)
            self.state = 2150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & ((1 << (MParser.LPAR - 20)) | (1 << (MParser.BOOLEAN - 20)) | (1 << (MParser.CHARACTER - 20)) | (1 << (MParser.TEXT - 20)) | (1 << (MParser.INTEGER - 20)) | (1 << (MParser.DECIMAL - 20)) | (1 << (MParser.DATE - 20)) | (1 << (MParser.TIME - 20)) | (1 << (MParser.DATETIME - 20)) | (1 << (MParser.PERIOD - 20)) | (1 << (MParser.VERSION - 20)) | (1 << (MParser.UUID - 20)) | (1 << (MParser.HTML - 20)))) != 0) or ((((_la - 122)) & ~0x3f) == 0 and ((1 << (_la - 122)) & ((1 << (MParser.NONE - 122)) | (1 << (MParser.NULL - 122)) | (1 << (MParser.READ - 122)) | (1 << (MParser.SELF - 122)) | (1 << (MParser.TEST - 122)) | (1 << (MParser.THIS - 122)) | (1 << (MParser.WRITE - 122)) | (1 << (MParser.BOOLEAN_LITERAL - 122)) | (1 << (MParser.CHAR_LITERAL - 122)) | (1 << (MParser.SYMBOL_IDENTIFIER - 122)) | (1 << (MParser.TYPE_IDENTIFIER - 122)) | (1 << (MParser.VARIABLE_IDENTIFIER - 122)) | (1 << (MParser.DOLLAR_IDENTIFIER - 122)) | (1 << (MParser.TEXT_LITERAL - 122)) | (1 << (MParser.INTEGER_LITERAL - 122)) | (1 << (MParser.DECIMAL_LITERAL - 122)))) != 0):
                self.state = 2149
                localctx.args = self.python_argument_list()


            self.state = 2152
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Python_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_python_argument_list

     
        def copyFrom(self, ctx):
            super(MParser.Python_argument_listContext, self).copyFrom(ctx)



    class PythonOrdinalOnlyArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_argument_listContext)
            super(MParser.PythonOrdinalOnlyArgumentListContext, self).__init__(parser)
            self.ordinal = None # Python_ordinal_argument_listContext
            self.copyFrom(ctx)

        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(MParser.Python_ordinal_argument_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonOrdinalOnlyArgumentList"):
                listener.enterPythonOrdinalOnlyArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonOrdinalOnlyArgumentList"):
                listener.exitPythonOrdinalOnlyArgumentList(self)


    class PythonNamedOnlyArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_argument_listContext)
            super(MParser.PythonNamedOnlyArgumentListContext, self).__init__(parser)
            self.named = None # Python_named_argument_listContext
            self.copyFrom(ctx)

        def python_named_argument_list(self):
            return self.getTypedRuleContext(MParser.Python_named_argument_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonNamedOnlyArgumentList"):
                listener.enterPythonNamedOnlyArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonNamedOnlyArgumentList"):
                listener.exitPythonNamedOnlyArgumentList(self)


    class PythonArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_argument_listContext)
            super(MParser.PythonArgumentListContext, self).__init__(parser)
            self.ordinal = None # Python_ordinal_argument_listContext
            self.named = None # Python_named_argument_listContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)
        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(MParser.Python_ordinal_argument_listContext,0)

        def python_named_argument_list(self):
            return self.getTypedRuleContext(MParser.Python_named_argument_listContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonArgumentList"):
                listener.enterPythonArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonArgumentList"):
                listener.exitPythonArgumentList(self)



    def python_argument_list(self):

        localctx = MParser.Python_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 362, self.RULE_python_argument_list)
        try:
            self.state = 2160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,169,self._ctx)
            if la_ == 1:
                localctx = MParser.PythonOrdinalOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2154
                localctx.ordinal = self.python_ordinal_argument_list(0)
                pass

            elif la_ == 2:
                localctx = MParser.PythonNamedOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2155
                localctx.named = self.python_named_argument_list(0)
                pass

            elif la_ == 3:
                localctx = MParser.PythonArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2156
                localctx.ordinal = self.python_ordinal_argument_list(0)
                self.state = 2157
                self.match(MParser.COMMA)
                self.state = 2158
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
            super(MParser.Python_ordinal_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_python_ordinal_argument_list

     
        def copyFrom(self, ctx):
            super(MParser.Python_ordinal_argument_listContext, self).copyFrom(ctx)


    class PythonOrdinalArgumentListContext(Python_ordinal_argument_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_ordinal_argument_listContext)
            super(MParser.PythonOrdinalArgumentListContext, self).__init__(parser)
            self.item = None # Python_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(MParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonOrdinalArgumentList"):
                listener.enterPythonOrdinalArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonOrdinalArgumentList"):
                listener.exitPythonOrdinalArgumentList(self)


    class PythonOrdinalArgumentListItemContext(Python_ordinal_argument_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_ordinal_argument_listContext)
            super(MParser.PythonOrdinalArgumentListItemContext, self).__init__(parser)
            self.items = None # Python_ordinal_argument_listContext
            self.item = None # Python_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)
        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(MParser.Python_ordinal_argument_listContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(MParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonOrdinalArgumentListItem"):
                listener.enterPythonOrdinalArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonOrdinalArgumentListItem"):
                listener.exitPythonOrdinalArgumentListItem(self)



    def python_ordinal_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Python_ordinal_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 364
        self.enterRecursionRule(localctx, 364, self.RULE_python_ordinal_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.PythonOrdinalArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2163
            localctx.item = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2170
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,170,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.PythonOrdinalArgumentListItemContext(self, MParser.Python_ordinal_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_ordinal_argument_list)
                    self.state = 2165
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2166
                    self.match(MParser.COMMA)
                    self.state = 2167
                    localctx.item = self.python_expression(0) 
                self.state = 2172
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,170,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_named_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Python_named_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_python_named_argument_list

     
        def copyFrom(self, ctx):
            super(MParser.Python_named_argument_listContext, self).copyFrom(ctx)


    class PythonNamedArgumentListContext(Python_named_argument_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_named_argument_listContext)
            super(MParser.PythonNamedArgumentListContext, self).__init__(parser)
            self.name = None # Python_identifierContext
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def EQ(self):
            return self.getToken(MParser.EQ, 0)
        def python_identifier(self):
            return self.getTypedRuleContext(MParser.Python_identifierContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(MParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonNamedArgumentList"):
                listener.enterPythonNamedArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonNamedArgumentList"):
                listener.exitPythonNamedArgumentList(self)


    class PythonNamedArgumentListItemContext(Python_named_argument_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_named_argument_listContext)
            super(MParser.PythonNamedArgumentListItemContext, self).__init__(parser)
            self.items = None # Python_named_argument_listContext
            self.name = None # Python_identifierContext
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)
        def EQ(self):
            return self.getToken(MParser.EQ, 0)
        def python_named_argument_list(self):
            return self.getTypedRuleContext(MParser.Python_named_argument_listContext,0)

        def python_identifier(self):
            return self.getTypedRuleContext(MParser.Python_identifierContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(MParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonNamedArgumentListItem"):
                listener.enterPythonNamedArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonNamedArgumentListItem"):
                listener.exitPythonNamedArgumentListItem(self)



    def python_named_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Python_named_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 366
        self.enterRecursionRule(localctx, 366, self.RULE_python_named_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.PythonNamedArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2174
            localctx.name = self.python_identifier()
            self.state = 2175
            self.match(MParser.EQ)
            self.state = 2176
            localctx.exp = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,171,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.PythonNamedArgumentListItemContext(self, MParser.Python_named_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_named_argument_list)
                    self.state = 2178
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2179
                    self.match(MParser.COMMA)
                    self.state = 2180
                    localctx.name = self.python_identifier()
                    self.state = 2181
                    self.match(MParser.EQ)
                    self.state = 2182
                    localctx.exp = self.python_expression(0) 
                self.state = 2188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,171,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Python_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Python_expressionContext

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def python_expression(self):
            return self.getTypedRuleContext(MParser.Python_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_python_parenthesis_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_parenthesis_expression"):
                listener.enterPython_parenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_parenthesis_expression"):
                listener.exitPython_parenthesis_expression(self)




    def python_parenthesis_expression(self):

        localctx = MParser.Python_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 368, self.RULE_python_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2189
            self.match(MParser.LPAR)
            self.state = 2190
            localctx.exp = self.python_expression(0)
            self.state = 2191
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Python_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_python_identifier_expression

     
        def copyFrom(self, ctx):
            super(MParser.Python_identifier_expressionContext, self).copyFrom(ctx)


    class PythonChildIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_identifier_expressionContext)
            super(MParser.PythonChildIdentifierContext, self).__init__(parser)
            self.parent = None # Python_identifier_expressionContext
            self.name = None # Python_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def python_identifier_expression(self):
            return self.getTypedRuleContext(MParser.Python_identifier_expressionContext,0)

        def python_identifier(self):
            return self.getTypedRuleContext(MParser.Python_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonChildIdentifier"):
                listener.enterPythonChildIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonChildIdentifier"):
                listener.exitPythonChildIdentifier(self)


    class PythonPromptoIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_identifier_expressionContext)
            super(MParser.PythonPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(MParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonPromptoIdentifier"):
                listener.enterPythonPromptoIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonPromptoIdentifier"):
                listener.exitPythonPromptoIdentifier(self)


    class PythonIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_identifier_expressionContext)
            super(MParser.PythonIdentifierContext, self).__init__(parser)
            self.name = None # Python_identifierContext
            self.copyFrom(ctx)

        def python_identifier(self):
            return self.getTypedRuleContext(MParser.Python_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPythonIdentifier"):
                listener.enterPythonIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonIdentifier"):
                listener.exitPythonIdentifier(self)



    def python_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Python_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 370
        self.enterRecursionRule(localctx, 370, self.RULE_python_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.DOLLAR_IDENTIFIER]:
                localctx = MParser.PythonPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2194
                self.match(MParser.DOLLAR_IDENTIFIER)
                pass
            elif token in [MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.VERSION, MParser.UUID, MParser.HTML, MParser.NONE, MParser.NULL, MParser.READ, MParser.TEST, MParser.THIS, MParser.WRITE, MParser.SYMBOL_IDENTIFIER, MParser.TYPE_IDENTIFIER, MParser.VARIABLE_IDENTIFIER]:
                localctx = MParser.PythonIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2195
                localctx.name = self.python_identifier()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2203
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,173,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.PythonChildIdentifierContext(self, MParser.Python_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_identifier_expression)
                    self.state = 2198
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2199
                    self.match(MParser.DOT)
                    self.state = 2200
                    localctx.name = self.python_identifier() 
                self.state = 2205
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,173,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Python_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_python_literal_expression

     
        def copyFrom(self, ctx):
            super(MParser.Python_literal_expressionContext, self).copyFrom(ctx)



    class PythonIntegerLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_literal_expressionContext)
            super(MParser.PythonIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(MParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonIntegerLiteral"):
                listener.enterPythonIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonIntegerLiteral"):
                listener.exitPythonIntegerLiteral(self)


    class PythonBooleanLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_literal_expressionContext)
            super(MParser.PythonBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(MParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonBooleanLiteral"):
                listener.enterPythonBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonBooleanLiteral"):
                listener.exitPythonBooleanLiteral(self)


    class PythonCharacterLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_literal_expressionContext)
            super(MParser.PythonCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(MParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonCharacterLiteral"):
                listener.enterPythonCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonCharacterLiteral"):
                listener.exitPythonCharacterLiteral(self)


    class PythonTextLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_literal_expressionContext)
            super(MParser.PythonTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(MParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonTextLiteral"):
                listener.enterPythonTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonTextLiteral"):
                listener.exitPythonTextLiteral(self)


    class PythonDecimalLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_literal_expressionContext)
            super(MParser.PythonDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(MParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterPythonDecimalLiteral"):
                listener.enterPythonDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPythonDecimalLiteral"):
                listener.exitPythonDecimalLiteral(self)



    def python_literal_expression(self):

        localctx = MParser.Python_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 372, self.RULE_python_literal_expression)
        try:
            self.state = 2211
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.INTEGER_LITERAL]:
                localctx = MParser.PythonIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2206
                localctx.t = self.match(MParser.INTEGER_LITERAL)
                pass
            elif token in [MParser.DECIMAL_LITERAL]:
                localctx = MParser.PythonDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2207
                localctx.t = self.match(MParser.DECIMAL_LITERAL)
                pass
            elif token in [MParser.TEXT_LITERAL]:
                localctx = MParser.PythonTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2208
                localctx.t = self.match(MParser.TEXT_LITERAL)
                pass
            elif token in [MParser.BOOLEAN_LITERAL]:
                localctx = MParser.PythonBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2209
                localctx.t = self.match(MParser.BOOLEAN_LITERAL)
                pass
            elif token in [MParser.CHAR_LITERAL]:
                localctx = MParser.PythonCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2210
                localctx.t = self.match(MParser.CHAR_LITERAL)
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
            super(MParser.Python_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(MParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(MParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(MParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(MParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(MParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(MParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(MParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(MParser.DATE, 0)

        def TIME(self):
            return self.getToken(MParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(MParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(MParser.PERIOD, 0)

        def VERSION(self):
            return self.getToken(MParser.VERSION, 0)

        def UUID(self):
            return self.getToken(MParser.UUID, 0)

        def HTML(self):
            return self.getToken(MParser.HTML, 0)

        def READ(self):
            return self.getToken(MParser.READ, 0)

        def WRITE(self):
            return self.getToken(MParser.WRITE, 0)

        def TEST(self):
            return self.getToken(MParser.TEST, 0)

        def THIS(self):
            return self.getToken(MParser.THIS, 0)

        def NONE(self):
            return self.getToken(MParser.NONE, 0)

        def NULL(self):
            return self.getToken(MParser.NULL, 0)

        def getRuleIndex(self):
            return MParser.RULE_python_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterPython_identifier"):
                listener.enterPython_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPython_identifier"):
                listener.exitPython_identifier(self)




    def python_identifier(self):

        localctx = MParser.Python_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 374, self.RULE_python_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2213
            _la = self._input.LA(1)
            if not(((((_la - 50)) & ~0x3f) == 0 and ((1 << (_la - 50)) & ((1 << (MParser.BOOLEAN - 50)) | (1 << (MParser.CHARACTER - 50)) | (1 << (MParser.TEXT - 50)) | (1 << (MParser.INTEGER - 50)) | (1 << (MParser.DECIMAL - 50)) | (1 << (MParser.DATE - 50)) | (1 << (MParser.TIME - 50)) | (1 << (MParser.DATETIME - 50)) | (1 << (MParser.PERIOD - 50)) | (1 << (MParser.VERSION - 50)) | (1 << (MParser.UUID - 50)) | (1 << (MParser.HTML - 50)))) != 0) or ((((_la - 122)) & ~0x3f) == 0 and ((1 << (_la - 122)) & ((1 << (MParser.NONE - 122)) | (1 << (MParser.NULL - 122)) | (1 << (MParser.READ - 122)) | (1 << (MParser.TEST - 122)) | (1 << (MParser.THIS - 122)) | (1 << (MParser.WRITE - 122)) | (1 << (MParser.SYMBOL_IDENTIFIER - 122)) | (1 << (MParser.TYPE_IDENTIFIER - 122)) | (1 << (MParser.VARIABLE_IDENTIFIER - 122)))) != 0)):
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
            super(MParser.Java_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_java_statement

     
        def copyFrom(self, ctx):
            super(MParser.Java_statementContext, self).copyFrom(ctx)



    class JavaReturnStatementContext(Java_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_statementContext)
            super(MParser.JavaReturnStatementContext, self).__init__(parser)
            self.exp = None # Java_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(MParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(MParser.SEMI, 0)
        def java_expression(self):
            return self.getTypedRuleContext(MParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaReturnStatement"):
                listener.enterJavaReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaReturnStatement"):
                listener.exitJavaReturnStatement(self)


    class JavaStatementContext(Java_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_statementContext)
            super(MParser.JavaStatementContext, self).__init__(parser)
            self.exp = None # Java_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(MParser.SEMI, 0)
        def java_expression(self):
            return self.getTypedRuleContext(MParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaStatement"):
                listener.enterJavaStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaStatement"):
                listener.exitJavaStatement(self)



    def java_statement(self):

        localctx = MParser.Java_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 376, self.RULE_java_statement)
        try:
            self.state = 2222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.RETURN]:
                localctx = MParser.JavaReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2215
                self.match(MParser.RETURN)
                self.state = 2216
                localctx.exp = self.java_expression(0)
                self.state = 2217
                self.match(MParser.SEMI)
                pass
            elif token in [MParser.LPAR, MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.VERSION, MParser.UUID, MParser.HTML, MParser.NONE, MParser.NULL, MParser.READ, MParser.SELF, MParser.TEST, MParser.THIS, MParser.WRITE, MParser.BOOLEAN_LITERAL, MParser.CHAR_LITERAL, MParser.SYMBOL_IDENTIFIER, MParser.TYPE_IDENTIFIER, MParser.VARIABLE_IDENTIFIER, MParser.NATIVE_IDENTIFIER, MParser.DOLLAR_IDENTIFIER, MParser.TEXT_LITERAL, MParser.INTEGER_LITERAL, MParser.DECIMAL_LITERAL]:
                localctx = MParser.JavaStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2219
                localctx.exp = self.java_expression(0)
                self.state = 2220
                self.match(MParser.SEMI)
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
            super(MParser.Java_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_java_expression

     
        def copyFrom(self, ctx):
            super(MParser.Java_expressionContext, self).copyFrom(ctx)


    class JavaSelectorExpressionContext(Java_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_expressionContext)
            super(MParser.JavaSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Java_expressionContext
            self.child = None # Java_selector_expressionContext
            self.copyFrom(ctx)

        def java_expression(self):
            return self.getTypedRuleContext(MParser.Java_expressionContext,0)

        def java_selector_expression(self):
            return self.getTypedRuleContext(MParser.Java_selector_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaSelectorExpression"):
                listener.enterJavaSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaSelectorExpression"):
                listener.exitJavaSelectorExpression(self)


    class JavaPrimaryExpressionContext(Java_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_expressionContext)
            super(MParser.JavaPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Java_primary_expressionContext
            self.copyFrom(ctx)

        def java_primary_expression(self):
            return self.getTypedRuleContext(MParser.Java_primary_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaPrimaryExpression"):
                listener.enterJavaPrimaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaPrimaryExpression"):
                listener.exitJavaPrimaryExpression(self)



    def java_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Java_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 378
        self.enterRecursionRule(localctx, 378, self.RULE_java_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.JavaPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2225
            localctx.exp = self.java_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2231
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,176,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.JavaSelectorExpressionContext(self, MParser.Java_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_expression)
                    self.state = 2227
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2228
                    localctx.child = self.java_selector_expression() 
                self.state = 2233
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,176,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Java_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def java_this_expression(self):
            return self.getTypedRuleContext(MParser.Java_this_expressionContext,0)


        def java_new_expression(self):
            return self.getTypedRuleContext(MParser.Java_new_expressionContext,0)


        def java_parenthesis_expression(self):
            return self.getTypedRuleContext(MParser.Java_parenthesis_expressionContext,0)


        def java_identifier_expression(self):
            return self.getTypedRuleContext(MParser.Java_identifier_expressionContext,0)


        def java_literal_expression(self):
            return self.getTypedRuleContext(MParser.Java_literal_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_java_primary_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_primary_expression"):
                listener.enterJava_primary_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_primary_expression"):
                listener.exitJava_primary_expression(self)




    def java_primary_expression(self):

        localctx = MParser.Java_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 380, self.RULE_java_primary_expression)
        try:
            self.state = 2239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,177,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2234
                self.java_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2235
                self.java_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2236
                self.java_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2237
                self.java_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2238
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
            super(MParser.Java_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(MParser.This_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_java_this_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_this_expression"):
                listener.enterJava_this_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_this_expression"):
                listener.exitJava_this_expression(self)




    def java_this_expression(self):

        localctx = MParser.Java_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 382, self.RULE_java_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2241
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
            super(MParser.Java_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(MParser.New_tokenContext,0)


        def java_method_expression(self):
            return self.getTypedRuleContext(MParser.Java_method_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_java_new_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_new_expression"):
                listener.enterJava_new_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_new_expression"):
                listener.exitJava_new_expression(self)




    def java_new_expression(self):

        localctx = MParser.Java_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 384, self.RULE_java_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2243
            self.new_token()
            self.state = 2244
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
            super(MParser.Java_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_java_selector_expression

     
        def copyFrom(self, ctx):
            super(MParser.Java_selector_expressionContext, self).copyFrom(ctx)



    class JavaItemExpressionContext(Java_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_selector_expressionContext)
            super(MParser.JavaItemExpressionContext, self).__init__(parser)
            self.exp = None # Java_item_expressionContext
            self.copyFrom(ctx)

        def java_item_expression(self):
            return self.getTypedRuleContext(MParser.Java_item_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaItemExpression"):
                listener.enterJavaItemExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaItemExpression"):
                listener.exitJavaItemExpression(self)


    class JavaMethodExpressionContext(Java_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_selector_expressionContext)
            super(MParser.JavaMethodExpressionContext, self).__init__(parser)
            self.exp = None # Java_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def java_method_expression(self):
            return self.getTypedRuleContext(MParser.Java_method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaMethodExpression"):
                listener.enterJavaMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaMethodExpression"):
                listener.exitJavaMethodExpression(self)



    def java_selector_expression(self):

        localctx = MParser.Java_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 386, self.RULE_java_selector_expression)
        try:
            self.state = 2249
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.DOT]:
                localctx = MParser.JavaMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2246
                self.match(MParser.DOT)
                self.state = 2247
                localctx.exp = self.java_method_expression()
                pass
            elif token in [MParser.LBRAK]:
                localctx = MParser.JavaItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2248
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
            super(MParser.Java_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Java_identifierContext
            self.args = None # Java_argumentsContext

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def java_identifier(self):
            return self.getTypedRuleContext(MParser.Java_identifierContext,0)


        def java_arguments(self):
            return self.getTypedRuleContext(MParser.Java_argumentsContext,0)


        def getRuleIndex(self):
            return MParser.RULE_java_method_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_method_expression"):
                listener.enterJava_method_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_method_expression"):
                listener.exitJava_method_expression(self)




    def java_method_expression(self):

        localctx = MParser.Java_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 388, self.RULE_java_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2251
            localctx.name = self.java_identifier()
            self.state = 2252
            self.match(MParser.LPAR)
            self.state = 2254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & ((1 << (MParser.LPAR - 20)) | (1 << (MParser.BOOLEAN - 20)) | (1 << (MParser.CHARACTER - 20)) | (1 << (MParser.TEXT - 20)) | (1 << (MParser.INTEGER - 20)) | (1 << (MParser.DECIMAL - 20)) | (1 << (MParser.DATE - 20)) | (1 << (MParser.TIME - 20)) | (1 << (MParser.DATETIME - 20)) | (1 << (MParser.PERIOD - 20)) | (1 << (MParser.VERSION - 20)) | (1 << (MParser.UUID - 20)) | (1 << (MParser.HTML - 20)))) != 0) or ((((_la - 122)) & ~0x3f) == 0 and ((1 << (_la - 122)) & ((1 << (MParser.NONE - 122)) | (1 << (MParser.NULL - 122)) | (1 << (MParser.READ - 122)) | (1 << (MParser.SELF - 122)) | (1 << (MParser.TEST - 122)) | (1 << (MParser.THIS - 122)) | (1 << (MParser.WRITE - 122)) | (1 << (MParser.BOOLEAN_LITERAL - 122)) | (1 << (MParser.CHAR_LITERAL - 122)) | (1 << (MParser.SYMBOL_IDENTIFIER - 122)) | (1 << (MParser.TYPE_IDENTIFIER - 122)) | (1 << (MParser.VARIABLE_IDENTIFIER - 122)) | (1 << (MParser.NATIVE_IDENTIFIER - 122)) | (1 << (MParser.DOLLAR_IDENTIFIER - 122)) | (1 << (MParser.TEXT_LITERAL - 122)) | (1 << (MParser.INTEGER_LITERAL - 122)) | (1 << (MParser.DECIMAL_LITERAL - 122)))) != 0):
                self.state = 2253
                localctx.args = self.java_arguments(0)


            self.state = 2256
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Java_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_java_arguments

     
        def copyFrom(self, ctx):
            super(MParser.Java_argumentsContext, self).copyFrom(ctx)


    class JavaArgumentListItemContext(Java_argumentsContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_argumentsContext)
            super(MParser.JavaArgumentListItemContext, self).__init__(parser)
            self.items = None # Java_argumentsContext
            self.item = None # Java_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)
        def java_arguments(self):
            return self.getTypedRuleContext(MParser.Java_argumentsContext,0)

        def java_expression(self):
            return self.getTypedRuleContext(MParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaArgumentListItem"):
                listener.enterJavaArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaArgumentListItem"):
                listener.exitJavaArgumentListItem(self)


    class JavaArgumentListContext(Java_argumentsContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_argumentsContext)
            super(MParser.JavaArgumentListContext, self).__init__(parser)
            self.item = None # Java_expressionContext
            self.copyFrom(ctx)

        def java_expression(self):
            return self.getTypedRuleContext(MParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaArgumentList"):
                listener.enterJavaArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaArgumentList"):
                listener.exitJavaArgumentList(self)



    def java_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Java_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 390
        self.enterRecursionRule(localctx, 390, self.RULE_java_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.JavaArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2259
            localctx.item = self.java_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,180,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.JavaArgumentListItemContext(self, MParser.Java_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_arguments)
                    self.state = 2261
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2262
                    self.match(MParser.COMMA)
                    self.state = 2263
                    localctx.item = self.java_expression(0) 
                self.state = 2268
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,180,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Java_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Java_expressionContext

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)

        def java_expression(self):
            return self.getTypedRuleContext(MParser.Java_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_java_item_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_item_expression"):
                listener.enterJava_item_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_item_expression"):
                listener.exitJava_item_expression(self)




    def java_item_expression(self):

        localctx = MParser.Java_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 392, self.RULE_java_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2269
            self.match(MParser.LBRAK)
            self.state = 2270
            localctx.exp = self.java_expression(0)
            self.state = 2271
            self.match(MParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Java_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Java_expressionContext

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def java_expression(self):
            return self.getTypedRuleContext(MParser.Java_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_java_parenthesis_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_parenthesis_expression"):
                listener.enterJava_parenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_parenthesis_expression"):
                listener.exitJava_parenthesis_expression(self)




    def java_parenthesis_expression(self):

        localctx = MParser.Java_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 394, self.RULE_java_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2273
            self.match(MParser.LPAR)
            self.state = 2274
            localctx.exp = self.java_expression(0)
            self.state = 2275
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Java_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_java_identifier_expression

     
        def copyFrom(self, ctx):
            super(MParser.Java_identifier_expressionContext, self).copyFrom(ctx)


    class JavaIdentifierContext(Java_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_identifier_expressionContext)
            super(MParser.JavaIdentifierContext, self).__init__(parser)
            self.name = None # Java_identifierContext
            self.copyFrom(ctx)

        def java_identifier(self):
            return self.getTypedRuleContext(MParser.Java_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaIdentifier"):
                listener.enterJavaIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaIdentifier"):
                listener.exitJavaIdentifier(self)


    class JavaChildIdentifierContext(Java_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_identifier_expressionContext)
            super(MParser.JavaChildIdentifierContext, self).__init__(parser)
            self.parent = None # Java_identifier_expressionContext
            self.name = None # Java_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def java_identifier_expression(self):
            return self.getTypedRuleContext(MParser.Java_identifier_expressionContext,0)

        def java_identifier(self):
            return self.getTypedRuleContext(MParser.Java_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaChildIdentifier"):
                listener.enterJavaChildIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaChildIdentifier"):
                listener.exitJavaChildIdentifier(self)



    def java_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Java_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 396
        self.enterRecursionRule(localctx, 396, self.RULE_java_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.JavaIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2278
            localctx.name = self.java_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2285
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,181,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.JavaChildIdentifierContext(self, MParser.Java_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_identifier_expression)
                    self.state = 2280
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2281
                    self.match(MParser.DOT)
                    self.state = 2282
                    localctx.name = self.java_identifier() 
                self.state = 2287
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,181,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_class_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Java_class_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_java_class_identifier_expression

     
        def copyFrom(self, ctx):
            super(MParser.Java_class_identifier_expressionContext, self).copyFrom(ctx)


    class JavaClassIdentifierContext(Java_class_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_class_identifier_expressionContext)
            super(MParser.JavaClassIdentifierContext, self).__init__(parser)
            self.klass = None # Java_identifier_expressionContext
            self.copyFrom(ctx)

        def java_identifier_expression(self):
            return self.getTypedRuleContext(MParser.Java_identifier_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJavaClassIdentifier"):
                listener.enterJavaClassIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaClassIdentifier"):
                listener.exitJavaClassIdentifier(self)


    class JavaChildClassIdentifierContext(Java_class_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_class_identifier_expressionContext)
            super(MParser.JavaChildClassIdentifierContext, self).__init__(parser)
            self.parent = None # Java_class_identifier_expressionContext
            self.name = None # Token
            self.copyFrom(ctx)

        def java_class_identifier_expression(self):
            return self.getTypedRuleContext(MParser.Java_class_identifier_expressionContext,0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(MParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaChildClassIdentifier"):
                listener.enterJavaChildClassIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaChildClassIdentifier"):
                listener.exitJavaChildClassIdentifier(self)



    def java_class_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Java_class_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 398
        self.enterRecursionRule(localctx, 398, self.RULE_java_class_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.JavaClassIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2289
            localctx.klass = self.java_identifier_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2295
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,182,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.JavaChildClassIdentifierContext(self, MParser.Java_class_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_class_identifier_expression)
                    self.state = 2291
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2292
                    localctx.name = self.match(MParser.DOLLAR_IDENTIFIER) 
                self.state = 2297
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,182,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Java_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_java_literal_expression

     
        def copyFrom(self, ctx):
            super(MParser.Java_literal_expressionContext, self).copyFrom(ctx)



    class JavaBooleanLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_literal_expressionContext)
            super(MParser.JavaBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(MParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaBooleanLiteral"):
                listener.enterJavaBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaBooleanLiteral"):
                listener.exitJavaBooleanLiteral(self)


    class JavaCharacterLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_literal_expressionContext)
            super(MParser.JavaCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(MParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaCharacterLiteral"):
                listener.enterJavaCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaCharacterLiteral"):
                listener.exitJavaCharacterLiteral(self)


    class JavaIntegerLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_literal_expressionContext)
            super(MParser.JavaIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(MParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaIntegerLiteral"):
                listener.enterJavaIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaIntegerLiteral"):
                listener.exitJavaIntegerLiteral(self)


    class JavaTextLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_literal_expressionContext)
            super(MParser.JavaTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(MParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaTextLiteral"):
                listener.enterJavaTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaTextLiteral"):
                listener.exitJavaTextLiteral(self)


    class JavaDecimalLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_literal_expressionContext)
            super(MParser.JavaDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(MParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJavaDecimalLiteral"):
                listener.enterJavaDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJavaDecimalLiteral"):
                listener.exitJavaDecimalLiteral(self)



    def java_literal_expression(self):

        localctx = MParser.Java_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 400, self.RULE_java_literal_expression)
        try:
            self.state = 2303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.INTEGER_LITERAL]:
                localctx = MParser.JavaIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2298
                localctx.t = self.match(MParser.INTEGER_LITERAL)
                pass
            elif token in [MParser.DECIMAL_LITERAL]:
                localctx = MParser.JavaDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2299
                localctx.t = self.match(MParser.DECIMAL_LITERAL)
                pass
            elif token in [MParser.TEXT_LITERAL]:
                localctx = MParser.JavaTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2300
                localctx.t = self.match(MParser.TEXT_LITERAL)
                pass
            elif token in [MParser.BOOLEAN_LITERAL]:
                localctx = MParser.JavaBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2301
                localctx.t = self.match(MParser.BOOLEAN_LITERAL)
                pass
            elif token in [MParser.CHAR_LITERAL]:
                localctx = MParser.JavaCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2302
                localctx.t = self.match(MParser.CHAR_LITERAL)
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
            super(MParser.Java_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(MParser.SYMBOL_IDENTIFIER, 0)

        def NATIVE_IDENTIFIER(self):
            return self.getToken(MParser.NATIVE_IDENTIFIER, 0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(MParser.DOLLAR_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(MParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(MParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(MParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(MParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(MParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(MParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(MParser.DATE, 0)

        def TIME(self):
            return self.getToken(MParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(MParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(MParser.PERIOD, 0)

        def VERSION(self):
            return self.getToken(MParser.VERSION, 0)

        def UUID(self):
            return self.getToken(MParser.UUID, 0)

        def HTML(self):
            return self.getToken(MParser.HTML, 0)

        def READ(self):
            return self.getToken(MParser.READ, 0)

        def WRITE(self):
            return self.getToken(MParser.WRITE, 0)

        def TEST(self):
            return self.getToken(MParser.TEST, 0)

        def SELF(self):
            return self.getToken(MParser.SELF, 0)

        def NONE(self):
            return self.getToken(MParser.NONE, 0)

        def NULL(self):
            return self.getToken(MParser.NULL, 0)

        def getRuleIndex(self):
            return MParser.RULE_java_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterJava_identifier"):
                listener.enterJava_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJava_identifier"):
                listener.exitJava_identifier(self)




    def java_identifier(self):

        localctx = MParser.Java_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 402, self.RULE_java_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2305
            _la = self._input.LA(1)
            if not(((((_la - 50)) & ~0x3f) == 0 and ((1 << (_la - 50)) & ((1 << (MParser.BOOLEAN - 50)) | (1 << (MParser.CHARACTER - 50)) | (1 << (MParser.TEXT - 50)) | (1 << (MParser.INTEGER - 50)) | (1 << (MParser.DECIMAL - 50)) | (1 << (MParser.DATE - 50)) | (1 << (MParser.TIME - 50)) | (1 << (MParser.DATETIME - 50)) | (1 << (MParser.PERIOD - 50)) | (1 << (MParser.VERSION - 50)) | (1 << (MParser.UUID - 50)) | (1 << (MParser.HTML - 50)))) != 0) or ((((_la - 122)) & ~0x3f) == 0 and ((1 << (_la - 122)) & ((1 << (MParser.NONE - 122)) | (1 << (MParser.NULL - 122)) | (1 << (MParser.READ - 122)) | (1 << (MParser.SELF - 122)) | (1 << (MParser.TEST - 122)) | (1 << (MParser.WRITE - 122)) | (1 << (MParser.SYMBOL_IDENTIFIER - 122)) | (1 << (MParser.TYPE_IDENTIFIER - 122)) | (1 << (MParser.VARIABLE_IDENTIFIER - 122)) | (1 << (MParser.NATIVE_IDENTIFIER - 122)) | (1 << (MParser.DOLLAR_IDENTIFIER - 122)))) != 0)):
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
            super(MParser.Csharp_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_csharp_statement

     
        def copyFrom(self, ctx):
            super(MParser.Csharp_statementContext, self).copyFrom(ctx)



    class CSharpReturnStatementContext(Csharp_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_statementContext)
            super(MParser.CSharpReturnStatementContext, self).__init__(parser)
            self.exp = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(MParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(MParser.SEMI, 0)
        def csharp_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpReturnStatement"):
                listener.enterCSharpReturnStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpReturnStatement"):
                listener.exitCSharpReturnStatement(self)


    class CSharpStatementContext(Csharp_statementContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_statementContext)
            super(MParser.CSharpStatementContext, self).__init__(parser)
            self.exp = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(MParser.SEMI, 0)
        def csharp_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpStatement"):
                listener.enterCSharpStatement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpStatement"):
                listener.exitCSharpStatement(self)



    def csharp_statement(self):

        localctx = MParser.Csharp_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 404, self.RULE_csharp_statement)
        try:
            self.state = 2314
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.RETURN]:
                localctx = MParser.CSharpReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2307
                self.match(MParser.RETURN)
                self.state = 2308
                localctx.exp = self.csharp_expression(0)
                self.state = 2309
                self.match(MParser.SEMI)
                pass
            elif token in [MParser.LPAR, MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.VERSION, MParser.UUID, MParser.HTML, MParser.NONE, MParser.NULL, MParser.READ, MParser.SELF, MParser.TEST, MParser.THIS, MParser.WRITE, MParser.BOOLEAN_LITERAL, MParser.CHAR_LITERAL, MParser.SYMBOL_IDENTIFIER, MParser.TYPE_IDENTIFIER, MParser.VARIABLE_IDENTIFIER, MParser.DOLLAR_IDENTIFIER, MParser.TEXT_LITERAL, MParser.INTEGER_LITERAL, MParser.DECIMAL_LITERAL]:
                localctx = MParser.CSharpStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2311
                localctx.exp = self.csharp_expression(0)
                self.state = 2312
                self.match(MParser.SEMI)
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
            super(MParser.Csharp_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_csharp_expression

     
        def copyFrom(self, ctx):
            super(MParser.Csharp_expressionContext, self).copyFrom(ctx)


    class CSharpSelectorExpressionContext(Csharp_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_expressionContext)
            super(MParser.CSharpSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Csharp_expressionContext
            self.child = None # Csharp_selector_expressionContext
            self.copyFrom(ctx)

        def csharp_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_expressionContext,0)

        def csharp_selector_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_selector_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpSelectorExpression"):
                listener.enterCSharpSelectorExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpSelectorExpression"):
                listener.exitCSharpSelectorExpression(self)


    class CSharpPrimaryExpressionContext(Csharp_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_expressionContext)
            super(MParser.CSharpPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_primary_expressionContext
            self.copyFrom(ctx)

        def csharp_primary_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_primary_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpPrimaryExpression"):
                listener.enterCSharpPrimaryExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpPrimaryExpression"):
                listener.exitCSharpPrimaryExpression(self)



    def csharp_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Csharp_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 406
        self.enterRecursionRule(localctx, 406, self.RULE_csharp_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.CSharpPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2317
            localctx.exp = self.csharp_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2323
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,185,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.CSharpSelectorExpressionContext(self, MParser.Csharp_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_expression)
                    self.state = 2319
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2320
                    localctx.child = self.csharp_selector_expression() 
                self.state = 2325
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,185,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Csharp_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def csharp_this_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_this_expressionContext,0)


        def csharp_new_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_new_expressionContext,0)


        def csharp_parenthesis_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_parenthesis_expressionContext,0)


        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_identifier_expressionContext,0)


        def csharp_literal_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_literal_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_csharp_primary_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_primary_expression"):
                listener.enterCsharp_primary_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_primary_expression"):
                listener.exitCsharp_primary_expression(self)




    def csharp_primary_expression(self):

        localctx = MParser.Csharp_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 408, self.RULE_csharp_primary_expression)
        try:
            self.state = 2331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,186,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2326
                self.csharp_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2327
                self.csharp_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2328
                self.csharp_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2329
                self.csharp_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2330
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
            super(MParser.Csharp_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(MParser.This_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_csharp_this_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_this_expression"):
                listener.enterCsharp_this_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_this_expression"):
                listener.exitCsharp_this_expression(self)




    def csharp_this_expression(self):

        localctx = MParser.Csharp_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 410, self.RULE_csharp_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2333
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
            super(MParser.Csharp_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(MParser.New_tokenContext,0)


        def csharp_method_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_method_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_csharp_new_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_new_expression"):
                listener.enterCsharp_new_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_new_expression"):
                listener.exitCsharp_new_expression(self)




    def csharp_new_expression(self):

        localctx = MParser.Csharp_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 412, self.RULE_csharp_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2335
            self.new_token()
            self.state = 2336
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
            super(MParser.Csharp_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_csharp_selector_expression

     
        def copyFrom(self, ctx):
            super(MParser.Csharp_selector_expressionContext, self).copyFrom(ctx)



    class CSharpMethodExpressionContext(Csharp_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_selector_expressionContext)
            super(MParser.CSharpMethodExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def csharp_method_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_method_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpMethodExpression"):
                listener.enterCSharpMethodExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpMethodExpression"):
                listener.exitCSharpMethodExpression(self)


    class CSharpItemExpressionContext(Csharp_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_selector_expressionContext)
            super(MParser.CSharpItemExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_item_expressionContext
            self.copyFrom(ctx)

        def csharp_item_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_item_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpItemExpression"):
                listener.enterCSharpItemExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpItemExpression"):
                listener.exitCSharpItemExpression(self)



    def csharp_selector_expression(self):

        localctx = MParser.Csharp_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 414, self.RULE_csharp_selector_expression)
        try:
            self.state = 2341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.DOT]:
                localctx = MParser.CSharpMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2338
                self.match(MParser.DOT)
                self.state = 2339
                localctx.exp = self.csharp_method_expression()
                pass
            elif token in [MParser.LBRAK]:
                localctx = MParser.CSharpItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2340
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
            super(MParser.Csharp_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Csharp_identifierContext
            self.args = None # Csharp_argumentsContext

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def csharp_identifier(self):
            return self.getTypedRuleContext(MParser.Csharp_identifierContext,0)


        def csharp_arguments(self):
            return self.getTypedRuleContext(MParser.Csharp_argumentsContext,0)


        def getRuleIndex(self):
            return MParser.RULE_csharp_method_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_method_expression"):
                listener.enterCsharp_method_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_method_expression"):
                listener.exitCsharp_method_expression(self)




    def csharp_method_expression(self):

        localctx = MParser.Csharp_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 416, self.RULE_csharp_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2343
            localctx.name = self.csharp_identifier()
            self.state = 2344
            self.match(MParser.LPAR)
            self.state = 2346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & ((1 << (MParser.LPAR - 20)) | (1 << (MParser.BOOLEAN - 20)) | (1 << (MParser.CHARACTER - 20)) | (1 << (MParser.TEXT - 20)) | (1 << (MParser.INTEGER - 20)) | (1 << (MParser.DECIMAL - 20)) | (1 << (MParser.DATE - 20)) | (1 << (MParser.TIME - 20)) | (1 << (MParser.DATETIME - 20)) | (1 << (MParser.PERIOD - 20)) | (1 << (MParser.VERSION - 20)) | (1 << (MParser.UUID - 20)) | (1 << (MParser.HTML - 20)))) != 0) or ((((_la - 122)) & ~0x3f) == 0 and ((1 << (_la - 122)) & ((1 << (MParser.NONE - 122)) | (1 << (MParser.NULL - 122)) | (1 << (MParser.READ - 122)) | (1 << (MParser.SELF - 122)) | (1 << (MParser.TEST - 122)) | (1 << (MParser.THIS - 122)) | (1 << (MParser.WRITE - 122)) | (1 << (MParser.BOOLEAN_LITERAL - 122)) | (1 << (MParser.CHAR_LITERAL - 122)) | (1 << (MParser.SYMBOL_IDENTIFIER - 122)) | (1 << (MParser.TYPE_IDENTIFIER - 122)) | (1 << (MParser.VARIABLE_IDENTIFIER - 122)) | (1 << (MParser.DOLLAR_IDENTIFIER - 122)) | (1 << (MParser.TEXT_LITERAL - 122)) | (1 << (MParser.INTEGER_LITERAL - 122)) | (1 << (MParser.DECIMAL_LITERAL - 122)))) != 0):
                self.state = 2345
                localctx.args = self.csharp_arguments(0)


            self.state = 2348
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Csharp_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_csharp_arguments

     
        def copyFrom(self, ctx):
            super(MParser.Csharp_argumentsContext, self).copyFrom(ctx)


    class CSharpArgumentListContext(Csharp_argumentsContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_argumentsContext)
            super(MParser.CSharpArgumentListContext, self).__init__(parser)
            self.item = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def csharp_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpArgumentList"):
                listener.enterCSharpArgumentList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpArgumentList"):
                listener.exitCSharpArgumentList(self)


    class CSharpArgumentListItemContext(Csharp_argumentsContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_argumentsContext)
            super(MParser.CSharpArgumentListItemContext, self).__init__(parser)
            self.items = None # Csharp_argumentsContext
            self.item = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(MParser.COMMA, 0)
        def csharp_arguments(self):
            return self.getTypedRuleContext(MParser.Csharp_argumentsContext,0)

        def csharp_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpArgumentListItem"):
                listener.enterCSharpArgumentListItem(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpArgumentListItem"):
                listener.exitCSharpArgumentListItem(self)



    def csharp_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Csharp_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 418
        self.enterRecursionRule(localctx, 418, self.RULE_csharp_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.CSharpArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2351
            localctx.item = self.csharp_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2358
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,189,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.CSharpArgumentListItemContext(self, MParser.Csharp_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_arguments)
                    self.state = 2353
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2354
                    self.match(MParser.COMMA)
                    self.state = 2355
                    localctx.item = self.csharp_expression(0) 
                self.state = 2360
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,189,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Csharp_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Csharp_expressionContext

        def LBRAK(self):
            return self.getToken(MParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(MParser.RBRAK, 0)

        def csharp_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_csharp_item_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_item_expression"):
                listener.enterCsharp_item_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_item_expression"):
                listener.exitCsharp_item_expression(self)




    def csharp_item_expression(self):

        localctx = MParser.Csharp_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 420, self.RULE_csharp_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2361
            self.match(MParser.LBRAK)
            self.state = 2362
            localctx.exp = self.csharp_expression(0)
            self.state = 2363
            self.match(MParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Csharp_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Csharp_expressionContext

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def csharp_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_expressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_csharp_parenthesis_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_parenthesis_expression"):
                listener.enterCsharp_parenthesis_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_parenthesis_expression"):
                listener.exitCsharp_parenthesis_expression(self)




    def csharp_parenthesis_expression(self):

        localctx = MParser.Csharp_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 422, self.RULE_csharp_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2365
            self.match(MParser.LPAR)
            self.state = 2366
            localctx.exp = self.csharp_expression(0)
            self.state = 2367
            self.match(MParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Csharp_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_csharp_identifier_expression

     
        def copyFrom(self, ctx):
            super(MParser.Csharp_identifier_expressionContext, self).copyFrom(ctx)


    class CSharpIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_identifier_expressionContext)
            super(MParser.CSharpIdentifierContext, self).__init__(parser)
            self.name = None # Csharp_identifierContext
            self.copyFrom(ctx)

        def csharp_identifier(self):
            return self.getTypedRuleContext(MParser.Csharp_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpIdentifier"):
                listener.enterCSharpIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpIdentifier"):
                listener.exitCSharpIdentifier(self)


    class CSharpChildIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_identifier_expressionContext)
            super(MParser.CSharpChildIdentifierContext, self).__init__(parser)
            self.parent = None # Csharp_identifier_expressionContext
            self.name = None # Csharp_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MParser.DOT, 0)
        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_identifier_expressionContext,0)

        def csharp_identifier(self):
            return self.getTypedRuleContext(MParser.Csharp_identifierContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpChildIdentifier"):
                listener.enterCSharpChildIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpChildIdentifier"):
                listener.exitCSharpChildIdentifier(self)


    class CSharpPromptoIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_identifier_expressionContext)
            super(MParser.CSharpPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(MParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpPromptoIdentifier"):
                listener.enterCSharpPromptoIdentifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpPromptoIdentifier"):
                listener.exitCSharpPromptoIdentifier(self)



    def csharp_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Csharp_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 424
        self.enterRecursionRule(localctx, 424, self.RULE_csharp_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2372
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.DOLLAR_IDENTIFIER]:
                localctx = MParser.CSharpPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2370
                self.match(MParser.DOLLAR_IDENTIFIER)
                pass
            elif token in [MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.VERSION, MParser.UUID, MParser.HTML, MParser.NONE, MParser.NULL, MParser.READ, MParser.SELF, MParser.TEST, MParser.WRITE, MParser.SYMBOL_IDENTIFIER, MParser.TYPE_IDENTIFIER, MParser.VARIABLE_IDENTIFIER]:
                localctx = MParser.CSharpIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2371
                localctx.name = self.csharp_identifier()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,191,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.CSharpChildIdentifierContext(self, MParser.Csharp_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_identifier_expression)
                    self.state = 2374
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2375
                    self.match(MParser.DOT)
                    self.state = 2376
                    localctx.name = self.csharp_identifier() 
                self.state = 2381
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,191,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Csharp_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_csharp_literal_expression

     
        def copyFrom(self, ctx):
            super(MParser.Csharp_literal_expressionContext, self).copyFrom(ctx)



    class CSharpBooleanLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_literal_expressionContext)
            super(MParser.CSharpBooleanLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(MParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpBooleanLiteral"):
                listener.enterCSharpBooleanLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpBooleanLiteral"):
                listener.exitCSharpBooleanLiteral(self)


    class CSharpIntegerLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_literal_expressionContext)
            super(MParser.CSharpIntegerLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(MParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpIntegerLiteral"):
                listener.enterCSharpIntegerLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpIntegerLiteral"):
                listener.exitCSharpIntegerLiteral(self)


    class CSharpDecimalLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_literal_expressionContext)
            super(MParser.CSharpDecimalLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(MParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpDecimalLiteral"):
                listener.enterCSharpDecimalLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpDecimalLiteral"):
                listener.exitCSharpDecimalLiteral(self)


    class CSharpCharacterLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_literal_expressionContext)
            super(MParser.CSharpCharacterLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(MParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpCharacterLiteral"):
                listener.enterCSharpCharacterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpCharacterLiteral"):
                listener.exitCSharpCharacterLiteral(self)


    class CSharpTextLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_literal_expressionContext)
            super(MParser.CSharpTextLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(MParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterCSharpTextLiteral"):
                listener.enterCSharpTextLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCSharpTextLiteral"):
                listener.exitCSharpTextLiteral(self)



    def csharp_literal_expression(self):

        localctx = MParser.Csharp_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 426, self.RULE_csharp_literal_expression)
        try:
            self.state = 2387
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.INTEGER_LITERAL]:
                localctx = MParser.CSharpIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2382
                self.match(MParser.INTEGER_LITERAL)
                pass
            elif token in [MParser.DECIMAL_LITERAL]:
                localctx = MParser.CSharpDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2383
                self.match(MParser.DECIMAL_LITERAL)
                pass
            elif token in [MParser.TEXT_LITERAL]:
                localctx = MParser.CSharpTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2384
                self.match(MParser.TEXT_LITERAL)
                pass
            elif token in [MParser.BOOLEAN_LITERAL]:
                localctx = MParser.CSharpBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2385
                self.match(MParser.BOOLEAN_LITERAL)
                pass
            elif token in [MParser.CHAR_LITERAL]:
                localctx = MParser.CSharpCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2386
                self.match(MParser.CHAR_LITERAL)
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
            super(MParser.Csharp_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(MParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(MParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(MParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(MParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(MParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(MParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(MParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(MParser.DATE, 0)

        def TIME(self):
            return self.getToken(MParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(MParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(MParser.PERIOD, 0)

        def VERSION(self):
            return self.getToken(MParser.VERSION, 0)

        def UUID(self):
            return self.getToken(MParser.UUID, 0)

        def HTML(self):
            return self.getToken(MParser.HTML, 0)

        def READ(self):
            return self.getToken(MParser.READ, 0)

        def WRITE(self):
            return self.getToken(MParser.WRITE, 0)

        def TEST(self):
            return self.getToken(MParser.TEST, 0)

        def SELF(self):
            return self.getToken(MParser.SELF, 0)

        def NONE(self):
            return self.getToken(MParser.NONE, 0)

        def NULL(self):
            return self.getToken(MParser.NULL, 0)

        def getRuleIndex(self):
            return MParser.RULE_csharp_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterCsharp_identifier"):
                listener.enterCsharp_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCsharp_identifier"):
                listener.exitCsharp_identifier(self)




    def csharp_identifier(self):

        localctx = MParser.Csharp_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 428, self.RULE_csharp_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2389
            _la = self._input.LA(1)
            if not(((((_la - 50)) & ~0x3f) == 0 and ((1 << (_la - 50)) & ((1 << (MParser.BOOLEAN - 50)) | (1 << (MParser.CHARACTER - 50)) | (1 << (MParser.TEXT - 50)) | (1 << (MParser.INTEGER - 50)) | (1 << (MParser.DECIMAL - 50)) | (1 << (MParser.DATE - 50)) | (1 << (MParser.TIME - 50)) | (1 << (MParser.DATETIME - 50)) | (1 << (MParser.PERIOD - 50)) | (1 << (MParser.VERSION - 50)) | (1 << (MParser.UUID - 50)) | (1 << (MParser.HTML - 50)))) != 0) or ((((_la - 122)) & ~0x3f) == 0 and ((1 << (_la - 122)) & ((1 << (MParser.NONE - 122)) | (1 << (MParser.NULL - 122)) | (1 << (MParser.READ - 122)) | (1 << (MParser.SELF - 122)) | (1 << (MParser.TEST - 122)) | (1 << (MParser.WRITE - 122)) | (1 << (MParser.SYMBOL_IDENTIFIER - 122)) | (1 << (MParser.TYPE_IDENTIFIER - 122)) | (1 << (MParser.VARIABLE_IDENTIFIER - 122)))) != 0)):
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
            super(MParser.Jsx_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def jsx_element(self):
            return self.getTypedRuleContext(MParser.Jsx_elementContext,0)


        def jsx_fragment(self):
            return self.getTypedRuleContext(MParser.Jsx_fragmentContext,0)


        def getRuleIndex(self):
            return MParser.RULE_jsx_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_expression"):
                listener.enterJsx_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_expression"):
                listener.exitJsx_expression(self)




    def jsx_expression(self):

        localctx = MParser.Jsx_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 430, self.RULE_jsx_expression)
        try:
            self.state = 2393
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,193,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2391
                self.jsx_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2392
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
            super(MParser.Jsx_elementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_jsx_element

     
        def copyFrom(self, ctx):
            super(MParser.Jsx_elementContext, self).copyFrom(ctx)



    class JsxSelfClosingContext(Jsx_elementContext):

        def __init__(self, parser, ctx): # actually a MParser.Jsx_elementContext)
            super(MParser.JsxSelfClosingContext, self).__init__(parser)
            self.jsx = None # Jsx_self_closingContext
            self.copyFrom(ctx)

        def jsx_self_closing(self):
            return self.getTypedRuleContext(MParser.Jsx_self_closingContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJsxSelfClosing"):
                listener.enterJsxSelfClosing(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxSelfClosing"):
                listener.exitJsxSelfClosing(self)


    class JsxElementContext(Jsx_elementContext):

        def __init__(self, parser, ctx): # actually a MParser.Jsx_elementContext)
            super(MParser.JsxElementContext, self).__init__(parser)
            self.jsx = None # Jsx_openingContext
            self.children_ = None # Jsx_childrenContext
            self.copyFrom(ctx)

        def jsx_closing(self):
            return self.getTypedRuleContext(MParser.Jsx_closingContext,0)

        def jsx_opening(self):
            return self.getTypedRuleContext(MParser.Jsx_openingContext,0)

        def jsx_children(self):
            return self.getTypedRuleContext(MParser.Jsx_childrenContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJsxElement"):
                listener.enterJsxElement(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxElement"):
                listener.exitJsxElement(self)



    def jsx_element(self):

        localctx = MParser.Jsx_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 432, self.RULE_jsx_element)
        try:
            self.state = 2402
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,195,self._ctx)
            if la_ == 1:
                localctx = MParser.JsxSelfClosingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2395
                localctx.jsx = self.jsx_self_closing()
                pass

            elif la_ == 2:
                localctx = MParser.JsxElementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2396
                localctx.jsx = self.jsx_opening()
                self.state = 2398
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,194,self._ctx)
                if la_ == 1:
                    self.state = 2397
                    localctx.children_ = self.jsx_children()


                self.state = 2400
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
            super(MParser.Jsx_fragmentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.children_ = None # Jsx_childrenContext

        def jsx_fragment_start(self):
            return self.getTypedRuleContext(MParser.Jsx_fragment_startContext,0)


        def jsx_fragment_end(self):
            return self.getTypedRuleContext(MParser.Jsx_fragment_endContext,0)


        def jsx_children(self):
            return self.getTypedRuleContext(MParser.Jsx_childrenContext,0)


        def getRuleIndex(self):
            return MParser.RULE_jsx_fragment

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_fragment"):
                listener.enterJsx_fragment(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_fragment"):
                listener.exitJsx_fragment(self)




    def jsx_fragment(self):

        localctx = MParser.Jsx_fragmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 434, self.RULE_jsx_fragment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2404
            self.jsx_fragment_start()
            self.state = 2406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,196,self._ctx)
            if la_ == 1:
                self.state = 2405
                localctx.children_ = self.jsx_children()


            self.state = 2408
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
            super(MParser.Jsx_fragment_startContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(MParser.LT, 0)

        def GT(self):
            return self.getToken(MParser.GT, 0)

        def LTGT(self):
            return self.getToken(MParser.LTGT, 0)

        def getRuleIndex(self):
            return MParser.RULE_jsx_fragment_start

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_fragment_start"):
                listener.enterJsx_fragment_start(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_fragment_start"):
                listener.exitJsx_fragment_start(self)




    def jsx_fragment_start(self):

        localctx = MParser.Jsx_fragment_startContext(self, self._ctx, self.state)
        self.enterRule(localctx, 436, self.RULE_jsx_fragment_start)
        try:
            self.state = 2413
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.LT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2410
                self.match(MParser.LT)
                self.state = 2411
                self.match(MParser.GT)
                pass
            elif token in [MParser.LTGT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2412
                self.match(MParser.LTGT)
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
            super(MParser.Jsx_fragment_endContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(MParser.LT, 0)

        def SLASH(self):
            return self.getToken(MParser.SLASH, 0)

        def GT(self):
            return self.getToken(MParser.GT, 0)

        def getRuleIndex(self):
            return MParser.RULE_jsx_fragment_end

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_fragment_end"):
                listener.enterJsx_fragment_end(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_fragment_end"):
                listener.exitJsx_fragment_end(self)




    def jsx_fragment_end(self):

        localctx = MParser.Jsx_fragment_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 438, self.RULE_jsx_fragment_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2415
            self.match(MParser.LT)
            self.state = 2416
            self.match(MParser.SLASH)
            self.state = 2417
            self.match(MParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_self_closingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Jsx_self_closingContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Jsx_element_nameContext
            self.attributes = None # Jsx_attributeContext

        def LT(self):
            return self.getToken(MParser.LT, 0)

        def SLASH(self):
            return self.getToken(MParser.SLASH, 0)

        def GT(self):
            return self.getToken(MParser.GT, 0)

        def jsx_element_name(self):
            return self.getTypedRuleContext(MParser.Jsx_element_nameContext,0)


        def jsx_attribute(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Jsx_attributeContext)
            else:
                return self.getTypedRuleContext(MParser.Jsx_attributeContext,i)


        def getRuleIndex(self):
            return MParser.RULE_jsx_self_closing

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_self_closing"):
                listener.enterJsx_self_closing(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_self_closing"):
                listener.exitJsx_self_closing(self)




    def jsx_self_closing(self):

        localctx = MParser.Jsx_self_closingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 440, self.RULE_jsx_self_closing)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2419
            self.match(MParser.LT)
            self.state = 2420
            localctx.name = self.jsx_element_name()
            self.state = 2424
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.JAVA) | (1 << MParser.CSHARP) | (1 << MParser.PYTHON2) | (1 << MParser.PYTHON3) | (1 << MParser.JAVASCRIPT) | (1 << MParser.SWIFT) | (1 << MParser.BOOLEAN) | (1 << MParser.CHARACTER) | (1 << MParser.TEXT) | (1 << MParser.INTEGER) | (1 << MParser.DECIMAL) | (1 << MParser.DATE) | (1 << MParser.TIME) | (1 << MParser.DATETIME) | (1 << MParser.PERIOD) | (1 << MParser.VERSION) | (1 << MParser.METHOD_T) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (MParser.IMAGE - 64)) | (1 << (MParser.UUID - 64)) | (1 << (MParser.ITERATOR - 64)) | (1 << (MParser.CURSOR - 64)) | (1 << (MParser.HTML - 64)) | (1 << (MParser.ABSTRACT - 64)) | (1 << (MParser.ALL - 64)) | (1 << (MParser.ALWAYS - 64)) | (1 << (MParser.AND - 64)) | (1 << (MParser.ANY - 64)) | (1 << (MParser.AS - 64)) | (1 << (MParser.ASC - 64)) | (1 << (MParser.ATTR - 64)) | (1 << (MParser.ATTRIBUTE - 64)) | (1 << (MParser.ATTRIBUTES - 64)) | (1 << (MParser.BINDINGS - 64)) | (1 << (MParser.BREAK - 64)) | (1 << (MParser.BY - 64)) | (1 << (MParser.CASE - 64)) | (1 << (MParser.CATCH - 64)) | (1 << (MParser.CATEGORY - 64)) | (1 << (MParser.CLASS - 64)) | (1 << (MParser.CLOSE - 64)) | (1 << (MParser.CONTAINS - 64)) | (1 << (MParser.DEF - 64)) | (1 << (MParser.DEFAULT - 64)) | (1 << (MParser.DEFINE - 64)) | (1 << (MParser.DELETE - 64)) | (1 << (MParser.DESC - 64)) | (1 << (MParser.DO - 64)) | (1 << (MParser.DOING - 64)) | (1 << (MParser.EACH - 64)) | (1 << (MParser.ELSE - 64)) | (1 << (MParser.ENUM - 64)) | (1 << (MParser.ENUMERATED - 64)) | (1 << (MParser.EXCEPT - 64)) | (1 << (MParser.EXECUTE - 64)) | (1 << (MParser.EXPECTING - 64)) | (1 << (MParser.EXTENDS - 64)) | (1 << (MParser.FETCH - 64)) | (1 << (MParser.FILTERED - 64)) | (1 << (MParser.FINALLY - 64)) | (1 << (MParser.FLUSH - 64)) | (1 << (MParser.FOR - 64)) | (1 << (MParser.FROM - 64)) | (1 << (MParser.GETTER - 64)) | (1 << (MParser.HAS - 64)) | (1 << (MParser.IF - 64)) | (1 << (MParser.IN - 64)) | (1 << (MParser.INDEX - 64)) | (1 << (MParser.INVOKE - 64)) | (1 << (MParser.IS - 64)) | (1 << (MParser.MATCHING - 64)) | (1 << (MParser.METHOD - 64)) | (1 << (MParser.METHODS - 64)) | (1 << (MParser.MODULO - 64)) | (1 << (MParser.MUTABLE - 64)) | (1 << (MParser.NATIVE - 64)) | (1 << (MParser.NONE - 64)) | (1 << (MParser.NOT - 64)) | (1 << (MParser.NOTHING - 64)) | (1 << (MParser.NULL - 64)) | (1 << (MParser.ON - 64)) | (1 << (MParser.ONE - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (MParser.OPEN - 128)) | (1 << (MParser.OPERATOR - 128)) | (1 << (MParser.OR - 128)) | (1 << (MParser.ORDER - 128)) | (1 << (MParser.OTHERWISE - 128)) | (1 << (MParser.PASS - 128)) | (1 << (MParser.RAISE - 128)) | (1 << (MParser.READ - 128)) | (1 << (MParser.RECEIVING - 128)) | (1 << (MParser.RESOURCE - 128)) | (1 << (MParser.RETURN - 128)) | (1 << (MParser.RETURNING - 128)) | (1 << (MParser.ROWS - 128)) | (1 << (MParser.SELF - 128)) | (1 << (MParser.SETTER - 128)) | (1 << (MParser.SINGLETON - 128)) | (1 << (MParser.SORTED - 128)) | (1 << (MParser.STORABLE - 128)) | (1 << (MParser.STORE - 128)) | (1 << (MParser.SWITCH - 128)) | (1 << (MParser.TEST - 128)) | (1 << (MParser.THIS - 128)) | (1 << (MParser.THROW - 128)) | (1 << (MParser.TO - 128)) | (1 << (MParser.TRY - 128)) | (1 << (MParser.VERIFYING - 128)) | (1 << (MParser.WIDGET - 128)) | (1 << (MParser.WITH - 128)) | (1 << (MParser.WHEN - 128)) | (1 << (MParser.WHERE - 128)) | (1 << (MParser.WHILE - 128)) | (1 << (MParser.WRITE - 128)) | (1 << (MParser.SYMBOL_IDENTIFIER - 128)) | (1 << (MParser.TYPE_IDENTIFIER - 128)) | (1 << (MParser.VARIABLE_IDENTIFIER - 128)))) != 0):
                self.state = 2421
                localctx.attributes = self.jsx_attribute()
                self.state = 2426
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2427
            self.match(MParser.SLASH)
            self.state = 2428
            self.match(MParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_openingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Jsx_openingContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Jsx_element_nameContext
            self.attributes = None # Jsx_attributeContext

        def LT(self):
            return self.getToken(MParser.LT, 0)

        def GT(self):
            return self.getToken(MParser.GT, 0)

        def jsx_element_name(self):
            return self.getTypedRuleContext(MParser.Jsx_element_nameContext,0)


        def jsx_attribute(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Jsx_attributeContext)
            else:
                return self.getTypedRuleContext(MParser.Jsx_attributeContext,i)


        def getRuleIndex(self):
            return MParser.RULE_jsx_opening

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_opening"):
                listener.enterJsx_opening(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_opening"):
                listener.exitJsx_opening(self)




    def jsx_opening(self):

        localctx = MParser.Jsx_openingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 442, self.RULE_jsx_opening)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2430
            self.match(MParser.LT)
            self.state = 2431
            localctx.name = self.jsx_element_name()
            self.state = 2435
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.JAVA) | (1 << MParser.CSHARP) | (1 << MParser.PYTHON2) | (1 << MParser.PYTHON3) | (1 << MParser.JAVASCRIPT) | (1 << MParser.SWIFT) | (1 << MParser.BOOLEAN) | (1 << MParser.CHARACTER) | (1 << MParser.TEXT) | (1 << MParser.INTEGER) | (1 << MParser.DECIMAL) | (1 << MParser.DATE) | (1 << MParser.TIME) | (1 << MParser.DATETIME) | (1 << MParser.PERIOD) | (1 << MParser.VERSION) | (1 << MParser.METHOD_T) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (MParser.IMAGE - 64)) | (1 << (MParser.UUID - 64)) | (1 << (MParser.ITERATOR - 64)) | (1 << (MParser.CURSOR - 64)) | (1 << (MParser.HTML - 64)) | (1 << (MParser.ABSTRACT - 64)) | (1 << (MParser.ALL - 64)) | (1 << (MParser.ALWAYS - 64)) | (1 << (MParser.AND - 64)) | (1 << (MParser.ANY - 64)) | (1 << (MParser.AS - 64)) | (1 << (MParser.ASC - 64)) | (1 << (MParser.ATTR - 64)) | (1 << (MParser.ATTRIBUTE - 64)) | (1 << (MParser.ATTRIBUTES - 64)) | (1 << (MParser.BINDINGS - 64)) | (1 << (MParser.BREAK - 64)) | (1 << (MParser.BY - 64)) | (1 << (MParser.CASE - 64)) | (1 << (MParser.CATCH - 64)) | (1 << (MParser.CATEGORY - 64)) | (1 << (MParser.CLASS - 64)) | (1 << (MParser.CLOSE - 64)) | (1 << (MParser.CONTAINS - 64)) | (1 << (MParser.DEF - 64)) | (1 << (MParser.DEFAULT - 64)) | (1 << (MParser.DEFINE - 64)) | (1 << (MParser.DELETE - 64)) | (1 << (MParser.DESC - 64)) | (1 << (MParser.DO - 64)) | (1 << (MParser.DOING - 64)) | (1 << (MParser.EACH - 64)) | (1 << (MParser.ELSE - 64)) | (1 << (MParser.ENUM - 64)) | (1 << (MParser.ENUMERATED - 64)) | (1 << (MParser.EXCEPT - 64)) | (1 << (MParser.EXECUTE - 64)) | (1 << (MParser.EXPECTING - 64)) | (1 << (MParser.EXTENDS - 64)) | (1 << (MParser.FETCH - 64)) | (1 << (MParser.FILTERED - 64)) | (1 << (MParser.FINALLY - 64)) | (1 << (MParser.FLUSH - 64)) | (1 << (MParser.FOR - 64)) | (1 << (MParser.FROM - 64)) | (1 << (MParser.GETTER - 64)) | (1 << (MParser.HAS - 64)) | (1 << (MParser.IF - 64)) | (1 << (MParser.IN - 64)) | (1 << (MParser.INDEX - 64)) | (1 << (MParser.INVOKE - 64)) | (1 << (MParser.IS - 64)) | (1 << (MParser.MATCHING - 64)) | (1 << (MParser.METHOD - 64)) | (1 << (MParser.METHODS - 64)) | (1 << (MParser.MODULO - 64)) | (1 << (MParser.MUTABLE - 64)) | (1 << (MParser.NATIVE - 64)) | (1 << (MParser.NONE - 64)) | (1 << (MParser.NOT - 64)) | (1 << (MParser.NOTHING - 64)) | (1 << (MParser.NULL - 64)) | (1 << (MParser.ON - 64)) | (1 << (MParser.ONE - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (MParser.OPEN - 128)) | (1 << (MParser.OPERATOR - 128)) | (1 << (MParser.OR - 128)) | (1 << (MParser.ORDER - 128)) | (1 << (MParser.OTHERWISE - 128)) | (1 << (MParser.PASS - 128)) | (1 << (MParser.RAISE - 128)) | (1 << (MParser.READ - 128)) | (1 << (MParser.RECEIVING - 128)) | (1 << (MParser.RESOURCE - 128)) | (1 << (MParser.RETURN - 128)) | (1 << (MParser.RETURNING - 128)) | (1 << (MParser.ROWS - 128)) | (1 << (MParser.SELF - 128)) | (1 << (MParser.SETTER - 128)) | (1 << (MParser.SINGLETON - 128)) | (1 << (MParser.SORTED - 128)) | (1 << (MParser.STORABLE - 128)) | (1 << (MParser.STORE - 128)) | (1 << (MParser.SWITCH - 128)) | (1 << (MParser.TEST - 128)) | (1 << (MParser.THIS - 128)) | (1 << (MParser.THROW - 128)) | (1 << (MParser.TO - 128)) | (1 << (MParser.TRY - 128)) | (1 << (MParser.VERIFYING - 128)) | (1 << (MParser.WIDGET - 128)) | (1 << (MParser.WITH - 128)) | (1 << (MParser.WHEN - 128)) | (1 << (MParser.WHERE - 128)) | (1 << (MParser.WHILE - 128)) | (1 << (MParser.WRITE - 128)) | (1 << (MParser.SYMBOL_IDENTIFIER - 128)) | (1 << (MParser.TYPE_IDENTIFIER - 128)) | (1 << (MParser.VARIABLE_IDENTIFIER - 128)))) != 0):
                self.state = 2432
                localctx.attributes = self.jsx_attribute()
                self.state = 2437
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2438
            self.match(MParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_closingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Jsx_closingContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Jsx_element_nameContext

        def LT(self):
            return self.getToken(MParser.LT, 0)

        def SLASH(self):
            return self.getToken(MParser.SLASH, 0)

        def GT(self):
            return self.getToken(MParser.GT, 0)

        def jsx_element_name(self):
            return self.getTypedRuleContext(MParser.Jsx_element_nameContext,0)


        def getRuleIndex(self):
            return MParser.RULE_jsx_closing

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_closing"):
                listener.enterJsx_closing(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_closing"):
                listener.exitJsx_closing(self)




    def jsx_closing(self):

        localctx = MParser.Jsx_closingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 444, self.RULE_jsx_closing)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2440
            self.match(MParser.LT)
            self.state = 2441
            self.match(MParser.SLASH)
            self.state = 2442
            localctx.name = self.jsx_element_name()
            self.state = 2443
            self.match(MParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_element_nameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Jsx_element_nameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def jsx_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Jsx_identifierContext)
            else:
                return self.getTypedRuleContext(MParser.Jsx_identifierContext,i)


        def DOT(self, i=None):
            if i is None:
                return self.getTokens(MParser.DOT)
            else:
                return self.getToken(MParser.DOT, i)

        def getRuleIndex(self):
            return MParser.RULE_jsx_element_name

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_element_name"):
                listener.enterJsx_element_name(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_element_name"):
                listener.exitJsx_element_name(self)




    def jsx_element_name(self):

        localctx = MParser.Jsx_element_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 446, self.RULE_jsx_element_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2445
            self.jsx_identifier()
            self.state = 2450
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.DOT:
                self.state = 2446
                self.match(MParser.DOT)
                self.state = 2447
                self.jsx_identifier()
                self.state = 2452
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
            super(MParser.Jsx_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier_or_keyword(self):
            return self.getTypedRuleContext(MParser.Identifier_or_keywordContext,0)


        def nospace_hyphen_identifier_or_keyword(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Nospace_hyphen_identifier_or_keywordContext)
            else:
                return self.getTypedRuleContext(MParser.Nospace_hyphen_identifier_or_keywordContext,i)


        def getRuleIndex(self):
            return MParser.RULE_jsx_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_identifier"):
                listener.enterJsx_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_identifier"):
                listener.exitJsx_identifier(self)




    def jsx_identifier(self):

        localctx = MParser.Jsx_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 448, self.RULE_jsx_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2453
            self.identifier_or_keyword()
            self.state = 2457
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,201,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2454
                    self.nospace_hyphen_identifier_or_keyword() 
                self.state = 2459
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,201,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_attributeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Jsx_attributeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Jsx_identifierContext
            self.value = None # Jsx_attribute_valueContext

        def jsx_identifier(self):
            return self.getTypedRuleContext(MParser.Jsx_identifierContext,0)


        def EQ(self):
            return self.getToken(MParser.EQ, 0)

        def jsx_attribute_value(self):
            return self.getTypedRuleContext(MParser.Jsx_attribute_valueContext,0)


        def getRuleIndex(self):
            return MParser.RULE_jsx_attribute

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_attribute"):
                listener.enterJsx_attribute(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_attribute"):
                listener.exitJsx_attribute(self)




    def jsx_attribute(self):

        localctx = MParser.Jsx_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 450, self.RULE_jsx_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2460
            localctx.name = self.jsx_identifier()
            self.state = 2463
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MParser.EQ:
                self.state = 2461
                self.match(MParser.EQ)
                self.state = 2462
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
            super(MParser.Jsx_attribute_valueContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_jsx_attribute_value

     
        def copyFrom(self, ctx):
            super(MParser.Jsx_attribute_valueContext, self).copyFrom(ctx)



    class JsxValueContext(Jsx_attribute_valueContext):

        def __init__(self, parser, ctx): # actually a MParser.Jsx_attribute_valueContext)
            super(MParser.JsxValueContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(MParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(MParser.RCURL, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJsxValue"):
                listener.enterJsxValue(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxValue"):
                listener.exitJsxValue(self)


    class JsxLiteralContext(Jsx_attribute_valueContext):

        def __init__(self, parser, ctx): # actually a MParser.Jsx_attribute_valueContext)
            super(MParser.JsxLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(MParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterJsxLiteral"):
                listener.enterJsxLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxLiteral"):
                listener.exitJsxLiteral(self)



    def jsx_attribute_value(self):

        localctx = MParser.Jsx_attribute_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 452, self.RULE_jsx_attribute_value)
        try:
            self.state = 2470
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.TEXT_LITERAL]:
                localctx = MParser.JsxLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2465
                self.match(MParser.TEXT_LITERAL)
                pass
            elif token in [MParser.LCURL]:
                localctx = MParser.JsxValueContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2466
                self.match(MParser.LCURL)
                self.state = 2467
                localctx.exp = self.expression(0)
                self.state = 2468
                self.match(MParser.RCURL)
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
            super(MParser.Jsx_childrenContext, self).__init__(parent, invokingState)
            self.parser = parser

        def jsx_child(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Jsx_childContext)
            else:
                return self.getTypedRuleContext(MParser.Jsx_childContext,i)


        def getRuleIndex(self):
            return MParser.RULE_jsx_children

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_children"):
                listener.enterJsx_children(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_children"):
                listener.exitJsx_children(self)




    def jsx_children(self):

        localctx = MParser.Jsx_childrenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 454, self.RULE_jsx_children)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2473 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 2472
                    self.jsx_child()

                else:
                    raise NoViableAltException(self)
                self.state = 2475 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,204,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Jsx_childContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Jsx_childContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_jsx_child

     
        def copyFrom(self, ctx):
            super(MParser.Jsx_childContext, self).copyFrom(ctx)



    class JsxTextContext(Jsx_childContext):

        def __init__(self, parser, ctx): # actually a MParser.Jsx_childContext)
            super(MParser.JsxTextContext, self).__init__(parser)
            self.text = None # Jsx_textContext
            self.copyFrom(ctx)

        def jsx_text(self):
            return self.getTypedRuleContext(MParser.Jsx_textContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJsxText"):
                listener.enterJsxText(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxText"):
                listener.exitJsxText(self)


    class JsxChildContext(Jsx_childContext):

        def __init__(self, parser, ctx): # actually a MParser.Jsx_childContext)
            super(MParser.JsxChildContext, self).__init__(parser)
            self.jsx = None # Jsx_elementContext
            self.copyFrom(ctx)

        def jsx_element(self):
            return self.getTypedRuleContext(MParser.Jsx_elementContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJsxChild"):
                listener.enterJsxChild(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxChild"):
                listener.exitJsxChild(self)


    class JsxCodeContext(Jsx_childContext):

        def __init__(self, parser, ctx): # actually a MParser.Jsx_childContext)
            super(MParser.JsxCodeContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(MParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(MParser.RCURL, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterJsxCode"):
                listener.enterJsxCode(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsxCode"):
                listener.exitJsxCode(self)



    def jsx_child(self):

        localctx = MParser.Jsx_childContext(self, self._ctx, self.state)
        self.enterRule(localctx, 456, self.RULE_jsx_child)
        self._la = 0 # Token type
        try:
            self.state = 2484
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.INDENT, MParser.DEDENT, MParser.LF_TAB, MParser.LF_MORE, MParser.LF, MParser.TAB, MParser.WS, MParser.COMMENT, MParser.JAVA, MParser.CSHARP, MParser.PYTHON2, MParser.PYTHON3, MParser.JAVASCRIPT, MParser.SWIFT, MParser.COLON, MParser.SEMI, MParser.COMMA, MParser.RANGE, MParser.DOT, MParser.LPAR, MParser.RPAR, MParser.LBRAK, MParser.RBRAK, MParser.QMARK, MParser.XMARK, MParser.AMP, MParser.AMP2, MParser.PIPE, MParser.PIPE2, MParser.PLUS, MParser.MINUS, MParser.STAR, MParser.SLASH, MParser.BSLASH, MParser.PERCENT, MParser.GTE, MParser.LTE, MParser.LTGT, MParser.EQ, MParser.XEQ, MParser.EQ2, MParser.TEQ, MParser.TILDE, MParser.LARROW, MParser.RARROW, MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.VERSION, MParser.METHOD_T, MParser.CODE, MParser.DOCUMENT, MParser.BLOB, MParser.IMAGE, MParser.UUID, MParser.ITERATOR, MParser.CURSOR, MParser.HTML, MParser.ABSTRACT, MParser.ALL, MParser.ALWAYS, MParser.AND, MParser.ANY, MParser.AS, MParser.ASC, MParser.ATTR, MParser.ATTRIBUTE, MParser.ATTRIBUTES, MParser.BINDINGS, MParser.BREAK, MParser.BY, MParser.CASE, MParser.CATCH, MParser.CATEGORY, MParser.CLASS, MParser.CLOSE, MParser.CONTAINS, MParser.DEF, MParser.DEFAULT, MParser.DEFINE, MParser.DELETE, MParser.DESC, MParser.DO, MParser.DOING, MParser.EACH, MParser.ELSE, MParser.ENUM, MParser.ENUMERATED, MParser.EXCEPT, MParser.EXECUTE, MParser.EXPECTING, MParser.EXTENDS, MParser.FETCH, MParser.FILTERED, MParser.FINALLY, MParser.FLUSH, MParser.FOR, MParser.FROM, MParser.GETTER, MParser.HAS, MParser.IF, MParser.IN, MParser.INDEX, MParser.INVOKE, MParser.IS, MParser.MATCHING, MParser.METHOD, MParser.METHODS, MParser.MODULO, MParser.MUTABLE, MParser.NATIVE, MParser.NONE, MParser.NOT, MParser.NOTHING, MParser.NULL, MParser.ON, MParser.ONE, MParser.OPEN, MParser.OPERATOR, MParser.OR, MParser.ORDER, MParser.OTHERWISE, MParser.PASS, MParser.RAISE, MParser.READ, MParser.RECEIVING, MParser.RESOURCE, MParser.RETURN, MParser.RETURNING, MParser.ROWS, MParser.SELF, MParser.SETTER, MParser.SINGLETON, MParser.SORTED, MParser.STORABLE, MParser.STORE, MParser.SWITCH, MParser.TEST, MParser.THIS, MParser.THROW, MParser.TO, MParser.TRY, MParser.VERIFYING, MParser.WIDGET, MParser.WITH, MParser.WHEN, MParser.WHERE, MParser.WHILE, MParser.WRITE, MParser.BOOLEAN_LITERAL, MParser.CHAR_LITERAL, MParser.MIN_INTEGER, MParser.MAX_INTEGER, MParser.SYMBOL_IDENTIFIER, MParser.TYPE_IDENTIFIER, MParser.VARIABLE_IDENTIFIER, MParser.NATIVE_IDENTIFIER, MParser.DOLLAR_IDENTIFIER, MParser.TEXT_LITERAL, MParser.UUID_LITERAL, MParser.INTEGER_LITERAL, MParser.HEXA_LITERAL, MParser.DECIMAL_LITERAL, MParser.DATETIME_LITERAL, MParser.TIME_LITERAL, MParser.DATE_LITERAL, MParser.PERIOD_LITERAL, MParser.VERSION_LITERAL]:
                localctx = MParser.JsxTextContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2477
                localctx.text = self.jsx_text()
                pass
            elif token in [MParser.LT]:
                localctx = MParser.JsxChildContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2478
                localctx.jsx = self.jsx_element()
                pass
            elif token in [MParser.LCURL]:
                localctx = MParser.JsxCodeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2479
                self.match(MParser.LCURL)
                self.state = 2481
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.LTGT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 100)) & ~0x3f) == 0 and ((1 << (_la - 100)) & ((1 << (MParser.EXECUTE - 100)) | (1 << (MParser.FETCH - 100)) | (1 << (MParser.MUTABLE - 100)) | (1 << (MParser.NONE - 100)) | (1 << (MParser.NOT - 100)) | (1 << (MParser.READ - 100)) | (1 << (MParser.SELF - 100)) | (1 << (MParser.SORTED - 100)) | (1 << (MParser.THIS - 100)) | (1 << (MParser.BOOLEAN_LITERAL - 100)) | (1 << (MParser.CHAR_LITERAL - 100)) | (1 << (MParser.MIN_INTEGER - 100)) | (1 << (MParser.MAX_INTEGER - 100)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (MParser.SYMBOL_IDENTIFIER - 164)) | (1 << (MParser.TYPE_IDENTIFIER - 164)) | (1 << (MParser.VARIABLE_IDENTIFIER - 164)) | (1 << (MParser.TEXT_LITERAL - 164)) | (1 << (MParser.UUID_LITERAL - 164)) | (1 << (MParser.INTEGER_LITERAL - 164)) | (1 << (MParser.HEXA_LITERAL - 164)) | (1 << (MParser.DECIMAL_LITERAL - 164)) | (1 << (MParser.DATETIME_LITERAL - 164)) | (1 << (MParser.TIME_LITERAL - 164)) | (1 << (MParser.DATE_LITERAL - 164)) | (1 << (MParser.PERIOD_LITERAL - 164)) | (1 << (MParser.VERSION_LITERAL - 164)))) != 0):
                    self.state = 2480
                    localctx.exp = self.expression(0)


                self.state = 2483
                self.match(MParser.RCURL)
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
            super(MParser.Jsx_textContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LCURL(self, i=None):
            if i is None:
                return self.getTokens(MParser.LCURL)
            else:
                return self.getToken(MParser.LCURL, i)

        def RCURL(self, i=None):
            if i is None:
                return self.getTokens(MParser.RCURL)
            else:
                return self.getToken(MParser.RCURL, i)

        def LT(self, i=None):
            if i is None:
                return self.getTokens(MParser.LT)
            else:
                return self.getToken(MParser.LT, i)

        def GT(self, i=None):
            if i is None:
                return self.getTokens(MParser.GT)
            else:
                return self.getToken(MParser.GT, i)

        def getRuleIndex(self):
            return MParser.RULE_jsx_text

        def enterRule(self, listener):
            if hasattr(listener, "enterJsx_text"):
                listener.enterJsx_text(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitJsx_text"):
                listener.exitJsx_text(self)




    def jsx_text(self):

        localctx = MParser.Jsx_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 458, self.RULE_jsx_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2487 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 2486
                    _la = self._input.LA(1)
                    if _la <= 0 or (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LCURL) | (1 << MParser.RCURL) | (1 << MParser.GT) | (1 << MParser.LT))) != 0):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 2489 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,207,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Css_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Css_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.field = None # Css_fieldContext

        def LCURL(self):
            return self.getToken(MParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(MParser.RCURL, 0)

        def css_field(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Css_fieldContext)
            else:
                return self.getTypedRuleContext(MParser.Css_fieldContext,i)


        def getRuleIndex(self):
            return MParser.RULE_css_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterCss_expression"):
                listener.enterCss_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCss_expression"):
                listener.exitCss_expression(self)




    def css_expression(self):

        localctx = MParser.Css_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 460, self.RULE_css_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2491
            self.match(MParser.LCURL)
            self.state = 2493 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2492
                localctx.field = self.css_field()
                self.state = 2495 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.JAVA) | (1 << MParser.CSHARP) | (1 << MParser.PYTHON2) | (1 << MParser.PYTHON3) | (1 << MParser.JAVASCRIPT) | (1 << MParser.SWIFT) | (1 << MParser.MINUS) | (1 << MParser.BOOLEAN) | (1 << MParser.CHARACTER) | (1 << MParser.TEXT) | (1 << MParser.INTEGER) | (1 << MParser.DECIMAL) | (1 << MParser.DATE) | (1 << MParser.TIME) | (1 << MParser.DATETIME) | (1 << MParser.PERIOD) | (1 << MParser.VERSION) | (1 << MParser.METHOD_T) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (MParser.IMAGE - 64)) | (1 << (MParser.UUID - 64)) | (1 << (MParser.ITERATOR - 64)) | (1 << (MParser.CURSOR - 64)) | (1 << (MParser.HTML - 64)) | (1 << (MParser.ABSTRACT - 64)) | (1 << (MParser.ALL - 64)) | (1 << (MParser.ALWAYS - 64)) | (1 << (MParser.AND - 64)) | (1 << (MParser.ANY - 64)) | (1 << (MParser.AS - 64)) | (1 << (MParser.ASC - 64)) | (1 << (MParser.ATTR - 64)) | (1 << (MParser.ATTRIBUTE - 64)) | (1 << (MParser.ATTRIBUTES - 64)) | (1 << (MParser.BINDINGS - 64)) | (1 << (MParser.BREAK - 64)) | (1 << (MParser.BY - 64)) | (1 << (MParser.CASE - 64)) | (1 << (MParser.CATCH - 64)) | (1 << (MParser.CATEGORY - 64)) | (1 << (MParser.CLASS - 64)) | (1 << (MParser.CLOSE - 64)) | (1 << (MParser.CONTAINS - 64)) | (1 << (MParser.DEF - 64)) | (1 << (MParser.DEFAULT - 64)) | (1 << (MParser.DEFINE - 64)) | (1 << (MParser.DELETE - 64)) | (1 << (MParser.DESC - 64)) | (1 << (MParser.DO - 64)) | (1 << (MParser.DOING - 64)) | (1 << (MParser.EACH - 64)) | (1 << (MParser.ELSE - 64)) | (1 << (MParser.ENUM - 64)) | (1 << (MParser.ENUMERATED - 64)) | (1 << (MParser.EXCEPT - 64)) | (1 << (MParser.EXECUTE - 64)) | (1 << (MParser.EXPECTING - 64)) | (1 << (MParser.EXTENDS - 64)) | (1 << (MParser.FETCH - 64)) | (1 << (MParser.FILTERED - 64)) | (1 << (MParser.FINALLY - 64)) | (1 << (MParser.FLUSH - 64)) | (1 << (MParser.FOR - 64)) | (1 << (MParser.FROM - 64)) | (1 << (MParser.GETTER - 64)) | (1 << (MParser.HAS - 64)) | (1 << (MParser.IF - 64)) | (1 << (MParser.IN - 64)) | (1 << (MParser.INDEX - 64)) | (1 << (MParser.INVOKE - 64)) | (1 << (MParser.IS - 64)) | (1 << (MParser.MATCHING - 64)) | (1 << (MParser.METHOD - 64)) | (1 << (MParser.METHODS - 64)) | (1 << (MParser.MODULO - 64)) | (1 << (MParser.MUTABLE - 64)) | (1 << (MParser.NATIVE - 64)) | (1 << (MParser.NONE - 64)) | (1 << (MParser.NOT - 64)) | (1 << (MParser.NOTHING - 64)) | (1 << (MParser.NULL - 64)) | (1 << (MParser.ON - 64)) | (1 << (MParser.ONE - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (MParser.OPEN - 128)) | (1 << (MParser.OPERATOR - 128)) | (1 << (MParser.OR - 128)) | (1 << (MParser.ORDER - 128)) | (1 << (MParser.OTHERWISE - 128)) | (1 << (MParser.PASS - 128)) | (1 << (MParser.RAISE - 128)) | (1 << (MParser.READ - 128)) | (1 << (MParser.RECEIVING - 128)) | (1 << (MParser.RESOURCE - 128)) | (1 << (MParser.RETURN - 128)) | (1 << (MParser.RETURNING - 128)) | (1 << (MParser.ROWS - 128)) | (1 << (MParser.SELF - 128)) | (1 << (MParser.SETTER - 128)) | (1 << (MParser.SINGLETON - 128)) | (1 << (MParser.SORTED - 128)) | (1 << (MParser.STORABLE - 128)) | (1 << (MParser.STORE - 128)) | (1 << (MParser.SWITCH - 128)) | (1 << (MParser.TEST - 128)) | (1 << (MParser.THIS - 128)) | (1 << (MParser.THROW - 128)) | (1 << (MParser.TO - 128)) | (1 << (MParser.TRY - 128)) | (1 << (MParser.VERIFYING - 128)) | (1 << (MParser.WIDGET - 128)) | (1 << (MParser.WITH - 128)) | (1 << (MParser.WHEN - 128)) | (1 << (MParser.WHERE - 128)) | (1 << (MParser.WHILE - 128)) | (1 << (MParser.WRITE - 128)) | (1 << (MParser.SYMBOL_IDENTIFIER - 128)) | (1 << (MParser.TYPE_IDENTIFIER - 128)) | (1 << (MParser.VARIABLE_IDENTIFIER - 128)))) != 0)):
                    break

            self.state = 2497
            self.match(MParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Css_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Css_fieldContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Css_identifierContext
            self.value = None # Css_valueContext

        def COLON(self):
            return self.getToken(MParser.COLON, 0)

        def SEMI(self):
            return self.getToken(MParser.SEMI, 0)

        def css_identifier(self):
            return self.getTypedRuleContext(MParser.Css_identifierContext,0)


        def css_value(self):
            return self.getTypedRuleContext(MParser.Css_valueContext,0)


        def getRuleIndex(self):
            return MParser.RULE_css_field

        def enterRule(self, listener):
            if hasattr(listener, "enterCss_field"):
                listener.enterCss_field(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCss_field"):
                listener.exitCss_field(self)




    def css_field(self):

        localctx = MParser.Css_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 462, self.RULE_css_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2499
            localctx.name = self.css_identifier(0)
            self.state = 2500
            self.match(MParser.COLON)
            self.state = 2501
            localctx.value = self.css_value()
            self.state = 2502
            self.match(MParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Css_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Css_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier_or_keyword(self):
            return self.getTypedRuleContext(MParser.Identifier_or_keywordContext,0)


        def MINUS(self):
            return self.getToken(MParser.MINUS, 0)

        def nospace_identifier_or_keyword(self):
            return self.getTypedRuleContext(MParser.Nospace_identifier_or_keywordContext,0)


        def css_identifier(self):
            return self.getTypedRuleContext(MParser.Css_identifierContext,0)


        def nospace_hyphen_identifier_or_keyword(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.Nospace_hyphen_identifier_or_keywordContext)
            else:
                return self.getTypedRuleContext(MParser.Nospace_hyphen_identifier_or_keywordContext,i)


        def getRuleIndex(self):
            return MParser.RULE_css_identifier

        def enterRule(self, listener):
            if hasattr(listener, "enterCss_identifier"):
                listener.enterCss_identifier(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCss_identifier"):
                listener.exitCss_identifier(self)



    def css_identifier(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Css_identifierContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 464
        self.enterRecursionRule(localctx, 464, self.RULE_css_identifier, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2508
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.JAVA, MParser.CSHARP, MParser.PYTHON2, MParser.PYTHON3, MParser.JAVASCRIPT, MParser.SWIFT, MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.VERSION, MParser.METHOD_T, MParser.CODE, MParser.DOCUMENT, MParser.BLOB, MParser.IMAGE, MParser.UUID, MParser.ITERATOR, MParser.CURSOR, MParser.HTML, MParser.ABSTRACT, MParser.ALL, MParser.ALWAYS, MParser.AND, MParser.ANY, MParser.AS, MParser.ASC, MParser.ATTR, MParser.ATTRIBUTE, MParser.ATTRIBUTES, MParser.BINDINGS, MParser.BREAK, MParser.BY, MParser.CASE, MParser.CATCH, MParser.CATEGORY, MParser.CLASS, MParser.CLOSE, MParser.CONTAINS, MParser.DEF, MParser.DEFAULT, MParser.DEFINE, MParser.DELETE, MParser.DESC, MParser.DO, MParser.DOING, MParser.EACH, MParser.ELSE, MParser.ENUM, MParser.ENUMERATED, MParser.EXCEPT, MParser.EXECUTE, MParser.EXPECTING, MParser.EXTENDS, MParser.FETCH, MParser.FILTERED, MParser.FINALLY, MParser.FLUSH, MParser.FOR, MParser.FROM, MParser.GETTER, MParser.HAS, MParser.IF, MParser.IN, MParser.INDEX, MParser.INVOKE, MParser.IS, MParser.MATCHING, MParser.METHOD, MParser.METHODS, MParser.MODULO, MParser.MUTABLE, MParser.NATIVE, MParser.NONE, MParser.NOT, MParser.NOTHING, MParser.NULL, MParser.ON, MParser.ONE, MParser.OPEN, MParser.OPERATOR, MParser.OR, MParser.ORDER, MParser.OTHERWISE, MParser.PASS, MParser.RAISE, MParser.READ, MParser.RECEIVING, MParser.RESOURCE, MParser.RETURN, MParser.RETURNING, MParser.ROWS, MParser.SELF, MParser.SETTER, MParser.SINGLETON, MParser.SORTED, MParser.STORABLE, MParser.STORE, MParser.SWITCH, MParser.TEST, MParser.THIS, MParser.THROW, MParser.TO, MParser.TRY, MParser.VERIFYING, MParser.WIDGET, MParser.WITH, MParser.WHEN, MParser.WHERE, MParser.WHILE, MParser.WRITE, MParser.SYMBOL_IDENTIFIER, MParser.TYPE_IDENTIFIER, MParser.VARIABLE_IDENTIFIER]:
                self.state = 2505
                self.identifier_or_keyword()
                pass
            elif token in [MParser.MINUS]:
                self.state = 2506
                self.match(MParser.MINUS)
                self.state = 2507
                self.nospace_identifier_or_keyword()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2518
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,211,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.Css_identifierContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_css_identifier)
                    self.state = 2510
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2512 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 2511
                            self.nospace_hyphen_identifier_or_keyword()

                        else:
                            raise NoViableAltException(self)
                        self.state = 2514 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,210,self._ctx)
             
                self.state = 2520
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,211,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Css_valueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Css_valueContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_css_value

     
        def copyFrom(self, ctx):
            super(MParser.Css_valueContext, self).copyFrom(ctx)



    class CssTextContext(Css_valueContext):

        def __init__(self, parser, ctx): # actually a MParser.Css_valueContext)
            super(MParser.CssTextContext, self).__init__(parser)
            self.text = None # Css_textContext
            self.copyFrom(ctx)

        def css_text(self):
            return self.getTypedRuleContext(MParser.Css_textContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCssText"):
                listener.enterCssText(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCssText"):
                listener.exitCssText(self)


    class CssValueContext(Css_valueContext):

        def __init__(self, parser, ctx): # actually a MParser.Css_valueContext)
            super(MParser.CssValueContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(MParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(MParser.RCURL, 0)
        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCssValue"):
                listener.enterCssValue(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCssValue"):
                listener.exitCssValue(self)



    def css_value(self):

        localctx = MParser.Css_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 466, self.RULE_css_value)
        try:
            self.state = 2526
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MParser.LCURL]:
                localctx = MParser.CssValueContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2521
                self.match(MParser.LCURL)
                self.state = 2522
                localctx.exp = self.expression(0)
                self.state = 2523
                self.match(MParser.RCURL)
                pass
            elif token in [MParser.INDENT, MParser.DEDENT, MParser.LF_TAB, MParser.LF_MORE, MParser.LF, MParser.TAB, MParser.COMMENT, MParser.JAVA, MParser.CSHARP, MParser.PYTHON2, MParser.PYTHON3, MParser.JAVASCRIPT, MParser.SWIFT, MParser.COMMA, MParser.RANGE, MParser.DOT, MParser.LPAR, MParser.RPAR, MParser.LBRAK, MParser.RBRAK, MParser.QMARK, MParser.XMARK, MParser.AMP, MParser.AMP2, MParser.PIPE, MParser.PIPE2, MParser.PLUS, MParser.MINUS, MParser.STAR, MParser.SLASH, MParser.BSLASH, MParser.PERCENT, MParser.GT, MParser.GTE, MParser.LT, MParser.LTE, MParser.LTGT, MParser.EQ, MParser.XEQ, MParser.EQ2, MParser.TEQ, MParser.TILDE, MParser.LARROW, MParser.RARROW, MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.VERSION, MParser.METHOD_T, MParser.CODE, MParser.DOCUMENT, MParser.BLOB, MParser.IMAGE, MParser.UUID, MParser.ITERATOR, MParser.CURSOR, MParser.HTML, MParser.ABSTRACT, MParser.ALL, MParser.ALWAYS, MParser.AND, MParser.ANY, MParser.AS, MParser.ASC, MParser.ATTR, MParser.ATTRIBUTE, MParser.ATTRIBUTES, MParser.BINDINGS, MParser.BREAK, MParser.BY, MParser.CASE, MParser.CATCH, MParser.CATEGORY, MParser.CLASS, MParser.CLOSE, MParser.CONTAINS, MParser.DEF, MParser.DEFAULT, MParser.DEFINE, MParser.DELETE, MParser.DESC, MParser.DO, MParser.DOING, MParser.EACH, MParser.ELSE, MParser.ENUM, MParser.ENUMERATED, MParser.EXCEPT, MParser.EXECUTE, MParser.EXPECTING, MParser.EXTENDS, MParser.FETCH, MParser.FILTERED, MParser.FINALLY, MParser.FLUSH, MParser.FOR, MParser.FROM, MParser.GETTER, MParser.HAS, MParser.IF, MParser.IN, MParser.INDEX, MParser.INVOKE, MParser.IS, MParser.MATCHING, MParser.METHOD, MParser.METHODS, MParser.MODULO, MParser.MUTABLE, MParser.NATIVE, MParser.NONE, MParser.NOT, MParser.NOTHING, MParser.NULL, MParser.ON, MParser.ONE, MParser.OPEN, MParser.OPERATOR, MParser.OR, MParser.ORDER, MParser.OTHERWISE, MParser.PASS, MParser.RAISE, MParser.READ, MParser.RECEIVING, MParser.RESOURCE, MParser.RETURN, MParser.RETURNING, MParser.ROWS, MParser.SELF, MParser.SETTER, MParser.SINGLETON, MParser.SORTED, MParser.STORABLE, MParser.STORE, MParser.SWITCH, MParser.TEST, MParser.THIS, MParser.THROW, MParser.TO, MParser.TRY, MParser.VERIFYING, MParser.WIDGET, MParser.WITH, MParser.WHEN, MParser.WHERE, MParser.WHILE, MParser.WRITE, MParser.BOOLEAN_LITERAL, MParser.CHAR_LITERAL, MParser.MIN_INTEGER, MParser.MAX_INTEGER, MParser.SYMBOL_IDENTIFIER, MParser.TYPE_IDENTIFIER, MParser.VARIABLE_IDENTIFIER, MParser.NATIVE_IDENTIFIER, MParser.DOLLAR_IDENTIFIER, MParser.TEXT_LITERAL, MParser.UUID_LITERAL, MParser.INTEGER_LITERAL, MParser.HEXA_LITERAL, MParser.DECIMAL_LITERAL, MParser.DATETIME_LITERAL, MParser.TIME_LITERAL, MParser.DATE_LITERAL, MParser.PERIOD_LITERAL, MParser.VERSION_LITERAL]:
                localctx = MParser.CssTextContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2525
                localctx.text = self.css_text()
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

    class Css_textContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(MParser.Css_textContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LCURL(self, i=None):
            if i is None:
                return self.getTokens(MParser.LCURL)
            else:
                return self.getToken(MParser.LCURL, i)

        def RCURL(self, i=None):
            if i is None:
                return self.getTokens(MParser.RCURL)
            else:
                return self.getToken(MParser.RCURL, i)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(MParser.COLON)
            else:
                return self.getToken(MParser.COLON, i)

        def SEMI(self, i=None):
            if i is None:
                return self.getTokens(MParser.SEMI)
            else:
                return self.getToken(MParser.SEMI, i)

        def WS(self, i=None):
            if i is None:
                return self.getTokens(MParser.WS)
            else:
                return self.getToken(MParser.WS, i)

        def getRuleIndex(self):
            return MParser.RULE_css_text

        def enterRule(self, listener):
            if hasattr(listener, "enterCss_text"):
                listener.enterCss_text(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCss_text"):
                listener.exitCss_text(self)




    def css_text(self):

        localctx = MParser.Css_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 468, self.RULE_css_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2529 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2528
                _la = self._input.LA(1)
                if _la <= 0 or (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.WS) | (1 << MParser.COLON) | (1 << MParser.SEMI) | (1 << MParser.LCURL) | (1 << MParser.RCURL))) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 2531 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.INDENT) | (1 << MParser.DEDENT) | (1 << MParser.LF_TAB) | (1 << MParser.LF_MORE) | (1 << MParser.LF) | (1 << MParser.TAB) | (1 << MParser.COMMENT) | (1 << MParser.JAVA) | (1 << MParser.CSHARP) | (1 << MParser.PYTHON2) | (1 << MParser.PYTHON3) | (1 << MParser.JAVASCRIPT) | (1 << MParser.SWIFT) | (1 << MParser.COMMA) | (1 << MParser.RANGE) | (1 << MParser.DOT) | (1 << MParser.LPAR) | (1 << MParser.RPAR) | (1 << MParser.LBRAK) | (1 << MParser.RBRAK) | (1 << MParser.QMARK) | (1 << MParser.XMARK) | (1 << MParser.AMP) | (1 << MParser.AMP2) | (1 << MParser.PIPE) | (1 << MParser.PIPE2) | (1 << MParser.PLUS) | (1 << MParser.MINUS) | (1 << MParser.STAR) | (1 << MParser.SLASH) | (1 << MParser.BSLASH) | (1 << MParser.PERCENT) | (1 << MParser.GT) | (1 << MParser.GTE) | (1 << MParser.LT) | (1 << MParser.LTE) | (1 << MParser.LTGT) | (1 << MParser.EQ) | (1 << MParser.XEQ) | (1 << MParser.EQ2) | (1 << MParser.TEQ) | (1 << MParser.TILDE) | (1 << MParser.LARROW) | (1 << MParser.RARROW) | (1 << MParser.BOOLEAN) | (1 << MParser.CHARACTER) | (1 << MParser.TEXT) | (1 << MParser.INTEGER) | (1 << MParser.DECIMAL) | (1 << MParser.DATE) | (1 << MParser.TIME) | (1 << MParser.DATETIME) | (1 << MParser.PERIOD) | (1 << MParser.VERSION) | (1 << MParser.METHOD_T) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (MParser.IMAGE - 64)) | (1 << (MParser.UUID - 64)) | (1 << (MParser.ITERATOR - 64)) | (1 << (MParser.CURSOR - 64)) | (1 << (MParser.HTML - 64)) | (1 << (MParser.ABSTRACT - 64)) | (1 << (MParser.ALL - 64)) | (1 << (MParser.ALWAYS - 64)) | (1 << (MParser.AND - 64)) | (1 << (MParser.ANY - 64)) | (1 << (MParser.AS - 64)) | (1 << (MParser.ASC - 64)) | (1 << (MParser.ATTR - 64)) | (1 << (MParser.ATTRIBUTE - 64)) | (1 << (MParser.ATTRIBUTES - 64)) | (1 << (MParser.BINDINGS - 64)) | (1 << (MParser.BREAK - 64)) | (1 << (MParser.BY - 64)) | (1 << (MParser.CASE - 64)) | (1 << (MParser.CATCH - 64)) | (1 << (MParser.CATEGORY - 64)) | (1 << (MParser.CLASS - 64)) | (1 << (MParser.CLOSE - 64)) | (1 << (MParser.CONTAINS - 64)) | (1 << (MParser.DEF - 64)) | (1 << (MParser.DEFAULT - 64)) | (1 << (MParser.DEFINE - 64)) | (1 << (MParser.DELETE - 64)) | (1 << (MParser.DESC - 64)) | (1 << (MParser.DO - 64)) | (1 << (MParser.DOING - 64)) | (1 << (MParser.EACH - 64)) | (1 << (MParser.ELSE - 64)) | (1 << (MParser.ENUM - 64)) | (1 << (MParser.ENUMERATED - 64)) | (1 << (MParser.EXCEPT - 64)) | (1 << (MParser.EXECUTE - 64)) | (1 << (MParser.EXPECTING - 64)) | (1 << (MParser.EXTENDS - 64)) | (1 << (MParser.FETCH - 64)) | (1 << (MParser.FILTERED - 64)) | (1 << (MParser.FINALLY - 64)) | (1 << (MParser.FLUSH - 64)) | (1 << (MParser.FOR - 64)) | (1 << (MParser.FROM - 64)) | (1 << (MParser.GETTER - 64)) | (1 << (MParser.HAS - 64)) | (1 << (MParser.IF - 64)) | (1 << (MParser.IN - 64)) | (1 << (MParser.INDEX - 64)) | (1 << (MParser.INVOKE - 64)) | (1 << (MParser.IS - 64)) | (1 << (MParser.MATCHING - 64)) | (1 << (MParser.METHOD - 64)) | (1 << (MParser.METHODS - 64)) | (1 << (MParser.MODULO - 64)) | (1 << (MParser.MUTABLE - 64)) | (1 << (MParser.NATIVE - 64)) | (1 << (MParser.NONE - 64)) | (1 << (MParser.NOT - 64)) | (1 << (MParser.NOTHING - 64)) | (1 << (MParser.NULL - 64)) | (1 << (MParser.ON - 64)) | (1 << (MParser.ONE - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (MParser.OPEN - 128)) | (1 << (MParser.OPERATOR - 128)) | (1 << (MParser.OR - 128)) | (1 << (MParser.ORDER - 128)) | (1 << (MParser.OTHERWISE - 128)) | (1 << (MParser.PASS - 128)) | (1 << (MParser.RAISE - 128)) | (1 << (MParser.READ - 128)) | (1 << (MParser.RECEIVING - 128)) | (1 << (MParser.RESOURCE - 128)) | (1 << (MParser.RETURN - 128)) | (1 << (MParser.RETURNING - 128)) | (1 << (MParser.ROWS - 128)) | (1 << (MParser.SELF - 128)) | (1 << (MParser.SETTER - 128)) | (1 << (MParser.SINGLETON - 128)) | (1 << (MParser.SORTED - 128)) | (1 << (MParser.STORABLE - 128)) | (1 << (MParser.STORE - 128)) | (1 << (MParser.SWITCH - 128)) | (1 << (MParser.TEST - 128)) | (1 << (MParser.THIS - 128)) | (1 << (MParser.THROW - 128)) | (1 << (MParser.TO - 128)) | (1 << (MParser.TRY - 128)) | (1 << (MParser.VERIFYING - 128)) | (1 << (MParser.WIDGET - 128)) | (1 << (MParser.WITH - 128)) | (1 << (MParser.WHEN - 128)) | (1 << (MParser.WHERE - 128)) | (1 << (MParser.WHILE - 128)) | (1 << (MParser.WRITE - 128)) | (1 << (MParser.BOOLEAN_LITERAL - 128)) | (1 << (MParser.CHAR_LITERAL - 128)) | (1 << (MParser.MIN_INTEGER - 128)) | (1 << (MParser.MAX_INTEGER - 128)) | (1 << (MParser.SYMBOL_IDENTIFIER - 128)) | (1 << (MParser.TYPE_IDENTIFIER - 128)) | (1 << (MParser.VARIABLE_IDENTIFIER - 128)) | (1 << (MParser.NATIVE_IDENTIFIER - 128)) | (1 << (MParser.DOLLAR_IDENTIFIER - 128)) | (1 << (MParser.TEXT_LITERAL - 128)) | (1 << (MParser.UUID_LITERAL - 128)) | (1 << (MParser.INTEGER_LITERAL - 128)) | (1 << (MParser.HEXA_LITERAL - 128)) | (1 << (MParser.DECIMAL_LITERAL - 128)) | (1 << (MParser.DATETIME_LITERAL - 128)) | (1 << (MParser.TIME_LITERAL - 128)) | (1 << (MParser.DATE_LITERAL - 128)) | (1 << (MParser.PERIOD_LITERAL - 128)) | (1 << (MParser.VERSION_LITERAL - 128)))) != 0)):
                    break

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
        self._predicates[19] = self.native_category_binding_list_sempred
        self._predicates[31] = self.callable_parent_sempred
        self._predicates[41] = self.else_if_statement_list_sempred
        self._predicates[47] = self.expression_sempred
        self._predicates[49] = self.instance_expression_sempred
        self._predicates[51] = self.instance_selector_sempred
        self._predicates[55] = self.copy_from_sempred
        self._predicates[56] = self.argument_assignment_list_sempred
        self._predicates[63] = self.child_instance_sempred
        self._predicates[83] = self.typedef_sempred
        self._predicates[94] = self.nospace_hyphen_identifier_or_keyword_sempred
        self._predicates[95] = self.nospace_identifier_or_keyword_sempred
        self._predicates[107] = self.any_type_sempred
        self._predicates[144] = self.assignable_instance_sempred
        self._predicates[145] = self.is_expression_sempred
        self._predicates[152] = self.new_token_sempred
        self._predicates[153] = self.key_token_sempred
        self._predicates[154] = self.module_token_sempred
        self._predicates[155] = self.value_token_sempred
        self._predicates[156] = self.symbols_token_sempred
        self._predicates[163] = self.javascript_expression_sempred
        self._predicates[169] = self.javascript_arguments_sempred
        self._predicates[176] = self.python_expression_sempred
        self._predicates[182] = self.python_ordinal_argument_list_sempred
        self._predicates[183] = self.python_named_argument_list_sempred
        self._predicates[185] = self.python_identifier_expression_sempred
        self._predicates[189] = self.java_expression_sempred
        self._predicates[195] = self.java_arguments_sempred
        self._predicates[198] = self.java_identifier_expression_sempred
        self._predicates[199] = self.java_class_identifier_expression_sempred
        self._predicates[203] = self.csharp_expression_sempred
        self._predicates[209] = self.csharp_arguments_sempred
        self._predicates[212] = self.csharp_identifier_expression_sempred
        self._predicates[232] = self.css_identifier_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def native_category_binding_list_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def callable_parent_sempred(self, localctx, predIndex):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def else_if_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx, predIndex):
            if predIndex == 3:
                return self.precpred(self._ctx, 32)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 31)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 30)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 29)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 25)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 23:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 24:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 25:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 26:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 27:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 28:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 29:
                return self.precpred(self._ctx, 36)
         

            if predIndex == 30:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 31:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 32:
                return self.precpred(self._ctx, 21)
         

    def instance_expression_sempred(self, localctx, predIndex):
            if predIndex == 33:
                return self.precpred(self._ctx, 1)
         

    def instance_selector_sempred(self, localctx, predIndex):
            if predIndex == 34:
                return self.wasNot(MParser.WS)
         

            if predIndex == 35:
                return self.wasNot(MParser.WS)
         

            if predIndex == 36:
                return self.wasNot(MParser.WS)
         

    def copy_from_sempred(self, localctx, predIndex):
            if predIndex == 37:
                return self.willNotBe(self.equalToken())
         

    def argument_assignment_list_sempred(self, localctx, predIndex):
            if predIndex == 38:
                return self.willNotBe(self.equalToken())
         

            if predIndex == 39:
                return self.precpred(self._ctx, 1)
         

    def child_instance_sempred(self, localctx, predIndex):
            if predIndex == 40:
                return self.wasNot(MParser.WS)
         

            if predIndex == 41:
                return self.wasNot(MParser.WS)
         

    def typedef_sempred(self, localctx, predIndex):
            if predIndex == 42:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 43:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 44:
                return self.precpred(self._ctx, 3)
         

    def nospace_hyphen_identifier_or_keyword_sempred(self, localctx, predIndex):
            if predIndex == 45:
                return self.wasNotWhiteSpace()
         

    def nospace_identifier_or_keyword_sempred(self, localctx, predIndex):
            if predIndex == 46:
                return self.wasNotWhiteSpace()
         

    def any_type_sempred(self, localctx, predIndex):
            if predIndex == 47:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 48:
                return self.precpred(self._ctx, 1)
         

    def assignable_instance_sempred(self, localctx, predIndex):
            if predIndex == 49:
                return self.precpred(self._ctx, 1)
         

    def is_expression_sempred(self, localctx, predIndex):
            if predIndex == 50:
                return self.willBeAOrAn()
         

    def new_token_sempred(self, localctx, predIndex):
            if predIndex == 51:
                return self.isText(localctx.i1,"new")
         

    def key_token_sempred(self, localctx, predIndex):
            if predIndex == 52:
                return self.isText(localctx.i1,"key")
         

    def module_token_sempred(self, localctx, predIndex):
            if predIndex == 53:
                return self.isText(localctx.i1,"module")
         

    def value_token_sempred(self, localctx, predIndex):
            if predIndex == 54:
                return self.isText(localctx.i1,"value")
         

    def symbols_token_sempred(self, localctx, predIndex):
            if predIndex == 55:
                return self.isText(localctx.i1,"symbols")
         

    def javascript_expression_sempred(self, localctx, predIndex):
            if predIndex == 56:
                return self.precpred(self._ctx, 1)
         

    def javascript_arguments_sempred(self, localctx, predIndex):
            if predIndex == 57:
                return self.precpred(self._ctx, 1)
         

    def python_expression_sempred(self, localctx, predIndex):
            if predIndex == 58:
                return self.precpred(self._ctx, 1)
         

    def python_ordinal_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 59:
                return self.precpred(self._ctx, 1)
         

    def python_named_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 60:
                return self.precpred(self._ctx, 1)
         

    def python_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 61:
                return self.precpred(self._ctx, 1)
         

    def java_expression_sempred(self, localctx, predIndex):
            if predIndex == 62:
                return self.precpred(self._ctx, 1)
         

    def java_arguments_sempred(self, localctx, predIndex):
            if predIndex == 63:
                return self.precpred(self._ctx, 1)
         

    def java_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 64:
                return self.precpred(self._ctx, 1)
         

    def java_class_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 65:
                return self.precpred(self._ctx, 1)
         

    def csharp_expression_sempred(self, localctx, predIndex):
            if predIndex == 66:
                return self.precpred(self._ctx, 1)
         

    def csharp_arguments_sempred(self, localctx, predIndex):
            if predIndex == 67:
                return self.precpred(self._ctx, 1)
         

    def csharp_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 68:
                return self.precpred(self._ctx, 1)
         

    def css_identifier_sempred(self, localctx, predIndex):
            if predIndex == 69:
                return self.precpred(self._ctx, 1)
         




