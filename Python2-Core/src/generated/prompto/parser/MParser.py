# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .MParserListener import MParserListener
else:
    from MParserListener import MParserListener
from .AbstractParser import AbstractParser

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\u00af\u08cf\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
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
        buf.write(u"\4\u00cf\t\u00cf\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u01a5\n")
        buf.write(u"\2\3\2\5\2\u01a8\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5")
        buf.write(u"\3\5\3\5\5\5\u01c1\n\5\3\5\3\5\3\6\5\6\u01c6\n\6\3\6")
        buf.write(u"\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u01d4")
        buf.write(u"\n\6\3\6\3\6\3\6\3\6\5\6\u01da\n\6\5\6\u01dc\n\6\5\6")
        buf.write(u"\u01de\n\6\3\6\3\6\3\7\3\7\3\7\5\7\u01e5\n\7\3\7\3\7")
        buf.write(u"\3\b\5\b\u01ea\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write(u"\b\5\b\u01f5\n\b\3\b\3\b\3\b\3\b\3\b\5\b\u01fc\n\b\3")
        buf.write(u"\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u0209")
        buf.write(u"\n\t\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write(u"\13\3\13\5\13\u0217\n\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write(u"\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\5\r")
        buf.write(u"\u022b\n\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write(u"\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write(u"\17\5\17\u0242\n\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write(u"\3\17\3\20\5\20\u024d\n\20\3\20\3\20\3\20\3\20\3\20\5")
        buf.write(u"\20\u0254\n\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20")
        buf.write(u"\u025d\n\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\5\21\u0266")
        buf.write(u"\n\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u026f\n")
        buf.write(u"\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write(u"\3\23\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u0282\n\23\f")
        buf.write(u"\23\16\23\u0285\13\23\3\24\3\24\3\24\3\24\3\24\5\24\u028c")
        buf.write(u"\n\24\3\24\3\24\3\24\5\24\u0291\n\24\3\25\3\25\3\25\3")
        buf.write(u"\25\5\25\u0297\n\25\3\25\3\25\3\25\5\25\u029c\n\25\3")
        buf.write(u"\25\3\25\3\25\3\25\3\25\3\26\3\26\5\26\u02a5\n\26\3\26")
        buf.write(u"\3\26\3\26\5\26\u02aa\n\26\3\26\3\26\3\26\5\26\u02af")
        buf.write(u"\n\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3")
        buf.write(u"\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write(u"\3\27\3\27\5\27\u02c7\n\27\3\30\3\30\3\31\3\31\3\31\3")
        buf.write(u"\31\3\31\3\31\3\31\5\31\u02d2\n\31\3\31\3\31\5\31\u02d6")
        buf.write(u"\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write(u"\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32")
        buf.write(u"\u02eb\n\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3")
        buf.write(u"\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write(u"\3\34\3\34\3\34\3\34\3\34\5\34\u0305\n\34\3\35\3\35\3")
        buf.write(u"\35\5\35\u030a\n\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write(u"\5\36\u0313\n\36\3\37\3\37\3\37\3\37\3\37\7\37\u031a")
        buf.write(u"\n\37\f\37\16\37\u031d\13\37\3 \3 \3 \3 \3 \3 \5 \u0325")
        buf.write(u"\n \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write(u"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\5#\u0342\n#\3")
        buf.write(u"#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$")
        buf.write(u"\u0355\n$\3%\3%\3%\3%\5%\u035b\n%\3%\3%\3%\3%\3%\3%\3")
        buf.write(u"%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write(u"\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u037d\n(\3(\3(\3(")
        buf.write(u"\3(\3(\3(\3(\5(\u0386\n(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(u")\3)\3)\3)\3)\3)\3)\3)\3)\3)\7)\u039b\n)\f)\16)\u039e")
        buf.write(u"\13)\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\5+\u03ab\n+\3+")
        buf.write(u"\3+\3+\3+\3+\3+\3+\5+\u03b4\n+\3+\3+\3+\3+\3+\3+\3+\5")
        buf.write(u"+\u03bd\n+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,")
        buf.write(u"\3,\3,\3,\3,\3,\3,\3,\5,\u03d4\n,\3-\3-\3.\3.\5.\u03da")
        buf.write(u"\n.\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3")
        buf.write(u"/\3/\5/\u03ee\n/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/")
        buf.write(u"\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3")
        buf.write(u"/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/")
        buf.write(u"\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3")
        buf.write(u"/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/")
        buf.write(u"\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3")
        buf.write(u"/\3/\3/\7/\u0456\n/\f/\16/\u0459\13/\3\60\3\60\3\61\3")
        buf.write(u"\61\3\61\3\61\3\61\7\61\u0462\n\61\f\61\16\61\u0465\13")
        buf.write(u"\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u046f")
        buf.write(u"\n\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3")
        buf.write(u"\63\3\63\3\63\3\63\5\63\u047e\n\63\3\64\3\64\3\64\5\64")
        buf.write(u"\u0483\n\64\3\64\3\64\3\65\3\65\3\65\5\65\u048a\n\65")
        buf.write(u"\3\65\3\65\3\66\3\66\3\66\5\66\u0491\n\66\3\66\3\66\3")
        buf.write(u"\67\3\67\3\67\3\67\3\67\5\67\u049a\n\67\3\67\3\67\3\67")
        buf.write(u"\7\67\u049f\n\67\f\67\16\67\u04a2\13\67\38\38\38\38\3")
        buf.write(u"9\39\39\39\39\3:\3:\3:\3:\3:\3:\3;\3;\3;\5;\u04b6\n;")
        buf.write(u"\3;\3;\3;\3;\3;\3;\3;\3;\3;\5;\u04c1\n;\3;\3;\5;\u04c5")
        buf.write(u"\n;\3;\3;\3;\5;\u04ca\n;\3;\3;\3;\5;\u04cf\n;\5;\u04d1")
        buf.write(u"\n;\3<\3<\5<\u04d5\n<\3<\3<\3<\3<\3<\3<\3<\5<\u04de\n")
        buf.write(u"<\3<\3<\3=\3=\3=\3=\3>\3>\3>\3>\3>\3>\3>\3>\5>\u04ee")
        buf.write(u"\n>\3?\3?\3?\3?\3@\7@\u04f5\n@\f@\16@\u04f8\13@\3A\6")
        buf.write(u"A\u04fb\nA\rA\16A\u04fc\3B\6B\u0500\nB\rB\16B\u0501\3")
        buf.write(u"B\3B\3C\7C\u0507\nC\fC\16C\u050a\13C\3C\3C\3D\3D\3E\5")
        buf.write(u"E\u0511\nE\3E\3E\3E\3F\3F\3F\3F\7F\u051a\nF\fF\16F\u051d")
        buf.write(u"\13F\3G\3G\3G\7G\u0522\nG\fG\16G\u0525\13G\3G\3G\3G\3")
        buf.write(u"G\3G\5G\u052c\nG\3H\3H\3I\3I\5I\u0532\nI\3J\3J\3J\3J")
        buf.write(u"\7J\u0538\nJ\fJ\16J\u053b\13J\3K\3K\3K\3K\7K\u0541\n")
        buf.write(u"K\fK\16K\u0544\13K\3L\3L\3L\7L\u0549\nL\fL\16L\u054c")
        buf.write(u"\13L\3M\3M\3M\3M\3M\3M\3M\3M\3M\3M\5M\u0558\nM\3N\5N")
        buf.write(u"\u055b\nN\3N\3N\5N\u055f\nN\3N\3N\3O\5O\u0564\nO\3O\3")
        buf.write(u"O\5O\u0568\nO\3O\3O\3P\3P\3P\7P\u056f\nP\fP\16P\u0572")
        buf.write(u"\13P\3Q\3Q\3Q\3Q\3Q\3Q\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R")
        buf.write(u"\3R\3R\5R\u0586\nR\3R\3R\3R\3R\3R\3R\3R\3R\7R\u0590\n")
        buf.write(u"R\fR\16R\u0593\13R\3S\3S\5S\u0597\nS\3T\3T\3T\3T\3T\3")
        buf.write(u"T\3T\3T\3T\3T\3T\3T\3T\3T\5T\u05a7\nT\3U\3U\3V\5V\u05ac")
        buf.write(u"\nV\3V\3V\3W\3W\3X\3X\3X\5X\u05b5\nX\3Y\3Y\3Y\7Y\u05ba")
        buf.write(u"\nY\fY\16Y\u05bd\13Y\3Z\3Z\5Z\u05c1\nZ\3[\3[\3[\5[\u05c6")
        buf.write(u"\n[\3\\\3\\\3]\3]\3^\3^\3_\3_\3`\3`\3`\7`\u05d3\n`\f")
        buf.write(u"`\16`\u05d6\13`\3a\3a\5a\u05da\na\3a\5a\u05dd\na\3b\3")
        buf.write(u"b\5b\u05e1\nb\3c\3c\3c\5c\u05e6\nc\3d\3d\3d\3e\3e\5e")
        buf.write(u"\u05ed\ne\3f\3f\3f\3f\3f\3f\3f\3f\3f\7f\u05f8\nf\ff\16")
        buf.write(u"f\u05fb\13f\3g\3g\3g\3g\7g\u0601\ng\fg\16g\u0604\13g")
        buf.write(u"\3h\3h\3h\3h\3h\5h\u060b\nh\3i\3i\3i\3i\7i\u0611\ni\f")
        buf.write(u"i\16i\u0614\13i\3j\3j\3j\5j\u0619\nj\3k\3k\3k\3k\3k\3")
        buf.write(u"k\3k\3k\3k\3k\5k\u0625\nk\3l\3l\5l\u0629\nl\3m\3m\3m")
        buf.write(u"\3m\3m\3m\7m\u0631\nm\fm\16m\u0634\13m\3n\3n\5n\u0638")
        buf.write(u"\nn\3o\3o\3o\3o\5o\u063e\no\3o\3o\3o\7o\u0643\no\fo\16")
        buf.write(u"o\u0646\13o\3o\3o\5o\u064a\no\3p\3p\3p\7p\u064f\np\f")
        buf.write(u"p\16p\u0652\13p\3q\3q\3q\7q\u0657\nq\fq\16q\u065a\13")
        buf.write(u"q\3r\3r\3r\3r\5r\u0660\nr\3s\3s\3t\3t\3t\3t\7t\u0668")
        buf.write(u"\nt\ft\16t\u066b\13t\3u\3u\3u\3u\3u\3u\3u\3u\3u\3u\5")
        buf.write(u"u\u0677\nu\3v\3v\5v\u067b\nv\3v\5v\u067e\nv\3w\3w\5w")
        buf.write(u"\u0682\nw\3w\5w\u0685\nw\3x\3x\3x\3x\7x\u068b\nx\fx\16")
        buf.write(u"x\u068e\13x\3y\3y\3y\3y\7y\u0694\ny\fy\16y\u0697\13y")
        buf.write(u"\3z\3z\3z\3z\7z\u069d\nz\fz\16z\u06a0\13z\3{\3{\3{\3")
        buf.write(u"{\7{\u06a6\n{\f{\16{\u06a9\13{\3|\3|\3|\3|\3|\3|\3|\3")
        buf.write(u"|\3|\3|\3|\3|\3|\3|\5|\u06b9\n|\3}\3}\3}\3}\3}\3}\3}")
        buf.write(u"\3}\3}\3}\3}\3}\3}\3}\5}\u06c9\n}\3~\3~\3~\7~\u06ce\n")
        buf.write(u"~\f~\16~\u06d1\13~\3\177\3\177\3\177\3\177\5\177\u06d7")
        buf.write(u"\n\177\3\u0080\3\u0080\3\u0081\3\u0081\3\u0081\3\u0081")
        buf.write(u"\3\u0082\3\u0082\5\u0082\u06e1\n\u0082\3\u0083\3\u0083")
        buf.write(u"\3\u0083\3\u0083\3\u0083\5\u0083\u06e8\n\u0083\3\u0084")
        buf.write(u"\5\u0084\u06eb\n\u0084\3\u0084\3\u0084\5\u0084\u06ef")
        buf.write(u"\n\u0084\3\u0084\3\u0084\3\u0085\5\u0085\u06f4\n\u0085")
        buf.write(u"\3\u0085\3\u0085\5\u0085\u06f8\n\u0085\3\u0085\3\u0085")
        buf.write(u"\3\u0086\3\u0086\3\u0086\3\u0086\3\u0086\7\u0086\u0701")
        buf.write(u"\n\u0086\f\u0086\16\u0086\u0704\13\u0086\5\u0086\u0706")
        buf.write(u"\n\u0086\3\u0087\3\u0087\3\u0087\7\u0087\u070b\n\u0087")
        buf.write(u"\f\u0087\16\u0087\u070e\13\u0087\3\u0088\3\u0088\3\u0088")
        buf.write(u"\3\u0088\3\u0089\3\u0089\3\u0089\3\u0089\3\u0089\3\u0089")
        buf.write(u"\3\u0089\3\u0089\3\u0089\5\u0089\u071d\n\u0089\3\u008a")
        buf.write(u"\3\u008a\3\u008a\3\u008a\3\u008b\3\u008b\3\u008b\3\u008b")
        buf.write(u"\3\u008b\7\u008b\u0728\n\u008b\f\u008b\16\u008b\u072b")
        buf.write(u"\13\u008b\3\u008c\3\u008c\3\u008c\3\u008c\5\u008c\u0731")
        buf.write(u"\n\u008c\3\u008d\3\u008d\3\u008d\3\u008d\3\u008d\3\u008e")
        buf.write(u"\3\u008e\3\u008e\3\u008e\3\u008e\3\u008f\3\u008f\3\u008f")
        buf.write(u"\7\u008f\u0740\n\u008f\f\u008f\16\u008f\u0743\13\u008f")
        buf.write(u"\3\u0090\3\u0090\3\u0090\7\u0090\u0748\n\u0090\f\u0090")
        buf.write(u"\16\u0090\u074b\13\u0090\3\u0090\5\u0090\u074e\n\u0090")
        buf.write(u"\3\u0091\3\u0091\3\u0091\3\u0091\3\u0091\3\u0091\5\u0091")
        buf.write(u"\u0756\n\u0091\3\u0092\3\u0092\3\u0092\3\u0093\3\u0093")
        buf.write(u"\3\u0093\3\u0094\3\u0094\3\u0094\3\u0095\3\u0095\3\u0095")
        buf.write(u"\3\u0096\3\u0096\3\u0096\3\u0097\3\u0097\3\u0098\3\u0098")
        buf.write(u"\3\u0099\3\u0099\3\u009a\3\u009a\3\u009b\3\u009b\3\u009c")
        buf.write(u"\3\u009c\3\u009c\3\u009c\3\u009c\3\u009c\3\u009c\5\u009c")
        buf.write(u"\u0778\n\u009c\3\u009d\3\u009d\3\u009d\3\u009d\3\u009d")
        buf.write(u"\7\u009d\u077f\n\u009d\f\u009d\16\u009d\u0782\13\u009d")
        buf.write(u"\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e")
        buf.write(u"\5\u009e\u078b\n\u009e\3\u009f\3\u009f\3\u00a0\3\u00a0")
        buf.write(u"\3\u00a0\3\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1\5\u00a1")
        buf.write(u"\u0797\n\u00a1\3\u00a2\3\u00a2\3\u00a2\5\u00a2\u079c")
        buf.write(u"\n\u00a2\3\u00a2\3\u00a2\3\u00a3\3\u00a3\3\u00a3\3\u00a3")
        buf.write(u"\3\u00a3\3\u00a3\7\u00a3\u07a6\n\u00a3\f\u00a3\16\u00a3")
        buf.write(u"\u07a9\13\u00a3\3\u00a4\3\u00a4\3\u00a4\3\u00a4\3\u00a5")
        buf.write(u"\3\u00a5\3\u00a5\3\u00a5\3\u00a6\3\u00a6\3\u00a7\3\u00a7")
        buf.write(u"\3\u00a7\3\u00a7\3\u00a7\5\u00a7\u07ba\n\u00a7\3\u00a8")
        buf.write(u"\3\u00a8\3\u00a9\3\u00a9\3\u00a9\5\u00a9\u07c1\n\u00a9")
        buf.write(u"\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa\7\u00aa\u07c8")
        buf.write(u"\n\u00aa\f\u00aa\16\u00aa\u07cb\13\u00aa\3\u00ab\3\u00ab")
        buf.write(u"\3\u00ab\3\u00ab\5\u00ab\u07d1\n\u00ab\3\u00ac\3\u00ac")
        buf.write(u"\3\u00ac\3\u00ac\3\u00ac\3\u00ac\5\u00ac\u07d9\n\u00ac")
        buf.write(u"\3\u00ad\3\u00ad\3\u00ad\5\u00ad\u07de\n\u00ad\3\u00ad")
        buf.write(u"\3\u00ad\3\u00ae\3\u00ae\3\u00ae\3\u00ae\3\u00ae\3\u00ae")
        buf.write(u"\5\u00ae\u07e8\n\u00ae\3\u00af\3\u00af\3\u00af\3\u00af")
        buf.write(u"\3\u00af\3\u00af\7\u00af\u07f0\n\u00af\f\u00af\16\u00af")
        buf.write(u"\u07f3\13\u00af\3\u00b0\3\u00b0\3\u00b0\3\u00b0\3\u00b0")
        buf.write(u"\3\u00b0\3\u00b0\3\u00b0\3\u00b0\3\u00b0\3\u00b0\7\u00b0")
        buf.write(u"\u0800\n\u00b0\f\u00b0\16\u00b0\u0803\13\u00b0\3\u00b1")
        buf.write(u"\3\u00b1\3\u00b1\3\u00b1\3\u00b2\3\u00b2\3\u00b2\5\u00b2")
        buf.write(u"\u080c\n\u00b2\3\u00b2\3\u00b2\3\u00b2\7\u00b2\u0811")
        buf.write(u"\n\u00b2\f\u00b2\16\u00b2\u0814\13\u00b2\3\u00b3\3\u00b3")
        buf.write(u"\3\u00b3\3\u00b3\3\u00b3\5\u00b3\u081b\n\u00b3\3\u00b4")
        buf.write(u"\3\u00b4\3\u00b5\3\u00b5\3\u00b5\3\u00b5\3\u00b5\3\u00b5")
        buf.write(u"\3\u00b5\5\u00b5\u0826\n\u00b5\3\u00b6\3\u00b6\3\u00b6")
        buf.write(u"\3\u00b6\3\u00b6\7\u00b6\u082d\n\u00b6\f\u00b6\16\u00b6")
        buf.write(u"\u0830\13\u00b6\3\u00b7\3\u00b7\3\u00b7\3\u00b7\3\u00b7")
        buf.write(u"\5\u00b7\u0837\n\u00b7\3\u00b8\3\u00b8\3\u00b9\3\u00b9")
        buf.write(u"\3\u00b9\3\u00ba\3\u00ba\3\u00ba\5\u00ba\u0841\n\u00ba")
        buf.write(u"\3\u00bb\3\u00bb\3\u00bb\5\u00bb\u0846\n\u00bb\3\u00bb")
        buf.write(u"\3\u00bb\3\u00bc\3\u00bc\3\u00bc\3\u00bc\3\u00bc\3\u00bc")
        buf.write(u"\7\u00bc\u0850\n\u00bc\f\u00bc\16\u00bc\u0853\13\u00bc")
        buf.write(u"\3\u00bd\3\u00bd\3\u00bd\3\u00bd\3\u00be\3\u00be\3\u00be")
        buf.write(u"\3\u00be\3\u00bf\3\u00bf\3\u00bf\3\u00bf\3\u00bf\3\u00bf")
        buf.write(u"\7\u00bf\u0863\n\u00bf\f\u00bf\16\u00bf\u0866\13\u00bf")
        buf.write(u"\3\u00c0\3\u00c0\3\u00c0\3\u00c0\3\u00c0\7\u00c0\u086d")
        buf.write(u"\n\u00c0\f\u00c0\16\u00c0\u0870\13\u00c0\3\u00c1\3\u00c1")
        buf.write(u"\3\u00c1\3\u00c1\3\u00c1\5\u00c1\u0877\n\u00c1\3\u00c2")
        buf.write(u"\3\u00c2\3\u00c3\3\u00c3\3\u00c3\3\u00c3\3\u00c3\3\u00c3")
        buf.write(u"\3\u00c3\5\u00c3\u0882\n\u00c3\3\u00c4\3\u00c4\3\u00c4")
        buf.write(u"\3\u00c4\3\u00c4\7\u00c4\u0889\n\u00c4\f\u00c4\16\u00c4")
        buf.write(u"\u088c\13\u00c4\3\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c5")
        buf.write(u"\5\u00c5\u0893\n\u00c5\3\u00c6\3\u00c6\3\u00c7\3\u00c7")
        buf.write(u"\3\u00c7\3\u00c8\3\u00c8\3\u00c8\5\u00c8\u089d\n\u00c8")
        buf.write(u"\3\u00c9\3\u00c9\3\u00c9\5\u00c9\u08a2\n\u00c9\3\u00c9")
        buf.write(u"\3\u00c9\3\u00ca\3\u00ca\3\u00ca\3\u00ca\3\u00ca\3\u00ca")
        buf.write(u"\7\u00ca\u08ac\n\u00ca\f\u00ca\16\u00ca\u08af\13\u00ca")
        buf.write(u"\3\u00cb\3\u00cb\3\u00cb\3\u00cb\3\u00cc\3\u00cc\3\u00cc")
        buf.write(u"\3\u00cc\3\u00cd\3\u00cd\3\u00cd\5\u00cd\u08bc\n\u00cd")
        buf.write(u"\3\u00cd\3\u00cd\3\u00cd\7\u00cd\u08c1\n\u00cd\f\u00cd")
        buf.write(u"\16\u00cd\u08c4\13\u00cd\3\u00ce\3\u00ce\3\u00ce\3\u00ce")
        buf.write(u"\3\u00ce\5\u00ce\u08cb\n\u00ce\3\u00cf\3\u00cf\3\u00cf")
        buf.write(u"\2\30$<P\\`l\u00a2\u00ca\u0114\u0138\u0144\u0152\u015c")
        buf.write(u"\u015e\u0162\u016a\u0176\u017c\u017e\u0186\u0192\u0198")
        buf.write(u"\u00d0\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*")
        buf.write(u",.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080")
        buf.write(u"\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092")
        buf.write(u"\u0094\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4")
        buf.write(u"\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4\u00b6")
        buf.write(u"\u00b8\u00ba\u00bc\u00be\u00c0\u00c2\u00c4\u00c6\u00c8")
        buf.write(u"\u00ca\u00cc\u00ce\u00d0\u00d2\u00d4\u00d6\u00d8\u00da")
        buf.write(u"\u00dc\u00de\u00e0\u00e2\u00e4\u00e6\u00e8\u00ea\u00ec")
        buf.write(u"\u00ee\u00f0\u00f2\u00f4\u00f6\u00f8\u00fa\u00fc\u00fe")
        buf.write(u"\u0100\u0102\u0104\u0106\u0108\u010a\u010c\u010e\u0110")
        buf.write(u"\u0112\u0114\u0116\u0118\u011a\u011c\u011e\u0120\u0122")
        buf.write(u"\u0124\u0126\u0128\u012a\u012c\u012e\u0130\u0132\u0134")
        buf.write(u"\u0136\u0138\u013a\u013c\u013e\u0140\u0142\u0144\u0146")
        buf.write(u"\u0148\u014a\u014c\u014e\u0150\u0152\u0154\u0156\u0158")
        buf.write(u"\u015a\u015c\u015e\u0160\u0162\u0164\u0166\u0168\u016a")
        buf.write(u"\u016c\u016e\u0170\u0172\u0174\u0176\u0178\u017a\u017c")
        buf.write(u"\u017e\u0180\u0182\u0184\u0186\u0188\u018a\u018c\u018e")
        buf.write(u"\u0190\u0192\u0194\u0196\u0198\u019a\u019c\2\f\3\2TU")
        buf.write(u"\3\2\"#\4\2\u0090\u0090\u00a4\u00a4\4\2\u008c\u008c\u0094")
        buf.write(u"\u0094\4\2KK\\\\\4\2\'\'vv\b\2\64<\u0086\u0086\u0093")
        buf.write(u"\u0093\u009d\u009d\u00a2\u00a4\u00a6\u00a6\b\2\64<\u0086")
        buf.write(u"\u0086\u008c\u008c\u0093\u0094\u009d\u009d\u00a2\u00a4")
        buf.write(u"\7\2\64<\u0086\u0086\u0093\u0093\u009d\u009d\u00a2\u00a6")
        buf.write(u"\7\2\64<\u0086\u0086\u0093\u0093\u009d\u009d\u00a2\u00a4")
        buf.write(u"\u0946\2\u019e\3\2\2\2\4\u01af\3\2\2\2\6\u01b9\3\2\2")
        buf.write(u"\2\b\u01bd\3\2\2\2\n\u01c5\3\2\2\2\f\u01e1\3\2\2\2\16")
        buf.write(u"\u01e9\3\2\2\2\20\u01ff\3\2\2\2\22\u020c\3\2\2\2\24\u020e")
        buf.write(u"\3\2\2\2\26\u021d\3\2\2\2\30\u0227\3\2\2\2\32\u0234\3")
        buf.write(u"\2\2\2\34\u023e\3\2\2\2\36\u024c\3\2\2\2 \u0260\3\2\2")
        buf.write(u"\2\"\u0272\3\2\2\2$\u027a\3\2\2\2&\u0286\3\2\2\2(\u0292")
        buf.write(u"\3\2\2\2*\u02a2\3\2\2\2,\u02b5\3\2\2\2.\u02c8\3\2\2\2")
        buf.write(u"\60\u02ca\3\2\2\2\62\u02ea\3\2\2\2\64\u02ec\3\2\2\2\66")
        buf.write(u"\u0304\3\2\2\28\u0306\3\2\2\2:\u0312\3\2\2\2<\u0314\3")
        buf.write(u"\2\2\2>\u0324\3\2\2\2@\u0326\3\2\2\2B\u032d\3\2\2\2D")
        buf.write(u"\u0334\3\2\2\2F\u0354\3\2\2\2H\u0356\3\2\2\2J\u0363\3")
        buf.write(u"\2\2\2L\u036c\3\2\2\2N\u0373\3\2\2\2P\u0387\3\2\2\2R")
        buf.write(u"\u039f\3\2\2\2T\u03a2\3\2\2\2V\u03d3\3\2\2\2X\u03d5\3")
        buf.write(u"\2\2\2Z\u03d7\3\2\2\2\\\u03ed\3\2\2\2^\u045a\3\2\2\2")
        buf.write(u"`\u045c\3\2\2\2b\u046e\3\2\2\2d\u047d\3\2\2\2f\u047f")
        buf.write(u"\3\2\2\2h\u0486\3\2\2\2j\u048d\3\2\2\2l\u0499\3\2\2\2")
        buf.write(u"n\u04a3\3\2\2\2p\u04a7\3\2\2\2r\u04ac\3\2\2\2t\u04d0")
        buf.write(u"\3\2\2\2v\u04d2\3\2\2\2x\u04e1\3\2\2\2z\u04ed\3\2\2\2")
        buf.write(u"|\u04ef\3\2\2\2~\u04f6\3\2\2\2\u0080\u04fa\3\2\2\2\u0082")
        buf.write(u"\u04ff\3\2\2\2\u0084\u0508\3\2\2\2\u0086\u050d\3\2\2")
        buf.write(u"\2\u0088\u0510\3\2\2\2\u008a\u0515\3\2\2\2\u008c\u0523")
        buf.write(u"\3\2\2\2\u008e\u052d\3\2\2\2\u0090\u0531\3\2\2\2\u0092")
        buf.write(u"\u0533\3\2\2\2\u0094\u053c\3\2\2\2\u0096\u0545\3\2\2")
        buf.write(u"\2\u0098\u0557\3\2\2\2\u009a\u055a\3\2\2\2\u009c\u0563")
        buf.write(u"\3\2\2\2\u009e\u056b\3\2\2\2\u00a0\u0573\3\2\2\2\u00a2")
        buf.write(u"\u0585\3\2\2\2\u00a4\u0596\3\2\2\2\u00a6\u05a6\3\2\2")
        buf.write(u"\2\u00a8\u05a8\3\2\2\2\u00aa\u05ab\3\2\2\2\u00ac\u05af")
        buf.write(u"\3\2\2\2\u00ae\u05b4\3\2\2\2\u00b0\u05b6\3\2\2\2\u00b2")
        buf.write(u"\u05c0\3\2\2\2\u00b4\u05c5\3\2\2\2\u00b6\u05c7\3\2\2")
        buf.write(u"\2\u00b8\u05c9\3\2\2\2\u00ba\u05cb\3\2\2\2\u00bc\u05cd")
        buf.write(u"\3\2\2\2\u00be\u05cf\3\2\2\2\u00c0\u05dc\3\2\2\2\u00c2")
        buf.write(u"\u05e0\3\2\2\2\u00c4\u05e2\3\2\2\2\u00c6\u05e7\3\2\2")
        buf.write(u"\2\u00c8\u05ec\3\2\2\2\u00ca\u05ee\3\2\2\2\u00cc\u05fc")
        buf.write(u"\3\2\2\2\u00ce\u060a\3\2\2\2\u00d0\u060c\3\2\2\2\u00d2")
        buf.write(u"\u0618\3\2\2\2\u00d4\u0624\3\2\2\2\u00d6\u0626\3\2\2")
        buf.write(u"\2\u00d8\u062a\3\2\2\2\u00da\u0635\3\2\2\2\u00dc\u0639")
        buf.write(u"\3\2\2\2\u00de\u064b\3\2\2\2\u00e0\u0653\3\2\2\2\u00e2")
        buf.write(u"\u065f\3\2\2\2\u00e4\u0661\3\2\2\2\u00e6\u0663\3\2\2")
        buf.write(u"\2\u00e8\u0676\3\2\2\2\u00ea\u0678\3\2\2\2\u00ec\u067f")
        buf.write(u"\3\2\2\2\u00ee\u0686\3\2\2\2\u00f0\u068f\3\2\2\2\u00f2")
        buf.write(u"\u0698\3\2\2\2\u00f4\u06a1\3\2\2\2\u00f6\u06b8\3\2\2")
        buf.write(u"\2\u00f8\u06c8\3\2\2\2\u00fa\u06ca\3\2\2\2\u00fc\u06d6")
        buf.write(u"\3\2\2\2\u00fe\u06d8\3\2\2\2\u0100\u06da\3\2\2\2\u0102")
        buf.write(u"\u06e0\3\2\2\2\u0104\u06e7\3\2\2\2\u0106\u06ea\3\2\2")
        buf.write(u"\2\u0108\u06f3\3\2\2\2\u010a\u06fb\3\2\2\2\u010c\u0707")
        buf.write(u"\3\2\2\2\u010e\u070f\3\2\2\2\u0110\u071c\3\2\2\2\u0112")
        buf.write(u"\u071e\3\2\2\2\u0114\u0722\3\2\2\2\u0116\u0730\3\2\2")
        buf.write(u"\2\u0118\u0732\3\2\2\2\u011a\u0737\3\2\2\2\u011c\u073c")
        buf.write(u"\3\2\2\2\u011e\u0744\3\2\2\2\u0120\u0755\3\2\2\2\u0122")
        buf.write(u"\u0757\3\2\2\2\u0124\u075a\3\2\2\2\u0126\u075d\3\2\2")
        buf.write(u"\2\u0128\u0760\3\2\2\2\u012a\u0763\3\2\2\2\u012c\u0766")
        buf.write(u"\3\2\2\2\u012e\u0768\3\2\2\2\u0130\u076a\3\2\2\2\u0132")
        buf.write(u"\u076c\3\2\2\2\u0134\u076e\3\2\2\2\u0136\u0777\3\2\2")
        buf.write(u"\2\u0138\u0779\3\2\2\2\u013a\u078a\3\2\2\2\u013c\u078c")
        buf.write(u"\3\2\2\2\u013e\u078e\3\2\2\2\u0140\u0796\3\2\2\2\u0142")
        buf.write(u"\u0798\3\2\2\2\u0144\u079f\3\2\2\2\u0146\u07aa\3\2\2")
        buf.write(u"\2\u0148\u07ae\3\2\2\2\u014a\u07b2\3\2\2\2\u014c\u07b9")
        buf.write(u"\3\2\2\2\u014e\u07bb\3\2\2\2\u0150\u07c0\3\2\2\2\u0152")
        buf.write(u"\u07c2\3\2\2\2\u0154\u07d0\3\2\2\2\u0156\u07d8\3\2\2")
        buf.write(u"\2\u0158\u07da\3\2\2\2\u015a\u07e7\3\2\2\2\u015c\u07e9")
        buf.write(u"\3\2\2\2\u015e\u07f4\3\2\2\2\u0160\u0804\3\2\2\2\u0162")
        buf.write(u"\u080b\3\2\2\2\u0164\u081a\3\2\2\2\u0166\u081c\3\2\2")
        buf.write(u"\2\u0168\u0825\3\2\2\2\u016a\u0827\3\2\2\2\u016c\u0836")
        buf.write(u"\3\2\2\2\u016e\u0838\3\2\2\2\u0170\u083a\3\2\2\2\u0172")
        buf.write(u"\u0840\3\2\2\2\u0174\u0842\3\2\2\2\u0176\u0849\3\2\2")
        buf.write(u"\2\u0178\u0854\3\2\2\2\u017a\u0858\3\2\2\2\u017c\u085c")
        buf.write(u"\3\2\2\2\u017e\u0867\3\2\2\2\u0180\u0876\3\2\2\2\u0182")
        buf.write(u"\u0878\3\2\2\2\u0184\u0881\3\2\2\2\u0186\u0883\3\2\2")
        buf.write(u"\2\u0188\u0892\3\2\2\2\u018a\u0894\3\2\2\2\u018c\u0896")
        buf.write(u"\3\2\2\2\u018e\u089c\3\2\2\2\u0190\u089e\3\2\2\2\u0192")
        buf.write(u"\u08a5\3\2\2\2\u0194\u08b0\3\2\2\2\u0196\u08b4\3\2\2")
        buf.write(u"\2\u0198\u08bb\3\2\2\2\u019a\u08ca\3\2\2\2\u019c\u08cc")
        buf.write(u"\3\2\2\2\u019e\u019f\7a\2\2\u019f\u01a0\5\u00ba^\2\u01a0")
        buf.write(u"\u01a7\7\26\2\2\u01a1\u01a4\5\u00ba^\2\u01a2\u01a3\7")
        buf.write(u"\23\2\2\u01a3\u01a5\5\u00e0q\2\u01a4\u01a2\3\2\2\2\u01a4")
        buf.write(u"\u01a5\3\2\2\2\u01a5\u01a8\3\2\2\2\u01a6\u01a8\5\u00e0")
        buf.write(u"q\2\u01a7\u01a1\3\2\2\2\u01a7\u01a6\3\2\2\2\u01a8\u01a9")
        buf.write(u"\3\2\2\2\u01a9\u01aa\7\27\2\2\u01aa\u01ab\7\21\2\2\u01ab")
        buf.write(u"\u01ac\5\u0082B\2\u01ac\u01ad\5\u0094K\2\u01ad\u01ae")
        buf.write(u"\5\u0084C\2\u01ae\3\3\2\2\2\u01af\u01b0\7a\2\2\u01b0")
        buf.write(u"\u01b1\5\u00ba^\2\u01b1\u01b2\7\26\2\2\u01b2\u01b3\5")
        buf.write(u"\u00a6T\2\u01b3\u01b4\7\27\2\2\u01b4\u01b5\7\21\2\2\u01b5")
        buf.write(u"\u01b6\5\u0082B\2\u01b6\u01b7\5\u0092J\2\u01b7\u01b8")
        buf.write(u"\5\u0084C\2\u01b8\5\3\2\2\2\u01b9\u01ba\5\u00bc_\2\u01ba")
        buf.write(u"\u01bb\7-\2\2\u01bb\u01bc\5\\/\2\u01bc\7\3\2\2\2\u01bd")
        buf.write(u"\u01be\5\u00bc_\2\u01be\u01c0\7\26\2\2\u01bf\u01c1\5")
        buf.write(u"l\67\2\u01c0\u01bf\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1")
        buf.write(u"\u01c2\3\2\2\2\u01c2\u01c3\7\27\2\2\u01c3\t\3\2\2\2\u01c4")
        buf.write(u"\u01c6\7\u0090\2\2\u01c5\u01c4\3\2\2\2\u01c5\u01c6\3")
        buf.write(u"\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c8\7L\2\2\u01c8\u01c9")
        buf.write(u"\5\u00b8]\2\u01c9\u01ca\7\26\2\2\u01ca\u01cb\5\u00a2")
        buf.write(u"R\2\u01cb\u01cc\7\27\2\2\u01cc\u01cd\7\21\2\2\u01cd\u01dd")
        buf.write(u"\5\u0082B\2\u01ce\u01de\7\u0084\2\2\u01cf\u01d3\5\u0098")
        buf.write(u"M\2\u01d0\u01d1\5\u0080A\2\u01d1\u01d2\5\f\7\2\u01d2")
        buf.write(u"\u01d4\3\2\2\2\u01d3\u01d0\3\2\2\2\u01d3\u01d4\3\2\2")
        buf.write(u"\2\u01d4\u01dc\3\2\2\2\u01d5\u01d9\5\f\7\2\u01d6\u01d7")
        buf.write(u"\5\u0080A\2\u01d7\u01d8\5\u0098M\2\u01d8\u01da\3\2\2")
        buf.write(u"\2\u01d9\u01d6\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01dc")
        buf.write(u"\3\2\2\2\u01db\u01cf\3\2\2\2\u01db\u01d5\3\2\2\2\u01dc")
        buf.write(u"\u01de\3\2\2\2\u01dd\u01ce\3\2\2\2\u01dd\u01db\3\2\2")
        buf.write(u"\2\u01de\u01df\3\2\2\2\u01df\u01e0\5\u0084C\2\u01e0\13")
        buf.write(u"\3\2\2\2\u01e1\u01e2\7p\2\2\u01e2\u01e4\7\26\2\2\u01e3")
        buf.write(u"\u01e5\5\u00dep\2\u01e4\u01e3\3\2\2\2\u01e4\u01e5\3\2")
        buf.write(u"\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e7\7\27\2\2\u01e7\r")
        buf.write(u"\3\2\2\2\u01e8\u01ea\7\u0090\2\2\u01e9\u01e8\3\2\2\2")
        buf.write(u"\u01e9\u01ea\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ec")
        buf.write(u"\t\2\2\2\u01ec\u01ed\5\u00ba^\2\u01ed\u01f4\7\26\2\2")
        buf.write(u"\u01ee\u01f5\5\22\n\2\u01ef\u01f5\5\u00e0q\2\u01f0\u01f1")
        buf.write(u"\5\22\n\2\u01f1\u01f2\7\23\2\2\u01f2\u01f3\5\u00e0q\2")
        buf.write(u"\u01f3\u01f5\3\2\2\2\u01f4\u01ee\3\2\2\2\u01f4\u01ef")
        buf.write(u"\3\2\2\2\u01f4\u01f0\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6")
        buf.write(u"\u01f7\7\27\2\2\u01f7\u01f8\7\21\2\2\u01f8\u01fb\5\u0082")
        buf.write(u"B\2\u01f9\u01fc\5\u00ccg\2\u01fa\u01fc\7\u0084\2\2\u01fb")
        buf.write(u"\u01f9\3\2\2\2\u01fb\u01fa\3\2\2\2\u01fc\u01fd\3\2\2")
        buf.write(u"\2\u01fd\u01fe\5\u0084C\2\u01fe\17\3\2\2\2\u01ff\u0200")
        buf.write(u"\7\u008e\2\2\u0200\u0201\5\u00ba^\2\u0201\u0202\7\26")
        buf.write(u"\2\2\u0202\u0203\5\u00e0q\2\u0203\u0204\7\27\2\2\u0204")
        buf.write(u"\u0205\7\21\2\2\u0205\u0208\5\u0082B\2\u0206\u0209\5")
        buf.write(u"\u00ccg\2\u0207\u0209\7\u0084\2\2\u0208\u0206\3\2\2\2")
        buf.write(u"\u0208\u0207\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u020b")
        buf.write(u"\5\u0084C\2\u020b\21\3\2\2\2\u020c\u020d\5\u00b0Y\2\u020d")
        buf.write(u"\23\3\2\2\2\u020e\u020f\7X\2\2\u020f\u0210\7\u0080\2")
        buf.write(u"\2\u0210\u0211\5\u0120\u0091\2\u0211\u0212\7\26\2\2\u0212")
        buf.write(u"\u0213\5\u00c2b\2\u0213\u0216\7\27\2\2\u0214\u0215\7")
        buf.write(u"\63\2\2\u0215\u0217\5\u00a2R\2\u0216\u0214\3\2\2\2\u0216")
        buf.write(u"\u0217\3\2\2\2\u0217\u0218\3\2\2\2\u0218\u0219\7\21\2")
        buf.write(u"\2\u0219\u021a\5\u0082B\2\u021a\u021b\5\u00eex\2\u021b")
        buf.write(u"\u021c\5\u0084C\2\u021c\25\3\2\2\2\u021d\u021e\7X\2\2")
        buf.write(u"\u021e\u021f\5\u00b6\\\2\u021f\u0220\7\u008d\2\2\u0220")
        buf.write(u"\u0221\7\26\2\2\u0221\u0222\7\27\2\2\u0222\u0223\7\21")
        buf.write(u"\2\2\u0223\u0224\5\u0082B\2\u0224\u0225\5\u00eex\2\u0225")
        buf.write(u"\u0226\5\u0084C\2\u0226\27\3\2\2\2\u0227\u0228\7X\2\2")
        buf.write(u"\u0228\u022a\5\u00b6\\\2\u0229\u022b\7x\2\2\u022a\u0229")
        buf.write(u"\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022c\3\2\2\2\u022c")
        buf.write(u"\u022d\7\u008d\2\2\u022d\u022e\7\26\2\2\u022e\u022f\7")
        buf.write(u"\27\2\2\u022f\u0230\7\21\2\2\u0230\u0231\5\u0082B\2\u0231")
        buf.write(u"\u0232\5\u00e6t\2\u0232\u0233\5\u0084C\2\u0233\31\3\2")
        buf.write(u"\2\2\u0234\u0235\7X\2\2\u0235\u0236\5\u00b6\\\2\u0236")
        buf.write(u"\u0237\7m\2\2\u0237\u0238\7\26\2\2\u0238\u0239\7\27\2")
        buf.write(u"\2\u0239\u023a\7\21\2\2\u023a\u023b\5\u0082B\2\u023b")
        buf.write(u"\u023c\5\u00eex\2\u023c\u023d\5\u0084C\2\u023d\33\3\2")
        buf.write(u"\2\2\u023e\u023f\7X\2\2\u023f\u0241\5\u00b6\\\2\u0240")
        buf.write(u"\u0242\7x\2\2\u0241\u0240\3\2\2\2\u0241\u0242\3\2\2\2")
        buf.write(u"\u0242\u0243\3\2\2\2\u0243\u0244\7m\2\2\u0244\u0245\7")
        buf.write(u"\26\2\2\u0245\u0246\7\27\2\2\u0246\u0247\7\21\2\2\u0247")
        buf.write(u"\u0248\5\u0082B\2\u0248\u0249\5\u00e6t\2\u0249\u024a")
        buf.write(u"\5\u0084C\2\u024a\35\3\2\2\2\u024b\u024d\7\u0090\2\2")
        buf.write(u"\u024c\u024b\3\2\2\2\u024c\u024d\3\2\2\2\u024d\u024e")
        buf.write(u"\3\2\2\2\u024e\u024f\7x\2\2\u024f\u0250\t\2\2\2\u0250")
        buf.write(u"\u0251\5\u00ba^\2\u0251\u0253\7\26\2\2\u0252\u0254\5")
        buf.write(u"\u00e0q\2\u0253\u0252\3\2\2\2\u0253\u0254\3\2\2\2\u0254")
        buf.write(u"\u0255\3\2\2\2\u0255\u0256\7\27\2\2\u0256\u0257\7\21")
        buf.write(u"\2\2\u0257\u0258\5\u0082B\2\u0258\u025c\5\"\22\2\u0259")
        buf.write(u"\u025a\5\u0080A\2\u025a\u025b\5\u00d0i\2\u025b\u025d")
        buf.write(u"\3\2\2\2\u025c\u0259\3\2\2\2\u025c\u025d\3\2\2\2\u025d")
        buf.write(u"\u025e\3\2\2\2\u025e\u025f\5\u0084C\2\u025f\37\3\2\2")
        buf.write(u"\2\u0260\u0261\7x\2\2\u0261\u0262\7\u0088\2\2\u0262\u0263")
        buf.write(u"\5\u00ba^\2\u0263\u0265\7\26\2\2\u0264\u0266\5\u00e0")
        buf.write(u"q\2\u0265\u0264\3\2\2\2\u0265\u0266\3\2\2\2\u0266\u0267")
        buf.write(u"\3\2\2\2\u0267\u0268\7\27\2\2\u0268\u0269\7\21\2\2\u0269")
        buf.write(u"\u026a\5\u0082B\2\u026a\u026e\5\"\22\2\u026b\u026c\5")
        buf.write(u"\u0080A\2\u026c\u026d\5\u00d0i\2\u026d\u026f\3\2\2\2")
        buf.write(u"\u026e\u026b\3\2\2\2\u026e\u026f\3\2\2\2\u026f\u0270")
        buf.write(u"\3\2\2\2\u0270\u0271\5\u0084C\2\u0271!\3\2\2\2\u0272")
        buf.write(u"\u0273\7X\2\2\u0273\u0274\t\2\2\2\u0274\u0275\7O\2\2")
        buf.write(u"\u0275\u0276\7\21\2\2\u0276\u0277\5\u0082B\2\u0277\u0278")
        buf.write(u"\5$\23\2\u0278\u0279\5\u0084C\2\u0279#\3\2\2\2\u027a")
        buf.write(u"\u027b\b\23\1\2\u027b\u027c\5\u00d4k\2\u027c\u0283\3")
        buf.write(u"\2\2\2\u027d\u027e\f\3\2\2\u027e\u027f\5\u0080A\2\u027f")
        buf.write(u"\u0280\5\u00d4k\2\u0280\u0282\3\2\2\2\u0281\u027d\3\2")
        buf.write(u"\2\2\u0282\u0285\3\2\2\2\u0283\u0281\3\2\2\2\u0283\u0284")
        buf.write(u"\3\2\2\2\u0284%\3\2\2\2\u0285\u0283\3\2\2\2\u0286\u0287")
        buf.write(u"\7E\2\2\u0287\u0288\7X\2\2\u0288\u0289\5\u00b2Z\2\u0289")
        buf.write(u"\u028b\7\26\2\2\u028a\u028c\5\u00be`\2\u028b\u028a\3")
        buf.write(u"\2\2\2\u028b\u028c\3\2\2\2\u028c\u028d\3\2\2\2\u028d")
        buf.write(u"\u0290\7\27\2\2\u028e\u028f\7\63\2\2\u028f\u0291\5\u00a2")
        buf.write(u"R\2\u0290\u028e\3\2\2\2\u0290\u0291\3\2\2\2\u0291\'\3")
        buf.write(u"\2\2\2\u0292\u0293\7X\2\2\u0293\u0294\5\u00b2Z\2\u0294")
        buf.write(u"\u0296\7\26\2\2\u0295\u0297\5\u00be`\2\u0296\u0295\3")
        buf.write(u"\2\2\2\u0296\u0297\3\2\2\2\u0297\u0298\3\2\2\2\u0298")
        buf.write(u"\u029b\7\27\2\2\u0299\u029a\7\63\2\2\u029a\u029c\5\u00a2")
        buf.write(u"R\2\u029b\u0299\3\2\2\2\u029b\u029c\3\2\2\2\u029c\u029d")
        buf.write(u"\3\2\2\2\u029d\u029e\7\21\2\2\u029e\u029f\5\u0082B\2")
        buf.write(u"\u029f\u02a0\5\u00eex\2\u02a0\u02a1\5\u0084C\2\u02a1")
        buf.write(u")\3\2\2\2\u02a2\u02a4\7X\2\2\u02a3\u02a5\7x\2\2\u02a4")
        buf.write(u"\u02a3\3\2\2\2\u02a4\u02a5\3\2\2\2\u02a5\u02a6\3\2\2")
        buf.write(u"\2\u02a6\u02a7\5\u00b2Z\2\u02a7\u02a9\7\26\2\2\u02a8")
        buf.write(u"\u02aa\5\u00be`\2\u02a9\u02a8\3\2\2\2\u02a9\u02aa\3\2")
        buf.write(u"\2\2\u02aa\u02ab\3\2\2\2\u02ab\u02ae\7\27\2\2\u02ac\u02ad")
        buf.write(u"\7\63\2\2\u02ad\u02af\5\u00c8e\2\u02ae\u02ac\3\2\2\2")
        buf.write(u"\u02ae\u02af\3\2\2\2\u02af\u02b0\3\2\2\2\u02b0\u02b1")
        buf.write(u"\7\21\2\2\u02b1\u02b2\5\u0082B\2\u02b2\u02b3\5\u00e6")
        buf.write(u"t\2\u02b3\u02b4\5\u0084C\2\u02b4+\3\2\2\2\u02b5\u02b6")
        buf.write(u"\7X\2\2\u02b6\u02b7\7\u0093\2\2\u02b7\u02b8\7\u00a7\2")
        buf.write(u"\2\u02b8\u02b9\7\26\2\2\u02b9\u02ba\7\27\2\2\u02ba\u02bb")
        buf.write(u"\7\21\2\2\u02bb\u02bc\5\u0082B\2\u02bc\u02bd\5\u00ee")
        buf.write(u"x\2\u02bd\u02be\5\u0084C\2\u02be\u02bf\5\u0080A\2\u02bf")
        buf.write(u"\u02c0\7\u0098\2\2\u02c0\u02c6\7\21\2\2\u02c1\u02c2\5")
        buf.write(u"\u0082B\2\u02c2\u02c3\5\u00f0y\2\u02c3\u02c4\5\u0084")
        buf.write(u"C\2\u02c4\u02c7\3\2\2\2\u02c5\u02c7\5\u00bc_\2\u02c6")
        buf.write(u"\u02c1\3\2\2\2\u02c6\u02c5\3\2\2\2\u02c7-\3\2\2\2\u02c8")
        buf.write(u"\u02c9\5\\/\2\u02c9/\3\2\2\2\u02ca\u02cb\5\u00b6\\\2")
        buf.write(u"\u02cb\u02cc\7\21\2\2\u02cc\u02d1\5\u00c8e\2\u02cd\u02ce")
        buf.write(u"\7\26\2\2\u02ce\u02cf\5\u00e0q\2\u02cf\u02d0\7\27\2\2")
        buf.write(u"\u02d0\u02d2\3\2\2\2\u02d1\u02cd\3\2\2\2\u02d1\u02d2")
        buf.write(u"\3\2\2\2\u02d2\u02d5\3\2\2\2\u02d3\u02d4\7-\2\2\u02d4")
        buf.write(u"\u02d6\5\u0102\u0082\2\u02d5\u02d3\3\2\2\2\u02d5\u02d6")
        buf.write(u"\3\2\2\2\u02d6\61\3\2\2\2\u02d7\u02eb\58\35\2\u02d8\u02eb")
        buf.write(u"\5x=\2\u02d9\u02eb\5|?\2\u02da\u02eb\5\66\34\2\u02db")
        buf.write(u"\u02eb\5\64\33\2\u02dc\u02eb\5X-\2\u02dd\u02eb\5Z.\2")
        buf.write(u"\u02de\u02eb\5N(\2\u02df\u02eb\5D#\2\u02e0\u02eb\5H%")
        buf.write(u"\2\u02e1\u02eb\5L\'\2\u02e2\u02eb\5J&\2\u02e3\u02eb\5")
        buf.write(u"R*\2\u02e4\u02eb\5T+\2\u02e5\u02eb\5p9\2\u02e6\u02eb")
        buf.write(u"\5@!\2\u02e7\u02eb\5B\"\2\u02e8\u02eb\5(\25\2\u02e9\u02eb")
        buf.write(u"\5\u00e4s\2\u02ea\u02d7\3\2\2\2\u02ea\u02d8\3\2\2\2\u02ea")
        buf.write(u"\u02d9\3\2\2\2\u02ea\u02da\3\2\2\2\u02ea\u02db\3\2\2")
        buf.write(u"\2\u02ea\u02dc\3\2\2\2\u02ea\u02dd\3\2\2\2\u02ea\u02de")
        buf.write(u"\3\2\2\2\u02ea\u02df\3\2\2\2\u02ea\u02e0\3\2\2\2\u02ea")
        buf.write(u"\u02e1\3\2\2\2\u02ea\u02e2\3\2\2\2\u02ea\u02e3\3\2\2")
        buf.write(u"\2\u02ea\u02e4\3\2\2\2\u02ea\u02e5\3\2\2\2\u02ea\u02e6")
        buf.write(u"\3\2\2\2\u02ea\u02e7\3\2\2\2\u02ea\u02e8\3\2\2\2\u02ea")
        buf.write(u"\u02e9\3\2\2\2\u02eb\63\3\2\2\2\u02ec\u02ed\7j\2\2\u02ed")
        buf.write(u"\u02ee\7\26\2\2\u02ee\u02ef\7\27\2\2\u02ef\65\3\2\2\2")
        buf.write(u"\u02f0\u02f1\7[\2\2\u02f1\u02f2\7\26\2\2\u02f2\u02f3")
        buf.write(u"\5\u009eP\2\u02f3\u02f4\7\27\2\2\u02f4\u0305\3\2\2\2")
        buf.write(u"\u02f5\u02f6\7\u0091\2\2\u02f6\u02f7\7\26\2\2\u02f7\u02f8")
        buf.write(u"\5\u009eP\2\u02f8\u02f9\7\27\2\2\u02f9\u0305\3\2\2\2")
        buf.write(u"\u02fa\u02fb\7[\2\2\u02fb\u02fc\7\26\2\2\u02fc\u02fd")
        buf.write(u"\5\u009eP\2\u02fd\u02fe\7\27\2\2\u02fe\u02ff\7H\2\2\u02ff")
        buf.write(u"\u0300\7\u0091\2\2\u0300\u0301\7\26\2\2\u0301\u0302\5")
        buf.write(u"\u009eP\2\u0302\u0303\7\27\2\2\u0303\u0305\3\2\2\2\u0304")
        buf.write(u"\u02f0\3\2\2\2\u0304\u02f5\3\2\2\2\u0304\u02fa\3\2\2")
        buf.write(u"\2\u0305\67\3\2\2\2\u0306\u0307\5:\36\2\u0307\u0309\7")
        buf.write(u"\26\2\2\u0308\u030a\5l\67\2\u0309\u0308\3\2\2\2\u0309")
        buf.write(u"\u030a\3\2\2\2\u030a\u030b\3\2\2\2\u030b\u030c\7\27\2")
        buf.write(u"\2\u030c9\3\2\2\2\u030d\u0313\5\u00b2Z\2\u030e\u030f")
        buf.write(u"\5<\37\2\u030f\u0310\7\25\2\2\u0310\u0311\5\u00b2Z\2")
        buf.write(u"\u0311\u0313\3\2\2\2\u0312\u030d\3\2\2\2\u0312\u030e")
        buf.write(u"\3\2\2\2\u0313;\3\2\2\2\u0314\u0315\b\37\1\2\u0315\u0316")
        buf.write(u"\5\u00b4[\2\u0316\u031b\3\2\2\2\u0317\u0318\f\3\2\2\u0318")
        buf.write(u"\u031a\5> \2\u0319\u0317\3\2\2\2\u031a\u031d\3\2\2\2")
        buf.write(u"\u031b\u0319\3\2\2\2\u031b\u031c\3\2\2\2\u031c=\3\2\2")
        buf.write(u"\2\u031d\u031b\3\2\2\2\u031e\u031f\7\25\2\2\u031f\u0325")
        buf.write(u"\5\u00b6\\\2\u0320\u0321\7\30\2\2\u0321\u0322\5\\/\2")
        buf.write(u"\u0322\u0323\7\31\2\2\u0323\u0325\3\2\2\2\u0324\u031e")
        buf.write(u"\3\2\2\2\u0324\u0320\3\2\2\2\u0325?\3\2\2\2\u0326\u0327")
        buf.write(u"\7\u0099\2\2\u0327\u0328\5\u0112\u008a\2\u0328\u0329")
        buf.write(u"\7\21\2\2\u0329\u032a\5\u0082B\2\u032a\u032b\5\u00ee")
        buf.write(u"x\2\u032b\u032c\5\u0084C\2\u032cA\3\2\2\2\u032d\u032e")
        buf.write(u"\7\u0099\2\2\u032e\u032f\5\u00ba^\2\u032f\u0330\7\21")
        buf.write(u"\2\2\u0330\u0331\5\u0082B\2\u0331\u0332\5\u00eex\2\u0332")
        buf.write(u"\u0333\5\u0084C\2\u0333C\3\2\2\2\u0334\u0335\7\u0092")
        buf.write(u"\2\2\u0335\u0336\7}\2\2\u0336\u0337\5\\/\2\u0337\u0338")
        buf.write(u"\7\21\2\2\u0338\u0339\5\u0082B\2\u0339\u0341\5\u00f2")
        buf.write(u"z\2\u033a\u033b\5\u0080A\2\u033b\u033c\7\u0083\2\2\u033c")
        buf.write(u"\u033d\7\21\2\2\u033d\u033e\5\u0082B\2\u033e\u033f\5")
        buf.write(u"\u00eex\2\u033f\u0340\5\u0084C\2\u0340\u0342\3\2\2\2")
        buf.write(u"\u0341\u033a\3\2\2\2\u0341\u0342\3\2\2\2\u0342\u0343")
        buf.write(u"\3\2\2\2\u0343\u0344\5\u0084C\2\u0344E\3\2\2\2\u0345")
        buf.write(u"\u0346\7\u009a\2\2\u0346\u0347\5\u00f8}\2\u0347\u0348")
        buf.write(u"\7\21\2\2\u0348\u0349\5\u0082B\2\u0349\u034a\5\u00ee")
        buf.write(u"x\2\u034a\u034b\5\u0084C\2\u034b\u0355\3\2\2\2\u034c")
        buf.write(u"\u034d\7\u009a\2\2\u034d\u034e\7o\2\2\u034e\u034f\5\u00f6")
        buf.write(u"|\2\u034f\u0350\7\21\2\2\u0350\u0351\5\u0082B\2\u0351")
        buf.write(u"\u0352\5\u00eex\2\u0352\u0353\5\u0084C\2\u0353\u0355")
        buf.write(u"\3\2\2\2\u0354\u0345\3\2\2\2\u0354\u034c\3\2\2\2\u0355")
        buf.write(u"G\3\2\2\2\u0356\u0357\7k\2\2\u0357\u035a\5\u00b6\\\2")
        buf.write(u"\u0358\u0359\7\23\2\2\u0359\u035b\5\u00b6\\\2\u035a\u0358")
        buf.write(u"\3\2\2\2\u035a\u035b\3\2\2\2\u035b\u035c\3\2\2\2\u035c")
        buf.write(u"\u035d\7o\2\2\u035d\u035e\5\\/\2\u035e\u035f\7\21\2\2")
        buf.write(u"\u035f\u0360\5\u0082B\2\u0360\u0361\5\u00eex\2\u0361")
        buf.write(u"\u0362\5\u0084C\2\u0362I\3\2\2\2\u0363\u0364\7]\2\2\u0364")
        buf.write(u"\u0365\7\21\2\2\u0365\u0366\5\u0082B\2\u0366\u0367\5")
        buf.write(u"\u00eex\2\u0367\u0368\5\u0084C\2\u0368\u0369\5\u0080")
        buf.write(u"A\2\u0369\u036a\7\u009c\2\2\u036a\u036b\5\\/\2\u036b")
        buf.write(u"K\3\2\2\2\u036c\u036d\7\u009c\2\2\u036d\u036e\5\\/\2")
        buf.write(u"\u036e\u036f\7\21\2\2\u036f\u0370\5\u0082B\2\u0370\u0371")
        buf.write(u"\5\u00eex\2\u0371\u0372\5\u0084C\2\u0372M\3\2\2\2\u0373")
        buf.write(u"\u0374\7n\2\2\u0374\u0375\5\\/\2\u0375\u0376\7\21\2\2")
        buf.write(u"\u0376\u0377\5\u0082B\2\u0377\u0378\5\u00eex\2\u0378")
        buf.write(u"\u037c\5\u0084C\2\u0379\u037a\5\u0080A\2\u037a\u037b")
        buf.write(u"\5P)\2\u037b\u037d\3\2\2\2\u037c\u0379\3\2\2\2\u037c")
        buf.write(u"\u037d\3\2\2\2\u037d\u0385\3\2\2\2\u037e\u037f\5\u0080")
        buf.write(u"A\2\u037f\u0380\7`\2\2\u0380\u0381\7\21\2\2\u0381\u0382")
        buf.write(u"\5\u0082B\2\u0382\u0383\5\u00eex\2\u0383\u0384\5\u0084")
        buf.write(u"C\2\u0384\u0386\3\2\2\2\u0385\u037e\3\2\2\2\u0385\u0386")
        buf.write(u"\3\2\2\2\u0386O\3\2\2\2\u0387\u0388\b)\1\2\u0388\u0389")
        buf.write(u"\7`\2\2\u0389\u038a\7n\2\2\u038a\u038b\5\\/\2\u038b\u038c")
        buf.write(u"\7\21\2\2\u038c\u038d\5\u0082B\2\u038d\u038e\5\u00ee")
        buf.write(u"x\2\u038e\u038f\5\u0084C\2\u038f\u039c\3\2\2\2\u0390")
        buf.write(u"\u0391\f\3\2\2\u0391\u0392\5\u0080A\2\u0392\u0393\7`")
        buf.write(u"\2\2\u0393\u0394\7n\2\2\u0394\u0395\5\\/\2\u0395\u0396")
        buf.write(u"\7\21\2\2\u0396\u0397\5\u0082B\2\u0397\u0398\5\u00ee")
        buf.write(u"x\2\u0398\u0399\5\u0084C\2\u0399\u039b\3\2\2\2\u039a")
        buf.write(u"\u0390\3\2\2\2\u039b\u039e\3\2\2\2\u039c\u039a\3\2\2")
        buf.write(u"\2\u039c\u039d\3\2\2\2\u039dQ\3\2\2\2\u039e\u039c\3\2")
        buf.write(u"\2\2\u039f\u03a0\7\u0085\2\2\u03a0\u03a1\5\\/\2\u03a1")
        buf.write(u"S\3\2\2\2\u03a2\u03a3\7\u0097\2\2\u03a3\u03a4\5\u00b6")
        buf.write(u"\\\2\u03a4\u03a5\7\21\2\2\u03a5\u03a6\5\u0082B\2\u03a6")
        buf.write(u"\u03a7\5\u00eex\2\u03a7\u03a8\5\u0084C\2\u03a8\u03aa")
        buf.write(u"\5~@\2\u03a9\u03ab\5\u00f4{\2\u03aa\u03a9\3\2\2\2\u03aa")
        buf.write(u"\u03ab\3\2\2\2\u03ab\u03b3\3\2\2\2\u03ac\u03ad\7c\2\2")
        buf.write(u"\u03ad\u03ae\7\21\2\2\u03ae\u03af\5\u0082B\2\u03af\u03b0")
        buf.write(u"\5\u00eex\2\u03b0\u03b1\5\u0084C\2\u03b1\u03b2\5~@\2")
        buf.write(u"\u03b2\u03b4\3\2\2\2\u03b3\u03ac\3\2\2\2\u03b3\u03b4")
        buf.write(u"\3\2\2\2\u03b4\u03bc\3\2\2\2\u03b5\u03b6\7i\2\2\u03b6")
        buf.write(u"\u03b7\7\21\2\2\u03b7\u03b8\5\u0082B\2\u03b8\u03b9\5")
        buf.write(u"\u00eex\2\u03b9\u03ba\5\u0084C\2\u03ba\u03bb\5~@\2\u03bb")
        buf.write(u"\u03bd\3\2\2\2\u03bc\u03b5\3\2\2\2\u03bc\u03bd\3\2\2")
        buf.write(u"\2\u03bd\u03be\3\2\2\2\u03be\u03bf\5~@\2\u03bfU\3\2\2")
        buf.write(u"\2\u03c0\u03c1\7c\2\2\u03c1\u03c2\5\u00bc_\2\u03c2\u03c3")
        buf.write(u"\7\21\2\2\u03c3\u03c4\5\u0082B\2\u03c4\u03c5\5\u00ee")
        buf.write(u"x\2\u03c5\u03c6\5\u0084C\2\u03c6\u03c7\5~@\2\u03c7\u03d4")
        buf.write(u"\3\2\2\2\u03c8\u03c9\7c\2\2\u03c9\u03ca\7o\2\2\u03ca")
        buf.write(u"\u03cb\7\30\2\2\u03cb\u03cc\5\u0096L\2\u03cc\u03cd\7")
        buf.write(u"\31\2\2\u03cd\u03ce\7\21\2\2\u03ce\u03cf\5\u0082B\2\u03cf")
        buf.write(u"\u03d0\5\u00eex\2\u03d0\u03d1\5\u0084C\2\u03d1\u03d2")
        buf.write(u"\5~@\2\u03d2\u03d4\3\2\2\2\u03d3\u03c0\3\2\2\2\u03d3")
        buf.write(u"\u03c8\3\2\2\2\u03d4W\3\2\2\2\u03d5\u03d6\7P\2\2\u03d6")
        buf.write(u"Y\3\2\2\2\u03d7\u03d9\7\u0089\2\2\u03d8\u03da\5\\/\2")
        buf.write(u"\u03d9\u03d8\3\2\2\2\u03d9\u03da\3\2\2\2\u03da[\3\2\2")
        buf.write(u"\2\u03db\u03dc\b/\1\2\u03dc\u03dd\7#\2\2\u03dd\u03ee")
        buf.write(u"\5\\/\"\u03de\u03df\7z\2\2\u03df\u03ee\5\\/!\u03e0\u03ee")
        buf.write(u"\5`\61\2\u03e1\u03ee\5b\62\2\u03e2\u03e3\7>\2\2\u03e3")
        buf.write(u"\u03e4\7\26\2\2\u03e4\u03e5\5\\/\2\u03e5\u03e6\7\27\2")
        buf.write(u"\2\u03e6\u03ee\3\2\2\2\u03e7\u03e8\7d\2\2\u03e8\u03e9")
        buf.write(u"\7\26\2\2\u03e9\u03ea\5\u00b6\\\2\u03ea\u03eb\7\27\2")
        buf.write(u"\2\u03eb\u03ee\3\2\2\2\u03ec\u03ee\5^\60\2\u03ed\u03db")
        buf.write(u"\3\2\2\2\u03ed\u03de\3\2\2\2\u03ed\u03e0\3\2\2\2\u03ed")
        buf.write(u"\u03e1\3\2\2\2\u03ed\u03e2\3\2\2\2\u03ed\u03e7\3\2\2")
        buf.write(u"\2\u03ed\u03ec\3\2\2\2\u03ee\u0457\3\2\2\2\u03ef\u03f0")
        buf.write(u"\f \2\2\u03f0\u03f1\5\u012e\u0098\2\u03f1\u03f2\5\\/")
        buf.write(u"!\u03f2\u0456\3\2\2\2\u03f3\u03f4\f\37\2\2\u03f4\u03f5")
        buf.write(u"\5\u0130\u0099\2\u03f5\u03f6\5\\/ \u03f6\u0456\3\2\2")
        buf.write(u"\2\u03f7\u03f8\f\36\2\2\u03f8\u03f9\5\u0134\u009b\2\u03f9")
        buf.write(u"\u03fa\5\\/\37\u03fa\u0456\3\2\2\2\u03fb\u03fc\f\35\2")
        buf.write(u"\2\u03fc\u03fd\5\u0132\u009a\2\u03fd\u03fe\5\\/\36\u03fe")
        buf.write(u"\u0456\3\2\2\2\u03ff\u0400\f\34\2\2\u0400\u0401\t\3\2")
        buf.write(u"\2\u0401\u0456\5\\/\35\u0402\u0403\f\33\2\2\u0403\u0404")
        buf.write(u"\7*\2\2\u0404\u0456\5\\/\34\u0405\u0406\f\32\2\2\u0406")
        buf.write(u"\u0407\7+\2\2\u0407\u0456\5\\/\33\u0408\u0409\f\31\2")
        buf.write(u"\2\u0409\u040a\7(\2\2\u040a\u0456\5\\/\32\u040b\u040c")
        buf.write(u"\f\30\2\2\u040c\u040d\7)\2\2\u040d\u0456\5\\/\31\u040e")
        buf.write(u"\u040f\f\25\2\2\u040f\u0410\7/\2\2\u0410\u0456\5\\/\26")
        buf.write(u"\u0411\u0412\f\24\2\2\u0412\u0413\7.\2\2\u0413\u0456")
        buf.write(u"\5\\/\25\u0414\u0415\f\23\2\2\u0415\u0416\7\60\2\2\u0416")
        buf.write(u"\u0456\5\\/\24\u0417\u0418\f\22\2\2\u0418\u0419\7\u0081")
        buf.write(u"\2\2\u0419\u0456\5\\/\23\u041a\u041b\f\21\2\2\u041b\u041c")
        buf.write(u"\7H\2\2\u041c\u0456\5\\/\22\u041d\u041e\f\20\2\2\u041e")
        buf.write(u"\u041f\7n\2\2\u041f\u0420\5\\/\2\u0420\u0421\7`\2\2\u0421")
        buf.write(u"\u0422\5\\/\21\u0422\u0456\3\2\2\2\u0423\u0424\f\16\2")
        buf.write(u"\2\u0424\u0425\7o\2\2\u0425\u0456\5\\/\17\u0426\u0427")
        buf.write(u"\f\r\2\2\u0427\u0428\7W\2\2\u0428\u0456\5\\/\16\u0429")
        buf.write(u"\u042a\f\f\2\2\u042a\u042b\7W\2\2\u042b\u042c\7F\2\2")
        buf.write(u"\u042c\u0456\5\\/\r\u042d\u042e\f\13\2\2\u042e\u042f")
        buf.write(u"\7W\2\2\u042f\u0430\7I\2\2\u0430\u0456\5\\/\f\u0431\u0432")
        buf.write(u"\f\n\2\2\u0432\u0433\7z\2\2\u0433\u0434\7o\2\2\u0434")
        buf.write(u"\u0456\5\\/\13\u0435\u0436\f\t\2\2\u0436\u0437\7z\2\2")
        buf.write(u"\u0437\u0438\7W\2\2\u0438\u0456\5\\/\n\u0439\u043a\f")
        buf.write(u"\b\2\2\u043a\u043b\7z\2\2\u043b\u043c\7W\2\2\u043c\u043d")
        buf.write(u"\7F\2\2\u043d\u0456\5\\/\t\u043e\u043f\f\7\2\2\u043f")
        buf.write(u"\u0440\7z\2\2\u0440\u0441\7W\2\2\u0441\u0442\7I\2\2\u0442")
        buf.write(u"\u0456\5\\/\b\u0443\u0444\f\3\2\2\u0444\u0445\7k\2\2")
        buf.write(u"\u0445\u0446\5\u00b6\\\2\u0446\u0447\7o\2\2\u0447\u0448")
        buf.write(u"\5\\/\4\u0448\u0456\3\2\2\2\u0449\u044a\f$\2\2\u044a")
        buf.write(u"\u0456\5r:\2\u044b\u044c\f\27\2\2\u044c\u044d\7r\2\2")
        buf.write(u"\u044d\u044e\7z\2\2\u044e\u0456\5\u0116\u008c\2\u044f")
        buf.write(u"\u0450\f\26\2\2\u0450\u0451\7r\2\2\u0451\u0456\5\u0116")
        buf.write(u"\u008c\2\u0452\u0453\f\17\2\2\u0453\u0454\7J\2\2\u0454")
        buf.write(u"\u0456\5\u00c8e\2\u0455\u03ef\3\2\2\2\u0455\u03f3\3\2")
        buf.write(u"\2\2\u0455\u03f7\3\2\2\2\u0455\u03fb\3\2\2\2\u0455\u03ff")
        buf.write(u"\3\2\2\2\u0455\u0402\3\2\2\2\u0455\u0405\3\2\2\2\u0455")
        buf.write(u"\u0408\3\2\2\2\u0455\u040b\3\2\2\2\u0455\u040e\3\2\2")
        buf.write(u"\2\u0455\u0411\3\2\2\2\u0455\u0414\3\2\2\2\u0455\u0417")
        buf.write(u"\3\2\2\2\u0455\u041a\3\2\2\2\u0455\u041d\3\2\2\2\u0455")
        buf.write(u"\u0423\3\2\2\2\u0455\u0426\3\2\2\2\u0455\u0429\3\2\2")
        buf.write(u"\2\u0455\u042d\3\2\2\2\u0455\u0431\3\2\2\2\u0455\u0435")
        buf.write(u"\3\2\2\2\u0455\u0439\3\2\2\2\u0455\u043e\3\2\2\2\u0455")
        buf.write(u"\u0443\3\2\2\2\u0455\u0449\3\2\2\2\u0455\u044b\3\2\2")
        buf.write(u"\2\u0455\u044f\3\2\2\2\u0455\u0452\3\2\2\2\u0456\u0459")
        buf.write(u"\3\2\2\2\u0457\u0455\3\2\2\2\u0457\u0458\3\2\2\2\u0458")
        buf.write(u"]\3\2\2\2\u0459\u0457\3\2\2\2\u045a\u045b\5\u00ba^\2")
        buf.write(u"\u045b_\3\2\2\2\u045c\u045d\b\61\1\2\u045d\u045e\5\u00fc")
        buf.write(u"\177\2\u045e\u0463\3\2\2\2\u045f\u0460\f\3\2\2\u0460")
        buf.write(u"\u0462\5d\63\2\u0461\u045f\3\2\2\2\u0462\u0465\3\2\2")
        buf.write(u"\2\u0463\u0461\3\2\2\2\u0463\u0464\3\2\2\2\u0464a\3\2")
        buf.write(u"\2\2\u0465\u0463\3\2\2\2\u0466\u046f\5f\64\2\u0467\u046f")
        buf.write(u"\5h\65\2\u0468\u046f\5t;\2\u0469\u046f\5\u0118\u008d")
        buf.write(u"\2\u046a\u046f\5\u011a\u008e\2\u046b\u046f\5v<\2\u046c")
        buf.write(u"\u046f\58\35\2\u046d\u046f\5j\66\2\u046e\u0466\3\2\2")
        buf.write(u"\2\u046e\u0467\3\2\2\2\u046e\u0468\3\2\2\2\u046e\u0469")
        buf.write(u"\3\2\2\2\u046e\u046a\3\2\2\2\u046e\u046b\3\2\2\2\u046e")
        buf.write(u"\u046c\3\2\2\2\u046e\u046d\3\2\2\2\u046fc\3\2\2\2\u0470")
        buf.write(u"\u0471\6\63\"\3\u0471\u0472\7\25\2\2\u0472\u047e\5\u00b6")
        buf.write(u"\\\2\u0473\u0474\6\63#\3\u0474\u0475\7\30\2\2\u0475\u0476")
        buf.write(u"\5\u0110\u0089\2\u0476\u0477\7\31\2\2\u0477\u047e\3\2")
        buf.write(u"\2\2\u0478\u0479\6\63$\3\u0479\u047a\7\30\2\2\u047a\u047b")
        buf.write(u"\5\\/\2\u047b\u047c\7\31\2\2\u047c\u047e\3\2\2\2\u047d")
        buf.write(u"\u0470\3\2\2\2\u047d\u0473\3\2\2\2\u047d\u0478\3\2\2")
        buf.write(u"\2\u047ee\3\2\2\2\u047f\u0480\7@\2\2\u0480\u0482\7\26")
        buf.write(u"\2\2\u0481\u0483\5\\/\2\u0482\u0481\3\2\2\2\u0482\u0483")
        buf.write(u"\3\2\2\2\u0483\u0484\3\2\2\2\u0484\u0485\7\27\2\2\u0485")
        buf.write(u"g\3\2\2\2\u0486\u0487\7?\2\2\u0487\u0489\7\26\2\2\u0488")
        buf.write(u"\u048a\5\\/\2\u0489\u0488\3\2\2\2\u0489\u048a\3\2\2\2")
        buf.write(u"\u048a\u048b\3\2\2\2\u048b\u048c\7\27\2\2\u048ci\3\2")
        buf.write(u"\2\2\u048d\u048e\5\u00aaV\2\u048e\u0490\7\26\2\2\u048f")
        buf.write(u"\u0491\5l\67\2\u0490\u048f\3\2\2\2\u0490\u0491\3\2\2")
        buf.write(u"\2\u0491\u0492\3\2\2\2\u0492\u0493\7\27\2\2\u0493k\3")
        buf.write(u"\2\2\2\u0494\u0495\b\67\1\2\u0495\u0496\5\\/\2\u0496")
        buf.write(u"\u0497\6\67%\3\u0497\u049a\3\2\2\2\u0498\u049a\5n8\2")
        buf.write(u"\u0499\u0494\3\2\2\2\u0499\u0498\3\2\2\2\u049a\u04a0")
        buf.write(u"\3\2\2\2\u049b\u049c\f\3\2\2\u049c\u049d\7\23\2\2\u049d")
        buf.write(u"\u049f\5n8\2\u049e\u049b\3\2\2\2\u049f\u04a2\3\2\2\2")
        buf.write(u"\u04a0\u049e\3\2\2\2\u04a0\u04a1\3\2\2\2\u04a1m\3\2\2")
        buf.write(u"\2\u04a2\u04a0\3\2\2\2\u04a3\u04a4\5\u00b6\\\2\u04a4")
        buf.write(u"\u04a5\5\u012c\u0097\2\u04a5\u04a6\5\\/\2\u04a6o\3\2")
        buf.write(u"\2\2\u04a7\u04a8\7\u009d\2\2\u04a8\u04a9\5\\/\2\u04a9")
        buf.write(u"\u04aa\7\u0096\2\2\u04aa\u04ab\5\\/\2\u04abq\3\2\2\2")
        buf.write(u"\u04ac\u04ad\7h\2\2\u04ad\u04ae\7\u0099\2\2\u04ae\u04af")
        buf.write(u"\5\u00b6\\\2\u04af\u04b0\7\u009b\2\2\u04b0\u04b1\5\\")
        buf.write(u"/\2\u04b1s\3\2\2\2\u04b2\u04b3\7g\2\2\u04b3\u04b5\7~")
        buf.write(u"\2\2\u04b4\u04b6\5\u00aaV\2\u04b5\u04b4\3\2\2\2\u04b5")
        buf.write(u"\u04b6\3\2\2\2\u04b6\u04b7\3\2\2\2\u04b7\u04b8\7\u009b")
        buf.write(u"\2\2\u04b8\u04d1\5\\/\2\u04b9\u04c0\7g\2\2\u04ba\u04c1")
        buf.write(u"\7F\2\2\u04bb\u04bc\7\u008b\2\2\u04bc\u04bd\5\\/\2\u04bd")
        buf.write(u"\u04be\7\u0096\2\2\u04be\u04bf\5\\/\2\u04bf\u04c1\3\2")
        buf.write(u"\2\2\u04c0\u04ba\3\2\2\2\u04c0\u04bb\3\2\2\2\u04c1\u04c2")
        buf.write(u"\3\2\2\2\u04c2\u04c4\7\26\2\2\u04c3\u04c5\5\u00aaV\2")
        buf.write(u"\u04c4\u04c3\3\2\2\2\u04c4\u04c5\3\2\2\2\u04c5\u04c6")
        buf.write(u"\3\2\2\2\u04c6\u04c9\7\27\2\2\u04c7\u04c8\7\u009b\2\2")
        buf.write(u"\u04c8\u04ca\5\\/\2\u04c9\u04c7\3\2\2\2\u04c9\u04ca\3")
        buf.write(u"\2\2\2\u04ca\u04ce\3\2\2\2\u04cb\u04cc\7\u0082\2\2\u04cc")
        buf.write(u"\u04cd\7Q\2\2\u04cd\u04cf\5\u011c\u008f\2\u04ce\u04cb")
        buf.write(u"\3\2\2\2\u04ce\u04cf\3\2\2\2\u04cf\u04d1\3\2\2\2\u04d0")
        buf.write(u"\u04b2\3\2\2\2\u04d0\u04b9\3\2\2\2\u04d1u\3\2\2\2\u04d2")
        buf.write(u"\u04d4\7\u008f\2\2\u04d3\u04d5\7\\\2\2\u04d4\u04d3\3")
        buf.write(u"\2\2\2\u04d4\u04d5\3\2\2\2\u04d5\u04d6\3\2\2\2\u04d6")
        buf.write(u"\u04d7\7\26\2\2\u04d7\u04dd\5`\61\2\u04d8\u04d9\7\23")
        buf.write(u"\2\2\u04d9\u04da\5\u0124\u0093\2\u04da\u04db\7-\2\2\u04db")
        buf.write(u"\u04dc\5`\61\2\u04dc\u04de\3\2\2\2\u04dd\u04d8\3\2\2")
        buf.write(u"\2\u04dd\u04de\3\2\2\2\u04de\u04df\3\2\2\2\u04df\u04e0")
        buf.write(u"\7\27\2\2\u04e0w\3\2\2\2\u04e1\u04e2\5\u0114\u008b\2")
        buf.write(u"\u04e2\u04e3\5\u012c\u0097\2\u04e3\u04e4\5\\/\2\u04e4")
        buf.write(u"y\3\2\2\2\u04e5\u04e6\6>\'\3\u04e6\u04e7\7\25\2\2\u04e7")
        buf.write(u"\u04ee\5\u00b6\\\2\u04e8\u04e9\6>(\3\u04e9\u04ea\7\30")
        buf.write(u"\2\2\u04ea\u04eb\5\\/\2\u04eb\u04ec\7\31\2\2\u04ec\u04ee")
        buf.write(u"\3\2\2\2\u04ed\u04e5\3\2\2\2\u04ed\u04e8\3\2\2\2\u04ee")
        buf.write(u"{\3\2\2\2\u04ef\u04f0\5\u00dep\2\u04f0\u04f1\5\u012c")
        buf.write(u"\u0097\2\u04f1\u04f2\5\\/\2\u04f2}\3\2\2\2\u04f3\u04f5")
        buf.write(u"\7\7\2\2\u04f4\u04f3\3\2\2\2\u04f5\u04f8\3\2\2\2\u04f6")
        buf.write(u"\u04f4\3\2\2\2\u04f6\u04f7\3\2\2\2\u04f7\177\3\2\2\2")
        buf.write(u"\u04f8\u04f6\3\2\2\2\u04f9\u04fb\7\7\2\2\u04fa\u04f9")
        buf.write(u"\3\2\2\2\u04fb\u04fc\3\2\2\2\u04fc\u04fa\3\2\2\2\u04fc")
        buf.write(u"\u04fd\3\2\2\2\u04fd\u0081\3\2\2\2\u04fe\u0500\7\7\2")
        buf.write(u"\2\u04ff\u04fe\3\2\2\2\u0500\u0501\3\2\2\2\u0501\u04ff")
        buf.write(u"\3\2\2\2\u0501\u0502\3\2\2\2\u0502\u0503\3\2\2\2\u0503")
        buf.write(u"\u0504\7\3\2\2\u0504\u0083\3\2\2\2\u0505\u0507\7\7\2")
        buf.write(u"\2\u0506\u0505\3\2\2\2\u0507\u050a\3\2\2\2\u0508\u0506")
        buf.write(u"\3\2\2\2\u0508\u0509\3\2\2\2\u0509\u050b\3\2\2\2\u050a")
        buf.write(u"\u0508\3\2\2\2\u050b\u050c\7\4\2\2\u050c\u0085\3\2\2")
        buf.write(u"\2\u050d\u050e\7y\2\2\u050e\u0087\3\2\2\2\u050f\u0511")
        buf.write(u"\5\u008aF\2\u0510\u050f\3\2\2\2\u0510\u0511\3\2\2\2\u0511")
        buf.write(u"\u0512\3\2\2\2\u0512\u0513\5~@\2\u0513\u0514\7\2\2\3")
        buf.write(u"\u0514\u0089\3\2\2\2\u0515\u051b\5\u008cG\2\u0516\u0517")
        buf.write(u"\5\u0080A\2\u0517\u0518\5\u008cG\2\u0518\u051a\3\2\2")
        buf.write(u"\2\u0519\u0516\3\2\2\2\u051a\u051d\3\2\2\2\u051b\u0519")
        buf.write(u"\3\2\2\2\u051b\u051c\3\2\2\2\u051c\u008b\3\2\2\2\u051d")
        buf.write(u"\u051b\3\2\2\2\u051e\u051f\5\u00e4s\2\u051f\u0520\5\u0080")
        buf.write(u"A\2\u0520\u0522\3\2\2\2\u0521\u051e\3\2\2\2\u0522\u0525")
        buf.write(u"\3\2\2\2\u0523\u0521\3\2\2\2\u0523\u0524\3\2\2\2\u0524")
        buf.write(u"\u052b\3\2\2\2\u0525\u0523\3\2\2\2\u0526\u052c\5\n\6")
        buf.write(u"\2\u0527\u052c\5\u00aeX\2\u0528\u052c\5\u008eH\2\u0529")
        buf.write(u"\u052c\5\u0090I\2\u052a\u052c\5\u00e2r\2\u052b\u0526")
        buf.write(u"\3\2\2\2\u052b\u0527\3\2\2\2\u052b\u0528\3\2\2\2\u052b")
        buf.write(u"\u0529\3\2\2\2\u052b\u052a\3\2\2\2\u052c\u008d\3\2\2")
        buf.write(u"\2\u052d\u052e\5 \21\2\u052e\u008f\3\2\2\2\u052f\u0532")
        buf.write(u"\5\2\2\2\u0530\u0532\5\4\3\2\u0531\u052f\3\2\2\2\u0531")
        buf.write(u"\u0530\3\2\2\2\u0532\u0091\3\2\2\2\u0533\u0539\5\6\4")
        buf.write(u"\2\u0534\u0535\5\u0080A\2\u0535\u0536\5\6\4\2\u0536\u0538")
        buf.write(u"\3\2\2\2\u0537\u0534\3\2\2\2\u0538\u053b\3\2\2\2\u0539")
        buf.write(u"\u0537\3\2\2\2\u0539\u053a\3\2\2\2\u053a\u0093\3\2\2")
        buf.write(u"\2\u053b\u0539\3\2\2\2\u053c\u0542\5\b\5\2\u053d\u053e")
        buf.write(u"\5\u0080A\2\u053e\u053f\5\b\5\2\u053f\u0541\3\2\2\2\u0540")
        buf.write(u"\u053d\3\2\2\2\u0541\u0544\3\2\2\2\u0542\u0540\3\2\2")
        buf.write(u"\2\u0542\u0543\3\2\2\2\u0543\u0095\3\2\2\2\u0544\u0542")
        buf.write(u"\3\2\2\2\u0545\u054a\5\u00bc_\2\u0546\u0547\7\23\2\2")
        buf.write(u"\u0547\u0549\5\u00bc_\2\u0548\u0546\3\2\2\2\u0549\u054c")
        buf.write(u"\3\2\2\2\u054a\u0548\3\2\2\2\u054a\u054b\3\2\2\2\u054b")
        buf.write(u"\u0097\3\2\2\2\u054c\u054a\3\2\2\2\u054d\u054e\7o\2\2")
        buf.write(u"\u054e\u0558\5\u009aN\2\u054f\u0550\7o\2\2\u0550\u0558")
        buf.write(u"\5\u009cO\2\u0551\u0552\7o\2\2\u0552\u0558\5\u00a0Q\2")
        buf.write(u"\u0553\u0554\7s\2\2\u0554\u0558\7\u00a7\2\2\u0555\u0556")
        buf.write(u"\7s\2\2\u0556\u0558\5\\/\2\u0557\u054d\3\2\2\2\u0557")
        buf.write(u"\u054f\3\2\2\2\u0557\u0551\3\2\2\2\u0557\u0553\3\2\2")
        buf.write(u"\2\u0557\u0555\3\2\2\2\u0558\u0099\3\2\2\2\u0559\u055b")
        buf.write(u"\7w\2\2\u055a\u0559\3\2\2\2\u055a\u055b\3\2\2\2\u055b")
        buf.write(u"\u055c\3\2\2\2\u055c\u055e\7\30\2\2\u055d\u055f\5\u009e")
        buf.write(u"P\2\u055e\u055d\3\2\2\2\u055e\u055f\3\2\2\2\u055f\u0560")
        buf.write(u"\3\2\2\2\u0560\u0561\7\31\2\2\u0561\u009b\3\2\2\2\u0562")
        buf.write(u"\u0564\7w\2\2\u0563\u0562\3\2\2\2\u0563\u0564\3\2\2\2")
        buf.write(u"\u0564\u0565\3\2\2\2\u0565\u0567\7*\2\2\u0566\u0568\5")
        buf.write(u"\u009eP\2\u0567\u0566\3\2\2\2\u0567\u0568\3\2\2\2\u0568")
        buf.write(u"\u0569\3\2\2\2\u0569\u056a\7(\2\2\u056a\u009d\3\2\2\2")
        buf.write(u"\u056b\u0570\5\\/\2\u056c\u056d\7\23\2\2\u056d\u056f")
        buf.write(u"\5\\/\2\u056e\u056c\3\2\2\2\u056f\u0572\3\2\2\2\u0570")
        buf.write(u"\u056e\3\2\2\2\u0570\u0571\3\2\2\2\u0571\u009f\3\2\2")
        buf.write(u"\2\u0572\u0570\3\2\2\2\u0573\u0574\7\30\2\2\u0574\u0575")
        buf.write(u"\5\\/\2\u0575\u0576\7\24\2\2\u0576\u0577\5\\/\2\u0577")
        buf.write(u"\u0578\7\31\2\2\u0578\u00a1\3\2\2\2\u0579\u057a\bR\1")
        buf.write(u"\2\u057a\u0586\5\u00a4S\2\u057b\u057c\7D\2\2\u057c\u057d")
        buf.write(u"\7*\2\2\u057d\u057e\5\u00a2R\2\u057e\u057f\7(\2\2\u057f")
        buf.write(u"\u0586\3\2\2\2\u0580\u0581\7C\2\2\u0581\u0582\7*\2\2")
        buf.write(u"\u0582\u0583\5\u00a2R\2\u0583\u0584\7(\2\2\u0584\u0586")
        buf.write(u"\3\2\2\2\u0585\u0579\3\2\2\2\u0585\u057b\3\2\2\2\u0585")
        buf.write(u"\u0580\3\2\2\2\u0586\u0591\3\2\2\2\u0587\u0588\f\7\2")
        buf.write(u"\2\u0588\u0590\7,\2\2\u0589\u058a\f\6\2\2\u058a\u058b")
        buf.write(u"\7\30\2\2\u058b\u0590\7\31\2\2\u058c\u058d\f\5\2\2\u058d")
        buf.write(u"\u058e\7\32\2\2\u058e\u0590\7\33\2\2\u058f\u0587\3\2")
        buf.write(u"\2\2\u058f\u0589\3\2\2\2\u058f\u058c\3\2\2\2\u0590\u0593")
        buf.write(u"\3\2\2\2\u0591\u058f\3\2\2\2\u0591\u0592\3\2\2\2\u0592")
        buf.write(u"\u00a3\3\2\2\2\u0593\u0591\3\2\2\2\u0594\u0597\5\u00a6")
        buf.write(u"T\2\u0595\u0597\5\u00a8U\2\u0596\u0594\3\2\2\2\u0596")
        buf.write(u"\u0595\3\2\2\2\u0597\u00a5\3\2\2\2\u0598\u05a7\7\64\2")
        buf.write(u"\2\u0599\u05a7\7\65\2\2\u059a\u05a7\7\66\2\2\u059b\u05a7")
        buf.write(u"\7A\2\2\u059c\u05a7\7\67\2\2\u059d\u05a7\78\2\2\u059e")
        buf.write(u"\u05a7\7?\2\2\u059f\u05a7\79\2\2\u05a0\u05a7\7;\2\2\u05a1")
        buf.write(u"\u05a7\7:\2\2\u05a2\u05a7\7<\2\2\u05a3\u05a7\7>\2\2\u05a4")
        buf.write(u"\u05a7\7@\2\2\u05a5\u05a7\7B\2\2\u05a6\u0598\3\2\2\2")
        buf.write(u"\u05a6\u0599\3\2\2\2\u05a6\u059a\3\2\2\2\u05a6\u059b")
        buf.write(u"\3\2\2\2\u05a6\u059c\3\2\2\2\u05a6\u059d\3\2\2\2\u05a6")
        buf.write(u"\u059e\3\2\2\2\u05a6\u059f\3\2\2\2\u05a6\u05a0\3\2\2")
        buf.write(u"\2\u05a6\u05a1\3\2\2\2\u05a6\u05a2\3\2\2\2\u05a6\u05a3")
        buf.write(u"\3\2\2\2\u05a6\u05a4\3\2\2\2\u05a6\u05a5\3\2\2\2\u05a7")
        buf.write(u"\u00a7\3\2\2\2\u05a8\u05a9\7\u00a3\2\2\u05a9\u00a9\3")
        buf.write(u"\2\2\2\u05aa\u05ac\7w\2\2\u05ab\u05aa\3\2\2\2\u05ab\u05ac")
        buf.write(u"\3\2\2\2\u05ac\u05ad\3\2\2\2\u05ad\u05ae\5\u00a8U\2\u05ae")
        buf.write(u"\u00ab\3\2\2\2\u05af\u05b0\7>\2\2\u05b0\u00ad\3\2\2\2")
        buf.write(u"\u05b1\u05b5\5\16\b\2\u05b2\u05b5\5\36\20\2\u05b3\u05b5")
        buf.write(u"\5\20\t\2\u05b4\u05b1\3\2\2\2\u05b4\u05b2\3\2\2\2\u05b4")
        buf.write(u"\u05b3\3\2\2\2\u05b5\u00af\3\2\2\2\u05b6\u05bb\5\u00ba")
        buf.write(u"^\2\u05b7\u05b8\7\23\2\2\u05b8\u05ba\5\u00ba^\2\u05b9")
        buf.write(u"\u05b7\3\2\2\2\u05ba\u05bd\3\2\2\2\u05bb\u05b9\3\2\2")
        buf.write(u"\2\u05bb\u05bc\3\2\2\2\u05bc\u00b1\3\2\2\2\u05bd\u05bb")
        buf.write(u"\3\2\2\2\u05be\u05c1\5\u00b6\\\2\u05bf\u05c1\5\u00ba")
        buf.write(u"^\2\u05c0\u05be\3\2\2\2\u05c0\u05bf\3\2\2\2\u05c1\u00b3")
        buf.write(u"\3\2\2\2\u05c2\u05c6\5\u00b6\\\2\u05c3\u05c6\5\u00ba")
        buf.write(u"^\2\u05c4\u05c6\5\u00bc_\2\u05c5\u05c2\3\2\2\2\u05c5")
        buf.write(u"\u05c3\3\2\2\2\u05c5\u05c4\3\2\2\2\u05c6\u00b5\3\2\2")
        buf.write(u"\2\u05c7\u05c8\7\u00a4\2\2\u05c8\u00b7\3\2\2\2\u05c9")
        buf.write(u"\u05ca\t\4\2\2\u05ca\u00b9\3\2\2\2\u05cb\u05cc\7\u00a3")
        buf.write(u"\2\2\u05cc\u00bb\3\2\2\2\u05cd\u05ce\7\u00a2\2\2\u05ce")
        buf.write(u"\u00bd\3\2\2\2\u05cf\u05d4\5\u00c0a\2\u05d0\u05d1\7\23")
        buf.write(u"\2\2\u05d1\u05d3\5\u00c0a\2\u05d2\u05d0\3\2\2\2\u05d3")
        buf.write(u"\u05d6\3\2\2\2\u05d4\u05d2\3\2\2\2\u05d4\u05d5\3\2\2")
        buf.write(u"\2\u05d5\u00bf\3\2\2\2\u05d6\u05d4\3\2\2\2\u05d7\u05dd")
        buf.write(u"\5\u00c6d\2\u05d8\u05da\7w\2\2\u05d9\u05d8\3\2\2\2\u05d9")
        buf.write(u"\u05da\3\2\2\2\u05da\u05db\3\2\2\2\u05db\u05dd\5\u00c2")
        buf.write(u"b\2\u05dc\u05d7\3\2\2\2\u05dc\u05d9\3\2\2\2\u05dd\u00c1")
        buf.write(u"\3\2\2\2\u05de\u05e1\5\u00c4c\2\u05df\u05e1\5\60\31\2")
        buf.write(u"\u05e0\u05de\3\2\2\2\u05e0\u05df\3\2\2\2\u05e1\u00c3")
        buf.write(u"\3\2\2\2\u05e2\u05e5\5\u00b6\\\2\u05e3\u05e4\7-\2\2\u05e4")
        buf.write(u"\u05e6\5\u0102\u0082\2\u05e5\u05e3\3\2\2\2\u05e5\u05e6")
        buf.write(u"\3\2\2\2\u05e6\u00c5\3\2\2\2\u05e7\u05e8\5\u00acW\2\u05e8")
        buf.write(u"\u05e9\5\u00b6\\\2\u05e9\u00c7\3\2\2\2\u05ea\u05ed\5")
        buf.write(u"\u00a2R\2\u05eb\u05ed\5\u00caf\2\u05ec\u05ea\3\2\2\2")
        buf.write(u"\u05ec\u05eb\3\2\2\2\u05ed\u00c9\3\2\2\2\u05ee\u05ef")
        buf.write(u"\bf\1\2\u05ef\u05f0\7I\2\2\u05f0\u05f9\3\2\2\2\u05f1")
        buf.write(u"\u05f2\f\4\2\2\u05f2\u05f3\7\30\2\2\u05f3\u05f8\7\31")
        buf.write(u"\2\2\u05f4\u05f5\f\3\2\2\u05f5\u05f6\7\32\2\2\u05f6\u05f8")
        buf.write(u"\7\33\2\2\u05f7\u05f1\3\2\2\2\u05f7\u05f4\3\2\2\2\u05f8")
        buf.write(u"\u05fb\3\2\2\2\u05f9\u05f7\3\2\2\2\u05f9\u05fa\3\2\2")
        buf.write(u"\2\u05fa\u00cb\3\2\2\2\u05fb\u05f9\3\2\2\2\u05fc\u0602")
        buf.write(u"\5\u00ceh\2\u05fd\u05fe\5\u0080A\2\u05fe\u05ff\5\u00ce")
        buf.write(u"h\2\u05ff\u0601\3\2\2\2\u0600\u05fd\3\2\2\2\u0601\u0604")
        buf.write(u"\3\2\2\2\u0602\u0600\3\2\2\2\u0602\u0603\3\2\2\2\u0603")
        buf.write(u"\u00cd\3\2\2\2\u0604\u0602\3\2\2\2\u0605\u060b\5\26\f")
        buf.write(u"\2\u0606\u060b\5\32\16\2\u0607\u060b\5(\25\2\u0608\u060b")
        buf.write(u"\5&\24\2\u0609\u060b\5\24\13\2\u060a\u0605\3\2\2\2\u060a")
        buf.write(u"\u0606\3\2\2\2\u060a\u0607\3\2\2\2\u060a\u0608\3\2\2")
        buf.write(u"\2\u060a\u0609\3\2\2\2\u060b\u00cf\3\2\2\2\u060c\u0612")
        buf.write(u"\5\u00d2j\2\u060d\u060e\5\u0080A\2\u060e\u060f\5\u00d2")
        buf.write(u"j\2\u060f\u0611\3\2\2\2\u0610\u060d\3\2\2\2\u0611\u0614")
        buf.write(u"\3\2\2\2\u0612\u0610\3\2\2\2\u0612\u0613\3\2\2\2\u0613")
        buf.write(u"\u00d1\3\2\2\2\u0614\u0612\3\2\2\2\u0615\u0619\5\34\17")
        buf.write(u"\2\u0616\u0619\5\30\r\2\u0617\u0619\5*\26\2\u0618\u0615")
        buf.write(u"\3\2\2\2\u0618\u0616\3\2\2\2\u0618\u0617\3\2\2\2\u0619")
        buf.write(u"\u00d3\3\2\2\2\u061a\u061b\7\13\2\2\u061b\u0625\5\u017e")
        buf.write(u"\u00c0\2\u061c\u061d\7\f\2\2\u061d\u0625\5\u0198\u00cd")
        buf.write(u"\2\u061e\u061f\7\r\2\2\u061f\u0625\5\u00d6l\2\u0620\u0621")
        buf.write(u"\7\16\2\2\u0621\u0625\5\u00d6l\2\u0622\u0623\7\17\2\2")
        buf.write(u"\u0623\u0625\5\u00dan\2\u0624\u061a\3\2\2\2\u0624\u061c")
        buf.write(u"\3\2\2\2\u0624\u061e\3\2\2\2\u0624\u0620\3\2\2\2\u0624")
        buf.write(u"\u0622\3\2\2\2\u0625\u00d5\3\2\2\2\u0626\u0628\5\u00b4")
        buf.write(u"[\2\u0627\u0629\5\u00d8m\2\u0628\u0627\3\2\2\2\u0628")
        buf.write(u"\u0629\3\2\2\2\u0629\u00d7\3\2\2\2\u062a\u062b\7l\2\2")
        buf.write(u"\u062b\u062c\5\u0126\u0094\2\u062c\u062d\7\21\2\2\u062d")
        buf.write(u"\u0632\5\u00b4[\2\u062e\u062f\7\25\2\2\u062f\u0631\5")
        buf.write(u"\u00b4[\2\u0630\u062e\3\2\2\2\u0631\u0634\3\2\2\2\u0632")
        buf.write(u"\u0630\3\2\2\2\u0632\u0633\3\2\2\2\u0633\u00d9\3\2\2")
        buf.write(u"\2\u0634\u0632\3\2\2\2\u0635\u0637\5\u00b4[\2\u0636\u0638")
        buf.write(u"\5\u00dco\2\u0637\u0636\3\2\2\2\u0637\u0638\3\2\2\2\u0638")
        buf.write(u"\u00db\3\2\2\2\u0639\u063a\7l\2\2\u063a\u063b\5\u0126")
        buf.write(u"\u0094\2\u063b\u063d\7\21\2\2\u063c\u063e\7%\2\2\u063d")
        buf.write(u"\u063c\3\2\2\2\u063d\u063e\3\2\2\2\u063e\u063f\3\2\2")
        buf.write(u"\2\u063f\u0644\5\u014e\u00a8\2\u0640\u0641\7%\2\2\u0641")
        buf.write(u"\u0643\5\u014e\u00a8\2\u0642\u0640\3\2\2\2\u0643\u0646")
        buf.write(u"\3\2\2\2\u0644\u0642\3\2\2\2\u0644\u0645\3\2\2\2\u0645")
        buf.write(u"\u0649\3\2\2\2\u0646\u0644\3\2\2\2\u0647\u0648\7\25\2")
        buf.write(u"\2\u0648\u064a\5\u014e\u00a8\2\u0649\u0647\3\2\2\2\u0649")
        buf.write(u"\u064a\3\2\2\2\u064a\u00dd\3\2\2\2\u064b\u0650\5\u00b6")
        buf.write(u"\\\2\u064c\u064d\7\23\2\2\u064d\u064f\5\u00b6\\\2\u064e")
        buf.write(u"\u064c\3\2\2\2\u064f\u0652\3\2\2\2\u0650\u064e\3\2\2")
        buf.write(u"\2\u0650\u0651\3\2\2\2\u0651\u00df\3\2\2\2\u0652\u0650")
        buf.write(u"\3\2\2\2\u0653\u0658\5\u00b8]\2\u0654\u0655\7\23\2\2")
        buf.write(u"\u0655\u0657\5\u00b8]\2\u0656\u0654\3\2\2\2\u0657\u065a")
        buf.write(u"\3\2\2\2\u0658\u0656\3\2\2\2\u0658\u0659\3\2\2\2\u0659")
        buf.write(u"\u00e1\3\2\2\2\u065a\u0658\3\2\2\2\u065b\u0660\5&\24")
        buf.write(u"\2\u065c\u0660\5(\25\2\u065d\u0660\5*\26\2\u065e\u0660")
        buf.write(u"\5,\27\2\u065f\u065b\3\2\2\2\u065f\u065c\3\2\2\2\u065f")
        buf.write(u"\u065d\3\2\2\2\u065f\u065e\3\2\2\2\u0660\u00e3\3\2\2")
        buf.write(u"\2\u0661\u0662\7\n\2\2\u0662\u00e5\3\2\2\2\u0663\u0669")
        buf.write(u"\5\u00e8u\2\u0664\u0665\5\u0080A\2\u0665\u0666\5\u00e8")
        buf.write(u"u\2\u0666\u0668\3\2\2\2\u0667\u0664\3\2\2\2\u0668\u066b")
        buf.write(u"\3\2\2\2\u0669\u0667\3\2\2\2\u0669\u066a\3\2\2\2\u066a")
        buf.write(u"\u00e7\3\2\2\2\u066b\u0669\3\2\2\2\u066c\u066d\7\13\2")
        buf.write(u"\2\u066d\u0677\5\u0168\u00b5\2\u066e\u066f\7\f\2\2\u066f")
        buf.write(u"\u0677\5\u0184\u00c3\2\u0670\u0671\7\r\2\2\u0671\u0677")
        buf.write(u"\5\u00eav\2\u0672\u0673\7\16\2\2\u0673\u0677\5\u00ea")
        buf.write(u"v\2\u0674\u0675\7\17\2\2\u0675\u0677\5\u00ecw\2\u0676")
        buf.write(u"\u066c\3\2\2\2\u0676\u066e\3\2\2\2\u0676\u0670\3\2\2")
        buf.write(u"\2\u0676\u0672\3\2\2\2\u0676\u0674\3\2\2\2\u0677\u00e9")
        buf.write(u"\3\2\2\2\u0678\u067a\5\u0150\u00a9\2\u0679\u067b\7\22")
        buf.write(u"\2\2\u067a\u0679\3\2\2\2\u067a\u067b\3\2\2\2\u067b\u067d")
        buf.write(u"\3\2\2\2\u067c\u067e\5\u00d8m\2\u067d\u067c\3\2\2\2\u067d")
        buf.write(u"\u067e\3\2\2\2\u067e\u00eb\3\2\2\2\u067f\u0681\5\u0136")
        buf.write(u"\u009c\2\u0680\u0682\7\22\2\2\u0681\u0680\3\2\2\2\u0681")
        buf.write(u"\u0682\3\2\2\2\u0682\u0684\3\2\2\2\u0683\u0685\5\u00dc")
        buf.write(u"o\2\u0684\u0683\3\2\2\2\u0684\u0685\3\2\2\2\u0685\u00ed")
        buf.write(u"\3\2\2\2\u0686\u068c\5\62\32\2\u0687\u0688\5\u0080A\2")
        buf.write(u"\u0688\u0689\5\62\32\2\u0689\u068b\3\2\2\2\u068a\u0687")
        buf.write(u"\3\2\2\2\u068b\u068e\3\2\2\2\u068c\u068a\3\2\2\2\u068c")
        buf.write(u"\u068d\3\2\2\2\u068d\u00ef\3\2\2\2\u068e\u068c\3\2\2")
        buf.write(u"\2\u068f\u0695\5.\30\2\u0690\u0691\5\u0080A\2\u0691\u0692")
        buf.write(u"\5.\30\2\u0692\u0694\3\2\2\2\u0693\u0690\3\2\2\2\u0694")
        buf.write(u"\u0697\3\2\2\2\u0695\u0693\3\2\2\2\u0695\u0696\3\2\2")
        buf.write(u"\2\u0696\u00f1\3\2\2\2\u0697\u0695\3\2\2\2\u0698\u069e")
        buf.write(u"\5F$\2\u0699\u069a\5\u0080A\2\u069a\u069b\5F$\2\u069b")
        buf.write(u"\u069d\3\2\2\2\u069c\u0699\3\2\2\2\u069d\u06a0\3\2\2")
        buf.write(u"\2\u069e\u069c\3\2\2\2\u069e\u069f\3\2\2\2\u069f\u00f3")
        buf.write(u"\3\2\2\2\u06a0\u069e\3\2\2\2\u06a1\u06a7\5V,\2\u06a2")
        buf.write(u"\u06a3\5\u0080A\2\u06a3\u06a4\5V,\2\u06a4\u06a6\3\2\2")
        buf.write(u"\2\u06a5\u06a2\3\2\2\2\u06a6\u06a9\3\2\2\2\u06a7\u06a5")
        buf.write(u"\3\2\2\2\u06a7\u06a8\3\2\2\2\u06a8\u00f5\3\2\2\2\u06a9")
        buf.write(u"\u06a7\3\2\2\2\u06aa\u06ab\7\30\2\2\u06ab\u06ac\5\u00f8")
        buf.write(u"}\2\u06ac\u06ad\7\24\2\2\u06ad\u06ae\5\u00f8}\2\u06ae")
        buf.write(u"\u06af\7\31\2\2\u06af\u06b9\3\2\2\2\u06b0\u06b1\7\30")
        buf.write(u"\2\2\u06b1\u06b2\5\u00fa~\2\u06b2\u06b3\7\31\2\2\u06b3")
        buf.write(u"\u06b9\3\2\2\2\u06b4\u06b5\7*\2\2\u06b5\u06b6\5\u00fa")
        buf.write(u"~\2\u06b6\u06b7\7(\2\2\u06b7\u06b9\3\2\2\2\u06b8\u06aa")
        buf.write(u"\3\2\2\2\u06b8\u06b0\3\2\2\2\u06b8\u06b4\3\2\2\2\u06b9")
        buf.write(u"\u00f7\3\2\2\2\u06ba\u06c9\7\u00a0\2\2\u06bb\u06c9\7")
        buf.write(u"\u00a1\2\2\u06bc\u06c9\7\u00a9\2\2\u06bd\u06c9\7\u00aa")
        buf.write(u"\2\2\u06be\u06c9\7\u009f\2\2\u06bf\u06c9\7\u00ae\2\2")
        buf.write(u"\u06c0\u06c9\7\u00ad\2\2\u06c1\u06c9\7\u00a7\2\2\u06c2")
        buf.write(u"\u06c9\7\u00ab\2\2\u06c3\u06c9\7\u00ac\2\2\u06c4\u06c9")
        buf.write(u"\7\u009e\2\2\u06c5\u06c9\7\u00af\2\2\u06c6\u06c9\7\u00a8")
        buf.write(u"\2\2\u06c7\u06c9\5\u0086D\2\u06c8\u06ba\3\2\2\2\u06c8")
        buf.write(u"\u06bb\3\2\2\2\u06c8\u06bc\3\2\2\2\u06c8\u06bd\3\2\2")
        buf.write(u"\2\u06c8\u06be\3\2\2\2\u06c8\u06bf\3\2\2\2\u06c8\u06c0")
        buf.write(u"\3\2\2\2\u06c8\u06c1\3\2\2\2\u06c8\u06c2\3\2\2\2\u06c8")
        buf.write(u"\u06c3\3\2\2\2\u06c8\u06c4\3\2\2\2\u06c8\u06c5\3\2\2")
        buf.write(u"\2\u06c8\u06c6\3\2\2\2\u06c8\u06c7\3\2\2\2\u06c9\u00f9")
        buf.write(u"\3\2\2\2\u06ca\u06cf\5\u00f8}\2\u06cb\u06cc\7\23\2\2")
        buf.write(u"\u06cc\u06ce\5\u00f8}\2\u06cd\u06cb\3\2\2\2\u06ce\u06d1")
        buf.write(u"\3\2\2\2\u06cf\u06cd\3\2\2\2\u06cf\u06d0\3\2\2\2\u06d0")
        buf.write(u"\u00fb\3\2\2\2\u06d1\u06cf\3\2\2\2\u06d2\u06d7\5\u0100")
        buf.write(u"\u0081\2\u06d3\u06d7\5\u0102\u0082\2\u06d4\u06d7\5\u00b4")
        buf.write(u"[\2\u06d5\u06d7\5\u00fe\u0080\2\u06d6\u06d2\3\2\2\2\u06d6")
        buf.write(u"\u06d3\3\2\2\2\u06d6\u06d4\3\2\2\2\u06d6\u06d5\3\2\2")
        buf.write(u"\2\u06d7\u00fd\3\2\2\2\u06d8\u06d9\t\5\2\2\u06d9\u00ff")
        buf.write(u"\3\2\2\2\u06da\u06db\7\26\2\2\u06db\u06dc\5\\/\2\u06dc")
        buf.write(u"\u06dd\7\27\2\2\u06dd\u0101\3\2\2\2\u06de\u06e1\5\u00f8")
        buf.write(u"}\2\u06df\u06e1\5\u0104\u0083\2\u06e0\u06de\3\2\2\2\u06e0")
        buf.write(u"\u06df\3\2\2\2\u06e1\u0103\3\2\2\2\u06e2\u06e8\5\u00a0")
        buf.write(u"Q\2\u06e3\u06e8\5\u009aN\2\u06e4\u06e8\5\u009cO\2\u06e5")
        buf.write(u"\u06e8\5\u0108\u0085\2\u06e6\u06e8\5\u0106\u0084\2\u06e7")
        buf.write(u"\u06e2\3\2\2\2\u06e7\u06e3\3\2\2\2\u06e7\u06e4\3\2\2")
        buf.write(u"\2\u06e7\u06e5\3\2\2\2\u06e7\u06e6\3\2\2\2\u06e8\u0105")
        buf.write(u"\3\2\2\2\u06e9\u06eb\7w\2\2\u06ea\u06e9\3\2\2\2\u06ea")
        buf.write(u"\u06eb\3\2\2\2\u06eb\u06ec\3\2\2\2\u06ec\u06ee\7\26\2")
        buf.write(u"\2\u06ed\u06ef\5\u010a\u0086\2\u06ee\u06ed\3\2\2\2\u06ee")
        buf.write(u"\u06ef\3\2\2\2\u06ef\u06f0\3\2\2\2\u06f0\u06f1\7\27\2")
        buf.write(u"\2\u06f1\u0107\3\2\2\2\u06f2\u06f4\7w\2\2\u06f3\u06f2")
        buf.write(u"\3\2\2\2\u06f3\u06f4\3\2\2\2\u06f4\u06f5\3\2\2\2\u06f5")
        buf.write(u"\u06f7\7\32\2\2\u06f6\u06f8\5\u010c\u0087\2\u06f7\u06f6")
        buf.write(u"\3\2\2\2\u06f7\u06f8\3\2\2\2\u06f8\u06f9\3\2\2\2\u06f9")
        buf.write(u"\u06fa\7\33\2\2\u06fa\u0109\3\2\2\2\u06fb\u06fc\5\\/")
        buf.write(u"\2\u06fc\u0705\7\23\2\2\u06fd\u0702\5\\/\2\u06fe\u06ff")
        buf.write(u"\7\23\2\2\u06ff\u0701\5\\/\2\u0700\u06fe\3\2\2\2\u0701")
        buf.write(u"\u0704\3\2\2\2\u0702\u0700\3\2\2\2\u0702\u0703\3\2\2")
        buf.write(u"\2\u0703\u0706\3\2\2\2\u0704\u0702\3\2\2\2\u0705\u06fd")
        buf.write(u"\3\2\2\2\u0705\u0706\3\2\2\2\u0706\u010b\3\2\2\2\u0707")
        buf.write(u"\u070c\5\u010e\u0088\2\u0708\u0709\7\23\2\2\u0709\u070b")
        buf.write(u"\5\u010e\u0088\2\u070a\u0708\3\2\2\2\u070b\u070e\3\2")
        buf.write(u"\2\2\u070c\u070a\3\2\2\2\u070c\u070d\3\2\2\2\u070d\u010d")
        buf.write(u"\3\2\2\2\u070e\u070c\3\2\2\2\u070f\u0710\5\\/\2\u0710")
        buf.write(u"\u0711\7\21\2\2\u0711\u0712\5\\/\2\u0712\u010f\3\2\2")
        buf.write(u"\2\u0713\u0714\5\\/\2\u0714\u0715\7\21\2\2\u0715\u0716")
        buf.write(u"\5\\/\2\u0716\u071d\3\2\2\2\u0717\u0718\5\\/\2\u0718")
        buf.write(u"\u0719\7\21\2\2\u0719\u071d\3\2\2\2\u071a\u071b\7\21")
        buf.write(u"\2\2\u071b\u071d\5\\/\2\u071c\u0713\3\2\2\2\u071c\u0717")
        buf.write(u"\3\2\2\2\u071c\u071a\3\2\2\2\u071d\u0111\3\2\2\2\u071e")
        buf.write(u"\u071f\5\u00b6\\\2\u071f\u0720\5\u012c\u0097\2\u0720")
        buf.write(u"\u0721\5\\/\2\u0721\u0113\3\2\2\2\u0722\u0723\b\u008b")
        buf.write(u"\1\2\u0723\u0724\5\u00b6\\\2\u0724\u0729\3\2\2\2\u0725")
        buf.write(u"\u0726\f\3\2\2\u0726\u0728\5z>\2\u0727\u0725\3\2\2\2")
        buf.write(u"\u0728\u072b\3\2\2\2\u0729\u0727\3\2\2\2\u0729\u072a")
        buf.write(u"\3\2\2\2\u072a\u0115\3\2\2\2\u072b\u0729\3\2\2\2\u072c")
        buf.write(u"\u072d\6\u008c/\3\u072d\u072e\7\u00a4\2\2\u072e\u0731")
        buf.write(u"\5\u00c8e\2\u072f\u0731\5\\/\2\u0730\u072c\3\2\2\2\u0730")
        buf.write(u"\u072f\3\2\2\2\u0731\u0117\3\2\2\2\u0732\u0733\7\u0086")
        buf.write(u"\2\2\u0733\u0734\7F\2\2\u0734\u0735\7l\2\2\u0735\u0736")
        buf.write(u"\5\\/\2\u0736\u0119\3\2\2\2\u0737\u0738\7\u0086\2\2\u0738")
        buf.write(u"\u0739\7~\2\2\u0739\u073a\7l\2\2\u073a\u073b\5\\/\2\u073b")
        buf.write(u"\u011b\3\2\2\2\u073c\u0741\5\u011e\u0090\2\u073d\u073e")
        buf.write(u"\7\23\2\2\u073e\u0740\5\u011e\u0090\2\u073f\u073d\3\2")
        buf.write(u"\2\2\u0740\u0743\3\2\2\2\u0741\u073f\3\2\2\2\u0741\u0742")
        buf.write(u"\3\2\2\2\u0742\u011d\3\2\2\2\u0743\u0741\3\2\2\2\u0744")
        buf.write(u"\u0749\5\u00b6\\\2\u0745\u0746\7\25\2\2\u0746\u0748\5")
        buf.write(u"\u00b6\\\2\u0747\u0745\3\2\2\2\u0748\u074b\3\2\2\2\u0749")
        buf.write(u"\u0747\3\2\2\2\u0749\u074a\3\2\2\2\u074a\u074d\3\2\2")
        buf.write(u"\2\u074b\u0749\3\2\2\2\u074c\u074e\t\6\2\2\u074d\u074c")
        buf.write(u"\3\2\2\2\u074d\u074e\3\2\2\2\u074e\u011f\3\2\2\2\u074f")
        buf.write(u"\u0756\7\"\2\2\u0750\u0756\7#\2\2\u0751\u0756\5\u012e")
        buf.write(u"\u0098\2\u0752\u0756\5\u0130\u0099\2\u0753\u0756\5\u0132")
        buf.write(u"\u009a\2\u0754\u0756\5\u0134\u009b\2\u0755\u074f\3\2")
        buf.write(u"\2\2\u0755\u0750\3\2\2\2\u0755\u0751\3\2\2\2\u0755\u0752")
        buf.write(u"\3\2\2\2\u0755\u0753\3\2\2\2\u0755\u0754\3\2\2\2\u0756")
        buf.write(u"\u0121\3\2\2\2\u0757\u0758\7\u00a4\2\2\u0758\u0759\6")
        buf.write(u"\u0092\60\3\u0759\u0123\3\2\2\2\u075a\u075b\7\u00a4\2")
        buf.write(u"\2\u075b\u075c\6\u0093\61\3\u075c\u0125\3\2\2\2\u075d")
        buf.write(u"\u075e\7\u00a4\2\2\u075e\u075f\6\u0094\62\3\u075f\u0127")
        buf.write(u"\3\2\2\2\u0760\u0761\7\u00a4\2\2\u0761\u0762\6\u0095")
        buf.write(u"\63\3\u0762\u0129\3\2\2\2\u0763\u0764\7\u00a4\2\2\u0764")
        buf.write(u"\u0765\6\u0096\64\3\u0765\u012b\3\2\2\2\u0766\u0767\7")
        buf.write(u"-\2\2\u0767\u012d\3\2\2\2\u0768\u0769\7$\2\2\u0769\u012f")
        buf.write(u"\3\2\2\2\u076a\u076b\7%\2\2\u076b\u0131\3\2\2\2\u076c")
        buf.write(u"\u076d\7&\2\2\u076d\u0133\3\2\2\2\u076e\u076f\t\7\2\2")
        buf.write(u"\u076f\u0135\3\2\2\2\u0770\u0771\7\u0089\2\2\u0771\u0772")
        buf.write(u"\5\u0138\u009d\2\u0772\u0773\7\22\2\2\u0773\u0778\3\2")
        buf.write(u"\2\2\u0774\u0775\5\u0138\u009d\2\u0775\u0776\7\22\2\2")
        buf.write(u"\u0776\u0778\3\2\2\2\u0777\u0770\3\2\2\2\u0777\u0774")
        buf.write(u"\3\2\2\2\u0778\u0137\3\2\2\2\u0779\u077a\b\u009d\1\2")
        buf.write(u"\u077a\u077b\5\u013a\u009e\2\u077b\u0780\3\2\2\2\u077c")
        buf.write(u"\u077d\f\3\2\2\u077d\u077f\5\u0140\u00a1\2\u077e\u077c")
        buf.write(u"\3\2\2\2\u077f\u0782\3\2\2\2\u0780\u077e\3\2\2\2\u0780")
        buf.write(u"\u0781\3\2\2\2\u0781\u0139\3\2\2\2\u0782\u0780\3\2\2")
        buf.write(u"\2\u0783\u078b\5\u013c\u009f\2\u0784\u078b\5\u013e\u00a0")
        buf.write(u"\2\u0785\u078b\5\u0148\u00a5\2\u0786\u078b\5\u014a\u00a6")
        buf.write(u"\2\u0787\u078b\5\u014c\u00a7\2\u0788\u078b\5\u0142\u00a2")
        buf.write(u"\2\u0789\u078b\5\u0146\u00a4\2\u078a\u0783\3\2\2\2\u078a")
        buf.write(u"\u0784\3\2\2\2\u078a\u0785\3\2\2\2\u078a\u0786\3\2\2")
        buf.write(u"\2\u078a\u0787\3\2\2\2\u078a\u0788\3\2\2\2\u078a\u0789")
        buf.write(u"\3\2\2\2\u078b\u013b\3\2\2\2\u078c\u078d\5\u00fe\u0080")
        buf.write(u"\2\u078d\u013d\3\2\2\2\u078e\u078f\5\u0122\u0092\2\u078f")
        buf.write(u"\u0790\5\u0142\u00a2\2\u0790\u013f\3\2\2\2\u0791\u0792")
        buf.write(u"\7\25\2\2\u0792\u0797\5\u0142\u00a2\2\u0793\u0794\7\25")
        buf.write(u"\2\2\u0794\u0797\5\u014e\u00a8\2\u0795\u0797\5\u0146")
        buf.write(u"\u00a4\2\u0796\u0791\3\2\2\2\u0796\u0793\3\2\2\2\u0796")
        buf.write(u"\u0795\3\2\2\2\u0797\u0141\3\2\2\2\u0798\u0799\5\u014e")
        buf.write(u"\u00a8\2\u0799\u079b\7\26\2\2\u079a\u079c\5\u0144\u00a3")
        buf.write(u"\2\u079b\u079a\3\2\2\2\u079b\u079c\3\2\2\2\u079c\u079d")
        buf.write(u"\3\2\2\2\u079d\u079e\7\27\2\2\u079e\u0143\3\2\2\2\u079f")
        buf.write(u"\u07a0\b\u00a3\1\2\u07a0\u07a1\5\u0138\u009d\2\u07a1")
        buf.write(u"\u07a7\3\2\2\2\u07a2\u07a3\f\3\2\2\u07a3\u07a4\7\23\2")
        buf.write(u"\2\u07a4\u07a6\5\u0138\u009d\2\u07a5\u07a2\3\2\2\2\u07a6")
        buf.write(u"\u07a9\3\2\2\2\u07a7\u07a5\3\2\2\2\u07a7\u07a8\3\2\2")
        buf.write(u"\2\u07a8\u0145\3\2\2\2\u07a9\u07a7\3\2\2\2\u07aa\u07ab")
        buf.write(u"\7\30\2\2\u07ab\u07ac\5\u0138\u009d\2\u07ac\u07ad\7\31")
        buf.write(u"\2\2\u07ad\u0147\3\2\2\2\u07ae\u07af\7\26\2\2\u07af\u07b0")
        buf.write(u"\5\u0138\u009d\2\u07b0\u07b1\7\27\2\2\u07b1\u0149\3\2")
        buf.write(u"\2\2\u07b2\u07b3\5\u014e\u00a8\2\u07b3\u014b\3\2\2\2")
        buf.write(u"\u07b4\u07ba\7\u00a9\2\2\u07b5\u07ba\7\u00ab\2\2\u07b6")
        buf.write(u"\u07ba\7\u00a7\2\2\u07b7\u07ba\7\u009e\2\2\u07b8\u07ba")
        buf.write(u"\7\u009f\2\2\u07b9\u07b4\3\2\2\2\u07b9\u07b5\3\2\2\2")
        buf.write(u"\u07b9\u07b6\3\2\2\2\u07b9\u07b7\3\2\2\2\u07b9\u07b8")
        buf.write(u"\3\2\2\2\u07ba\u014d\3\2\2\2\u07bb\u07bc\t\b\2\2\u07bc")
        buf.write(u"\u014f\3\2\2\2\u07bd\u07be\7\u0089\2\2\u07be\u07c1\5")
        buf.write(u"\u0152\u00aa\2\u07bf\u07c1\5\u0152\u00aa\2\u07c0\u07bd")
        buf.write(u"\3\2\2\2\u07c0\u07bf\3\2\2\2\u07c1\u0151\3\2\2\2\u07c2")
        buf.write(u"\u07c3\b\u00aa\1\2\u07c3\u07c4\5\u0154\u00ab\2\u07c4")
        buf.write(u"\u07c9\3\2\2\2\u07c5\u07c6\f\3\2\2\u07c6\u07c8\5\u0156")
        buf.write(u"\u00ac\2\u07c7\u07c5\3\2\2\2\u07c8\u07cb\3\2\2\2\u07c9")
        buf.write(u"\u07c7\3\2\2\2\u07c9\u07ca\3\2\2\2\u07ca\u0153\3\2\2")
        buf.write(u"\2\u07cb\u07c9\3\2\2\2\u07cc\u07d1\5\u0160\u00b1\2\u07cd")
        buf.write(u"\u07d1\5\u0162\u00b2\2\u07ce\u07d1\5\u0164\u00b3\2\u07cf")
        buf.write(u"\u07d1\5\u0158\u00ad\2\u07d0\u07cc\3\2\2\2\u07d0\u07cd")
        buf.write(u"\3\2\2\2\u07d0\u07ce\3\2\2\2\u07d0\u07cf\3\2\2\2\u07d1")
        buf.write(u"\u0155\3\2\2\2\u07d2\u07d3\7\25\2\2\u07d3\u07d9\5\u0158")
        buf.write(u"\u00ad\2\u07d4\u07d5\7\30\2\2\u07d5\u07d6\5\u0152\u00aa")
        buf.write(u"\2\u07d6\u07d7\7\31\2\2\u07d7\u07d9\3\2\2\2\u07d8\u07d2")
        buf.write(u"\3\2\2\2\u07d8\u07d4\3\2\2\2\u07d9\u0157\3\2\2\2\u07da")
        buf.write(u"\u07db\5\u0166\u00b4\2\u07db\u07dd\7\26\2\2\u07dc\u07de")
        buf.write(u"\5\u015a\u00ae\2\u07dd\u07dc\3\2\2\2\u07dd\u07de\3\2")
        buf.write(u"\2\2\u07de\u07df\3\2\2\2\u07df\u07e0\7\27\2\2\u07e0\u0159")
        buf.write(u"\3\2\2\2\u07e1\u07e8\5\u015c\u00af\2\u07e2\u07e8\5\u015e")
        buf.write(u"\u00b0\2\u07e3\u07e4\5\u015c\u00af\2\u07e4\u07e5\7\23")
        buf.write(u"\2\2\u07e5\u07e6\5\u015e\u00b0\2\u07e6\u07e8\3\2\2\2")
        buf.write(u"\u07e7\u07e1\3\2\2\2\u07e7\u07e2\3\2\2\2\u07e7\u07e3")
        buf.write(u"\3\2\2\2\u07e8\u015b\3\2\2\2\u07e9\u07ea\b\u00af\1\2")
        buf.write(u"\u07ea\u07eb\5\u0152\u00aa\2\u07eb\u07f1\3\2\2\2\u07ec")
        buf.write(u"\u07ed\f\3\2\2\u07ed\u07ee\7\23\2\2\u07ee\u07f0\5\u0152")
        buf.write(u"\u00aa\2\u07ef\u07ec\3\2\2\2\u07f0\u07f3\3\2\2\2\u07f1")
        buf.write(u"\u07ef\3\2\2\2\u07f1\u07f2\3\2\2\2\u07f2\u015d\3\2\2")
        buf.write(u"\2\u07f3\u07f1\3\2\2\2\u07f4\u07f5\b\u00b0\1\2\u07f5")
        buf.write(u"\u07f6\5\u0166\u00b4\2\u07f6\u07f7\7-\2\2\u07f7\u07f8")
        buf.write(u"\5\u0152\u00aa\2\u07f8\u0801\3\2\2\2\u07f9\u07fa\f\3")
        buf.write(u"\2\2\u07fa\u07fb\7\23\2\2\u07fb\u07fc\5\u0166\u00b4\2")
        buf.write(u"\u07fc\u07fd\7-\2\2\u07fd\u07fe\5\u0152\u00aa\2\u07fe")
        buf.write(u"\u0800\3\2\2\2\u07ff\u07f9\3\2\2\2\u0800\u0803\3\2\2")
        buf.write(u"\2\u0801\u07ff\3\2\2\2\u0801\u0802\3\2\2\2\u0802\u015f")
        buf.write(u"\3\2\2\2\u0803\u0801\3\2\2\2\u0804\u0805\7\26\2\2\u0805")
        buf.write(u"\u0806\5\u0152\u00aa\2\u0806\u0807\7\27\2\2\u0807\u0161")
        buf.write(u"\3\2\2\2\u0808\u0809\b\u00b2\1\2\u0809\u080c\7\u00a6")
        buf.write(u"\2\2\u080a\u080c\5\u0166\u00b4\2\u080b\u0808\3\2\2\2")
        buf.write(u"\u080b\u080a\3\2\2\2\u080c\u0812\3\2\2\2\u080d\u080e")
        buf.write(u"\f\3\2\2\u080e\u080f\7\25\2\2\u080f\u0811\5\u0166\u00b4")
        buf.write(u"\2\u0810\u080d\3\2\2\2\u0811\u0814\3\2\2\2\u0812\u0810")
        buf.write(u"\3\2\2\2\u0812\u0813\3\2\2\2\u0813\u0163\3\2\2\2\u0814")
        buf.write(u"\u0812\3\2\2\2\u0815\u081b\7\u00a9\2\2\u0816\u081b\7")
        buf.write(u"\u00ab\2\2\u0817\u081b\7\u00a7\2\2\u0818\u081b\7\u009e")
        buf.write(u"\2\2\u0819\u081b\7\u009f\2\2\u081a\u0815\3\2\2\2\u081a")
        buf.write(u"\u0816\3\2\2\2\u081a\u0817\3\2\2\2\u081a\u0818\3\2\2")
        buf.write(u"\2\u081a\u0819\3\2\2\2\u081b\u0165\3\2\2\2\u081c\u081d")
        buf.write(u"\t\t\2\2\u081d\u0167\3\2\2\2\u081e\u081f\7\u0089\2\2")
        buf.write(u"\u081f\u0820\5\u016a\u00b6\2\u0820\u0821\7\22\2\2\u0821")
        buf.write(u"\u0826\3\2\2\2\u0822\u0823\5\u016a\u00b6\2\u0823\u0824")
        buf.write(u"\7\22\2\2\u0824\u0826\3\2\2\2\u0825\u081e\3\2\2\2\u0825")
        buf.write(u"\u0822\3\2\2\2\u0826\u0169\3\2\2\2\u0827\u0828\b\u00b6")
        buf.write(u"\1\2\u0828\u0829\5\u016c\u00b7\2\u0829\u082e\3\2\2\2")
        buf.write(u"\u082a\u082b\f\3\2\2\u082b\u082d\5\u0172\u00ba\2\u082c")
        buf.write(u"\u082a\3\2\2\2\u082d\u0830\3\2\2\2\u082e\u082c\3\2\2")
        buf.write(u"\2\u082e\u082f\3\2\2\2\u082f\u016b\3\2\2\2\u0830\u082e")
        buf.write(u"\3\2\2\2\u0831\u0837\5\u016e\u00b8\2\u0832\u0837\5\u0170")
        buf.write(u"\u00b9\2\u0833\u0837\5\u017a\u00be\2\u0834\u0837\5\u017c")
        buf.write(u"\u00bf\2\u0835\u0837\5\u0180\u00c1\2\u0836\u0831\3\2")
        buf.write(u"\2\2\u0836\u0832\3\2\2\2\u0836\u0833\3\2\2\2\u0836\u0834")
        buf.write(u"\3\2\2\2\u0836\u0835\3\2\2\2\u0837\u016d\3\2\2\2\u0838")
        buf.write(u"\u0839\5\u00fe\u0080\2\u0839\u016f\3\2\2\2\u083a\u083b")
        buf.write(u"\5\u0122\u0092\2\u083b\u083c\5\u0174\u00bb\2\u083c\u0171")
        buf.write(u"\3\2\2\2\u083d\u083e\7\25\2\2\u083e\u0841\5\u0174\u00bb")
        buf.write(u"\2\u083f\u0841\5\u0178\u00bd\2\u0840\u083d\3\2\2\2\u0840")
        buf.write(u"\u083f\3\2\2\2\u0841\u0173\3\2\2\2\u0842\u0843\5\u0182")
        buf.write(u"\u00c2\2\u0843\u0845\7\26\2\2\u0844\u0846\5\u0176\u00bc")
        buf.write(u"\2\u0845\u0844\3\2\2\2\u0845\u0846\3\2\2\2\u0846\u0847")
        buf.write(u"\3\2\2\2\u0847\u0848\7\27\2\2\u0848\u0175\3\2\2\2\u0849")
        buf.write(u"\u084a\b\u00bc\1\2\u084a\u084b\5\u016a\u00b6\2\u084b")
        buf.write(u"\u0851\3\2\2\2\u084c\u084d\f\3\2\2\u084d\u084e\7\23\2")
        buf.write(u"\2\u084e\u0850\5\u016a\u00b6\2\u084f\u084c\3\2\2\2\u0850")
        buf.write(u"\u0853\3\2\2\2\u0851\u084f\3\2\2\2\u0851\u0852\3\2\2")
        buf.write(u"\2\u0852\u0177\3\2\2\2\u0853\u0851\3\2\2\2\u0854\u0855")
        buf.write(u"\7\30\2\2\u0855\u0856\5\u016a\u00b6\2\u0856\u0857\7\31")
        buf.write(u"\2\2\u0857\u0179\3\2\2\2\u0858\u0859\7\26\2\2\u0859\u085a")
        buf.write(u"\5\u016a\u00b6\2\u085a\u085b\7\27\2\2\u085b\u017b\3\2")
        buf.write(u"\2\2\u085c\u085d\b\u00bf\1\2\u085d\u085e\5\u0182\u00c2")
        buf.write(u"\2\u085e\u0864\3\2\2\2\u085f\u0860\f\3\2\2\u0860\u0861")
        buf.write(u"\7\25\2\2\u0861\u0863\5\u0182\u00c2\2\u0862\u085f\3\2")
        buf.write(u"\2\2\u0863\u0866\3\2\2\2\u0864\u0862\3\2\2\2\u0864\u0865")
        buf.write(u"\3\2\2\2\u0865\u017d\3\2\2\2\u0866\u0864\3\2\2\2\u0867")
        buf.write(u"\u0868\b\u00c0\1\2\u0868\u0869\5\u017c\u00bf\2\u0869")
        buf.write(u"\u086e\3\2\2\2\u086a\u086b\f\3\2\2\u086b\u086d\7\u00a6")
        buf.write(u"\2\2\u086c\u086a\3\2\2\2\u086d\u0870\3\2\2\2\u086e\u086c")
        buf.write(u"\3\2\2\2\u086e\u086f\3\2\2\2\u086f\u017f\3\2\2\2\u0870")
        buf.write(u"\u086e\3\2\2\2\u0871\u0877\7\u00a9\2\2\u0872\u0877\7")
        buf.write(u"\u00ab\2\2\u0873\u0877\7\u00a7\2\2\u0874\u0877\7\u009e")
        buf.write(u"\2\2\u0875\u0877\7\u009f\2\2\u0876\u0871\3\2\2\2\u0876")
        buf.write(u"\u0872\3\2\2\2\u0876\u0873\3\2\2\2\u0876\u0874\3\2\2")
        buf.write(u"\2\u0876\u0875\3\2\2\2\u0877\u0181\3\2\2\2\u0878\u0879")
        buf.write(u"\t\n\2\2\u0879\u0183\3\2\2\2\u087a\u087b\7\u0089\2\2")
        buf.write(u"\u087b\u087c\5\u0186\u00c4\2\u087c\u087d\7\22\2\2\u087d")
        buf.write(u"\u0882\3\2\2\2\u087e\u087f\5\u0186\u00c4\2\u087f\u0880")
        buf.write(u"\7\22\2\2\u0880\u0882\3\2\2\2\u0881\u087a\3\2\2\2\u0881")
        buf.write(u"\u087e\3\2\2\2\u0882\u0185\3\2\2\2\u0883\u0884\b\u00c4")
        buf.write(u"\1\2\u0884\u0885\5\u0188\u00c5\2\u0885\u088a\3\2\2\2")
        buf.write(u"\u0886\u0887\f\3\2\2\u0887\u0889\5\u018e\u00c8\2\u0888")
        buf.write(u"\u0886\3\2\2\2\u0889\u088c\3\2\2\2\u088a\u0888\3\2\2")
        buf.write(u"\2\u088a\u088b\3\2\2\2\u088b\u0187\3\2\2\2\u088c\u088a")
        buf.write(u"\3\2\2\2\u088d\u0893\5\u018a\u00c6\2\u088e\u0893\5\u018c")
        buf.write(u"\u00c7\2\u088f\u0893\5\u0196\u00cc\2\u0890\u0893\5\u0198")
        buf.write(u"\u00cd\2\u0891\u0893\5\u019a\u00ce\2\u0892\u088d\3\2")
        buf.write(u"\2\2\u0892\u088e\3\2\2\2\u0892\u088f\3\2\2\2\u0892\u0890")
        buf.write(u"\3\2\2\2\u0892\u0891\3\2\2\2\u0893\u0189\3\2\2\2\u0894")
        buf.write(u"\u0895\5\u00fe\u0080\2\u0895\u018b\3\2\2\2\u0896\u0897")
        buf.write(u"\5\u0122\u0092\2\u0897\u0898\5\u0190\u00c9\2\u0898\u018d")
        buf.write(u"\3\2\2\2\u0899\u089a\7\25\2\2\u089a\u089d\5\u0190\u00c9")
        buf.write(u"\2\u089b\u089d\5\u0194\u00cb\2\u089c\u0899\3\2\2\2\u089c")
        buf.write(u"\u089b\3\2\2\2\u089d\u018f\3\2\2\2\u089e\u089f\5\u019c")
        buf.write(u"\u00cf\2\u089f\u08a1\7\26\2\2\u08a0\u08a2\5\u0192\u00ca")
        buf.write(u"\2\u08a1\u08a0\3\2\2\2\u08a1\u08a2\3\2\2\2\u08a2\u08a3")
        buf.write(u"\3\2\2\2\u08a3\u08a4\7\27\2\2\u08a4\u0191\3\2\2\2\u08a5")
        buf.write(u"\u08a6\b\u00ca\1\2\u08a6\u08a7\5\u0186\u00c4\2\u08a7")
        buf.write(u"\u08ad\3\2\2\2\u08a8\u08a9\f\3\2\2\u08a9\u08aa\7\23\2")
        buf.write(u"\2\u08aa\u08ac\5\u0186\u00c4\2\u08ab\u08a8\3\2\2\2\u08ac")
        buf.write(u"\u08af\3\2\2\2\u08ad\u08ab\3\2\2\2\u08ad\u08ae\3\2\2")
        buf.write(u"\2\u08ae\u0193\3\2\2\2\u08af\u08ad\3\2\2\2\u08b0\u08b1")
        buf.write(u"\7\30\2\2\u08b1\u08b2\5\u0186\u00c4\2\u08b2\u08b3\7\31")
        buf.write(u"\2\2\u08b3\u0195\3\2\2\2\u08b4\u08b5\7\26\2\2\u08b5\u08b6")
        buf.write(u"\5\u0186\u00c4\2\u08b6\u08b7\7\27\2\2\u08b7\u0197\3\2")
        buf.write(u"\2\2\u08b8\u08b9\b\u00cd\1\2\u08b9\u08bc\7\u00a6\2\2")
        buf.write(u"\u08ba\u08bc\5\u019c\u00cf\2\u08bb\u08b8\3\2\2\2\u08bb")
        buf.write(u"\u08ba\3\2\2\2\u08bc\u08c2\3\2\2\2\u08bd\u08be\f\3\2")
        buf.write(u"\2\u08be\u08bf\7\25\2\2\u08bf\u08c1\5\u019c\u00cf\2\u08c0")
        buf.write(u"\u08bd\3\2\2\2\u08c1\u08c4\3\2\2\2\u08c2\u08c0\3\2\2")
        buf.write(u"\2\u08c2\u08c3\3\2\2\2\u08c3\u0199\3\2\2\2\u08c4\u08c2")
        buf.write(u"\3\2\2\2\u08c5\u08cb\7\u00a9\2\2\u08c6\u08cb\7\u00ab")
        buf.write(u"\2\2\u08c7\u08cb\7\u00a7\2\2\u08c8\u08cb\7\u009e\2\2")
        buf.write(u"\u08c9\u08cb\7\u009f\2\2\u08ca\u08c5\3\2\2\2\u08ca\u08c6")
        buf.write(u"\3\2\2\2\u08ca\u08c7\3\2\2\2\u08ca\u08c8\3\2\2\2\u08ca")
        buf.write(u"\u08c9\3\2\2\2\u08cb\u019b\3\2\2\2\u08cc\u08cd\t\13\2")
        buf.write(u"\2\u08cd\u019d\3\2\2\2\u00bb\u01a4\u01a7\u01c0\u01c5")
        buf.write(u"\u01d3\u01d9\u01db\u01dd\u01e4\u01e9\u01f4\u01fb\u0208")
        buf.write(u"\u0216\u022a\u0241\u024c\u0253\u025c\u0265\u026e\u0283")
        buf.write(u"\u028b\u0290\u0296\u029b\u02a4\u02a9\u02ae\u02c6\u02d1")
        buf.write(u"\u02d5\u02ea\u0304\u0309\u0312\u031b\u0324\u0341\u0354")
        buf.write(u"\u035a\u037c\u0385\u039c\u03aa\u03b3\u03bc\u03d3\u03d9")
        buf.write(u"\u03ed\u0455\u0457\u0463\u046e\u047d\u0482\u0489\u0490")
        buf.write(u"\u0499\u04a0\u04b5\u04c0\u04c4\u04c9\u04ce\u04d0\u04d4")
        buf.write(u"\u04dd\u04ed\u04f6\u04fc\u0501\u0508\u0510\u051b\u0523")
        buf.write(u"\u052b\u0531\u0539\u0542\u054a\u0557\u055a\u055e\u0563")
        buf.write(u"\u0567\u0570\u0585\u058f\u0591\u0596\u05a6\u05ab\u05b4")
        buf.write(u"\u05bb\u05c0\u05c5\u05d4\u05d9\u05dc\u05e0\u05e5\u05ec")
        buf.write(u"\u05f7\u05f9\u0602\u060a\u0612\u0618\u0624\u0628\u0632")
        buf.write(u"\u0637\u063d\u0644\u0649\u0650\u0658\u065f\u0669\u0676")
        buf.write(u"\u067a\u067d\u0681\u0684\u068c\u0695\u069e\u06a7\u06b8")
        buf.write(u"\u06c8\u06cf\u06d6\u06e0\u06e7\u06ea\u06ee\u06f3\u06f7")
        buf.write(u"\u0702\u0705\u070c\u071c\u0729\u0730\u0741\u0749\u074d")
        buf.write(u"\u0755\u0777\u0780\u078a\u0796\u079b\u07a7\u07b9\u07c0")
        buf.write(u"\u07c9\u07d0\u07d8\u07dd\u07e7\u07f1\u0801\u080b\u0812")
        buf.write(u"\u081a\u0825\u082e\u0836\u0840\u0845\u0851\u0864\u086e")
        buf.write(u"\u0876\u0881\u088a\u0892\u089c\u08a1\u08ad\u08bb\u08c2")
        buf.write(u"\u08ca")
        return buf.getvalue()
		

class MParser ( AbstractParser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"'\t'", u"' '", u"<INVALID>", 
                     u"'Java:'", u"'C#:'", u"'Python2:'", u"'Python3:'", 
                     u"'JavaScript:'", u"'Swift:'", u"':'", u"';'", u"','", 
                     u"'..'", u"'.'", u"'('", u"')'", u"'['", u"']'", u"'{'", 
                     u"'}'", u"'?'", u"'!'", u"'&'", u"'&&'", u"'|'", u"'||'", 
                     u"'+'", u"'-'", u"'*'", u"'/'", u"'\\'", u"'%'", u"'>'", 
                     u"'>='", u"'<'", u"'<='", u"'<>'", u"'='", u"'!='", 
                     u"'=='", u"'~='", u"'~'", u"'<-'", u"'->'", u"'Boolean'", 
                     u"'Character'", u"'Text'", u"'Integer'", u"'Decimal'", 
                     u"'Date'", u"'Time'", u"'DateTime'", u"'Period'", u"'Method'", 
                     u"'Code'", u"'Document'", u"'Blob'", u"'Image'", u"'UUID'", 
                     u"'Iterator'", u"'Cursor'", u"'abstract'", u"'all'", 
                     u"'always'", u"'and'", u"'any'", u"'as'", u"<INVALID>", 
                     u"'attr'", u"'attribute'", u"'attributes'", u"'bindings'", 
                     u"'break'", u"'by'", u"'case'", u"'catch'", u"'category'", 
                     u"'class'", u"'close'", u"'contains'", u"'def'", u"'default'", 
                     u"'define'", u"'delete'", u"<INVALID>", u"'do'", u"'doing'", 
                     u"'each'", u"'else'", u"'enum'", u"'enumerated'", u"'except'", 
                     u"'execute'", u"'expecting'", u"'extends'", u"'fetch'", 
                     u"'filtered'", u"'finally'", u"'flush'", u"'for'", 
                     u"'from'", u"'getter'", u"'if'", u"'in'", u"'index'", 
                     u"'invoke'", u"'is'", u"'matching'", u"'method'", u"'methods'", 
                     u"'modulo'", u"'mutable'", u"'native'", u"'None'", 
                     u"'not'", u"<INVALID>", u"'null'", u"'on'", u"'one'", 
                     u"'open'", u"'operator'", u"'or'", u"'order'", u"'otherwise'", 
                     u"'pass'", u"'raise'", u"'read'", u"'receiving'", u"'resource'", 
                     u"'return'", u"'returning'", u"'rows'", u"'self'", 
                     u"'setter'", u"'singleton'", u"'sorted'", u"'storable'", 
                     u"'store'", u"'switch'", u"'test'", u"'this'", u"'throw'", 
                     u"'to'", u"'try'", u"'verifying'", u"'with'", u"'when'", 
                     u"'where'", u"'while'", u"'write'", u"<INVALID>", u"<INVALID>", 
                     u"'MIN_INTEGER'", u"'MAX_INTEGER'" ]

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
                      u"TIME", u"DATETIME", u"PERIOD", u"METHOD_T", u"CODE", 
                      u"DOCUMENT", u"BLOB", u"IMAGE", u"UUID", u"ITERATOR", 
                      u"CURSOR", u"ABSTRACT", u"ALL", u"ALWAYS", u"AND", 
                      u"ANY", u"AS", u"ASC", u"ATTR", u"ATTRIBUTE", u"ATTRIBUTES", 
                      u"BINDINGS", u"BREAK", u"BY", u"CASE", u"CATCH", u"CATEGORY", 
                      u"CLASS", u"CLOSE", u"CONTAINS", u"DEF", u"DEFAULT", 
                      u"DEFINE", u"DELETE", u"DESC", u"DO", u"DOING", u"EACH", 
                      u"ELSE", u"ENUM", u"ENUMERATED", u"EXCEPT", u"EXECUTE", 
                      u"EXPECTING", u"EXTENDS", u"FETCH", u"FILTERED", u"FINALLY", 
                      u"FLUSH", u"FOR", u"FROM", u"GETTER", u"IF", u"IN", 
                      u"INDEX", u"INVOKE", u"IS", u"MATCHING", u"METHOD", 
                      u"METHODS", u"MODULO", u"MUTABLE", u"NATIVE", u"NONE", 
                      u"NOT", u"NOTHING", u"NULL", u"ON", u"ONE", u"OPEN", 
                      u"OPERATOR", u"OR", u"ORDER", u"OTHERWISE", u"PASS", 
                      u"RAISE", u"READ", u"RECEIVING", u"RESOURCE", u"RETURN", 
                      u"RETURNING", u"ROWS", u"SELF", u"SETTER", u"SINGLETON", 
                      u"SORTED", u"STORABLE", u"STORE", u"SWITCH", u"TEST", 
                      u"THIS", u"THROW", u"TO", u"TRY", u"VERIFYING", u"WITH", 
                      u"WHEN", u"WHERE", u"WHILE", u"WRITE", u"BOOLEAN_LITERAL", 
                      u"CHAR_LITERAL", u"MIN_INTEGER", u"MAX_INTEGER", u"SYMBOL_IDENTIFIER", 
                      u"TYPE_IDENTIFIER", u"VARIABLE_IDENTIFIER", u"NATIVE_IDENTIFIER", 
                      u"DOLLAR_IDENTIFIER", u"TEXT_LITERAL", u"UUID_LITERAL", 
                      u"INTEGER_LITERAL", u"HEXA_LITERAL", u"DECIMAL_LITERAL", 
                      u"DATETIME_LITERAL", u"TIME_LITERAL", u"DATE_LITERAL", 
                      u"PERIOD_LITERAL" ]

    RULE_enum_category_declaration = 0
    RULE_enum_native_declaration = 1
    RULE_native_symbol = 2
    RULE_category_symbol = 3
    RULE_attribute_declaration = 4
    RULE_index_clause = 5
    RULE_concrete_category_declaration = 6
    RULE_singleton_category_declaration = 7
    RULE_derived_list = 8
    RULE_operator_method_declaration = 9
    RULE_setter_method_declaration = 10
    RULE_native_setter_declaration = 11
    RULE_getter_method_declaration = 12
    RULE_native_getter_declaration = 13
    RULE_native_category_declaration = 14
    RULE_native_resource_declaration = 15
    RULE_native_category_bindings = 16
    RULE_native_category_binding_list = 17
    RULE_abstract_method_declaration = 18
    RULE_concrete_method_declaration = 19
    RULE_native_method_declaration = 20
    RULE_test_method_declaration = 21
    RULE_assertion = 22
    RULE_typed_argument = 23
    RULE_statement = 24
    RULE_flush_statement = 25
    RULE_store_statement = 26
    RULE_method_call = 27
    RULE_method_selector = 28
    RULE_callable_parent = 29
    RULE_callable_selector = 30
    RULE_with_resource_statement = 31
    RULE_with_singleton_statement = 32
    RULE_switch_statement = 33
    RULE_switch_case_statement = 34
    RULE_for_each_statement = 35
    RULE_do_while_statement = 36
    RULE_while_statement = 37
    RULE_if_statement = 38
    RULE_else_if_statement_list = 39
    RULE_raise_statement = 40
    RULE_try_statement = 41
    RULE_catch_statement = 42
    RULE_break_statement = 43
    RULE_return_statement = 44
    RULE_expression = 45
    RULE_closure_expression = 46
    RULE_instance_expression = 47
    RULE_method_expression = 48
    RULE_instance_selector = 49
    RULE_blob_expression = 50
    RULE_document_expression = 51
    RULE_constructor_expression = 52
    RULE_argument_assignment_list = 53
    RULE_argument_assignment = 54
    RULE_write_statement = 55
    RULE_filtered_list_suffix = 56
    RULE_fetch_store_expression = 57
    RULE_sorted_expression = 58
    RULE_assign_instance_statement = 59
    RULE_child_instance = 60
    RULE_assign_tuple_statement = 61
    RULE_lfs = 62
    RULE_lfp = 63
    RULE_indent = 64
    RULE_dedent = 65
    RULE_null_literal = 66
    RULE_declaration_list = 67
    RULE_declarations = 68
    RULE_declaration = 69
    RULE_resource_declaration = 70
    RULE_enum_declaration = 71
    RULE_native_symbol_list = 72
    RULE_category_symbol_list = 73
    RULE_symbol_list = 74
    RULE_attribute_constraint = 75
    RULE_list_literal = 76
    RULE_set_literal = 77
    RULE_expression_list = 78
    RULE_range_literal = 79
    RULE_typedef = 80
    RULE_primary_type = 81
    RULE_native_type = 82
    RULE_category_type = 83
    RULE_mutable_category_type = 84
    RULE_code_type = 85
    RULE_category_declaration = 86
    RULE_type_identifier_list = 87
    RULE_method_identifier = 88
    RULE_identifier = 89
    RULE_variable_identifier = 90
    RULE_attribute_identifier = 91
    RULE_type_identifier = 92
    RULE_symbol_identifier = 93
    RULE_argument_list = 94
    RULE_argument = 95
    RULE_operator_argument = 96
    RULE_named_argument = 97
    RULE_code_argument = 98
    RULE_category_or_any_type = 99
    RULE_any_type = 100
    RULE_member_method_declaration_list = 101
    RULE_member_method_declaration = 102
    RULE_native_member_method_declaration_list = 103
    RULE_native_member_method_declaration = 104
    RULE_native_category_binding = 105
    RULE_python_category_binding = 106
    RULE_python_module = 107
    RULE_javascript_category_binding = 108
    RULE_javascript_module = 109
    RULE_variable_identifier_list = 110
    RULE_attribute_identifier_list = 111
    RULE_method_declaration = 112
    RULE_comment_statement = 113
    RULE_native_statement_list = 114
    RULE_native_statement = 115
    RULE_python_native_statement = 116
    RULE_javascript_native_statement = 117
    RULE_statement_list = 118
    RULE_assertion_list = 119
    RULE_switch_case_statement_list = 120
    RULE_catch_statement_list = 121
    RULE_literal_collection = 122
    RULE_atomic_literal = 123
    RULE_literal_list_literal = 124
    RULE_selectable_expression = 125
    RULE_this_expression = 126
    RULE_parenthesis_expression = 127
    RULE_literal_expression = 128
    RULE_collection_literal = 129
    RULE_tuple_literal = 130
    RULE_dict_literal = 131
    RULE_expression_tuple = 132
    RULE_dict_entry_list = 133
    RULE_dict_entry = 134
    RULE_slice_arguments = 135
    RULE_assign_variable_statement = 136
    RULE_assignable_instance = 137
    RULE_is_expression = 138
    RULE_read_all_expression = 139
    RULE_read_one_expression = 140
    RULE_order_by_list = 141
    RULE_order_by = 142
    RULE_operator = 143
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
    RULE_python_selector_expression = 170
    RULE_python_method_expression = 171
    RULE_python_argument_list = 172
    RULE_python_ordinal_argument_list = 173
    RULE_python_named_argument_list = 174
    RULE_python_parenthesis_expression = 175
    RULE_python_identifier_expression = 176
    RULE_python_literal_expression = 177
    RULE_python_identifier = 178
    RULE_java_statement = 179
    RULE_java_expression = 180
    RULE_java_primary_expression = 181
    RULE_java_this_expression = 182
    RULE_java_new_expression = 183
    RULE_java_selector_expression = 184
    RULE_java_method_expression = 185
    RULE_java_arguments = 186
    RULE_java_item_expression = 187
    RULE_java_parenthesis_expression = 188
    RULE_java_identifier_expression = 189
    RULE_java_class_identifier_expression = 190
    RULE_java_literal_expression = 191
    RULE_java_identifier = 192
    RULE_csharp_statement = 193
    RULE_csharp_expression = 194
    RULE_csharp_primary_expression = 195
    RULE_csharp_this_expression = 196
    RULE_csharp_new_expression = 197
    RULE_csharp_selector_expression = 198
    RULE_csharp_method_expression = 199
    RULE_csharp_arguments = 200
    RULE_csharp_item_expression = 201
    RULE_csharp_parenthesis_expression = 202
    RULE_csharp_identifier_expression = 203
    RULE_csharp_literal_expression = 204
    RULE_csharp_identifier = 205

    ruleNames =  [ u"enum_category_declaration", u"enum_native_declaration", 
                   u"native_symbol", u"category_symbol", u"attribute_declaration", 
                   u"index_clause", u"concrete_category_declaration", u"singleton_category_declaration", 
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
                   u"document_expression", u"constructor_expression", u"argument_assignment_list", 
                   u"argument_assignment", u"write_statement", u"filtered_list_suffix", 
                   u"fetch_store_expression", u"sorted_expression", u"assign_instance_statement", 
                   u"child_instance", u"assign_tuple_statement", u"lfs", 
                   u"lfp", u"indent", u"dedent", u"null_literal", u"declaration_list", 
                   u"declarations", u"declaration", u"resource_declaration", 
                   u"enum_declaration", u"native_symbol_list", u"category_symbol_list", 
                   u"symbol_list", u"attribute_constraint", u"list_literal", 
                   u"set_literal", u"expression_list", u"range_literal", 
                   u"typedef", u"primary_type", u"native_type", u"category_type", 
                   u"mutable_category_type", u"code_type", u"category_declaration", 
                   u"type_identifier_list", u"method_identifier", u"identifier", 
                   u"variable_identifier", u"attribute_identifier", u"type_identifier", 
                   u"symbol_identifier", u"argument_list", u"argument", 
                   u"operator_argument", u"named_argument", u"code_argument", 
                   u"category_or_any_type", u"any_type", u"member_method_declaration_list", 
                   u"member_method_declaration", u"native_member_method_declaration_list", 
                   u"native_member_method_declaration", u"native_category_binding", 
                   u"python_category_binding", u"python_module", u"javascript_category_binding", 
                   u"javascript_module", u"variable_identifier_list", u"attribute_identifier_list", 
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
                   u"javascript_statement", u"javascript_expression", u"javascript_primary_expression", 
                   u"javascript_this_expression", u"javascript_new_expression", 
                   u"javascript_selector_expression", u"javascript_method_expression", 
                   u"javascript_arguments", u"javascript_item_expression", 
                   u"javascript_parenthesis_expression", u"javascript_identifier_expression", 
                   u"javascript_literal_expression", u"javascript_identifier", 
                   u"python_statement", u"python_expression", u"python_primary_expression", 
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
    METHOD_T=59
    CODE=60
    DOCUMENT=61
    BLOB=62
    IMAGE=63
    UUID=64
    ITERATOR=65
    CURSOR=66
    ABSTRACT=67
    ALL=68
    ALWAYS=69
    AND=70
    ANY=71
    AS=72
    ASC=73
    ATTR=74
    ATTRIBUTE=75
    ATTRIBUTES=76
    BINDINGS=77
    BREAK=78
    BY=79
    CASE=80
    CATCH=81
    CATEGORY=82
    CLASS=83
    CLOSE=84
    CONTAINS=85
    DEF=86
    DEFAULT=87
    DEFINE=88
    DELETE=89
    DESC=90
    DO=91
    DOING=92
    EACH=93
    ELSE=94
    ENUM=95
    ENUMERATED=96
    EXCEPT=97
    EXECUTE=98
    EXPECTING=99
    EXTENDS=100
    FETCH=101
    FILTERED=102
    FINALLY=103
    FLUSH=104
    FOR=105
    FROM=106
    GETTER=107
    IF=108
    IN=109
    INDEX=110
    INVOKE=111
    IS=112
    MATCHING=113
    METHOD=114
    METHODS=115
    MODULO=116
    MUTABLE=117
    NATIVE=118
    NONE=119
    NOT=120
    NOTHING=121
    NULL=122
    ON=123
    ONE=124
    OPEN=125
    OPERATOR=126
    OR=127
    ORDER=128
    OTHERWISE=129
    PASS=130
    RAISE=131
    READ=132
    RECEIVING=133
    RESOURCE=134
    RETURN=135
    RETURNING=136
    ROWS=137
    SELF=138
    SETTER=139
    SINGLETON=140
    SORTED=141
    STORABLE=142
    STORE=143
    SWITCH=144
    TEST=145
    THIS=146
    THROW=147
    TO=148
    TRY=149
    VERIFYING=150
    WITH=151
    WHEN=152
    WHERE=153
    WHILE=154
    WRITE=155
    BOOLEAN_LITERAL=156
    CHAR_LITERAL=157
    MIN_INTEGER=158
    MAX_INTEGER=159
    SYMBOL_IDENTIFIER=160
    TYPE_IDENTIFIER=161
    VARIABLE_IDENTIFIER=162
    NATIVE_IDENTIFIER=163
    DOLLAR_IDENTIFIER=164
    TEXT_LITERAL=165
    UUID_LITERAL=166
    INTEGER_LITERAL=167
    HEXA_LITERAL=168
    DECIMAL_LITERAL=169
    DATETIME_LITERAL=170
    TIME_LITERAL=171
    DATE_LITERAL=172
    PERIOD_LITERAL=173

    def __init__(self, input):
        super(MParser, self).__init__(input)
        self.checkVersion("4.5")
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
            if isinstance( listener, MParserListener ):
                listener.enterEnum_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitEnum_category_declaration(self)




    def enum_category_declaration(self):

        localctx = MParser.Enum_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_enum_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(MParser.ENUM)
            self.state = 413 
            localctx.name = self.type_identifier()
            self.state = 414
            self.match(MParser.LPAR)
            self.state = 421
            token = self._input.LA(1)
            if token in [MParser.TYPE_IDENTIFIER]:
                self.state = 415 
                localctx.derived = self.type_identifier()
                self.state = 418
                _la = self._input.LA(1)
                if _la==MParser.COMMA:
                    self.state = 416
                    self.match(MParser.COMMA)
                    self.state = 417 
                    localctx.attrs = self.attribute_identifier_list()



            elif token in [MParser.STORABLE, MParser.VARIABLE_IDENTIFIER]:
                self.state = 420 
                localctx.attrs = self.attribute_identifier_list()

            else:
                raise NoViableAltException(self)

            self.state = 423
            self.match(MParser.RPAR)
            self.state = 424
            self.match(MParser.COLON)
            self.state = 425 
            self.indent()
            self.state = 426 
            localctx.symbols = self.category_symbol_list()
            self.state = 427 
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
            if isinstance( listener, MParserListener ):
                listener.enterEnum_native_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitEnum_native_declaration(self)




    def enum_native_declaration(self):

        localctx = MParser.Enum_native_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_enum_native_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(MParser.ENUM)
            self.state = 430 
            localctx.name = self.type_identifier()
            self.state = 431
            self.match(MParser.LPAR)
            self.state = 432 
            localctx.typ = self.native_type()
            self.state = 433
            self.match(MParser.RPAR)
            self.state = 434
            self.match(MParser.COLON)
            self.state = 435 
            self.indent()
            self.state = 436 
            localctx.symbols = self.native_symbol_list()
            self.state = 437 
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
            if isinstance( listener, MParserListener ):
                listener.enterNative_symbol(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitNative_symbol(self)




    def native_symbol(self):

        localctx = MParser.Native_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_native_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439 
            localctx.name = self.symbol_identifier()
            self.state = 440
            self.match(MParser.EQ)
            self.state = 441 
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
            if isinstance( listener, MParserListener ):
                listener.enterCategory_symbol(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCategory_symbol(self)




    def category_symbol(self):

        localctx = MParser.Category_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_category_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443 
            localctx.name = self.symbol_identifier()
            self.state = 444
            self.match(MParser.LPAR)
            self.state = 446
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (MParser.EXECUTE - 98)) | (1 << (MParser.FETCH - 98)) | (1 << (MParser.MUTABLE - 98)) | (1 << (MParser.NONE - 98)) | (1 << (MParser.NOT - 98)) | (1 << (MParser.READ - 98)) | (1 << (MParser.SELF - 98)) | (1 << (MParser.SORTED - 98)) | (1 << (MParser.THIS - 98)) | (1 << (MParser.BOOLEAN_LITERAL - 98)) | (1 << (MParser.CHAR_LITERAL - 98)) | (1 << (MParser.MIN_INTEGER - 98)) | (1 << (MParser.MAX_INTEGER - 98)) | (1 << (MParser.SYMBOL_IDENTIFIER - 98)) | (1 << (MParser.TYPE_IDENTIFIER - 98)))) != 0) or ((((_la - 162)) & ~0x3f) == 0 and ((1 << (_la - 162)) & ((1 << (MParser.VARIABLE_IDENTIFIER - 162)) | (1 << (MParser.TEXT_LITERAL - 162)) | (1 << (MParser.UUID_LITERAL - 162)) | (1 << (MParser.INTEGER_LITERAL - 162)) | (1 << (MParser.HEXA_LITERAL - 162)) | (1 << (MParser.DECIMAL_LITERAL - 162)) | (1 << (MParser.DATETIME_LITERAL - 162)) | (1 << (MParser.TIME_LITERAL - 162)) | (1 << (MParser.DATE_LITERAL - 162)) | (1 << (MParser.PERIOD_LITERAL - 162)))) != 0):
                self.state = 445 
                localctx.args = self.argument_assignment_list(0)


            self.state = 448
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
            if isinstance( listener, MParserListener ):
                listener.enterAttribute_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitAttribute_declaration(self)




    def attribute_declaration(self):

        localctx = MParser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            _la = self._input.LA(1)
            if _la==MParser.STORABLE:
                self.state = 450
                self.match(MParser.STORABLE)


            self.state = 453
            self.match(MParser.ATTR)
            self.state = 454 
            localctx.name = self.attribute_identifier()
            self.state = 455
            self.match(MParser.LPAR)
            self.state = 456 
            localctx.typ = self.typedef(0)
            self.state = 457
            self.match(MParser.RPAR)
            self.state = 458
            self.match(MParser.COLON)
            self.state = 459 
            self.indent()
            self.state = 475
            token = self._input.LA(1)
            if token in [MParser.PASS]:
                self.state = 460
                self.match(MParser.PASS)

            elif token in [MParser.IN, MParser.INDEX, MParser.MATCHING]:
                self.state = 473
                token = self._input.LA(1)
                if token in [MParser.IN, MParser.MATCHING]:
                    self.state = 461 
                    localctx.match = self.attribute_constraint()
                    self.state = 465
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        self.state = 462 
                        self.lfp()
                        self.state = 463 
                        localctx.indices = self.index_clause()



                elif token in [MParser.INDEX]:
                    self.state = 467 
                    localctx.indices = self.index_clause()
                    self.state = 471
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        self.state = 468 
                        self.lfp()
                        self.state = 469 
                        localctx.match = self.attribute_constraint()



                else:
                    raise NoViableAltException(self)


            else:
                raise NoViableAltException(self)

            self.state = 477 
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
            if isinstance( listener, MParserListener ):
                listener.enterIndex_clause(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitIndex_clause(self)




    def index_clause(self):

        localctx = MParser.Index_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_index_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.match(MParser.INDEX)
            self.state = 480
            self.match(MParser.LPAR)
            self.state = 482
            _la = self._input.LA(1)
            if _la==MParser.VARIABLE_IDENTIFIER:
                self.state = 481 
                localctx.indices = self.variable_identifier_list()


            self.state = 484
            self.match(MParser.RPAR)
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
            if isinstance( listener, MParserListener ):
                listener.enterConcrete_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitConcrete_category_declaration(self)




    def concrete_category_declaration(self):

        localctx = MParser.Concrete_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_concrete_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            _la = self._input.LA(1)
            if _la==MParser.STORABLE:
                self.state = 486
                self.match(MParser.STORABLE)


            self.state = 489
            _la = self._input.LA(1)
            if not(_la==MParser.CATEGORY or _la==MParser.CLASS):
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 490 
            localctx.name = self.type_identifier()
            self.state = 491
            self.match(MParser.LPAR)
            self.state = 498
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 492 
                localctx.derived = self.derived_list()
                pass

            elif la_ == 2:
                self.state = 493 
                localctx.attrs = self.attribute_identifier_list()
                pass

            elif la_ == 3:
                self.state = 494 
                localctx.derived = self.derived_list()
                self.state = 495
                self.match(MParser.COMMA)
                self.state = 496 
                localctx.attrs = self.attribute_identifier_list()
                pass


            self.state = 500
            self.match(MParser.RPAR)
            self.state = 501
            self.match(MParser.COLON)
            self.state = 502 
            self.indent()
            self.state = 505
            token = self._input.LA(1)
            if token in [MParser.ABSTRACT, MParser.DEF]:
                self.state = 503 
                localctx.methods = self.member_method_declaration_list()

            elif token in [MParser.PASS]:
                self.state = 504
                self.match(MParser.PASS)

            else:
                raise NoViableAltException(self)

            self.state = 507 
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
            if isinstance( listener, MParserListener ):
                listener.enterSingleton_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitSingleton_category_declaration(self)




    def singleton_category_declaration(self):

        localctx = MParser.Singleton_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_singleton_category_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            self.match(MParser.SINGLETON)
            self.state = 510 
            localctx.name = self.type_identifier()
            self.state = 511
            self.match(MParser.LPAR)
            self.state = 512 
            localctx.attrs = self.attribute_identifier_list()
            self.state = 513
            self.match(MParser.RPAR)
            self.state = 514
            self.match(MParser.COLON)
            self.state = 515 
            self.indent()
            self.state = 518
            token = self._input.LA(1)
            if token in [MParser.ABSTRACT, MParser.DEF]:
                self.state = 516 
                localctx.methods = self.member_method_declaration_list()

            elif token in [MParser.PASS]:
                self.state = 517
                self.match(MParser.PASS)

            else:
                raise NoViableAltException(self)

            self.state = 520 
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
            if isinstance( listener, MParserListener ):
                listener.enterDerived_list(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitDerived_list(self)




    def derived_list(self):

        localctx = MParser.Derived_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_derived_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522 
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
            if isinstance( listener, MParserListener ):
                listener.enterOperator_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitOperator_method_declaration(self)




    def operator_method_declaration(self):

        localctx = MParser.Operator_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_operator_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self.match(MParser.DEF)
            self.state = 525
            self.match(MParser.OPERATOR)
            self.state = 526 
            localctx.op = self.operator()
            self.state = 527
            self.match(MParser.LPAR)
            self.state = 528 
            localctx.arg = self.operator_argument()
            self.state = 529
            self.match(MParser.RPAR)
            self.state = 532
            _la = self._input.LA(1)
            if _la==MParser.RARROW:
                self.state = 530
                self.match(MParser.RARROW)
                self.state = 531 
                localctx.typ = self.typedef(0)


            self.state = 534
            self.match(MParser.COLON)
            self.state = 535 
            self.indent()
            self.state = 536 
            localctx.stmts = self.statement_list()
            self.state = 537 
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
            if isinstance( listener, MParserListener ):
                listener.enterSetter_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitSetter_method_declaration(self)




    def setter_method_declaration(self):

        localctx = MParser.Setter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_setter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            self.match(MParser.DEF)
            self.state = 540 
            localctx.name = self.variable_identifier()
            self.state = 541
            self.match(MParser.SETTER)
            self.state = 542
            self.match(MParser.LPAR)
            self.state = 543
            self.match(MParser.RPAR)
            self.state = 544
            self.match(MParser.COLON)
            self.state = 545 
            self.indent()
            self.state = 546 
            localctx.stmts = self.statement_list()
            self.state = 547 
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
            if isinstance( listener, MParserListener ):
                listener.enterNative_setter_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitNative_setter_declaration(self)




    def native_setter_declaration(self):

        localctx = MParser.Native_setter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_native_setter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self.match(MParser.DEF)
            self.state = 550 
            localctx.name = self.variable_identifier()
            self.state = 552
            _la = self._input.LA(1)
            if _la==MParser.NATIVE:
                self.state = 551
                self.match(MParser.NATIVE)


            self.state = 554
            self.match(MParser.SETTER)
            self.state = 555
            self.match(MParser.LPAR)
            self.state = 556
            self.match(MParser.RPAR)
            self.state = 557
            self.match(MParser.COLON)
            self.state = 558 
            self.indent()
            self.state = 559 
            localctx.stmts = self.native_statement_list()
            self.state = 560 
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
            if isinstance( listener, MParserListener ):
                listener.enterGetter_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitGetter_method_declaration(self)




    def getter_method_declaration(self):

        localctx = MParser.Getter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_getter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            self.match(MParser.DEF)
            self.state = 563 
            localctx.name = self.variable_identifier()
            self.state = 564
            self.match(MParser.GETTER)
            self.state = 565
            self.match(MParser.LPAR)
            self.state = 566
            self.match(MParser.RPAR)
            self.state = 567
            self.match(MParser.COLON)
            self.state = 568 
            self.indent()
            self.state = 569 
            localctx.stmts = self.statement_list()
            self.state = 570 
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
            if isinstance( listener, MParserListener ):
                listener.enterNative_getter_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitNative_getter_declaration(self)




    def native_getter_declaration(self):

        localctx = MParser.Native_getter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_native_getter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            self.match(MParser.DEF)
            self.state = 573 
            localctx.name = self.variable_identifier()
            self.state = 575
            _la = self._input.LA(1)
            if _la==MParser.NATIVE:
                self.state = 574
                self.match(MParser.NATIVE)


            self.state = 577
            self.match(MParser.GETTER)
            self.state = 578
            self.match(MParser.LPAR)
            self.state = 579
            self.match(MParser.RPAR)
            self.state = 580
            self.match(MParser.COLON)
            self.state = 581 
            self.indent()
            self.state = 582 
            localctx.stmts = self.native_statement_list()
            self.state = 583 
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
            if isinstance( listener, MParserListener ):
                listener.enterNative_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitNative_category_declaration(self)




    def native_category_declaration(self):

        localctx = MParser.Native_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_native_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            _la = self._input.LA(1)
            if _la==MParser.STORABLE:
                self.state = 585
                self.match(MParser.STORABLE)


            self.state = 588
            self.match(MParser.NATIVE)
            self.state = 589
            _la = self._input.LA(1)
            if not(_la==MParser.CATEGORY or _la==MParser.CLASS):
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 590 
            localctx.name = self.type_identifier()
            self.state = 591
            self.match(MParser.LPAR)
            self.state = 593
            _la = self._input.LA(1)
            if _la==MParser.STORABLE or _la==MParser.VARIABLE_IDENTIFIER:
                self.state = 592 
                localctx.attrs = self.attribute_identifier_list()


            self.state = 595
            self.match(MParser.RPAR)
            self.state = 596
            self.match(MParser.COLON)
            self.state = 597 
            self.indent()
            self.state = 598 
            localctx.bindings = self.native_category_bindings()
            self.state = 602
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 599 
                self.lfp()
                self.state = 600 
                localctx.methods = self.native_member_method_declaration_list()


            self.state = 604 
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


        def lfp(self):
            return self.getTypedRuleContext(MParser.LfpContext,0)


        def attribute_identifier_list(self):
            return self.getTypedRuleContext(MParser.Attribute_identifier_listContext,0)


        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(MParser.Native_member_method_declaration_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_native_resource_declaration

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterNative_resource_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitNative_resource_declaration(self)




    def native_resource_declaration(self):

        localctx = MParser.Native_resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_native_resource_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 606
            self.match(MParser.NATIVE)
            self.state = 607
            self.match(MParser.RESOURCE)
            self.state = 608 
            localctx.name = self.type_identifier()
            self.state = 609
            self.match(MParser.LPAR)
            self.state = 611
            _la = self._input.LA(1)
            if _la==MParser.STORABLE or _la==MParser.VARIABLE_IDENTIFIER:
                self.state = 610 
                localctx.attrs = self.attribute_identifier_list()


            self.state = 613
            self.match(MParser.RPAR)
            self.state = 614
            self.match(MParser.COLON)
            self.state = 615 
            self.indent()
            self.state = 616 
            localctx.bindings = self.native_category_bindings()
            self.state = 620
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 617 
                self.lfp()
                self.state = 618 
                localctx.methods = self.native_member_method_declaration_list()


            self.state = 622 
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
            if isinstance( listener, MParserListener ):
                listener.enterNative_category_bindings(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitNative_category_bindings(self)




    def native_category_bindings(self):

        localctx = MParser.Native_category_bindingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_native_category_bindings)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 624
            self.match(MParser.DEF)
            self.state = 625
            _la = self._input.LA(1)
            if not(_la==MParser.CATEGORY or _la==MParser.CLASS):
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 626
            self.match(MParser.BINDINGS)
            self.state = 627
            self.match(MParser.COLON)
            self.state = 628 
            self.indent()
            self.state = 629 
            localctx.items = self.native_category_binding_list(0)
            self.state = 630 
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
            if isinstance( listener, MParserListener ):
                listener.enterNativeCategoryBindingListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitNativeCategoryBindingListItem(self)


    class NativeCategoryBindingListContext(Native_category_binding_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_category_binding_listContext)
            super(MParser.NativeCategoryBindingListContext, self).__init__(parser)
            self.item = None # Native_category_bindingContext
            self.copyFrom(ctx)

        def native_category_binding(self):
            return self.getTypedRuleContext(MParser.Native_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterNativeCategoryBindingList(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitNativeCategoryBindingList(self)



    def native_category_binding_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Native_category_binding_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_native_category_binding_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.NativeCategoryBindingListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 633 
            localctx.item = self.native_category_binding()
            self._ctx.stop = self._input.LT(-1)
            self.state = 641
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.NativeCategoryBindingListItemContext(self, MParser.Native_category_binding_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_category_binding_list)
                    self.state = 635
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 636 
                    self.lfp()
                    self.state = 637 
                    localctx.item = self.native_category_binding() 
                self.state = 643
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterAbstract_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitAbstract_method_declaration(self)




    def abstract_method_declaration(self):

        localctx = MParser.Abstract_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_abstract_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 644
            self.match(MParser.ABSTRACT)
            self.state = 645
            self.match(MParser.DEF)
            self.state = 646 
            localctx.name = self.method_identifier()
            self.state = 647
            self.match(MParser.LPAR)
            self.state = 649
            _la = self._input.LA(1)
            if _la==MParser.CODE or _la==MParser.MUTABLE or _la==MParser.VARIABLE_IDENTIFIER:
                self.state = 648 
                localctx.args = self.argument_list()


            self.state = 651
            self.match(MParser.RPAR)
            self.state = 654
            _la = self._input.LA(1)
            if _la==MParser.RARROW:
                self.state = 652
                self.match(MParser.RARROW)
                self.state = 653 
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
            if isinstance( listener, MParserListener ):
                listener.enterConcrete_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitConcrete_method_declaration(self)




    def concrete_method_declaration(self):

        localctx = MParser.Concrete_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_concrete_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 656
            self.match(MParser.DEF)
            self.state = 657 
            localctx.name = self.method_identifier()
            self.state = 658
            self.match(MParser.LPAR)
            self.state = 660
            _la = self._input.LA(1)
            if _la==MParser.CODE or _la==MParser.MUTABLE or _la==MParser.VARIABLE_IDENTIFIER:
                self.state = 659 
                localctx.args = self.argument_list()


            self.state = 662
            self.match(MParser.RPAR)
            self.state = 665
            _la = self._input.LA(1)
            if _la==MParser.RARROW:
                self.state = 663
                self.match(MParser.RARROW)
                self.state = 664 
                localctx.typ = self.typedef(0)


            self.state = 667
            self.match(MParser.COLON)
            self.state = 668 
            self.indent()
            self.state = 669 
            localctx.stmts = self.statement_list()
            self.state = 670 
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
            if isinstance( listener, MParserListener ):
                listener.enterNative_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitNative_method_declaration(self)




    def native_method_declaration(self):

        localctx = MParser.Native_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_native_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 672
            self.match(MParser.DEF)
            self.state = 674
            _la = self._input.LA(1)
            if _la==MParser.NATIVE:
                self.state = 673
                self.match(MParser.NATIVE)


            self.state = 676 
            localctx.name = self.method_identifier()
            self.state = 677
            self.match(MParser.LPAR)
            self.state = 679
            _la = self._input.LA(1)
            if _la==MParser.CODE or _la==MParser.MUTABLE or _la==MParser.VARIABLE_IDENTIFIER:
                self.state = 678 
                localctx.args = self.argument_list()


            self.state = 681
            self.match(MParser.RPAR)
            self.state = 684
            _la = self._input.LA(1)
            if _la==MParser.RARROW:
                self.state = 682
                self.match(MParser.RARROW)
                self.state = 683 
                localctx.typ = self.category_or_any_type()


            self.state = 686
            self.match(MParser.COLON)
            self.state = 687 
            self.indent()
            self.state = 688 
            localctx.stmts = self.native_statement_list()
            self.state = 689 
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
            if isinstance( listener, MParserListener ):
                listener.enterTest_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitTest_method_declaration(self)




    def test_method_declaration(self):

        localctx = MParser.Test_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_test_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 691
            self.match(MParser.DEF)
            self.state = 692
            self.match(MParser.TEST)
            self.state = 693
            localctx.name = self.match(MParser.TEXT_LITERAL)
            self.state = 694
            self.match(MParser.LPAR)
            self.state = 695
            self.match(MParser.RPAR)
            self.state = 696
            self.match(MParser.COLON)
            self.state = 697 
            self.indent()
            self.state = 698 
            localctx.stmts = self.statement_list()
            self.state = 699 
            self.dedent()
            self.state = 700 
            self.lfp()
            self.state = 701
            self.match(MParser.VERIFYING)
            self.state = 702
            self.match(MParser.COLON)
            self.state = 708
            token = self._input.LA(1)
            if token in [MParser.LF]:
                self.state = 703 
                self.indent()
                self.state = 704 
                localctx.exps = self.assertion_list()
                self.state = 705 
                self.dedent()

            elif token in [MParser.SYMBOL_IDENTIFIER]:
                self.state = 707 
                localctx.error = self.symbol_identifier()

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
            if isinstance( listener, MParserListener ):
                listener.enterAssertion(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitAssertion(self)




    def assertion(self):

        localctx = MParser.AssertionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 710 
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
            if isinstance( listener, MParserListener ):
                listener.enterTyped_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitTyped_argument(self)




    def typed_argument(self):

        localctx = MParser.Typed_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_typed_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 712 
            localctx.name = self.variable_identifier()
            self.state = 713
            self.match(MParser.COLON)
            self.state = 714 
            localctx.typ = self.category_or_any_type()
            self.state = 719
            _la = self._input.LA(1)
            if _la==MParser.LPAR:
                self.state = 715
                self.match(MParser.LPAR)
                self.state = 716 
                localctx.attrs = self.attribute_identifier_list()
                self.state = 717
                self.match(MParser.RPAR)


            self.state = 723
            _la = self._input.LA(1)
            if _la==MParser.EQ:
                self.state = 721
                self.match(MParser.EQ)
                self.state = 722 
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
            if isinstance( listener, MParserListener ):
                listener.enterCommentStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCommentStatement(self)


    class StoreStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.StoreStatementContext, self).__init__(parser)
            self.stmt = None # Store_statementContext
            self.copyFrom(ctx)

        def store_statement(self):
            return self.getTypedRuleContext(MParser.Store_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterStoreStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitStoreStatement(self)


    class WithSingletonStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.WithSingletonStatementContext, self).__init__(parser)
            self.stmt = None # With_singleton_statementContext
            self.copyFrom(ctx)

        def with_singleton_statement(self):
            return self.getTypedRuleContext(MParser.With_singleton_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterWithSingletonStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitWithSingletonStatement(self)


    class WriteStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.WriteStatementContext, self).__init__(parser)
            self.stmt = None # Write_statementContext
            self.copyFrom(ctx)

        def write_statement(self):
            return self.getTypedRuleContext(MParser.Write_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterWriteStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitWriteStatement(self)


    class WhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.WhileStatementContext, self).__init__(parser)
            self.stmt = None # While_statementContext
            self.copyFrom(ctx)

        def while_statement(self):
            return self.getTypedRuleContext(MParser.While_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitWhileStatement(self)


    class WithResourceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.WithResourceStatementContext, self).__init__(parser)
            self.stmt = None # With_resource_statementContext
            self.copyFrom(ctx)

        def with_resource_statement(self):
            return self.getTypedRuleContext(MParser.With_resource_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterWithResourceStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitWithResourceStatement(self)


    class RaiseStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.RaiseStatementContext, self).__init__(parser)
            self.stmt = None # Raise_statementContext
            self.copyFrom(ctx)

        def raise_statement(self):
            return self.getTypedRuleContext(MParser.Raise_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterRaiseStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitRaiseStatement(self)


    class BreakStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.BreakStatementContext, self).__init__(parser)
            self.stmt = None # Break_statementContext
            self.copyFrom(ctx)

        def break_statement(self):
            return self.getTypedRuleContext(MParser.Break_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitBreakStatement(self)


    class AssignInstanceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.AssignInstanceStatementContext, self).__init__(parser)
            self.stmt = None # Assign_instance_statementContext
            self.copyFrom(ctx)

        def assign_instance_statement(self):
            return self.getTypedRuleContext(MParser.Assign_instance_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterAssignInstanceStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitAssignInstanceStatement(self)


    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.IfStatementContext, self).__init__(parser)
            self.stmt = None # If_statementContext
            self.copyFrom(ctx)

        def if_statement(self):
            return self.getTypedRuleContext(MParser.If_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterIfStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitIfStatement(self)


    class SwitchStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.SwitchStatementContext, self).__init__(parser)
            self.stmt = None # Switch_statementContext
            self.copyFrom(ctx)

        def switch_statement(self):
            return self.getTypedRuleContext(MParser.Switch_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitSwitchStatement(self)


    class TryStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.TryStatementContext, self).__init__(parser)
            self.stmt = None # Try_statementContext
            self.copyFrom(ctx)

        def try_statement(self):
            return self.getTypedRuleContext(MParser.Try_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterTryStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitTryStatement(self)


    class MethodCallStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.MethodCallStatementContext, self).__init__(parser)
            self.stmt = None # Method_callContext
            self.copyFrom(ctx)

        def method_call(self):
            return self.getTypedRuleContext(MParser.Method_callContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterMethodCallStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitMethodCallStatement(self)


    class ReturnStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.ReturnStatementContext, self).__init__(parser)
            self.stmt = None # Return_statementContext
            self.copyFrom(ctx)

        def return_statement(self):
            return self.getTypedRuleContext(MParser.Return_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitReturnStatement(self)


    class AssignTupleStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.AssignTupleStatementContext, self).__init__(parser)
            self.stmt = None # Assign_tuple_statementContext
            self.copyFrom(ctx)

        def assign_tuple_statement(self):
            return self.getTypedRuleContext(MParser.Assign_tuple_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterAssignTupleStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitAssignTupleStatement(self)


    class ClosureStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.ClosureStatementContext, self).__init__(parser)
            self.decl = None # Concrete_method_declarationContext
            self.copyFrom(ctx)

        def concrete_method_declaration(self):
            return self.getTypedRuleContext(MParser.Concrete_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterClosureStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitClosureStatement(self)


    class FlushStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.FlushStatementContext, self).__init__(parser)
            self.stmt = None # Flush_statementContext
            self.copyFrom(ctx)

        def flush_statement(self):
            return self.getTypedRuleContext(MParser.Flush_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterFlushStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitFlushStatement(self)


    class DoWhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.DoWhileStatementContext, self).__init__(parser)
            self.stmt = None # Do_while_statementContext
            self.copyFrom(ctx)

        def do_while_statement(self):
            return self.getTypedRuleContext(MParser.Do_while_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitDoWhileStatement(self)


    class ForEachStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a MParser.StatementContext)
            super(MParser.ForEachStatementContext, self).__init__(parser)
            self.stmt = None # For_each_statementContext
            self.copyFrom(ctx)

        def for_each_statement(self):
            return self.getTypedRuleContext(MParser.For_each_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterForEachStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitForEachStatement(self)



    def statement(self):

        localctx = MParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_statement)
        try:
            self.state = 744
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                localctx = MParser.MethodCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 725 
                localctx.stmt = self.method_call()
                pass

            elif la_ == 2:
                localctx = MParser.AssignInstanceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 726 
                localctx.stmt = self.assign_instance_statement()
                pass

            elif la_ == 3:
                localctx = MParser.AssignTupleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 727 
                localctx.stmt = self.assign_tuple_statement()
                pass

            elif la_ == 4:
                localctx = MParser.StoreStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 728 
                localctx.stmt = self.store_statement()
                pass

            elif la_ == 5:
                localctx = MParser.FlushStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 729 
                localctx.stmt = self.flush_statement()
                pass

            elif la_ == 6:
                localctx = MParser.BreakStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 730 
                localctx.stmt = self.break_statement()
                pass

            elif la_ == 7:
                localctx = MParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 731 
                localctx.stmt = self.return_statement()
                pass

            elif la_ == 8:
                localctx = MParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 732 
                localctx.stmt = self.if_statement()
                pass

            elif la_ == 9:
                localctx = MParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 733 
                localctx.stmt = self.switch_statement()
                pass

            elif la_ == 10:
                localctx = MParser.ForEachStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 734 
                localctx.stmt = self.for_each_statement()
                pass

            elif la_ == 11:
                localctx = MParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 735 
                localctx.stmt = self.while_statement()
                pass

            elif la_ == 12:
                localctx = MParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 736 
                localctx.stmt = self.do_while_statement()
                pass

            elif la_ == 13:
                localctx = MParser.RaiseStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 737 
                localctx.stmt = self.raise_statement()
                pass

            elif la_ == 14:
                localctx = MParser.TryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 738 
                localctx.stmt = self.try_statement()
                pass

            elif la_ == 15:
                localctx = MParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 739 
                localctx.stmt = self.write_statement()
                pass

            elif la_ == 16:
                localctx = MParser.WithResourceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 740 
                localctx.stmt = self.with_resource_statement()
                pass

            elif la_ == 17:
                localctx = MParser.WithSingletonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 741 
                localctx.stmt = self.with_singleton_statement()
                pass

            elif la_ == 18:
                localctx = MParser.ClosureStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 742 
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 19:
                localctx = MParser.CommentStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 19)
                self.state = 743 
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
            if isinstance( listener, MParserListener ):
                listener.enterFlush_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitFlush_statement(self)




    def flush_statement(self):

        localctx = MParser.Flush_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_flush_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 746
            self.match(MParser.FLUSH)
            self.state = 747
            self.match(MParser.LPAR)
            self.state = 748
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
            if isinstance( listener, MParserListener ):
                listener.enterStore_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitStore_statement(self)




    def store_statement(self):

        localctx = MParser.Store_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_store_statement)
        try:
            self.state = 770
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 750
                self.match(MParser.DELETE)
                self.state = 751
                self.match(MParser.LPAR)
                self.state = 752 
                localctx.to_del = self.expression_list()
                self.state = 753
                self.match(MParser.RPAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 755
                self.match(MParser.STORE)
                self.state = 756
                self.match(MParser.LPAR)
                self.state = 757 
                localctx.to_add = self.expression_list()
                self.state = 758
                self.match(MParser.RPAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 760
                self.match(MParser.DELETE)
                self.state = 761
                self.match(MParser.LPAR)
                self.state = 762 
                localctx.to_del = self.expression_list()
                self.state = 763
                self.match(MParser.RPAR)
                self.state = 764
                self.match(MParser.AND)
                self.state = 765
                self.match(MParser.STORE)
                self.state = 766
                self.match(MParser.LPAR)
                self.state = 767 
                localctx.to_add = self.expression_list()
                self.state = 768
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
            if isinstance( listener, MParserListener ):
                listener.enterMethod_call(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitMethod_call(self)




    def method_call(self):

        localctx = MParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 772 
            localctx.method = self.method_selector()
            self.state = 773
            self.match(MParser.LPAR)
            self.state = 775
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (MParser.EXECUTE - 98)) | (1 << (MParser.FETCH - 98)) | (1 << (MParser.MUTABLE - 98)) | (1 << (MParser.NONE - 98)) | (1 << (MParser.NOT - 98)) | (1 << (MParser.READ - 98)) | (1 << (MParser.SELF - 98)) | (1 << (MParser.SORTED - 98)) | (1 << (MParser.THIS - 98)) | (1 << (MParser.BOOLEAN_LITERAL - 98)) | (1 << (MParser.CHAR_LITERAL - 98)) | (1 << (MParser.MIN_INTEGER - 98)) | (1 << (MParser.MAX_INTEGER - 98)) | (1 << (MParser.SYMBOL_IDENTIFIER - 98)) | (1 << (MParser.TYPE_IDENTIFIER - 98)))) != 0) or ((((_la - 162)) & ~0x3f) == 0 and ((1 << (_la - 162)) & ((1 << (MParser.VARIABLE_IDENTIFIER - 162)) | (1 << (MParser.TEXT_LITERAL - 162)) | (1 << (MParser.UUID_LITERAL - 162)) | (1 << (MParser.INTEGER_LITERAL - 162)) | (1 << (MParser.HEXA_LITERAL - 162)) | (1 << (MParser.DECIMAL_LITERAL - 162)) | (1 << (MParser.DATETIME_LITERAL - 162)) | (1 << (MParser.TIME_LITERAL - 162)) | (1 << (MParser.DATE_LITERAL - 162)) | (1 << (MParser.PERIOD_LITERAL - 162)))) != 0):
                self.state = 774 
                localctx.args = self.argument_assignment_list(0)


            self.state = 777
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
            if isinstance( listener, MParserListener ):
                listener.enterMethodParent(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitMethodParent(self)


    class MethodNameContext(Method_selectorContext):

        def __init__(self, parser, ctx): # actually a MParser.Method_selectorContext)
            super(MParser.MethodNameContext, self).__init__(parser)
            self.name = None # Method_identifierContext
            self.copyFrom(ctx)

        def method_identifier(self):
            return self.getTypedRuleContext(MParser.Method_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterMethodName(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitMethodName(self)



    def method_selector(self):

        localctx = MParser.Method_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_method_selector)
        try:
            self.state = 784
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                localctx = MParser.MethodNameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 779 
                localctx.name = self.method_identifier()
                pass

            elif la_ == 2:
                localctx = MParser.MethodParentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 780 
                localctx.parent = self.callable_parent(0)
                self.state = 781
                self.match(MParser.DOT)
                self.state = 782 
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
            if isinstance( listener, MParserListener ):
                listener.enterCallableSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCallableSelector(self)


    class CallableRootContext(Callable_parentContext):

        def __init__(self, parser, ctx): # actually a MParser.Callable_parentContext)
            super(MParser.CallableRootContext, self).__init__(parser)
            self.name = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(MParser.IdentifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterCallableRoot(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCallableRoot(self)



    def callable_parent(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Callable_parentContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_callable_parent, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.CallableRootContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 787 
            localctx.name = self.identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 793
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.CallableSelectorContext(self, MParser.Callable_parentContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_callable_parent)
                    self.state = 789
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 790 
                    localctx.select = self.callable_selector() 
                self.state = 795
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterCallableItemSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterCallableMemberSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCallableMemberSelector(self)



    def callable_selector(self):

        localctx = MParser.Callable_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_callable_selector)
        try:
            self.state = 802
            token = self._input.LA(1)
            if token in [MParser.DOT]:
                localctx = MParser.CallableMemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 796
                self.match(MParser.DOT)
                self.state = 797 
                localctx.name = self.variable_identifier()

            elif token in [MParser.LBRAK]:
                localctx = MParser.CallableItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 798
                self.match(MParser.LBRAK)
                self.state = 799 
                localctx.exp = self.expression(0)
                self.state = 800
                self.match(MParser.RBRAK)

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
            if isinstance( listener, MParserListener ):
                listener.enterWith_resource_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitWith_resource_statement(self)




    def with_resource_statement(self):

        localctx = MParser.With_resource_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_with_resource_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 804
            self.match(MParser.WITH)
            self.state = 805 
            localctx.stmt = self.assign_variable_statement()
            self.state = 806
            self.match(MParser.COLON)
            self.state = 807 
            self.indent()
            self.state = 808 
            localctx.stmts = self.statement_list()
            self.state = 809 
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
            if isinstance( listener, MParserListener ):
                listener.enterWith_singleton_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitWith_singleton_statement(self)




    def with_singleton_statement(self):

        localctx = MParser.With_singleton_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_with_singleton_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 811
            self.match(MParser.WITH)
            self.state = 812 
            localctx.typ = self.type_identifier()
            self.state = 813
            self.match(MParser.COLON)
            self.state = 814 
            self.indent()
            self.state = 815 
            localctx.stmts = self.statement_list()
            self.state = 816 
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
            if isinstance( listener, MParserListener ):
                listener.enterSwitch_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitSwitch_statement(self)




    def switch_statement(self):

        localctx = MParser.Switch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_switch_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 818
            self.match(MParser.SWITCH)
            self.state = 819
            self.match(MParser.ON)
            self.state = 820 
            localctx.exp = self.expression(0)
            self.state = 821
            self.match(MParser.COLON)
            self.state = 822 
            self.indent()
            self.state = 823 
            localctx.cases = self.switch_case_statement_list()
            self.state = 831
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 824 
                self.lfp()
                self.state = 825
                self.match(MParser.OTHERWISE)
                self.state = 826
                self.match(MParser.COLON)
                self.state = 827 
                self.indent()
                self.state = 828 
                localctx.stmts = self.statement_list()
                self.state = 829 
                self.dedent()


            self.state = 833 
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
            if isinstance( listener, MParserListener ):
                listener.enterAtomicSwitchCase(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterCollectionSwitchCase(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCollectionSwitchCase(self)



    def switch_case_statement(self):

        localctx = MParser.Switch_case_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_switch_case_statement)
        try:
            self.state = 850
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                localctx = MParser.AtomicSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 835
                self.match(MParser.WHEN)
                self.state = 836 
                localctx.exp = self.atomic_literal()
                self.state = 837
                self.match(MParser.COLON)
                self.state = 838 
                self.indent()
                self.state = 839 
                localctx.stmts = self.statement_list()
                self.state = 840 
                self.dedent()
                pass

            elif la_ == 2:
                localctx = MParser.CollectionSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 842
                self.match(MParser.WHEN)
                self.state = 843
                self.match(MParser.IN)
                self.state = 844 
                localctx.exp = self.literal_collection()
                self.state = 845
                self.match(MParser.COLON)
                self.state = 846 
                self.indent()
                self.state = 847 
                localctx.stmts = self.statement_list()
                self.state = 848 
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
            if isinstance( listener, MParserListener ):
                listener.enterFor_each_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitFor_each_statement(self)




    def for_each_statement(self):

        localctx = MParser.For_each_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_for_each_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 852
            self.match(MParser.FOR)
            self.state = 853 
            localctx.name1 = self.variable_identifier()
            self.state = 856
            _la = self._input.LA(1)
            if _la==MParser.COMMA:
                self.state = 854
                self.match(MParser.COMMA)
                self.state = 855 
                localctx.name2 = self.variable_identifier()


            self.state = 858
            self.match(MParser.IN)
            self.state = 859 
            localctx.source = self.expression(0)
            self.state = 860
            self.match(MParser.COLON)
            self.state = 861 
            self.indent()
            self.state = 862 
            localctx.stmts = self.statement_list()
            self.state = 863 
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
            if isinstance( listener, MParserListener ):
                listener.enterDo_while_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitDo_while_statement(self)




    def do_while_statement(self):

        localctx = MParser.Do_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_do_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 865
            self.match(MParser.DO)
            self.state = 866
            self.match(MParser.COLON)
            self.state = 867 
            self.indent()
            self.state = 868 
            localctx.stmts = self.statement_list()
            self.state = 869 
            self.dedent()
            self.state = 870 
            self.lfp()
            self.state = 871
            self.match(MParser.WHILE)
            self.state = 872 
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
            if isinstance( listener, MParserListener ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitWhile_statement(self)




    def while_statement(self):

        localctx = MParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 874
            self.match(MParser.WHILE)
            self.state = 875 
            localctx.exp = self.expression(0)
            self.state = 876
            self.match(MParser.COLON)
            self.state = 877 
            self.indent()
            self.state = 878 
            localctx.stmts = self.statement_list()
            self.state = 879 
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
            if isinstance( listener, MParserListener ):
                listener.enterIf_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = MParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 881
            self.match(MParser.IF)
            self.state = 882 
            localctx.exp = self.expression(0)
            self.state = 883
            self.match(MParser.COLON)
            self.state = 884 
            self.indent()
            self.state = 885 
            localctx.stmts = self.statement_list()
            self.state = 886 
            self.dedent()
            self.state = 890
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 887 
                self.lfp()
                self.state = 888 
                localctx.elseIfs = self.else_if_statement_list(0)


            self.state = 899
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 892 
                self.lfp()
                self.state = 893
                self.match(MParser.ELSE)
                self.state = 894
                self.match(MParser.COLON)
                self.state = 895 
                self.indent()
                self.state = 896 
                localctx.elseStmts = self.statement_list()
                self.state = 897 
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
            if isinstance( listener, MParserListener ):
                listener.enterElseIfStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterElseIfStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitElseIfStatementListItem(self)



    def else_if_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Else_if_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_else_if_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.ElseIfStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 902
            self.match(MParser.ELSE)
            self.state = 903
            self.match(MParser.IF)
            self.state = 904 
            localctx.exp = self.expression(0)
            self.state = 905
            self.match(MParser.COLON)
            self.state = 906 
            self.indent()
            self.state = 907 
            localctx.stmts = self.statement_list()
            self.state = 908 
            self.dedent()
            self._ctx.stop = self._input.LT(-1)
            self.state = 922
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.ElseIfStatementListItemContext(self, MParser.Else_if_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_else_if_statement_list)
                    self.state = 910
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 911 
                    self.lfp()
                    self.state = 912
                    self.match(MParser.ELSE)
                    self.state = 913
                    self.match(MParser.IF)
                    self.state = 914 
                    localctx.exp = self.expression(0)
                    self.state = 915
                    self.match(MParser.COLON)
                    self.state = 916 
                    self.indent()
                    self.state = 917 
                    localctx.stmts = self.statement_list()
                    self.state = 918 
                    self.dedent() 
                self.state = 924
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterRaise_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitRaise_statement(self)




    def raise_statement(self):

        localctx = MParser.Raise_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_raise_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 925
            self.match(MParser.RAISE)
            self.state = 926 
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
            if isinstance( listener, MParserListener ):
                listener.enterTry_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitTry_statement(self)




    def try_statement(self):

        localctx = MParser.Try_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_try_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 928
            self.match(MParser.TRY)
            self.state = 929 
            localctx.name = self.variable_identifier()
            self.state = 930
            self.match(MParser.COLON)
            self.state = 931 
            self.indent()
            self.state = 932 
            localctx.stmts = self.statement_list()
            self.state = 933 
            self.dedent()
            self.state = 934 
            self.lfs()
            self.state = 936
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 935 
                localctx.handlers = self.catch_statement_list()


            self.state = 945
            _la = self._input.LA(1)
            if _la==MParser.EXCEPT:
                self.state = 938
                self.match(MParser.EXCEPT)
                self.state = 939
                self.match(MParser.COLON)
                self.state = 940 
                self.indent()
                self.state = 941 
                localctx.anyStmts = self.statement_list()
                self.state = 942 
                self.dedent()
                self.state = 943 
                self.lfs()


            self.state = 954
            _la = self._input.LA(1)
            if _la==MParser.FINALLY:
                self.state = 947
                self.match(MParser.FINALLY)
                self.state = 948
                self.match(MParser.COLON)
                self.state = 949 
                self.indent()
                self.state = 950 
                localctx.finalStmts = self.statement_list()
                self.state = 951 
                self.dedent()
                self.state = 952 
                self.lfs()


            self.state = 956 
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
            if isinstance( listener, MParserListener ):
                listener.enterCatchAtomicStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterCatchCollectionStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCatchCollectionStatement(self)



    def catch_statement(self):

        localctx = MParser.Catch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_catch_statement)
        try:
            self.state = 977
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                localctx = MParser.CatchAtomicStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 958
                self.match(MParser.EXCEPT)
                self.state = 959 
                localctx.name = self.symbol_identifier()
                self.state = 960
                self.match(MParser.COLON)
                self.state = 961 
                self.indent()
                self.state = 962 
                localctx.stmts = self.statement_list()
                self.state = 963 
                self.dedent()
                self.state = 964 
                self.lfs()
                pass

            elif la_ == 2:
                localctx = MParser.CatchCollectionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 966
                self.match(MParser.EXCEPT)
                self.state = 967
                self.match(MParser.IN)
                self.state = 968
                self.match(MParser.LBRAK)
                self.state = 969 
                localctx.exp = self.symbol_list()
                self.state = 970
                self.match(MParser.RBRAK)
                self.state = 971
                self.match(MParser.COLON)
                self.state = 972 
                self.indent()
                self.state = 973 
                localctx.stmts = self.statement_list()
                self.state = 974 
                self.dedent()
                self.state = 975 
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
            if isinstance( listener, MParserListener ):
                listener.enterBreak_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitBreak_statement(self)




    def break_statement(self):

        localctx = MParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 979
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
            if isinstance( listener, MParserListener ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitReturn_statement(self)




    def return_statement(self):

        localctx = MParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 981
            self.match(MParser.RETURN)
            self.state = 983
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (MParser.EXECUTE - 98)) | (1 << (MParser.FETCH - 98)) | (1 << (MParser.MUTABLE - 98)) | (1 << (MParser.NONE - 98)) | (1 << (MParser.NOT - 98)) | (1 << (MParser.READ - 98)) | (1 << (MParser.SELF - 98)) | (1 << (MParser.SORTED - 98)) | (1 << (MParser.THIS - 98)) | (1 << (MParser.BOOLEAN_LITERAL - 98)) | (1 << (MParser.CHAR_LITERAL - 98)) | (1 << (MParser.MIN_INTEGER - 98)) | (1 << (MParser.MAX_INTEGER - 98)) | (1 << (MParser.SYMBOL_IDENTIFIER - 98)) | (1 << (MParser.TYPE_IDENTIFIER - 98)))) != 0) or ((((_la - 162)) & ~0x3f) == 0 and ((1 << (_la - 162)) & ((1 << (MParser.VARIABLE_IDENTIFIER - 162)) | (1 << (MParser.TEXT_LITERAL - 162)) | (1 << (MParser.UUID_LITERAL - 162)) | (1 << (MParser.INTEGER_LITERAL - 162)) | (1 << (MParser.HEXA_LITERAL - 162)) | (1 << (MParser.DECIMAL_LITERAL - 162)) | (1 << (MParser.DATETIME_LITERAL - 162)) | (1 << (MParser.TIME_LITERAL - 162)) | (1 << (MParser.DATE_LITERAL - 162)) | (1 << (MParser.PERIOD_LITERAL - 162)))) != 0):
                self.state = 982 
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
            if isinstance( listener, MParserListener ):
                listener.enterIntDivideExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitIntDivideExpression(self)


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
            if isinstance( listener, MParserListener ):
                listener.enterTernaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitTernaryExpression(self)


    class ContainsAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.ContainsAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(MParser.CONTAINS, 0)
        def ALL(self):
            return self.getToken(MParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterContainsAllExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitContainsAllExpression(self)


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
            if isinstance( listener, MParserListener ):
                listener.enterNotEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterInExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitInExpression(self)


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
            if isinstance( listener, MParserListener ):
                listener.enterNotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterGreaterThanExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterOrExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterCodeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterLessThanOrEqualExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitLessThanOrEqualExpression(self)


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
            if isinstance( listener, MParserListener ):
                listener.enterAndExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitAndExpression(self)


    class ClosureExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.ClosureExpressionContext, self).__init__(parser)
            self.exp = None # Closure_expressionContext
            self.copyFrom(ctx)

        def closure_expression(self):
            return self.getTypedRuleContext(MParser.Closure_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterClosureExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitClosureExpression(self)


    class NotContainsAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.NotContainsAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(MParser.CONTAINS, 0)
        def ANY(self):
            return self.getToken(MParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterNotContainsAnyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitNotContainsAnyExpression(self)


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
            if isinstance( listener, MParserListener ):
                listener.enterContainsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterFilteredListExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterNotContainsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterMultiplyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterRoughlyEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterExecuteExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitExecuteExpression(self)


    class MethodExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.MethodExpressionContext, self).__init__(parser)
            self.exp = None # Method_expressionContext
            self.copyFrom(ctx)

        def method_expression(self):
            return self.getTypedRuleContext(MParser.Method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterGreaterThanOrEqualExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterNotInExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterIteratorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterIsNotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterDivideExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterIsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterMinusExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterAddExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitAddExpression(self)


    class NotContainsAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.NotContainsAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(MParser.CONTAINS, 0)
        def ALL(self):
            return self.getToken(MParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterNotContainsAllExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitNotContainsAllExpression(self)


    class InstanceExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.InstanceExpressionContext, self).__init__(parser)
            self.exp = None # Instance_expressionContext
            self.copyFrom(ctx)

        def instance_expression(self):
            return self.getTypedRuleContext(MParser.Instance_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterInstanceExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitInstanceExpression(self)


    class ContainsAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a MParser.ExpressionContext)
            super(MParser.ContainsAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(MParser.CONTAINS, 0)
        def ANY(self):
            return self.getToken(MParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterContainsAnyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitContainsAnyExpression(self)


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
            if isinstance( listener, MParserListener ):
                listener.enterCastExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterModuloExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterLessThanExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitEqualsExpression(self)



    def expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1003
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                localctx = MParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 986
                self.match(MParser.MINUS)
                self.state = 987 
                localctx.exp = self.expression(32)
                pass

            elif la_ == 2:
                localctx = MParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 988
                self.match(MParser.NOT)
                self.state = 989 
                localctx.exp = self.expression(31)
                pass

            elif la_ == 3:
                localctx = MParser.InstanceExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 990 
                localctx.exp = self.instance_expression(0)
                pass

            elif la_ == 4:
                localctx = MParser.MethodExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 991 
                localctx.exp = self.method_expression()
                pass

            elif la_ == 5:
                localctx = MParser.CodeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 992
                self.match(MParser.CODE)
                self.state = 993
                self.match(MParser.LPAR)
                self.state = 994 
                localctx.exp = self.expression(0)
                self.state = 995
                self.match(MParser.RPAR)
                pass

            elif la_ == 6:
                localctx = MParser.ExecuteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 997
                self.match(MParser.EXECUTE)
                self.state = 998
                self.match(MParser.LPAR)
                self.state = 999 
                localctx.name = self.variable_identifier()
                self.state = 1000
                self.match(MParser.RPAR)
                pass

            elif la_ == 7:
                localctx = MParser.ClosureExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1002 
                localctx.exp = self.closure_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1109
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1107
                    la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                    if la_ == 1:
                        localctx = MParser.MultiplyExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1005
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 1006 
                        self.multiply()
                        self.state = 1007 
                        localctx.right = self.expression(31)
                        pass

                    elif la_ == 2:
                        localctx = MParser.DivideExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1009
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 1010 
                        self.divide()
                        self.state = 1011 
                        localctx.right = self.expression(30)
                        pass

                    elif la_ == 3:
                        localctx = MParser.ModuloExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1013
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 1014 
                        self.modulo()
                        self.state = 1015 
                        localctx.right = self.expression(29)
                        pass

                    elif la_ == 4:
                        localctx = MParser.IntDivideExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1017
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 1018 
                        self.idivide()
                        self.state = 1019 
                        localctx.right = self.expression(28)
                        pass

                    elif la_ == 5:
                        localctx = MParser.AddExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1021
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 1022
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==MParser.PLUS or _la==MParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 1023 
                        localctx.right = self.expression(27)
                        pass

                    elif la_ == 6:
                        localctx = MParser.LessThanExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1024
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 1025
                        self.match(MParser.LT)
                        self.state = 1026 
                        localctx.right = self.expression(26)
                        pass

                    elif la_ == 7:
                        localctx = MParser.LessThanOrEqualExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1027
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 1028
                        self.match(MParser.LTE)
                        self.state = 1029 
                        localctx.right = self.expression(25)
                        pass

                    elif la_ == 8:
                        localctx = MParser.GreaterThanExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1030
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 1031
                        self.match(MParser.GT)
                        self.state = 1032 
                        localctx.right = self.expression(24)
                        pass

                    elif la_ == 9:
                        localctx = MParser.GreaterThanOrEqualExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1033
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 1034
                        self.match(MParser.GTE)
                        self.state = 1035 
                        localctx.right = self.expression(23)
                        pass

                    elif la_ == 10:
                        localctx = MParser.EqualsExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1036
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 1037
                        self.match(MParser.EQ2)
                        self.state = 1038 
                        localctx.right = self.expression(20)
                        pass

                    elif la_ == 11:
                        localctx = MParser.NotEqualsExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1039
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 1040
                        self.match(MParser.XEQ)
                        self.state = 1041 
                        localctx.right = self.expression(19)
                        pass

                    elif la_ == 12:
                        localctx = MParser.RoughlyEqualsExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1042
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 1043
                        self.match(MParser.TEQ)
                        self.state = 1044 
                        localctx.right = self.expression(18)
                        pass

                    elif la_ == 13:
                        localctx = MParser.OrExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1045
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 1046
                        self.match(MParser.OR)
                        self.state = 1047 
                        localctx.right = self.expression(17)
                        pass

                    elif la_ == 14:
                        localctx = MParser.AndExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1048
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 1049
                        self.match(MParser.AND)
                        self.state = 1050 
                        localctx.right = self.expression(16)
                        pass

                    elif la_ == 15:
                        localctx = MParser.TernaryExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.ifTrue = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1051
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 1052
                        self.match(MParser.IF)
                        self.state = 1053 
                        localctx.test = self.expression(0)
                        self.state = 1054
                        self.match(MParser.ELSE)
                        self.state = 1055 
                        localctx.ifFalse = self.expression(15)
                        pass

                    elif la_ == 16:
                        localctx = MParser.InExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1057
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 1058
                        self.match(MParser.IN)
                        self.state = 1059 
                        localctx.right = self.expression(13)
                        pass

                    elif la_ == 17:
                        localctx = MParser.ContainsExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1060
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 1061
                        self.match(MParser.CONTAINS)
                        self.state = 1062 
                        localctx.right = self.expression(12)
                        pass

                    elif la_ == 18:
                        localctx = MParser.ContainsAllExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1063
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 1064
                        self.match(MParser.CONTAINS)
                        self.state = 1065
                        self.match(MParser.ALL)
                        self.state = 1066 
                        localctx.right = self.expression(11)
                        pass

                    elif la_ == 19:
                        localctx = MParser.ContainsAnyExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1067
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 1068
                        self.match(MParser.CONTAINS)
                        self.state = 1069
                        self.match(MParser.ANY)
                        self.state = 1070 
                        localctx.right = self.expression(10)
                        pass

                    elif la_ == 20:
                        localctx = MParser.NotInExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1071
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 1072
                        self.match(MParser.NOT)
                        self.state = 1073
                        self.match(MParser.IN)
                        self.state = 1074 
                        localctx.right = self.expression(9)
                        pass

                    elif la_ == 21:
                        localctx = MParser.NotContainsExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1075
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 1076
                        self.match(MParser.NOT)
                        self.state = 1077
                        self.match(MParser.CONTAINS)
                        self.state = 1078 
                        localctx.right = self.expression(8)
                        pass

                    elif la_ == 22:
                        localctx = MParser.NotContainsAllExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1079
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 1080
                        self.match(MParser.NOT)
                        self.state = 1081
                        self.match(MParser.CONTAINS)
                        self.state = 1082
                        self.match(MParser.ALL)
                        self.state = 1083 
                        localctx.right = self.expression(7)
                        pass

                    elif la_ == 23:
                        localctx = MParser.NotContainsAnyExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1084
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 1085
                        self.match(MParser.NOT)
                        self.state = 1086
                        self.match(MParser.CONTAINS)
                        self.state = 1087
                        self.match(MParser.ANY)
                        self.state = 1088 
                        localctx.right = self.expression(6)
                        pass

                    elif la_ == 24:
                        localctx = MParser.IteratorExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.exp = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1089
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1090
                        self.match(MParser.FOR)
                        self.state = 1091 
                        localctx.name = self.variable_identifier()
                        self.state = 1092
                        self.match(MParser.IN)
                        self.state = 1093 
                        localctx.source = self.expression(2)
                        pass

                    elif la_ == 25:
                        localctx = MParser.FilteredListExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.src = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1095
                        if not self.precpred(self._ctx, 34):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 34)")
                        self.state = 1096 
                        self.filtered_list_suffix()
                        pass

                    elif la_ == 26:
                        localctx = MParser.IsNotExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1097
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 1098
                        self.match(MParser.IS)
                        self.state = 1099
                        self.match(MParser.NOT)
                        self.state = 1100 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 27:
                        localctx = MParser.IsExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1101
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 1102
                        self.match(MParser.IS)
                        self.state = 1103 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 28:
                        localctx = MParser.CastExpressionContext(self, MParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1104
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 1105
                        self.match(MParser.AS)
                        self.state = 1106 
                        localctx.right = self.category_or_any_type()
                        pass

             
                self.state = 1111
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterClosure_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitClosure_expression(self)




    def closure_expression(self):

        localctx = MParser.Closure_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_closure_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1112 
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
            if isinstance( listener, MParserListener ):
                listener.enterSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitSelectorExpression(self)


    class SelectableExpressionContext(Instance_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Instance_expressionContext)
            super(MParser.SelectableExpressionContext, self).__init__(parser)
            self.parent = None # Selectable_expressionContext
            self.copyFrom(ctx)

        def selectable_expression(self):
            return self.getTypedRuleContext(MParser.Selectable_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterSelectableExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitSelectableExpression(self)



    def instance_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Instance_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_instance_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.SelectableExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1115 
            localctx.parent = self.selectable_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1121
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.SelectorExpressionContext(self, MParser.Instance_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_expression)
                    self.state = 1117
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1118 
                    localctx.selector = self.instance_selector() 
                self.state = 1123
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterMethod_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitMethod_expression(self)




    def method_expression(self):

        localctx = MParser.Method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_method_expression)
        try:
            self.state = 1132
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1124 
                self.blob_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1125 
                self.document_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1126 
                self.fetch_store_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1127 
                self.read_all_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1128 
                self.read_one_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1129 
                self.sorted_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1130 
                self.method_call()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1131 
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
            if isinstance( listener, MParserListener ):
                listener.enterSliceSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterMemberSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterItemSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitItemSelector(self)



    def instance_selector(self):

        localctx = MParser.Instance_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_instance_selector)
        try:
            self.state = 1147
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                localctx = MParser.MemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1134
                if not self.wasNot(MParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(MParser.WS)")
                self.state = 1135
                self.match(MParser.DOT)
                self.state = 1136 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = MParser.SliceSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1137
                if not self.wasNot(MParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(MParser.WS)")
                self.state = 1138
                self.match(MParser.LBRAK)
                self.state = 1139 
                localctx.xslice = self.slice_arguments()
                self.state = 1140
                self.match(MParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = MParser.ItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1142
                if not self.wasNot(MParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(MParser.WS)")
                self.state = 1143
                self.match(MParser.LBRAK)
                self.state = 1144 
                localctx.exp = self.expression(0)
                self.state = 1145
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
            if isinstance( listener, MParserListener ):
                listener.enterBlob_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitBlob_expression(self)




    def blob_expression(self):

        localctx = MParser.Blob_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_blob_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1149
            self.match(MParser.BLOB)
            self.state = 1150
            self.match(MParser.LPAR)
            self.state = 1152
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (MParser.EXECUTE - 98)) | (1 << (MParser.FETCH - 98)) | (1 << (MParser.MUTABLE - 98)) | (1 << (MParser.NONE - 98)) | (1 << (MParser.NOT - 98)) | (1 << (MParser.READ - 98)) | (1 << (MParser.SELF - 98)) | (1 << (MParser.SORTED - 98)) | (1 << (MParser.THIS - 98)) | (1 << (MParser.BOOLEAN_LITERAL - 98)) | (1 << (MParser.CHAR_LITERAL - 98)) | (1 << (MParser.MIN_INTEGER - 98)) | (1 << (MParser.MAX_INTEGER - 98)) | (1 << (MParser.SYMBOL_IDENTIFIER - 98)) | (1 << (MParser.TYPE_IDENTIFIER - 98)))) != 0) or ((((_la - 162)) & ~0x3f) == 0 and ((1 << (_la - 162)) & ((1 << (MParser.VARIABLE_IDENTIFIER - 162)) | (1 << (MParser.TEXT_LITERAL - 162)) | (1 << (MParser.UUID_LITERAL - 162)) | (1 << (MParser.INTEGER_LITERAL - 162)) | (1 << (MParser.HEXA_LITERAL - 162)) | (1 << (MParser.DECIMAL_LITERAL - 162)) | (1 << (MParser.DATETIME_LITERAL - 162)) | (1 << (MParser.TIME_LITERAL - 162)) | (1 << (MParser.DATE_LITERAL - 162)) | (1 << (MParser.PERIOD_LITERAL - 162)))) != 0):
                self.state = 1151 
                self.expression(0)


            self.state = 1154
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
            if isinstance( listener, MParserListener ):
                listener.enterDocument_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitDocument_expression(self)




    def document_expression(self):

        localctx = MParser.Document_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_document_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1156
            self.match(MParser.DOCUMENT)
            self.state = 1157
            self.match(MParser.LPAR)
            self.state = 1159
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (MParser.EXECUTE - 98)) | (1 << (MParser.FETCH - 98)) | (1 << (MParser.MUTABLE - 98)) | (1 << (MParser.NONE - 98)) | (1 << (MParser.NOT - 98)) | (1 << (MParser.READ - 98)) | (1 << (MParser.SELF - 98)) | (1 << (MParser.SORTED - 98)) | (1 << (MParser.THIS - 98)) | (1 << (MParser.BOOLEAN_LITERAL - 98)) | (1 << (MParser.CHAR_LITERAL - 98)) | (1 << (MParser.MIN_INTEGER - 98)) | (1 << (MParser.MAX_INTEGER - 98)) | (1 << (MParser.SYMBOL_IDENTIFIER - 98)) | (1 << (MParser.TYPE_IDENTIFIER - 98)))) != 0) or ((((_la - 162)) & ~0x3f) == 0 and ((1 << (_la - 162)) & ((1 << (MParser.VARIABLE_IDENTIFIER - 162)) | (1 << (MParser.TEXT_LITERAL - 162)) | (1 << (MParser.UUID_LITERAL - 162)) | (1 << (MParser.INTEGER_LITERAL - 162)) | (1 << (MParser.HEXA_LITERAL - 162)) | (1 << (MParser.DECIMAL_LITERAL - 162)) | (1 << (MParser.DATETIME_LITERAL - 162)) | (1 << (MParser.TIME_LITERAL - 162)) | (1 << (MParser.DATE_LITERAL - 162)) | (1 << (MParser.PERIOD_LITERAL - 162)))) != 0):
                self.state = 1158 
                self.expression(0)


            self.state = 1161
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
            self.typ = None # Mutable_category_typeContext
            self.args = None # Argument_assignment_listContext

        def LPAR(self):
            return self.getToken(MParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(MParser.RPAR, 0)

        def mutable_category_type(self):
            return self.getTypedRuleContext(MParser.Mutable_category_typeContext,0)


        def argument_assignment_list(self):
            return self.getTypedRuleContext(MParser.Argument_assignment_listContext,0)


        def getRuleIndex(self):
            return MParser.RULE_constructor_expression

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterConstructor_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitConstructor_expression(self)




    def constructor_expression(self):

        localctx = MParser.Constructor_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_constructor_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1163 
            localctx.typ = self.mutable_category_type()
            self.state = 1164
            self.match(MParser.LPAR)
            self.state = 1166
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (MParser.EXECUTE - 98)) | (1 << (MParser.FETCH - 98)) | (1 << (MParser.MUTABLE - 98)) | (1 << (MParser.NONE - 98)) | (1 << (MParser.NOT - 98)) | (1 << (MParser.READ - 98)) | (1 << (MParser.SELF - 98)) | (1 << (MParser.SORTED - 98)) | (1 << (MParser.THIS - 98)) | (1 << (MParser.BOOLEAN_LITERAL - 98)) | (1 << (MParser.CHAR_LITERAL - 98)) | (1 << (MParser.MIN_INTEGER - 98)) | (1 << (MParser.MAX_INTEGER - 98)) | (1 << (MParser.SYMBOL_IDENTIFIER - 98)) | (1 << (MParser.TYPE_IDENTIFIER - 98)))) != 0) or ((((_la - 162)) & ~0x3f) == 0 and ((1 << (_la - 162)) & ((1 << (MParser.VARIABLE_IDENTIFIER - 162)) | (1 << (MParser.TEXT_LITERAL - 162)) | (1 << (MParser.UUID_LITERAL - 162)) | (1 << (MParser.INTEGER_LITERAL - 162)) | (1 << (MParser.HEXA_LITERAL - 162)) | (1 << (MParser.DECIMAL_LITERAL - 162)) | (1 << (MParser.DATETIME_LITERAL - 162)) | (1 << (MParser.TIME_LITERAL - 162)) | (1 << (MParser.DATE_LITERAL - 162)) | (1 << (MParser.PERIOD_LITERAL - 162)))) != 0):
                self.state = 1165 
                localctx.args = self.argument_assignment_list(0)


            self.state = 1168
            self.match(MParser.RPAR)
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
            if isinstance( listener, MParserListener ):
                listener.enterExpressionAssignmentList(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitExpressionAssignmentList(self)


    class ArgumentAssignmentListContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Argument_assignment_listContext)
            super(MParser.ArgumentAssignmentListContext, self).__init__(parser)
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def argument_assignment(self):
            return self.getTypedRuleContext(MParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterArgumentAssignmentList(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterArgumentAssignmentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitArgumentAssignmentListItem(self)



    def argument_assignment_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Argument_assignment_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_argument_assignment_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1175
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                localctx = MParser.ExpressionAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1171 
                localctx.exp = self.expression(0)
                self.state = 1172
                if not self.willNotBe(self.equalToken()):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willNotBe($parser.equalToken())")
                pass

            elif la_ == 2:
                localctx = MParser.ArgumentAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1174 
                localctx.item = self.argument_assignment()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1182
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,59,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.ArgumentAssignmentListItemContext(self, MParser.Argument_assignment_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_assignment_list)
                    self.state = 1177
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1178
                    self.match(MParser.COMMA)
                    self.state = 1179 
                    localctx.item = self.argument_assignment() 
                self.state = 1184
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,59,self._ctx)

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

        def assign(self):
            return self.getTypedRuleContext(MParser.AssignContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MParser.RULE_argument_assignment

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterArgument_assignment(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitArgument_assignment(self)




    def argument_assignment(self):

        localctx = MParser.Argument_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_argument_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1185 
            localctx.name = self.variable_identifier()
            self.state = 1186 
            self.assign()
            self.state = 1187 
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
            if isinstance( listener, MParserListener ):
                listener.enterWrite_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitWrite_statement(self)




    def write_statement(self):

        localctx = MParser.Write_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_write_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1189
            self.match(MParser.WRITE)
            self.state = 1190 
            localctx.what = self.expression(0)
            self.state = 1191
            self.match(MParser.TO)
            self.state = 1192 
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
            if isinstance( listener, MParserListener ):
                listener.enterFiltered_list_suffix(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitFiltered_list_suffix(self)




    def filtered_list_suffix(self):

        localctx = MParser.Filtered_list_suffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_filtered_list_suffix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1194
            self.match(MParser.FILTERED)
            self.state = 1195
            self.match(MParser.WITH)
            self.state = 1196 
            localctx.name = self.variable_identifier()
            self.state = 1197
            self.match(MParser.WHERE)
            self.state = 1198 
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
            if isinstance( listener, MParserListener ):
                listener.enterFetchOne(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterFetchMany(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitFetchMany(self)



    def fetch_store_expression(self):

        localctx = MParser.Fetch_store_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_fetch_store_expression)
        self._la = 0 # Token type
        try:
            self.state = 1230
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                localctx = MParser.FetchOneContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1200
                self.match(MParser.FETCH)
                self.state = 1201
                self.match(MParser.ONE)
                self.state = 1203
                _la = self._input.LA(1)
                if _la==MParser.MUTABLE or _la==MParser.TYPE_IDENTIFIER:
                    self.state = 1202 
                    localctx.typ = self.mutable_category_type()


                self.state = 1205
                self.match(MParser.WHERE)
                self.state = 1206 
                localctx.predicate = self.expression(0)
                pass

            elif la_ == 2:
                localctx = MParser.FetchManyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1207
                self.match(MParser.FETCH)
                self.state = 1214
                token = self._input.LA(1)
                if token in [MParser.ALL]:
                    self.state = 1208
                    self.match(MParser.ALL)

                elif token in [MParser.ROWS]:
                    self.state = 1209
                    self.match(MParser.ROWS)
                    self.state = 1210 
                    localctx.xstart = self.expression(0)
                    self.state = 1211
                    self.match(MParser.TO)
                    self.state = 1212 
                    localctx.xstop = self.expression(0)

                else:
                    raise NoViableAltException(self)

                self.state = 1216
                self.match(MParser.LPAR)
                self.state = 1218
                _la = self._input.LA(1)
                if _la==MParser.MUTABLE or _la==MParser.TYPE_IDENTIFIER:
                    self.state = 1217 
                    localctx.typ = self.mutable_category_type()


                self.state = 1220
                self.match(MParser.RPAR)
                self.state = 1223
                la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                if la_ == 1:
                    self.state = 1221
                    self.match(MParser.WHERE)
                    self.state = 1222 
                    localctx.predicate = self.expression(0)


                self.state = 1228
                la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
                if la_ == 1:
                    self.state = 1225
                    self.match(MParser.ORDER)
                    self.state = 1226
                    self.match(MParser.BY)
                    self.state = 1227 
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
            if isinstance( listener, MParserListener ):
                listener.enterSorted_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitSorted_expression(self)




    def sorted_expression(self):

        localctx = MParser.Sorted_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_sorted_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1232
            self.match(MParser.SORTED)
            self.state = 1234
            _la = self._input.LA(1)
            if _la==MParser.DESC:
                self.state = 1233
                self.match(MParser.DESC)


            self.state = 1236
            self.match(MParser.LPAR)
            self.state = 1237 
            localctx.source = self.instance_expression(0)
            self.state = 1243
            _la = self._input.LA(1)
            if _la==MParser.COMMA:
                self.state = 1238
                self.match(MParser.COMMA)
                self.state = 1239 
                self.key_token()
                self.state = 1240
                self.match(MParser.EQ)
                self.state = 1241 
                localctx.key = self.instance_expression(0)


            self.state = 1245
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
            if isinstance( listener, MParserListener ):
                listener.enterAssign_instance_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitAssign_instance_statement(self)




    def assign_instance_statement(self):

        localctx = MParser.Assign_instance_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_assign_instance_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1247 
            localctx.inst = self.assignable_instance(0)
            self.state = 1248 
            self.assign()
            self.state = 1249 
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
            if isinstance( listener, MParserListener ):
                listener.enterMemberInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterItemInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitItemInstance(self)



    def child_instance(self):

        localctx = MParser.Child_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_child_instance)
        try:
            self.state = 1259
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                localctx = MParser.MemberInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1251
                if not self.wasNot(MParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(MParser.WS)")
                self.state = 1252
                self.match(MParser.DOT)
                self.state = 1253 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = MParser.ItemInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1254
                if not self.wasNot(MParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(MParser.WS)")
                self.state = 1255
                self.match(MParser.LBRAK)
                self.state = 1256 
                localctx.exp = self.expression(0)
                self.state = 1257
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
            if isinstance( listener, MParserListener ):
                listener.enterAssign_tuple_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitAssign_tuple_statement(self)




    def assign_tuple_statement(self):

        localctx = MParser.Assign_tuple_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_assign_tuple_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1261 
            localctx.items = self.variable_identifier_list()
            self.state = 1262 
            self.assign()
            self.state = 1263 
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
            if isinstance( listener, MParserListener ):
                listener.enterLfs(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitLfs(self)




    def lfs(self):

        localctx = MParser.LfsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_lfs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1268
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,69,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1265
                    self.match(MParser.LF) 
                self.state = 1270
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,69,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterLfp(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitLfp(self)




    def lfp(self):

        localctx = MParser.LfpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_lfp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1272 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1271
                self.match(MParser.LF)
                self.state = 1274 
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
            if isinstance( listener, MParserListener ):
                listener.enterIndent(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitIndent(self)




    def indent(self):

        localctx = MParser.IndentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_indent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1277 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1276
                self.match(MParser.LF)
                self.state = 1279 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MParser.LF):
                    break

            self.state = 1281
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
            if isinstance( listener, MParserListener ):
                listener.enterDedent(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitDedent(self)




    def dedent(self):

        localctx = MParser.DedentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_dedent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.LF:
                self.state = 1283
                self.match(MParser.LF)
                self.state = 1288
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1289
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
            if isinstance( listener, MParserListener ):
                listener.enterNull_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitNull_literal(self)




    def null_literal(self):

        localctx = MParser.Null_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1291
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
            if isinstance( listener, MParserListener ):
                listener.enterFullDeclarationList(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitFullDeclarationList(self)



    def declaration_list(self):

        localctx = MParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            localctx = MParser.FullDeclarationListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 1294
            _la = self._input.LA(1)
            if _la==MParser.COMMENT or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (MParser.ABSTRACT - 67)) | (1 << (MParser.ATTR - 67)) | (1 << (MParser.CATEGORY - 67)) | (1 << (MParser.CLASS - 67)) | (1 << (MParser.DEF - 67)) | (1 << (MParser.ENUM - 67)) | (1 << (MParser.NATIVE - 67)))) != 0) or _la==MParser.SINGLETON or _la==MParser.STORABLE:
                self.state = 1293 
                self.declarations()


            self.state = 1296 
            self.lfs()
            self.state = 1297
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
            if isinstance( listener, MParserListener ):
                listener.enterDeclarations(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitDeclarations(self)




    def declarations(self):

        localctx = MParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_declarations)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1299 
            self.declaration()
            self.state = 1305
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,74,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1300 
                    self.lfp()
                    self.state = 1301 
                    self.declaration() 
                self.state = 1307
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,74,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = MParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMENT:
                self.state = 1308 
                self.comment_statement()
                self.state = 1309 
                self.lfp()
                self.state = 1315
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1321
            la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
            if la_ == 1:
                self.state = 1316 
                self.attribute_declaration()
                pass

            elif la_ == 2:
                self.state = 1317 
                self.category_declaration()
                pass

            elif la_ == 3:
                self.state = 1318 
                self.resource_declaration()
                pass

            elif la_ == 4:
                self.state = 1319 
                self.enum_declaration()
                pass

            elif la_ == 5:
                self.state = 1320 
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
            if isinstance( listener, MParserListener ):
                listener.enterResource_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitResource_declaration(self)




    def resource_declaration(self):

        localctx = MParser.Resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1323 
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
            if isinstance( listener, MParserListener ):
                listener.enterEnum_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitEnum_declaration(self)




    def enum_declaration(self):

        localctx = MParser.Enum_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_enum_declaration)
        try:
            self.state = 1327
            la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1325 
                self.enum_category_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1326 
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
            if isinstance( listener, MParserListener ):
                listener.enterNative_symbol_list(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitNative_symbol_list(self)




    def native_symbol_list(self):

        localctx = MParser.Native_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_native_symbol_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1329 
            self.native_symbol()
            self.state = 1335
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,78,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1330 
                    self.lfp()
                    self.state = 1331 
                    self.native_symbol() 
                self.state = 1337
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,78,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterCategory_symbol_list(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCategory_symbol_list(self)




    def category_symbol_list(self):

        localctx = MParser.Category_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_category_symbol_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1338 
            self.category_symbol()
            self.state = 1344
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,79,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1339 
                    self.lfp()
                    self.state = 1340 
                    self.category_symbol() 
                self.state = 1346
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,79,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterSymbol_list(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitSymbol_list(self)




    def symbol_list(self):

        localctx = MParser.Symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_symbol_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1347 
            self.symbol_identifier()
            self.state = 1352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMA:
                self.state = 1348
                self.match(MParser.COMMA)
                self.state = 1349 
                self.symbol_identifier()
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
            if isinstance( listener, MParserListener ):
                listener.enterMatchingSet(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterMatchingPattern(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterMatchingList(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterMatchingRange(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterMatchingExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitMatchingExpression(self)



    def attribute_constraint(self):

        localctx = MParser.Attribute_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_attribute_constraint)
        try:
            self.state = 1365
            la_ = self._interp.adaptivePredict(self._input,81,self._ctx)
            if la_ == 1:
                localctx = MParser.MatchingListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1355
                self.match(MParser.IN)
                self.state = 1356 
                localctx.source = self.list_literal()
                pass

            elif la_ == 2:
                localctx = MParser.MatchingSetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1357
                self.match(MParser.IN)
                self.state = 1358 
                localctx.source = self.set_literal()
                pass

            elif la_ == 3:
                localctx = MParser.MatchingRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1359
                self.match(MParser.IN)
                self.state = 1360 
                localctx.source = self.range_literal()
                pass

            elif la_ == 4:
                localctx = MParser.MatchingPatternContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1361
                self.match(MParser.MATCHING)
                self.state = 1362
                localctx.text = self.match(MParser.TEXT_LITERAL)
                pass

            elif la_ == 5:
                localctx = MParser.MatchingExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1363
                self.match(MParser.MATCHING)
                self.state = 1364 
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
            if isinstance( listener, MParserListener ):
                listener.enterList_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitList_literal(self)




    def list_literal(self):

        localctx = MParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1368
            _la = self._input.LA(1)
            if _la==MParser.MUTABLE:
                self.state = 1367
                self.match(MParser.MUTABLE)


            self.state = 1370
            self.match(MParser.LBRAK)
            self.state = 1372
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (MParser.EXECUTE - 98)) | (1 << (MParser.FETCH - 98)) | (1 << (MParser.MUTABLE - 98)) | (1 << (MParser.NONE - 98)) | (1 << (MParser.NOT - 98)) | (1 << (MParser.READ - 98)) | (1 << (MParser.SELF - 98)) | (1 << (MParser.SORTED - 98)) | (1 << (MParser.THIS - 98)) | (1 << (MParser.BOOLEAN_LITERAL - 98)) | (1 << (MParser.CHAR_LITERAL - 98)) | (1 << (MParser.MIN_INTEGER - 98)) | (1 << (MParser.MAX_INTEGER - 98)) | (1 << (MParser.SYMBOL_IDENTIFIER - 98)) | (1 << (MParser.TYPE_IDENTIFIER - 98)))) != 0) or ((((_la - 162)) & ~0x3f) == 0 and ((1 << (_la - 162)) & ((1 << (MParser.VARIABLE_IDENTIFIER - 162)) | (1 << (MParser.TEXT_LITERAL - 162)) | (1 << (MParser.UUID_LITERAL - 162)) | (1 << (MParser.INTEGER_LITERAL - 162)) | (1 << (MParser.HEXA_LITERAL - 162)) | (1 << (MParser.DECIMAL_LITERAL - 162)) | (1 << (MParser.DATETIME_LITERAL - 162)) | (1 << (MParser.TIME_LITERAL - 162)) | (1 << (MParser.DATE_LITERAL - 162)) | (1 << (MParser.PERIOD_LITERAL - 162)))) != 0):
                self.state = 1371 
                self.expression_list()


            self.state = 1374
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
            if isinstance( listener, MParserListener ):
                listener.enterSet_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitSet_literal(self)




    def set_literal(self):

        localctx = MParser.Set_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_set_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1377
            _la = self._input.LA(1)
            if _la==MParser.MUTABLE:
                self.state = 1376
                self.match(MParser.MUTABLE)


            self.state = 1379
            self.match(MParser.LT)
            self.state = 1381
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (MParser.EXECUTE - 98)) | (1 << (MParser.FETCH - 98)) | (1 << (MParser.MUTABLE - 98)) | (1 << (MParser.NONE - 98)) | (1 << (MParser.NOT - 98)) | (1 << (MParser.READ - 98)) | (1 << (MParser.SELF - 98)) | (1 << (MParser.SORTED - 98)) | (1 << (MParser.THIS - 98)) | (1 << (MParser.BOOLEAN_LITERAL - 98)) | (1 << (MParser.CHAR_LITERAL - 98)) | (1 << (MParser.MIN_INTEGER - 98)) | (1 << (MParser.MAX_INTEGER - 98)) | (1 << (MParser.SYMBOL_IDENTIFIER - 98)) | (1 << (MParser.TYPE_IDENTIFIER - 98)))) != 0) or ((((_la - 162)) & ~0x3f) == 0 and ((1 << (_la - 162)) & ((1 << (MParser.VARIABLE_IDENTIFIER - 162)) | (1 << (MParser.TEXT_LITERAL - 162)) | (1 << (MParser.UUID_LITERAL - 162)) | (1 << (MParser.INTEGER_LITERAL - 162)) | (1 << (MParser.HEXA_LITERAL - 162)) | (1 << (MParser.DECIMAL_LITERAL - 162)) | (1 << (MParser.DATETIME_LITERAL - 162)) | (1 << (MParser.TIME_LITERAL - 162)) | (1 << (MParser.DATE_LITERAL - 162)) | (1 << (MParser.PERIOD_LITERAL - 162)))) != 0):
                self.state = 1380 
                self.expression_list()


            self.state = 1383
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
            if isinstance( listener, MParserListener ):
                listener.enterExpression_list(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitExpression_list(self)




    def expression_list(self):

        localctx = MParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1385 
            self.expression(0)
            self.state = 1390
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMA:
                self.state = 1386
                self.match(MParser.COMMA)
                self.state = 1387 
                self.expression(0)
                self.state = 1392
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
            if isinstance( listener, MParserListener ):
                listener.enterRange_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitRange_literal(self)




    def range_literal(self):

        localctx = MParser.Range_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_range_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1393
            self.match(MParser.LBRAK)
            self.state = 1394 
            localctx.low = self.expression(0)
            self.state = 1395
            self.match(MParser.RANGE)
            self.state = 1396 
            localctx.high = self.expression(0)
            self.state = 1397
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
            if isinstance( listener, MParserListener ):
                listener.enterIteratorType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterSetType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterListType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterDictType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterCursorType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCursorType(self)


    class PrimaryTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a MParser.TypedefContext)
            super(MParser.PrimaryTypeContext, self).__init__(parser)
            self.p = None # Primary_typeContext
            self.copyFrom(ctx)

        def primary_type(self):
            return self.getTypedRuleContext(MParser.Primary_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterPrimaryType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPrimaryType(self)



    def typedef(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.TypedefContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 160
        self.enterRecursionRule(localctx, 160, self.RULE_typedef, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1411
            token = self._input.LA(1)
            if token in [MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.CODE, MParser.DOCUMENT, MParser.BLOB, MParser.IMAGE, MParser.UUID, MParser.TYPE_IDENTIFIER]:
                localctx = MParser.PrimaryTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1400 
                localctx.p = self.primary_type()

            elif token in [MParser.CURSOR]:
                localctx = MParser.CursorTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1401
                self.match(MParser.CURSOR)
                self.state = 1402
                self.match(MParser.LT)
                self.state = 1403 
                localctx.c = self.typedef(0)
                self.state = 1404
                self.match(MParser.GT)

            elif token in [MParser.ITERATOR]:
                localctx = MParser.IteratorTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1406
                self.match(MParser.ITERATOR)
                self.state = 1407
                self.match(MParser.LT)
                self.state = 1408 
                localctx.i = self.typedef(0)
                self.state = 1409
                self.match(MParser.GT)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 1423
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,89,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1421
                    la_ = self._interp.adaptivePredict(self._input,88,self._ctx)
                    if la_ == 1:
                        localctx = MParser.SetTypeContext(self, MParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.s = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1413
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 1414
                        self.match(MParser.LTGT)
                        pass

                    elif la_ == 2:
                        localctx = MParser.ListTypeContext(self, MParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1415
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 1416
                        self.match(MParser.LBRAK)
                        self.state = 1417
                        self.match(MParser.RBRAK)
                        pass

                    elif la_ == 3:
                        localctx = MParser.DictTypeContext(self, MParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.d = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1418
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1419
                        self.match(MParser.LCURL)
                        self.state = 1420
                        self.match(MParser.RCURL)
                        pass

             
                self.state = 1425
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,89,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterNativeType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitNativeType(self)


    class CategoryTypeContext(Primary_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Primary_typeContext)
            super(MParser.CategoryTypeContext, self).__init__(parser)
            self.c = None # Category_typeContext
            self.copyFrom(ctx)

        def category_type(self):
            return self.getTypedRuleContext(MParser.Category_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterCategoryType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCategoryType(self)



    def primary_type(self):

        localctx = MParser.Primary_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_primary_type)
        try:
            self.state = 1428
            token = self._input.LA(1)
            if token in [MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.CODE, MParser.DOCUMENT, MParser.BLOB, MParser.IMAGE, MParser.UUID]:
                localctx = MParser.NativeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1426 
                localctx.n = self.native_type()

            elif token in [MParser.TYPE_IDENTIFIER]:
                localctx = MParser.CategoryTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1427 
                localctx.c = self.category_type()

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
            if isinstance( listener, MParserListener ):
                listener.enterPeriodType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPeriodType(self)


    class BooleanTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.BooleanTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(MParser.BOOLEAN, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterBooleanType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitBooleanType(self)


    class DocumentTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.DocumentTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOCUMENT(self):
            return self.getToken(MParser.DOCUMENT, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterDocumentType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitDocumentType(self)


    class CharacterTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.CharacterTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHARACTER(self):
            return self.getToken(MParser.CHARACTER, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterCharacterType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCharacterType(self)


    class TextTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.TextTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT(self):
            return self.getToken(MParser.TEXT, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterTextType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitTextType(self)


    class ImageTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.ImageTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def IMAGE(self):
            return self.getToken(MParser.IMAGE, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterImageType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitImageType(self)


    class TimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.TimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TIME(self):
            return self.getToken(MParser.TIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitTimeType(self)


    class IntegerTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.IntegerTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(MParser.INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterIntegerType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitIntegerType(self)


    class DateTimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.DateTimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATETIME(self):
            return self.getToken(MParser.DATETIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterDateTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitDateTimeType(self)


    class BlobTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.BlobTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BLOB(self):
            return self.getToken(MParser.BLOB, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterBlobType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitBlobType(self)


    class UUIDTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.UUIDTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def UUID(self):
            return self.getToken(MParser.UUID, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterUUIDType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitUUIDType(self)


    class DecimalTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.DecimalTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL(self):
            return self.getToken(MParser.DECIMAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterDecimalType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitDecimalType(self)


    class CodeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.CodeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(MParser.CODE, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterCodeType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCodeType(self)


    class DateTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Native_typeContext)
            super(MParser.DateTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATE(self):
            return self.getToken(MParser.DATE, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterDateType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitDateType(self)



    def native_type(self):

        localctx = MParser.Native_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_native_type)
        try:
            self.state = 1444
            token = self._input.LA(1)
            if token in [MParser.BOOLEAN]:
                localctx = MParser.BooleanTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1430
                self.match(MParser.BOOLEAN)

            elif token in [MParser.CHARACTER]:
                localctx = MParser.CharacterTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1431
                self.match(MParser.CHARACTER)

            elif token in [MParser.TEXT]:
                localctx = MParser.TextTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1432
                self.match(MParser.TEXT)

            elif token in [MParser.IMAGE]:
                localctx = MParser.ImageTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1433
                self.match(MParser.IMAGE)

            elif token in [MParser.INTEGER]:
                localctx = MParser.IntegerTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1434
                self.match(MParser.INTEGER)

            elif token in [MParser.DECIMAL]:
                localctx = MParser.DecimalTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1435
                self.match(MParser.DECIMAL)

            elif token in [MParser.DOCUMENT]:
                localctx = MParser.DocumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1436
                self.match(MParser.DOCUMENT)

            elif token in [MParser.DATE]:
                localctx = MParser.DateTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1437
                self.match(MParser.DATE)

            elif token in [MParser.DATETIME]:
                localctx = MParser.DateTimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1438
                self.match(MParser.DATETIME)

            elif token in [MParser.TIME]:
                localctx = MParser.TimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1439
                self.match(MParser.TIME)

            elif token in [MParser.PERIOD]:
                localctx = MParser.PeriodTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1440
                self.match(MParser.PERIOD)

            elif token in [MParser.CODE]:
                localctx = MParser.CodeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1441
                self.match(MParser.CODE)

            elif token in [MParser.BLOB]:
                localctx = MParser.BlobTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1442
                self.match(MParser.BLOB)

            elif token in [MParser.UUID]:
                localctx = MParser.UUIDTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1443
                self.match(MParser.UUID)

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
            if isinstance( listener, MParserListener ):
                listener.enterCategory_type(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCategory_type(self)




    def category_type(self):

        localctx = MParser.Category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_category_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1446
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
            if isinstance( listener, MParserListener ):
                listener.enterMutable_category_type(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitMutable_category_type(self)




    def mutable_category_type(self):

        localctx = MParser.Mutable_category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_mutable_category_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1449
            _la = self._input.LA(1)
            if _la==MParser.MUTABLE:
                self.state = 1448
                self.match(MParser.MUTABLE)


            self.state = 1451 
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
            if isinstance( listener, MParserListener ):
                listener.enterCode_type(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCode_type(self)




    def code_type(self):

        localctx = MParser.Code_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_code_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1453
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
            if isinstance( listener, MParserListener ):
                listener.enterConcreteCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitConcreteCategoryDeclaration(self)


    class NativeCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a MParser.Category_declarationContext)
            super(MParser.NativeCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Native_category_declarationContext
            self.copyFrom(ctx)

        def native_category_declaration(self):
            return self.getTypedRuleContext(MParser.Native_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterNativeCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitNativeCategoryDeclaration(self)


    class SingletonCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a MParser.Category_declarationContext)
            super(MParser.SingletonCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Singleton_category_declarationContext
            self.copyFrom(ctx)

        def singleton_category_declaration(self):
            return self.getTypedRuleContext(MParser.Singleton_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterSingletonCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitSingletonCategoryDeclaration(self)



    def category_declaration(self):

        localctx = MParser.Category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_category_declaration)
        try:
            self.state = 1458
            la_ = self._interp.adaptivePredict(self._input,93,self._ctx)
            if la_ == 1:
                localctx = MParser.ConcreteCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1455 
                localctx.decl = self.concrete_category_declaration()
                pass

            elif la_ == 2:
                localctx = MParser.NativeCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1456 
                localctx.decl = self.native_category_declaration()
                pass

            elif la_ == 3:
                localctx = MParser.SingletonCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1457 
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
            if isinstance( listener, MParserListener ):
                listener.enterType_identifier_list(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitType_identifier_list(self)




    def type_identifier_list(self):

        localctx = MParser.Type_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_type_identifier_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1460 
            self.type_identifier()
            self.state = 1465
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,94,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1461
                    self.match(MParser.COMMA)
                    self.state = 1462 
                    self.type_identifier() 
                self.state = 1467
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,94,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterMethod_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitMethod_identifier(self)




    def method_identifier(self):

        localctx = MParser.Method_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_method_identifier)
        try:
            self.state = 1470
            token = self._input.LA(1)
            if token in [MParser.VARIABLE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1468 
                self.variable_identifier()

            elif token in [MParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1469 
                self.type_identifier()

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
            if isinstance( listener, MParserListener ):
                listener.enterTypeIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitTypeIdentifier(self)


    class SymbolIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a MParser.IdentifierContext)
            super(MParser.SymbolIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def symbol_identifier(self):
            return self.getTypedRuleContext(MParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterSymbolIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitSymbolIdentifier(self)


    class VariableIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a MParser.IdentifierContext)
            super(MParser.VariableIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterVariableIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitVariableIdentifier(self)



    def identifier(self):

        localctx = MParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_identifier)
        try:
            self.state = 1475
            token = self._input.LA(1)
            if token in [MParser.VARIABLE_IDENTIFIER]:
                localctx = MParser.VariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1472 
                self.variable_identifier()

            elif token in [MParser.TYPE_IDENTIFIER]:
                localctx = MParser.TypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1473 
                self.type_identifier()

            elif token in [MParser.SYMBOL_IDENTIFIER]:
                localctx = MParser.SymbolIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1474 
                self.symbol_identifier()

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
            if isinstance( listener, MParserListener ):
                listener.enterVariable_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitVariable_identifier(self)




    def variable_identifier(self):

        localctx = MParser.Variable_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_variable_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1477
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
            if isinstance( listener, MParserListener ):
                listener.enterAttribute_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitAttribute_identifier(self)




    def attribute_identifier(self):

        localctx = MParser.Attribute_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_attribute_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1479
            _la = self._input.LA(1)
            if not(_la==MParser.STORABLE or _la==MParser.VARIABLE_IDENTIFIER):
                self._errHandler.recoverInline(self)
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
            if isinstance( listener, MParserListener ):
                listener.enterType_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitType_identifier(self)




    def type_identifier(self):

        localctx = MParser.Type_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_type_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1481
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
            if isinstance( listener, MParserListener ):
                listener.enterSymbol_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitSymbol_identifier(self)




    def symbol_identifier(self):

        localctx = MParser.Symbol_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_symbol_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1483
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
            if isinstance( listener, MParserListener ):
                listener.enterArgument_list(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitArgument_list(self)




    def argument_list(self):

        localctx = MParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1485 
            self.argument()
            self.state = 1490
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMA:
                self.state = 1486
                self.match(MParser.COMMA)
                self.state = 1487 
                self.argument()
                self.state = 1492
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
            if isinstance( listener, MParserListener ):
                listener.enterOperatorArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitOperatorArgument(self)


    class CodeArgumentContext(ArgumentContext):

        def __init__(self, parser, ctx): # actually a MParser.ArgumentContext)
            super(MParser.CodeArgumentContext, self).__init__(parser)
            self.arg = None # Code_argumentContext
            self.copyFrom(ctx)

        def code_argument(self):
            return self.getTypedRuleContext(MParser.Code_argumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterCodeArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCodeArgument(self)



    def argument(self):

        localctx = MParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.state = 1498
            token = self._input.LA(1)
            if token in [MParser.CODE]:
                localctx = MParser.CodeArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1493 
                localctx.arg = self.code_argument()

            elif token in [MParser.MUTABLE, MParser.VARIABLE_IDENTIFIER]:
                localctx = MParser.OperatorArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1495
                _la = self._input.LA(1)
                if _la==MParser.MUTABLE:
                    self.state = 1494
                    self.match(MParser.MUTABLE)


                self.state = 1497 
                localctx.arg = self.operator_argument()

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
            if isinstance( listener, MParserListener ):
                listener.enterOperator_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitOperator_argument(self)




    def operator_argument(self):

        localctx = MParser.Operator_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_operator_argument)
        try:
            self.state = 1502
            la_ = self._interp.adaptivePredict(self._input,100,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1500 
                self.named_argument()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1501 
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
            if isinstance( listener, MParserListener ):
                listener.enterNamed_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitNamed_argument(self)




    def named_argument(self):

        localctx = MParser.Named_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_named_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1504 
            self.variable_identifier()
            self.state = 1507
            _la = self._input.LA(1)
            if _la==MParser.EQ:
                self.state = 1505
                self.match(MParser.EQ)
                self.state = 1506 
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
            if isinstance( listener, MParserListener ):
                listener.enterCode_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCode_argument(self)




    def code_argument(self):

        localctx = MParser.Code_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_code_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1509 
            self.code_type()
            self.state = 1510 
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
            if isinstance( listener, MParserListener ):
                listener.enterCategory_or_any_type(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCategory_or_any_type(self)




    def category_or_any_type(self):

        localctx = MParser.Category_or_any_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_category_or_any_type)
        try:
            self.state = 1514
            token = self._input.LA(1)
            if token in [MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.CODE, MParser.DOCUMENT, MParser.BLOB, MParser.IMAGE, MParser.UUID, MParser.ITERATOR, MParser.CURSOR, MParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1512 
                self.typedef(0)

            elif token in [MParser.ANY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1513 
                self.any_type(0)

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
            if isinstance( listener, MParserListener ):
                listener.enterAnyListType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitAnyListType(self)


    class AnyTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a MParser.Any_typeContext)
            super(MParser.AnyTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ANY(self):
            return self.getToken(MParser.ANY, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterAnyType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterAnyDictType(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitAnyDictType(self)



    def any_type(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Any_typeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 200
        self.enterRecursionRule(localctx, 200, self.RULE_any_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.AnyTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1517
            self.match(MParser.ANY)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1527
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,104,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1525
                    la_ = self._interp.adaptivePredict(self._input,103,self._ctx)
                    if la_ == 1:
                        localctx = MParser.AnyListTypeContext(self, MParser.Any_typeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1519
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1520
                        self.match(MParser.LBRAK)
                        self.state = 1521
                        self.match(MParser.RBRAK)
                        pass

                    elif la_ == 2:
                        localctx = MParser.AnyDictTypeContext(self, MParser.Any_typeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1522
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1523
                        self.match(MParser.LCURL)
                        self.state = 1524
                        self.match(MParser.RCURL)
                        pass

             
                self.state = 1529
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,104,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterMember_method_declaration_list(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitMember_method_declaration_list(self)




    def member_method_declaration_list(self):

        localctx = MParser.Member_method_declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_member_method_declaration_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1530 
            self.member_method_declaration()
            self.state = 1536
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,105,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1531 
                    self.lfp()
                    self.state = 1532 
                    self.member_method_declaration() 
                self.state = 1538
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,105,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterMember_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitMember_method_declaration(self)




    def member_method_declaration(self):

        localctx = MParser.Member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_member_method_declaration)
        try:
            self.state = 1544
            la_ = self._interp.adaptivePredict(self._input,106,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1539 
                self.setter_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1540 
                self.getter_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1541 
                self.concrete_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1542 
                self.abstract_method_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1543 
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
            if isinstance( listener, MParserListener ):
                listener.enterNative_member_method_declaration_list(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitNative_member_method_declaration_list(self)




    def native_member_method_declaration_list(self):

        localctx = MParser.Native_member_method_declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 206, self.RULE_native_member_method_declaration_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1546 
            self.native_member_method_declaration()
            self.state = 1552
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,107,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1547 
                    self.lfp()
                    self.state = 1548 
                    self.native_member_method_declaration() 
                self.state = 1554
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,107,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterNative_member_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitNative_member_method_declaration(self)




    def native_member_method_declaration(self):

        localctx = MParser.Native_member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_native_member_method_declaration)
        try:
            self.state = 1558
            la_ = self._interp.adaptivePredict(self._input,108,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1555 
                self.native_getter_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1556 
                self.native_setter_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1557 
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
            if isinstance( listener, MParserListener ):
                listener.enterPython2CategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterPython3CategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterJavaCategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterCSharpCategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterJavaScriptCategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavaScriptCategoryBinding(self)



    def native_category_binding(self):

        localctx = MParser.Native_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_native_category_binding)
        try:
            self.state = 1570
            token = self._input.LA(1)
            if token in [MParser.JAVA]:
                localctx = MParser.JavaCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1560
                self.match(MParser.JAVA)
                self.state = 1561 
                localctx.binding = self.java_class_identifier_expression(0)

            elif token in [MParser.CSHARP]:
                localctx = MParser.CSharpCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1562
                self.match(MParser.CSHARP)
                self.state = 1563 
                localctx.binding = self.csharp_identifier_expression(0)

            elif token in [MParser.PYTHON2]:
                localctx = MParser.Python2CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1564
                self.match(MParser.PYTHON2)
                self.state = 1565 
                localctx.binding = self.python_category_binding()

            elif token in [MParser.PYTHON3]:
                localctx = MParser.Python3CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1566
                self.match(MParser.PYTHON3)
                self.state = 1567 
                localctx.binding = self.python_category_binding()

            elif token in [MParser.JAVASCRIPT]:
                localctx = MParser.JavaScriptCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1568
                self.match(MParser.JAVASCRIPT)
                self.state = 1569 
                localctx.binding = self.javascript_category_binding()

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
            if isinstance( listener, MParserListener ):
                listener.enterPython_category_binding(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPython_category_binding(self)




    def python_category_binding(self):

        localctx = MParser.Python_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_python_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1572 
            self.identifier()
            self.state = 1574
            la_ = self._interp.adaptivePredict(self._input,110,self._ctx)
            if la_ == 1:
                self.state = 1573 
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
            if isinstance( listener, MParserListener ):
                listener.enterPython_module(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPython_module(self)




    def python_module(self):

        localctx = MParser.Python_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_python_module)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1576
            self.match(MParser.FROM)
            self.state = 1577 
            self.module_token()
            self.state = 1578
            self.match(MParser.COLON)
            self.state = 1579 
            self.identifier()
            self.state = 1584
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,111,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1580
                    self.match(MParser.DOT)
                    self.state = 1581 
                    self.identifier() 
                self.state = 1586
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,111,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterJavascript_category_binding(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavascript_category_binding(self)




    def javascript_category_binding(self):

        localctx = MParser.Javascript_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_javascript_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1587 
            self.identifier()
            self.state = 1589
            la_ = self._interp.adaptivePredict(self._input,112,self._ctx)
            if la_ == 1:
                self.state = 1588 
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
            if isinstance( listener, MParserListener ):
                listener.enterJavascript_module(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavascript_module(self)




    def javascript_module(self):

        localctx = MParser.Javascript_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_javascript_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1591
            self.match(MParser.FROM)
            self.state = 1592 
            self.module_token()
            self.state = 1593
            self.match(MParser.COLON)
            self.state = 1595
            _la = self._input.LA(1)
            if _la==MParser.SLASH:
                self.state = 1594
                self.match(MParser.SLASH)


            self.state = 1597 
            self.javascript_identifier()
            self.state = 1602
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,114,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1598
                    self.match(MParser.SLASH)
                    self.state = 1599 
                    self.javascript_identifier() 
                self.state = 1604
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,114,self._ctx)

            self.state = 1607
            la_ = self._interp.adaptivePredict(self._input,115,self._ctx)
            if la_ == 1:
                self.state = 1605
                self.match(MParser.DOT)
                self.state = 1606 
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
            if isinstance( listener, MParserListener ):
                listener.enterVariable_identifier_list(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitVariable_identifier_list(self)




    def variable_identifier_list(self):

        localctx = MParser.Variable_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 220, self.RULE_variable_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1609 
            self.variable_identifier()
            self.state = 1614
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMA:
                self.state = 1610
                self.match(MParser.COMMA)
                self.state = 1611 
                self.variable_identifier()
                self.state = 1616
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
            if isinstance( listener, MParserListener ):
                listener.enterAttribute_identifier_list(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitAttribute_identifier_list(self)




    def attribute_identifier_list(self):

        localctx = MParser.Attribute_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 222, self.RULE_attribute_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1617 
            self.attribute_identifier()
            self.state = 1622
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMA:
                self.state = 1618
                self.match(MParser.COMMA)
                self.state = 1619 
                self.attribute_identifier()
                self.state = 1624
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
            if isinstance( listener, MParserListener ):
                listener.enterMethod_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitMethod_declaration(self)




    def method_declaration(self):

        localctx = MParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 224, self.RULE_method_declaration)
        try:
            self.state = 1629
            la_ = self._interp.adaptivePredict(self._input,118,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1625 
                self.abstract_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1626 
                self.concrete_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1627 
                self.native_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1628 
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
            if isinstance( listener, MParserListener ):
                listener.enterComment_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitComment_statement(self)




    def comment_statement(self):

        localctx = MParser.Comment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 226, self.RULE_comment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1631
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
            if isinstance( listener, MParserListener ):
                listener.enterNative_statement_list(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitNative_statement_list(self)




    def native_statement_list(self):

        localctx = MParser.Native_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 228, self.RULE_native_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1633 
            self.native_statement()
            self.state = 1639
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,119,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1634 
                    self.lfp()
                    self.state = 1635 
                    self.native_statement() 
                self.state = 1641
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,119,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterCSharpNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterJavaNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterJavaScriptNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterPython2NativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterPython3NativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPython3NativeStatement(self)



    def native_statement(self):

        localctx = MParser.Native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 230, self.RULE_native_statement)
        try:
            self.state = 1652
            token = self._input.LA(1)
            if token in [MParser.JAVA]:
                localctx = MParser.JavaNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1642
                self.match(MParser.JAVA)
                self.state = 1643 
                self.java_statement()

            elif token in [MParser.CSHARP]:
                localctx = MParser.CSharpNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1644
                self.match(MParser.CSHARP)
                self.state = 1645 
                self.csharp_statement()

            elif token in [MParser.PYTHON2]:
                localctx = MParser.Python2NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1646
                self.match(MParser.PYTHON2)
                self.state = 1647 
                self.python_native_statement()

            elif token in [MParser.PYTHON3]:
                localctx = MParser.Python3NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1648
                self.match(MParser.PYTHON3)
                self.state = 1649 
                self.python_native_statement()

            elif token in [MParser.JAVASCRIPT]:
                localctx = MParser.JavaScriptNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1650
                self.match(MParser.JAVASCRIPT)
                self.state = 1651 
                self.javascript_native_statement()

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
            if isinstance( listener, MParserListener ):
                listener.enterPython_native_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPython_native_statement(self)




    def python_native_statement(self):

        localctx = MParser.Python_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_python_native_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1654 
            self.python_statement()
            self.state = 1656
            _la = self._input.LA(1)
            if _la==MParser.SEMI:
                self.state = 1655
                self.match(MParser.SEMI)


            self.state = 1659
            _la = self._input.LA(1)
            if _la==MParser.FROM:
                self.state = 1658 
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
            if isinstance( listener, MParserListener ):
                listener.enterJavascript_native_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavascript_native_statement(self)




    def javascript_native_statement(self):

        localctx = MParser.Javascript_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_javascript_native_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1661 
            self.javascript_statement()
            self.state = 1663
            _la = self._input.LA(1)
            if _la==MParser.SEMI:
                self.state = 1662
                self.match(MParser.SEMI)


            self.state = 1666
            _la = self._input.LA(1)
            if _la==MParser.FROM:
                self.state = 1665 
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
            if isinstance( listener, MParserListener ):
                listener.enterStatement_list(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitStatement_list(self)




    def statement_list(self):

        localctx = MParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1668 
            self.statement()
            self.state = 1674
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,125,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1669 
                    self.lfp()
                    self.state = 1670 
                    self.statement() 
                self.state = 1676
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,125,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterAssertion_list(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitAssertion_list(self)




    def assertion_list(self):

        localctx = MParser.Assertion_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_assertion_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1677 
            self.assertion()
            self.state = 1683
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,126,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1678 
                    self.lfp()
                    self.state = 1679 
                    self.assertion() 
                self.state = 1685
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,126,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterSwitch_case_statement_list(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitSwitch_case_statement_list(self)




    def switch_case_statement_list(self):

        localctx = MParser.Switch_case_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_switch_case_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1686 
            self.switch_case_statement()
            self.state = 1692
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,127,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1687 
                    self.lfp()
                    self.state = 1688 
                    self.switch_case_statement() 
                self.state = 1694
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,127,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterCatch_statement_list(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCatch_statement_list(self)




    def catch_statement_list(self):

        localctx = MParser.Catch_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_catch_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1695 
            self.catch_statement()
            self.state = 1701
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,128,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1696 
                    self.lfp()
                    self.state = 1697 
                    self.catch_statement() 
                self.state = 1703
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,128,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterLiteralListLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterLiteralRangeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterLiteralSetLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitLiteralSetLiteral(self)



    def literal_collection(self):

        localctx = MParser.Literal_collectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_literal_collection)
        try:
            self.state = 1718
            la_ = self._interp.adaptivePredict(self._input,129,self._ctx)
            if la_ == 1:
                localctx = MParser.LiteralRangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1704
                self.match(MParser.LBRAK)
                self.state = 1705 
                localctx.low = self.atomic_literal()
                self.state = 1706
                self.match(MParser.RANGE)
                self.state = 1707 
                localctx.high = self.atomic_literal()
                self.state = 1708
                self.match(MParser.RBRAK)
                pass

            elif la_ == 2:
                localctx = MParser.LiteralListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1710
                self.match(MParser.LBRAK)
                self.state = 1711 
                self.literal_list_literal()
                self.state = 1712
                self.match(MParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = MParser.LiteralSetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1714
                self.match(MParser.LT)
                self.state = 1715 
                self.literal_list_literal()
                self.state = 1716
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
            if isinstance( listener, MParserListener ):
                listener.enterMinIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitMinIntegerLiteral(self)


    class DateLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.DateLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATE_LITERAL(self):
            return self.getToken(MParser.DATE_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterDateLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitDateLiteral(self)


    class BooleanLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.BooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(MParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitBooleanLiteral(self)


    class HexadecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.HexadecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def HEXA_LITERAL(self):
            return self.getToken(MParser.HEXA_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterHexadecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitHexadecimalLiteral(self)


    class UUIDLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.UUIDLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def UUID_LITERAL(self):
            return self.getToken(MParser.UUID_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterUUIDLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitUUIDLiteral(self)


    class MaxIntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.MaxIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def MAX_INTEGER(self):
            return self.getToken(MParser.MAX_INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterMaxIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitMaxIntegerLiteral(self)


    class DateTimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.DateTimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATETIME_LITERAL(self):
            return self.getToken(MParser.DATETIME_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterDateTimeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitDateTimeLiteral(self)


    class PeriodLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.PeriodLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def PERIOD_LITERAL(self):
            return self.getToken(MParser.PERIOD_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterPeriodLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPeriodLiteral(self)


    class DecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.DecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(MParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitDecimalLiteral(self)


    class TextLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.TextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(MParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitTextLiteral(self)


    class NullLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.NullLiteralContext, self).__init__(parser)
            self.n = None # Null_literalContext
            self.copyFrom(ctx)

        def null_literal(self):
            return self.getTypedRuleContext(MParser.Null_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterNullLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitNullLiteral(self)


    class IntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.IntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(MParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitIntegerLiteral(self)


    class TimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.TimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TIME_LITERAL(self):
            return self.getToken(MParser.TIME_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterTimeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitTimeLiteral(self)


    class CharacterLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a MParser.Atomic_literalContext)
            super(MParser.CharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(MParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCharacterLiteral(self)



    def atomic_literal(self):

        localctx = MParser.Atomic_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_atomic_literal)
        try:
            self.state = 1734
            token = self._input.LA(1)
            if token in [MParser.MIN_INTEGER]:
                localctx = MParser.MinIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1720
                localctx.t = self.match(MParser.MIN_INTEGER)

            elif token in [MParser.MAX_INTEGER]:
                localctx = MParser.MaxIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1721
                localctx.t = self.match(MParser.MAX_INTEGER)

            elif token in [MParser.INTEGER_LITERAL]:
                localctx = MParser.IntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1722
                localctx.t = self.match(MParser.INTEGER_LITERAL)

            elif token in [MParser.HEXA_LITERAL]:
                localctx = MParser.HexadecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1723
                localctx.t = self.match(MParser.HEXA_LITERAL)

            elif token in [MParser.CHAR_LITERAL]:
                localctx = MParser.CharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1724
                localctx.t = self.match(MParser.CHAR_LITERAL)

            elif token in [MParser.DATE_LITERAL]:
                localctx = MParser.DateLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1725
                localctx.t = self.match(MParser.DATE_LITERAL)

            elif token in [MParser.TIME_LITERAL]:
                localctx = MParser.TimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1726
                localctx.t = self.match(MParser.TIME_LITERAL)

            elif token in [MParser.TEXT_LITERAL]:
                localctx = MParser.TextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1727
                localctx.t = self.match(MParser.TEXT_LITERAL)

            elif token in [MParser.DECIMAL_LITERAL]:
                localctx = MParser.DecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1728
                localctx.t = self.match(MParser.DECIMAL_LITERAL)

            elif token in [MParser.DATETIME_LITERAL]:
                localctx = MParser.DateTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1729
                localctx.t = self.match(MParser.DATETIME_LITERAL)

            elif token in [MParser.BOOLEAN_LITERAL]:
                localctx = MParser.BooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1730
                localctx.t = self.match(MParser.BOOLEAN_LITERAL)

            elif token in [MParser.PERIOD_LITERAL]:
                localctx = MParser.PeriodLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1731
                localctx.t = self.match(MParser.PERIOD_LITERAL)

            elif token in [MParser.UUID_LITERAL]:
                localctx = MParser.UUIDLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1732
                localctx.t = self.match(MParser.UUID_LITERAL)

            elif token in [MParser.NONE]:
                localctx = MParser.NullLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1733 
                localctx.n = self.null_literal()

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
            if isinstance( listener, MParserListener ):
                listener.enterLiteral_list_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitLiteral_list_literal(self)




    def literal_list_literal(self):

        localctx = MParser.Literal_list_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_literal_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1736 
            self.atomic_literal()
            self.state = 1741
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMA:
                self.state = 1737
                self.match(MParser.COMMA)
                self.state = 1738 
                self.atomic_literal()
                self.state = 1743
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
            if isinstance( listener, MParserListener ):
                listener.enterThisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitThisExpression(self)


    class ParenthesisExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Selectable_expressionContext)
            super(MParser.ParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Parenthesis_expressionContext
            self.copyFrom(ctx)

        def parenthesis_expression(self):
            return self.getTypedRuleContext(MParser.Parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterParenthesisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitParenthesisExpression(self)


    class LiteralExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Selectable_expressionContext)
            super(MParser.LiteralExpressionContext, self).__init__(parser)
            self.exp = None # Literal_expressionContext
            self.copyFrom(ctx)

        def literal_expression(self):
            return self.getTypedRuleContext(MParser.Literal_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitLiteralExpression(self)


    class IdentifierExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Selectable_expressionContext)
            super(MParser.IdentifierExpressionContext, self).__init__(parser)
            self.exp = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(MParser.IdentifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitIdentifierExpression(self)



    def selectable_expression(self):

        localctx = MParser.Selectable_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_selectable_expression)
        try:
            self.state = 1748
            la_ = self._interp.adaptivePredict(self._input,132,self._ctx)
            if la_ == 1:
                localctx = MParser.ParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1744 
                localctx.exp = self.parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = MParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1745 
                localctx.exp = self.literal_expression()
                pass

            elif la_ == 3:
                localctx = MParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1746 
                localctx.exp = self.identifier()
                pass

            elif la_ == 4:
                localctx = MParser.ThisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1747 
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
            if isinstance( listener, MParserListener ):
                listener.enterThis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitThis_expression(self)




    def this_expression(self):

        localctx = MParser.This_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 252, self.RULE_this_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1750
            _la = self._input.LA(1)
            if not(_la==MParser.SELF or _la==MParser.THIS):
                self._errHandler.recoverInline(self)
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
            if isinstance( listener, MParserListener ):
                listener.enterParenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitParenthesis_expression(self)




    def parenthesis_expression(self):

        localctx = MParser.Parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 254, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1752
            self.match(MParser.LPAR)
            self.state = 1753 
            self.expression(0)
            self.state = 1754
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
            if isinstance( listener, MParserListener ):
                listener.enterLiteral_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitLiteral_expression(self)




    def literal_expression(self):

        localctx = MParser.Literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_literal_expression)
        try:
            self.state = 1758
            token = self._input.LA(1)
            if token in [MParser.NONE, MParser.BOOLEAN_LITERAL, MParser.CHAR_LITERAL, MParser.MIN_INTEGER, MParser.MAX_INTEGER, MParser.TEXT_LITERAL, MParser.UUID_LITERAL, MParser.INTEGER_LITERAL, MParser.HEXA_LITERAL, MParser.DECIMAL_LITERAL, MParser.DATETIME_LITERAL, MParser.TIME_LITERAL, MParser.DATE_LITERAL, MParser.PERIOD_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1756 
                self.atomic_literal()

            elif token in [MParser.LPAR, MParser.LBRAK, MParser.LCURL, MParser.LT, MParser.MUTABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1757 
                self.collection_literal()

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
            if isinstance( listener, MParserListener ):
                listener.enterCollection_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCollection_literal(self)




    def collection_literal(self):

        localctx = MParser.Collection_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_collection_literal)
        try:
            self.state = 1765
            la_ = self._interp.adaptivePredict(self._input,134,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1760 
                self.range_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1761 
                self.list_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1762 
                self.set_literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1763 
                self.dict_literal()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1764 
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
            if isinstance( listener, MParserListener ):
                listener.enterTuple_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitTuple_literal(self)




    def tuple_literal(self):

        localctx = MParser.Tuple_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_tuple_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1768
            _la = self._input.LA(1)
            if _la==MParser.MUTABLE:
                self.state = 1767
                self.match(MParser.MUTABLE)


            self.state = 1770
            self.match(MParser.LPAR)
            self.state = 1772
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (MParser.EXECUTE - 98)) | (1 << (MParser.FETCH - 98)) | (1 << (MParser.MUTABLE - 98)) | (1 << (MParser.NONE - 98)) | (1 << (MParser.NOT - 98)) | (1 << (MParser.READ - 98)) | (1 << (MParser.SELF - 98)) | (1 << (MParser.SORTED - 98)) | (1 << (MParser.THIS - 98)) | (1 << (MParser.BOOLEAN_LITERAL - 98)) | (1 << (MParser.CHAR_LITERAL - 98)) | (1 << (MParser.MIN_INTEGER - 98)) | (1 << (MParser.MAX_INTEGER - 98)) | (1 << (MParser.SYMBOL_IDENTIFIER - 98)) | (1 << (MParser.TYPE_IDENTIFIER - 98)))) != 0) or ((((_la - 162)) & ~0x3f) == 0 and ((1 << (_la - 162)) & ((1 << (MParser.VARIABLE_IDENTIFIER - 162)) | (1 << (MParser.TEXT_LITERAL - 162)) | (1 << (MParser.UUID_LITERAL - 162)) | (1 << (MParser.INTEGER_LITERAL - 162)) | (1 << (MParser.HEXA_LITERAL - 162)) | (1 << (MParser.DECIMAL_LITERAL - 162)) | (1 << (MParser.DATETIME_LITERAL - 162)) | (1 << (MParser.TIME_LITERAL - 162)) | (1 << (MParser.DATE_LITERAL - 162)) | (1 << (MParser.PERIOD_LITERAL - 162)))) != 0):
                self.state = 1771 
                self.expression_tuple()


            self.state = 1774
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
            if isinstance( listener, MParserListener ):
                listener.enterDict_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitDict_literal(self)




    def dict_literal(self):

        localctx = MParser.Dict_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 262, self.RULE_dict_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1777
            _la = self._input.LA(1)
            if _la==MParser.MUTABLE:
                self.state = 1776
                self.match(MParser.MUTABLE)


            self.state = 1779
            self.match(MParser.LCURL)
            self.state = 1781
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (MParser.EXECUTE - 98)) | (1 << (MParser.FETCH - 98)) | (1 << (MParser.MUTABLE - 98)) | (1 << (MParser.NONE - 98)) | (1 << (MParser.NOT - 98)) | (1 << (MParser.READ - 98)) | (1 << (MParser.SELF - 98)) | (1 << (MParser.SORTED - 98)) | (1 << (MParser.THIS - 98)) | (1 << (MParser.BOOLEAN_LITERAL - 98)) | (1 << (MParser.CHAR_LITERAL - 98)) | (1 << (MParser.MIN_INTEGER - 98)) | (1 << (MParser.MAX_INTEGER - 98)) | (1 << (MParser.SYMBOL_IDENTIFIER - 98)) | (1 << (MParser.TYPE_IDENTIFIER - 98)))) != 0) or ((((_la - 162)) & ~0x3f) == 0 and ((1 << (_la - 162)) & ((1 << (MParser.VARIABLE_IDENTIFIER - 162)) | (1 << (MParser.TEXT_LITERAL - 162)) | (1 << (MParser.UUID_LITERAL - 162)) | (1 << (MParser.INTEGER_LITERAL - 162)) | (1 << (MParser.HEXA_LITERAL - 162)) | (1 << (MParser.DECIMAL_LITERAL - 162)) | (1 << (MParser.DATETIME_LITERAL - 162)) | (1 << (MParser.TIME_LITERAL - 162)) | (1 << (MParser.DATE_LITERAL - 162)) | (1 << (MParser.PERIOD_LITERAL - 162)))) != 0):
                self.state = 1780 
                self.dict_entry_list()


            self.state = 1783
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
            if isinstance( listener, MParserListener ):
                listener.enterExpression_tuple(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitExpression_tuple(self)




    def expression_tuple(self):

        localctx = MParser.Expression_tupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_expression_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1785 
            self.expression(0)
            self.state = 1786
            self.match(MParser.COMMA)
            self.state = 1795
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.LCURL) | (1 << MParser.MINUS) | (1 << MParser.LT) | (1 << MParser.CODE) | (1 << MParser.DOCUMENT) | (1 << MParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (MParser.EXECUTE - 98)) | (1 << (MParser.FETCH - 98)) | (1 << (MParser.MUTABLE - 98)) | (1 << (MParser.NONE - 98)) | (1 << (MParser.NOT - 98)) | (1 << (MParser.READ - 98)) | (1 << (MParser.SELF - 98)) | (1 << (MParser.SORTED - 98)) | (1 << (MParser.THIS - 98)) | (1 << (MParser.BOOLEAN_LITERAL - 98)) | (1 << (MParser.CHAR_LITERAL - 98)) | (1 << (MParser.MIN_INTEGER - 98)) | (1 << (MParser.MAX_INTEGER - 98)) | (1 << (MParser.SYMBOL_IDENTIFIER - 98)) | (1 << (MParser.TYPE_IDENTIFIER - 98)))) != 0) or ((((_la - 162)) & ~0x3f) == 0 and ((1 << (_la - 162)) & ((1 << (MParser.VARIABLE_IDENTIFIER - 162)) | (1 << (MParser.TEXT_LITERAL - 162)) | (1 << (MParser.UUID_LITERAL - 162)) | (1 << (MParser.INTEGER_LITERAL - 162)) | (1 << (MParser.HEXA_LITERAL - 162)) | (1 << (MParser.DECIMAL_LITERAL - 162)) | (1 << (MParser.DATETIME_LITERAL - 162)) | (1 << (MParser.TIME_LITERAL - 162)) | (1 << (MParser.DATE_LITERAL - 162)) | (1 << (MParser.PERIOD_LITERAL - 162)))) != 0):
                self.state = 1787 
                self.expression(0)
                self.state = 1792
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MParser.COMMA:
                    self.state = 1788
                    self.match(MParser.COMMA)
                    self.state = 1789 
                    self.expression(0)
                    self.state = 1794
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
            if isinstance( listener, MParserListener ):
                listener.enterDict_entry_list(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitDict_entry_list(self)




    def dict_entry_list(self):

        localctx = MParser.Dict_entry_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_dict_entry_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1797 
            self.dict_entry()
            self.state = 1802
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MParser.COMMA:
                self.state = 1798
                self.match(MParser.COMMA)
                self.state = 1799 
                self.dict_entry()
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
            if isinstance( listener, MParserListener ):
                listener.enterDict_entry(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitDict_entry(self)




    def dict_entry(self):

        localctx = MParser.Dict_entryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_dict_entry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1805 
            localctx.key = self.expression(0)
            self.state = 1806
            self.match(MParser.COLON)
            self.state = 1807 
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
            if isinstance( listener, MParserListener ):
                listener.enterSliceFirstAndLast(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterSliceLastOnly(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterSliceFirstOnly(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitSliceFirstOnly(self)



    def slice_arguments(self):

        localctx = MParser.Slice_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_slice_arguments)
        try:
            self.state = 1818
            la_ = self._interp.adaptivePredict(self._input,142,self._ctx)
            if la_ == 1:
                localctx = MParser.SliceFirstAndLastContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1809 
                localctx.first = self.expression(0)
                self.state = 1810
                self.match(MParser.COLON)
                self.state = 1811 
                localctx.last = self.expression(0)
                pass

            elif la_ == 2:
                localctx = MParser.SliceFirstOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1813 
                localctx.first = self.expression(0)
                self.state = 1814
                self.match(MParser.COLON)
                pass

            elif la_ == 3:
                localctx = MParser.SliceLastOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1816
                self.match(MParser.COLON)
                self.state = 1817 
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
            if isinstance( listener, MParserListener ):
                listener.enterAssign_variable_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitAssign_variable_statement(self)




    def assign_variable_statement(self):

        localctx = MParser.Assign_variable_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 272, self.RULE_assign_variable_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1820 
            self.variable_identifier()
            self.state = 1821 
            self.assign()
            self.state = 1822 
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
            if isinstance( listener, MParserListener ):
                listener.enterChildInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitChildInstance(self)


    class RootInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a MParser.Assignable_instanceContext)
            super(MParser.RootInstanceContext, self).__init__(parser)
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(MParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterRootInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitRootInstance(self)



    def assignable_instance(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Assignable_instanceContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 274
        self.enterRecursionRule(localctx, 274, self.RULE_assignable_instance, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.RootInstanceContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1825 
            self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1831
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,143,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.ChildInstanceContext(self, MParser.Assignable_instanceContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignable_instance)
                    self.state = 1827
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1828 
                    self.child_instance() 
                self.state = 1833
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,143,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterIsATypeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitIsATypeExpression(self)


    class IsOtherExpressionContext(Is_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Is_expressionContext)
            super(MParser.IsOtherExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterIsOtherExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitIsOtherExpression(self)



    def is_expression(self):

        localctx = MParser.Is_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_is_expression)
        try:
            self.state = 1838
            la_ = self._interp.adaptivePredict(self._input,144,self._ctx)
            if la_ == 1:
                localctx = MParser.IsATypeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1834
                if not self.willBeAOrAn():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willBeAOrAn()")
                self.state = 1835
                self.match(MParser.VARIABLE_IDENTIFIER)
                self.state = 1836 
                self.category_or_any_type()
                pass

            elif la_ == 2:
                localctx = MParser.IsOtherExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1837 
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
            if isinstance( listener, MParserListener ):
                listener.enterRead_all_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitRead_all_expression(self)




    def read_all_expression(self):

        localctx = MParser.Read_all_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 278, self.RULE_read_all_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1840
            self.match(MParser.READ)
            self.state = 1841
            self.match(MParser.ALL)
            self.state = 1842
            self.match(MParser.FROM)
            self.state = 1843 
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
            if isinstance( listener, MParserListener ):
                listener.enterRead_one_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitRead_one_expression(self)




    def read_one_expression(self):

        localctx = MParser.Read_one_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_read_one_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1845
            self.match(MParser.READ)
            self.state = 1846
            self.match(MParser.ONE)
            self.state = 1847
            self.match(MParser.FROM)
            self.state = 1848 
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
            if isinstance( listener, MParserListener ):
                listener.enterOrder_by_list(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitOrder_by_list(self)




    def order_by_list(self):

        localctx = MParser.Order_by_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 282, self.RULE_order_by_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1850 
            self.order_by()
            self.state = 1855
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,145,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1851
                    self.match(MParser.COMMA)
                    self.state = 1852 
                    self.order_by() 
                self.state = 1857
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,145,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterOrder_by(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitOrder_by(self)




    def order_by(self):

        localctx = MParser.Order_byContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_order_by)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1858 
            self.variable_identifier()
            self.state = 1863
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,146,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1859
                    self.match(MParser.DOT)
                    self.state = 1860 
                    self.variable_identifier() 
                self.state = 1865
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,146,self._ctx)

            self.state = 1867
            la_ = self._interp.adaptivePredict(self._input,147,self._ctx)
            if la_ == 1:
                self.state = 1866
                _la = self._input.LA(1)
                if not(_la==MParser.ASC or _la==MParser.DESC):
                    self._errHandler.recoverInline(self)
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
            if isinstance( listener, MParserListener ):
                listener.enterOperatorPlus(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitOperatorPlus(self)


    class OperatorDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a MParser.OperatorContext)
            super(MParser.OperatorDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def divide(self):
            return self.getTypedRuleContext(MParser.DivideContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterOperatorDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitOperatorDivide(self)


    class OperatorIDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a MParser.OperatorContext)
            super(MParser.OperatorIDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def idivide(self):
            return self.getTypedRuleContext(MParser.IdivideContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterOperatorIDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitOperatorIDivide(self)


    class OperatorMultiplyContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a MParser.OperatorContext)
            super(MParser.OperatorMultiplyContext, self).__init__(parser)
            self.copyFrom(ctx)

        def multiply(self):
            return self.getTypedRuleContext(MParser.MultiplyContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterOperatorMultiply(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitOperatorMultiply(self)


    class OperatorMinusContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a MParser.OperatorContext)
            super(MParser.OperatorMinusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(MParser.MINUS, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterOperatorMinus(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitOperatorMinus(self)


    class OperatorModuloContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a MParser.OperatorContext)
            super(MParser.OperatorModuloContext, self).__init__(parser)
            self.copyFrom(ctx)

        def modulo(self):
            return self.getTypedRuleContext(MParser.ModuloContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterOperatorModulo(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitOperatorModulo(self)



    def operator(self):

        localctx = MParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 286, self.RULE_operator)
        try:
            self.state = 1875
            token = self._input.LA(1)
            if token in [MParser.PLUS]:
                localctx = MParser.OperatorPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1869
                self.match(MParser.PLUS)

            elif token in [MParser.MINUS]:
                localctx = MParser.OperatorMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1870
                self.match(MParser.MINUS)

            elif token in [MParser.STAR]:
                localctx = MParser.OperatorMultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1871 
                self.multiply()

            elif token in [MParser.SLASH]:
                localctx = MParser.OperatorDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1872 
                self.divide()

            elif token in [MParser.BSLASH]:
                localctx = MParser.OperatorIDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1873 
                self.idivide()

            elif token in [MParser.PERCENT, MParser.MODULO]:
                localctx = MParser.OperatorModuloContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1874 
                self.modulo()

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
            super(MParser.New_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(MParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MParser.RULE_new_token

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterNew_token(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitNew_token(self)




    def new_token(self):

        localctx = MParser.New_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 288, self.RULE_new_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1877
            localctx.i1 = self.match(MParser.VARIABLE_IDENTIFIER)
            self.state = 1878
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
            if isinstance( listener, MParserListener ):
                listener.enterKey_token(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitKey_token(self)




    def key_token(self):

        localctx = MParser.Key_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_key_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1880
            localctx.i1 = self.match(MParser.VARIABLE_IDENTIFIER)
            self.state = 1881
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
            if isinstance( listener, MParserListener ):
                listener.enterModule_token(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitModule_token(self)




    def module_token(self):

        localctx = MParser.Module_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 292, self.RULE_module_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1883
            localctx.i1 = self.match(MParser.VARIABLE_IDENTIFIER)
            self.state = 1884
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
            if isinstance( listener, MParserListener ):
                listener.enterValue_token(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitValue_token(self)




    def value_token(self):

        localctx = MParser.Value_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_value_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1886
            localctx.i1 = self.match(MParser.VARIABLE_IDENTIFIER)
            self.state = 1887
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
            if isinstance( listener, MParserListener ):
                listener.enterSymbols_token(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitSymbols_token(self)




    def symbols_token(self):

        localctx = MParser.Symbols_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 296, self.RULE_symbols_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1889
            localctx.i1 = self.match(MParser.VARIABLE_IDENTIFIER)
            self.state = 1890
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
            if isinstance( listener, MParserListener ):
                listener.enterAssign(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitAssign(self)




    def assign(self):

        localctx = MParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1892
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
            if isinstance( listener, MParserListener ):
                listener.enterMultiply(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitMultiply(self)




    def multiply(self):

        localctx = MParser.MultiplyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 300, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1894
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
            if isinstance( listener, MParserListener ):
                listener.enterDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitDivide(self)




    def divide(self):

        localctx = MParser.DivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_divide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1896
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
            if isinstance( listener, MParserListener ):
                listener.enterIdivide(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitIdivide(self)




    def idivide(self):

        localctx = MParser.IdivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_idivide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1898
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
            if isinstance( listener, MParserListener ):
                listener.enterModulo(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitModulo(self)




    def modulo(self):

        localctx = MParser.ModuloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 306, self.RULE_modulo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1900
            _la = self._input.LA(1)
            if not(_la==MParser.PERCENT or _la==MParser.MODULO):
                self._errHandler.recoverInline(self)
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
            if isinstance( listener, MParserListener ):
                listener.enterJavascriptStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterJavascriptReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavascriptReturnStatement(self)



    def javascript_statement(self):

        localctx = MParser.Javascript_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 308, self.RULE_javascript_statement)
        try:
            self.state = 1909
            token = self._input.LA(1)
            if token in [MParser.RETURN]:
                localctx = MParser.JavascriptReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1902
                self.match(MParser.RETURN)
                self.state = 1903 
                localctx.exp = self.javascript_expression(0)
                self.state = 1904
                self.match(MParser.SEMI)

            elif token in [MParser.LPAR, MParser.LBRAK, MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.READ, MParser.SELF, MParser.TEST, MParser.THIS, MParser.WRITE, MParser.BOOLEAN_LITERAL, MParser.CHAR_LITERAL, MParser.SYMBOL_IDENTIFIER, MParser.TYPE_IDENTIFIER, MParser.VARIABLE_IDENTIFIER, MParser.DOLLAR_IDENTIFIER, MParser.TEXT_LITERAL, MParser.INTEGER_LITERAL, MParser.DECIMAL_LITERAL]:
                localctx = MParser.JavascriptStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1906 
                localctx.exp = self.javascript_expression(0)
                self.state = 1907
                self.match(MParser.SEMI)

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
            if isinstance( listener, MParserListener ):
                listener.enterJavascriptSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavascriptSelectorExpression(self)


    class JavascriptPrimaryExpressionContext(Javascript_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_expressionContext)
            super(MParser.JavascriptPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_primary_expressionContext
            self.copyFrom(ctx)

        def javascript_primary_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterJavascriptPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavascriptPrimaryExpression(self)



    def javascript_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Javascript_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 310
        self.enterRecursionRule(localctx, 310, self.RULE_javascript_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.JavascriptPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1912 
            localctx.exp = self.javascript_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1918
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,150,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.JavascriptSelectorExpressionContext(self, MParser.Javascript_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_expression)
                    self.state = 1914
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1915 
                    localctx.child = self.javascript_selector_expression() 
                self.state = 1920
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,150,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterJavascript_primary_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavascript_primary_expression(self)




    def javascript_primary_expression(self):

        localctx = MParser.Javascript_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 312, self.RULE_javascript_primary_expression)
        try:
            self.state = 1928
            la_ = self._interp.adaptivePredict(self._input,151,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1921 
                self.javascript_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1922 
                self.javascript_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1923 
                self.javascript_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1924 
                self.javascript_identifier_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1925 
                self.javascript_literal_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1926 
                self.javascript_method_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1927 
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
            if isinstance( listener, MParserListener ):
                listener.enterJavascript_this_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavascript_this_expression(self)




    def javascript_this_expression(self):

        localctx = MParser.Javascript_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 314, self.RULE_javascript_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1930 
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
            if isinstance( listener, MParserListener ):
                listener.enterJavascript_new_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavascript_new_expression(self)




    def javascript_new_expression(self):

        localctx = MParser.Javascript_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 316, self.RULE_javascript_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1932 
            self.new_token()
            self.state = 1933 
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
            if isinstance( listener, MParserListener ):
                listener.enterJavaScriptMemberExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavaScriptMemberExpression(self)


    class JavaScriptItemExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_selector_expressionContext)
            super(MParser.JavaScriptItemExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_item_expressionContext
            self.copyFrom(ctx)

        def javascript_item_expression(self):
            return self.getTypedRuleContext(MParser.Javascript_item_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterJavaScriptItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterJavaScriptMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavaScriptMethodExpression(self)



    def javascript_selector_expression(self):

        localctx = MParser.Javascript_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 318, self.RULE_javascript_selector_expression)
        try:
            self.state = 1940
            la_ = self._interp.adaptivePredict(self._input,152,self._ctx)
            if la_ == 1:
                localctx = MParser.JavaScriptMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1935
                self.match(MParser.DOT)
                self.state = 1936 
                localctx.method = self.javascript_method_expression()
                pass

            elif la_ == 2:
                localctx = MParser.JavaScriptMemberExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1937
                self.match(MParser.DOT)
                self.state = 1938 
                localctx.name = self.javascript_identifier()
                pass

            elif la_ == 3:
                localctx = MParser.JavaScriptItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1939 
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
            if isinstance( listener, MParserListener ):
                listener.enterJavascript_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavascript_method_expression(self)




    def javascript_method_expression(self):

        localctx = MParser.Javascript_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 320, self.RULE_javascript_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1942 
            localctx.name = self.javascript_identifier()
            self.state = 1943
            self.match(MParser.LPAR)
            self.state = 1945
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.LBRAK) | (1 << MParser.BOOLEAN) | (1 << MParser.CHARACTER) | (1 << MParser.TEXT) | (1 << MParser.INTEGER) | (1 << MParser.DECIMAL) | (1 << MParser.DATE) | (1 << MParser.TIME) | (1 << MParser.DATETIME) | (1 << MParser.PERIOD))) != 0) or ((((_la - 132)) & ~0x3f) == 0 and ((1 << (_la - 132)) & ((1 << (MParser.READ - 132)) | (1 << (MParser.SELF - 132)) | (1 << (MParser.TEST - 132)) | (1 << (MParser.THIS - 132)) | (1 << (MParser.WRITE - 132)) | (1 << (MParser.BOOLEAN_LITERAL - 132)) | (1 << (MParser.CHAR_LITERAL - 132)) | (1 << (MParser.SYMBOL_IDENTIFIER - 132)) | (1 << (MParser.TYPE_IDENTIFIER - 132)) | (1 << (MParser.VARIABLE_IDENTIFIER - 132)) | (1 << (MParser.DOLLAR_IDENTIFIER - 132)) | (1 << (MParser.TEXT_LITERAL - 132)) | (1 << (MParser.INTEGER_LITERAL - 132)) | (1 << (MParser.DECIMAL_LITERAL - 132)))) != 0):
                self.state = 1944 
                localctx.args = self.javascript_arguments(0)


            self.state = 1947
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
            if isinstance( listener, MParserListener ):
                listener.enterJavascriptArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterJavascriptArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavascriptArgumentListItem(self)



    def javascript_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Javascript_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 322
        self.enterRecursionRule(localctx, 322, self.RULE_javascript_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.JavascriptArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1950 
            localctx.item = self.javascript_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1957
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,154,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.JavascriptArgumentListItemContext(self, MParser.Javascript_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_arguments)
                    self.state = 1952
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1953
                    self.match(MParser.COMMA)
                    self.state = 1954 
                    localctx.item = self.javascript_expression(0) 
                self.state = 1959
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,154,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterJavascript_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavascript_item_expression(self)




    def javascript_item_expression(self):

        localctx = MParser.Javascript_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 324, self.RULE_javascript_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1960
            self.match(MParser.LBRAK)
            self.state = 1961 
            localctx.exp = self.javascript_expression(0)
            self.state = 1962
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
            if isinstance( listener, MParserListener ):
                listener.enterJavascript_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavascript_parenthesis_expression(self)




    def javascript_parenthesis_expression(self):

        localctx = MParser.Javascript_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 326, self.RULE_javascript_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1964
            self.match(MParser.LPAR)
            self.state = 1965 
            localctx.exp = self.javascript_expression(0)
            self.state = 1966
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
            if isinstance( listener, MParserListener ):
                listener.enterJavascript_identifier_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavascript_identifier_expression(self)




    def javascript_identifier_expression(self):

        localctx = MParser.Javascript_identifier_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 328, self.RULE_javascript_identifier_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1968 
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
            if isinstance( listener, MParserListener ):
                listener.enterJavascriptIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavascriptIntegerLiteral(self)


    class JavascriptBooleanLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_literal_expressionContext)
            super(MParser.JavascriptBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(MParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterJavascriptBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavascriptBooleanLiteral(self)


    class JavascriptCharacterLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_literal_expressionContext)
            super(MParser.JavascriptCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(MParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterJavascriptCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavascriptCharacterLiteral(self)


    class JavascriptTextLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_literal_expressionContext)
            super(MParser.JavascriptTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(MParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterJavascriptTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavascriptTextLiteral(self)


    class JavascriptDecimalLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Javascript_literal_expressionContext)
            super(MParser.JavascriptDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(MParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterJavascriptDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavascriptDecimalLiteral(self)



    def javascript_literal_expression(self):

        localctx = MParser.Javascript_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 330, self.RULE_javascript_literal_expression)
        try:
            self.state = 1975
            token = self._input.LA(1)
            if token in [MParser.INTEGER_LITERAL]:
                localctx = MParser.JavascriptIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1970
                localctx.t = self.match(MParser.INTEGER_LITERAL)

            elif token in [MParser.DECIMAL_LITERAL]:
                localctx = MParser.JavascriptDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1971
                localctx.t = self.match(MParser.DECIMAL_LITERAL)

            elif token in [MParser.TEXT_LITERAL]:
                localctx = MParser.JavascriptTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1972
                localctx.t = self.match(MParser.TEXT_LITERAL)

            elif token in [MParser.BOOLEAN_LITERAL]:
                localctx = MParser.JavascriptBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1973
                localctx.t = self.match(MParser.BOOLEAN_LITERAL)

            elif token in [MParser.CHAR_LITERAL]:
                localctx = MParser.JavascriptCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1974
                localctx.t = self.match(MParser.CHAR_LITERAL)

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

        def READ(self):
            return self.getToken(MParser.READ, 0)

        def WRITE(self):
            return self.getToken(MParser.WRITE, 0)

        def TEST(self):
            return self.getToken(MParser.TEST, 0)

        def getRuleIndex(self):
            return MParser.RULE_javascript_identifier

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterJavascript_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavascript_identifier(self)




    def javascript_identifier(self):

        localctx = MParser.Javascript_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 332, self.RULE_javascript_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1977
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.BOOLEAN) | (1 << MParser.CHARACTER) | (1 << MParser.TEXT) | (1 << MParser.INTEGER) | (1 << MParser.DECIMAL) | (1 << MParser.DATE) | (1 << MParser.TIME) | (1 << MParser.DATETIME) | (1 << MParser.PERIOD))) != 0) or ((((_la - 132)) & ~0x3f) == 0 and ((1 << (_la - 132)) & ((1 << (MParser.READ - 132)) | (1 << (MParser.TEST - 132)) | (1 << (MParser.WRITE - 132)) | (1 << (MParser.SYMBOL_IDENTIFIER - 132)) | (1 << (MParser.TYPE_IDENTIFIER - 132)) | (1 << (MParser.VARIABLE_IDENTIFIER - 132)) | (1 << (MParser.DOLLAR_IDENTIFIER - 132)))) != 0)):
                self._errHandler.recoverInline(self)
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
            if isinstance( listener, MParserListener ):
                listener.enterPythonStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterPythonReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPythonReturnStatement(self)



    def python_statement(self):

        localctx = MParser.Python_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 334, self.RULE_python_statement)
        try:
            self.state = 1982
            token = self._input.LA(1)
            if token in [MParser.RETURN]:
                localctx = MParser.PythonReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1979
                self.match(MParser.RETURN)
                self.state = 1980 
                localctx.exp = self.python_expression(0)

            elif token in [MParser.LPAR, MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.READ, MParser.SELF, MParser.TEST, MParser.THIS, MParser.WRITE, MParser.BOOLEAN_LITERAL, MParser.CHAR_LITERAL, MParser.SYMBOL_IDENTIFIER, MParser.TYPE_IDENTIFIER, MParser.VARIABLE_IDENTIFIER, MParser.DOLLAR_IDENTIFIER, MParser.TEXT_LITERAL, MParser.INTEGER_LITERAL, MParser.DECIMAL_LITERAL]:
                localctx = MParser.PythonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1981 
                localctx.exp = self.python_expression(0)

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
            if isinstance( listener, MParserListener ):
                listener.enterPythonSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPythonSelectorExpression(self)


    class PythonPrimaryExpressionContext(Python_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_expressionContext)
            super(MParser.PythonPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Python_primary_expressionContext
            self.copyFrom(ctx)

        def python_primary_expression(self):
            return self.getTypedRuleContext(MParser.Python_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterPythonPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPythonPrimaryExpression(self)



    def python_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Python_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 336
        self.enterRecursionRule(localctx, 336, self.RULE_python_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.PythonPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1985 
            localctx.exp = self.python_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1991
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,157,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.PythonSelectorExpressionContext(self, MParser.Python_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_expression)
                    self.state = 1987
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1988 
                    localctx.child = self.python_selector_expression() 
                self.state = 1993
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,157,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterPythonParenthesisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPythonParenthesisExpression(self)


    class PythonIdentifierExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_primary_expressionContext)
            super(MParser.PythonIdentifierExpressionContext, self).__init__(parser)
            self.exp = None # Python_identifier_expressionContext
            self.copyFrom(ctx)

        def python_identifier_expression(self):
            return self.getTypedRuleContext(MParser.Python_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterPythonIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPythonIdentifierExpression(self)


    class PythonLiteralExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_primary_expressionContext)
            super(MParser.PythonLiteralExpressionContext, self).__init__(parser)
            self.exp = None # Python_literal_expressionContext
            self.copyFrom(ctx)

        def python_literal_expression(self):
            return self.getTypedRuleContext(MParser.Python_literal_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterPythonLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPythonLiteralExpression(self)


    class PythonGlobalMethodExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_primary_expressionContext)
            super(MParser.PythonGlobalMethodExpressionContext, self).__init__(parser)
            self.exp = None # Python_method_expressionContext
            self.copyFrom(ctx)

        def python_method_expression(self):
            return self.getTypedRuleContext(MParser.Python_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterPythonGlobalMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPythonGlobalMethodExpression(self)



    def python_primary_expression(self):

        localctx = MParser.Python_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 338, self.RULE_python_primary_expression)
        try:
            self.state = 1998
            la_ = self._interp.adaptivePredict(self._input,158,self._ctx)
            if la_ == 1:
                localctx = MParser.PythonParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1994 
                localctx.exp = self.python_parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = MParser.PythonIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1995 
                localctx.exp = self.python_identifier_expression(0)
                pass

            elif la_ == 3:
                localctx = MParser.PythonLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1996 
                localctx.exp = self.python_literal_expression()
                pass

            elif la_ == 4:
                localctx = MParser.PythonGlobalMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1997 
                localctx.exp = self.python_method_expression()
                pass


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
            if isinstance( listener, MParserListener ):
                listener.enterPythonMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterPythonItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPythonItemExpression(self)



    def python_selector_expression(self):

        localctx = MParser.Python_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 340, self.RULE_python_selector_expression)
        try:
            self.state = 2006
            token = self._input.LA(1)
            if token in [MParser.DOT]:
                localctx = MParser.PythonMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2000
                self.match(MParser.DOT)
                self.state = 2001 
                localctx.exp = self.python_method_expression()

            elif token in [MParser.LBRAK]:
                localctx = MParser.PythonItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2002
                self.match(MParser.LBRAK)
                self.state = 2003 
                localctx.exp = self.python_expression(0)
                self.state = 2004
                self.match(MParser.RBRAK)

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
            if isinstance( listener, MParserListener ):
                listener.enterPython_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPython_method_expression(self)




    def python_method_expression(self):

        localctx = MParser.Python_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 342, self.RULE_python_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2008 
            localctx.name = self.python_identifier()
            self.state = 2009
            self.match(MParser.LPAR)
            self.state = 2011
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.BOOLEAN) | (1 << MParser.CHARACTER) | (1 << MParser.TEXT) | (1 << MParser.INTEGER) | (1 << MParser.DECIMAL) | (1 << MParser.DATE) | (1 << MParser.TIME) | (1 << MParser.DATETIME) | (1 << MParser.PERIOD))) != 0) or ((((_la - 132)) & ~0x3f) == 0 and ((1 << (_la - 132)) & ((1 << (MParser.READ - 132)) | (1 << (MParser.SELF - 132)) | (1 << (MParser.TEST - 132)) | (1 << (MParser.THIS - 132)) | (1 << (MParser.WRITE - 132)) | (1 << (MParser.BOOLEAN_LITERAL - 132)) | (1 << (MParser.CHAR_LITERAL - 132)) | (1 << (MParser.SYMBOL_IDENTIFIER - 132)) | (1 << (MParser.TYPE_IDENTIFIER - 132)) | (1 << (MParser.VARIABLE_IDENTIFIER - 132)) | (1 << (MParser.DOLLAR_IDENTIFIER - 132)) | (1 << (MParser.TEXT_LITERAL - 132)) | (1 << (MParser.INTEGER_LITERAL - 132)) | (1 << (MParser.DECIMAL_LITERAL - 132)))) != 0):
                self.state = 2010 
                localctx.args = self.python_argument_list()


            self.state = 2013
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
            if isinstance( listener, MParserListener ):
                listener.enterPythonOrdinalOnlyArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPythonOrdinalOnlyArgumentList(self)


    class PythonNamedOnlyArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_argument_listContext)
            super(MParser.PythonNamedOnlyArgumentListContext, self).__init__(parser)
            self.named = None # Python_named_argument_listContext
            self.copyFrom(ctx)

        def python_named_argument_list(self):
            return self.getTypedRuleContext(MParser.Python_named_argument_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterPythonNamedOnlyArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterPythonArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPythonArgumentList(self)



    def python_argument_list(self):

        localctx = MParser.Python_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 344, self.RULE_python_argument_list)
        try:
            self.state = 2021
            la_ = self._interp.adaptivePredict(self._input,161,self._ctx)
            if la_ == 1:
                localctx = MParser.PythonOrdinalOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2015 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                pass

            elif la_ == 2:
                localctx = MParser.PythonNamedOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2016 
                localctx.named = self.python_named_argument_list(0)
                pass

            elif la_ == 3:
                localctx = MParser.PythonArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2017 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                self.state = 2018
                self.match(MParser.COMMA)
                self.state = 2019 
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
            if isinstance( listener, MParserListener ):
                listener.enterPythonOrdinalArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterPythonOrdinalArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPythonOrdinalArgumentListItem(self)



    def python_ordinal_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Python_ordinal_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 346
        self.enterRecursionRule(localctx, 346, self.RULE_python_ordinal_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.PythonOrdinalArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2024 
            localctx.item = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2031
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,162,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.PythonOrdinalArgumentListItemContext(self, MParser.Python_ordinal_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_ordinal_argument_list)
                    self.state = 2026
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2027
                    self.match(MParser.COMMA)
                    self.state = 2028 
                    localctx.item = self.python_expression(0) 
                self.state = 2033
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,162,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterPythonNamedArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterPythonNamedArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPythonNamedArgumentListItem(self)



    def python_named_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Python_named_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 348
        self.enterRecursionRule(localctx, 348, self.RULE_python_named_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.PythonNamedArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2035 
            localctx.name = self.python_identifier()
            self.state = 2036
            self.match(MParser.EQ)
            self.state = 2037 
            localctx.exp = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2047
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,163,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.PythonNamedArgumentListItemContext(self, MParser.Python_named_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_named_argument_list)
                    self.state = 2039
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2040
                    self.match(MParser.COMMA)
                    self.state = 2041 
                    localctx.name = self.python_identifier()
                    self.state = 2042
                    self.match(MParser.EQ)
                    self.state = 2043 
                    localctx.exp = self.python_expression(0) 
                self.state = 2049
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,163,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterPython_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPython_parenthesis_expression(self)




    def python_parenthesis_expression(self):

        localctx = MParser.Python_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 350, self.RULE_python_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2050
            self.match(MParser.LPAR)
            self.state = 2051 
            localctx.exp = self.python_expression(0)
            self.state = 2052
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
            if isinstance( listener, MParserListener ):
                listener.enterPythonChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPythonChildIdentifier(self)


    class PythonPromptoIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_identifier_expressionContext)
            super(MParser.PythonPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(MParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterPythonPromptoIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPythonPromptoIdentifier(self)


    class PythonIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_identifier_expressionContext)
            super(MParser.PythonIdentifierContext, self).__init__(parser)
            self.name = None # Python_identifierContext
            self.copyFrom(ctx)

        def python_identifier(self):
            return self.getTypedRuleContext(MParser.Python_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterPythonIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPythonIdentifier(self)



    def python_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Python_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 352
        self.enterRecursionRule(localctx, 352, self.RULE_python_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2057
            token = self._input.LA(1)
            if token in [MParser.DOLLAR_IDENTIFIER]:
                localctx = MParser.PythonPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2055
                self.match(MParser.DOLLAR_IDENTIFIER)

            elif token in [MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.READ, MParser.SELF, MParser.TEST, MParser.THIS, MParser.WRITE, MParser.SYMBOL_IDENTIFIER, MParser.TYPE_IDENTIFIER, MParser.VARIABLE_IDENTIFIER]:
                localctx = MParser.PythonIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2056 
                localctx.name = self.python_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2064
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,165,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.PythonChildIdentifierContext(self, MParser.Python_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_identifier_expression)
                    self.state = 2059
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2060
                    self.match(MParser.DOT)
                    self.state = 2061 
                    localctx.name = self.python_identifier() 
                self.state = 2066
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,165,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterPythonIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPythonIntegerLiteral(self)


    class PythonBooleanLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_literal_expressionContext)
            super(MParser.PythonBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(MParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterPythonBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPythonBooleanLiteral(self)


    class PythonCharacterLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_literal_expressionContext)
            super(MParser.PythonCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(MParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterPythonCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPythonCharacterLiteral(self)


    class PythonTextLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_literal_expressionContext)
            super(MParser.PythonTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(MParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterPythonTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPythonTextLiteral(self)


    class PythonDecimalLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Python_literal_expressionContext)
            super(MParser.PythonDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(MParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterPythonDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPythonDecimalLiteral(self)



    def python_literal_expression(self):

        localctx = MParser.Python_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 354, self.RULE_python_literal_expression)
        try:
            self.state = 2072
            token = self._input.LA(1)
            if token in [MParser.INTEGER_LITERAL]:
                localctx = MParser.PythonIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2067
                localctx.t = self.match(MParser.INTEGER_LITERAL)

            elif token in [MParser.DECIMAL_LITERAL]:
                localctx = MParser.PythonDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2068
                localctx.t = self.match(MParser.DECIMAL_LITERAL)

            elif token in [MParser.TEXT_LITERAL]:
                localctx = MParser.PythonTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2069
                localctx.t = self.match(MParser.TEXT_LITERAL)

            elif token in [MParser.BOOLEAN_LITERAL]:
                localctx = MParser.PythonBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2070
                localctx.t = self.match(MParser.BOOLEAN_LITERAL)

            elif token in [MParser.CHAR_LITERAL]:
                localctx = MParser.PythonCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2071
                localctx.t = self.match(MParser.CHAR_LITERAL)

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

        def READ(self):
            return self.getToken(MParser.READ, 0)

        def WRITE(self):
            return self.getToken(MParser.WRITE, 0)

        def TEST(self):
            return self.getToken(MParser.TEST, 0)

        def SELF(self):
            return self.getToken(MParser.SELF, 0)

        def THIS(self):
            return self.getToken(MParser.THIS, 0)

        def getRuleIndex(self):
            return MParser.RULE_python_identifier

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterPython_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitPython_identifier(self)




    def python_identifier(self):

        localctx = MParser.Python_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 356, self.RULE_python_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2074
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.BOOLEAN) | (1 << MParser.CHARACTER) | (1 << MParser.TEXT) | (1 << MParser.INTEGER) | (1 << MParser.DECIMAL) | (1 << MParser.DATE) | (1 << MParser.TIME) | (1 << MParser.DATETIME) | (1 << MParser.PERIOD))) != 0) or ((((_la - 132)) & ~0x3f) == 0 and ((1 << (_la - 132)) & ((1 << (MParser.READ - 132)) | (1 << (MParser.SELF - 132)) | (1 << (MParser.TEST - 132)) | (1 << (MParser.THIS - 132)) | (1 << (MParser.WRITE - 132)) | (1 << (MParser.SYMBOL_IDENTIFIER - 132)) | (1 << (MParser.TYPE_IDENTIFIER - 132)) | (1 << (MParser.VARIABLE_IDENTIFIER - 132)))) != 0)):
                self._errHandler.recoverInline(self)
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
            if isinstance( listener, MParserListener ):
                listener.enterJavaReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterJavaStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavaStatement(self)



    def java_statement(self):

        localctx = MParser.Java_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 358, self.RULE_java_statement)
        try:
            self.state = 2083
            token = self._input.LA(1)
            if token in [MParser.RETURN]:
                localctx = MParser.JavaReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2076
                self.match(MParser.RETURN)
                self.state = 2077 
                localctx.exp = self.java_expression(0)
                self.state = 2078
                self.match(MParser.SEMI)

            elif token in [MParser.LPAR, MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.READ, MParser.SELF, MParser.TEST, MParser.THIS, MParser.WRITE, MParser.BOOLEAN_LITERAL, MParser.CHAR_LITERAL, MParser.SYMBOL_IDENTIFIER, MParser.TYPE_IDENTIFIER, MParser.VARIABLE_IDENTIFIER, MParser.NATIVE_IDENTIFIER, MParser.DOLLAR_IDENTIFIER, MParser.TEXT_LITERAL, MParser.INTEGER_LITERAL, MParser.DECIMAL_LITERAL]:
                localctx = MParser.JavaStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2080 
                localctx.exp = self.java_expression(0)
                self.state = 2081
                self.match(MParser.SEMI)

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
            if isinstance( listener, MParserListener ):
                listener.enterJavaSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavaSelectorExpression(self)


    class JavaPrimaryExpressionContext(Java_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_expressionContext)
            super(MParser.JavaPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Java_primary_expressionContext
            self.copyFrom(ctx)

        def java_primary_expression(self):
            return self.getTypedRuleContext(MParser.Java_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterJavaPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavaPrimaryExpression(self)



    def java_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Java_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 360
        self.enterRecursionRule(localctx, 360, self.RULE_java_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.JavaPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2086 
            localctx.exp = self.java_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2092
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,168,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.JavaSelectorExpressionContext(self, MParser.Java_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_expression)
                    self.state = 2088
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2089 
                    localctx.child = self.java_selector_expression() 
                self.state = 2094
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,168,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterJava_primary_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJava_primary_expression(self)




    def java_primary_expression(self):

        localctx = MParser.Java_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 362, self.RULE_java_primary_expression)
        try:
            self.state = 2100
            la_ = self._interp.adaptivePredict(self._input,169,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2095 
                self.java_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2096 
                self.java_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2097 
                self.java_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2098 
                self.java_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2099 
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
            if isinstance( listener, MParserListener ):
                listener.enterJava_this_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJava_this_expression(self)




    def java_this_expression(self):

        localctx = MParser.Java_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 364, self.RULE_java_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2102 
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
            if isinstance( listener, MParserListener ):
                listener.enterJava_new_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJava_new_expression(self)




    def java_new_expression(self):

        localctx = MParser.Java_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 366, self.RULE_java_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2104 
            self.new_token()
            self.state = 2105 
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
            if isinstance( listener, MParserListener ):
                listener.enterJavaItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterJavaMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavaMethodExpression(self)



    def java_selector_expression(self):

        localctx = MParser.Java_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 368, self.RULE_java_selector_expression)
        try:
            self.state = 2110
            token = self._input.LA(1)
            if token in [MParser.DOT]:
                localctx = MParser.JavaMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2107
                self.match(MParser.DOT)
                self.state = 2108 
                localctx.exp = self.java_method_expression()

            elif token in [MParser.LBRAK]:
                localctx = MParser.JavaItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2109 
                localctx.exp = self.java_item_expression()

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
            if isinstance( listener, MParserListener ):
                listener.enterJava_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJava_method_expression(self)




    def java_method_expression(self):

        localctx = MParser.Java_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 370, self.RULE_java_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2112 
            localctx.name = self.java_identifier()
            self.state = 2113
            self.match(MParser.LPAR)
            self.state = 2115
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.BOOLEAN) | (1 << MParser.CHARACTER) | (1 << MParser.TEXT) | (1 << MParser.INTEGER) | (1 << MParser.DECIMAL) | (1 << MParser.DATE) | (1 << MParser.TIME) | (1 << MParser.DATETIME) | (1 << MParser.PERIOD))) != 0) or ((((_la - 132)) & ~0x3f) == 0 and ((1 << (_la - 132)) & ((1 << (MParser.READ - 132)) | (1 << (MParser.SELF - 132)) | (1 << (MParser.TEST - 132)) | (1 << (MParser.THIS - 132)) | (1 << (MParser.WRITE - 132)) | (1 << (MParser.BOOLEAN_LITERAL - 132)) | (1 << (MParser.CHAR_LITERAL - 132)) | (1 << (MParser.SYMBOL_IDENTIFIER - 132)) | (1 << (MParser.TYPE_IDENTIFIER - 132)) | (1 << (MParser.VARIABLE_IDENTIFIER - 132)) | (1 << (MParser.NATIVE_IDENTIFIER - 132)) | (1 << (MParser.DOLLAR_IDENTIFIER - 132)) | (1 << (MParser.TEXT_LITERAL - 132)) | (1 << (MParser.INTEGER_LITERAL - 132)) | (1 << (MParser.DECIMAL_LITERAL - 132)))) != 0):
                self.state = 2114 
                localctx.args = self.java_arguments(0)


            self.state = 2117
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
            if isinstance( listener, MParserListener ):
                listener.enterJavaArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavaArgumentListItem(self)


    class JavaArgumentListContext(Java_argumentsContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_argumentsContext)
            super(MParser.JavaArgumentListContext, self).__init__(parser)
            self.item = None # Java_expressionContext
            self.copyFrom(ctx)

        def java_expression(self):
            return self.getTypedRuleContext(MParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterJavaArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavaArgumentList(self)



    def java_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Java_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 372
        self.enterRecursionRule(localctx, 372, self.RULE_java_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.JavaArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2120 
            localctx.item = self.java_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2127
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,172,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.JavaArgumentListItemContext(self, MParser.Java_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_arguments)
                    self.state = 2122
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2123
                    self.match(MParser.COMMA)
                    self.state = 2124 
                    localctx.item = self.java_expression(0) 
                self.state = 2129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,172,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterJava_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJava_item_expression(self)




    def java_item_expression(self):

        localctx = MParser.Java_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 374, self.RULE_java_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2130
            self.match(MParser.LBRAK)
            self.state = 2131 
            localctx.exp = self.java_expression(0)
            self.state = 2132
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
            if isinstance( listener, MParserListener ):
                listener.enterJava_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJava_parenthesis_expression(self)




    def java_parenthesis_expression(self):

        localctx = MParser.Java_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 376, self.RULE_java_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2134
            self.match(MParser.LPAR)
            self.state = 2135 
            localctx.exp = self.java_expression(0)
            self.state = 2136
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
            if isinstance( listener, MParserListener ):
                listener.enterJavaIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterJavaChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavaChildIdentifier(self)



    def java_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Java_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 378
        self.enterRecursionRule(localctx, 378, self.RULE_java_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.JavaIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2139 
            localctx.name = self.java_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2146
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,173,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.JavaChildIdentifierContext(self, MParser.Java_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_identifier_expression)
                    self.state = 2141
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2142
                    self.match(MParser.DOT)
                    self.state = 2143 
                    localctx.name = self.java_identifier() 
                self.state = 2148
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,173,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterJavaClassIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterJavaChildClassIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavaChildClassIdentifier(self)



    def java_class_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Java_class_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 380
        self.enterRecursionRule(localctx, 380, self.RULE_java_class_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.JavaClassIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2150 
            localctx.klass = self.java_identifier_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2156
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,174,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.JavaChildClassIdentifierContext(self, MParser.Java_class_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_class_identifier_expression)
                    self.state = 2152
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2153
                    localctx.name = self.match(MParser.DOLLAR_IDENTIFIER) 
                self.state = 2158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,174,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterJavaBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavaBooleanLiteral(self)


    class JavaCharacterLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_literal_expressionContext)
            super(MParser.JavaCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(MParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterJavaCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavaCharacterLiteral(self)


    class JavaIntegerLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_literal_expressionContext)
            super(MParser.JavaIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(MParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterJavaIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavaIntegerLiteral(self)


    class JavaTextLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_literal_expressionContext)
            super(MParser.JavaTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(MParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterJavaTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavaTextLiteral(self)


    class JavaDecimalLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Java_literal_expressionContext)
            super(MParser.JavaDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(MParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterJavaDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJavaDecimalLiteral(self)



    def java_literal_expression(self):

        localctx = MParser.Java_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 382, self.RULE_java_literal_expression)
        try:
            self.state = 2164
            token = self._input.LA(1)
            if token in [MParser.INTEGER_LITERAL]:
                localctx = MParser.JavaIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2159
                localctx.t = self.match(MParser.INTEGER_LITERAL)

            elif token in [MParser.DECIMAL_LITERAL]:
                localctx = MParser.JavaDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2160
                localctx.t = self.match(MParser.DECIMAL_LITERAL)

            elif token in [MParser.TEXT_LITERAL]:
                localctx = MParser.JavaTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2161
                localctx.t = self.match(MParser.TEXT_LITERAL)

            elif token in [MParser.BOOLEAN_LITERAL]:
                localctx = MParser.JavaBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2162
                localctx.t = self.match(MParser.BOOLEAN_LITERAL)

            elif token in [MParser.CHAR_LITERAL]:
                localctx = MParser.JavaCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2163
                localctx.t = self.match(MParser.CHAR_LITERAL)

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

        def READ(self):
            return self.getToken(MParser.READ, 0)

        def WRITE(self):
            return self.getToken(MParser.WRITE, 0)

        def TEST(self):
            return self.getToken(MParser.TEST, 0)

        def getRuleIndex(self):
            return MParser.RULE_java_identifier

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterJava_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitJava_identifier(self)




    def java_identifier(self):

        localctx = MParser.Java_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 384, self.RULE_java_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2166
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.BOOLEAN) | (1 << MParser.CHARACTER) | (1 << MParser.TEXT) | (1 << MParser.INTEGER) | (1 << MParser.DECIMAL) | (1 << MParser.DATE) | (1 << MParser.TIME) | (1 << MParser.DATETIME) | (1 << MParser.PERIOD))) != 0) or ((((_la - 132)) & ~0x3f) == 0 and ((1 << (_la - 132)) & ((1 << (MParser.READ - 132)) | (1 << (MParser.TEST - 132)) | (1 << (MParser.WRITE - 132)) | (1 << (MParser.SYMBOL_IDENTIFIER - 132)) | (1 << (MParser.TYPE_IDENTIFIER - 132)) | (1 << (MParser.VARIABLE_IDENTIFIER - 132)) | (1 << (MParser.NATIVE_IDENTIFIER - 132)) | (1 << (MParser.DOLLAR_IDENTIFIER - 132)))) != 0)):
                self._errHandler.recoverInline(self)
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
            if isinstance( listener, MParserListener ):
                listener.enterCSharpReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterCSharpStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCSharpStatement(self)



    def csharp_statement(self):

        localctx = MParser.Csharp_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 386, self.RULE_csharp_statement)
        try:
            self.state = 2175
            token = self._input.LA(1)
            if token in [MParser.RETURN]:
                localctx = MParser.CSharpReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2168
                self.match(MParser.RETURN)
                self.state = 2169 
                localctx.exp = self.csharp_expression(0)
                self.state = 2170
                self.match(MParser.SEMI)

            elif token in [MParser.LPAR, MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.READ, MParser.SELF, MParser.TEST, MParser.THIS, MParser.WRITE, MParser.BOOLEAN_LITERAL, MParser.CHAR_LITERAL, MParser.SYMBOL_IDENTIFIER, MParser.TYPE_IDENTIFIER, MParser.VARIABLE_IDENTIFIER, MParser.DOLLAR_IDENTIFIER, MParser.TEXT_LITERAL, MParser.INTEGER_LITERAL, MParser.DECIMAL_LITERAL]:
                localctx = MParser.CSharpStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2172 
                localctx.exp = self.csharp_expression(0)
                self.state = 2173
                self.match(MParser.SEMI)

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
            if isinstance( listener, MParserListener ):
                listener.enterCSharpSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCSharpSelectorExpression(self)


    class CSharpPrimaryExpressionContext(Csharp_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_expressionContext)
            super(MParser.CSharpPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_primary_expressionContext
            self.copyFrom(ctx)

        def csharp_primary_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterCSharpPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCSharpPrimaryExpression(self)



    def csharp_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Csharp_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 388
        self.enterRecursionRule(localctx, 388, self.RULE_csharp_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.CSharpPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2178 
            localctx.exp = self.csharp_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2184
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,177,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.CSharpSelectorExpressionContext(self, MParser.Csharp_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_expression)
                    self.state = 2180
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2181 
                    localctx.child = self.csharp_selector_expression() 
                self.state = 2186
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,177,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterCsharp_primary_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCsharp_primary_expression(self)




    def csharp_primary_expression(self):

        localctx = MParser.Csharp_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 390, self.RULE_csharp_primary_expression)
        try:
            self.state = 2192
            la_ = self._interp.adaptivePredict(self._input,178,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2187 
                self.csharp_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2188 
                self.csharp_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2189 
                self.csharp_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2190 
                self.csharp_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2191 
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
            if isinstance( listener, MParserListener ):
                listener.enterCsharp_this_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCsharp_this_expression(self)




    def csharp_this_expression(self):

        localctx = MParser.Csharp_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 392, self.RULE_csharp_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2194 
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
            if isinstance( listener, MParserListener ):
                listener.enterCsharp_new_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCsharp_new_expression(self)




    def csharp_new_expression(self):

        localctx = MParser.Csharp_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 394, self.RULE_csharp_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2196 
            self.new_token()
            self.state = 2197 
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
            if isinstance( listener, MParserListener ):
                listener.enterCSharpMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCSharpMethodExpression(self)


    class CSharpItemExpressionContext(Csharp_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_selector_expressionContext)
            super(MParser.CSharpItemExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_item_expressionContext
            self.copyFrom(ctx)

        def csharp_item_expression(self):
            return self.getTypedRuleContext(MParser.Csharp_item_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterCSharpItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCSharpItemExpression(self)



    def csharp_selector_expression(self):

        localctx = MParser.Csharp_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 396, self.RULE_csharp_selector_expression)
        try:
            self.state = 2202
            token = self._input.LA(1)
            if token in [MParser.DOT]:
                localctx = MParser.CSharpMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2199
                self.match(MParser.DOT)
                self.state = 2200 
                localctx.exp = self.csharp_method_expression()

            elif token in [MParser.LBRAK]:
                localctx = MParser.CSharpItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2201 
                localctx.exp = self.csharp_item_expression()

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
            if isinstance( listener, MParserListener ):
                listener.enterCsharp_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCsharp_method_expression(self)




    def csharp_method_expression(self):

        localctx = MParser.Csharp_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 398, self.RULE_csharp_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2204 
            localctx.name = self.csharp_identifier()
            self.state = 2205
            self.match(MParser.LPAR)
            self.state = 2207
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.LPAR) | (1 << MParser.BOOLEAN) | (1 << MParser.CHARACTER) | (1 << MParser.TEXT) | (1 << MParser.INTEGER) | (1 << MParser.DECIMAL) | (1 << MParser.DATE) | (1 << MParser.TIME) | (1 << MParser.DATETIME) | (1 << MParser.PERIOD))) != 0) or ((((_la - 132)) & ~0x3f) == 0 and ((1 << (_la - 132)) & ((1 << (MParser.READ - 132)) | (1 << (MParser.SELF - 132)) | (1 << (MParser.TEST - 132)) | (1 << (MParser.THIS - 132)) | (1 << (MParser.WRITE - 132)) | (1 << (MParser.BOOLEAN_LITERAL - 132)) | (1 << (MParser.CHAR_LITERAL - 132)) | (1 << (MParser.SYMBOL_IDENTIFIER - 132)) | (1 << (MParser.TYPE_IDENTIFIER - 132)) | (1 << (MParser.VARIABLE_IDENTIFIER - 132)) | (1 << (MParser.DOLLAR_IDENTIFIER - 132)) | (1 << (MParser.TEXT_LITERAL - 132)) | (1 << (MParser.INTEGER_LITERAL - 132)) | (1 << (MParser.DECIMAL_LITERAL - 132)))) != 0):
                self.state = 2206 
                localctx.args = self.csharp_arguments(0)


            self.state = 2209
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
            if isinstance( listener, MParserListener ):
                listener.enterCSharpArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterCSharpArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCSharpArgumentListItem(self)



    def csharp_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Csharp_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 400
        self.enterRecursionRule(localctx, 400, self.RULE_csharp_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MParser.CSharpArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2212 
            localctx.item = self.csharp_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2219
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,181,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.CSharpArgumentListItemContext(self, MParser.Csharp_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_arguments)
                    self.state = 2214
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2215
                    self.match(MParser.COMMA)
                    self.state = 2216 
                    localctx.item = self.csharp_expression(0) 
                self.state = 2221
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,181,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterCsharp_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCsharp_item_expression(self)




    def csharp_item_expression(self):

        localctx = MParser.Csharp_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 402, self.RULE_csharp_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2222
            self.match(MParser.LBRAK)
            self.state = 2223 
            localctx.exp = self.csharp_expression(0)
            self.state = 2224
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
            if isinstance( listener, MParserListener ):
                listener.enterCsharp_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCsharp_parenthesis_expression(self)




    def csharp_parenthesis_expression(self):

        localctx = MParser.Csharp_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 404, self.RULE_csharp_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2226
            self.match(MParser.LPAR)
            self.state = 2227 
            localctx.exp = self.csharp_expression(0)
            self.state = 2228
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
            if isinstance( listener, MParserListener ):
                listener.enterCSharpIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
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
            if isinstance( listener, MParserListener ):
                listener.enterCSharpChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCSharpChildIdentifier(self)


    class CSharpPromptoIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_identifier_expressionContext)
            super(MParser.CSharpPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(MParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterCSharpPromptoIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCSharpPromptoIdentifier(self)



    def csharp_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.Csharp_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 406
        self.enterRecursionRule(localctx, 406, self.RULE_csharp_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2233
            token = self._input.LA(1)
            if token in [MParser.DOLLAR_IDENTIFIER]:
                localctx = MParser.CSharpPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2231
                self.match(MParser.DOLLAR_IDENTIFIER)

            elif token in [MParser.BOOLEAN, MParser.CHARACTER, MParser.TEXT, MParser.INTEGER, MParser.DECIMAL, MParser.DATE, MParser.TIME, MParser.DATETIME, MParser.PERIOD, MParser.READ, MParser.TEST, MParser.WRITE, MParser.SYMBOL_IDENTIFIER, MParser.TYPE_IDENTIFIER, MParser.VARIABLE_IDENTIFIER]:
                localctx = MParser.CSharpIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2232 
                localctx.name = self.csharp_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2240
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,183,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.CSharpChildIdentifierContext(self, MParser.Csharp_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_identifier_expression)
                    self.state = 2235
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2236
                    self.match(MParser.DOT)
                    self.state = 2237 
                    localctx.name = self.csharp_identifier() 
                self.state = 2242
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,183,self._ctx)

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
            if isinstance( listener, MParserListener ):
                listener.enterCSharpBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCSharpBooleanLiteral(self)


    class CSharpIntegerLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_literal_expressionContext)
            super(MParser.CSharpIntegerLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(MParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterCSharpIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCSharpIntegerLiteral(self)


    class CSharpDecimalLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_literal_expressionContext)
            super(MParser.CSharpDecimalLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(MParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterCSharpDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCSharpDecimalLiteral(self)


    class CSharpCharacterLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_literal_expressionContext)
            super(MParser.CSharpCharacterLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(MParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterCSharpCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCSharpCharacterLiteral(self)


    class CSharpTextLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a MParser.Csharp_literal_expressionContext)
            super(MParser.CSharpTextLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(MParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterCSharpTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCSharpTextLiteral(self)



    def csharp_literal_expression(self):

        localctx = MParser.Csharp_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 408, self.RULE_csharp_literal_expression)
        try:
            self.state = 2248
            token = self._input.LA(1)
            if token in [MParser.INTEGER_LITERAL]:
                localctx = MParser.CSharpIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2243
                self.match(MParser.INTEGER_LITERAL)

            elif token in [MParser.DECIMAL_LITERAL]:
                localctx = MParser.CSharpDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2244
                self.match(MParser.DECIMAL_LITERAL)

            elif token in [MParser.TEXT_LITERAL]:
                localctx = MParser.CSharpTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2245
                self.match(MParser.TEXT_LITERAL)

            elif token in [MParser.BOOLEAN_LITERAL]:
                localctx = MParser.CSharpBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2246
                self.match(MParser.BOOLEAN_LITERAL)

            elif token in [MParser.CHAR_LITERAL]:
                localctx = MParser.CSharpCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2247
                self.match(MParser.CHAR_LITERAL)

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

        def READ(self):
            return self.getToken(MParser.READ, 0)

        def WRITE(self):
            return self.getToken(MParser.WRITE, 0)

        def TEST(self):
            return self.getToken(MParser.TEST, 0)

        def getRuleIndex(self):
            return MParser.RULE_csharp_identifier

        def enterRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.enterCsharp_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, MParserListener ):
                listener.exitCsharp_identifier(self)




    def csharp_identifier(self):

        localctx = MParser.Csharp_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 410, self.RULE_csharp_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2250
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MParser.BOOLEAN) | (1 << MParser.CHARACTER) | (1 << MParser.TEXT) | (1 << MParser.INTEGER) | (1 << MParser.DECIMAL) | (1 << MParser.DATE) | (1 << MParser.TIME) | (1 << MParser.DATETIME) | (1 << MParser.PERIOD))) != 0) or ((((_la - 132)) & ~0x3f) == 0 and ((1 << (_la - 132)) & ((1 << (MParser.READ - 132)) | (1 << (MParser.TEST - 132)) | (1 << (MParser.WRITE - 132)) | (1 << (MParser.SYMBOL_IDENTIFIER - 132)) | (1 << (MParser.TYPE_IDENTIFIER - 132)) | (1 << (MParser.VARIABLE_IDENTIFIER - 132)))) != 0)):
                self._errHandler.recoverInline(self)
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
        self._predicates[17] = self.native_category_binding_list_sempred
        self._predicates[29] = self.callable_parent_sempred
        self._predicates[39] = self.else_if_statement_list_sempred
        self._predicates[45] = self.expression_sempred
        self._predicates[47] = self.instance_expression_sempred
        self._predicates[49] = self.instance_selector_sempred
        self._predicates[53] = self.argument_assignment_list_sempred
        self._predicates[60] = self.child_instance_sempred
        self._predicates[80] = self.typedef_sempred
        self._predicates[100] = self.any_type_sempred
        self._predicates[137] = self.assignable_instance_sempred
        self._predicates[138] = self.is_expression_sempred
        self._predicates[144] = self.new_token_sempred
        self._predicates[145] = self.key_token_sempred
        self._predicates[146] = self.module_token_sempred
        self._predicates[147] = self.value_token_sempred
        self._predicates[148] = self.symbols_token_sempred
        self._predicates[155] = self.javascript_expression_sempred
        self._predicates[161] = self.javascript_arguments_sempred
        self._predicates[168] = self.python_expression_sempred
        self._predicates[173] = self.python_ordinal_argument_list_sempred
        self._predicates[174] = self.python_named_argument_list_sempred
        self._predicates[176] = self.python_identifier_expression_sempred
        self._predicates[180] = self.java_expression_sempred
        self._predicates[186] = self.java_arguments_sempred
        self._predicates[189] = self.java_identifier_expression_sempred
        self._predicates[190] = self.java_class_identifier_expression_sempred
        self._predicates[194] = self.csharp_expression_sempred
        self._predicates[200] = self.csharp_arguments_sempred
        self._predicates[203] = self.csharp_identifier_expression_sempred
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
                return self.precpred(self._ctx, 30)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 29)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 25)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 23:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 24:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 25:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 26:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 27:
                return self.precpred(self._ctx, 34)
         

            if predIndex == 28:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 29:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 30:
                return self.precpred(self._ctx, 13)
         

    def instance_expression_sempred(self, localctx, predIndex):
            if predIndex == 31:
                return self.precpred(self._ctx, 1)
         

    def instance_selector_sempred(self, localctx, predIndex):
            if predIndex == 32:
                return self.wasNot(MParser.WS)
         

            if predIndex == 33:
                return self.wasNot(MParser.WS)
         

            if predIndex == 34:
                return self.wasNot(MParser.WS)
         

    def argument_assignment_list_sempred(self, localctx, predIndex):
            if predIndex == 35:
                return self.willNotBe(self.equalToken())
         

            if predIndex == 36:
                return self.precpred(self._ctx, 1)
         

    def child_instance_sempred(self, localctx, predIndex):
            if predIndex == 37:
                return self.wasNot(MParser.WS)
         

            if predIndex == 38:
                return self.wasNot(MParser.WS)
         

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
         


