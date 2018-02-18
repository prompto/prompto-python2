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
        buf.write(u"\u00ae\u08e0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
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
        buf.write(u"\4\u00cf\t\u00cf\4\u00d0\t\u00d0\3\2\3\2\3\2\3\2\3\2")
        buf.write(u"\3\2\3\2\5\2\u01a8\n\2\3\2\3\2\5\2\u01ac\n\2\3\2\3\2")
        buf.write(u"\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4")
        buf.write(u"\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\5\6\u01c7\n")
        buf.write(u"\6\3\6\3\6\3\6\3\6\3\6\5\6\u01ce\n\6\3\6\3\6\3\6\3\6")
        buf.write(u"\3\6\3\6\5\6\u01d6\n\6\5\6\u01d8\n\6\3\6\3\6\3\7\5\7")
        buf.write(u"\u01dd\n\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u01e5\n\7\3\7")
        buf.write(u"\3\7\5\7\u01e9\n\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\5")
        buf.write(u"\b\u01f3\n\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u01fd")
        buf.write(u"\n\t\f\t\16\t\u0200\13\t\3\n\3\n\3\n\5\n\u0205\n\n\3")
        buf.write(u"\n\5\n\u0208\n\n\3\13\5\13\u020b\n\13\3\13\3\13\3\13")
        buf.write(u"\3\13\3\13\3\13\3\13\5\13\u0214\n\13\3\13\3\13\3\f\3")
        buf.write(u"\f\3\f\3\f\5\f\u021c\n\f\3\f\3\f\3\r\5\r\u0221\n\r\3")
        buf.write(u"\r\3\r\3\r\3\r\5\r\u0227\n\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write(u"\16\5\16\u022f\n\16\3\16\3\16\3\17\5\17\u0234\n\17\3")
        buf.write(u"\17\3\17\3\17\3\17\5\17\u023a\n\17\3\17\3\17\3\20\3\20")
        buf.write(u"\3\20\3\20\3\20\3\20\3\20\5\20\u0245\n\20\3\20\3\20\3")
        buf.write(u"\20\5\20\u024a\n\20\3\20\3\20\3\21\5\21\u024f\n\21\3")
        buf.write(u"\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u0258\n\21\3\21")
        buf.write(u"\3\21\3\21\5\21\u025d\n\21\3\21\3\21\3\22\3\22\3\22\3")
        buf.write(u"\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write(u"\7\23\u026f\n\23\f\23\16\23\u0272\13\23\3\24\3\24\5\24")
        buf.write(u"\u0276\n\24\3\24\3\24\3\24\3\24\5\24\u027c\n\24\3\24")
        buf.write(u"\3\24\3\24\3\25\5\25\u0282\n\25\3\25\3\25\3\25\3\25\5")
        buf.write(u"\25\u0288\n\25\3\25\3\25\3\25\5\25\u028d\n\25\3\25\3")
        buf.write(u"\25\3\26\5\26\u0292\n\26\3\26\5\26\u0295\n\26\3\26\3")
        buf.write(u"\26\3\26\3\26\5\26\u029b\n\26\3\26\3\26\3\26\3\26\3\26")
        buf.write(u"\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write(u"\27\3\27\3\27\3\27\3\27\3\27\5\27\u02b2\n\27\3\30\3\30")
        buf.write(u"\3\30\3\31\3\31\3\31\3\31\3\31\5\31\u02bc\n\31\3\31\3")
        buf.write(u"\31\3\31\5\31\u02c1\n\31\3\32\3\32\3\32\3\32\3\32\5\32")
        buf.write(u"\u02c8\n\32\5\32\u02ca\n\32\3\33\3\33\3\33\3\33\3\33")
        buf.write(u"\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write(u"\33\3\33\3\33\3\33\3\33\3\33\5\33\u02e1\n\33\3\34\3\34")
        buf.write(u"\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write(u"\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write(u"\3\35\3\35\3\35\3\35\3\35\5\35\u02ff\n\35\3\36\3\36\3")
        buf.write(u"\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3")
        buf.write(u" \3 \3 \3 \3 \3 \3 \3 \5 \u0316\n \5 \u0318\n \3 \3 ")
        buf.write(u"\3!\3!\3!\3!\5!\u0320\n!\3!\3!\3!\3!\3!\5!\u0327\n!\5")
        buf.write(u"!\u0329\n!\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u0331\n\"\3\"")
        buf.write(u"\3\"\3\"\3\"\3\"\3#\3#\3#\5#\u033b\n#\3#\3#\3#\3#\3#")
        buf.write(u"\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\5%\u0350\n")
        buf.write(u"%\3%\3%\5%\u0354\n%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&")
        buf.write(u"\3&\3&\3&\3&\3&\7&\u0366\n&\f&\16&\u0369\13&\3\'\3\'")
        buf.write(u"\3\'\3\'\3(\3(\3(\3(\3(\3(\5(\u0375\n(\3(\3(\5(\u0379")
        buf.write(u"\n(\3(\3(\3(\3(\3(\3(\5(\u0381\n(\3(\5(\u0384\n(\3(\3")
        buf.write(u"(\3(\5(\u0389\n(\3(\5(\u038c\n(\3)\3)\3)\3)\3)\3)\5)")
        buf.write(u"\u0394\n)\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u039f\n)\3)\3")
        buf.write(u")\5)\u03a3\n)\3*\3*\3*\3+\3+\5+\u03aa\n+\3+\3+\3,\3,")
        buf.write(u"\3,\5,\u03b1\n,\3,\3,\3-\3-\3-\3-\3-\5-\u03ba\n-\3.\3")
        buf.write(u".\3.\3.\3.\7.\u03c1\n.\f.\16.\u03c4\13.\3/\3/\3/\3/\3")
        buf.write(u"/\3/\5/\u03cc\n/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write(u"\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\3\60\3\60\3\60\3\60\5\60\u03e5\n\60\3\60\3\60\3")
        buf.write(u"\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write(u"\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write(u"\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write(u"\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write(u"\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write(u"\60\3\60\3\60\3\60\3\60\3\60\3\60\7\60\u0459\n\60\f\60")
        buf.write(u"\16\60\u045c\13\60\3\61\3\61\3\61\3\61\3\62\3\62\3\63")
        buf.write(u"\3\63\3\63\3\63\3\63\7\63\u0469\n\63\f\63\16\63\u046c")
        buf.write(u"\13\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5")
        buf.write(u"\64\u0477\n\64\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write(u"\5\66\u0481\n\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3")
        buf.write(u"\67\3\67\3\67\38\38\38\38\38\38\38\38\38\38\38\38\38")
        buf.write(u"\39\39\39\39\39\39\59\u04a0\n9\39\39\39\39\39\39\39\3")
        buf.write(u"9\39\39\39\59\u04ad\n9\39\39\39\39\59\u04b3\n9\39\39")
        buf.write(u"\39\39\39\39\39\59\u04bc\n9\39\39\39\39\39\59\u04c3\n")
        buf.write(u"9\39\39\39\39\39\39\59\u04cb\n9\59\u04cd\n9\3:\3:\5:")
        buf.write(u"\u04d1\n:\3:\3:\3:\3:\3:\3:\3:\5:\u04da\n:\3:\3:\3;\3")
        buf.write(u";\3;\3;\3;\3;\3;\3;\3;\3;\5;\u04e8\n;\3<\3<\3<\5<\u04ed")
        buf.write(u"\n<\3<\3<\3=\3=\3=\3=\3=\5=\u04f6\n=\3=\3=\3=\7=\u04fb")
        buf.write(u"\n=\f=\16=\u04fe\13=\3>\3>\3>\3>\3?\3?\3?\3?\3?\3@\3")
        buf.write(u"@\3@\3@\3@\3@\5@\u050f\n@\3A\3A\3A\3A\3A\3B\3B\3C\5C")
        buf.write(u"\u0519\nC\3C\3C\3C\3D\3D\3D\3D\7D\u0522\nD\fD\16D\u0525")
        buf.write(u"\13D\3E\3E\3E\7E\u052a\nE\fE\16E\u052d\13E\3E\3E\3E\3")
        buf.write(u"E\3E\5E\u0534\nE\3F\3F\3G\3G\5G\u053a\nG\3H\3H\3H\3H")
        buf.write(u"\7H\u0540\nH\fH\16H\u0543\13H\3I\3I\3I\3I\7I\u0549\n")
        buf.write(u"I\fI\16I\u054c\13I\3J\3J\3J\7J\u0551\nJ\fJ\16J\u0554")
        buf.write(u"\13J\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K\5K\u0560\nK\3L\5L")
        buf.write(u"\u0563\nL\3L\3L\5L\u0567\nL\3L\3L\3M\5M\u056c\nM\3M\3")
        buf.write(u"M\5M\u0570\nM\3M\3M\3N\3N\3N\7N\u0577\nN\fN\16N\u057a")
        buf.write(u"\13N\3O\3O\3O\3O\3O\3O\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P")
        buf.write(u"\3P\3P\5P\u058e\nP\3P\3P\3P\3P\3P\3P\3P\3P\7P\u0598\n")
        buf.write(u"P\fP\16P\u059b\13P\3Q\3Q\5Q\u059f\nQ\3R\3R\3R\3R\3R\3")
        buf.write(u"R\3R\3R\3R\3R\3R\3R\3R\3R\3R\5R\u05b0\nR\3S\3S\3T\5T")
        buf.write(u"\u05b5\nT\3T\3T\3U\3U\3V\3V\3V\5V\u05be\nV\3W\3W\3W\7")
        buf.write(u"W\u05c3\nW\fW\16W\u05c6\13W\3X\3X\5X\u05ca\nX\3Y\3Y\3")
        buf.write(u"Y\5Y\u05cf\nY\3Z\3Z\3[\3[\3\\\3\\\3]\3]\3^\3^\3^\7^\u05dc")
        buf.write(u"\n^\f^\16^\u05df\13^\3_\3_\5_\u05e3\n_\3_\5_\u05e6\n")
        buf.write(u"_\3`\3`\5`\u05ea\n`\3a\3a\3a\5a\u05ef\na\3b\3b\3b\3c")
        buf.write(u"\3c\5c\u05f6\nc\3d\3d\3d\3d\3d\3d\3d\3d\3d\7d\u0601\n")
        buf.write(u"d\fd\16d\u0604\13d\3e\3e\3e\3e\7e\u060a\ne\fe\16e\u060d")
        buf.write(u"\13e\3f\3f\3f\3f\3f\5f\u0614\nf\3g\3g\3g\3g\7g\u061a")
        buf.write(u"\ng\fg\16g\u061d\13g\3h\3h\3h\5h\u0622\nh\3i\3i\3i\3")
        buf.write(u"i\3i\3i\3i\3i\3i\3i\5i\u062e\ni\3j\3j\5j\u0632\nj\3k")
        buf.write(u"\3k\3k\3k\3k\3k\7k\u063a\nk\fk\16k\u063d\13k\3l\3l\5")
        buf.write(u"l\u0641\nl\3m\3m\3m\3m\5m\u0647\nm\3m\3m\3m\7m\u064c")
        buf.write(u"\nm\fm\16m\u064f\13m\3m\3m\5m\u0653\nm\3n\3n\3n\7n\u0658")
        buf.write(u"\nn\fn\16n\u065b\13n\3o\3o\3o\7o\u0660\no\fo\16o\u0663")
        buf.write(u"\13o\3p\3p\3p\3p\5p\u0669\np\3q\3q\3r\3r\3r\3r\7r\u0671")
        buf.write(u"\nr\fr\16r\u0674\13r\3s\3s\3s\3s\3s\3s\3s\3s\3s\3s\5")
        buf.write(u"s\u0680\ns\3t\3t\5t\u0684\nt\3t\5t\u0687\nt\3u\3u\5u")
        buf.write(u"\u068b\nu\3u\5u\u068e\nu\3v\3v\3v\3v\7v\u0694\nv\fv\16")
        buf.write(u"v\u0697\13v\3w\3w\3w\3w\7w\u069d\nw\fw\16w\u06a0\13w")
        buf.write(u"\3x\3x\3x\3x\7x\u06a6\nx\fx\16x\u06a9\13x\3y\3y\3y\3")
        buf.write(u"y\7y\u06af\ny\fy\16y\u06b2\13y\3z\3z\3z\3z\3z\3z\3z\3")
        buf.write(u"z\3z\3z\3z\3z\3z\3z\5z\u06c2\nz\3{\3{\3{\3{\3{\3{\3{")
        buf.write(u"\3{\3{\3{\3{\3{\3{\3{\3{\5{\u06d3\n{\3|\3|\3|\7|\u06d8")
        buf.write(u"\n|\f|\16|\u06db\13|\3}\3}\3}\3}\5}\u06e1\n}\3~\3~\3")
        buf.write(u"\177\3\177\3\177\3\177\3\u0080\3\u0080\5\u0080\u06eb")
        buf.write(u"\n\u0080\3\u0081\3\u0081\3\u0081\3\u0081\3\u0081\5\u0081")
        buf.write(u"\u06f2\n\u0081\3\u0082\5\u0082\u06f5\n\u0082\3\u0082")
        buf.write(u"\3\u0082\5\u0082\u06f9\n\u0082\3\u0082\3\u0082\3\u0083")
        buf.write(u"\5\u0083\u06fe\n\u0083\3\u0083\3\u0083\5\u0083\u0702")
        buf.write(u"\n\u0083\3\u0083\3\u0083\3\u0084\3\u0084\3\u0084\3\u0084")
        buf.write(u"\3\u0084\7\u0084\u070b\n\u0084\f\u0084\16\u0084\u070e")
        buf.write(u"\13\u0084\5\u0084\u0710\n\u0084\3\u0085\3\u0085\3\u0085")
        buf.write(u"\7\u0085\u0715\n\u0085\f\u0085\16\u0085\u0718\13\u0085")
        buf.write(u"\3\u0086\3\u0086\3\u0086\3\u0086\3\u0087\3\u0087\3\u0087")
        buf.write(u"\3\u0087\3\u0087\3\u0087\3\u0087\3\u0087\3\u0087\5\u0087")
        buf.write(u"\u0727\n\u0087\3\u0088\3\u0088\3\u0088\3\u0088\3\u0089")
        buf.write(u"\3\u0089\3\u0089\3\u0089\3\u0089\7\u0089\u0732\n\u0089")
        buf.write(u"\f\u0089\16\u0089\u0735\13\u0089\3\u008a\3\u008a\3\u008a")
        buf.write(u"\3\u008a\5\u008a\u073b\n\u008a\3\u008b\3\u008b\3\u008b")
        buf.write(u"\3\u008b\3\u008b\3\u008c\3\u008c\3\u008c\3\u008c\3\u008c")
        buf.write(u"\3\u008d\3\u008d\3\u008d\7\u008d\u074a\n\u008d\f\u008d")
        buf.write(u"\16\u008d\u074d\13\u008d\3\u008e\3\u008e\3\u008e\7\u008e")
        buf.write(u"\u0752\n\u008e\f\u008e\16\u008e\u0755\13\u008e\3\u008e")
        buf.write(u"\5\u008e\u0758\n\u008e\3\u008f\3\u008f\3\u008f\3\u008f")
        buf.write(u"\3\u008f\3\u008f\5\u008f\u0760\n\u008f\3\u0090\3\u0090")
        buf.write(u"\3\u0090\3\u0091\3\u0091\3\u0091\3\u0092\3\u0092\3\u0092")
        buf.write(u"\3\u0093\3\u0093\3\u0093\3\u0094\3\u0094\3\u0094\3\u0095")
        buf.write(u"\3\u0095\3\u0096\3\u0096\3\u0097\3\u0097\3\u0098\3\u0098")
        buf.write(u"\3\u0099\3\u0099\3\u009a\3\u009a\3\u009b\3\u009b\3\u009c")
        buf.write(u"\3\u009c\3\u009c\3\u009c\3\u009c\3\u009c\3\u009c\5\u009c")
        buf.write(u"\u0786\n\u009c\3\u009d\3\u009d\3\u009d\3\u009d\3\u009d")
        buf.write(u"\7\u009d\u078d\n\u009d\f\u009d\16\u009d\u0790\13\u009d")
        buf.write(u"\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e")
        buf.write(u"\5\u009e\u0799\n\u009e\3\u009f\3\u009f\3\u00a0\3\u00a0")
        buf.write(u"\3\u00a0\3\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1\5\u00a1")
        buf.write(u"\u07a5\n\u00a1\3\u00a2\3\u00a2\3\u00a2\5\u00a2\u07aa")
        buf.write(u"\n\u00a2\3\u00a2\3\u00a2\3\u00a3\3\u00a3\3\u00a3\3\u00a3")
        buf.write(u"\3\u00a3\3\u00a3\7\u00a3\u07b4\n\u00a3\f\u00a3\16\u00a3")
        buf.write(u"\u07b7\13\u00a3\3\u00a4\3\u00a4\3\u00a4\3\u00a4\3\u00a5")
        buf.write(u"\3\u00a5\3\u00a5\3\u00a5\3\u00a6\3\u00a6\3\u00a7\3\u00a7")
        buf.write(u"\3\u00a7\3\u00a7\3\u00a7\5\u00a7\u07c8\n\u00a7\3\u00a8")
        buf.write(u"\3\u00a8\3\u00a9\3\u00a9\3\u00a9\5\u00a9\u07cf\n\u00a9")
        buf.write(u"\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa\7\u00aa\u07d6")
        buf.write(u"\n\u00aa\f\u00aa\16\u00aa\u07d9\13\u00aa\3\u00ab\3\u00ab")
        buf.write(u"\3\u00ab\3\u00ab\3\u00ab\5\u00ab\u07e0\n\u00ab\3\u00ac")
        buf.write(u"\3\u00ac\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad")
        buf.write(u"\5\u00ad\u07ea\n\u00ad\3\u00ae\3\u00ae\3\u00ae\5\u00ae")
        buf.write(u"\u07ef\n\u00ae\3\u00ae\3\u00ae\3\u00af\3\u00af\3\u00af")
        buf.write(u"\3\u00af\3\u00af\3\u00af\5\u00af\u07f9\n\u00af\3\u00b0")
        buf.write(u"\3\u00b0\3\u00b0\3\u00b0\3\u00b0\3\u00b0\7\u00b0\u0801")
        buf.write(u"\n\u00b0\f\u00b0\16\u00b0\u0804\13\u00b0\3\u00b1\3\u00b1")
        buf.write(u"\3\u00b1\3\u00b1\3\u00b1\3\u00b1\3\u00b1\3\u00b1\3\u00b1")
        buf.write(u"\3\u00b1\3\u00b1\7\u00b1\u0811\n\u00b1\f\u00b1\16\u00b1")
        buf.write(u"\u0814\13\u00b1\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b3")
        buf.write(u"\3\u00b3\3\u00b3\5\u00b3\u081d\n\u00b3\3\u00b3\3\u00b3")
        buf.write(u"\3\u00b3\7\u00b3\u0822\n\u00b3\f\u00b3\16\u00b3\u0825")
        buf.write(u"\13\u00b3\3\u00b4\3\u00b4\3\u00b4\3\u00b4\3\u00b4\5\u00b4")
        buf.write(u"\u082c\n\u00b4\3\u00b5\3\u00b5\3\u00b6\3\u00b6\3\u00b6")
        buf.write(u"\3\u00b6\3\u00b6\3\u00b6\3\u00b6\5\u00b6\u0837\n\u00b6")
        buf.write(u"\3\u00b7\3\u00b7\3\u00b7\3\u00b7\3\u00b7\7\u00b7\u083e")
        buf.write(u"\n\u00b7\f\u00b7\16\u00b7\u0841\13\u00b7\3\u00b8\3\u00b8")
        buf.write(u"\3\u00b8\3\u00b8\3\u00b8\5\u00b8\u0848\n\u00b8\3\u00b9")
        buf.write(u"\3\u00b9\3\u00ba\3\u00ba\3\u00ba\3\u00bb\3\u00bb\3\u00bb")
        buf.write(u"\5\u00bb\u0852\n\u00bb\3\u00bc\3\u00bc\3\u00bc\5\u00bc")
        buf.write(u"\u0857\n\u00bc\3\u00bc\3\u00bc\3\u00bd\3\u00bd\3\u00bd")
        buf.write(u"\3\u00bd\3\u00bd\3\u00bd\7\u00bd\u0861\n\u00bd\f\u00bd")
        buf.write(u"\16\u00bd\u0864\13\u00bd\3\u00be\3\u00be\3\u00be\3\u00be")
        buf.write(u"\3\u00bf\3\u00bf\3\u00bf\3\u00bf\3\u00c0\3\u00c0\3\u00c0")
        buf.write(u"\3\u00c0\3\u00c0\3\u00c0\7\u00c0\u0874\n\u00c0\f\u00c0")
        buf.write(u"\16\u00c0\u0877\13\u00c0\3\u00c1\3\u00c1\3\u00c1\3\u00c1")
        buf.write(u"\3\u00c1\7\u00c1\u087e\n\u00c1\f\u00c1\16\u00c1\u0881")
        buf.write(u"\13\u00c1\3\u00c2\3\u00c2\3\u00c2\3\u00c2\3\u00c2\5\u00c2")
        buf.write(u"\u0888\n\u00c2\3\u00c3\3\u00c3\3\u00c4\3\u00c4\3\u00c4")
        buf.write(u"\3\u00c4\3\u00c4\3\u00c4\3\u00c4\5\u00c4\u0893\n\u00c4")
        buf.write(u"\3\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c5\7\u00c5\u089a")
        buf.write(u"\n\u00c5\f\u00c5\16\u00c5\u089d\13\u00c5\3\u00c6\3\u00c6")
        buf.write(u"\3\u00c6\3\u00c6\3\u00c6\5\u00c6\u08a4\n\u00c6\3\u00c7")
        buf.write(u"\3\u00c7\3\u00c8\3\u00c8\3\u00c8\3\u00c9\3\u00c9\3\u00c9")
        buf.write(u"\5\u00c9\u08ae\n\u00c9\3\u00ca\3\u00ca\3\u00ca\5\u00ca")
        buf.write(u"\u08b3\n\u00ca\3\u00ca\3\u00ca\3\u00cb\3\u00cb\3\u00cb")
        buf.write(u"\3\u00cb\3\u00cb\3\u00cb\7\u00cb\u08bd\n\u00cb\f\u00cb")
        buf.write(u"\16\u00cb\u08c0\13\u00cb\3\u00cc\3\u00cc\3\u00cc\3\u00cc")
        buf.write(u"\3\u00cd\3\u00cd\3\u00cd\3\u00cd\3\u00ce\3\u00ce\3\u00ce")
        buf.write(u"\5\u00ce\u08cd\n\u00ce\3\u00ce\3\u00ce\3\u00ce\7\u00ce")
        buf.write(u"\u08d2\n\u00ce\f\u00ce\16\u00ce\u08d5\13\u00ce\3\u00cf")
        buf.write(u"\3\u00cf\3\u00cf\3\u00cf\3\u00cf\5\u00cf\u08dc\n\u00cf")
        buf.write(u"\3\u00d0\3\u00d0\3\u00d0\2\31\20$JZ^dx\u009e\u00c6\u0110")
        buf.write(u"\u0138\u0144\u0152\u015e\u0160\u0164\u016c\u0178\u017e")
        buf.write(u"\u0180\u0188\u0194\u019a\u00d1\2\4\6\b\n\f\16\20\22\24")
        buf.write(u"\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTV")
        buf.write(u"XZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a")
        buf.write(u"\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a\u009c")
        buf.write(u"\u009e\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa\u00ac\u00ae")
        buf.write(u"\u00b0\u00b2\u00b4\u00b6\u00b8\u00ba\u00bc\u00be\u00c0")
        buf.write(u"\u00c2\u00c4\u00c6\u00c8\u00ca\u00cc\u00ce\u00d0\u00d2")
        buf.write(u"\u00d4\u00d6\u00d8\u00da\u00dc\u00de\u00e0\u00e2\u00e4")
        buf.write(u"\u00e6\u00e8\u00ea\u00ec\u00ee\u00f0\u00f2\u00f4\u00f6")
        buf.write(u"\u00f8\u00fa\u00fc\u00fe\u0100\u0102\u0104\u0106\u0108")
        buf.write(u"\u010a\u010c\u010e\u0110\u0112\u0114\u0116\u0118\u011a")
        buf.write(u"\u011c\u011e\u0120\u0122\u0124\u0126\u0128\u012a\u012c")
        buf.write(u"\u012e\u0130\u0132\u0134\u0136\u0138\u013a\u013c\u013e")
        buf.write(u"\u0140\u0142\u0144\u0146\u0148\u014a\u014c\u014e\u0150")
        buf.write(u"\u0152\u0154\u0156\u0158\u015a\u015c\u015e\u0160\u0162")
        buf.write(u"\u0164\u0166\u0168\u016a\u016c\u016e\u0170\u0172\u0174")
        buf.write(u"\u0176\u0178\u017a\u017c\u017e\u0180\u0182\u0184\u0186")
        buf.write(u"\u0188\u018a\u018c\u018e\u0190\u0192\u0194\u0196\u0198")
        buf.write(u"\u019a\u019c\u019e\2\13\3\2\36\37\4\2\u008e\u008e\u00a2")
        buf.write(u"\u00a2\4\2\u008a\u008a\u0092\u0092\4\2HHYY\4\2##tt\f")
        buf.write(u"\2\609??wwzz\u0084\u0084\u008a\u008a\u0091\u0091\u009b")
        buf.write(u"\u009b\u00a0\u00a2\u00a4\u00a4\n\2\609??wwzz\u0084\u0084")
        buf.write(u"\u0091\u0092\u009b\u009b\u00a0\u00a2\13\2\609??wwzz\u0084")
        buf.write(u"\u0084\u008a\u008a\u0091\u0091\u009b\u009b\u00a0\u00a4")
        buf.write(u"\13\2\609??wwzz\u0084\u0084\u008a\u008a\u0091\u0091\u009b")
        buf.write(u"\u009b\u00a0\u00a2\2\u0969\2\u01a0\3\2\2\2\4\u01b1\3")
        buf.write(u"\2\2\2\6\u01ba\3\2\2\2\b\u01c0\3\2\2\2\n\u01c6\3\2\2")
        buf.write(u"\2\f\u01dc\3\2\2\2\16\u01ec\3\2\2\2\20\u01f6\3\2\2\2")
        buf.write(u"\22\u0207\3\2\2\2\24\u020a\3\2\2\2\26\u0217\3\2\2\2\30")
        buf.write(u"\u0220\3\2\2\2\32\u022a\3\2\2\2\34\u0233\3\2\2\2\36\u023d")
        buf.write(u"\3\2\2\2 \u024e\3\2\2\2\"\u0260\3\2\2\2$\u0266\3\2\2")
        buf.write(u"\2&\u0273\3\2\2\2(\u0281\3\2\2\2*\u0291\3\2\2\2,\u02a1")
        buf.write(u"\3\2\2\2.\u02b3\3\2\2\2\60\u02b6\3\2\2\2\62\u02c9\3\2")
        buf.write(u"\2\2\64\u02e0\3\2\2\2\66\u02e2\3\2\2\28\u02fe\3\2\2\2")
        buf.write(u":\u0300\3\2\2\2<\u0306\3\2\2\2>\u030c\3\2\2\2@\u0328")
        buf.write(u"\3\2\2\2B\u032a\3\2\2\2D\u0337\3\2\2\2F\u0343\3\2\2\2")
        buf.write(u"H\u0349\3\2\2\2J\u0355\3\2\2\2L\u036a\3\2\2\2N\u036e")
        buf.write(u"\3\2\2\2P\u03a2\3\2\2\2R\u03a4\3\2\2\2T\u03a7\3\2\2\2")
        buf.write(u"V\u03ad\3\2\2\2X\u03b9\3\2\2\2Z\u03bb\3\2\2\2\\\u03cb")
        buf.write(u"\3\2\2\2^\u03e4\3\2\2\2`\u045d\3\2\2\2b\u0461\3\2\2\2")
        buf.write(u"d\u0463\3\2\2\2f\u0476\3\2\2\2h\u0478\3\2\2\2j\u047d")
        buf.write(u"\3\2\2\2l\u0484\3\2\2\2n\u048c\3\2\2\2p\u04cc\3\2\2\2")
        buf.write(u"r\u04ce\3\2\2\2t\u04e7\3\2\2\2v\u04e9\3\2\2\2x\u04f5")
        buf.write(u"\3\2\2\2z\u04ff\3\2\2\2|\u0503\3\2\2\2~\u050e\3\2\2\2")
        buf.write(u"\u0080\u0510\3\2\2\2\u0082\u0515\3\2\2\2\u0084\u0518")
        buf.write(u"\3\2\2\2\u0086\u051d\3\2\2\2\u0088\u052b\3\2\2\2\u008a")
        buf.write(u"\u0535\3\2\2\2\u008c\u0539\3\2\2\2\u008e\u053b\3\2\2")
        buf.write(u"\2\u0090\u0544\3\2\2\2\u0092\u054d\3\2\2\2\u0094\u055f")
        buf.write(u"\3\2\2\2\u0096\u0562\3\2\2\2\u0098\u056b\3\2\2\2\u009a")
        buf.write(u"\u0573\3\2\2\2\u009c\u057b\3\2\2\2\u009e\u058d\3\2\2")
        buf.write(u"\2\u00a0\u059e\3\2\2\2\u00a2\u05af\3\2\2\2\u00a4\u05b1")
        buf.write(u"\3\2\2\2\u00a6\u05b4\3\2\2\2\u00a8\u05b8\3\2\2\2\u00aa")
        buf.write(u"\u05bd\3\2\2\2\u00ac\u05bf\3\2\2\2\u00ae\u05c9\3\2\2")
        buf.write(u"\2\u00b0\u05ce\3\2\2\2\u00b2\u05d0\3\2\2\2\u00b4\u05d2")
        buf.write(u"\3\2\2\2\u00b6\u05d4\3\2\2\2\u00b8\u05d6\3\2\2\2\u00ba")
        buf.write(u"\u05d8\3\2\2\2\u00bc\u05e5\3\2\2\2\u00be\u05e9\3\2\2")
        buf.write(u"\2\u00c0\u05eb\3\2\2\2\u00c2\u05f0\3\2\2\2\u00c4\u05f5")
        buf.write(u"\3\2\2\2\u00c6\u05f7\3\2\2\2\u00c8\u0605\3\2\2\2\u00ca")
        buf.write(u"\u0613\3\2\2\2\u00cc\u0615\3\2\2\2\u00ce\u0621\3\2\2")
        buf.write(u"\2\u00d0\u062d\3\2\2\2\u00d2\u062f\3\2\2\2\u00d4\u0633")
        buf.write(u"\3\2\2\2\u00d6\u063e\3\2\2\2\u00d8\u0642\3\2\2\2\u00da")
        buf.write(u"\u0654\3\2\2\2\u00dc\u065c\3\2\2\2\u00de\u0668\3\2\2")
        buf.write(u"\2\u00e0\u066a\3\2\2\2\u00e2\u066c\3\2\2\2\u00e4\u067f")
        buf.write(u"\3\2\2\2\u00e6\u0681\3\2\2\2\u00e8\u0688\3\2\2\2\u00ea")
        buf.write(u"\u068f\3\2\2\2\u00ec\u0698\3\2\2\2\u00ee\u06a1\3\2\2")
        buf.write(u"\2\u00f0\u06aa\3\2\2\2\u00f2\u06c1\3\2\2\2\u00f4\u06d2")
        buf.write(u"\3\2\2\2\u00f6\u06d4\3\2\2\2\u00f8\u06e0\3\2\2\2\u00fa")
        buf.write(u"\u06e2\3\2\2\2\u00fc\u06e4\3\2\2\2\u00fe\u06ea\3\2\2")
        buf.write(u"\2\u0100\u06f1\3\2\2\2\u0102\u06f4\3\2\2\2\u0104\u06fd")
        buf.write(u"\3\2\2\2\u0106\u0705\3\2\2\2\u0108\u0711\3\2\2\2\u010a")
        buf.write(u"\u0719\3\2\2\2\u010c\u0726\3\2\2\2\u010e\u0728\3\2\2")
        buf.write(u"\2\u0110\u072c\3\2\2\2\u0112\u073a\3\2\2\2\u0114\u073c")
        buf.write(u"\3\2\2\2\u0116\u0741\3\2\2\2\u0118\u0746\3\2\2\2\u011a")
        buf.write(u"\u074e\3\2\2\2\u011c\u075f\3\2\2\2\u011e\u0761\3\2\2")
        buf.write(u"\2\u0120\u0764\3\2\2\2\u0122\u0767\3\2\2\2\u0124\u076a")
        buf.write(u"\3\2\2\2\u0126\u076d\3\2\2\2\u0128\u0770\3\2\2\2\u012a")
        buf.write(u"\u0772\3\2\2\2\u012c\u0774\3\2\2\2\u012e\u0776\3\2\2")
        buf.write(u"\2\u0130\u0778\3\2\2\2\u0132\u077a\3\2\2\2\u0134\u077c")
        buf.write(u"\3\2\2\2\u0136\u0785\3\2\2\2\u0138\u0787\3\2\2\2\u013a")
        buf.write(u"\u0798\3\2\2\2\u013c\u079a\3\2\2\2\u013e\u079c\3\2\2")
        buf.write(u"\2\u0140\u07a4\3\2\2\2\u0142\u07a6\3\2\2\2\u0144\u07ad")
        buf.write(u"\3\2\2\2\u0146\u07b8\3\2\2\2\u0148\u07bc\3\2\2\2\u014a")
        buf.write(u"\u07c0\3\2\2\2\u014c\u07c7\3\2\2\2\u014e\u07c9\3\2\2")
        buf.write(u"\2\u0150\u07ce\3\2\2\2\u0152\u07d0\3\2\2\2\u0154\u07df")
        buf.write(u"\3\2\2\2\u0156\u07e1\3\2\2\2\u0158\u07e9\3\2\2\2\u015a")
        buf.write(u"\u07eb\3\2\2\2\u015c\u07f8\3\2\2\2\u015e\u07fa\3\2\2")
        buf.write(u"\2\u0160\u0805\3\2\2\2\u0162\u0815\3\2\2\2\u0164\u081c")
        buf.write(u"\3\2\2\2\u0166\u082b\3\2\2\2\u0168\u082d\3\2\2\2\u016a")
        buf.write(u"\u0836\3\2\2\2\u016c\u0838\3\2\2\2\u016e\u0847\3\2\2")
        buf.write(u"\2\u0170\u0849\3\2\2\2\u0172\u084b\3\2\2\2\u0174\u0851")
        buf.write(u"\3\2\2\2\u0176\u0853\3\2\2\2\u0178\u085a\3\2\2\2\u017a")
        buf.write(u"\u0865\3\2\2\2\u017c\u0869\3\2\2\2\u017e\u086d\3\2\2")
        buf.write(u"\2\u0180\u0878\3\2\2\2\u0182\u0887\3\2\2\2\u0184\u0889")
        buf.write(u"\3\2\2\2\u0186\u0892\3\2\2\2\u0188\u0894\3\2\2\2\u018a")
        buf.write(u"\u08a3\3\2\2\2\u018c\u08a5\3\2\2\2\u018e\u08a7\3\2\2")
        buf.write(u"\2\u0190\u08ad\3\2\2\2\u0192\u08af\3\2\2\2\u0194\u08b6")
        buf.write(u"\3\2\2\2\u0196\u08c1\3\2\2\2\u0198\u08c5\3\2\2\2\u019a")
        buf.write(u"\u08cc\3\2\2\2\u019c\u08db\3\2\2\2\u019e\u08dd\3\2\2")
        buf.write(u"\2\u01a0\u01a1\7_\2\2\u01a1\u01a2\7Q\2\2\u01a2\u01a7")
        buf.write(u"\5\u00b6\\\2\u01a3\u01a4\7\22\2\2\u01a4\u01a5\5\u00dc")
        buf.write(u"o\2\u01a5\u01a6\7\23\2\2\u01a6\u01a8\3\2\2\2\u01a7\u01a3")
        buf.write(u"\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9")
        buf.write(u"\u01aa\7c\2\2\u01aa\u01ac\5\u00b6\\\2\u01ab\u01a9\3\2")
        buf.write(u"\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ae")
        buf.write(u"\7\26\2\2\u01ae\u01af\5\u0090I\2\u01af\u01b0\7\27\2\2")
        buf.write(u"\u01b0\3\3\2\2\2\u01b1\u01b2\7_\2\2\u01b2\u01b3\5\u00b6")
        buf.write(u"\\\2\u01b3\u01b4\7\22\2\2\u01b4\u01b5\5\u00a2R\2\u01b5")
        buf.write(u"\u01b6\7\23\2\2\u01b6\u01b7\7\26\2\2\u01b7\u01b8\5\u008e")
        buf.write(u"H\2\u01b8\u01b9\7\27\2\2\u01b9\5\3\2\2\2\u01ba\u01bb")
        buf.write(u"\5\u00b8]\2\u01bb\u01bc\7\22\2\2\u01bc\u01bd\5x=\2\u01bd")
        buf.write(u"\u01be\7\23\2\2\u01be\u01bf\7\16\2\2\u01bf\7\3\2\2\2")
        buf.write(u"\u01c0\u01c1\5\u00b8]\2\u01c1\u01c2\7)\2\2\u01c2\u01c3")
        buf.write(u"\5^\60\2\u01c3\u01c4\7\16\2\2\u01c4\t\3\2\2\2\u01c5\u01c7")
        buf.write(u"\7\u008e\2\2\u01c6\u01c5\3\2\2\2\u01c6\u01c7\3\2\2\2")
        buf.write(u"\u01c7\u01c8\3\2\2\2\u01c8\u01c9\7J\2\2\u01c9\u01ca\5")
        buf.write(u"\u00b4[\2\u01ca\u01cb\7\r\2\2\u01cb\u01cd\5\u009eP\2")
        buf.write(u"\u01cc\u01ce\5\u0094K\2\u01cd\u01cc\3\2\2\2\u01cd\u01ce")
        buf.write(u"\3\2\2\2\u01ce\u01d7\3\2\2\2\u01cf\u01d0\7\u0097\2\2")
        buf.write(u"\u01d0\u01d5\7n\2\2\u01d1\u01d2\7\22\2\2\u01d2\u01d3")
        buf.write(u"\5\u00dan\2\u01d3\u01d4\7\23\2\2\u01d4\u01d6\3\2\2\2")
        buf.write(u"\u01d5\u01d1\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d8")
        buf.write(u"\3\2\2\2\u01d7\u01cf\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8")
        buf.write(u"\u01d9\3\2\2\2\u01d9\u01da\7\16\2\2\u01da\13\3\2\2\2")
        buf.write(u"\u01db\u01dd\7\u008e\2\2\u01dc\u01db\3\2\2\2\u01dc\u01dd")
        buf.write(u"\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01df\7Q\2\2\u01df")
        buf.write(u"\u01e4\5\u00b6\\\2\u01e0\u01e1\7\22\2\2\u01e1\u01e2\5")
        buf.write(u"\u00dco\2\u01e2\u01e3\7\23\2\2\u01e3\u01e5\3\2\2\2\u01e4")
        buf.write(u"\u01e0\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e8\3\2\2")
        buf.write(u"\2\u01e6\u01e7\7c\2\2\u01e7\u01e9\5\20\t\2\u01e8\u01e6")
        buf.write(u"\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea")
        buf.write(u"\u01eb\5\22\n\2\u01eb\r\3\2\2\2\u01ec\u01ed\7\u008c\2")
        buf.write(u"\2\u01ed\u01f2\5\u00b6\\\2\u01ee\u01ef\7\22\2\2\u01ef")
        buf.write(u"\u01f0\5\u00dco\2\u01f0\u01f1\7\23\2\2\u01f1\u01f3\3")
        buf.write(u"\2\2\2\u01f2\u01ee\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3")
        buf.write(u"\u01f4\3\2\2\2\u01f4\u01f5\5\22\n\2\u01f5\17\3\2\2\2")
        buf.write(u"\u01f6\u01f7\b\t\1\2\u01f7\u01f8\5\u00b6\\\2\u01f8\u01fe")
        buf.write(u"\3\2\2\2\u01f9\u01fa\f\3\2\2\u01fa\u01fb\7\17\2\2\u01fb")
        buf.write(u"\u01fd\5\u00b6\\\2\u01fc\u01f9\3\2\2\2\u01fd\u0200\3")
        buf.write(u"\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff")
        buf.write(u"\21\3\2\2\2\u0200\u01fe\3\2\2\2\u0201\u0208\7\16\2\2")
        buf.write(u"\u0202\u0204\7\26\2\2\u0203\u0205\5\u00c8e\2\u0204\u0203")
        buf.write(u"\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0206\3\2\2\2\u0206")
        buf.write(u"\u0208\7\27\2\2\u0207\u0201\3\2\2\2\u0207\u0202\3\2\2")
        buf.write(u"\2\u0208\23\3\2\2\2\u0209\u020b\5\u009eP\2\u020a\u0209")
        buf.write(u"\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u020c\3\2\2\2\u020c")
        buf.write(u"\u020d\7~\2\2\u020d\u020e\5\u011c\u008f\2\u020e\u020f")
        buf.write(u"\7\22\2\2\u020f\u0210\5\u00be`\2\u0210\u0211\7\23\2\2")
        buf.write(u"\u0211\u0213\7\26\2\2\u0212\u0214\5\u00eav\2\u0213\u0212")
        buf.write(u"\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u0215\3\2\2\2\u0215")
        buf.write(u"\u0216\7\27\2\2\u0216\25\3\2\2\2\u0217\u0218\7\u008b")
        buf.write(u"\2\2\u0218\u0219\5\u00b2Z\2\u0219\u021b\7\26\2\2\u021a")
        buf.write(u"\u021c\5\u00eav\2\u021b\u021a\3\2\2\2\u021b\u021c\3\2")
        buf.write(u"\2\2\u021c\u021d\3\2\2\2\u021d\u021e\7\27\2\2\u021e\27")
        buf.write(u"\3\2\2\2\u021f\u0221\7v\2\2\u0220\u021f\3\2\2\2\u0220")
        buf.write(u"\u0221\3\2\2\2\u0221\u0222\3\2\2\2\u0222\u0223\7\u008b")
        buf.write(u"\2\2\u0223\u0224\5\u00b2Z\2\u0224\u0226\7\26\2\2\u0225")
        buf.write(u"\u0227\5\u00e2r\2\u0226\u0225\3\2\2\2\u0226\u0227\3\2")
        buf.write(u"\2\2\u0227\u0228\3\2\2\2\u0228\u0229\7\27\2\2\u0229\31")
        buf.write(u"\3\2\2\2\u022a\u022b\7j\2\2\u022b\u022c\5\u00b2Z\2\u022c")
        buf.write(u"\u022e\7\26\2\2\u022d\u022f\5\u00eav\2\u022e\u022d\3")
        buf.write(u"\2\2\2\u022e\u022f\3\2\2\2\u022f\u0230\3\2\2\2\u0230")
        buf.write(u"\u0231\7\27\2\2\u0231\33\3\2\2\2\u0232\u0234\7v\2\2\u0233")
        buf.write(u"\u0232\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0235\3\2\2")
        buf.write(u"\2\u0235\u0236\7j\2\2\u0236\u0237\5\u00b2Z\2\u0237\u0239")
        buf.write(u"\7\26\2\2\u0238\u023a\5\u00e2r\2\u0239\u0238\3\2\2\2")
        buf.write(u"\u0239\u023a\3\2\2\2\u023a\u023b\3\2\2\2\u023b\u023c")
        buf.write(u"\7\27\2\2\u023c\35\3\2\2\2\u023d\u023e\7v\2\2\u023e\u023f")
        buf.write(u"\7\u0086\2\2\u023f\u0244\5\u00b6\\\2\u0240\u0241\7\22")
        buf.write(u"\2\2\u0241\u0242\5\u00dco\2\u0242\u0243\7\23\2\2\u0243")
        buf.write(u"\u0245\3\2\2\2\u0244\u0240\3\2\2\2\u0244\u0245\3\2\2")
        buf.write(u"\2\u0245\u0246\3\2\2\2\u0246\u0247\7\26\2\2\u0247\u0249")
        buf.write(u"\5\"\22\2\u0248\u024a\5\u00ccg\2\u0249\u0248\3\2\2\2")
        buf.write(u"\u0249\u024a\3\2\2\2\u024a\u024b\3\2\2\2\u024b\u024c")
        buf.write(u"\7\27\2\2\u024c\37\3\2\2\2\u024d\u024f\7\u008e\2\2\u024e")
        buf.write(u"\u024d\3\2\2\2\u024e\u024f\3\2\2\2\u024f\u0250\3\2\2")
        buf.write(u"\2\u0250\u0251\7v\2\2\u0251\u0252\7Q\2\2\u0252\u0257")
        buf.write(u"\5\u00b6\\\2\u0253\u0254\7\22\2\2\u0254\u0255\5\u00dc")
        buf.write(u"o\2\u0255\u0256\7\23\2\2\u0256\u0258\3\2\2\2\u0257\u0253")
        buf.write(u"\3\2\2\2\u0257\u0258\3\2\2\2\u0258\u0259\3\2\2\2\u0259")
        buf.write(u"\u025a\7\26\2\2\u025a\u025c\5\"\22\2\u025b\u025d\5\u00cc")
        buf.write(u"g\2\u025c\u025b\3\2\2\2\u025c\u025d\3\2\2\2\u025d\u025e")
        buf.write(u"\3\2\2\2\u025e\u025f\7\27\2\2\u025f!\3\2\2\2\u0260\u0261")
        buf.write(u"\7Q\2\2\u0261\u0262\7L\2\2\u0262\u0263\7\26\2\2\u0263")
        buf.write(u"\u0264\5$\23\2\u0264\u0265\7\27\2\2\u0265#\3\2\2\2\u0266")
        buf.write(u"\u0267\b\23\1\2\u0267\u0268\5\u00d0i\2\u0268\u0269\7")
        buf.write(u"\16\2\2\u0269\u0270\3\2\2\2\u026a\u026b\f\3\2\2\u026b")
        buf.write(u"\u026c\5\u00d0i\2\u026c\u026d\7\16\2\2\u026d\u026f\3")
        buf.write(u"\2\2\2\u026e\u026a\3\2\2\2\u026f\u0272\3\2\2\2\u0270")
        buf.write(u"\u026e\3\2\2\2\u0270\u0271\3\2\2\2\u0271%\3\2\2\2\u0272")
        buf.write(u"\u0270\3\2\2\2\u0273\u0275\7B\2\2\u0274\u0276\5\u009e")
        buf.write(u"P\2\u0275\u0274\3\2\2\2\u0275\u0276\3\2\2\2\u0276\u0277")
        buf.write(u"\3\2\2\2\u0277\u0278\7r\2\2\u0278\u0279\5\u00aeX\2\u0279")
        buf.write(u"\u027b\7\22\2\2\u027a\u027c\5\u00ba^\2\u027b\u027a\3")
        buf.write(u"\2\2\2\u027b\u027c\3\2\2\2\u027c\u027d\3\2\2\2\u027d")
        buf.write(u"\u027e\7\23\2\2\u027e\u027f\7\16\2\2\u027f\'\3\2\2\2")
        buf.write(u"\u0280\u0282\5\u009eP\2\u0281\u0280\3\2\2\2\u0281\u0282")
        buf.write(u"\3\2\2\2\u0282\u0283\3\2\2\2\u0283\u0284\7r\2\2\u0284")
        buf.write(u"\u0285\5\u00aeX\2\u0285\u0287\7\22\2\2\u0286\u0288\5")
        buf.write(u"\u00ba^\2\u0287\u0286\3\2\2\2\u0287\u0288\3\2\2\2\u0288")
        buf.write(u"\u0289\3\2\2\2\u0289\u028a\7\23\2\2\u028a\u028c\7\26")
        buf.write(u"\2\2\u028b\u028d\5\u00eav\2\u028c\u028b\3\2\2\2\u028c")
        buf.write(u"\u028d\3\2\2\2\u028d\u028e\3\2\2\2\u028e\u028f\7\27\2")
        buf.write(u"\2\u028f)\3\2\2\2\u0290\u0292\5\u00c4c\2\u0291\u0290")
        buf.write(u"\3\2\2\2\u0291\u0292\3\2\2\2\u0292\u0294\3\2\2\2\u0293")
        buf.write(u"\u0295\7v\2\2\u0294\u0293\3\2\2\2\u0294\u0295\3\2\2\2")
        buf.write(u"\u0295\u0296\3\2\2\2\u0296\u0297\7r\2\2\u0297\u0298\5")
        buf.write(u"\u00aeX\2\u0298\u029a\7\22\2\2\u0299\u029b\5\u00ba^\2")
        buf.write(u"\u029a\u0299\3\2\2\2\u029a\u029b\3\2\2\2\u029b\u029c")
        buf.write(u"\3\2\2\2\u029c\u029d\7\23\2\2\u029d\u029e\7\26\2\2\u029e")
        buf.write(u"\u029f\5\u00e2r\2\u029f\u02a0\7\27\2\2\u02a0+\3\2\2\2")
        buf.write(u"\u02a1\u02a2\7\u0091\2\2\u02a2\u02a3\7r\2\2\u02a3\u02a4")
        buf.write(u"\7\u00a5\2\2\u02a4\u02a5\7\22\2\2\u02a5\u02a6\7\23\2")
        buf.write(u"\2\u02a6\u02a7\7\26\2\2\u02a7\u02a8\5\u00eav\2\u02a8")
        buf.write(u"\u02a9\7\27\2\2\u02a9\u02b1\7\u0096\2\2\u02aa\u02ab\7")
        buf.write(u"\26\2\2\u02ab\u02ac\5\u00ecw\2\u02ac\u02ad\7\27\2\2\u02ad")
        buf.write(u"\u02b2\3\2\2\2\u02ae\u02af\5\u00b8]\2\u02af\u02b0\7\16")
        buf.write(u"\2\2\u02b0\u02b2\3\2\2\2\u02b1\u02aa\3\2\2\2\u02b1\u02ae")
        buf.write(u"\3\2\2\2\u02b2-\3\2\2\2\u02b3\u02b4\5^\60\2\u02b4\u02b5")
        buf.write(u"\7\16\2\2\u02b5/\3\2\2\2\u02b6\u02bb\5\u00c4c\2\u02b7")
        buf.write(u"\u02b8\7\22\2\2\u02b8\u02b9\5\u00dco\2\u02b9\u02ba\7")
        buf.write(u"\23\2\2\u02ba\u02bc\3\2\2\2\u02bb\u02b7\3\2\2\2\u02bb")
        buf.write(u"\u02bc\3\2\2\2\u02bc\u02bd\3\2\2\2\u02bd\u02c0\5\u00b2")
        buf.write(u"Z\2\u02be\u02bf\7)\2\2\u02bf\u02c1\5\u00fe\u0080\2\u02c0")
        buf.write(u"\u02be\3\2\2\2\u02c0\u02c1\3\2\2\2\u02c1\61\3\2\2\2\u02c2")
        buf.write(u"\u02ca\5\64\33\2\u02c3\u02c7\7\26\2\2\u02c4\u02c5\5\u00ea")
        buf.write(u"v\2\u02c5\u02c6\7\27\2\2\u02c6\u02c8\3\2\2\2\u02c7\u02c4")
        buf.write(u"\3\2\2\2\u02c7\u02c8\3\2\2\2\u02c8\u02ca\3\2\2\2\u02c9")
        buf.write(u"\u02c2\3\2\2\2\u02c9\u02c3\3\2\2\2\u02ca\63\3\2\2\2\u02cb")
        buf.write(u"\u02cc\5V,\2\u02cc\u02cd\7\16\2\2\u02cd\u02e1\3\2\2\2")
        buf.write(u"\u02ce\u02e1\5|?\2\u02cf\u02e1\5\u0080A\2\u02d0\u02e1")
        buf.write(u"\58\35\2\u02d1\u02e1\5\66\34\2\u02d2\u02e1\5R*\2\u02d3")
        buf.write(u"\u02e1\5T+\2\u02d4\u02e1\5H%\2\u02d5\u02e1\5> \2\u02d6")
        buf.write(u"\u02e1\5B\"\2\u02d7\u02e1\5F$\2\u02d8\u02e1\5D#\2\u02d9")
        buf.write(u"\u02e1\5N(\2\u02da\u02e1\5L\'\2\u02db\u02e1\5l\67\2\u02dc")
        buf.write(u"\u02e1\5:\36\2\u02dd\u02e1\5<\37\2\u02de\u02e1\5(\25")
        buf.write(u"\2\u02df\u02e1\5\u00e0q\2\u02e0\u02cb\3\2\2\2\u02e0\u02ce")
        buf.write(u"\3\2\2\2\u02e0\u02cf\3\2\2\2\u02e0\u02d0\3\2\2\2\u02e0")
        buf.write(u"\u02d1\3\2\2\2\u02e0\u02d2\3\2\2\2\u02e0\u02d3\3\2\2")
        buf.write(u"\2\u02e0\u02d4\3\2\2\2\u02e0\u02d5\3\2\2\2\u02e0\u02d6")
        buf.write(u"\3\2\2\2\u02e0\u02d7\3\2\2\2\u02e0\u02d8\3\2\2\2\u02e0")
        buf.write(u"\u02d9\3\2\2\2\u02e0\u02da\3\2\2\2\u02e0\u02db\3\2\2")
        buf.write(u"\2\u02e0\u02dc\3\2\2\2\u02e0\u02dd\3\2\2\2\u02e0\u02de")
        buf.write(u"\3\2\2\2\u02e0\u02df\3\2\2\2\u02e1\65\3\2\2\2\u02e2\u02e3")
        buf.write(u"\7g\2\2\u02e3\u02e4\7\22\2\2\u02e4\u02e5\7\23\2\2\u02e5")
        buf.write(u"\u02e6\7\16\2\2\u02e6\67\3\2\2\2\u02e7\u02e8\7X\2\2\u02e8")
        buf.write(u"\u02e9\7\22\2\2\u02e9\u02ea\5\u009aN\2\u02ea\u02eb\7")
        buf.write(u"\23\2\2\u02eb\u02ec\7\16\2\2\u02ec\u02ff\3\2\2\2\u02ed")
        buf.write(u"\u02ee\7\u008f\2\2\u02ee\u02ef\7\22\2\2\u02ef\u02f0\5")
        buf.write(u"\u009aN\2\u02f0\u02f1\7\23\2\2\u02f1\u02f2\7\16\2\2\u02f2")
        buf.write(u"\u02ff\3\2\2\2\u02f3\u02f4\7X\2\2\u02f4\u02f5\7\22\2")
        buf.write(u"\2\u02f5\u02f6\5\u009aN\2\u02f6\u02f7\7\23\2\2\u02f7")
        buf.write(u"\u02f8\7E\2\2\u02f8\u02f9\7\u008f\2\2\u02f9\u02fa\7\22")
        buf.write(u"\2\2\u02fa\u02fb\5\u009aN\2\u02fb\u02fc\7\23\2\2\u02fc")
        buf.write(u"\u02fd\7\16\2\2\u02fd\u02ff\3\2\2\2\u02fe\u02e7\3\2\2")
        buf.write(u"\2\u02fe\u02ed\3\2\2\2\u02fe\u02f3\3\2\2\2\u02ff9\3\2")
        buf.write(u"\2\2\u0300\u0301\7\u0097\2\2\u0301\u0302\7\22\2\2\u0302")
        buf.write(u"\u0303\5\u010e\u0088\2\u0303\u0304\7\23\2\2\u0304\u0305")
        buf.write(u"\5\62\32\2\u0305;\3\2\2\2\u0306\u0307\7\u0097\2\2\u0307")
        buf.write(u"\u0308\7\22\2\2\u0308\u0309\5\u00b6\\\2\u0309\u030a\7")
        buf.write(u"\23\2\2\u030a\u030b\5\62\32\2\u030b=\3\2\2\2\u030c\u030d")
        buf.write(u"\7\u0090\2\2\u030d\u030e\7\22\2\2\u030e\u030f\5^\60\2")
        buf.write(u"\u030f\u0310\7\23\2\2\u0310\u0311\7\26\2\2\u0311\u0317")
        buf.write(u"\5\u00eex\2\u0312\u0313\7V\2\2\u0313\u0315\7\r\2\2\u0314")
        buf.write(u"\u0316\5\u00eav\2\u0315\u0314\3\2\2\2\u0315\u0316\3\2")
        buf.write(u"\2\2\u0316\u0318\3\2\2\2\u0317\u0312\3\2\2\2\u0317\u0318")
        buf.write(u"\3\2\2\2\u0318\u0319\3\2\2\2\u0319\u031a\7\27\2\2\u031a")
        buf.write(u"?\3\2\2\2\u031b\u031c\7O\2\2\u031c\u031d\5\u00f4{\2\u031d")
        buf.write(u"\u031f\7\r\2\2\u031e\u0320\5\u00eav\2\u031f\u031e\3\2")
        buf.write(u"\2\2\u031f\u0320\3\2\2\2\u0320\u0329\3\2\2\2\u0321\u0322")
        buf.write(u"\7O\2\2\u0322\u0323\7m\2\2\u0323\u0324\5\u00f2z\2\u0324")
        buf.write(u"\u0326\7\r\2\2\u0325\u0327\5\u00eav\2\u0326\u0325\3\2")
        buf.write(u"\2\2\u0326\u0327\3\2\2\2\u0327\u0329\3\2\2\2\u0328\u031b")
        buf.write(u"\3\2\2\2\u0328\u0321\3\2\2\2\u0329A\3\2\2\2\u032a\u032b")
        buf.write(u"\7h\2\2\u032b\u032c\7\\\2\2\u032c\u032d\7\22\2\2\u032d")
        buf.write(u"\u0330\5\u00b2Z\2\u032e\u032f\7\17\2\2\u032f\u0331\5")
        buf.write(u"\u00b2Z\2\u0330\u032e\3\2\2\2\u0330\u0331\3\2\2\2\u0331")
        buf.write(u"\u0332\3\2\2\2\u0332\u0333\7m\2\2\u0333\u0334\5^\60\2")
        buf.write(u"\u0334\u0335\7\23\2\2\u0335\u0336\5\62\32\2\u0336C\3")
        buf.write(u"\2\2\2\u0337\u0338\7Z\2\2\u0338\u033a\7\26\2\2\u0339")
        buf.write(u"\u033b\5\u00eav\2\u033a\u0339\3\2\2\2\u033a\u033b\3\2")
        buf.write(u"\2\2\u033b\u033c\3\2\2\2\u033c\u033d\7\27\2\2\u033d\u033e")
        buf.write(u"\7\u009a\2\2\u033e\u033f\7\22\2\2\u033f\u0340\5^\60\2")
        buf.write(u"\u0340\u0341\7\23\2\2\u0341\u0342\7\16\2\2\u0342E\3\2")
        buf.write(u"\2\2\u0343\u0344\7\u009a\2\2\u0344\u0345\7\22\2\2\u0345")
        buf.write(u"\u0346\5^\60\2\u0346\u0347\7\23\2\2\u0347\u0348\5\62")
        buf.write(u"\32\2\u0348G\3\2\2\2\u0349\u034a\7l\2\2\u034a\u034b\7")
        buf.write(u"\22\2\2\u034b\u034c\5^\60\2\u034c\u034d\7\23\2\2\u034d")
        buf.write(u"\u034f\5\62\32\2\u034e\u0350\5J&\2\u034f\u034e\3\2\2")
        buf.write(u"\2\u034f\u0350\3\2\2\2\u0350\u0353\3\2\2\2\u0351\u0352")
        buf.write(u"\7]\2\2\u0352\u0354\5\62\32\2\u0353\u0351\3\2\2\2\u0353")
        buf.write(u"\u0354\3\2\2\2\u0354I\3\2\2\2\u0355\u0356\b&\1\2\u0356")
        buf.write(u"\u0357\7]\2\2\u0357\u0358\7l\2\2\u0358\u0359\7\22\2\2")
        buf.write(u"\u0359\u035a\5^\60\2\u035a\u035b\7\23\2\2\u035b\u035c")
        buf.write(u"\5\62\32\2\u035c\u0367\3\2\2\2\u035d\u035e\f\3\2\2\u035e")
        buf.write(u"\u035f\7]\2\2\u035f\u0360\7l\2\2\u0360\u0361\7\22\2\2")
        buf.write(u"\u0361\u0362\5^\60\2\u0362\u0363\7\23\2\2\u0363\u0364")
        buf.write(u"\5\62\32\2\u0364\u0366\3\2\2\2\u0365\u035d\3\2\2\2\u0366")
        buf.write(u"\u0369\3\2\2\2\u0367\u0365\3\2\2\2\u0367\u0368\3\2\2")
        buf.write(u"\2\u0368K\3\2\2\2\u0369\u0367\3\2\2\2\u036a\u036b\7\u0093")
        buf.write(u"\2\2\u036b\u036c\5^\60\2\u036c\u036d\7\16\2\2\u036dM")
        buf.write(u"\3\2\2\2\u036e\u036f\7\u0095\2\2\u036f\u0370\7\22\2\2")
        buf.write(u"\u0370\u0371\5\u00b2Z\2\u0371\u0372\7\23\2\2\u0372\u0374")
        buf.write(u"\7\26\2\2\u0373\u0375\5\u00eav\2\u0374\u0373\3\2\2\2")
        buf.write(u"\u0374\u0375\3\2\2\2\u0375\u0376\3\2\2\2\u0376\u0378")
        buf.write(u"\7\27\2\2\u0377\u0379\5\u00f0y\2\u0378\u0377\3\2\2\2")
        buf.write(u"\u0378\u0379\3\2\2\2\u0379\u0383\3\2\2\2\u037a\u037b")
        buf.write(u"\7P\2\2\u037b\u037c\7\22\2\2\u037c\u037d\7F\2\2\u037d")
        buf.write(u"\u037e\7\23\2\2\u037e\u0380\7\26\2\2\u037f\u0381\5\u00ea")
        buf.write(u"v\2\u0380\u037f\3\2\2\2\u0380\u0381\3\2\2\2\u0381\u0382")
        buf.write(u"\3\2\2\2\u0382\u0384\7\27\2\2\u0383\u037a\3\2\2\2\u0383")
        buf.write(u"\u0384\3\2\2\2\u0384\u038b\3\2\2\2\u0385\u0386\7f\2\2")
        buf.write(u"\u0386\u0388\7\26\2\2\u0387\u0389\5\u00eav\2\u0388\u0387")
        buf.write(u"\3\2\2\2\u0388\u0389\3\2\2\2\u0389\u038a\3\2\2\2\u038a")
        buf.write(u"\u038c\7\27\2\2\u038b\u0385\3\2\2\2\u038b\u038c\3\2\2")
        buf.write(u"\2\u038cO\3\2\2\2\u038d\u038e\7P\2\2\u038e\u038f\7\22")
        buf.write(u"\2\2\u038f\u0390\5\u00b8]\2\u0390\u0391\7\23\2\2\u0391")
        buf.write(u"\u0393\7\26\2\2\u0392\u0394\5\u00eav\2\u0393\u0392\3")
        buf.write(u"\2\2\2\u0393\u0394\3\2\2\2\u0394\u0395\3\2\2\2\u0395")
        buf.write(u"\u0396\7\27\2\2\u0396\u03a3\3\2\2\2\u0397\u0398\7P\2")
        buf.write(u"\2\u0398\u0399\7m\2\2\u0399\u039a\7\22\2\2\u039a\u039b")
        buf.write(u"\5\u0092J\2\u039b\u039c\7\23\2\2\u039c\u039e\7\26\2\2")
        buf.write(u"\u039d\u039f\5\u00eav\2\u039e\u039d\3\2\2\2\u039e\u039f")
        buf.write(u"\3\2\2\2\u039f\u03a0\3\2\2\2\u03a0\u03a1\7\27\2\2\u03a1")
        buf.write(u"\u03a3\3\2\2\2\u03a2\u038d\3\2\2\2\u03a2\u0397\3\2\2")
        buf.write(u"\2\u03a3Q\3\2\2\2\u03a4\u03a5\7M\2\2\u03a5\u03a6\7\16")
        buf.write(u"\2\2\u03a6S\3\2\2\2\u03a7\u03a9\7\u0087\2\2\u03a8\u03aa")
        buf.write(u"\5^\60\2\u03a9\u03a8\3\2\2\2\u03a9\u03aa\3\2\2\2\u03aa")
        buf.write(u"\u03ab\3\2\2\2\u03ab\u03ac\7\16\2\2\u03acU\3\2\2\2\u03ad")
        buf.write(u"\u03ae\5X-\2\u03ae\u03b0\7\22\2\2\u03af\u03b1\5x=\2\u03b0")
        buf.write(u"\u03af\3\2\2\2\u03b0\u03b1\3\2\2\2\u03b1\u03b2\3\2\2")
        buf.write(u"\2\u03b2\u03b3\7\23\2\2\u03b3W\3\2\2\2\u03b4\u03ba\5")
        buf.write(u"\u00aeX\2\u03b5\u03b6\5Z.\2\u03b6\u03b7\7\21\2\2\u03b7")
        buf.write(u"\u03b8\5\u00aeX\2\u03b8\u03ba\3\2\2\2\u03b9\u03b4\3\2")
        buf.write(u"\2\2\u03b9\u03b5\3\2\2\2\u03baY\3\2\2\2\u03bb\u03bc\b")
        buf.write(u".\1\2\u03bc\u03bd\5\u00b0Y\2\u03bd\u03c2\3\2\2\2\u03be")
        buf.write(u"\u03bf\f\3\2\2\u03bf\u03c1\5\\/\2\u03c0\u03be\3\2\2\2")
        buf.write(u"\u03c1\u03c4\3\2\2\2\u03c2\u03c0\3\2\2\2\u03c2\u03c3")
        buf.write(u"\3\2\2\2\u03c3[\3\2\2\2\u03c4\u03c2\3\2\2\2\u03c5\u03c6")
        buf.write(u"\7\21\2\2\u03c6\u03cc\5\u00b2Z\2\u03c7\u03c8\7\24\2\2")
        buf.write(u"\u03c8\u03c9\5^\60\2\u03c9\u03ca\7\25\2\2\u03ca\u03cc")
        buf.write(u"\3\2\2\2\u03cb\u03c5\3\2\2\2\u03cb\u03c7\3\2\2\2\u03cc")
        buf.write(u"]\3\2\2\2\u03cd\u03ce\b\60\1\2\u03ce\u03e5\5d\63\2\u03cf")
        buf.write(u"\u03e5\5f\64\2\u03d0\u03d1\7\37\2\2\u03d1\u03e5\5^\60")
        buf.write(u"&\u03d2\u03d3\7\31\2\2\u03d3\u03e5\5^\60%\u03d4\u03d5")
        buf.write(u"\7\22\2\2\u03d5\u03d6\5\u00c4c\2\u03d6\u03d7\7\23\2\2")
        buf.write(u"\u03d7\u03d8\5^\60\37\u03d8\u03e5\3\2\2\2\u03d9\u03da")
        buf.write(u"\7;\2\2\u03da\u03db\7\22\2\2\u03db\u03dc\5^\60\2\u03dc")
        buf.write(u"\u03dd\7\23\2\2\u03dd\u03e5\3\2\2\2\u03de\u03df\7a\2")
        buf.write(u"\2\u03df\u03e0\7\22\2\2\u03e0\u03e1\5\u00b2Z\2\u03e1")
        buf.write(u"\u03e2\7\23\2\2\u03e2\u03e5\3\2\2\2\u03e3\u03e5\5b\62")
        buf.write(u"\2\u03e4\u03cd\3\2\2\2\u03e4\u03cf\3\2\2\2\u03e4\u03d0")
        buf.write(u"\3\2\2\2\u03e4\u03d2\3\2\2\2\u03e4\u03d4\3\2\2\2\u03e4")
        buf.write(u"\u03d9\3\2\2\2\u03e4\u03de\3\2\2\2\u03e4\u03e3\3\2\2")
        buf.write(u"\2\u03e5\u045a\3\2\2\2\u03e6\u03e7\f$\2\2\u03e7\u03e8")
        buf.write(u"\5\u012a\u0096\2\u03e8\u03e9\5^\60%\u03e9\u0459\3\2\2")
        buf.write(u"\2\u03ea\u03eb\f#\2\2\u03eb\u03ec\5\u012c\u0097\2\u03ec")
        buf.write(u"\u03ed\5^\60$\u03ed\u0459\3\2\2\2\u03ee\u03ef\f\"\2\2")
        buf.write(u"\u03ef\u03f0\5\u0130\u0099\2\u03f0\u03f1\5^\60#\u03f1")
        buf.write(u"\u0459\3\2\2\2\u03f2\u03f3\f!\2\2\u03f3\u03f4\5\u012e")
        buf.write(u"\u0098\2\u03f4\u03f5\5^\60\"\u03f5\u0459\3\2\2\2\u03f6")
        buf.write(u"\u03f7\f \2\2\u03f7\u03f8\t\2\2\2\u03f8\u0459\5^\60!")
        buf.write(u"\u03f9\u03fa\f\36\2\2\u03fa\u03fb\7&\2\2\u03fb\u0459")
        buf.write(u"\5^\60\37\u03fc\u03fd\f\35\2\2\u03fd\u03fe\7\'\2\2\u03fe")
        buf.write(u"\u0459\5^\60\36\u03ff\u0400\f\34\2\2\u0400\u0401\7$\2")
        buf.write(u"\2\u0401\u0459\5^\60\35\u0402\u0403\f\33\2\2\u0403\u0404")
        buf.write(u"\7%\2\2\u0404\u0459\5^\60\34\u0405\u0406\f\30\2\2\u0406")
        buf.write(u"\u0407\7p\2\2\u0407\u0408\7x\2\2\u0408\u0459\5^\60\31")
        buf.write(u"\u0409\u040a\f\27\2\2\u040a\u040b\7p\2\2\u040b\u0459")
        buf.write(u"\5^\60\30\u040c\u040d\f\26\2\2\u040d\u040e\7+\2\2\u040e")
        buf.write(u"\u0459\5^\60\27\u040f\u0410\f\25\2\2\u0410\u0411\7*\2")
        buf.write(u"\2\u0411\u0459\5^\60\26\u0412\u0413\f\24\2\2\u0413\u0414")
        buf.write(u"\7,\2\2\u0414\u0459\5^\60\25\u0415\u0416\f\23\2\2\u0416")
        buf.write(u"\u0417\7T\2\2\u0417\u0459\5^\60\24\u0418\u0419\f\22\2")
        buf.write(u"\2\u0419\u041a\7m\2\2\u041a\u0459\5^\60\23\u041b\u041c")
        buf.write(u"\f\21\2\2\u041c\u041d\7k\2\2\u041d\u0459\5^\60\22\u041e")
        buf.write(u"\u041f\f\20\2\2\u041f\u0420\7k\2\2\u0420\u0421\7C\2\2")
        buf.write(u"\u0421\u0459\5^\60\21\u0422\u0423\f\17\2\2\u0423\u0424")
        buf.write(u"\7k\2\2\u0424\u0425\7F\2\2\u0425\u0459\5^\60\20\u0426")
        buf.write(u"\u0427\f\16\2\2\u0427\u0428\7x\2\2\u0428\u0429\7T\2\2")
        buf.write(u"\u0429\u0459\5^\60\17\u042a\u042b\f\r\2\2\u042b\u042c")
        buf.write(u"\7x\2\2\u042c\u042d\7m\2\2\u042d\u0459\5^\60\16\u042e")
        buf.write(u"\u042f\f\f\2\2\u042f\u0430\7x\2\2\u0430\u0431\7k\2\2")
        buf.write(u"\u0431\u0459\5^\60\r\u0432\u0433\f\13\2\2\u0433\u0434")
        buf.write(u"\7x\2\2\u0434\u0435\7k\2\2\u0435\u0436\7C\2\2\u0436\u0459")
        buf.write(u"\5^\60\f\u0437\u0438\f\n\2\2\u0438\u0439\7x\2\2\u0439")
        buf.write(u"\u043a\7k\2\2\u043a\u043b\7F\2\2\u043b\u0459\5^\60\13")
        buf.write(u"\u043c\u043d\f\t\2\2\u043d\u043e\7\35\2\2\u043e\u0459")
        buf.write(u"\5^\60\n\u043f\u0440\f\b\2\2\u0440\u0441\7\33\2\2\u0441")
        buf.write(u"\u0459\5^\60\t\u0442\u0443\f\7\2\2\u0443\u0444\7\30\2")
        buf.write(u"\2\u0444\u0445\5^\60\2\u0445\u0446\7\r\2\2\u0446\u0447")
        buf.write(u"\5^\60\b\u0447\u0459\3\2\2\2\u0448\u0449\f\32\2\2\u0449")
        buf.write(u"\u044a\7p\2\2\u044a\u044b\7x\2\2\u044b\u0459\5`\61\2")
        buf.write(u"\u044c\u044d\f\31\2\2\u044d\u044e\7p\2\2\u044e\u0459")
        buf.write(u"\5`\61\2\u044f\u0450\f\3\2\2\u0450\u0451\7h\2\2\u0451")
        buf.write(u"\u0452\7\\\2\2\u0452\u0453\7\22\2\2\u0453\u0454\5\u00b2")
        buf.write(u"Z\2\u0454\u0455\7m\2\2\u0455\u0456\5^\60\2\u0456\u0457")
        buf.write(u"\7\23\2\2\u0457\u0459\3\2\2\2\u0458\u03e6\3\2\2\2\u0458")
        buf.write(u"\u03ea\3\2\2\2\u0458\u03ee\3\2\2\2\u0458\u03f2\3\2\2")
        buf.write(u"\2\u0458\u03f6\3\2\2\2\u0458\u03f9\3\2\2\2\u0458\u03fc")
        buf.write(u"\3\2\2\2\u0458\u03ff\3\2\2\2\u0458\u0402\3\2\2\2\u0458")
        buf.write(u"\u0405\3\2\2\2\u0458\u0409\3\2\2\2\u0458\u040c\3\2\2")
        buf.write(u"\2\u0458\u040f\3\2\2\2\u0458\u0412\3\2\2\2\u0458\u0415")
        buf.write(u"\3\2\2\2\u0458\u0418\3\2\2\2\u0458\u041b\3\2\2\2\u0458")
        buf.write(u"\u041e\3\2\2\2\u0458\u0422\3\2\2\2\u0458\u0426\3\2\2")
        buf.write(u"\2\u0458\u042a\3\2\2\2\u0458\u042e\3\2\2\2\u0458\u0432")
        buf.write(u"\3\2\2\2\u0458\u0437\3\2\2\2\u0458\u043c\3\2\2\2\u0458")
        buf.write(u"\u043f\3\2\2\2\u0458\u0442\3\2\2\2\u0458\u0448\3\2\2")
        buf.write(u"\2\u0458\u044c\3\2\2\2\u0458\u044f\3\2\2\2\u0459\u045c")
        buf.write(u"\3\2\2\2\u045a\u0458\3\2\2\2\u045a\u045b\3\2\2\2\u045b")
        buf.write(u"_\3\2\2\2\u045c\u045a\3\2\2\2\u045d\u045e\6\61$\3\u045e")
        buf.write(u"\u045f\7\u00a2\2\2\u045f\u0460\5\u00c4c\2\u0460a\3\2")
        buf.write(u"\2\2\u0461\u0462\5\u00b6\\\2\u0462c\3\2\2\2\u0463\u0464")
        buf.write(u"\b\63\1\2\u0464\u0465\5\u00f8}\2\u0465\u046a\3\2\2\2")
        buf.write(u"\u0466\u0467\f\3\2\2\u0467\u0469\5t;\2\u0468\u0466\3")
        buf.write(u"\2\2\2\u0469\u046c\3\2\2\2\u046a\u0468\3\2\2\2\u046a")
        buf.write(u"\u046b\3\2\2\2\u046be\3\2\2\2\u046c\u046a\3\2\2\2\u046d")
        buf.write(u"\u0477\5h\65\2\u046e\u0477\5j\66\2\u046f\u0477\5n8\2")
        buf.write(u"\u0470\u0477\5p9\2\u0471\u0477\5\u0114\u008b\2\u0472")
        buf.write(u"\u0477\5\u0116\u008c\2\u0473\u0477\5r:\2\u0474\u0477")
        buf.write(u"\5V,\2\u0475\u0477\5v<\2\u0476\u046d\3\2\2\2\u0476\u046e")
        buf.write(u"\3\2\2\2\u0476\u046f\3\2\2\2\u0476\u0470\3\2\2\2\u0476")
        buf.write(u"\u0471\3\2\2\2\u0476\u0472\3\2\2\2\u0476\u0473\3\2\2")
        buf.write(u"\2\u0476\u0474\3\2\2\2\u0476\u0475\3\2\2\2\u0477g\3\2")
        buf.write(u"\2\2\u0478\u0479\7=\2\2\u0479\u047a\7\22\2\2\u047a\u047b")
        buf.write(u"\5^\60\2\u047b\u047c\7\23\2\2\u047ci\3\2\2\2\u047d\u047e")
        buf.write(u"\7<\2\2\u047e\u0480\7\22\2\2\u047f\u0481\5^\60\2\u0480")
        buf.write(u"\u047f\3\2\2\2\u0480\u0481\3\2\2\2\u0481\u0482\3\2\2")
        buf.write(u"\2\u0482\u0483\7\23\2\2\u0483k\3\2\2\2\u0484\u0485\7")
        buf.write(u"\u009b\2\2\u0485\u0486\7\22\2\2\u0486\u0487\5^\60\2\u0487")
        buf.write(u"\u0488\7\23\2\2\u0488\u0489\7\u0094\2\2\u0489\u048a\5")
        buf.write(u"^\60\2\u048a\u048b\7\16\2\2\u048bm\3\2\2\2\u048c\u048d")
        buf.write(u"\7e\2\2\u048d\u048e\7\22\2\2\u048e\u048f\5^\60\2\u048f")
        buf.write(u"\u0490\7\23\2\2\u0490\u0491\7\u0097\2\2\u0491\u0492\7")
        buf.write(u"\22\2\2\u0492\u0493\5\u00b2Z\2\u0493\u0494\7\23\2\2\u0494")
        buf.write(u"\u0495\7\u0099\2\2\u0495\u0496\7\22\2\2\u0496\u0497\5")
        buf.write(u"^\60\2\u0497\u0498\7\23\2\2\u0498o\3\2\2\2\u0499\u049a")
        buf.write(u"\7d\2\2\u049a\u049f\7|\2\2\u049b\u049c\7\22\2\2\u049c")
        buf.write(u"\u049d\5\u00a6T\2\u049d\u049e\7\23\2\2\u049e\u04a0\3")
        buf.write(u"\2\2\2\u049f\u049b\3\2\2\2\u049f\u04a0\3\2\2\2\u04a0")
        buf.write(u"\u04a1\3\2\2\2\u04a1\u04a2\7\u0099\2\2\u04a2\u04a3\7")
        buf.write(u"\22\2\2\u04a3\u04a4\5^\60\2\u04a4\u04a5\7\23\2\2\u04a5")
        buf.write(u"\u04cd\3\2\2\2\u04a6\u04bb\7d\2\2\u04a7\u04ac\7C\2\2")
        buf.write(u"\u04a8\u04a9\7\22\2\2\u04a9\u04aa\5\u00a6T\2\u04aa\u04ab")
        buf.write(u"\7\23\2\2\u04ab\u04ad\3\2\2\2\u04ac\u04a8\3\2\2\2\u04ac")
        buf.write(u"\u04ad\3\2\2\2\u04ad\u04bc\3\2\2\2\u04ae\u04af\7\22\2")
        buf.write(u"\2\u04af\u04b0\5\u00a6T\2\u04b0\u04b1\7\23\2\2\u04b1")
        buf.write(u"\u04b3\3\2\2\2\u04b2\u04ae\3\2\2\2\u04b2\u04b3\3\2\2")
        buf.write(u"\2\u04b3\u04b4\3\2\2\2\u04b4\u04b5\7\u0089\2\2\u04b5")
        buf.write(u"\u04b6\7\22\2\2\u04b6\u04b7\5^\60\2\u04b7\u04b8\7\u0094")
        buf.write(u"\2\2\u04b8\u04b9\5^\60\2\u04b9\u04ba\7\23\2\2\u04ba\u04bc")
        buf.write(u"\3\2\2\2\u04bb\u04a7\3\2\2\2\u04bb\u04b2\3\2\2\2\u04bc")
        buf.write(u"\u04c2\3\2\2\2\u04bd\u04be\7\u0099\2\2\u04be\u04bf\7")
        buf.write(u"\22\2\2\u04bf\u04c0\5^\60\2\u04c0\u04c1\7\23\2\2\u04c1")
        buf.write(u"\u04c3\3\2\2\2\u04c2\u04bd\3\2\2\2\u04c2\u04c3\3\2\2")
        buf.write(u"\2\u04c3\u04ca\3\2\2\2\u04c4\u04c5\7\u0080\2\2\u04c5")
        buf.write(u"\u04c6\7N\2\2\u04c6\u04c7\7\22\2\2\u04c7\u04c8\5\u0118")
        buf.write(u"\u008d\2\u04c8\u04c9\7\23\2\2\u04c9\u04cb\3\2\2\2\u04ca")
        buf.write(u"\u04c4\3\2\2\2\u04ca\u04cb\3\2\2\2\u04cb\u04cd\3\2\2")
        buf.write(u"\2\u04cc\u0499\3\2\2\2\u04cc\u04a6\3\2\2\2\u04cdq\3\2")
        buf.write(u"\2\2\u04ce\u04d0\7\u008d\2\2\u04cf\u04d1\7Y\2\2\u04d0")
        buf.write(u"\u04cf\3\2\2\2\u04d0\u04d1\3\2\2\2\u04d1\u04d2\3\2\2")
        buf.write(u"\2\u04d2\u04d3\7\22\2\2\u04d3\u04d9\5d\63\2\u04d4\u04d5")
        buf.write(u"\7\17\2\2\u04d5\u04d6\5\u0120\u0091\2\u04d6\u04d7\7)")
        buf.write(u"\2\2\u04d7\u04d8\5d\63\2\u04d8\u04da\3\2\2\2\u04d9\u04d4")
        buf.write(u"\3\2\2\2\u04d9\u04da\3\2\2\2\u04da\u04db\3\2\2\2\u04db")
        buf.write(u"\u04dc\7\23\2\2\u04dcs\3\2\2\2\u04dd\u04de\7\21\2\2\u04de")
        buf.write(u"\u04e8\5\u00b2Z\2\u04df\u04e0\7\24\2\2\u04e0\u04e1\5")
        buf.write(u"^\60\2\u04e1\u04e2\7\25\2\2\u04e2\u04e8\3\2\2\2\u04e3")
        buf.write(u"\u04e4\7\24\2\2\u04e4\u04e5\5\u010c\u0087\2\u04e5\u04e6")
        buf.write(u"\7\25\2\2\u04e6\u04e8\3\2\2\2\u04e7\u04dd\3\2\2\2\u04e7")
        buf.write(u"\u04df\3\2\2\2\u04e7\u04e3\3\2\2\2\u04e8u\3\2\2\2\u04e9")
        buf.write(u"\u04ea\5\u00a6T\2\u04ea\u04ec\7\22\2\2\u04eb\u04ed\5")
        buf.write(u"x=\2\u04ec\u04eb\3\2\2\2\u04ec\u04ed\3\2\2\2\u04ed\u04ee")
        buf.write(u"\3\2\2\2\u04ee\u04ef\7\23\2\2\u04efw\3\2\2\2\u04f0\u04f1")
        buf.write(u"\b=\1\2\u04f1\u04f2\5^\60\2\u04f2\u04f3\6=&\3\u04f3\u04f6")
        buf.write(u"\3\2\2\2\u04f4\u04f6\5z>\2\u04f5\u04f0\3\2\2\2\u04f5")
        buf.write(u"\u04f4\3\2\2\2\u04f6\u04fc\3\2\2\2\u04f7\u04f8\f\3\2")
        buf.write(u"\2\u04f8\u04f9\7\17\2\2\u04f9\u04fb\5z>\2\u04fa\u04f7")
        buf.write(u"\3\2\2\2\u04fb\u04fe\3\2\2\2\u04fc\u04fa\3\2\2\2\u04fc")
        buf.write(u"\u04fd\3\2\2\2\u04fdy\3\2\2\2\u04fe\u04fc\3\2\2\2\u04ff")
        buf.write(u"\u0500\5\u00b2Z\2\u0500\u0501\5\u0128\u0095\2\u0501\u0502")
        buf.write(u"\5^\60\2\u0502{\3\2\2\2\u0503\u0504\5\u0110\u0089\2\u0504")
        buf.write(u"\u0505\5\u0128\u0095\2\u0505\u0506\5^\60\2\u0506\u0507")
        buf.write(u"\7\16\2\2\u0507}\3\2\2\2\u0508\u0509\7\21\2\2\u0509\u050f")
        buf.write(u"\5\u00b2Z\2\u050a\u050b\7\24\2\2\u050b\u050c\5^\60\2")
        buf.write(u"\u050c\u050d\7\25\2\2\u050d\u050f\3\2\2\2\u050e\u0508")
        buf.write(u"\3\2\2\2\u050e\u050a\3\2\2\2\u050f\177\3\2\2\2\u0510")
        buf.write(u"\u0511\5\u00dan\2\u0511\u0512\5\u0128\u0095\2\u0512\u0513")
        buf.write(u"\5^\60\2\u0513\u0514\7\16\2\2\u0514\u0081\3\2\2\2\u0515")
        buf.write(u"\u0516\7z\2\2\u0516\u0083\3\2\2\2\u0517\u0519\5\u0086")
        buf.write(u"D\2\u0518\u0517\3\2\2\2\u0518\u0519\3\2\2\2\u0519\u051a")
        buf.write(u"\3\2\2\2\u051a\u051b\5\u0132\u009a\2\u051b\u051c\7\2")
        buf.write(u"\2\3\u051c\u0085\3\2\2\2\u051d\u0523\5\u0088E\2\u051e")
        buf.write(u"\u051f\5\u0134\u009b\2\u051f\u0520\5\u0088E\2\u0520\u0522")
        buf.write(u"\3\2\2\2\u0521\u051e\3\2\2\2\u0522\u0525\3\2\2\2\u0523")
        buf.write(u"\u0521\3\2\2\2\u0523\u0524\3\2\2\2\u0524\u0087\3\2\2")
        buf.write(u"\2\u0525\u0523\3\2\2\2\u0526\u0527\5\u00e0q\2\u0527\u0528")
        buf.write(u"\5\u0134\u009b\2\u0528\u052a\3\2\2\2\u0529\u0526\3\2")
        buf.write(u"\2\2\u052a\u052d\3\2\2\2\u052b\u0529\3\2\2\2\u052b\u052c")
        buf.write(u"\3\2\2\2\u052c\u0533\3\2\2\2\u052d\u052b\3\2\2\2\u052e")
        buf.write(u"\u0534\5\n\6\2\u052f\u0534\5\u00aaV\2\u0530\u0534\5\u008a")
        buf.write(u"F\2\u0531\u0534\5\u008cG\2\u0532\u0534\5\u00dep\2\u0533")
        buf.write(u"\u052e\3\2\2\2\u0533\u052f\3\2\2\2\u0533\u0530\3\2\2")
        buf.write(u"\2\u0533\u0531\3\2\2\2\u0533\u0532\3\2\2\2\u0534\u0089")
        buf.write(u"\3\2\2\2\u0535\u0536\5\36\20\2\u0536\u008b\3\2\2\2\u0537")
        buf.write(u"\u053a\5\2\2\2\u0538\u053a\5\4\3\2\u0539\u0537\3\2\2")
        buf.write(u"\2\u0539\u0538\3\2\2\2\u053a\u008d\3\2\2\2\u053b\u0541")
        buf.write(u"\5\b\5\2\u053c\u053d\5\u0134\u009b\2\u053d\u053e\5\b")
        buf.write(u"\5\2\u053e\u0540\3\2\2\2\u053f\u053c\3\2\2\2\u0540\u0543")
        buf.write(u"\3\2\2\2\u0541\u053f\3\2\2\2\u0541\u0542\3\2\2\2\u0542")
        buf.write(u"\u008f\3\2\2\2\u0543\u0541\3\2\2\2\u0544\u054a\5\6\4")
        buf.write(u"\2\u0545\u0546\5\u0134\u009b\2\u0546\u0547\5\6\4\2\u0547")
        buf.write(u"\u0549\3\2\2\2\u0548\u0545\3\2\2\2\u0549\u054c\3\2\2")
        buf.write(u"\2\u054a\u0548\3\2\2\2\u054a\u054b\3\2\2\2\u054b\u0091")
        buf.write(u"\3\2\2\2\u054c\u054a\3\2\2\2\u054d\u0552\5\u00b8]\2\u054e")
        buf.write(u"\u054f\7\17\2\2\u054f\u0551\5\u00b8]\2\u0550\u054e\3")
        buf.write(u"\2\2\2\u0551\u0554\3\2\2\2\u0552\u0550\3\2\2\2\u0552")
        buf.write(u"\u0553\3\2\2\2\u0553\u0093\3\2\2\2\u0554\u0552\3\2\2")
        buf.write(u"\2\u0555\u0556\7m\2\2\u0556\u0560\5\u0096L\2\u0557\u0558")
        buf.write(u"\7m\2\2\u0558\u0560\5\u0098M\2\u0559\u055a\7m\2\2\u055a")
        buf.write(u"\u0560\5\u009cO\2\u055b\u055c\7q\2\2\u055c\u0560\7\u00a5")
        buf.write(u"\2\2\u055d\u055e\7q\2\2\u055e\u0560\5^\60\2\u055f\u0555")
        buf.write(u"\3\2\2\2\u055f\u0557\3\2\2\2\u055f\u0559\3\2\2\2\u055f")
        buf.write(u"\u055b\3\2\2\2\u055f\u055d\3\2\2\2\u0560\u0095\3\2\2")
        buf.write(u"\2\u0561\u0563\7u\2\2\u0562\u0561\3\2\2\2\u0562\u0563")
        buf.write(u"\3\2\2\2\u0563\u0564\3\2\2\2\u0564\u0566\7\24\2\2\u0565")
        buf.write(u"\u0567\5\u009aN\2\u0566\u0565\3\2\2\2\u0566\u0567\3\2")
        buf.write(u"\2\2\u0567\u0568\3\2\2\2\u0568\u0569\7\25\2\2\u0569\u0097")
        buf.write(u"\3\2\2\2\u056a\u056c\7u\2\2\u056b\u056a\3\2\2\2\u056b")
        buf.write(u"\u056c\3\2\2\2\u056c\u056d\3\2\2\2\u056d\u056f\7&\2\2")
        buf.write(u"\u056e\u0570\5\u009aN\2\u056f\u056e\3\2\2\2\u056f\u0570")
        buf.write(u"\3\2\2\2\u0570\u0571\3\2\2\2\u0571\u0572\7$\2\2\u0572")
        buf.write(u"\u0099\3\2\2\2\u0573\u0578\5^\60\2\u0574\u0575\7\17\2")
        buf.write(u"\2\u0575\u0577\5^\60\2\u0576\u0574\3\2\2\2\u0577\u057a")
        buf.write(u"\3\2\2\2\u0578\u0576\3\2\2\2\u0578\u0579\3\2\2\2\u0579")
        buf.write(u"\u009b\3\2\2\2\u057a\u0578\3\2\2\2\u057b\u057c\7\24\2")
        buf.write(u"\2\u057c\u057d\5^\60\2\u057d\u057e\7\20\2\2\u057e\u057f")
        buf.write(u"\5^\60\2\u057f\u0580\7\25\2\2\u0580\u009d\3\2\2\2\u0581")
        buf.write(u"\u0582\bP\1\2\u0582\u058e\5\u00a0Q\2\u0583\u0584\7A\2")
        buf.write(u"\2\u0584\u0585\7&\2\2\u0585\u0586\5\u009eP\2\u0586\u0587")
        buf.write(u"\7$\2\2\u0587\u058e\3\2\2\2\u0588\u0589\7@\2\2\u0589")
        buf.write(u"\u058a\7&\2\2\u058a\u058b\5\u009eP\2\u058b\u058c\7$\2")
        buf.write(u"\2\u058c\u058e\3\2\2\2\u058d\u0581\3\2\2\2\u058d\u0583")
        buf.write(u"\3\2\2\2\u058d\u0588\3\2\2\2\u058e\u0599\3\2\2\2\u058f")
        buf.write(u"\u0590\f\7\2\2\u0590\u0598\7(\2\2\u0591\u0592\f\6\2\2")
        buf.write(u"\u0592\u0593\7\24\2\2\u0593\u0598\7\25\2\2\u0594\u0595")
        buf.write(u"\f\5\2\2\u0595\u0596\7\26\2\2\u0596\u0598\7\27\2\2\u0597")
        buf.write(u"\u058f\3\2\2\2\u0597\u0591\3\2\2\2\u0597\u0594\3\2\2")
        buf.write(u"\2\u0598\u059b\3\2\2\2\u0599\u0597\3\2\2\2\u0599\u059a")
        buf.write(u"\3\2\2\2\u059a\u009f\3\2\2\2\u059b\u0599\3\2\2\2\u059c")
        buf.write(u"\u059f\5\u00a2R\2\u059d\u059f\5\u00a4S\2\u059e\u059c")
        buf.write(u"\3\2\2\2\u059e\u059d\3\2\2\2\u059f\u00a1\3\2\2\2\u05a0")
        buf.write(u"\u05b0\7\60\2\2\u05a1\u05b0\7\61\2\2\u05a2\u05b0\7\62")
        buf.write(u"\2\2\u05a3\u05b0\7>\2\2\u05a4\u05b0\7\63\2\2\u05a5\u05b0")
        buf.write(u"\7\64\2\2\u05a6\u05b0\7<\2\2\u05a7\u05b0\7\65\2\2\u05a8")
        buf.write(u"\u05b0\7\67\2\2\u05a9\u05b0\7\66\2\2\u05aa\u05b0\78\2")
        buf.write(u"\2\u05ab\u05b0\79\2\2\u05ac\u05b0\7;\2\2\u05ad\u05b0")
        buf.write(u"\7=\2\2\u05ae\u05b0\7?\2\2\u05af\u05a0\3\2\2\2\u05af")
        buf.write(u"\u05a1\3\2\2\2\u05af\u05a2\3\2\2\2\u05af\u05a3\3\2\2")
        buf.write(u"\2\u05af\u05a4\3\2\2\2\u05af\u05a5\3\2\2\2\u05af\u05a6")
        buf.write(u"\3\2\2\2\u05af\u05a7\3\2\2\2\u05af\u05a8\3\2\2\2\u05af")
        buf.write(u"\u05a9\3\2\2\2\u05af\u05aa\3\2\2\2\u05af\u05ab\3\2\2")
        buf.write(u"\2\u05af\u05ac\3\2\2\2\u05af\u05ad\3\2\2\2\u05af\u05ae")
        buf.write(u"\3\2\2\2\u05b0\u00a3\3\2\2\2\u05b1\u05b2\7\u00a1\2\2")
        buf.write(u"\u05b2\u00a5\3\2\2\2\u05b3\u05b5\7u\2\2\u05b4\u05b3\3")
        buf.write(u"\2\2\2\u05b4\u05b5\3\2\2\2\u05b5\u05b6\3\2\2\2\u05b6")
        buf.write(u"\u05b7\5\u00a4S\2\u05b7\u00a7\3\2\2\2\u05b8\u05b9\7;")
        buf.write(u"\2\2\u05b9\u00a9\3\2\2\2\u05ba\u05be\5\f\7\2\u05bb\u05be")
        buf.write(u"\5 \21\2\u05bc\u05be\5\16\b\2\u05bd\u05ba\3\2\2\2\u05bd")
        buf.write(u"\u05bb\3\2\2\2\u05bd\u05bc\3\2\2\2\u05be\u00ab\3\2\2")
        buf.write(u"\2\u05bf\u05c4\5\u00b6\\\2\u05c0\u05c1\7\17\2\2\u05c1")
        buf.write(u"\u05c3\5\u00b6\\\2\u05c2\u05c0\3\2\2\2\u05c3\u05c6\3")
        buf.write(u"\2\2\2\u05c4\u05c2\3\2\2\2\u05c4\u05c5\3\2\2\2\u05c5")
        buf.write(u"\u00ad\3\2\2\2\u05c6\u05c4\3\2\2\2\u05c7\u05ca\5\u00b2")
        buf.write(u"Z\2\u05c8\u05ca\5\u00b6\\\2\u05c9\u05c7\3\2\2\2\u05c9")
        buf.write(u"\u05c8\3\2\2\2\u05ca\u00af\3\2\2\2\u05cb\u05cf\5\u00b2")
        buf.write(u"Z\2\u05cc\u05cf\5\u00b6\\\2\u05cd\u05cf\5\u00b8]\2\u05ce")
        buf.write(u"\u05cb\3\2\2\2\u05ce\u05cc\3\2\2\2\u05ce\u05cd\3\2\2")
        buf.write(u"\2\u05cf\u00b1\3\2\2\2\u05d0\u05d1\7\u00a2\2\2\u05d1")
        buf.write(u"\u00b3\3\2\2\2\u05d2\u05d3\t\3\2\2\u05d3\u00b5\3\2\2")
        buf.write(u"\2\u05d4\u05d5\7\u00a1\2\2\u05d5\u00b7\3\2\2\2\u05d6")
        buf.write(u"\u05d7\7\u00a0\2\2\u05d7\u00b9\3\2\2\2\u05d8\u05dd\5")
        buf.write(u"\u00bc_\2\u05d9\u05da\7\17\2\2\u05da\u05dc\5\u00bc_\2")
        buf.write(u"\u05db\u05d9\3\2\2\2\u05dc\u05df\3\2\2\2\u05dd\u05db")
        buf.write(u"\3\2\2\2\u05dd\u05de\3\2\2\2\u05de\u00bb\3\2\2\2\u05df")
        buf.write(u"\u05dd\3\2\2\2\u05e0\u05e6\5\u00c2b\2\u05e1\u05e3\7u")
        buf.write(u"\2\2\u05e2\u05e1\3\2\2\2\u05e2\u05e3\3\2\2\2\u05e3\u05e4")
        buf.write(u"\3\2\2\2\u05e4\u05e6\5\u00be`\2\u05e5\u05e0\3\2\2\2\u05e5")
        buf.write(u"\u05e2\3\2\2\2\u05e6\u00bd\3\2\2\2\u05e7\u05ea\5\u00c0")
        buf.write(u"a\2\u05e8\u05ea\5\60\31\2\u05e9\u05e7\3\2\2\2\u05e9\u05e8")
        buf.write(u"\3\2\2\2\u05ea\u00bf\3\2\2\2\u05eb\u05ee\5\u00b2Z\2\u05ec")
        buf.write(u"\u05ed\7)\2\2\u05ed\u05ef\5\u00fe\u0080\2\u05ee\u05ec")
        buf.write(u"\3\2\2\2\u05ee\u05ef\3\2\2\2\u05ef\u00c1\3\2\2\2\u05f0")
        buf.write(u"\u05f1\5\u00a8U\2\u05f1\u05f2\5\u00b2Z\2\u05f2\u00c3")
        buf.write(u"\3\2\2\2\u05f3\u05f6\5\u009eP\2\u05f4\u05f6\5\u00c6d")
        buf.write(u"\2\u05f5\u05f3\3\2\2\2\u05f5\u05f4\3\2\2\2\u05f6\u00c5")
        buf.write(u"\3\2\2\2\u05f7\u05f8\bd\1\2\u05f8\u05f9\7F\2\2\u05f9")
        buf.write(u"\u0602\3\2\2\2\u05fa\u05fb\f\4\2\2\u05fb\u05fc\7\24\2")
        buf.write(u"\2\u05fc\u0601\7\25\2\2\u05fd\u05fe\f\3\2\2\u05fe\u05ff")
        buf.write(u"\7\26\2\2\u05ff\u0601\7\27\2\2\u0600\u05fa\3\2\2\2\u0600")
        buf.write(u"\u05fd\3\2\2\2\u0601\u0604\3\2\2\2\u0602\u0600\3\2\2")
        buf.write(u"\2\u0602\u0603\3\2\2\2\u0603\u00c7\3\2\2\2\u0604\u0602")
        buf.write(u"\3\2\2\2\u0605\u060b\5\u00caf\2\u0606\u0607\5\u0134\u009b")
        buf.write(u"\2\u0607\u0608\5\u00caf\2\u0608\u060a\3\2\2\2\u0609\u0606")
        buf.write(u"\3\2\2\2\u060a\u060d\3\2\2\2\u060b\u0609\3\2\2\2\u060b")
        buf.write(u"\u060c\3\2\2\2\u060c\u00c9\3\2\2\2\u060d\u060b\3\2\2")
        buf.write(u"\2\u060e\u0614\5\26\f\2\u060f\u0614\5\32\16\2\u0610\u0614")
        buf.write(u"\5(\25\2\u0611\u0614\5&\24\2\u0612\u0614\5\24\13\2\u0613")
        buf.write(u"\u060e\3\2\2\2\u0613\u060f\3\2\2\2\u0613\u0610\3\2\2")
        buf.write(u"\2\u0613\u0611\3\2\2\2\u0613\u0612\3\2\2\2\u0614\u00cb")
        buf.write(u"\3\2\2\2\u0615\u061b\5\u00ceh\2\u0616\u0617\5\u0134\u009b")
        buf.write(u"\2\u0617\u0618\5\u00ceh\2\u0618\u061a\3\2\2\2\u0619\u0616")
        buf.write(u"\3\2\2\2\u061a\u061d\3\2\2\2\u061b\u0619\3\2\2\2\u061b")
        buf.write(u"\u061c\3\2\2\2\u061c\u00cd\3\2\2\2\u061d\u061b\3\2\2")
        buf.write(u"\2\u061e\u0622\5\34\17\2\u061f\u0622\5\30\r\2\u0620\u0622")
        buf.write(u"\5*\26\2\u0621\u061e\3\2\2\2\u0621\u061f\3\2\2\2\u0621")
        buf.write(u"\u0620\3\2\2\2\u0622\u00cf\3\2\2\2\u0623\u0624\7\7\2")
        buf.write(u"\2\u0624\u062e\5\u0180\u00c1\2\u0625\u0626\7\b\2\2\u0626")
        buf.write(u"\u062e\5\u019a\u00ce\2\u0627\u0628\7\t\2\2\u0628\u062e")
        buf.write(u"\5\u00d2j\2\u0629\u062a\7\n\2\2\u062a\u062e\5\u00d2j")
        buf.write(u"\2\u062b\u062c\7\13\2\2\u062c\u062e\5\u00d6l\2\u062d")
        buf.write(u"\u0623\3\2\2\2\u062d\u0625\3\2\2\2\u062d\u0627\3\2\2")
        buf.write(u"\2\u062d\u0629\3\2\2\2\u062d\u062b\3\2\2\2\u062e\u00d1")
        buf.write(u"\3\2\2\2\u062f\u0631\5\u00b0Y\2\u0630\u0632\5\u00d4k")
        buf.write(u"\2\u0631\u0630\3\2\2\2\u0631\u0632\3\2\2\2\u0632\u00d3")
        buf.write(u"\3\2\2\2\u0633\u0634\7i\2\2\u0634\u0635\5\u0122\u0092")
        buf.write(u"\2\u0635\u0636\7\r\2\2\u0636\u063b\5\u00b0Y\2\u0637\u0638")
        buf.write(u"\7\21\2\2\u0638\u063a\5\u00b0Y\2\u0639\u0637\3\2\2\2")
        buf.write(u"\u063a\u063d\3\2\2\2\u063b\u0639\3\2\2\2\u063b\u063c")
        buf.write(u"\3\2\2\2\u063c\u00d5\3\2\2\2\u063d\u063b\3\2\2\2\u063e")
        buf.write(u"\u0640\5\u00b0Y\2\u063f\u0641\5\u00d8m\2\u0640\u063f")
        buf.write(u"\3\2\2\2\u0640\u0641\3\2\2\2\u0641\u00d7\3\2\2\2\u0642")
        buf.write(u"\u0643\7i\2\2\u0643\u0644\5\u0122\u0092\2\u0644\u0646")
        buf.write(u"\7\r\2\2\u0645\u0647\7!\2\2\u0646\u0645\3\2\2\2\u0646")
        buf.write(u"\u0647\3\2\2\2\u0647\u0648\3\2\2\2\u0648\u064d\5\u014e")
        buf.write(u"\u00a8\2\u0649\u064a\7!\2\2\u064a\u064c\5\u014e\u00a8")
        buf.write(u"\2\u064b\u0649\3\2\2\2\u064c\u064f\3\2\2\2\u064d\u064b")
        buf.write(u"\3\2\2\2\u064d\u064e\3\2\2\2\u064e\u0652\3\2\2\2\u064f")
        buf.write(u"\u064d\3\2\2\2\u0650\u0651\7\21\2\2\u0651\u0653\5\u014e")
        buf.write(u"\u00a8\2\u0652\u0650\3\2\2\2\u0652\u0653\3\2\2\2\u0653")
        buf.write(u"\u00d9\3\2\2\2\u0654\u0659\5\u00b2Z\2\u0655\u0656\7\17")
        buf.write(u"\2\2\u0656\u0658\5\u00b2Z\2\u0657\u0655\3\2\2\2\u0658")
        buf.write(u"\u065b\3\2\2\2\u0659\u0657\3\2\2\2\u0659\u065a\3\2\2")
        buf.write(u"\2\u065a\u00db\3\2\2\2\u065b\u0659\3\2\2\2\u065c\u0661")
        buf.write(u"\5\u00b4[\2\u065d\u065e\7\17\2\2\u065e\u0660\5\u00b4")
        buf.write(u"[\2\u065f\u065d\3\2\2\2\u0660\u0663\3\2\2\2\u0661\u065f")
        buf.write(u"\3\2\2\2\u0661\u0662\3\2\2\2\u0662\u00dd\3\2\2\2\u0663")
        buf.write(u"\u0661\3\2\2\2\u0664\u0669\5&\24\2\u0665\u0669\5(\25")
        buf.write(u"\2\u0666\u0669\5*\26\2\u0667\u0669\5,\27\2\u0668\u0664")
        buf.write(u"\3\2\2\2\u0668\u0665\3\2\2\2\u0668\u0666\3\2\2\2\u0668")
        buf.write(u"\u0667\3\2\2\2\u0669\u00df\3\2\2\2\u066a\u066b\7\6\2")
        buf.write(u"\2\u066b\u00e1\3\2\2\2\u066c\u0672\5\u00e4s\2\u066d\u066e")
        buf.write(u"\5\u0134\u009b\2\u066e\u066f\5\u00e4s\2\u066f\u0671\3")
        buf.write(u"\2\2\2\u0670\u066d\3\2\2\2\u0671\u0674\3\2\2\2\u0672")
        buf.write(u"\u0670\3\2\2\2\u0672\u0673\3\2\2\2\u0673\u00e3\3\2\2")
        buf.write(u"\2\u0674\u0672\3\2\2\2\u0675\u0676\7\7\2\2\u0676\u0680")
        buf.write(u"\5\u016a\u00b6\2\u0677\u0678\7\b\2\2\u0678\u0680\5\u0186")
        buf.write(u"\u00c4\2\u0679\u067a\7\t\2\2\u067a\u0680\5\u00e6t\2\u067b")
        buf.write(u"\u067c\7\n\2\2\u067c\u0680\5\u00e6t\2\u067d\u067e\7\13")
        buf.write(u"\2\2\u067e\u0680\5\u00e8u\2\u067f\u0675\3\2\2\2\u067f")
        buf.write(u"\u0677\3\2\2\2\u067f\u0679\3\2\2\2\u067f\u067b\3\2\2")
        buf.write(u"\2\u067f\u067d\3\2\2\2\u0680\u00e5\3\2\2\2\u0681\u0683")
        buf.write(u"\5\u0150\u00a9\2\u0682\u0684\7\16\2\2\u0683\u0682\3\2")
        buf.write(u"\2\2\u0683\u0684\3\2\2\2\u0684\u0686\3\2\2\2\u0685\u0687")
        buf.write(u"\5\u00d4k\2\u0686\u0685\3\2\2\2\u0686\u0687\3\2\2\2\u0687")
        buf.write(u"\u00e7\3\2\2\2\u0688\u068a\5\u0136\u009c\2\u0689\u068b")
        buf.write(u"\7\16\2\2\u068a\u0689\3\2\2\2\u068a\u068b\3\2\2\2\u068b")
        buf.write(u"\u068d\3\2\2\2\u068c\u068e\5\u00d8m\2\u068d\u068c\3\2")
        buf.write(u"\2\2\u068d\u068e\3\2\2\2\u068e\u00e9\3\2\2\2\u068f\u0695")
        buf.write(u"\5\64\33\2\u0690\u0691\5\u0134\u009b\2\u0691\u0692\5")
        buf.write(u"\64\33\2\u0692\u0694\3\2\2\2\u0693\u0690\3\2\2\2\u0694")
        buf.write(u"\u0697\3\2\2\2\u0695\u0693\3\2\2\2\u0695\u0696\3\2\2")
        buf.write(u"\2\u0696\u00eb\3\2\2\2\u0697\u0695\3\2\2\2\u0698\u069e")
        buf.write(u"\5.\30\2\u0699\u069a\5\u0134\u009b\2\u069a\u069b\5.\30")
        buf.write(u"\2\u069b\u069d\3\2\2\2\u069c\u0699\3\2\2\2\u069d\u06a0")
        buf.write(u"\3\2\2\2\u069e\u069c\3\2\2\2\u069e\u069f\3\2\2\2\u069f")
        buf.write(u"\u00ed\3\2\2\2\u06a0\u069e\3\2\2\2\u06a1\u06a7\5@!\2")
        buf.write(u"\u06a2\u06a3\5\u0134\u009b\2\u06a3\u06a4\5@!\2\u06a4")
        buf.write(u"\u06a6\3\2\2\2\u06a5\u06a2\3\2\2\2\u06a6\u06a9\3\2\2")
        buf.write(u"\2\u06a7\u06a5\3\2\2\2\u06a7\u06a8\3\2\2\2\u06a8\u00ef")
        buf.write(u"\3\2\2\2\u06a9\u06a7\3\2\2\2\u06aa\u06b0\5P)\2\u06ab")
        buf.write(u"\u06ac\5\u0134\u009b\2\u06ac\u06ad\5P)\2\u06ad\u06af")
        buf.write(u"\3\2\2\2\u06ae\u06ab\3\2\2\2\u06af\u06b2\3\2\2\2\u06b0")
        buf.write(u"\u06ae\3\2\2\2\u06b0\u06b1\3\2\2\2\u06b1\u00f1\3\2\2")
        buf.write(u"\2\u06b2\u06b0\3\2\2\2\u06b3\u06b4\7\24\2\2\u06b4\u06b5")
        buf.write(u"\5\u00f4{\2\u06b5\u06b6\7\20\2\2\u06b6\u06b7\5\u00f4")
        buf.write(u"{\2\u06b7\u06b8\7\25\2\2\u06b8\u06c2\3\2\2\2\u06b9\u06ba")
        buf.write(u"\7\24\2\2\u06ba\u06bb\5\u00f6|\2\u06bb\u06bc\7\25\2\2")
        buf.write(u"\u06bc\u06c2\3\2\2\2\u06bd\u06be\7&\2\2\u06be\u06bf\5")
        buf.write(u"\u00f6|\2\u06bf\u06c0\7$\2\2\u06c0\u06c2\3\2\2\2\u06c1")
        buf.write(u"\u06b3\3\2\2\2\u06c1\u06b9\3\2\2\2\u06c1\u06bd\3\2\2")
        buf.write(u"\2\u06c2\u00f3\3\2\2\2\u06c3\u06d3\7\u009e\2\2\u06c4")
        buf.write(u"\u06d3\7\u009f\2\2\u06c5\u06d3\7\u00a7\2\2\u06c6\u06d3")
        buf.write(u"\7\u00a8\2\2\u06c7\u06d3\7\u009d\2\2\u06c8\u06d3\7\u00ac")
        buf.write(u"\2\2\u06c9\u06d3\7\u00ab\2\2\u06ca\u06d3\7\u00a5\2\2")
        buf.write(u"\u06cb\u06d3\7\u00a9\2\2\u06cc\u06d3\7\u00aa\2\2\u06cd")
        buf.write(u"\u06d3\7\u009c\2\2\u06ce\u06d3\7\u00ad\2\2\u06cf\u06d3")
        buf.write(u"\7\u00ae\2\2\u06d0\u06d3\7\u00a6\2\2\u06d1\u06d3\5\u0082")
        buf.write(u"B\2\u06d2\u06c3\3\2\2\2\u06d2\u06c4\3\2\2\2\u06d2\u06c5")
        buf.write(u"\3\2\2\2\u06d2\u06c6\3\2\2\2\u06d2\u06c7\3\2\2\2\u06d2")
        buf.write(u"\u06c8\3\2\2\2\u06d2\u06c9\3\2\2\2\u06d2\u06ca\3\2\2")
        buf.write(u"\2\u06d2\u06cb\3\2\2\2\u06d2\u06cc\3\2\2\2\u06d2\u06cd")
        buf.write(u"\3\2\2\2\u06d2\u06ce\3\2\2\2\u06d2\u06cf\3\2\2\2\u06d2")
        buf.write(u"\u06d0\3\2\2\2\u06d2\u06d1\3\2\2\2\u06d3\u00f5\3\2\2")
        buf.write(u"\2\u06d4\u06d9\5\u00f4{\2\u06d5\u06d6\7\17\2\2\u06d6")
        buf.write(u"\u06d8\5\u00f4{\2\u06d7\u06d5\3\2\2\2\u06d8\u06db\3\2")
        buf.write(u"\2\2\u06d9\u06d7\3\2\2\2\u06d9\u06da\3\2\2\2\u06da\u00f7")
        buf.write(u"\3\2\2\2\u06db\u06d9\3\2\2\2\u06dc\u06e1\5\u00fc\177")
        buf.write(u"\2\u06dd\u06e1\5\u00fe\u0080\2\u06de\u06e1\5\u00b0Y\2")
        buf.write(u"\u06df\u06e1\5\u00fa~\2\u06e0\u06dc\3\2\2\2\u06e0\u06dd")
        buf.write(u"\3\2\2\2\u06e0\u06de\3\2\2\2\u06e0\u06df\3\2\2\2\u06e1")
        buf.write(u"\u00f9\3\2\2\2\u06e2\u06e3\t\4\2\2\u06e3\u00fb\3\2\2")
        buf.write(u"\2\u06e4\u06e5\7\22\2\2\u06e5\u06e6\5^\60\2\u06e6\u06e7")
        buf.write(u"\7\23\2\2\u06e7\u00fd\3\2\2\2\u06e8\u06eb\5\u00f4{\2")
        buf.write(u"\u06e9\u06eb\5\u0100\u0081\2\u06ea\u06e8\3\2\2\2\u06ea")
        buf.write(u"\u06e9\3\2\2\2\u06eb\u00ff\3\2\2\2\u06ec\u06f2\5\u009c")
        buf.write(u"O\2\u06ed\u06f2\5\u0096L\2\u06ee\u06f2\5\u0098M\2\u06ef")
        buf.write(u"\u06f2\5\u0104\u0083\2\u06f0\u06f2\5\u0102\u0082\2\u06f1")
        buf.write(u"\u06ec\3\2\2\2\u06f1\u06ed\3\2\2\2\u06f1\u06ee\3\2\2")
        buf.write(u"\2\u06f1\u06ef\3\2\2\2\u06f1\u06f0\3\2\2\2\u06f2\u0101")
        buf.write(u"\3\2\2\2\u06f3\u06f5\7u\2\2\u06f4\u06f3\3\2\2\2\u06f4")
        buf.write(u"\u06f5\3\2\2\2\u06f5\u06f6\3\2\2\2\u06f6\u06f8\7\22\2")
        buf.write(u"\2\u06f7\u06f9\5\u0106\u0084\2\u06f8\u06f7\3\2\2\2\u06f8")
        buf.write(u"\u06f9\3\2\2\2\u06f9\u06fa\3\2\2\2\u06fa\u06fb\7\23\2")
        buf.write(u"\2\u06fb\u0103\3\2\2\2\u06fc\u06fe\7u\2\2\u06fd\u06fc")
        buf.write(u"\3\2\2\2\u06fd\u06fe\3\2\2\2\u06fe\u06ff\3\2\2\2\u06ff")
        buf.write(u"\u0701\7\26\2\2\u0700\u0702\5\u0108\u0085\2\u0701\u0700")
        buf.write(u"\3\2\2\2\u0701\u0702\3\2\2\2\u0702\u0703\3\2\2\2\u0703")
        buf.write(u"\u0704\7\27\2\2\u0704\u0105\3\2\2\2\u0705\u0706\5^\60")
        buf.write(u"\2\u0706\u070f\7\17\2\2\u0707\u070c\5^\60\2\u0708\u0709")
        buf.write(u"\7\17\2\2\u0709\u070b\5^\60\2\u070a\u0708\3\2\2\2\u070b")
        buf.write(u"\u070e\3\2\2\2\u070c\u070a\3\2\2\2\u070c\u070d\3\2\2")
        buf.write(u"\2\u070d\u0710\3\2\2\2\u070e\u070c\3\2\2\2\u070f\u0707")
        buf.write(u"\3\2\2\2\u070f\u0710\3\2\2\2\u0710\u0107\3\2\2\2\u0711")
        buf.write(u"\u0716\5\u010a\u0086\2\u0712\u0713\7\17\2\2\u0713\u0715")
        buf.write(u"\5\u010a\u0086\2\u0714\u0712\3\2\2\2\u0715\u0718\3\2")
        buf.write(u"\2\2\u0716\u0714\3\2\2\2\u0716\u0717\3\2\2\2\u0717\u0109")
        buf.write(u"\3\2\2\2\u0718\u0716\3\2\2\2\u0719\u071a\5^\60\2\u071a")
        buf.write(u"\u071b\7\r\2\2\u071b\u071c\5^\60\2\u071c\u010b\3\2\2")
        buf.write(u"\2\u071d\u071e\5^\60\2\u071e\u071f\7\r\2\2\u071f\u0720")
        buf.write(u"\5^\60\2\u0720\u0727\3\2\2\2\u0721\u0722\5^\60\2\u0722")
        buf.write(u"\u0723\7\r\2\2\u0723\u0727\3\2\2\2\u0724\u0725\7\r\2")
        buf.write(u"\2\u0725\u0727\5^\60\2\u0726\u071d\3\2\2\2\u0726\u0721")
        buf.write(u"\3\2\2\2\u0726\u0724\3\2\2\2\u0727\u010d\3\2\2\2\u0728")
        buf.write(u"\u0729\5\u00b2Z\2\u0729\u072a\5\u0128\u0095\2\u072a\u072b")
        buf.write(u"\5^\60\2\u072b\u010f\3\2\2\2\u072c\u072d\b\u0089\1\2")
        buf.write(u"\u072d\u072e\5\u00b2Z\2\u072e\u0733\3\2\2\2\u072f\u0730")
        buf.write(u"\f\3\2\2\u0730\u0732\5~@\2\u0731\u072f\3\2\2\2\u0732")
        buf.write(u"\u0735\3\2\2\2\u0733\u0731\3\2\2\2\u0733\u0734\3\2\2")
        buf.write(u"\2\u0734\u0111\3\2\2\2\u0735\u0733\3\2\2\2\u0736\u0737")
        buf.write(u"\6\u008a.\3\u0737\u0738\7\u00a2\2\2\u0738\u073b\5\u00c4")
        buf.write(u"c\2\u0739\u073b\5^\60\2\u073a\u0736\3\2\2\2\u073a\u0739")
        buf.write(u"\3\2\2\2\u073b\u0113\3\2\2\2\u073c\u073d\7\u0084\2\2")
        buf.write(u"\u073d\u073e\7C\2\2\u073e\u073f\7i\2\2\u073f\u0740\5")
        buf.write(u"^\60\2\u0740\u0115\3\2\2\2\u0741\u0742\7\u0084\2\2\u0742")
        buf.write(u"\u0743\7|\2\2\u0743\u0744\7i\2\2\u0744\u0745\5^\60\2")
        buf.write(u"\u0745\u0117\3\2\2\2\u0746\u074b\5\u011a\u008e\2\u0747")
        buf.write(u"\u0748\7\17\2\2\u0748\u074a\5\u011a\u008e\2\u0749\u0747")
        buf.write(u"\3\2\2\2\u074a\u074d\3\2\2\2\u074b\u0749\3\2\2\2\u074b")
        buf.write(u"\u074c\3\2\2\2\u074c\u0119\3\2\2\2\u074d\u074b\3\2\2")
        buf.write(u"\2\u074e\u0753\5\u00b2Z\2\u074f\u0750\7\21\2\2\u0750")
        buf.write(u"\u0752\5\u00b2Z\2\u0751\u074f\3\2\2\2\u0752\u0755\3\2")
        buf.write(u"\2\2\u0753\u0751\3\2\2\2\u0753\u0754\3\2\2\2\u0754\u0757")
        buf.write(u"\3\2\2\2\u0755\u0753\3\2\2\2\u0756\u0758\t\5\2\2\u0757")
        buf.write(u"\u0756\3\2\2\2\u0757\u0758\3\2\2\2\u0758\u011b\3\2\2")
        buf.write(u"\2\u0759\u0760\7\36\2\2\u075a\u0760\7\37\2\2\u075b\u0760")
        buf.write(u"\5\u012a\u0096\2\u075c\u0760\5\u012c\u0097\2\u075d\u0760")
        buf.write(u"\5\u012e\u0098\2\u075e\u0760\5\u0130\u0099\2\u075f\u0759")
        buf.write(u"\3\2\2\2\u075f\u075a\3\2\2\2\u075f\u075b\3\2\2\2\u075f")
        buf.write(u"\u075c\3\2\2\2\u075f\u075d\3\2\2\2\u075f\u075e\3\2\2")
        buf.write(u"\2\u0760\u011d\3\2\2\2\u0761\u0762\7\u00a2\2\2\u0762")
        buf.write(u"\u0763\6\u0090/\3\u0763\u011f\3\2\2\2\u0764\u0765\7\u00a2")
        buf.write(u"\2\2\u0765\u0766\6\u0091\60\3\u0766\u0121\3\2\2\2\u0767")
        buf.write(u"\u0768\7\u00a2\2\2\u0768\u0769\6\u0092\61\3\u0769\u0123")
        buf.write(u"\3\2\2\2\u076a\u076b\7\u00a2\2\2\u076b\u076c\6\u0093")
        buf.write(u"\62\3\u076c\u0125\3\2\2\2\u076d\u076e\7\u00a2\2\2\u076e")
        buf.write(u"\u076f\6\u0094\63\3\u076f\u0127\3\2\2\2\u0770\u0771\7")
        buf.write(u")\2\2\u0771\u0129\3\2\2\2\u0772\u0773\7 \2\2\u0773\u012b")
        buf.write(u"\3\2\2\2\u0774\u0775\7!\2\2\u0775\u012d\3\2\2\2\u0776")
        buf.write(u"\u0777\7\"\2\2\u0777\u012f\3\2\2\2\u0778\u0779\t\6\2")
        buf.write(u"\2\u0779\u0131\3\2\2\2\u077a\u077b\3\2\2\2\u077b\u0133")
        buf.write(u"\3\2\2\2\u077c\u077d\3\2\2\2\u077d\u0135\3\2\2\2\u077e")
        buf.write(u"\u077f\7\u0087\2\2\u077f\u0780\5\u0138\u009d\2\u0780")
        buf.write(u"\u0781\7\16\2\2\u0781\u0786\3\2\2\2\u0782\u0783\5\u0138")
        buf.write(u"\u009d\2\u0783\u0784\7\16\2\2\u0784\u0786\3\2\2\2\u0785")
        buf.write(u"\u077e\3\2\2\2\u0785\u0782\3\2\2\2\u0786\u0137\3\2\2")
        buf.write(u"\2\u0787\u0788\b\u009d\1\2\u0788\u0789\5\u013a\u009e")
        buf.write(u"\2\u0789\u078e\3\2\2\2\u078a\u078b\f\3\2\2\u078b\u078d")
        buf.write(u"\5\u0140\u00a1\2\u078c\u078a\3\2\2\2\u078d\u0790\3\2")
        buf.write(u"\2\2\u078e\u078c\3\2\2\2\u078e\u078f\3\2\2\2\u078f\u0139")
        buf.write(u"\3\2\2\2\u0790\u078e\3\2\2\2\u0791\u0799\5\u013c\u009f")
        buf.write(u"\2\u0792\u0799\5\u013e\u00a0\2\u0793\u0799\5\u0148\u00a5")
        buf.write(u"\2\u0794\u0799\5\u014a\u00a6\2\u0795\u0799\5\u014c\u00a7")
        buf.write(u"\2\u0796\u0799\5\u0142\u00a2\2\u0797\u0799\5\u0146\u00a4")
        buf.write(u"\2\u0798\u0791\3\2\2\2\u0798\u0792\3\2\2\2\u0798\u0793")
        buf.write(u"\3\2\2\2\u0798\u0794\3\2\2\2\u0798\u0795\3\2\2\2\u0798")
        buf.write(u"\u0796\3\2\2\2\u0798\u0797\3\2\2\2\u0799\u013b\3\2\2")
        buf.write(u"\2\u079a\u079b\5\u00fa~\2\u079b\u013d\3\2\2\2\u079c\u079d")
        buf.write(u"\5\u011e\u0090\2\u079d\u079e\5\u0142\u00a2\2\u079e\u013f")
        buf.write(u"\3\2\2\2\u079f\u07a0\7\21\2\2\u07a0\u07a5\5\u0142\u00a2")
        buf.write(u"\2\u07a1\u07a2\7\21\2\2\u07a2\u07a5\5\u014e\u00a8\2\u07a3")
        buf.write(u"\u07a5\5\u0146\u00a4\2\u07a4\u079f\3\2\2\2\u07a4\u07a1")
        buf.write(u"\3\2\2\2\u07a4\u07a3\3\2\2\2\u07a5\u0141\3\2\2\2\u07a6")
        buf.write(u"\u07a7\5\u014e\u00a8\2\u07a7\u07a9\7\22\2\2\u07a8\u07aa")
        buf.write(u"\5\u0144\u00a3\2\u07a9\u07a8\3\2\2\2\u07a9\u07aa\3\2")
        buf.write(u"\2\2\u07aa\u07ab\3\2\2\2\u07ab\u07ac\7\23\2\2\u07ac\u0143")
        buf.write(u"\3\2\2\2\u07ad\u07ae\b\u00a3\1\2\u07ae\u07af\5\u0138")
        buf.write(u"\u009d\2\u07af\u07b5\3\2\2\2\u07b0\u07b1\f\3\2\2\u07b1")
        buf.write(u"\u07b2\7\17\2\2\u07b2\u07b4\5\u0138\u009d\2\u07b3\u07b0")
        buf.write(u"\3\2\2\2\u07b4\u07b7\3\2\2\2\u07b5\u07b3\3\2\2\2\u07b5")
        buf.write(u"\u07b6\3\2\2\2\u07b6\u0145\3\2\2\2\u07b7\u07b5\3\2\2")
        buf.write(u"\2\u07b8\u07b9\7\24\2\2\u07b9\u07ba\5\u0138\u009d\2\u07ba")
        buf.write(u"\u07bb\7\25\2\2\u07bb\u0147\3\2\2\2\u07bc\u07bd\7\22")
        buf.write(u"\2\2\u07bd\u07be\5\u0138\u009d\2\u07be\u07bf\7\23\2\2")
        buf.write(u"\u07bf\u0149\3\2\2\2\u07c0\u07c1\5\u014e\u00a8\2\u07c1")
        buf.write(u"\u014b\3\2\2\2\u07c2\u07c8\7\u00a7\2\2\u07c3\u07c8\7")
        buf.write(u"\u00a9\2\2\u07c4\u07c8\7\u00a5\2\2\u07c5\u07c8\7\u009c")
        buf.write(u"\2\2\u07c6\u07c8\7\u009d\2\2\u07c7\u07c2\3\2\2\2\u07c7")
        buf.write(u"\u07c3\3\2\2\2\u07c7\u07c4\3\2\2\2\u07c7\u07c5\3\2\2")
        buf.write(u"\2\u07c7\u07c6\3\2\2\2\u07c8\u014d\3\2\2\2\u07c9\u07ca")
        buf.write(u"\t\7\2\2\u07ca\u014f\3\2\2\2\u07cb\u07cc\7\u0087\2\2")
        buf.write(u"\u07cc\u07cf\5\u0152\u00aa\2\u07cd\u07cf\5\u0152\u00aa")
        buf.write(u"\2\u07ce\u07cb\3\2\2\2\u07ce\u07cd\3\2\2\2\u07cf\u0151")
        buf.write(u"\3\2\2\2\u07d0\u07d1\b\u00aa\1\2\u07d1\u07d2\5\u0154")
        buf.write(u"\u00ab\2\u07d2\u07d7\3\2\2\2\u07d3\u07d4\f\3\2\2\u07d4")
        buf.write(u"\u07d6\5\u0158\u00ad\2\u07d5\u07d3\3\2\2\2\u07d6\u07d9")
        buf.write(u"\3\2\2\2\u07d7\u07d5\3\2\2\2\u07d7\u07d8\3\2\2\2\u07d8")
        buf.write(u"\u0153\3\2\2\2\u07d9\u07d7\3\2\2\2\u07da\u07e0\5\u0156")
        buf.write(u"\u00ac\2\u07db\u07e0\5\u0162\u00b2\2\u07dc\u07e0\5\u0164")
        buf.write(u"\u00b3\2\u07dd\u07e0\5\u0166\u00b4\2\u07de\u07e0\5\u015a")
        buf.write(u"\u00ae\2\u07df\u07da\3\2\2\2\u07df\u07db\3\2\2\2\u07df")
        buf.write(u"\u07dc\3\2\2\2\u07df\u07dd\3\2\2\2\u07df\u07de\3\2\2")
        buf.write(u"\2\u07e0\u0155\3\2\2\2\u07e1\u07e2\5\u00fa~\2\u07e2\u0157")
        buf.write(u"\3\2\2\2\u07e3\u07e4\7\21\2\2\u07e4\u07ea\5\u015a\u00ae")
        buf.write(u"\2\u07e5\u07e6\7\24\2\2\u07e6\u07e7\5\u0152\u00aa\2\u07e7")
        buf.write(u"\u07e8\7\25\2\2\u07e8\u07ea\3\2\2\2\u07e9\u07e3\3\2\2")
        buf.write(u"\2\u07e9\u07e5\3\2\2\2\u07ea\u0159\3\2\2\2\u07eb\u07ec")
        buf.write(u"\5\u0168\u00b5\2\u07ec\u07ee\7\22\2\2\u07ed\u07ef\5\u015c")
        buf.write(u"\u00af\2\u07ee\u07ed\3\2\2\2\u07ee\u07ef\3\2\2\2\u07ef")
        buf.write(u"\u07f0\3\2\2\2\u07f0\u07f1\7\23\2\2\u07f1\u015b\3\2\2")
        buf.write(u"\2\u07f2\u07f9\5\u015e\u00b0\2\u07f3\u07f9\5\u0160\u00b1")
        buf.write(u"\2\u07f4\u07f5\5\u015e\u00b0\2\u07f5\u07f6\7\17\2\2\u07f6")
        buf.write(u"\u07f7\5\u0160\u00b1\2\u07f7\u07f9\3\2\2\2\u07f8\u07f2")
        buf.write(u"\3\2\2\2\u07f8\u07f3\3\2\2\2\u07f8\u07f4\3\2\2\2\u07f9")
        buf.write(u"\u015d\3\2\2\2\u07fa\u07fb\b\u00b0\1\2\u07fb\u07fc\5")
        buf.write(u"\u0152\u00aa\2\u07fc\u0802\3\2\2\2\u07fd\u07fe\f\3\2")
        buf.write(u"\2\u07fe\u07ff\7\17\2\2\u07ff\u0801\5\u0152\u00aa\2\u0800")
        buf.write(u"\u07fd\3\2\2\2\u0801\u0804\3\2\2\2\u0802\u0800\3\2\2")
        buf.write(u"\2\u0802\u0803\3\2\2\2\u0803\u015f\3\2\2\2\u0804\u0802")
        buf.write(u"\3\2\2\2\u0805\u0806\b\u00b1\1\2\u0806\u0807\5\u0168")
        buf.write(u"\u00b5\2\u0807\u0808\7)\2\2\u0808\u0809\5\u0152\u00aa")
        buf.write(u"\2\u0809\u0812\3\2\2\2\u080a\u080b\f\3\2\2\u080b\u080c")
        buf.write(u"\7\17\2\2\u080c\u080d\5\u0168\u00b5\2\u080d\u080e\7)")
        buf.write(u"\2\2\u080e\u080f\5\u0152\u00aa\2\u080f\u0811\3\2\2\2")
        buf.write(u"\u0810\u080a\3\2\2\2\u0811\u0814\3\2\2\2\u0812\u0810")
        buf.write(u"\3\2\2\2\u0812\u0813\3\2\2\2\u0813\u0161\3\2\2\2\u0814")
        buf.write(u"\u0812\3\2\2\2\u0815\u0816\7\22\2\2\u0816\u0817\5\u0152")
        buf.write(u"\u00aa\2\u0817\u0818\7\23\2\2\u0818\u0163\3\2\2\2\u0819")
        buf.write(u"\u081a\b\u00b3\1\2\u081a\u081d\7\u00a4\2\2\u081b\u081d")
        buf.write(u"\5\u0168\u00b5\2\u081c\u0819\3\2\2\2\u081c\u081b\3\2")
        buf.write(u"\2\2\u081d\u0823\3\2\2\2\u081e\u081f\f\3\2\2\u081f\u0820")
        buf.write(u"\7\21\2\2\u0820\u0822\5\u0168\u00b5\2\u0821\u081e\3\2")
        buf.write(u"\2\2\u0822\u0825\3\2\2\2\u0823\u0821\3\2\2\2\u0823\u0824")
        buf.write(u"\3\2\2\2\u0824\u0165\3\2\2\2\u0825\u0823\3\2\2\2\u0826")
        buf.write(u"\u082c\7\u00a7\2\2\u0827\u082c\7\u00a9\2\2\u0828\u082c")
        buf.write(u"\7\u00a5\2\2\u0829\u082c\7\u009c\2\2\u082a\u082c\7\u009d")
        buf.write(u"\2\2\u082b\u0826\3\2\2\2\u082b\u0827\3\2\2\2\u082b\u0828")
        buf.write(u"\3\2\2\2\u082b\u0829\3\2\2\2\u082b\u082a\3\2\2\2\u082c")
        buf.write(u"\u0167\3\2\2\2\u082d\u082e\t\b\2\2\u082e\u0169\3\2\2")
        buf.write(u"\2\u082f\u0830\7\u0087\2\2\u0830\u0831\5\u016c\u00b7")
        buf.write(u"\2\u0831\u0832\7\16\2\2\u0832\u0837\3\2\2\2\u0833\u0834")
        buf.write(u"\5\u016c\u00b7\2\u0834\u0835\7\16\2\2\u0835\u0837\3\2")
        buf.write(u"\2\2\u0836\u082f\3\2\2\2\u0836\u0833\3\2\2\2\u0837\u016b")
        buf.write(u"\3\2\2\2\u0838\u0839\b\u00b7\1\2\u0839\u083a\5\u016e")
        buf.write(u"\u00b8\2\u083a\u083f\3\2\2\2\u083b\u083c\f\3\2\2\u083c")
        buf.write(u"\u083e\5\u0174\u00bb\2\u083d\u083b\3\2\2\2\u083e\u0841")
        buf.write(u"\3\2\2\2\u083f\u083d\3\2\2\2\u083f\u0840\3\2\2\2\u0840")
        buf.write(u"\u016d\3\2\2\2\u0841\u083f\3\2\2\2\u0842\u0848\5\u0170")
        buf.write(u"\u00b9\2\u0843\u0848\5\u0172\u00ba\2\u0844\u0848\5\u017c")
        buf.write(u"\u00bf\2\u0845\u0848\5\u017e\u00c0\2\u0846\u0848\5\u0182")
        buf.write(u"\u00c2\2\u0847\u0842\3\2\2\2\u0847\u0843\3\2\2\2\u0847")
        buf.write(u"\u0844\3\2\2\2\u0847\u0845\3\2\2\2\u0847\u0846\3\2\2")
        buf.write(u"\2\u0848\u016f\3\2\2\2\u0849\u084a\5\u00fa~\2\u084a\u0171")
        buf.write(u"\3\2\2\2\u084b\u084c\5\u011e\u0090\2\u084c\u084d\5\u0176")
        buf.write(u"\u00bc\2\u084d\u0173\3\2\2\2\u084e\u084f\7\21\2\2\u084f")
        buf.write(u"\u0852\5\u0176\u00bc\2\u0850\u0852\5\u017a\u00be\2\u0851")
        buf.write(u"\u084e\3\2\2\2\u0851\u0850\3\2\2\2\u0852\u0175\3\2\2")
        buf.write(u"\2\u0853\u0854\5\u0184\u00c3\2\u0854\u0856\7\22\2\2\u0855")
        buf.write(u"\u0857\5\u0178\u00bd\2\u0856\u0855\3\2\2\2\u0856\u0857")
        buf.write(u"\3\2\2\2\u0857\u0858\3\2\2\2\u0858\u0859\7\23\2\2\u0859")
        buf.write(u"\u0177\3\2\2\2\u085a\u085b\b\u00bd\1\2\u085b\u085c\5")
        buf.write(u"\u016c\u00b7\2\u085c\u0862\3\2\2\2\u085d\u085e\f\3\2")
        buf.write(u"\2\u085e\u085f\7\17\2\2\u085f\u0861\5\u016c\u00b7\2\u0860")
        buf.write(u"\u085d\3\2\2\2\u0861\u0864\3\2\2\2\u0862\u0860\3\2\2")
        buf.write(u"\2\u0862\u0863\3\2\2\2\u0863\u0179\3\2\2\2\u0864\u0862")
        buf.write(u"\3\2\2\2\u0865\u0866\7\24\2\2\u0866\u0867\5\u016c\u00b7")
        buf.write(u"\2\u0867\u0868\7\25\2\2\u0868\u017b\3\2\2\2\u0869\u086a")
        buf.write(u"\7\22\2\2\u086a\u086b\5\u016c\u00b7\2\u086b\u086c\7\23")
        buf.write(u"\2\2\u086c\u017d\3\2\2\2\u086d\u086e\b\u00c0\1\2\u086e")
        buf.write(u"\u086f\5\u0184\u00c3\2\u086f\u0875\3\2\2\2\u0870\u0871")
        buf.write(u"\f\3\2\2\u0871\u0872\7\21\2\2\u0872\u0874\5\u0184\u00c3")
        buf.write(u"\2\u0873\u0870\3\2\2\2\u0874\u0877\3\2\2\2\u0875\u0873")
        buf.write(u"\3\2\2\2\u0875\u0876\3\2\2\2\u0876\u017f\3\2\2\2\u0877")
        buf.write(u"\u0875\3\2\2\2\u0878\u0879\b\u00c1\1\2\u0879\u087a\5")
        buf.write(u"\u017e\u00c0\2\u087a\u087f\3\2\2\2\u087b\u087c\f\3\2")
        buf.write(u"\2\u087c\u087e\7\u00a4\2\2\u087d\u087b\3\2\2\2\u087e")
        buf.write(u"\u0881\3\2\2\2\u087f\u087d\3\2\2\2\u087f\u0880\3\2\2")
        buf.write(u"\2\u0880\u0181\3\2\2\2\u0881\u087f\3\2\2\2\u0882\u0888")
        buf.write(u"\7\u00a7\2\2\u0883\u0888\7\u00a9\2\2\u0884\u0888\7\u00a5")
        buf.write(u"\2\2\u0885\u0888\7\u009c\2\2\u0886\u0888\7\u009d\2\2")
        buf.write(u"\u0887\u0882\3\2\2\2\u0887\u0883\3\2\2\2\u0887\u0884")
        buf.write(u"\3\2\2\2\u0887\u0885\3\2\2\2\u0887\u0886\3\2\2\2\u0888")
        buf.write(u"\u0183\3\2\2\2\u0889\u088a\t\t\2\2\u088a\u0185\3\2\2")
        buf.write(u"\2\u088b\u088c\7\u0087\2\2\u088c\u088d\5\u0188\u00c5")
        buf.write(u"\2\u088d\u088e\7\16\2\2\u088e\u0893\3\2\2\2\u088f\u0890")
        buf.write(u"\5\u0188\u00c5\2\u0890\u0891\7\16\2\2\u0891\u0893\3\2")
        buf.write(u"\2\2\u0892\u088b\3\2\2\2\u0892\u088f\3\2\2\2\u0893\u0187")
        buf.write(u"\3\2\2\2\u0894\u0895\b\u00c5\1\2\u0895\u0896\5\u018a")
        buf.write(u"\u00c6\2\u0896\u089b\3\2\2\2\u0897\u0898\f\3\2\2\u0898")
        buf.write(u"\u089a\5\u0190\u00c9\2\u0899\u0897\3\2\2\2\u089a\u089d")
        buf.write(u"\3\2\2\2\u089b\u0899\3\2\2\2\u089b\u089c\3\2\2\2\u089c")
        buf.write(u"\u0189\3\2\2\2\u089d\u089b\3\2\2\2\u089e\u08a4\5\u018c")
        buf.write(u"\u00c7\2\u089f\u08a4\5\u018e\u00c8\2\u08a0\u08a4\5\u0198")
        buf.write(u"\u00cd\2\u08a1\u08a4\5\u019a\u00ce\2\u08a2\u08a4\5\u019c")
        buf.write(u"\u00cf\2\u08a3\u089e\3\2\2\2\u08a3\u089f\3\2\2\2\u08a3")
        buf.write(u"\u08a0\3\2\2\2\u08a3\u08a1\3\2\2\2\u08a3\u08a2\3\2\2")
        buf.write(u"\2\u08a4\u018b\3\2\2\2\u08a5\u08a6\5\u00fa~\2\u08a6\u018d")
        buf.write(u"\3\2\2\2\u08a7\u08a8\5\u011e\u0090\2\u08a8\u08a9\5\u0192")
        buf.write(u"\u00ca\2\u08a9\u018f\3\2\2\2\u08aa\u08ab\7\21\2\2\u08ab")
        buf.write(u"\u08ae\5\u0192\u00ca\2\u08ac\u08ae\5\u0196\u00cc\2\u08ad")
        buf.write(u"\u08aa\3\2\2\2\u08ad\u08ac\3\2\2\2\u08ae\u0191\3\2\2")
        buf.write(u"\2\u08af\u08b0\5\u019e\u00d0\2\u08b0\u08b2\7\22\2\2\u08b1")
        buf.write(u"\u08b3\5\u0194\u00cb\2\u08b2\u08b1\3\2\2\2\u08b2\u08b3")
        buf.write(u"\3\2\2\2\u08b3\u08b4\3\2\2\2\u08b4\u08b5\7\23\2\2\u08b5")
        buf.write(u"\u0193\3\2\2\2\u08b6\u08b7\b\u00cb\1\2\u08b7\u08b8\5")
        buf.write(u"\u0188\u00c5\2\u08b8\u08be\3\2\2\2\u08b9\u08ba\f\3\2")
        buf.write(u"\2\u08ba\u08bb\7\17\2\2\u08bb\u08bd\5\u0188\u00c5\2\u08bc")
        buf.write(u"\u08b9\3\2\2\2\u08bd\u08c0\3\2\2\2\u08be\u08bc\3\2\2")
        buf.write(u"\2\u08be\u08bf\3\2\2\2\u08bf\u0195\3\2\2\2\u08c0\u08be")
        buf.write(u"\3\2\2\2\u08c1\u08c2\7\24\2\2\u08c2\u08c3\5\u0188\u00c5")
        buf.write(u"\2\u08c3\u08c4\7\25\2\2\u08c4\u0197\3\2\2\2\u08c5\u08c6")
        buf.write(u"\7\22\2\2\u08c6\u08c7\5\u0188\u00c5\2\u08c7\u08c8\7\23")
        buf.write(u"\2\2\u08c8\u0199\3\2\2\2\u08c9\u08ca\b\u00ce\1\2\u08ca")
        buf.write(u"\u08cd\7\u00a4\2\2\u08cb\u08cd\5\u019e\u00d0\2\u08cc")
        buf.write(u"\u08c9\3\2\2\2\u08cc\u08cb\3\2\2\2\u08cd\u08d3\3\2\2")
        buf.write(u"\2\u08ce\u08cf\f\3\2\2\u08cf\u08d0\7\21\2\2\u08d0\u08d2")
        buf.write(u"\5\u019e\u00d0\2\u08d1\u08ce\3\2\2\2\u08d2\u08d5\3\2")
        buf.write(u"\2\2\u08d3\u08d1\3\2\2\2\u08d3\u08d4\3\2\2\2\u08d4\u019b")
        buf.write(u"\3\2\2\2\u08d5\u08d3\3\2\2\2\u08d6\u08dc\7\u00a7\2\2")
        buf.write(u"\u08d7\u08dc\7\u00a9\2\2\u08d8\u08dc\7\u00a5\2\2\u08d9")
        buf.write(u"\u08dc\7\u009c\2\2\u08da\u08dc\7\u009d\2\2\u08db\u08d6")
        buf.write(u"\3\2\2\2\u08db\u08d7\3\2\2\2\u08db\u08d8\3\2\2\2\u08db")
        buf.write(u"\u08d9\3\2\2\2\u08db\u08da\3\2\2\2\u08dc\u019d\3\2\2")
        buf.write(u"\2\u08dd\u08de\t\n\2\2\u08de\u019f\3\2\2\2\u00c8\u01a7")
        buf.write(u"\u01ab\u01c6\u01cd\u01d5\u01d7\u01dc\u01e4\u01e8\u01f2")
        buf.write(u"\u01fe\u0204\u0207\u020a\u0213\u021b\u0220\u0226\u022e")
        buf.write(u"\u0233\u0239\u0244\u0249\u024e\u0257\u025c\u0270\u0275")
        buf.write(u"\u027b\u0281\u0287\u028c\u0291\u0294\u029a\u02b1\u02bb")
        buf.write(u"\u02c0\u02c7\u02c9\u02e0\u02fe\u0315\u0317\u031f\u0326")
        buf.write(u"\u0328\u0330\u033a\u034f\u0353\u0367\u0374\u0378\u0380")
        buf.write(u"\u0383\u0388\u038b\u0393\u039e\u03a2\u03a9\u03b0\u03b9")
        buf.write(u"\u03c2\u03cb\u03e4\u0458\u045a\u046a\u0476\u0480\u049f")
        buf.write(u"\u04ac\u04b2\u04bb\u04c2\u04ca\u04cc\u04d0\u04d9\u04e7")
        buf.write(u"\u04ec\u04f5\u04fc\u050e\u0518\u0523\u052b\u0533\u0539")
        buf.write(u"\u0541\u054a\u0552\u055f\u0562\u0566\u056b\u056f\u0578")
        buf.write(u"\u058d\u0597\u0599\u059e\u05af\u05b4\u05bd\u05c4\u05c9")
        buf.write(u"\u05ce\u05dd\u05e2\u05e5\u05e9\u05ee\u05f5\u0600\u0602")
        buf.write(u"\u060b\u0613\u061b\u0621\u062d\u0631\u063b\u0640\u0646")
        buf.write(u"\u064d\u0652\u0659\u0661\u0668\u0672\u067f\u0683\u0686")
        buf.write(u"\u068a\u068d\u0695\u069e\u06a7\u06b0\u06c1\u06d2\u06d9")
        buf.write(u"\u06e0\u06ea\u06f1\u06f4\u06f8\u06fd\u0701\u070c\u070f")
        buf.write(u"\u0716\u0726\u0733\u073a\u074b\u0753\u0757\u075f\u0785")
        buf.write(u"\u078e\u0798\u07a4\u07a9\u07b5\u07c7\u07ce\u07d7\u07df")
        buf.write(u"\u07e9\u07ee\u07f8\u0802\u0812\u081c\u0823\u082b\u0836")
        buf.write(u"\u083f\u0847\u0851\u0856\u0862\u0875\u087f\u0887\u0892")
        buf.write(u"\u089b\u08a3\u08ad\u08b2\u08be\u08cc\u08d3\u08db")
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
                     u"'Document'", u"'Blob'", u"'Image'", u"'UUID'", u"'Iterator'", 
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
    RULE_argument_assignment_list = 59
    RULE_argument_assignment = 60
    RULE_assign_instance_statement = 61
    RULE_child_instance = 62
    RULE_assign_tuple_statement = 63
    RULE_null_literal = 64
    RULE_declaration_list = 65
    RULE_declarations = 66
    RULE_declaration = 67
    RULE_resource_declaration = 68
    RULE_enum_declaration = 69
    RULE_native_symbol_list = 70
    RULE_category_symbol_list = 71
    RULE_symbol_list = 72
    RULE_attribute_constraint = 73
    RULE_list_literal = 74
    RULE_set_literal = 75
    RULE_expression_list = 76
    RULE_range_literal = 77
    RULE_typedef = 78
    RULE_primary_type = 79
    RULE_native_type = 80
    RULE_category_type = 81
    RULE_mutable_category_type = 82
    RULE_code_type = 83
    RULE_category_declaration = 84
    RULE_type_identifier_list = 85
    RULE_method_identifier = 86
    RULE_identifier = 87
    RULE_variable_identifier = 88
    RULE_attribute_identifier = 89
    RULE_type_identifier = 90
    RULE_symbol_identifier = 91
    RULE_argument_list = 92
    RULE_argument = 93
    RULE_operator_argument = 94
    RULE_named_argument = 95
    RULE_code_argument = 96
    RULE_category_or_any_type = 97
    RULE_any_type = 98
    RULE_member_method_declaration_list = 99
    RULE_member_method_declaration = 100
    RULE_native_member_method_declaration_list = 101
    RULE_native_member_method_declaration = 102
    RULE_native_category_binding = 103
    RULE_python_category_binding = 104
    RULE_python_module = 105
    RULE_javascript_category_binding = 106
    RULE_javascript_module = 107
    RULE_variable_identifier_list = 108
    RULE_attribute_identifier_list = 109
    RULE_method_declaration = 110
    RULE_comment_statement = 111
    RULE_native_statement_list = 112
    RULE_native_statement = 113
    RULE_python_native_statement = 114
    RULE_javascript_native_statement = 115
    RULE_statement_list = 116
    RULE_assertion_list = 117
    RULE_switch_case_statement_list = 118
    RULE_catch_statement_list = 119
    RULE_literal_collection = 120
    RULE_atomic_literal = 121
    RULE_literal_list_literal = 122
    RULE_selectable_expression = 123
    RULE_this_expression = 124
    RULE_parenthesis_expression = 125
    RULE_literal_expression = 126
    RULE_collection_literal = 127
    RULE_tuple_literal = 128
    RULE_dict_literal = 129
    RULE_expression_tuple = 130
    RULE_dict_entry_list = 131
    RULE_dict_entry = 132
    RULE_slice_arguments = 133
    RULE_assign_variable_statement = 134
    RULE_assignable_instance = 135
    RULE_is_expression = 136
    RULE_read_all_expression = 137
    RULE_read_one_expression = 138
    RULE_order_by_list = 139
    RULE_order_by = 140
    RULE_operator = 141
    RULE_new_token = 142
    RULE_key_token = 143
    RULE_module_token = 144
    RULE_value_token = 145
    RULE_symbols_token = 146
    RULE_assign = 147
    RULE_multiply = 148
    RULE_divide = 149
    RULE_idivide = 150
    RULE_modulo = 151
    RULE_lfs = 152
    RULE_lfp = 153
    RULE_javascript_statement = 154
    RULE_javascript_expression = 155
    RULE_javascript_primary_expression = 156
    RULE_javascript_this_expression = 157
    RULE_javascript_new_expression = 158
    RULE_javascript_selector_expression = 159
    RULE_javascript_method_expression = 160
    RULE_javascript_arguments = 161
    RULE_javascript_item_expression = 162
    RULE_javascript_parenthesis_expression = 163
    RULE_javascript_identifier_expression = 164
    RULE_javascript_literal_expression = 165
    RULE_javascript_identifier = 166
    RULE_python_statement = 167
    RULE_python_expression = 168
    RULE_python_primary_expression = 169
    RULE_python_self_expression = 170
    RULE_python_selector_expression = 171
    RULE_python_method_expression = 172
    RULE_python_argument_list = 173
    RULE_python_ordinal_argument_list = 174
    RULE_python_named_argument_list = 175
    RULE_python_parenthesis_expression = 176
    RULE_python_identifier_expression = 177
    RULE_python_literal_expression = 178
    RULE_python_identifier = 179
    RULE_java_statement = 180
    RULE_java_expression = 181
    RULE_java_primary_expression = 182
    RULE_java_this_expression = 183
    RULE_java_new_expression = 184
    RULE_java_selector_expression = 185
    RULE_java_method_expression = 186
    RULE_java_arguments = 187
    RULE_java_item_expression = 188
    RULE_java_parenthesis_expression = 189
    RULE_java_identifier_expression = 190
    RULE_java_class_identifier_expression = 191
    RULE_java_literal_expression = 192
    RULE_java_identifier = 193
    RULE_csharp_statement = 194
    RULE_csharp_expression = 195
    RULE_csharp_primary_expression = 196
    RULE_csharp_this_expression = 197
    RULE_csharp_new_expression = 198
    RULE_csharp_selector_expression = 199
    RULE_csharp_method_expression = 200
    RULE_csharp_arguments = 201
    RULE_csharp_item_expression = 202
    RULE_csharp_parenthesis_expression = 203
    RULE_csharp_identifier_expression = 204
    RULE_csharp_literal_expression = 205
    RULE_csharp_identifier = 206

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
                   u"argument_assignment_list", u"argument_assignment", 
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
                   u"order_by_list", u"order_by", u"operator", u"new_token", 
                   u"key_token", u"module_token", u"value_token", u"symbols_token", 
                   u"assign", u"multiply", u"divide", u"idivide", u"modulo", 
                   u"lfs", u"lfp", u"javascript_statement", u"javascript_expression", 
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
                   u"csharp_literal_expression", u"csharp_identifier" ]

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
            self.state = 414
            self.match(OParser.ENUMERATED)
            self.state = 415
            self.match(OParser.CATEGORY)
            self.state = 416
            localctx.name = self.type_identifier()
            self.state = 421
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 417
                self.match(OParser.LPAR)
                self.state = 418
                localctx.attrs = self.attribute_identifier_list()
                self.state = 419
                self.match(OParser.RPAR)


            self.state = 425
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.EXTENDS:
                self.state = 423
                self.match(OParser.EXTENDS)
                self.state = 424
                localctx.derived = self.type_identifier()


            self.state = 427
            self.match(OParser.LCURL)
            self.state = 428
            localctx.symbols = self.category_symbol_list()
            self.state = 429
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
            self.state = 431
            self.match(OParser.ENUMERATED)
            self.state = 432
            localctx.name = self.type_identifier()
            self.state = 433
            self.match(OParser.LPAR)
            self.state = 434
            localctx.typ = self.native_type()
            self.state = 435
            self.match(OParser.RPAR)
            self.state = 436
            self.match(OParser.LCURL)
            self.state = 437
            localctx.symbols = self.native_symbol_list()
            self.state = 438
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
            self.state = 440
            localctx.name = self.symbol_identifier()
            self.state = 441
            self.match(OParser.LPAR)
            self.state = 442
            localctx.args = self.argument_assignment_list(0)
            self.state = 443
            self.match(OParser.RPAR)
            self.state = 444
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
            self.state = 446
            localctx.name = self.symbol_identifier()
            self.state = 447
            self.match(OParser.EQ)
            self.state = 448
            localctx.exp = self.expression(0)
            self.state = 449
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
            self.state = 452
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.STORABLE:
                self.state = 451
                self.match(OParser.STORABLE)


            self.state = 454
            self.match(OParser.ATTRIBUTE)
            self.state = 455
            localctx.name = self.attribute_identifier()
            self.state = 456
            self.match(OParser.COLON)
            self.state = 457
            localctx.typ = self.typedef(0)
            self.state = 459
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.IN or _la==OParser.MATCHING:
                self.state = 458
                localctx.match = self.attribute_constraint()


            self.state = 469
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.WITH:
                self.state = 461
                self.match(OParser.WITH)
                self.state = 462
                self.match(OParser.INDEX)
                self.state = 467
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==OParser.LPAR:
                    self.state = 463
                    self.match(OParser.LPAR)
                    self.state = 464
                    localctx.indices = self.variable_identifier_list()
                    self.state = 465
                    self.match(OParser.RPAR)




            self.state = 471
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
            self.state = 474
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.STORABLE:
                self.state = 473
                self.match(OParser.STORABLE)


            self.state = 476
            self.match(OParser.CATEGORY)
            self.state = 477
            localctx.name = self.type_identifier()
            self.state = 482
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 478
                self.match(OParser.LPAR)
                self.state = 479
                localctx.attrs = self.attribute_identifier_list()
                self.state = 480
                self.match(OParser.RPAR)


            self.state = 486
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.EXTENDS:
                self.state = 484
                self.match(OParser.EXTENDS)
                self.state = 485
                localctx.derived = self.derived_list(0)


            self.state = 488
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
            self.state = 490
            self.match(OParser.SINGLETON)
            self.state = 491
            localctx.name = self.type_identifier()
            self.state = 496
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 492
                self.match(OParser.LPAR)
                self.state = 493
                localctx.attrs = self.attribute_identifier_list()
                self.state = 494
                self.match(OParser.RPAR)


            self.state = 498
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

            self.state = 501
            localctx.item = self.type_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 508
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
                    self.state = 503
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 504
                    self.match(OParser.COMMA)
                    self.state = 505
                    localctx.item = self.type_identifier() 
                self.state = 510
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
            self.state = 517
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.SEMI]:
                localctx = OParser.EmptyCategoryMethodListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.match(OParser.SEMI)
                pass
            elif token in [OParser.LCURL]:
                localctx = OParser.CurlyCategoryMethodListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 512
                self.match(OParser.LCURL)
                self.state = 514
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ABSTRACT - 46)) | (1 << (OParser.GETTER - 46)))) != 0) or ((((_la - 112)) & ~0x3f) == 0 and ((1 << (_la - 112)) & ((1 << (OParser.METHOD - 112)) | (1 << (OParser.OPERATOR - 112)) | (1 << (OParser.SETTER - 112)) | (1 << (OParser.TYPE_IDENTIFIER - 112)))) != 0):
                    self.state = 513
                    localctx.items = self.member_method_declaration_list()


                self.state = 516
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
            self.state = 520
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or _la==OParser.TYPE_IDENTIFIER:
                self.state = 519
                localctx.typ = self.typedef(0)


            self.state = 522
            self.match(OParser.OPERATOR)
            self.state = 523
            localctx.op = self.operator()
            self.state = 524
            self.match(OParser.LPAR)
            self.state = 525
            localctx.arg = self.operator_argument()
            self.state = 526
            self.match(OParser.RPAR)
            self.state = 527
            self.match(OParser.LCURL)
            self.state = 529
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                self.state = 528
                localctx.stmts = self.statement_list()


            self.state = 531
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
            self.state = 533
            self.match(OParser.SETTER)
            self.state = 534
            localctx.name = self.variable_identifier()
            self.state = 535
            self.match(OParser.LCURL)
            self.state = 537
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                self.state = 536
                localctx.stmts = self.statement_list()


            self.state = 539
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
            self.state = 542
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.NATIVE:
                self.state = 541
                self.match(OParser.NATIVE)


            self.state = 544
            self.match(OParser.SETTER)
            self.state = 545
            localctx.name = self.variable_identifier()
            self.state = 546
            self.match(OParser.LCURL)
            self.state = 548
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.JAVA) | (1 << OParser.CSHARP) | (1 << OParser.PYTHON2) | (1 << OParser.PYTHON3) | (1 << OParser.JAVASCRIPT))) != 0):
                self.state = 547
                localctx.stmts = self.native_statement_list()


            self.state = 550
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
            self.state = 552
            self.match(OParser.GETTER)
            self.state = 553
            localctx.name = self.variable_identifier()
            self.state = 554
            self.match(OParser.LCURL)
            self.state = 556
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                self.state = 555
                localctx.stmts = self.statement_list()


            self.state = 558
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
            self.state = 561
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.NATIVE:
                self.state = 560
                self.match(OParser.NATIVE)


            self.state = 563
            self.match(OParser.GETTER)
            self.state = 564
            localctx.name = self.variable_identifier()
            self.state = 565
            self.match(OParser.LCURL)
            self.state = 567
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.JAVA) | (1 << OParser.CSHARP) | (1 << OParser.PYTHON2) | (1 << OParser.PYTHON3) | (1 << OParser.JAVASCRIPT))) != 0):
                self.state = 566
                localctx.stmts = self.native_statement_list()


            self.state = 569
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
            self.state = 571
            self.match(OParser.NATIVE)
            self.state = 572
            self.match(OParser.RESOURCE)
            self.state = 573
            localctx.name = self.type_identifier()
            self.state = 578
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 574
                self.match(OParser.LPAR)
                self.state = 575
                localctx.attrs = self.attribute_identifier_list()
                self.state = 576
                self.match(OParser.RPAR)


            self.state = 580
            self.match(OParser.LCURL)
            self.state = 581
            localctx.bindings = self.native_category_bindings()
            self.state = 583
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ANY - 46)) | (1 << (OParser.GETTER - 46)))) != 0) or ((((_la - 112)) & ~0x3f) == 0 and ((1 << (_la - 112)) & ((1 << (OParser.METHOD - 112)) | (1 << (OParser.NATIVE - 112)) | (1 << (OParser.SETTER - 112)) | (1 << (OParser.TYPE_IDENTIFIER - 112)))) != 0):
                self.state = 582
                localctx.methods = self.native_member_method_declaration_list()


            self.state = 585
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
            self.state = 588
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.STORABLE:
                self.state = 587
                self.match(OParser.STORABLE)


            self.state = 590
            self.match(OParser.NATIVE)
            self.state = 591
            self.match(OParser.CATEGORY)
            self.state = 592
            localctx.name = self.type_identifier()
            self.state = 597
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 593
                self.match(OParser.LPAR)
                self.state = 594
                localctx.attrs = self.attribute_identifier_list()
                self.state = 595
                self.match(OParser.RPAR)


            self.state = 599
            self.match(OParser.LCURL)
            self.state = 600
            localctx.bindings = self.native_category_bindings()
            self.state = 602
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ANY - 46)) | (1 << (OParser.GETTER - 46)))) != 0) or ((((_la - 112)) & ~0x3f) == 0 and ((1 << (_la - 112)) & ((1 << (OParser.METHOD - 112)) | (1 << (OParser.NATIVE - 112)) | (1 << (OParser.SETTER - 112)) | (1 << (OParser.TYPE_IDENTIFIER - 112)))) != 0):
                self.state = 601
                localctx.methods = self.native_member_method_declaration_list()


            self.state = 604
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
            self.state = 606
            self.match(OParser.CATEGORY)
            self.state = 607
            self.match(OParser.BINDINGS)
            self.state = 608
            self.match(OParser.LCURL)
            self.state = 609
            localctx.items = self.native_category_binding_list(0)
            self.state = 610
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

            self.state = 613
            localctx.item = self.native_category_binding()
            self.state = 614
            self.match(OParser.SEMI)
            self._ctx.stop = self._input.LT(-1)
            self.state = 622
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.NativeCategoryBindingListItemContext(self, OParser.Native_category_binding_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_category_binding_list)
                    self.state = 616
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 617
                    localctx.item = self.native_category_binding()
                    self.state = 618
                    self.match(OParser.SEMI) 
                self.state = 624
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
            self.state = 625
            self.match(OParser.ABSTRACT)
            self.state = 627
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or _la==OParser.TYPE_IDENTIFIER:
                self.state = 626
                localctx.typ = self.typedef(0)


            self.state = 629
            self.match(OParser.METHOD)
            self.state = 630
            localctx.name = self.method_identifier()
            self.state = 631
            self.match(OParser.LPAR)
            self.state = 633
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ANY - 46)))) != 0) or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (OParser.MUTABLE - 115)) | (1 << (OParser.TYPE_IDENTIFIER - 115)) | (1 << (OParser.VARIABLE_IDENTIFIER - 115)))) != 0):
                self.state = 632
                localctx.args = self.argument_list()


            self.state = 635
            self.match(OParser.RPAR)
            self.state = 636
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
            self.state = 639
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or _la==OParser.TYPE_IDENTIFIER:
                self.state = 638
                localctx.typ = self.typedef(0)


            self.state = 641
            self.match(OParser.METHOD)
            self.state = 642
            localctx.name = self.method_identifier()
            self.state = 643
            self.match(OParser.LPAR)
            self.state = 645
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ANY - 46)))) != 0) or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (OParser.MUTABLE - 115)) | (1 << (OParser.TYPE_IDENTIFIER - 115)) | (1 << (OParser.VARIABLE_IDENTIFIER - 115)))) != 0):
                self.state = 644
                localctx.args = self.argument_list()


            self.state = 647
            self.match(OParser.RPAR)
            self.state = 648
            self.match(OParser.LCURL)
            self.state = 650
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                self.state = 649
                localctx.stmts = self.statement_list()


            self.state = 652
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
            self.state = 655
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ANY - 46)))) != 0) or _la==OParser.TYPE_IDENTIFIER:
                self.state = 654
                localctx.typ = self.category_or_any_type()


            self.state = 658
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.NATIVE:
                self.state = 657
                self.match(OParser.NATIVE)


            self.state = 660
            self.match(OParser.METHOD)
            self.state = 661
            localctx.name = self.method_identifier()
            self.state = 662
            self.match(OParser.LPAR)
            self.state = 664
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ANY - 46)))) != 0) or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (OParser.MUTABLE - 115)) | (1 << (OParser.TYPE_IDENTIFIER - 115)) | (1 << (OParser.VARIABLE_IDENTIFIER - 115)))) != 0):
                self.state = 663
                localctx.args = self.argument_list()


            self.state = 666
            self.match(OParser.RPAR)
            self.state = 667
            self.match(OParser.LCURL)
            self.state = 668
            localctx.stmts = self.native_statement_list()
            self.state = 669
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
            self.state = 671
            self.match(OParser.TEST)
            self.state = 672
            self.match(OParser.METHOD)
            self.state = 673
            localctx.name = self.match(OParser.TEXT_LITERAL)
            self.state = 674
            self.match(OParser.LPAR)
            self.state = 675
            self.match(OParser.RPAR)
            self.state = 676
            self.match(OParser.LCURL)
            self.state = 677
            localctx.stmts = self.statement_list()
            self.state = 678
            self.match(OParser.RCURL)
            self.state = 679
            self.match(OParser.VERIFYING)
            self.state = 687
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.LCURL]:
                self.state = 680
                self.match(OParser.LCURL)
                self.state = 681
                localctx.exps = self.assertion_list()
                self.state = 682
                self.match(OParser.RCURL)
                pass
            elif token in [OParser.SYMBOL_IDENTIFIER]:
                self.state = 684
                localctx.error = self.symbol_identifier()
                self.state = 685
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
            self.state = 689
            localctx.exp = self.expression(0)
            self.state = 690
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
            self.state = 692
            localctx.typ = self.category_or_any_type()
            self.state = 697
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.LPAR:
                self.state = 693
                self.match(OParser.LPAR)
                self.state = 694
                localctx.attrs = self.attribute_identifier_list()
                self.state = 695
                self.match(OParser.RPAR)


            self.state = 699
            localctx.name = self.variable_identifier()
            self.state = 702
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.EQ:
                self.state = 700
                self.match(OParser.EQ)
                self.state = 701
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
            self.state = 711
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.COMMENT, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID, OParser.ITERATOR, OParser.CURSOR, OParser.BREAK, OParser.DELETE, OParser.DO, OParser.FLUSH, OParser.FOR, OParser.IF, OParser.METHOD, OParser.RETURN, OParser.STORE, OParser.SWITCH, OParser.THROW, OParser.TRY, OParser.WITH, OParser.WHILE, OParser.WRITE, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER]:
                localctx = OParser.SingleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 704
                localctx.stmt = self.statement()
                pass
            elif token in [OParser.LCURL]:
                localctx = OParser.CurlyStatementListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 705
                self.match(OParser.LCURL)
                self.state = 709
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                if la_ == 1:
                    self.state = 706
                    localctx.items = self.statement_list()
                    self.state = 707
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
            self.state = 734
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                localctx = OParser.MethodCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 713
                localctx.stmt = self.method_call()
                self.state = 714
                self.match(OParser.SEMI)
                pass

            elif la_ == 2:
                localctx = OParser.AssignInstanceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 716
                localctx.stmt = self.assign_instance_statement()
                pass

            elif la_ == 3:
                localctx = OParser.AssignTupleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 717
                localctx.stmt = self.assign_tuple_statement()
                pass

            elif la_ == 4:
                localctx = OParser.StoreStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 718
                localctx.stmt = self.store_statement()
                pass

            elif la_ == 5:
                localctx = OParser.FlushStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 719
                localctx.stmt = self.flush_statement()
                pass

            elif la_ == 6:
                localctx = OParser.BreakStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 720
                localctx.stmt = self.break_statement()
                pass

            elif la_ == 7:
                localctx = OParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 721
                localctx.stmt = self.return_statement()
                pass

            elif la_ == 8:
                localctx = OParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 722
                localctx.stmt = self.if_statement()
                pass

            elif la_ == 9:
                localctx = OParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 723
                localctx.stmt = self.switch_statement()
                pass

            elif la_ == 10:
                localctx = OParser.ForEachStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 724
                localctx.stmt = self.for_each_statement()
                pass

            elif la_ == 11:
                localctx = OParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 725
                localctx.stmt = self.while_statement()
                pass

            elif la_ == 12:
                localctx = OParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 726
                localctx.stmt = self.do_while_statement()
                pass

            elif la_ == 13:
                localctx = OParser.TryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 727
                localctx.stmt = self.try_statement()
                pass

            elif la_ == 14:
                localctx = OParser.RaiseStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 728
                localctx.stmt = self.raise_statement()
                pass

            elif la_ == 15:
                localctx = OParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 729
                localctx.stmt = self.write_statement()
                pass

            elif la_ == 16:
                localctx = OParser.WithResourceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 730
                localctx.stmt = self.with_resource_statement()
                pass

            elif la_ == 17:
                localctx = OParser.WithSingletonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 731
                localctx.stmt = self.with_singleton_statement()
                pass

            elif la_ == 18:
                localctx = OParser.ClosureStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 732
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 19:
                localctx = OParser.CommentStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 19)
                self.state = 733
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
            self.state = 736
            self.match(OParser.FLUSH)
            self.state = 737
            self.match(OParser.LPAR)
            self.state = 738
            self.match(OParser.RPAR)
            self.state = 739
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
            self.state = 764
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 741
                self.match(OParser.DELETE)
                self.state = 742
                self.match(OParser.LPAR)
                self.state = 743
                localctx.to_del = self.expression_list()
                self.state = 744
                self.match(OParser.RPAR)
                self.state = 745
                self.match(OParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 747
                self.match(OParser.STORE)
                self.state = 748
                self.match(OParser.LPAR)
                self.state = 749
                localctx.to_add = self.expression_list()
                self.state = 750
                self.match(OParser.RPAR)
                self.state = 751
                self.match(OParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 753
                self.match(OParser.DELETE)
                self.state = 754
                self.match(OParser.LPAR)
                self.state = 755
                localctx.to_del = self.expression_list()
                self.state = 756
                self.match(OParser.RPAR)
                self.state = 757
                self.match(OParser.AND)
                self.state = 758
                self.match(OParser.STORE)
                self.state = 759
                self.match(OParser.LPAR)
                self.state = 760
                localctx.to_add = self.expression_list()
                self.state = 761
                self.match(OParser.RPAR)
                self.state = 762
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
            self.state = 766
            self.match(OParser.WITH)
            self.state = 767
            self.match(OParser.LPAR)
            self.state = 768
            localctx.stmt = self.assign_variable_statement()
            self.state = 769
            self.match(OParser.RPAR)
            self.state = 770
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
            self.state = 772
            self.match(OParser.WITH)
            self.state = 773
            self.match(OParser.LPAR)
            self.state = 774
            localctx.typ = self.type_identifier()
            self.state = 775
            self.match(OParser.RPAR)
            self.state = 776
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
            self.state = 778
            self.match(OParser.SWITCH)
            self.state = 779
            self.match(OParser.LPAR)
            self.state = 780
            localctx.exp = self.expression(0)
            self.state = 781
            self.match(OParser.RPAR)
            self.state = 782
            self.match(OParser.LCURL)
            self.state = 783
            localctx.cases = self.switch_case_statement_list()
            self.state = 789
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.DEFAULT:
                self.state = 784
                self.match(OParser.DEFAULT)
                self.state = 785
                self.match(OParser.COLON)
                self.state = 787
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                    self.state = 786
                    localctx.stmts = self.statement_list()




            self.state = 791
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
            self.state = 806
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                localctx = OParser.AtomicSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 793
                self.match(OParser.CASE)
                self.state = 794
                localctx.exp = self.atomic_literal()
                self.state = 795
                self.match(OParser.COLON)
                self.state = 797
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                    self.state = 796
                    localctx.stmts = self.statement_list()


                pass

            elif la_ == 2:
                localctx = OParser.CollectionSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 799
                self.match(OParser.CASE)
                self.state = 800
                self.match(OParser.IN)
                self.state = 801
                localctx.exp = self.literal_collection()
                self.state = 802
                self.match(OParser.COLON)
                self.state = 804
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                    self.state = 803
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
            self.state = 808
            self.match(OParser.FOR)
            self.state = 809
            self.match(OParser.EACH)
            self.state = 810
            self.match(OParser.LPAR)
            self.state = 811
            localctx.name1 = self.variable_identifier()
            self.state = 814
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.COMMA:
                self.state = 812
                self.match(OParser.COMMA)
                self.state = 813
                localctx.name2 = self.variable_identifier()


            self.state = 816
            self.match(OParser.IN)
            self.state = 817
            localctx.source = self.expression(0)
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
            self.state = 821
            self.match(OParser.DO)
            self.state = 822
            self.match(OParser.LCURL)
            self.state = 824
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                self.state = 823
                localctx.stmts = self.statement_list()


            self.state = 826
            self.match(OParser.RCURL)
            self.state = 827
            self.match(OParser.WHILE)
            self.state = 828
            self.match(OParser.LPAR)
            self.state = 829
            localctx.exp = self.expression(0)
            self.state = 830
            self.match(OParser.RPAR)
            self.state = 831
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
            self.state = 833
            self.match(OParser.WHILE)
            self.state = 834
            self.match(OParser.LPAR)
            self.state = 835
            localctx.exp = self.expression(0)
            self.state = 836
            self.match(OParser.RPAR)
            self.state = 837
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
            self.state = 839
            self.match(OParser.IF)
            self.state = 840
            self.match(OParser.LPAR)
            self.state = 841
            localctx.exp = self.expression(0)
            self.state = 842
            self.match(OParser.RPAR)
            self.state = 843
            localctx.stmts = self.statement_or_list()
            self.state = 845
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 844
                localctx.elseIfs = self.else_if_statement_list(0)


            self.state = 849
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 847
                self.match(OParser.ELSE)
                self.state = 848
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

            self.state = 852
            self.match(OParser.ELSE)
            self.state = 853
            self.match(OParser.IF)
            self.state = 854
            self.match(OParser.LPAR)
            self.state = 855
            localctx.exp = self.expression(0)
            self.state = 856
            self.match(OParser.RPAR)
            self.state = 857
            localctx.stmts = self.statement_or_list()
            self._ctx.stop = self._input.LT(-1)
            self.state = 869
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.ElseIfStatementListItemContext(self, OParser.Else_if_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_else_if_statement_list)
                    self.state = 859
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 860
                    self.match(OParser.ELSE)
                    self.state = 861
                    self.match(OParser.IF)
                    self.state = 862
                    self.match(OParser.LPAR)
                    self.state = 863
                    localctx.exp = self.expression(0)
                    self.state = 864
                    self.match(OParser.RPAR)
                    self.state = 865
                    localctx.stmts = self.statement_or_list() 
                self.state = 871
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

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
            self.state = 872
            self.match(OParser.THROW)
            self.state = 873
            localctx.exp = self.expression(0)
            self.state = 874
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
            self.state = 876
            self.match(OParser.TRY)
            self.state = 877
            self.match(OParser.LPAR)
            self.state = 878
            localctx.name = self.variable_identifier()
            self.state = 879
            self.match(OParser.RPAR)
            self.state = 880
            self.match(OParser.LCURL)
            self.state = 882
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                self.state = 881
                localctx.stmts = self.statement_list()


            self.state = 884
            self.match(OParser.RCURL)
            self.state = 886
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 885
                localctx.handlers = self.catch_statement_list()


            self.state = 897
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.state = 888
                self.match(OParser.CATCH)
                self.state = 889
                self.match(OParser.LPAR)
                self.state = 890
                self.match(OParser.ANY)
                self.state = 891
                self.match(OParser.RPAR)
                self.state = 892
                self.match(OParser.LCURL)
                self.state = 894
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                    self.state = 893
                    localctx.anyStmts = self.statement_list()


                self.state = 896
                self.match(OParser.RCURL)


            self.state = 905
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.state = 899
                self.match(OParser.FINALLY)
                self.state = 900
                self.match(OParser.LCURL)
                self.state = 902
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                    self.state = 901
                    localctx.finalStmts = self.statement_list()


                self.state = 904
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
            self.state = 928
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                localctx = OParser.CatchAtomicStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 907
                self.match(OParser.CATCH)
                self.state = 908
                self.match(OParser.LPAR)
                self.state = 909
                localctx.name = self.symbol_identifier()
                self.state = 910
                self.match(OParser.RPAR)
                self.state = 911
                self.match(OParser.LCURL)
                self.state = 913
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                    self.state = 912
                    localctx.stmts = self.statement_list()


                self.state = 915
                self.match(OParser.RCURL)
                pass

            elif la_ == 2:
                localctx = OParser.CatchCollectionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 917
                self.match(OParser.CATCH)
                self.state = 918
                self.match(OParser.IN)
                self.state = 919
                self.match(OParser.LPAR)
                self.state = 920
                localctx.exp = self.symbol_list()
                self.state = 921
                self.match(OParser.RPAR)
                self.state = 922
                self.match(OParser.LCURL)
                self.state = 924
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                    self.state = 923
                    localctx.stmts = self.statement_list()


                self.state = 926
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
            self.state = 930
            self.match(OParser.BREAK)
            self.state = 931
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
            self.state = 933
            self.match(OParser.RETURN)
            self.state = 935
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (OParser.EXECUTE - 95)) | (1 << (OParser.FETCH - 95)) | (1 << (OParser.FILTERED - 95)) | (1 << (OParser.MUTABLE - 95)) | (1 << (OParser.NULL - 95)) | (1 << (OParser.READ - 95)) | (1 << (OParser.SELF - 95)) | (1 << (OParser.SORTED - 95)) | (1 << (OParser.THIS - 95)) | (1 << (OParser.BOOLEAN_LITERAL - 95)) | (1 << (OParser.CHAR_LITERAL - 95)) | (1 << (OParser.MIN_INTEGER - 95)) | (1 << (OParser.MAX_INTEGER - 95)) | (1 << (OParser.SYMBOL_IDENTIFIER - 95)))) != 0) or ((((_la - 159)) & ~0x3f) == 0 and ((1 << (_la - 159)) & ((1 << (OParser.TYPE_IDENTIFIER - 159)) | (1 << (OParser.VARIABLE_IDENTIFIER - 159)) | (1 << (OParser.TEXT_LITERAL - 159)) | (1 << (OParser.UUID_LITERAL - 159)) | (1 << (OParser.INTEGER_LITERAL - 159)) | (1 << (OParser.HEXA_LITERAL - 159)) | (1 << (OParser.DECIMAL_LITERAL - 159)) | (1 << (OParser.DATETIME_LITERAL - 159)) | (1 << (OParser.TIME_LITERAL - 159)) | (1 << (OParser.DATE_LITERAL - 159)) | (1 << (OParser.PERIOD_LITERAL - 159)) | (1 << (OParser.VERSION_LITERAL - 159)))) != 0):
                self.state = 934
                localctx.exp = self.expression(0)


            self.state = 937
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
            self.state = 939
            localctx.method = self.method_selector()
            self.state = 940
            self.match(OParser.LPAR)
            self.state = 942
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (OParser.EXECUTE - 95)) | (1 << (OParser.FETCH - 95)) | (1 << (OParser.FILTERED - 95)) | (1 << (OParser.MUTABLE - 95)) | (1 << (OParser.NULL - 95)) | (1 << (OParser.READ - 95)) | (1 << (OParser.SELF - 95)) | (1 << (OParser.SORTED - 95)) | (1 << (OParser.THIS - 95)) | (1 << (OParser.BOOLEAN_LITERAL - 95)) | (1 << (OParser.CHAR_LITERAL - 95)) | (1 << (OParser.MIN_INTEGER - 95)) | (1 << (OParser.MAX_INTEGER - 95)) | (1 << (OParser.SYMBOL_IDENTIFIER - 95)))) != 0) or ((((_la - 159)) & ~0x3f) == 0 and ((1 << (_la - 159)) & ((1 << (OParser.TYPE_IDENTIFIER - 159)) | (1 << (OParser.VARIABLE_IDENTIFIER - 159)) | (1 << (OParser.TEXT_LITERAL - 159)) | (1 << (OParser.UUID_LITERAL - 159)) | (1 << (OParser.INTEGER_LITERAL - 159)) | (1 << (OParser.HEXA_LITERAL - 159)) | (1 << (OParser.DECIMAL_LITERAL - 159)) | (1 << (OParser.DATETIME_LITERAL - 159)) | (1 << (OParser.TIME_LITERAL - 159)) | (1 << (OParser.DATE_LITERAL - 159)) | (1 << (OParser.PERIOD_LITERAL - 159)) | (1 << (OParser.VERSION_LITERAL - 159)))) != 0):
                self.state = 941
                localctx.args = self.argument_assignment_list(0)


            self.state = 944
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
            self.state = 951
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                localctx = OParser.MethodNameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 946
                localctx.name = self.method_identifier()
                pass

            elif la_ == 2:
                localctx = OParser.MethodParentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 947
                localctx.parent = self.callable_parent(0)
                self.state = 948
                self.match(OParser.DOT)
                self.state = 949
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

            self.state = 954
            localctx.name = self.identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 960
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.CallableSelectorContext(self, OParser.Callable_parentContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_callable_parent)
                    self.state = 956
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 957
                    localctx.select = self.callable_selector() 
                self.state = 962
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

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
            self.state = 969
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.CallableMemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 963
                self.match(OParser.DOT)
                self.state = 964
                localctx.name = self.variable_identifier()
                pass
            elif token in [OParser.LBRAK]:
                localctx = OParser.CallableItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 965
                self.match(OParser.LBRAK)
                self.state = 966
                localctx.exp = self.expression(0)
                self.state = 967
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
            self.state = 994
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                localctx = OParser.InstanceExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 972
                localctx.exp = self.instance_expression(0)
                pass

            elif la_ == 2:
                localctx = OParser.MethodExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 973
                localctx.exp = self.method_expression()
                pass

            elif la_ == 3:
                localctx = OParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 974
                self.match(OParser.MINUS)
                self.state = 975
                localctx.exp = self.expression(36)
                pass

            elif la_ == 4:
                localctx = OParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 976
                self.match(OParser.XMARK)
                self.state = 977
                localctx.exp = self.expression(35)
                pass

            elif la_ == 5:
                localctx = OParser.CastExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 978
                self.match(OParser.LPAR)
                self.state = 979
                localctx.right = self.category_or_any_type()
                self.state = 980
                self.match(OParser.RPAR)
                self.state = 981
                localctx.left = self.expression(29)
                pass

            elif la_ == 6:
                localctx = OParser.CodeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 983
                self.match(OParser.CODE)
                self.state = 984
                self.match(OParser.LPAR)
                self.state = 985
                localctx.exp = self.expression(0)
                self.state = 986
                self.match(OParser.RPAR)
                pass

            elif la_ == 7:
                localctx = OParser.ExecuteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 988
                self.match(OParser.EXECUTE)
                self.state = 989
                self.match(OParser.LPAR)
                self.state = 990
                localctx.name = self.variable_identifier()
                self.state = 991
                self.match(OParser.RPAR)
                pass

            elif la_ == 8:
                localctx = OParser.ClosureExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 993
                localctx.exp = self.closure_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1112
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,68,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1110
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
                    if la_ == 1:
                        localctx = OParser.MultiplyExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 996
                        if not self.precpred(self._ctx, 34):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 34)")
                        self.state = 997
                        self.multiply()
                        self.state = 998
                        localctx.right = self.expression(35)
                        pass

                    elif la_ == 2:
                        localctx = OParser.DivideExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1000
                        if not self.precpred(self._ctx, 33):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 33)")
                        self.state = 1001
                        self.divide()
                        self.state = 1002
                        localctx.right = self.expression(34)
                        pass

                    elif la_ == 3:
                        localctx = OParser.ModuloExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1004
                        if not self.precpred(self._ctx, 32):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 32)")
                        self.state = 1005
                        self.modulo()
                        self.state = 1006
                        localctx.right = self.expression(33)
                        pass

                    elif la_ == 4:
                        localctx = OParser.IntDivideExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1008
                        if not self.precpred(self._ctx, 31):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 31)")
                        self.state = 1009
                        self.idivide()
                        self.state = 1010
                        localctx.right = self.expression(32)
                        pass

                    elif la_ == 5:
                        localctx = OParser.AddExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1012
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 1013
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==OParser.PLUS or _la==OParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 1014
                        localctx.right = self.expression(31)
                        pass

                    elif la_ == 6:
                        localctx = OParser.LessThanExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1015
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 1016
                        self.match(OParser.LT)
                        self.state = 1017
                        localctx.right = self.expression(29)
                        pass

                    elif la_ == 7:
                        localctx = OParser.LessThanOrEqualExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1018
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 1019
                        self.match(OParser.LTE)
                        self.state = 1020
                        localctx.right = self.expression(28)
                        pass

                    elif la_ == 8:
                        localctx = OParser.GreaterThanExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1021
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 1022
                        self.match(OParser.GT)
                        self.state = 1023
                        localctx.right = self.expression(27)
                        pass

                    elif la_ == 9:
                        localctx = OParser.GreaterThanOrEqualExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1024
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 1025
                        self.match(OParser.GTE)
                        self.state = 1026
                        localctx.right = self.expression(26)
                        pass

                    elif la_ == 10:
                        localctx = OParser.IsNotExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1027
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 1028
                        self.match(OParser.IS)
                        self.state = 1029
                        self.match(OParser.NOT)
                        self.state = 1030
                        localctx.right = self.expression(23)
                        pass

                    elif la_ == 11:
                        localctx = OParser.IsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1031
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 1032
                        self.match(OParser.IS)
                        self.state = 1033
                        localctx.right = self.expression(22)
                        pass

                    elif la_ == 12:
                        localctx = OParser.EqualsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1034
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 1035
                        self.match(OParser.EQ2)
                        self.state = 1036
                        localctx.right = self.expression(21)
                        pass

                    elif la_ == 13:
                        localctx = OParser.NotEqualsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1037
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 1038
                        self.match(OParser.XEQ)
                        self.state = 1039
                        localctx.right = self.expression(20)
                        pass

                    elif la_ == 14:
                        localctx = OParser.RoughlyEqualsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1040
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 1041
                        self.match(OParser.TEQ)
                        self.state = 1042
                        localctx.right = self.expression(19)
                        pass

                    elif la_ == 15:
                        localctx = OParser.ContainsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1043
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 1044
                        self.match(OParser.CONTAINS)
                        self.state = 1045
                        localctx.right = self.expression(18)
                        pass

                    elif la_ == 16:
                        localctx = OParser.InExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1046
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 1047
                        self.match(OParser.IN)
                        self.state = 1048
                        localctx.right = self.expression(17)
                        pass

                    elif la_ == 17:
                        localctx = OParser.HasExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1049
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 1050
                        self.match(OParser.HAS)
                        self.state = 1051
                        localctx.right = self.expression(16)
                        pass

                    elif la_ == 18:
                        localctx = OParser.HasAllExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1052
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 1053
                        self.match(OParser.HAS)
                        self.state = 1054
                        self.match(OParser.ALL)
                        self.state = 1055
                        localctx.right = self.expression(15)
                        pass

                    elif la_ == 19:
                        localctx = OParser.HasAnyExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1056
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 1057
                        self.match(OParser.HAS)
                        self.state = 1058
                        self.match(OParser.ANY)
                        self.state = 1059
                        localctx.right = self.expression(14)
                        pass

                    elif la_ == 20:
                        localctx = OParser.NotContainsExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1060
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 1061
                        self.match(OParser.NOT)
                        self.state = 1062
                        self.match(OParser.CONTAINS)
                        self.state = 1063
                        localctx.right = self.expression(13)
                        pass

                    elif la_ == 21:
                        localctx = OParser.NotInExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1064
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 1065
                        self.match(OParser.NOT)
                        self.state = 1066
                        self.match(OParser.IN)
                        self.state = 1067
                        localctx.right = self.expression(12)
                        pass

                    elif la_ == 22:
                        localctx = OParser.NotHasExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1068
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 1069
                        self.match(OParser.NOT)
                        self.state = 1070
                        self.match(OParser.HAS)
                        self.state = 1071
                        localctx.right = self.expression(11)
                        pass

                    elif la_ == 23:
                        localctx = OParser.NotHasAllExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1072
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 1073
                        self.match(OParser.NOT)
                        self.state = 1074
                        self.match(OParser.HAS)
                        self.state = 1075
                        self.match(OParser.ALL)
                        self.state = 1076
                        localctx.right = self.expression(10)
                        pass

                    elif la_ == 24:
                        localctx = OParser.NotHasAnyExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1077
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 1078
                        self.match(OParser.NOT)
                        self.state = 1079
                        self.match(OParser.HAS)
                        self.state = 1080
                        self.match(OParser.ANY)
                        self.state = 1081
                        localctx.right = self.expression(9)
                        pass

                    elif la_ == 25:
                        localctx = OParser.OrExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1082
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 1083
                        self.match(OParser.PIPE2)
                        self.state = 1084
                        localctx.right = self.expression(8)
                        pass

                    elif la_ == 26:
                        localctx = OParser.AndExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1085
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 1086
                        self.match(OParser.AMP2)
                        self.state = 1087
                        localctx.right = self.expression(7)
                        pass

                    elif la_ == 27:
                        localctx = OParser.TernaryExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.test = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1088
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 1089
                        self.match(OParser.QMARK)
                        self.state = 1090
                        localctx.ifTrue = self.expression(0)
                        self.state = 1091
                        self.match(OParser.COLON)
                        self.state = 1092
                        localctx.ifFalse = self.expression(6)
                        pass

                    elif la_ == 28:
                        localctx = OParser.IsNotAnExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1094
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 1095
                        self.match(OParser.IS)
                        self.state = 1096
                        self.match(OParser.NOT)
                        self.state = 1097
                        localctx.right = self.an_expression()
                        pass

                    elif la_ == 29:
                        localctx = OParser.IsAnExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1098
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 1099
                        self.match(OParser.IS)
                        self.state = 1100
                        localctx.right = self.an_expression()
                        pass

                    elif la_ == 30:
                        localctx = OParser.IteratorExpressionContext(self, OParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.exp = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1101
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1102
                        self.match(OParser.FOR)
                        self.state = 1103
                        self.match(OParser.EACH)
                        self.state = 1104
                        self.match(OParser.LPAR)
                        self.state = 1105
                        localctx.name = self.variable_identifier()
                        self.state = 1106
                        self.match(OParser.IN)
                        self.state = 1107
                        localctx.source = self.expression(0)
                        self.state = 1108
                        self.match(OParser.RPAR)
                        pass

             
                self.state = 1114
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,68,self._ctx)

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
            self.state = 1115
            if not self.willBeAOrAn():
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$parser.willBeAOrAn()")
            self.state = 1116
            self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1117
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
            self.state = 1119
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

            self.state = 1122
            localctx.parent = self.selectable_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1128
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,69,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.SelectorExpressionContext(self, OParser.Instance_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_expression)
                    self.state = 1124
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1125
                    localctx.selector = self.selector_expression() 
                self.state = 1130
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,69,self._ctx)

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
            self.state = 1140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1131
                self.blob_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1132
                self.document_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1133
                self.filtered_list_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1134
                self.fetch_store_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1135
                self.read_all_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1136
                self.read_one_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1137
                self.sorted_expression()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1138
                self.method_call()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 1139
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
            self.state = 1142
            self.match(OParser.BLOB)
            self.state = 1143
            self.match(OParser.LPAR)
            self.state = 1144
            self.expression(0)
            self.state = 1145
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
            self.state = 1147
            self.match(OParser.DOCUMENT)
            self.state = 1148
            self.match(OParser.LPAR)
            self.state = 1150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (OParser.EXECUTE - 95)) | (1 << (OParser.FETCH - 95)) | (1 << (OParser.FILTERED - 95)) | (1 << (OParser.MUTABLE - 95)) | (1 << (OParser.NULL - 95)) | (1 << (OParser.READ - 95)) | (1 << (OParser.SELF - 95)) | (1 << (OParser.SORTED - 95)) | (1 << (OParser.THIS - 95)) | (1 << (OParser.BOOLEAN_LITERAL - 95)) | (1 << (OParser.CHAR_LITERAL - 95)) | (1 << (OParser.MIN_INTEGER - 95)) | (1 << (OParser.MAX_INTEGER - 95)) | (1 << (OParser.SYMBOL_IDENTIFIER - 95)))) != 0) or ((((_la - 159)) & ~0x3f) == 0 and ((1 << (_la - 159)) & ((1 << (OParser.TYPE_IDENTIFIER - 159)) | (1 << (OParser.VARIABLE_IDENTIFIER - 159)) | (1 << (OParser.TEXT_LITERAL - 159)) | (1 << (OParser.UUID_LITERAL - 159)) | (1 << (OParser.INTEGER_LITERAL - 159)) | (1 << (OParser.HEXA_LITERAL - 159)) | (1 << (OParser.DECIMAL_LITERAL - 159)) | (1 << (OParser.DATETIME_LITERAL - 159)) | (1 << (OParser.TIME_LITERAL - 159)) | (1 << (OParser.DATE_LITERAL - 159)) | (1 << (OParser.PERIOD_LITERAL - 159)) | (1 << (OParser.VERSION_LITERAL - 159)))) != 0):
                self.state = 1149
                self.expression(0)


            self.state = 1152
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
            self.state = 1154
            self.match(OParser.WRITE)
            self.state = 1155
            self.match(OParser.LPAR)
            self.state = 1156
            localctx.what = self.expression(0)
            self.state = 1157
            self.match(OParser.RPAR)
            self.state = 1158
            self.match(OParser.TO)
            self.state = 1159
            localctx.target = self.expression(0)
            self.state = 1160
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
            self.state = 1162
            self.match(OParser.FILTERED)
            self.state = 1163
            self.match(OParser.LPAR)
            self.state = 1164
            localctx.source = self.expression(0)
            self.state = 1165
            self.match(OParser.RPAR)
            self.state = 1166
            self.match(OParser.WITH)
            self.state = 1167
            self.match(OParser.LPAR)
            self.state = 1168
            localctx.name = self.variable_identifier()
            self.state = 1169
            self.match(OParser.RPAR)
            self.state = 1170
            self.match(OParser.WHERE)
            self.state = 1171
            self.match(OParser.LPAR)
            self.state = 1172
            localctx.predicate = self.expression(0)
            self.state = 1173
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
            self.state = 1226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
            if la_ == 1:
                localctx = OParser.FetchOneContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1175
                self.match(OParser.FETCH)
                self.state = 1176
                self.match(OParser.ONE)
                self.state = 1181
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==OParser.LPAR:
                    self.state = 1177
                    self.match(OParser.LPAR)
                    self.state = 1178
                    localctx.typ = self.mutable_category_type()
                    self.state = 1179
                    self.match(OParser.RPAR)


                self.state = 1183
                self.match(OParser.WHERE)
                self.state = 1184
                self.match(OParser.LPAR)
                self.state = 1185
                localctx.predicate = self.expression(0)
                self.state = 1186
                self.match(OParser.RPAR)
                pass

            elif la_ == 2:
                localctx = OParser.FetchManyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1188
                self.match(OParser.FETCH)
                self.state = 1209
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [OParser.ALL]:
                    self.state = 1189
                    self.match(OParser.ALL)
                    self.state = 1194
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
                    if la_ == 1:
                        self.state = 1190
                        self.match(OParser.LPAR)
                        self.state = 1191
                        localctx.typ = self.mutable_category_type()
                        self.state = 1192
                        self.match(OParser.RPAR)


                    pass
                elif token in [OParser.LPAR, OParser.ROWS]:
                    self.state = 1200
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==OParser.LPAR:
                        self.state = 1196
                        self.match(OParser.LPAR)
                        self.state = 1197
                        localctx.typ = self.mutable_category_type()
                        self.state = 1198
                        self.match(OParser.RPAR)


                    self.state = 1202
                    self.match(OParser.ROWS)
                    self.state = 1203
                    self.match(OParser.LPAR)
                    self.state = 1204
                    localctx.xstart = self.expression(0)
                    self.state = 1205
                    self.match(OParser.TO)
                    self.state = 1206
                    localctx.xstop = self.expression(0)
                    self.state = 1207
                    self.match(OParser.RPAR)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1216
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
                if la_ == 1:
                    self.state = 1211
                    self.match(OParser.WHERE)
                    self.state = 1212
                    self.match(OParser.LPAR)
                    self.state = 1213
                    localctx.predicate = self.expression(0)
                    self.state = 1214
                    self.match(OParser.RPAR)


                self.state = 1224
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
                if la_ == 1:
                    self.state = 1218
                    self.match(OParser.ORDER)
                    self.state = 1219
                    self.match(OParser.BY)
                    self.state = 1220
                    self.match(OParser.LPAR)
                    self.state = 1221
                    localctx.orderby = self.order_by_list()
                    self.state = 1222
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
            self.state = 1228
            self.match(OParser.SORTED)
            self.state = 1230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.DESC:
                self.state = 1229
                self.match(OParser.DESC)


            self.state = 1232
            self.match(OParser.LPAR)
            self.state = 1233
            localctx.source = self.instance_expression(0)
            self.state = 1239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.COMMA:
                self.state = 1234
                self.match(OParser.COMMA)
                self.state = 1235
                self.key_token()
                self.state = 1236
                self.match(OParser.EQ)
                self.state = 1237
                localctx.key = self.instance_expression(0)


            self.state = 1241
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
            self.state = 1253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,81,self._ctx)
            if la_ == 1:
                localctx = OParser.MemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1243
                self.match(OParser.DOT)
                self.state = 1244
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = OParser.ItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1245
                self.match(OParser.LBRAK)
                self.state = 1246
                localctx.exp = self.expression(0)
                self.state = 1247
                self.match(OParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = OParser.SliceSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1249
                self.match(OParser.LBRAK)
                self.state = 1250
                localctx.xslice = self.slice_arguments()
                self.state = 1251
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
            self.typ = None # Mutable_category_typeContext
            self.args = None # Argument_assignment_listContext

        def LPAR(self):
            return self.getToken(OParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(OParser.RPAR, 0)

        def mutable_category_type(self):
            return self.getTypedRuleContext(OParser.Mutable_category_typeContext,0)


        def argument_assignment_list(self):
            return self.getTypedRuleContext(OParser.Argument_assignment_listContext,0)


        def getRuleIndex(self):
            return OParser.RULE_constructor_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterConstructor_expression"):
                listener.enterConstructor_expression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConstructor_expression"):
                listener.exitConstructor_expression(self)




    def constructor_expression(self):

        localctx = OParser.Constructor_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_constructor_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1255
            localctx.typ = self.mutable_category_type()
            self.state = 1256
            self.match(OParser.LPAR)
            self.state = 1258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (OParser.EXECUTE - 95)) | (1 << (OParser.FETCH - 95)) | (1 << (OParser.FILTERED - 95)) | (1 << (OParser.MUTABLE - 95)) | (1 << (OParser.NULL - 95)) | (1 << (OParser.READ - 95)) | (1 << (OParser.SELF - 95)) | (1 << (OParser.SORTED - 95)) | (1 << (OParser.THIS - 95)) | (1 << (OParser.BOOLEAN_LITERAL - 95)) | (1 << (OParser.CHAR_LITERAL - 95)) | (1 << (OParser.MIN_INTEGER - 95)) | (1 << (OParser.MAX_INTEGER - 95)) | (1 << (OParser.SYMBOL_IDENTIFIER - 95)))) != 0) or ((((_la - 159)) & ~0x3f) == 0 and ((1 << (_la - 159)) & ((1 << (OParser.TYPE_IDENTIFIER - 159)) | (1 << (OParser.VARIABLE_IDENTIFIER - 159)) | (1 << (OParser.TEXT_LITERAL - 159)) | (1 << (OParser.UUID_LITERAL - 159)) | (1 << (OParser.INTEGER_LITERAL - 159)) | (1 << (OParser.HEXA_LITERAL - 159)) | (1 << (OParser.DECIMAL_LITERAL - 159)) | (1 << (OParser.DATETIME_LITERAL - 159)) | (1 << (OParser.TIME_LITERAL - 159)) | (1 << (OParser.DATE_LITERAL - 159)) | (1 << (OParser.PERIOD_LITERAL - 159)) | (1 << (OParser.VERSION_LITERAL - 159)))) != 0):
                self.state = 1257
                localctx.args = self.argument_assignment_list(0)


            self.state = 1260
            self.match(OParser.RPAR)
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
        _startState = 118
        self.enterRecursionRule(localctx, 118, self.RULE_argument_assignment_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,83,self._ctx)
            if la_ == 1:
                localctx = OParser.ExpressionAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1263
                localctx.exp = self.expression(0)
                self.state = 1264
                if not self.willNotBe(self.equalToken()):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willNotBe($parser.equalToken())")
                pass

            elif la_ == 2:
                localctx = OParser.ArgumentAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1266
                localctx.item = self.argument_assignment()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1274
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,84,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.ArgumentAssignmentListItemContext(self, OParser.Argument_assignment_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_assignment_list)
                    self.state = 1269
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1270
                    self.match(OParser.COMMA)
                    self.state = 1271
                    localctx.item = self.argument_assignment() 
                self.state = 1276
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,84,self._ctx)

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

        def assign(self):
            return self.getTypedRuleContext(OParser.AssignContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(OParser.Variable_identifierContext,0)


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
        self.enterRule(localctx, 120, self.RULE_argument_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1277
            localctx.name = self.variable_identifier()
            self.state = 1278
            self.assign()
            self.state = 1279
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
        self.enterRule(localctx, 122, self.RULE_assign_instance_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1281
            localctx.inst = self.assignable_instance(0)
            self.state = 1282
            self.assign()
            self.state = 1283
            localctx.exp = self.expression(0)
            self.state = 1284
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
        self.enterRule(localctx, 124, self.RULE_child_instance)
        try:
            self.state = 1292
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.MemberInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1286
                self.match(OParser.DOT)
                self.state = 1287
                localctx.name = self.variable_identifier()
                pass
            elif token in [OParser.LBRAK]:
                localctx = OParser.ItemInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1288
                self.match(OParser.LBRAK)
                self.state = 1289
                localctx.exp = self.expression(0)
                self.state = 1290
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
        self.enterRule(localctx, 126, self.RULE_assign_tuple_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1294
            localctx.items = self.variable_identifier_list()
            self.state = 1295
            self.assign()
            self.state = 1296
            localctx.exp = self.expression(0)
            self.state = 1297
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
        self.enterRule(localctx, 128, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1299
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
        self.enterRule(localctx, 130, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            localctx = OParser.FullDeclarationListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 1302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.ABSTRACT - 64)) | (1 << (OParser.ANY - 64)) | (1 << (OParser.ATTRIBUTE - 64)) | (1 << (OParser.CATEGORY - 64)) | (1 << (OParser.ENUMERATED - 64)) | (1 << (OParser.METHOD - 64)) | (1 << (OParser.NATIVE - 64)))) != 0) or ((((_la - 138)) & ~0x3f) == 0 and ((1 << (_la - 138)) & ((1 << (OParser.SINGLETON - 138)) | (1 << (OParser.STORABLE - 138)) | (1 << (OParser.TEST - 138)) | (1 << (OParser.TYPE_IDENTIFIER - 138)))) != 0):
                self.state = 1301
                self.declarations()


            self.state = 1304
            self.lfs()
            self.state = 1305
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
        self.enterRule(localctx, 132, self.RULE_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1307
            self.declaration()
            self.state = 1313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (OParser.ABSTRACT - 64)) | (1 << (OParser.ANY - 64)) | (1 << (OParser.ATTRIBUTE - 64)) | (1 << (OParser.CATEGORY - 64)) | (1 << (OParser.ENUMERATED - 64)) | (1 << (OParser.METHOD - 64)) | (1 << (OParser.NATIVE - 64)))) != 0) or ((((_la - 138)) & ~0x3f) == 0 and ((1 << (_la - 138)) & ((1 << (OParser.SINGLETON - 138)) | (1 << (OParser.STORABLE - 138)) | (1 << (OParser.TEST - 138)) | (1 << (OParser.TYPE_IDENTIFIER - 138)))) != 0):
                self.state = 1308
                self.lfp()
                self.state = 1309
                self.declaration()
                self.state = 1315
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
        self.enterRule(localctx, 134, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMENT:
                self.state = 1316
                self.comment_statement()
                self.state = 1317
                self.lfp()
                self.state = 1323
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
            if la_ == 1:
                self.state = 1324
                self.attribute_declaration()
                pass

            elif la_ == 2:
                self.state = 1325
                self.category_declaration()
                pass

            elif la_ == 3:
                self.state = 1326
                self.resource_declaration()
                pass

            elif la_ == 4:
                self.state = 1327
                self.enum_declaration()
                pass

            elif la_ == 5:
                self.state = 1328
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
        self.enterRule(localctx, 136, self.RULE_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1331
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
        self.enterRule(localctx, 138, self.RULE_enum_declaration)
        try:
            self.state = 1335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,90,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1333
                self.enum_category_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1334
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
        self.enterRule(localctx, 140, self.RULE_native_symbol_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1337
            self.native_symbol()
            self.state = 1343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.SYMBOL_IDENTIFIER:
                self.state = 1338
                self.lfp()
                self.state = 1339
                self.native_symbol()
                self.state = 1345
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
        self.enterRule(localctx, 142, self.RULE_category_symbol_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1346
            self.category_symbol()
            self.state = 1352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.SYMBOL_IDENTIFIER:
                self.state = 1347
                self.lfp()
                self.state = 1348
                self.category_symbol()
                self.state = 1354
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
        self.enterRule(localctx, 144, self.RULE_symbol_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1355
            self.symbol_identifier()
            self.state = 1360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1356
                self.match(OParser.COMMA)
                self.state = 1357
                self.symbol_identifier()
                self.state = 1362
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
        self.enterRule(localctx, 146, self.RULE_attribute_constraint)
        try:
            self.state = 1373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,94,self._ctx)
            if la_ == 1:
                localctx = OParser.MatchingListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1363
                self.match(OParser.IN)
                self.state = 1364
                localctx.source = self.list_literal()
                pass

            elif la_ == 2:
                localctx = OParser.MatchingSetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1365
                self.match(OParser.IN)
                self.state = 1366
                localctx.source = self.set_literal()
                pass

            elif la_ == 3:
                localctx = OParser.MatchingRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1367
                self.match(OParser.IN)
                self.state = 1368
                localctx.source = self.range_literal()
                pass

            elif la_ == 4:
                localctx = OParser.MatchingPatternContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1369
                self.match(OParser.MATCHING)
                self.state = 1370
                localctx.text = self.match(OParser.TEXT_LITERAL)
                pass

            elif la_ == 5:
                localctx = OParser.MatchingExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1371
                self.match(OParser.MATCHING)
                self.state = 1372
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
        self.enterRule(localctx, 148, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1376
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.MUTABLE:
                self.state = 1375
                self.match(OParser.MUTABLE)


            self.state = 1378
            self.match(OParser.LBRAK)
            self.state = 1380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (OParser.EXECUTE - 95)) | (1 << (OParser.FETCH - 95)) | (1 << (OParser.FILTERED - 95)) | (1 << (OParser.MUTABLE - 95)) | (1 << (OParser.NULL - 95)) | (1 << (OParser.READ - 95)) | (1 << (OParser.SELF - 95)) | (1 << (OParser.SORTED - 95)) | (1 << (OParser.THIS - 95)) | (1 << (OParser.BOOLEAN_LITERAL - 95)) | (1 << (OParser.CHAR_LITERAL - 95)) | (1 << (OParser.MIN_INTEGER - 95)) | (1 << (OParser.MAX_INTEGER - 95)) | (1 << (OParser.SYMBOL_IDENTIFIER - 95)))) != 0) or ((((_la - 159)) & ~0x3f) == 0 and ((1 << (_la - 159)) & ((1 << (OParser.TYPE_IDENTIFIER - 159)) | (1 << (OParser.VARIABLE_IDENTIFIER - 159)) | (1 << (OParser.TEXT_LITERAL - 159)) | (1 << (OParser.UUID_LITERAL - 159)) | (1 << (OParser.INTEGER_LITERAL - 159)) | (1 << (OParser.HEXA_LITERAL - 159)) | (1 << (OParser.DECIMAL_LITERAL - 159)) | (1 << (OParser.DATETIME_LITERAL - 159)) | (1 << (OParser.TIME_LITERAL - 159)) | (1 << (OParser.DATE_LITERAL - 159)) | (1 << (OParser.PERIOD_LITERAL - 159)) | (1 << (OParser.VERSION_LITERAL - 159)))) != 0):
                self.state = 1379
                self.expression_list()


            self.state = 1382
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
        self.enterRule(localctx, 150, self.RULE_set_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1385
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.MUTABLE:
                self.state = 1384
                self.match(OParser.MUTABLE)


            self.state = 1387
            self.match(OParser.LT)
            self.state = 1389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (OParser.EXECUTE - 95)) | (1 << (OParser.FETCH - 95)) | (1 << (OParser.FILTERED - 95)) | (1 << (OParser.MUTABLE - 95)) | (1 << (OParser.NULL - 95)) | (1 << (OParser.READ - 95)) | (1 << (OParser.SELF - 95)) | (1 << (OParser.SORTED - 95)) | (1 << (OParser.THIS - 95)) | (1 << (OParser.BOOLEAN_LITERAL - 95)) | (1 << (OParser.CHAR_LITERAL - 95)) | (1 << (OParser.MIN_INTEGER - 95)) | (1 << (OParser.MAX_INTEGER - 95)) | (1 << (OParser.SYMBOL_IDENTIFIER - 95)))) != 0) or ((((_la - 159)) & ~0x3f) == 0 and ((1 << (_la - 159)) & ((1 << (OParser.TYPE_IDENTIFIER - 159)) | (1 << (OParser.VARIABLE_IDENTIFIER - 159)) | (1 << (OParser.TEXT_LITERAL - 159)) | (1 << (OParser.UUID_LITERAL - 159)) | (1 << (OParser.INTEGER_LITERAL - 159)) | (1 << (OParser.HEXA_LITERAL - 159)) | (1 << (OParser.DECIMAL_LITERAL - 159)) | (1 << (OParser.DATETIME_LITERAL - 159)) | (1 << (OParser.TIME_LITERAL - 159)) | (1 << (OParser.DATE_LITERAL - 159)) | (1 << (OParser.PERIOD_LITERAL - 159)) | (1 << (OParser.VERSION_LITERAL - 159)))) != 0):
                self.state = 1388
                self.expression_list()


            self.state = 1391
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
        self.enterRule(localctx, 152, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1393
            self.expression(0)
            self.state = 1398
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1394
                self.match(OParser.COMMA)
                self.state = 1395
                self.expression(0)
                self.state = 1400
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
        self.enterRule(localctx, 154, self.RULE_range_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1401
            self.match(OParser.LBRAK)
            self.state = 1402
            localctx.low = self.expression(0)
            self.state = 1403
            self.match(OParser.RANGE)
            self.state = 1404
            localctx.high = self.expression(0)
            self.state = 1405
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
        _startState = 156
        self.enterRecursionRule(localctx, 156, self.RULE_typedef, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1419
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID, OParser.TYPE_IDENTIFIER]:
                localctx = OParser.PrimaryTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1408
                localctx.p = self.primary_type()
                pass
            elif token in [OParser.CURSOR]:
                localctx = OParser.CursorTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1409
                self.match(OParser.CURSOR)
                self.state = 1410
                self.match(OParser.LT)
                self.state = 1411
                localctx.c = self.typedef(0)
                self.state = 1412
                self.match(OParser.GT)
                pass
            elif token in [OParser.ITERATOR]:
                localctx = OParser.IteratorTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1414
                self.match(OParser.ITERATOR)
                self.state = 1415
                self.match(OParser.LT)
                self.state = 1416
                localctx.i = self.typedef(0)
                self.state = 1417
                self.match(OParser.GT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 1431
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,102,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1429
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,101,self._ctx)
                    if la_ == 1:
                        localctx = OParser.SetTypeContext(self, OParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.s = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1421
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 1422
                        self.match(OParser.LTGT)
                        pass

                    elif la_ == 2:
                        localctx = OParser.ListTypeContext(self, OParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1423
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 1424
                        self.match(OParser.LBRAK)
                        self.state = 1425
                        self.match(OParser.RBRAK)
                        pass

                    elif la_ == 3:
                        localctx = OParser.DictTypeContext(self, OParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.d = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1426
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1427
                        self.match(OParser.LCURL)
                        self.state = 1428
                        self.match(OParser.RCURL)
                        pass

             
                self.state = 1433
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,102,self._ctx)

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
        self.enterRule(localctx, 158, self.RULE_primary_type)
        try:
            self.state = 1436
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID]:
                localctx = OParser.NativeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1434
                localctx.n = self.native_type()
                pass
            elif token in [OParser.TYPE_IDENTIFIER]:
                localctx = OParser.CategoryTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1435
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
        self.enterRule(localctx, 160, self.RULE_native_type)
        try:
            self.state = 1453
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.BOOLEAN]:
                localctx = OParser.BooleanTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1438
                self.match(OParser.BOOLEAN)
                pass
            elif token in [OParser.CHARACTER]:
                localctx = OParser.CharacterTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1439
                self.match(OParser.CHARACTER)
                pass
            elif token in [OParser.TEXT]:
                localctx = OParser.TextTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1440
                self.match(OParser.TEXT)
                pass
            elif token in [OParser.IMAGE]:
                localctx = OParser.ImageTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1441
                self.match(OParser.IMAGE)
                pass
            elif token in [OParser.INTEGER]:
                localctx = OParser.IntegerTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1442
                self.match(OParser.INTEGER)
                pass
            elif token in [OParser.DECIMAL]:
                localctx = OParser.DecimalTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1443
                self.match(OParser.DECIMAL)
                pass
            elif token in [OParser.DOCUMENT]:
                localctx = OParser.DocumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1444
                self.match(OParser.DOCUMENT)
                pass
            elif token in [OParser.DATE]:
                localctx = OParser.DateTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1445
                self.match(OParser.DATE)
                pass
            elif token in [OParser.DATETIME]:
                localctx = OParser.DateTimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1446
                self.match(OParser.DATETIME)
                pass
            elif token in [OParser.TIME]:
                localctx = OParser.TimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1447
                self.match(OParser.TIME)
                pass
            elif token in [OParser.PERIOD]:
                localctx = OParser.PeriodTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1448
                self.match(OParser.PERIOD)
                pass
            elif token in [OParser.VERSION]:
                localctx = OParser.VersionTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1449
                self.match(OParser.VERSION)
                pass
            elif token in [OParser.CODE]:
                localctx = OParser.CodeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1450
                self.match(OParser.CODE)
                pass
            elif token in [OParser.BLOB]:
                localctx = OParser.BlobTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1451
                self.match(OParser.BLOB)
                pass
            elif token in [OParser.UUID]:
                localctx = OParser.UUIDTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 1452
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
        self.enterRule(localctx, 162, self.RULE_category_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1455
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
        self.enterRule(localctx, 164, self.RULE_mutable_category_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1458
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.MUTABLE:
                self.state = 1457
                self.match(OParser.MUTABLE)


            self.state = 1460
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
        self.enterRule(localctx, 166, self.RULE_code_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1462
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
        self.enterRule(localctx, 168, self.RULE_category_declaration)
        try:
            self.state = 1467
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,106,self._ctx)
            if la_ == 1:
                localctx = OParser.ConcreteCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1464
                localctx.decl = self.concrete_category_declaration()
                pass

            elif la_ == 2:
                localctx = OParser.NativeCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1465
                localctx.decl = self.native_category_declaration()
                pass

            elif la_ == 3:
                localctx = OParser.SingletonCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1466
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
        self.enterRule(localctx, 170, self.RULE_type_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1469
            self.type_identifier()
            self.state = 1474
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1470
                self.match(OParser.COMMA)
                self.state = 1471
                self.type_identifier()
                self.state = 1476
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
        self.enterRule(localctx, 172, self.RULE_method_identifier)
        try:
            self.state = 1479
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.VARIABLE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1477
                self.variable_identifier()
                pass
            elif token in [OParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1478
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
        self.enterRule(localctx, 174, self.RULE_identifier)
        try:
            self.state = 1484
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.VARIABLE_IDENTIFIER]:
                localctx = OParser.VariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1481
                self.variable_identifier()
                pass
            elif token in [OParser.TYPE_IDENTIFIER]:
                localctx = OParser.TypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1482
                self.type_identifier()
                pass
            elif token in [OParser.SYMBOL_IDENTIFIER]:
                localctx = OParser.SymbolIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1483
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
        self.enterRule(localctx, 176, self.RULE_variable_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1486
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
        self.enterRule(localctx, 178, self.RULE_attribute_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1488
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
        self.enterRule(localctx, 180, self.RULE_type_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1490
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
        self.enterRule(localctx, 182, self.RULE_symbol_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1492
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
        self.enterRule(localctx, 184, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1494
            self.argument()
            self.state = 1499
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1495
                self.match(OParser.COMMA)
                self.state = 1496
                self.argument()
                self.state = 1501
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
        self.enterRule(localctx, 186, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.state = 1507
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,112,self._ctx)
            if la_ == 1:
                localctx = OParser.CodeArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1502
                localctx.arg = self.code_argument()
                pass

            elif la_ == 2:
                localctx = OParser.OperatorArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1504
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==OParser.MUTABLE:
                    self.state = 1503
                    self.match(OParser.MUTABLE)


                self.state = 1506
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
        self.enterRule(localctx, 188, self.RULE_operator_argument)
        try:
            self.state = 1511
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.VARIABLE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1509
                self.named_argument()
                pass
            elif token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID, OParser.ITERATOR, OParser.CURSOR, OParser.ANY, OParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1510
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
        self.enterRule(localctx, 190, self.RULE_named_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1513
            self.variable_identifier()
            self.state = 1516
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.EQ:
                self.state = 1514
                self.match(OParser.EQ)
                self.state = 1515
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
        self.enterRule(localctx, 192, self.RULE_code_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1518
            self.code_type()
            self.state = 1519
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
        self.enterRule(localctx, 194, self.RULE_category_or_any_type)
        try:
            self.state = 1523
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.CODE, OParser.DOCUMENT, OParser.BLOB, OParser.IMAGE, OParser.UUID, OParser.ITERATOR, OParser.CURSOR, OParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1521
                self.typedef(0)
                pass
            elif token in [OParser.ANY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1522
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
        _startState = 196
        self.enterRecursionRule(localctx, 196, self.RULE_any_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.AnyTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1526
            self.match(OParser.ANY)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1536
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,117,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1534
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,116,self._ctx)
                    if la_ == 1:
                        localctx = OParser.AnyListTypeContext(self, OParser.Any_typeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1528
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1529
                        self.match(OParser.LBRAK)
                        self.state = 1530
                        self.match(OParser.RBRAK)
                        pass

                    elif la_ == 2:
                        localctx = OParser.AnyDictTypeContext(self, OParser.Any_typeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1531
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1532
                        self.match(OParser.LCURL)
                        self.state = 1533
                        self.match(OParser.RCURL)
                        pass

             
                self.state = 1538
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,117,self._ctx)

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
        self.enterRule(localctx, 198, self.RULE_member_method_declaration_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1539
            self.member_method_declaration()
            self.state = 1545
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ABSTRACT - 46)) | (1 << (OParser.GETTER - 46)))) != 0) or ((((_la - 112)) & ~0x3f) == 0 and ((1 << (_la - 112)) & ((1 << (OParser.METHOD - 112)) | (1 << (OParser.OPERATOR - 112)) | (1 << (OParser.SETTER - 112)) | (1 << (OParser.TYPE_IDENTIFIER - 112)))) != 0):
                self.state = 1540
                self.lfp()
                self.state = 1541
                self.member_method_declaration()
                self.state = 1547
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
        self.enterRule(localctx, 200, self.RULE_member_method_declaration)
        try:
            self.state = 1553
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,119,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1548
                self.setter_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1549
                self.getter_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1550
                self.concrete_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1551
                self.abstract_method_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1552
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
        self.enterRule(localctx, 202, self.RULE_native_member_method_declaration_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1555
            self.native_member_method_declaration()
            self.state = 1561
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (OParser.BOOLEAN - 46)) | (1 << (OParser.CHARACTER - 46)) | (1 << (OParser.TEXT - 46)) | (1 << (OParser.INTEGER - 46)) | (1 << (OParser.DECIMAL - 46)) | (1 << (OParser.DATE - 46)) | (1 << (OParser.TIME - 46)) | (1 << (OParser.DATETIME - 46)) | (1 << (OParser.PERIOD - 46)) | (1 << (OParser.VERSION - 46)) | (1 << (OParser.CODE - 46)) | (1 << (OParser.DOCUMENT - 46)) | (1 << (OParser.BLOB - 46)) | (1 << (OParser.IMAGE - 46)) | (1 << (OParser.UUID - 46)) | (1 << (OParser.ITERATOR - 46)) | (1 << (OParser.CURSOR - 46)) | (1 << (OParser.ANY - 46)) | (1 << (OParser.GETTER - 46)))) != 0) or ((((_la - 112)) & ~0x3f) == 0 and ((1 << (_la - 112)) & ((1 << (OParser.METHOD - 112)) | (1 << (OParser.NATIVE - 112)) | (1 << (OParser.SETTER - 112)) | (1 << (OParser.TYPE_IDENTIFIER - 112)))) != 0):
                self.state = 1556
                self.lfp()
                self.state = 1557
                self.native_member_method_declaration()
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
        self.enterRule(localctx, 204, self.RULE_native_member_method_declaration)
        try:
            self.state = 1567
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,121,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1564
                self.native_getter_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1565
                self.native_setter_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1566
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
        self.enterRule(localctx, 206, self.RULE_native_category_binding)
        try:
            self.state = 1579
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.JAVA]:
                localctx = OParser.JavaCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1569
                self.match(OParser.JAVA)
                self.state = 1570
                localctx.binding = self.java_class_identifier_expression(0)
                pass
            elif token in [OParser.CSHARP]:
                localctx = OParser.CSharpCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1571
                self.match(OParser.CSHARP)
                self.state = 1572
                localctx.binding = self.csharp_identifier_expression(0)
                pass
            elif token in [OParser.PYTHON2]:
                localctx = OParser.Python2CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1573
                self.match(OParser.PYTHON2)
                self.state = 1574
                localctx.binding = self.python_category_binding()
                pass
            elif token in [OParser.PYTHON3]:
                localctx = OParser.Python3CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1575
                self.match(OParser.PYTHON3)
                self.state = 1576
                localctx.binding = self.python_category_binding()
                pass
            elif token in [OParser.JAVASCRIPT]:
                localctx = OParser.JavaScriptCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1577
                self.match(OParser.JAVASCRIPT)
                self.state = 1578
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
        self.enterRule(localctx, 208, self.RULE_python_category_binding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1581
            self.identifier()
            self.state = 1583
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.FROM:
                self.state = 1582
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
        self.enterRule(localctx, 210, self.RULE_python_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1585
            self.match(OParser.FROM)
            self.state = 1586
            self.module_token()
            self.state = 1587
            self.match(OParser.COLON)
            self.state = 1588
            self.identifier()
            self.state = 1593
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.DOT:
                self.state = 1589
                self.match(OParser.DOT)
                self.state = 1590
                self.identifier()
                self.state = 1595
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
        self.enterRule(localctx, 212, self.RULE_javascript_category_binding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1596
            self.identifier()
            self.state = 1598
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.FROM:
                self.state = 1597
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
        self.enterRule(localctx, 214, self.RULE_javascript_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1600
            self.match(OParser.FROM)
            self.state = 1601
            self.module_token()
            self.state = 1602
            self.match(OParser.COLON)
            self.state = 1604
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.SLASH:
                self.state = 1603
                self.match(OParser.SLASH)


            self.state = 1606
            self.javascript_identifier()
            self.state = 1611
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.SLASH:
                self.state = 1607
                self.match(OParser.SLASH)
                self.state = 1608
                self.javascript_identifier()
                self.state = 1613
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1616
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.DOT:
                self.state = 1614
                self.match(OParser.DOT)
                self.state = 1615
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
        self.enterRule(localctx, 216, self.RULE_variable_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1618
            self.variable_identifier()
            self.state = 1623
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1619
                self.match(OParser.COMMA)
                self.state = 1620
                self.variable_identifier()
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
        self.enterRule(localctx, 218, self.RULE_attribute_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1626
            self.attribute_identifier()
            self.state = 1631
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1627
                self.match(OParser.COMMA)
                self.state = 1628
                self.attribute_identifier()
                self.state = 1633
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
        self.enterRule(localctx, 220, self.RULE_method_declaration)
        try:
            self.state = 1638
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,131,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1634
                self.abstract_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1635
                self.concrete_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1636
                self.native_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1637
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
        self.enterRule(localctx, 222, self.RULE_comment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1640
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
        self.enterRule(localctx, 224, self.RULE_native_statement_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1642
            self.native_statement()
            self.state = 1648
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.JAVA) | (1 << OParser.CSHARP) | (1 << OParser.PYTHON2) | (1 << OParser.PYTHON3) | (1 << OParser.JAVASCRIPT))) != 0):
                self.state = 1643
                self.lfp()
                self.state = 1644
                self.native_statement()
                self.state = 1650
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
        self.enterRule(localctx, 226, self.RULE_native_statement)
        try:
            self.state = 1661
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.JAVA]:
                localctx = OParser.JavaNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1651
                self.match(OParser.JAVA)
                self.state = 1652
                self.java_statement()
                pass
            elif token in [OParser.CSHARP]:
                localctx = OParser.CSharpNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1653
                self.match(OParser.CSHARP)
                self.state = 1654
                self.csharp_statement()
                pass
            elif token in [OParser.PYTHON2]:
                localctx = OParser.Python2NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1655
                self.match(OParser.PYTHON2)
                self.state = 1656
                self.python_native_statement()
                pass
            elif token in [OParser.PYTHON3]:
                localctx = OParser.Python3NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1657
                self.match(OParser.PYTHON3)
                self.state = 1658
                self.python_native_statement()
                pass
            elif token in [OParser.JAVASCRIPT]:
                localctx = OParser.JavaScriptNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1659
                self.match(OParser.JAVASCRIPT)
                self.state = 1660
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
        self.enterRule(localctx, 228, self.RULE_python_native_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1663
            self.python_statement()
            self.state = 1665
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.SEMI:
                self.state = 1664
                self.match(OParser.SEMI)


            self.state = 1668
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.FROM:
                self.state = 1667
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
        self.enterRule(localctx, 230, self.RULE_javascript_native_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1670
            self.javascript_statement()
            self.state = 1672
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.SEMI:
                self.state = 1671
                self.match(OParser.SEMI)


            self.state = 1675
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.FROM:
                self.state = 1674
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
        self.enterRule(localctx, 232, self.RULE_statement_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1677
            self.statement()
            self.state = 1683
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.COMMENT) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB) | (1 << OParser.IMAGE) | (1 << OParser.UUID) | (1 << OParser.ITERATOR) | (1 << OParser.CURSOR))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (OParser.BREAK - 75)) | (1 << (OParser.DELETE - 75)) | (1 << (OParser.DO - 75)) | (1 << (OParser.FLUSH - 75)) | (1 << (OParser.FOR - 75)) | (1 << (OParser.IF - 75)) | (1 << (OParser.METHOD - 75)) | (1 << (OParser.RETURN - 75)))) != 0) or ((((_la - 141)) & ~0x3f) == 0 and ((1 << (_la - 141)) & ((1 << (OParser.STORE - 141)) | (1 << (OParser.SWITCH - 141)) | (1 << (OParser.THROW - 141)) | (1 << (OParser.TRY - 141)) | (1 << (OParser.WITH - 141)) | (1 << (OParser.WHILE - 141)) | (1 << (OParser.WRITE - 141)) | (1 << (OParser.SYMBOL_IDENTIFIER - 141)) | (1 << (OParser.TYPE_IDENTIFIER - 141)) | (1 << (OParser.VARIABLE_IDENTIFIER - 141)))) != 0):
                self.state = 1678
                self.lfp()
                self.state = 1679
                self.statement()
                self.state = 1685
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
        self.enterRule(localctx, 234, self.RULE_assertion_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1686
            self.assertion()
            self.state = 1692
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (OParser.EXECUTE - 95)) | (1 << (OParser.FETCH - 95)) | (1 << (OParser.FILTERED - 95)) | (1 << (OParser.MUTABLE - 95)) | (1 << (OParser.NULL - 95)) | (1 << (OParser.READ - 95)) | (1 << (OParser.SELF - 95)) | (1 << (OParser.SORTED - 95)) | (1 << (OParser.THIS - 95)) | (1 << (OParser.BOOLEAN_LITERAL - 95)) | (1 << (OParser.CHAR_LITERAL - 95)) | (1 << (OParser.MIN_INTEGER - 95)) | (1 << (OParser.MAX_INTEGER - 95)) | (1 << (OParser.SYMBOL_IDENTIFIER - 95)))) != 0) or ((((_la - 159)) & ~0x3f) == 0 and ((1 << (_la - 159)) & ((1 << (OParser.TYPE_IDENTIFIER - 159)) | (1 << (OParser.VARIABLE_IDENTIFIER - 159)) | (1 << (OParser.TEXT_LITERAL - 159)) | (1 << (OParser.UUID_LITERAL - 159)) | (1 << (OParser.INTEGER_LITERAL - 159)) | (1 << (OParser.HEXA_LITERAL - 159)) | (1 << (OParser.DECIMAL_LITERAL - 159)) | (1 << (OParser.DATETIME_LITERAL - 159)) | (1 << (OParser.TIME_LITERAL - 159)) | (1 << (OParser.DATE_LITERAL - 159)) | (1 << (OParser.PERIOD_LITERAL - 159)) | (1 << (OParser.VERSION_LITERAL - 159)))) != 0):
                self.state = 1687
                self.lfp()
                self.state = 1688
                self.assertion()
                self.state = 1694
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
        self.enterRule(localctx, 236, self.RULE_switch_case_statement_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1695
            self.switch_case_statement()
            self.state = 1701
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.CASE:
                self.state = 1696
                self.lfp()
                self.state = 1697
                self.switch_case_statement()
                self.state = 1703
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
        self.enterRule(localctx, 238, self.RULE_catch_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1704
            self.catch_statement()
            self.state = 1710
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,141,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1705
                    self.lfp()
                    self.state = 1706
                    self.catch_statement() 
                self.state = 1712
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,141,self._ctx)

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
        self.enterRule(localctx, 240, self.RULE_literal_collection)
        try:
            self.state = 1727
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,142,self._ctx)
            if la_ == 1:
                localctx = OParser.LiteralRangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1713
                self.match(OParser.LBRAK)
                self.state = 1714
                localctx.low = self.atomic_literal()
                self.state = 1715
                self.match(OParser.RANGE)
                self.state = 1716
                localctx.high = self.atomic_literal()
                self.state = 1717
                self.match(OParser.RBRAK)
                pass

            elif la_ == 2:
                localctx = OParser.LiteralListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1719
                self.match(OParser.LBRAK)
                self.state = 1720
                self.literal_list_literal()
                self.state = 1721
                self.match(OParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = OParser.LiteralSetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1723
                self.match(OParser.LT)
                self.state = 1724
                self.literal_list_literal()
                self.state = 1725
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
        self.enterRule(localctx, 242, self.RULE_atomic_literal)
        try:
            self.state = 1744
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.MIN_INTEGER]:
                localctx = OParser.MinIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1729
                localctx.t = self.match(OParser.MIN_INTEGER)
                pass
            elif token in [OParser.MAX_INTEGER]:
                localctx = OParser.MaxIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1730
                localctx.t = self.match(OParser.MAX_INTEGER)
                pass
            elif token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.IntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1731
                localctx.t = self.match(OParser.INTEGER_LITERAL)
                pass
            elif token in [OParser.HEXA_LITERAL]:
                localctx = OParser.HexadecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1732
                localctx.t = self.match(OParser.HEXA_LITERAL)
                pass
            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.CharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1733
                localctx.t = self.match(OParser.CHAR_LITERAL)
                pass
            elif token in [OParser.DATE_LITERAL]:
                localctx = OParser.DateLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1734
                localctx.t = self.match(OParser.DATE_LITERAL)
                pass
            elif token in [OParser.TIME_LITERAL]:
                localctx = OParser.TimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1735
                localctx.t = self.match(OParser.TIME_LITERAL)
                pass
            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.TextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1736
                localctx.t = self.match(OParser.TEXT_LITERAL)
                pass
            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.DecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1737
                localctx.t = self.match(OParser.DECIMAL_LITERAL)
                pass
            elif token in [OParser.DATETIME_LITERAL]:
                localctx = OParser.DateTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1738
                localctx.t = self.match(OParser.DATETIME_LITERAL)
                pass
            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.BooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1739
                localctx.t = self.match(OParser.BOOLEAN_LITERAL)
                pass
            elif token in [OParser.PERIOD_LITERAL]:
                localctx = OParser.PeriodLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1740
                localctx.t = self.match(OParser.PERIOD_LITERAL)
                pass
            elif token in [OParser.VERSION_LITERAL]:
                localctx = OParser.VersionLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1741
                localctx.t = self.match(OParser.VERSION_LITERAL)
                pass
            elif token in [OParser.UUID_LITERAL]:
                localctx = OParser.UUIDLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1742
                localctx.t = self.match(OParser.UUID_LITERAL)
                pass
            elif token in [OParser.NULL]:
                localctx = OParser.NullLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 1743
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
        self.enterRule(localctx, 244, self.RULE_literal_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1746
            self.atomic_literal()
            self.state = 1751
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1747
                self.match(OParser.COMMA)
                self.state = 1748
                self.atomic_literal()
                self.state = 1753
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
        self.enterRule(localctx, 246, self.RULE_selectable_expression)
        try:
            self.state = 1758
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,145,self._ctx)
            if la_ == 1:
                localctx = OParser.ParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1754
                localctx.exp = self.parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = OParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1755
                localctx.exp = self.literal_expression()
                pass

            elif la_ == 3:
                localctx = OParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1756
                localctx.exp = self.identifier()
                pass

            elif la_ == 4:
                localctx = OParser.ThisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1757
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
        self.enterRule(localctx, 248, self.RULE_this_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1760
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
        self.enterRule(localctx, 250, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1762
            self.match(OParser.LPAR)
            self.state = 1763
            self.expression(0)
            self.state = 1764
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
        self.enterRule(localctx, 252, self.RULE_literal_expression)
        try:
            self.state = 1768
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.NULL, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.MIN_INTEGER, OParser.MAX_INTEGER, OParser.TEXT_LITERAL, OParser.UUID_LITERAL, OParser.INTEGER_LITERAL, OParser.HEXA_LITERAL, OParser.DECIMAL_LITERAL, OParser.DATETIME_LITERAL, OParser.TIME_LITERAL, OParser.DATE_LITERAL, OParser.PERIOD_LITERAL, OParser.VERSION_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1766
                self.atomic_literal()
                pass
            elif token in [OParser.LPAR, OParser.LBRAK, OParser.LCURL, OParser.LT, OParser.MUTABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1767
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
        self.enterRule(localctx, 254, self.RULE_collection_literal)
        try:
            self.state = 1775
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,147,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1770
                self.range_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1771
                self.list_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1772
                self.set_literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1773
                self.dict_literal()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1774
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
        self.enterRule(localctx, 256, self.RULE_tuple_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1778
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.MUTABLE:
                self.state = 1777
                self.match(OParser.MUTABLE)


            self.state = 1780
            self.match(OParser.LPAR)
            self.state = 1782
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (OParser.EXECUTE - 95)) | (1 << (OParser.FETCH - 95)) | (1 << (OParser.FILTERED - 95)) | (1 << (OParser.MUTABLE - 95)) | (1 << (OParser.NULL - 95)) | (1 << (OParser.READ - 95)) | (1 << (OParser.SELF - 95)) | (1 << (OParser.SORTED - 95)) | (1 << (OParser.THIS - 95)) | (1 << (OParser.BOOLEAN_LITERAL - 95)) | (1 << (OParser.CHAR_LITERAL - 95)) | (1 << (OParser.MIN_INTEGER - 95)) | (1 << (OParser.MAX_INTEGER - 95)) | (1 << (OParser.SYMBOL_IDENTIFIER - 95)))) != 0) or ((((_la - 159)) & ~0x3f) == 0 and ((1 << (_la - 159)) & ((1 << (OParser.TYPE_IDENTIFIER - 159)) | (1 << (OParser.VARIABLE_IDENTIFIER - 159)) | (1 << (OParser.TEXT_LITERAL - 159)) | (1 << (OParser.UUID_LITERAL - 159)) | (1 << (OParser.INTEGER_LITERAL - 159)) | (1 << (OParser.HEXA_LITERAL - 159)) | (1 << (OParser.DECIMAL_LITERAL - 159)) | (1 << (OParser.DATETIME_LITERAL - 159)) | (1 << (OParser.TIME_LITERAL - 159)) | (1 << (OParser.DATE_LITERAL - 159)) | (1 << (OParser.PERIOD_LITERAL - 159)) | (1 << (OParser.VERSION_LITERAL - 159)))) != 0):
                self.state = 1781
                self.expression_tuple()


            self.state = 1784
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
        self.enterRule(localctx, 258, self.RULE_dict_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1787
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.MUTABLE:
                self.state = 1786
                self.match(OParser.MUTABLE)


            self.state = 1789
            self.match(OParser.LCURL)
            self.state = 1791
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (OParser.EXECUTE - 95)) | (1 << (OParser.FETCH - 95)) | (1 << (OParser.FILTERED - 95)) | (1 << (OParser.MUTABLE - 95)) | (1 << (OParser.NULL - 95)) | (1 << (OParser.READ - 95)) | (1 << (OParser.SELF - 95)) | (1 << (OParser.SORTED - 95)) | (1 << (OParser.THIS - 95)) | (1 << (OParser.BOOLEAN_LITERAL - 95)) | (1 << (OParser.CHAR_LITERAL - 95)) | (1 << (OParser.MIN_INTEGER - 95)) | (1 << (OParser.MAX_INTEGER - 95)) | (1 << (OParser.SYMBOL_IDENTIFIER - 95)))) != 0) or ((((_la - 159)) & ~0x3f) == 0 and ((1 << (_la - 159)) & ((1 << (OParser.TYPE_IDENTIFIER - 159)) | (1 << (OParser.VARIABLE_IDENTIFIER - 159)) | (1 << (OParser.TEXT_LITERAL - 159)) | (1 << (OParser.UUID_LITERAL - 159)) | (1 << (OParser.INTEGER_LITERAL - 159)) | (1 << (OParser.HEXA_LITERAL - 159)) | (1 << (OParser.DECIMAL_LITERAL - 159)) | (1 << (OParser.DATETIME_LITERAL - 159)) | (1 << (OParser.TIME_LITERAL - 159)) | (1 << (OParser.DATE_LITERAL - 159)) | (1 << (OParser.PERIOD_LITERAL - 159)) | (1 << (OParser.VERSION_LITERAL - 159)))) != 0):
                self.state = 1790
                self.dict_entry_list()


            self.state = 1793
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
        self.enterRule(localctx, 260, self.RULE_expression_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1795
            self.expression(0)
            self.state = 1796
            self.match(OParser.COMMA)
            self.state = 1805
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.LCURL) | (1 << OParser.XMARK) | (1 << OParser.MINUS) | (1 << OParser.LT) | (1 << OParser.CODE) | (1 << OParser.DOCUMENT) | (1 << OParser.BLOB))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (OParser.EXECUTE - 95)) | (1 << (OParser.FETCH - 95)) | (1 << (OParser.FILTERED - 95)) | (1 << (OParser.MUTABLE - 95)) | (1 << (OParser.NULL - 95)) | (1 << (OParser.READ - 95)) | (1 << (OParser.SELF - 95)) | (1 << (OParser.SORTED - 95)) | (1 << (OParser.THIS - 95)) | (1 << (OParser.BOOLEAN_LITERAL - 95)) | (1 << (OParser.CHAR_LITERAL - 95)) | (1 << (OParser.MIN_INTEGER - 95)) | (1 << (OParser.MAX_INTEGER - 95)) | (1 << (OParser.SYMBOL_IDENTIFIER - 95)))) != 0) or ((((_la - 159)) & ~0x3f) == 0 and ((1 << (_la - 159)) & ((1 << (OParser.TYPE_IDENTIFIER - 159)) | (1 << (OParser.VARIABLE_IDENTIFIER - 159)) | (1 << (OParser.TEXT_LITERAL - 159)) | (1 << (OParser.UUID_LITERAL - 159)) | (1 << (OParser.INTEGER_LITERAL - 159)) | (1 << (OParser.HEXA_LITERAL - 159)) | (1 << (OParser.DECIMAL_LITERAL - 159)) | (1 << (OParser.DATETIME_LITERAL - 159)) | (1 << (OParser.TIME_LITERAL - 159)) | (1 << (OParser.DATE_LITERAL - 159)) | (1 << (OParser.PERIOD_LITERAL - 159)) | (1 << (OParser.VERSION_LITERAL - 159)))) != 0):
                self.state = 1797
                self.expression(0)
                self.state = 1802
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==OParser.COMMA:
                    self.state = 1798
                    self.match(OParser.COMMA)
                    self.state = 1799
                    self.expression(0)
                    self.state = 1804
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
        self.enterRule(localctx, 262, self.RULE_dict_entry_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1807
            self.dict_entry()
            self.state = 1812
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1808
                self.match(OParser.COMMA)
                self.state = 1809
                self.dict_entry()
                self.state = 1814
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
        self.enterRule(localctx, 264, self.RULE_dict_entry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1815
            localctx.key = self.expression(0)
            self.state = 1816
            self.match(OParser.COLON)
            self.state = 1817
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
        self.enterRule(localctx, 266, self.RULE_slice_arguments)
        try:
            self.state = 1828
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,155,self._ctx)
            if la_ == 1:
                localctx = OParser.SliceFirstAndLastContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1819
                localctx.first = self.expression(0)
                self.state = 1820
                self.match(OParser.COLON)
                self.state = 1821
                localctx.last = self.expression(0)
                pass

            elif la_ == 2:
                localctx = OParser.SliceFirstOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1823
                localctx.first = self.expression(0)
                self.state = 1824
                self.match(OParser.COLON)
                pass

            elif la_ == 3:
                localctx = OParser.SliceLastOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1826
                self.match(OParser.COLON)
                self.state = 1827
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
        self.enterRule(localctx, 268, self.RULE_assign_variable_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1830
            self.variable_identifier()
            self.state = 1831
            self.assign()
            self.state = 1832
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
        _startState = 270
        self.enterRecursionRule(localctx, 270, self.RULE_assignable_instance, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.RootInstanceContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1835
            self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1841
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,156,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.ChildInstanceContext(self, OParser.Assignable_instanceContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignable_instance)
                    self.state = 1837
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1838
                    self.child_instance() 
                self.state = 1843
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,156,self._ctx)

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
        self.enterRule(localctx, 272, self.RULE_is_expression)
        try:
            self.state = 1848
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,157,self._ctx)
            if la_ == 1:
                localctx = OParser.IsATypeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1844
                if not self.willBeAOrAn():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willBeAOrAn()")
                self.state = 1845
                self.match(OParser.VARIABLE_IDENTIFIER)
                self.state = 1846
                self.category_or_any_type()
                pass

            elif la_ == 2:
                localctx = OParser.IsOtherExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1847
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
        self.enterRule(localctx, 274, self.RULE_read_all_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1850
            self.match(OParser.READ)
            self.state = 1851
            self.match(OParser.ALL)
            self.state = 1852
            self.match(OParser.FROM)
            self.state = 1853
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
        self.enterRule(localctx, 276, self.RULE_read_one_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1855
            self.match(OParser.READ)
            self.state = 1856
            self.match(OParser.ONE)
            self.state = 1857
            self.match(OParser.FROM)
            self.state = 1858
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
        self.enterRule(localctx, 278, self.RULE_order_by_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1860
            self.order_by()
            self.state = 1865
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.COMMA:
                self.state = 1861
                self.match(OParser.COMMA)
                self.state = 1862
                self.order_by()
                self.state = 1867
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
        self.enterRule(localctx, 280, self.RULE_order_by)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1868
            self.variable_identifier()
            self.state = 1873
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OParser.DOT:
                self.state = 1869
                self.match(OParser.DOT)
                self.state = 1870
                self.variable_identifier()
                self.state = 1875
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1877
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OParser.ASC or _la==OParser.DESC:
                self.state = 1876
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
        self.enterRule(localctx, 282, self.RULE_operator)
        try:
            self.state = 1885
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.PLUS]:
                localctx = OParser.OperatorPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1879
                self.match(OParser.PLUS)
                pass
            elif token in [OParser.MINUS]:
                localctx = OParser.OperatorMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1880
                self.match(OParser.MINUS)
                pass
            elif token in [OParser.STAR]:
                localctx = OParser.OperatorMultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1881
                self.multiply()
                pass
            elif token in [OParser.SLASH]:
                localctx = OParser.OperatorDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1882
                self.divide()
                pass
            elif token in [OParser.BSLASH]:
                localctx = OParser.OperatorIDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1883
                self.idivide()
                pass
            elif token in [OParser.PERCENT, OParser.MODULO]:
                localctx = OParser.OperatorModuloContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1884
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
        self.enterRule(localctx, 284, self.RULE_new_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1887
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1888
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
        self.enterRule(localctx, 286, self.RULE_key_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1890
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1891
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
        self.enterRule(localctx, 288, self.RULE_module_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1893
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1894
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
        self.enterRule(localctx, 290, self.RULE_value_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1896
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1897
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
        self.enterRule(localctx, 292, self.RULE_symbols_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1899
            localctx.i1 = self.match(OParser.VARIABLE_IDENTIFIER)
            self.state = 1900
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
        self.enterRule(localctx, 294, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1902
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
        self.enterRule(localctx, 296, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1904
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
        self.enterRule(localctx, 298, self.RULE_divide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1906
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
        self.enterRule(localctx, 300, self.RULE_idivide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1908
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
        self.enterRule(localctx, 302, self.RULE_modulo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1910
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
        self.enterRule(localctx, 304, self.RULE_lfs)
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
        self.enterRule(localctx, 306, self.RULE_lfp)
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
        self.enterRule(localctx, 308, self.RULE_javascript_statement)
        try:
            self.state = 1923
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.RETURN]:
                localctx = OParser.JavascriptReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1916
                self.match(OParser.RETURN)
                self.state = 1917
                localctx.exp = self.javascript_expression(0)
                self.state = 1918
                self.match(OParser.SEMI)
                pass
            elif token in [OParser.LPAR, OParser.LBRAK, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.UUID, OParser.NONE, OParser.NULL, OParser.READ, OParser.SELF, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER, OParser.TEXT_LITERAL, OParser.INTEGER_LITERAL, OParser.DECIMAL_LITERAL]:
                localctx = OParser.JavascriptStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1920
                localctx.exp = self.javascript_expression(0)
                self.state = 1921
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
        _startState = 310
        self.enterRecursionRule(localctx, 310, self.RULE_javascript_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavascriptPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1926
            localctx.exp = self.javascript_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1932
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,163,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavascriptSelectorExpressionContext(self, OParser.Javascript_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_expression)
                    self.state = 1928
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1929
                    localctx.child = self.javascript_selector_expression() 
                self.state = 1934
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,163,self._ctx)

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
        self.enterRule(localctx, 312, self.RULE_javascript_primary_expression)
        try:
            self.state = 1942
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,164,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1935
                self.javascript_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1936
                self.javascript_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1937
                self.javascript_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1938
                self.javascript_identifier_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1939
                self.javascript_literal_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1940
                self.javascript_method_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1941
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
        self.enterRule(localctx, 314, self.RULE_javascript_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1944
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
        self.enterRule(localctx, 316, self.RULE_javascript_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1946
            self.new_token()
            self.state = 1947
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
        self.enterRule(localctx, 318, self.RULE_javascript_selector_expression)
        try:
            self.state = 1954
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,165,self._ctx)
            if la_ == 1:
                localctx = OParser.JavaScriptMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1949
                self.match(OParser.DOT)
                self.state = 1950
                localctx.method = self.javascript_method_expression()
                pass

            elif la_ == 2:
                localctx = OParser.JavaScriptMemberExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1951
                self.match(OParser.DOT)
                self.state = 1952
                localctx.name = self.javascript_identifier()
                pass

            elif la_ == 3:
                localctx = OParser.JavaScriptItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1953
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
        self.enterRule(localctx, 320, self.RULE_javascript_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1956
            localctx.name = self.javascript_identifier()
            self.state = 1957
            self.match(OParser.LPAR)
            self.state = 1959
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.LBRAK) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.UUID))) != 0) or ((((_la - 117)) & ~0x3f) == 0 and ((1 << (_la - 117)) & ((1 << (OParser.NONE - 117)) | (1 << (OParser.NULL - 117)) | (1 << (OParser.READ - 117)) | (1 << (OParser.SELF - 117)) | (1 << (OParser.TEST - 117)) | (1 << (OParser.THIS - 117)) | (1 << (OParser.WRITE - 117)) | (1 << (OParser.BOOLEAN_LITERAL - 117)) | (1 << (OParser.CHAR_LITERAL - 117)) | (1 << (OParser.SYMBOL_IDENTIFIER - 117)) | (1 << (OParser.TYPE_IDENTIFIER - 117)) | (1 << (OParser.VARIABLE_IDENTIFIER - 117)) | (1 << (OParser.DOLLAR_IDENTIFIER - 117)) | (1 << (OParser.TEXT_LITERAL - 117)) | (1 << (OParser.INTEGER_LITERAL - 117)) | (1 << (OParser.DECIMAL_LITERAL - 117)))) != 0):
                self.state = 1958
                localctx.args = self.javascript_arguments(0)


            self.state = 1961
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
        _startState = 322
        self.enterRecursionRule(localctx, 322, self.RULE_javascript_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavascriptArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1964
            localctx.item = self.javascript_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1971
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,167,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavascriptArgumentListItemContext(self, OParser.Javascript_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_arguments)
                    self.state = 1966
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1967
                    self.match(OParser.COMMA)
                    self.state = 1968
                    localctx.item = self.javascript_expression(0) 
                self.state = 1973
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,167,self._ctx)

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
        self.enterRule(localctx, 324, self.RULE_javascript_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1974
            self.match(OParser.LBRAK)
            self.state = 1975
            localctx.exp = self.javascript_expression(0)
            self.state = 1976
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
        self.enterRule(localctx, 326, self.RULE_javascript_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1978
            self.match(OParser.LPAR)
            self.state = 1979
            localctx.exp = self.javascript_expression(0)
            self.state = 1980
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
        self.enterRule(localctx, 328, self.RULE_javascript_identifier_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1982
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
        self.enterRule(localctx, 330, self.RULE_javascript_literal_expression)
        try:
            self.state = 1989
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.JavascriptIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1984
                localctx.t = self.match(OParser.INTEGER_LITERAL)
                pass
            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.JavascriptDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1985
                localctx.t = self.match(OParser.DECIMAL_LITERAL)
                pass
            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.JavascriptTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1986
                localctx.t = self.match(OParser.TEXT_LITERAL)
                pass
            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.JavascriptBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1987
                localctx.t = self.match(OParser.BOOLEAN_LITERAL)
                pass
            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.JavascriptCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1988
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
        self.enterRule(localctx, 332, self.RULE_javascript_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1991
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
        self.enterRule(localctx, 334, self.RULE_python_statement)
        try:
            self.state = 1996
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.RETURN]:
                localctx = OParser.PythonReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1993
                self.match(OParser.RETURN)
                self.state = 1994
                localctx.exp = self.python_expression(0)
                pass
            elif token in [OParser.LPAR, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.UUID, OParser.NONE, OParser.NULL, OParser.READ, OParser.SELF, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER, OParser.TEXT_LITERAL, OParser.INTEGER_LITERAL, OParser.DECIMAL_LITERAL]:
                localctx = OParser.PythonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1995
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
        _startState = 336
        self.enterRecursionRule(localctx, 336, self.RULE_python_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.PythonPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1999
            localctx.exp = self.python_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2005
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,170,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.PythonSelectorExpressionContext(self, OParser.Python_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_expression)
                    self.state = 2001
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2002
                    localctx.child = self.python_selector_expression() 
                self.state = 2007
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,170,self._ctx)

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
        self.enterRule(localctx, 338, self.RULE_python_primary_expression)
        try:
            self.state = 2013
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,171,self._ctx)
            if la_ == 1:
                localctx = OParser.PythonSelfExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2008
                localctx.exp = self.python_self_expression()
                pass

            elif la_ == 2:
                localctx = OParser.PythonParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2009
                localctx.exp = self.python_parenthesis_expression()
                pass

            elif la_ == 3:
                localctx = OParser.PythonIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2010
                localctx.exp = self.python_identifier_expression(0)
                pass

            elif la_ == 4:
                localctx = OParser.PythonLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2011
                localctx.exp = self.python_literal_expression()
                pass

            elif la_ == 5:
                localctx = OParser.PythonGlobalMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2012
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
        self.enterRule(localctx, 340, self.RULE_python_self_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2015
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
        self.enterRule(localctx, 342, self.RULE_python_selector_expression)
        try:
            self.state = 2023
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.PythonMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2017
                self.match(OParser.DOT)
                self.state = 2018
                localctx.exp = self.python_method_expression()
                pass
            elif token in [OParser.LBRAK]:
                localctx = OParser.PythonItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2019
                self.match(OParser.LBRAK)
                self.state = 2020
                localctx.exp = self.python_expression(0)
                self.state = 2021
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
        self.enterRule(localctx, 344, self.RULE_python_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2025
            localctx.name = self.python_identifier()
            self.state = 2026
            self.match(OParser.LPAR)
            self.state = 2028
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.UUID))) != 0) or ((((_la - 117)) & ~0x3f) == 0 and ((1 << (_la - 117)) & ((1 << (OParser.NONE - 117)) | (1 << (OParser.NULL - 117)) | (1 << (OParser.READ - 117)) | (1 << (OParser.SELF - 117)) | (1 << (OParser.TEST - 117)) | (1 << (OParser.THIS - 117)) | (1 << (OParser.WRITE - 117)) | (1 << (OParser.BOOLEAN_LITERAL - 117)) | (1 << (OParser.CHAR_LITERAL - 117)) | (1 << (OParser.SYMBOL_IDENTIFIER - 117)) | (1 << (OParser.TYPE_IDENTIFIER - 117)) | (1 << (OParser.VARIABLE_IDENTIFIER - 117)) | (1 << (OParser.DOLLAR_IDENTIFIER - 117)) | (1 << (OParser.TEXT_LITERAL - 117)) | (1 << (OParser.INTEGER_LITERAL - 117)) | (1 << (OParser.DECIMAL_LITERAL - 117)))) != 0):
                self.state = 2027
                localctx.args = self.python_argument_list()


            self.state = 2030
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
        self.enterRule(localctx, 346, self.RULE_python_argument_list)
        try:
            self.state = 2038
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,174,self._ctx)
            if la_ == 1:
                localctx = OParser.PythonOrdinalOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2032
                localctx.ordinal = self.python_ordinal_argument_list(0)
                pass

            elif la_ == 2:
                localctx = OParser.PythonNamedOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2033
                localctx.named = self.python_named_argument_list(0)
                pass

            elif la_ == 3:
                localctx = OParser.PythonArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2034
                localctx.ordinal = self.python_ordinal_argument_list(0)
                self.state = 2035
                self.match(OParser.COMMA)
                self.state = 2036
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
        _startState = 348
        self.enterRecursionRule(localctx, 348, self.RULE_python_ordinal_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.PythonOrdinalArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2041
            localctx.item = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2048
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,175,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.PythonOrdinalArgumentListItemContext(self, OParser.Python_ordinal_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_ordinal_argument_list)
                    self.state = 2043
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2044
                    self.match(OParser.COMMA)
                    self.state = 2045
                    localctx.item = self.python_expression(0) 
                self.state = 2050
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,175,self._ctx)

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
        _startState = 350
        self.enterRecursionRule(localctx, 350, self.RULE_python_named_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.PythonNamedArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2052
            localctx.name = self.python_identifier()
            self.state = 2053
            self.match(OParser.EQ)
            self.state = 2054
            localctx.exp = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2064
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,176,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.PythonNamedArgumentListItemContext(self, OParser.Python_named_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_named_argument_list)
                    self.state = 2056
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2057
                    self.match(OParser.COMMA)
                    self.state = 2058
                    localctx.name = self.python_identifier()
                    self.state = 2059
                    self.match(OParser.EQ)
                    self.state = 2060
                    localctx.exp = self.python_expression(0) 
                self.state = 2066
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,176,self._ctx)

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
        self.enterRule(localctx, 352, self.RULE_python_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2067
            self.match(OParser.LPAR)
            self.state = 2068
            localctx.exp = self.python_expression(0)
            self.state = 2069
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
        _startState = 354
        self.enterRecursionRule(localctx, 354, self.RULE_python_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2074
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.DOLLAR_IDENTIFIER]:
                localctx = OParser.PythonPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2072
                self.match(OParser.DOLLAR_IDENTIFIER)
                pass
            elif token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.UUID, OParser.NONE, OParser.NULL, OParser.READ, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER]:
                localctx = OParser.PythonIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2073
                localctx.name = self.python_identifier()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2081
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,178,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.PythonChildIdentifierContext(self, OParser.Python_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_identifier_expression)
                    self.state = 2076
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2077
                    self.match(OParser.DOT)
                    self.state = 2078
                    localctx.name = self.python_identifier() 
                self.state = 2083
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,178,self._ctx)

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
        self.enterRule(localctx, 356, self.RULE_python_literal_expression)
        try:
            self.state = 2089
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.PythonIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2084
                localctx.t = self.match(OParser.INTEGER_LITERAL)
                pass
            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.PythonDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2085
                localctx.t = self.match(OParser.DECIMAL_LITERAL)
                pass
            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.PythonTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2086
                localctx.t = self.match(OParser.TEXT_LITERAL)
                pass
            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.PythonBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2087
                localctx.t = self.match(OParser.BOOLEAN_LITERAL)
                pass
            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.PythonCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2088
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
        self.enterRule(localctx, 358, self.RULE_python_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2091
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
        self.enterRule(localctx, 360, self.RULE_java_statement)
        try:
            self.state = 2100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.RETURN]:
                localctx = OParser.JavaReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2093
                self.match(OParser.RETURN)
                self.state = 2094
                localctx.exp = self.java_expression(0)
                self.state = 2095
                self.match(OParser.SEMI)
                pass
            elif token in [OParser.LPAR, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.UUID, OParser.NONE, OParser.NULL, OParser.READ, OParser.SELF, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.NATIVE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER, OParser.TEXT_LITERAL, OParser.INTEGER_LITERAL, OParser.DECIMAL_LITERAL]:
                localctx = OParser.JavaStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2097
                localctx.exp = self.java_expression(0)
                self.state = 2098
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
        _startState = 362
        self.enterRecursionRule(localctx, 362, self.RULE_java_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavaPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2103
            localctx.exp = self.java_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2109
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,181,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavaSelectorExpressionContext(self, OParser.Java_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_expression)
                    self.state = 2105
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2106
                    localctx.child = self.java_selector_expression() 
                self.state = 2111
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,181,self._ctx)

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
        self.enterRule(localctx, 364, self.RULE_java_primary_expression)
        try:
            self.state = 2117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,182,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2112
                self.java_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2113
                self.java_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2114
                self.java_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2115
                self.java_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2116
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
        self.enterRule(localctx, 366, self.RULE_java_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2119
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
        self.enterRule(localctx, 368, self.RULE_java_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2121
            self.new_token()
            self.state = 2122
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
        self.enterRule(localctx, 370, self.RULE_java_selector_expression)
        try:
            self.state = 2127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.JavaMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2124
                self.match(OParser.DOT)
                self.state = 2125
                localctx.exp = self.java_method_expression()
                pass
            elif token in [OParser.LBRAK]:
                localctx = OParser.JavaItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2126
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
        self.enterRule(localctx, 372, self.RULE_java_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2129
            localctx.name = self.java_identifier()
            self.state = 2130
            self.match(OParser.LPAR)
            self.state = 2132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.UUID))) != 0) or ((((_la - 117)) & ~0x3f) == 0 and ((1 << (_la - 117)) & ((1 << (OParser.NONE - 117)) | (1 << (OParser.NULL - 117)) | (1 << (OParser.READ - 117)) | (1 << (OParser.SELF - 117)) | (1 << (OParser.TEST - 117)) | (1 << (OParser.THIS - 117)) | (1 << (OParser.WRITE - 117)) | (1 << (OParser.BOOLEAN_LITERAL - 117)) | (1 << (OParser.CHAR_LITERAL - 117)) | (1 << (OParser.SYMBOL_IDENTIFIER - 117)) | (1 << (OParser.TYPE_IDENTIFIER - 117)) | (1 << (OParser.VARIABLE_IDENTIFIER - 117)) | (1 << (OParser.NATIVE_IDENTIFIER - 117)) | (1 << (OParser.DOLLAR_IDENTIFIER - 117)) | (1 << (OParser.TEXT_LITERAL - 117)) | (1 << (OParser.INTEGER_LITERAL - 117)) | (1 << (OParser.DECIMAL_LITERAL - 117)))) != 0):
                self.state = 2131
                localctx.args = self.java_arguments(0)


            self.state = 2134
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
        _startState = 374
        self.enterRecursionRule(localctx, 374, self.RULE_java_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavaArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2137
            localctx.item = self.java_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2144
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,185,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavaArgumentListItemContext(self, OParser.Java_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_arguments)
                    self.state = 2139
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2140
                    self.match(OParser.COMMA)
                    self.state = 2141
                    localctx.item = self.java_expression(0) 
                self.state = 2146
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,185,self._ctx)

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
        self.enterRule(localctx, 376, self.RULE_java_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2147
            self.match(OParser.LBRAK)
            self.state = 2148
            localctx.exp = self.java_expression(0)
            self.state = 2149
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
        self.enterRule(localctx, 378, self.RULE_java_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2151
            self.match(OParser.LPAR)
            self.state = 2152
            localctx.exp = self.java_expression(0)
            self.state = 2153
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
        _startState = 380
        self.enterRecursionRule(localctx, 380, self.RULE_java_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavaIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2156
            localctx.name = self.java_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2163
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,186,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavaChildIdentifierContext(self, OParser.Java_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_identifier_expression)
                    self.state = 2158
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2159
                    self.match(OParser.DOT)
                    self.state = 2160
                    localctx.name = self.java_identifier() 
                self.state = 2165
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,186,self._ctx)

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
        _startState = 382
        self.enterRecursionRule(localctx, 382, self.RULE_java_class_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.JavaClassIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2167
            localctx.klass = self.java_identifier_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2173
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,187,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.JavaChildClassIdentifierContext(self, OParser.Java_class_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_class_identifier_expression)
                    self.state = 2169
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2170
                    localctx.name = self.match(OParser.DOLLAR_IDENTIFIER) 
                self.state = 2175
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,187,self._ctx)

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
        self.enterRule(localctx, 384, self.RULE_java_literal_expression)
        try:
            self.state = 2181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.JavaIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2176
                localctx.t = self.match(OParser.INTEGER_LITERAL)
                pass
            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.JavaDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2177
                localctx.t = self.match(OParser.DECIMAL_LITERAL)
                pass
            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.JavaTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2178
                localctx.t = self.match(OParser.TEXT_LITERAL)
                pass
            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.JavaBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2179
                localctx.t = self.match(OParser.BOOLEAN_LITERAL)
                pass
            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.JavaCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2180
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
        self.enterRule(localctx, 386, self.RULE_java_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2183
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
        self.enterRule(localctx, 388, self.RULE_csharp_statement)
        try:
            self.state = 2192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.RETURN]:
                localctx = OParser.CSharpReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2185
                self.match(OParser.RETURN)
                self.state = 2186
                localctx.exp = self.csharp_expression(0)
                self.state = 2187
                self.match(OParser.SEMI)
                pass
            elif token in [OParser.LPAR, OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.UUID, OParser.NONE, OParser.NULL, OParser.READ, OParser.SELF, OParser.TEST, OParser.THIS, OParser.WRITE, OParser.BOOLEAN_LITERAL, OParser.CHAR_LITERAL, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER, OParser.DOLLAR_IDENTIFIER, OParser.TEXT_LITERAL, OParser.INTEGER_LITERAL, OParser.DECIMAL_LITERAL]:
                localctx = OParser.CSharpStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2189
                localctx.exp = self.csharp_expression(0)
                self.state = 2190
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
        _startState = 390
        self.enterRecursionRule(localctx, 390, self.RULE_csharp_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.CSharpPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2195
            localctx.exp = self.csharp_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2201
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,190,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.CSharpSelectorExpressionContext(self, OParser.Csharp_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_expression)
                    self.state = 2197
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2198
                    localctx.child = self.csharp_selector_expression() 
                self.state = 2203
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,190,self._ctx)

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
        self.enterRule(localctx, 392, self.RULE_csharp_primary_expression)
        try:
            self.state = 2209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,191,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2204
                self.csharp_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2205
                self.csharp_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2206
                self.csharp_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2207
                self.csharp_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2208
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
        self.enterRule(localctx, 394, self.RULE_csharp_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2211
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
        self.enterRule(localctx, 396, self.RULE_csharp_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2213
            self.new_token()
            self.state = 2214
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
        self.enterRule(localctx, 398, self.RULE_csharp_selector_expression)
        try:
            self.state = 2219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.DOT]:
                localctx = OParser.CSharpMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2216
                self.match(OParser.DOT)
                self.state = 2217
                localctx.exp = self.csharp_method_expression()
                pass
            elif token in [OParser.LBRAK]:
                localctx = OParser.CSharpItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2218
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
        self.enterRule(localctx, 400, self.RULE_csharp_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2221
            localctx.name = self.csharp_identifier()
            self.state = 2222
            self.match(OParser.LPAR)
            self.state = 2224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OParser.LPAR) | (1 << OParser.BOOLEAN) | (1 << OParser.CHARACTER) | (1 << OParser.TEXT) | (1 << OParser.INTEGER) | (1 << OParser.DECIMAL) | (1 << OParser.DATE) | (1 << OParser.TIME) | (1 << OParser.DATETIME) | (1 << OParser.PERIOD) | (1 << OParser.VERSION) | (1 << OParser.UUID))) != 0) or ((((_la - 117)) & ~0x3f) == 0 and ((1 << (_la - 117)) & ((1 << (OParser.NONE - 117)) | (1 << (OParser.NULL - 117)) | (1 << (OParser.READ - 117)) | (1 << (OParser.SELF - 117)) | (1 << (OParser.TEST - 117)) | (1 << (OParser.THIS - 117)) | (1 << (OParser.WRITE - 117)) | (1 << (OParser.BOOLEAN_LITERAL - 117)) | (1 << (OParser.CHAR_LITERAL - 117)) | (1 << (OParser.SYMBOL_IDENTIFIER - 117)) | (1 << (OParser.TYPE_IDENTIFIER - 117)) | (1 << (OParser.VARIABLE_IDENTIFIER - 117)) | (1 << (OParser.DOLLAR_IDENTIFIER - 117)) | (1 << (OParser.TEXT_LITERAL - 117)) | (1 << (OParser.INTEGER_LITERAL - 117)) | (1 << (OParser.DECIMAL_LITERAL - 117)))) != 0):
                self.state = 2223
                localctx.args = self.csharp_arguments(0)


            self.state = 2226
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
        _startState = 402
        self.enterRecursionRule(localctx, 402, self.RULE_csharp_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = OParser.CSharpArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2229
            localctx.item = self.csharp_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,194,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.CSharpArgumentListItemContext(self, OParser.Csharp_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_arguments)
                    self.state = 2231
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2232
                    self.match(OParser.COMMA)
                    self.state = 2233
                    localctx.item = self.csharp_expression(0) 
                self.state = 2238
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,194,self._ctx)

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
        self.enterRule(localctx, 404, self.RULE_csharp_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2239
            self.match(OParser.LBRAK)
            self.state = 2240
            localctx.exp = self.csharp_expression(0)
            self.state = 2241
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
        self.enterRule(localctx, 406, self.RULE_csharp_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2243
            self.match(OParser.LPAR)
            self.state = 2244
            localctx.exp = self.csharp_expression(0)
            self.state = 2245
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
        _startState = 408
        self.enterRecursionRule(localctx, 408, self.RULE_csharp_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2250
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.DOLLAR_IDENTIFIER]:
                localctx = OParser.CSharpPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2248
                self.match(OParser.DOLLAR_IDENTIFIER)
                pass
            elif token in [OParser.BOOLEAN, OParser.CHARACTER, OParser.TEXT, OParser.INTEGER, OParser.DECIMAL, OParser.DATE, OParser.TIME, OParser.DATETIME, OParser.PERIOD, OParser.VERSION, OParser.UUID, OParser.NONE, OParser.NULL, OParser.READ, OParser.SELF, OParser.TEST, OParser.WRITE, OParser.SYMBOL_IDENTIFIER, OParser.TYPE_IDENTIFIER, OParser.VARIABLE_IDENTIFIER]:
                localctx = OParser.CSharpIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2249
                localctx.name = self.csharp_identifier()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2257
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,196,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = OParser.CSharpChildIdentifierContext(self, OParser.Csharp_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_identifier_expression)
                    self.state = 2252
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2253
                    self.match(OParser.DOT)
                    self.state = 2254
                    localctx.name = self.csharp_identifier() 
                self.state = 2259
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,196,self._ctx)

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
        self.enterRule(localctx, 410, self.RULE_csharp_literal_expression)
        try:
            self.state = 2265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OParser.INTEGER_LITERAL]:
                localctx = OParser.CSharpIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2260
                self.match(OParser.INTEGER_LITERAL)
                pass
            elif token in [OParser.DECIMAL_LITERAL]:
                localctx = OParser.CSharpDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2261
                self.match(OParser.DECIMAL_LITERAL)
                pass
            elif token in [OParser.TEXT_LITERAL]:
                localctx = OParser.CSharpTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2262
                self.match(OParser.TEXT_LITERAL)
                pass
            elif token in [OParser.BOOLEAN_LITERAL]:
                localctx = OParser.CSharpBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2263
                self.match(OParser.BOOLEAN_LITERAL)
                pass
            elif token in [OParser.CHAR_LITERAL]:
                localctx = OParser.CSharpCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2264
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
        self.enterRule(localctx, 412, self.RULE_csharp_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2267
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
        self._predicates[59] = self.argument_assignment_list_sempred
        self._predicates[78] = self.typedef_sempred
        self._predicates[98] = self.any_type_sempred
        self._predicates[135] = self.assignable_instance_sempred
        self._predicates[136] = self.is_expression_sempred
        self._predicates[142] = self.new_token_sempred
        self._predicates[143] = self.key_token_sempred
        self._predicates[144] = self.module_token_sempred
        self._predicates[145] = self.value_token_sempred
        self._predicates[146] = self.symbols_token_sempred
        self._predicates[155] = self.javascript_expression_sempred
        self._predicates[161] = self.javascript_arguments_sempred
        self._predicates[168] = self.python_expression_sempred
        self._predicates[174] = self.python_ordinal_argument_list_sempred
        self._predicates[175] = self.python_named_argument_list_sempred
        self._predicates[177] = self.python_identifier_expression_sempred
        self._predicates[181] = self.java_expression_sempred
        self._predicates[187] = self.java_arguments_sempred
        self._predicates[190] = self.java_identifier_expression_sempred
        self._predicates[191] = self.java_class_identifier_expression_sempred
        self._predicates[195] = self.csharp_expression_sempred
        self._predicates[201] = self.csharp_arguments_sempred
        self._predicates[204] = self.csharp_identifier_expression_sempred
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
         

    def argument_assignment_list_sempred(self, localctx, predIndex):
            if predIndex == 36:
                return self.willNotBe(self.equalToken())
         

            if predIndex == 37:
                return self.precpred(self._ctx, 1)
         

    def typedef_sempred(self, localctx, predIndex):
            if predIndex == 38:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 39:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 40:
                return self.precpred(self._ctx, 3)
         

    def any_type_sempred(self, localctx, predIndex):
            if predIndex == 41:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 42:
                return self.precpred(self._ctx, 1)
         

    def assignable_instance_sempred(self, localctx, predIndex):
            if predIndex == 43:
                return self.precpred(self._ctx, 1)
         

    def is_expression_sempred(self, localctx, predIndex):
            if predIndex == 44:
                return self.willBeAOrAn()
         

    def new_token_sempred(self, localctx, predIndex):
            if predIndex == 45:
                return self.isText(localctx.i1,"new")
         

    def key_token_sempred(self, localctx, predIndex):
            if predIndex == 46:
                return self.isText(localctx.i1,"key")
         

    def module_token_sempred(self, localctx, predIndex):
            if predIndex == 47:
                return self.isText(localctx.i1,"module")
         

    def value_token_sempred(self, localctx, predIndex):
            if predIndex == 48:
                return self.isText(localctx.i1,"value")
         

    def symbols_token_sempred(self, localctx, predIndex):
            if predIndex == 49:
                return self.isText(localctx.i1,"symbols")
         

    def javascript_expression_sempred(self, localctx, predIndex):
            if predIndex == 50:
                return self.precpred(self._ctx, 1)
         

    def javascript_arguments_sempred(self, localctx, predIndex):
            if predIndex == 51:
                return self.precpred(self._ctx, 1)
         

    def python_expression_sempred(self, localctx, predIndex):
            if predIndex == 52:
                return self.precpred(self._ctx, 1)
         

    def python_ordinal_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 53:
                return self.precpred(self._ctx, 1)
         

    def python_named_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 54:
                return self.precpred(self._ctx, 1)
         

    def python_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 55:
                return self.precpred(self._ctx, 1)
         

    def java_expression_sempred(self, localctx, predIndex):
            if predIndex == 56:
                return self.precpred(self._ctx, 1)
         

    def java_arguments_sempred(self, localctx, predIndex):
            if predIndex == 57:
                return self.precpred(self._ctx, 1)
         

    def java_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 58:
                return self.precpred(self._ctx, 1)
         

    def java_class_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 59:
                return self.precpred(self._ctx, 1)
         

    def csharp_expression_sempred(self, localctx, predIndex):
            if predIndex == 60:
                return self.precpred(self._ctx, 1)
         

    def csharp_arguments_sempred(self, localctx, predIndex):
            if predIndex == 61:
                return self.precpred(self._ctx, 1)
         

    def csharp_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 62:
                return self.precpred(self._ctx, 1)
         




