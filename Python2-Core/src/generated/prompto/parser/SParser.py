# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .SParserListener import SParserListener
else:
    from SParserListener import SParserListener
from .AbstractParser import AbstractParser

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\u00a9\u0880\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
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
        buf.write(u"\t\u00c4\4\u00c5\t\u00c5\4\u00c6\t\u00c6\3\2\3\2\3\2")
        buf.write(u"\3\2\3\2\3\2\5\2\u0193\n\2\3\2\5\2\u0196\n\2\3\2\3\2")
        buf.write(u"\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\5\5\u01af\n\5\3\5\3")
        buf.write(u"\5\3\6\5\6\u01b4\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write(u"\3\6\5\6\u01bf\n\6\3\6\3\6\3\7\5\7\u01c4\n\7\3\7\3\7")
        buf.write(u"\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u01cf\n\7\3\7\3\7\3")
        buf.write(u"\7\3\7\3\7\5\7\u01d6\n\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write(u"\3\b\3\b\3\b\3\b\5\b\u01e3\n\b\3\b\3\b\3\t\3\t\3\n\3")
        buf.write(u"\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u01f1\n\n\3\n\3\n\3\n")
        buf.write(u"\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write(u"\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\5\r")
        buf.write(u"\u020d\n\r\3\r\3\r\3\r\3\r\3\r\5\r\u0214\n\r\3\r\3\r")
        buf.write(u"\3\r\3\r\3\r\3\r\3\r\5\r\u021d\n\r\3\r\3\r\3\16\3\16")
        buf.write(u"\3\16\3\16\3\16\5\16\u0226\n\16\3\16\3\16\3\16\3\16\3")
        buf.write(u"\16\3\16\3\16\5\16\u022f\n\16\3\16\3\16\3\17\3\17\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3")
        buf.write(u"\20\3\20\7\20\u0242\n\20\f\20\16\20\u0245\13\20\3\21")
        buf.write(u"\3\21\3\22\3\22\3\22\3\22\3\22\5\22\u024e\n\22\3\22\3")
        buf.write(u"\22\3\22\5\22\u0253\n\22\3\23\3\23\3\23\3\23\5\23\u0259")
        buf.write(u"\n\23\3\23\3\23\3\23\5\23\u025e\n\23\3\23\3\23\3\23\3")
        buf.write(u"\23\3\23\3\24\3\24\3\24\3\24\3\24\5\24\u026a\n\24\3\24")
        buf.write(u"\3\24\3\24\5\24\u026f\n\24\3\24\3\24\3\24\3\24\3\24\3")
        buf.write(u"\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write(u"\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u0287\n\25\3\26\3")
        buf.write(u"\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0292\n\27")
        buf.write(u"\3\27\3\27\5\27\u0296\n\27\3\30\3\30\3\30\3\30\3\30\3")
        buf.write(u"\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write(u"\3\30\5\30\u02a9\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write(u"\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write(u"\3\31\3\31\3\31\5\31\u02bf\n\31\3\32\3\32\3\32\5\32\u02c4")
        buf.write(u"\n\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\5\33\u02cd\n")
        buf.write(u"\33\3\34\3\34\3\34\3\34\3\34\7\34\u02d4\n\34\f\34\16")
        buf.write(u"\34\u02d7\13\34\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u02df")
        buf.write(u"\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3")
        buf.write(u"\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(u" \3 \3 \3 \5 \u02fc\n \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!")
        buf.write(u"\3!\3!\3!\3!\3!\3!\3!\5!\u030f\n!\3\"\3\"\3\"\3\"\5\"")
        buf.write(u"\u0315\n\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3")
        buf.write(u"#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%")
        buf.write(u"\3%\3%\3%\5%\u0337\n%\3%\3%\3%\3%\3%\3%\3%\5%\u0340\n")
        buf.write(u"%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&")
        buf.write(u"\3&\3&\7&\u0355\n&\f&\16&\u0358\13&\3\'\3\'\3\'\3(\3")
        buf.write(u"(\3(\3(\3(\3(\3(\3(\5(\u0365\n(\3(\3(\3(\3(\3(\3(\3(")
        buf.write(u"\5(\u036e\n(\3(\3(\3(\3(\3(\3(\3(\5(\u0377\n(\3(\3(\3")
        buf.write(u")\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)")
        buf.write(u"\3)\5)\u038e\n)\3*\3*\5*\u0392\n*\3+\3+\3+\3+\3+\3+\3")
        buf.write(u"+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\5+\u03a6\n+\3+\3+")
        buf.write(u"\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write(u"+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+")
        buf.write(u"\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write(u"+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+")
        buf.write(u"\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write(u"+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\7+\u040c\n+\f+\16+\u040f")
        buf.write(u"\13+\3,\3,\3-\3-\3-\3-\3-\7-\u0418\n-\f-\16-\u041b\13")
        buf.write(u"-\3.\3.\3.\3.\3.\3.\5.\u0423\n.\3/\3/\3/\3/\3/\3/\3/")
        buf.write(u"\3/\3/\3/\3/\3/\3/\5/\u0432\n/\3\60\3\60\3\60\3\60\3")
        buf.write(u"\61\3\61\3\61\5\61\u043b\n\61\3\61\3\61\3\62\3\62\3\62")
        buf.write(u"\3\62\3\62\5\62\u0444\n\62\3\62\3\62\3\62\7\62\u0449")
        buf.write(u"\n\62\f\62\16\62\u044c\13\62\3\63\3\63\3\63\3\63\3\64")
        buf.write(u"\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3")
        buf.write(u"\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u0465\n\66")
        buf.write(u"\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u0470")
        buf.write(u"\n\66\3\66\3\66\5\66\u0474\n\66\3\66\3\66\3\66\5\66\u0479")
        buf.write(u"\n\66\3\66\3\66\3\66\5\66\u047e\n\66\5\66\u0480\n\66")
        buf.write(u"\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u048a\n")
        buf.write(u"\67\3\67\3\67\38\38\38\38\39\39\39\39\39\39\39\39\59")
        buf.write(u"\u049a\n9\3:\3:\3:\3:\3;\7;\u04a1\n;\f;\16;\u04a4\13")
        buf.write(u";\3<\6<\u04a7\n<\r<\16<\u04a8\3=\6=\u04ac\n=\r=\16=\u04ad")
        buf.write(u"\3=\3=\3>\7>\u04b3\n>\f>\16>\u04b6\13>\3>\3>\3?\3?\3")
        buf.write(u"@\5@\u04bd\n@\3@\3@\3@\3A\3A\3A\3A\3A\3A\3A\7A\u04c9")
        buf.write(u"\nA\fA\16A\u04cc\13A\3B\3B\3B\7B\u04d1\nB\fB\16B\u04d4")
        buf.write(u"\13B\3B\3B\3B\3B\3B\5B\u04db\nB\3C\3C\3D\3D\5D\u04e1")
        buf.write(u"\nD\3E\3E\3E\3E\3E\3E\3E\7E\u04ea\nE\fE\16E\u04ed\13")
        buf.write(u"E\3F\3F\3F\3F\3F\3F\3F\7F\u04f6\nF\fF\16F\u04f9\13F\3")
        buf.write(u"G\3G\3G\3G\3G\3G\7G\u0501\nG\fG\16G\u0504\13G\3H\3H\3")
        buf.write(u"H\3H\3H\3H\3H\3H\3H\3H\5H\u0510\nH\3I\3I\5I\u0514\nI")
        buf.write(u"\3I\3I\3J\3J\5J\u051a\nJ\3J\3J\3K\3K\3K\3K\3K\3K\7K\u0524")
        buf.write(u"\nK\fK\16K\u0527\13K\3L\3L\3L\3L\3L\3L\3M\3M\3M\3M\3")
        buf.write(u"M\3M\3M\3M\3M\3M\3M\7M\u053a\nM\fM\16M\u053d\13M\3N\3")
        buf.write(u"N\5N\u0541\nN\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O")
        buf.write(u"\3O\5O\u0551\nO\3P\3P\3Q\5Q\u0556\nQ\3Q\3Q\3R\3R\3S\3")
        buf.write(u"S\3S\5S\u055f\nS\3T\3T\3T\3T\3T\3T\7T\u0567\nT\fT\16")
        buf.write(u"T\u056a\13T\3U\3U\5U\u056e\nU\3V\3V\3V\5V\u0573\nV\3")
        buf.write(u"W\3W\3X\3X\3Y\3Y\3Z\3Z\3Z\3Z\3Z\3Z\7Z\u0581\nZ\fZ\16")
        buf.write(u"Z\u0584\13Z\3[\3[\5[\u0588\n[\3[\5[\u058b\n[\3\\\3\\")
        buf.write(u"\5\\\u058f\n\\\3]\3]\3]\5]\u0594\n]\3^\3^\3^\3_\3_\5")
        buf.write(u"_\u059b\n_\3`\3`\3`\3`\3`\3`\3`\3`\3`\7`\u05a6\n`\f`")
        buf.write(u"\16`\u05a9\13`\3a\3a\3a\3a\3a\3a\3a\7a\u05b2\na\fa\16")
        buf.write(u"a\u05b5\13a\3b\3b\3b\3b\3b\5b\u05bc\nb\3c\3c\3c\3c\3")
        buf.write(u"c\3c\3c\7c\u05c5\nc\fc\16c\u05c8\13c\3d\3d\5d\u05cc\n")
        buf.write(u"d\3e\3e\3e\3e\3e\3e\3e\3e\3e\3e\5e\u05d8\ne\3f\3f\5f")
        buf.write(u"\u05dc\nf\3g\3g\3g\3g\3g\3g\7g\u05e4\ng\fg\16g\u05e7")
        buf.write(u"\13g\3h\3h\3h\3i\3i\5i\u05ee\ni\3j\3j\3j\3j\5j\u05f4")
        buf.write(u"\nj\3j\3j\3j\7j\u05f9\nj\fj\16j\u05fc\13j\3j\3j\5j\u0600")
        buf.write(u"\nj\3k\3k\3k\3k\3k\3k\7k\u0608\nk\fk\16k\u060b\13k\3")
        buf.write(u"l\3l\3l\3l\5l\u0611\nl\3m\3m\3n\3n\3n\3n\3n\3n\3n\7n")
        buf.write(u"\u061c\nn\fn\16n\u061f\13n\3o\3o\3o\3o\3o\3o\3o\3o\3")
        buf.write(u"o\3o\5o\u062b\no\3p\3p\5p\u062f\np\3p\5p\u0632\np\3q")
        buf.write(u"\3q\5q\u0636\nq\3q\5q\u0639\nq\3r\3r\3r\3r\3r\3r\3r\7")
        buf.write(u"r\u0642\nr\fr\16r\u0645\13r\3s\3s\3s\3s\3s\3s\3s\7s\u064e")
        buf.write(u"\ns\fs\16s\u0651\13s\3t\3t\3t\3t\3t\3t\3t\7t\u065a\n")
        buf.write(u"t\ft\16t\u065d\13t\3u\3u\3u\3u\3u\3u\3u\7u\u0666\nu\f")
        buf.write(u"u\16u\u0669\13u\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\3")
        buf.write(u"v\3v\5v\u0679\nv\3w\3w\3w\3w\3w\3w\3w\3w\3w\3w\3w\3w")
        buf.write(u"\3w\5w\u0688\nw\3x\3x\3x\3x\3x\3x\7x\u0690\nx\fx\16x")
        buf.write(u"\u0693\13x\3y\3y\3y\3y\5y\u0699\ny\3z\3z\3{\3{\3{\3{")
        buf.write(u"\3|\3|\5|\u06a3\n|\3}\3}\3}\3}\3}\5}\u06aa\n}\3~\3~\5")
        buf.write(u"~\u06ae\n~\3~\3~\3\177\3\177\5\177\u06b4\n\177\3\177")
        buf.write(u"\3\177\3\u0080\3\u0080\3\u0080\3\u0080\3\u0080\3\u0080")
        buf.write(u"\7\u0080\u06be\n\u0080\f\u0080\16\u0080\u06c1\13\u0080")
        buf.write(u"\3\u0081\3\u0081\3\u0081\3\u0081\3\u0081\3\u0081\7\u0081")
        buf.write(u"\u06c9\n\u0081\f\u0081\16\u0081\u06cc\13\u0081\3\u0082")
        buf.write(u"\3\u0082\3\u0082\3\u0082\3\u0083\3\u0083\3\u0083\3\u0083")
        buf.write(u"\3\u0083\3\u0083\3\u0083\3\u0083\3\u0083\5\u0083\u06db")
        buf.write(u"\n\u0083\3\u0084\3\u0084\3\u0084\3\u0084\3\u0085\3\u0085")
        buf.write(u"\3\u0085\3\u0085\3\u0085\7\u0085\u06e6\n\u0085\f\u0085")
        buf.write(u"\16\u0085\u06e9\13\u0085\3\u0086\3\u0086\3\u0086\3\u0086")
        buf.write(u"\5\u0086\u06ef\n\u0086\3\u0087\3\u0087\3\u0087\7\u0087")
        buf.write(u"\u06f4\n\u0087\f\u0087\16\u0087\u06f7\13\u0087\3\u0088")
        buf.write(u"\3\u0088\3\u0088\7\u0088\u06fc\n\u0088\f\u0088\16\u0088")
        buf.write(u"\u06ff\13\u0088\3\u0088\5\u0088\u0702\n\u0088\3\u0089")
        buf.write(u"\3\u0089\3\u0089\3\u0089\3\u0089\3\u0089\5\u0089\u070a")
        buf.write(u"\n\u0089\3\u008a\3\u008a\3\u008a\3\u008b\3\u008b\3\u008b")
        buf.write(u"\3\u008c\3\u008c\3\u008c\3\u008d\3\u008d\3\u008d\3\u008e")
        buf.write(u"\3\u008e\3\u008f\3\u008f\3\u0090\3\u0090\3\u0091\3\u0091")
        buf.write(u"\3\u0092\3\u0092\3\u0093\3\u0093\3\u0093\3\u0093\3\u0093")
        buf.write(u"\3\u0093\3\u0093\5\u0093\u0729\n\u0093\3\u0094\3\u0094")
        buf.write(u"\3\u0094\3\u0094\3\u0094\7\u0094\u0730\n\u0094\f\u0094")
        buf.write(u"\16\u0094\u0733\13\u0094\3\u0095\3\u0095\3\u0095\3\u0095")
        buf.write(u"\3\u0095\3\u0095\3\u0095\5\u0095\u073c\n\u0095\3\u0096")
        buf.write(u"\3\u0096\3\u0097\3\u0097\3\u0097\3\u0098\3\u0098\3\u0098")
        buf.write(u"\3\u0098\3\u0098\5\u0098\u0748\n\u0098\3\u0099\3\u0099")
        buf.write(u"\3\u0099\5\u0099\u074d\n\u0099\3\u0099\3\u0099\3\u009a")
        buf.write(u"\3\u009a\3\u009a\3\u009a\3\u009a\3\u009a\7\u009a\u0757")
        buf.write(u"\n\u009a\f\u009a\16\u009a\u075a\13\u009a\3\u009b\3\u009b")
        buf.write(u"\3\u009b\3\u009b\3\u009c\3\u009c\3\u009c\3\u009c\3\u009d")
        buf.write(u"\3\u009d\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e\5\u009e")
        buf.write(u"\u076b\n\u009e\3\u009f\3\u009f\3\u00a0\3\u00a0\3\u00a0")
        buf.write(u"\5\u00a0\u0772\n\u00a0\3\u00a1\3\u00a1\3\u00a1\3\u00a1")
        buf.write(u"\3\u00a1\7\u00a1\u0779\n\u00a1\f\u00a1\16\u00a1\u077c")
        buf.write(u"\13\u00a1\3\u00a2\3\u00a2\3\u00a2\3\u00a2\5\u00a2\u0782")
        buf.write(u"\n\u00a2\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3")
        buf.write(u"\5\u00a3\u078a\n\u00a3\3\u00a4\3\u00a4\3\u00a4\5\u00a4")
        buf.write(u"\u078f\n\u00a4\3\u00a4\3\u00a4\3\u00a5\3\u00a5\3\u00a5")
        buf.write(u"\3\u00a5\3\u00a5\3\u00a5\5\u00a5\u0799\n\u00a5\3\u00a6")
        buf.write(u"\3\u00a6\3\u00a6\3\u00a6\3\u00a6\3\u00a6\7\u00a6\u07a1")
        buf.write(u"\n\u00a6\f\u00a6\16\u00a6\u07a4\13\u00a6\3\u00a7\3\u00a7")
        buf.write(u"\3\u00a7\3\u00a7\3\u00a7\3\u00a7\3\u00a7\3\u00a7\3\u00a7")
        buf.write(u"\3\u00a7\3\u00a7\7\u00a7\u07b1\n\u00a7\f\u00a7\16\u00a7")
        buf.write(u"\u07b4\13\u00a7\3\u00a8\3\u00a8\3\u00a8\3\u00a8\3\u00a9")
        buf.write(u"\3\u00a9\3\u00a9\5\u00a9\u07bd\n\u00a9\3\u00a9\3\u00a9")
        buf.write(u"\3\u00a9\7\u00a9\u07c2\n\u00a9\f\u00a9\16\u00a9\u07c5")
        buf.write(u"\13\u00a9\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00aa\5\u00aa")
        buf.write(u"\u07cc\n\u00aa\3\u00ab\3\u00ab\3\u00ac\3\u00ac\3\u00ac")
        buf.write(u"\3\u00ac\3\u00ac\3\u00ac\3\u00ac\5\u00ac\u07d7\n\u00ac")
        buf.write(u"\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad\7\u00ad\u07de")
        buf.write(u"\n\u00ad\f\u00ad\16\u00ad\u07e1\13\u00ad\3\u00ae\3\u00ae")
        buf.write(u"\3\u00ae\3\u00ae\3\u00ae\5\u00ae\u07e8\n\u00ae\3\u00af")
        buf.write(u"\3\u00af\3\u00b0\3\u00b0\3\u00b0\3\u00b1\3\u00b1\3\u00b1")
        buf.write(u"\5\u00b1\u07f2\n\u00b1\3\u00b2\3\u00b2\3\u00b2\5\u00b2")
        buf.write(u"\u07f7\n\u00b2\3\u00b2\3\u00b2\3\u00b3\3\u00b3\3\u00b3")
        buf.write(u"\3\u00b3\3\u00b3\3\u00b3\7\u00b3\u0801\n\u00b3\f\u00b3")
        buf.write(u"\16\u00b3\u0804\13\u00b3\3\u00b4\3\u00b4\3\u00b4\3\u00b4")
        buf.write(u"\3\u00b5\3\u00b5\3\u00b5\3\u00b5\3\u00b6\3\u00b6\3\u00b6")
        buf.write(u"\3\u00b6\3\u00b6\3\u00b6\7\u00b6\u0814\n\u00b6\f\u00b6")
        buf.write(u"\16\u00b6\u0817\13\u00b6\3\u00b7\3\u00b7\3\u00b7\3\u00b7")
        buf.write(u"\3\u00b7\7\u00b7\u081e\n\u00b7\f\u00b7\16\u00b7\u0821")
        buf.write(u"\13\u00b7\3\u00b8\3\u00b8\3\u00b8\3\u00b8\3\u00b8\5\u00b8")
        buf.write(u"\u0828\n\u00b8\3\u00b9\3\u00b9\3\u00ba\3\u00ba\3\u00ba")
        buf.write(u"\3\u00ba\3\u00ba\3\u00ba\3\u00ba\5\u00ba\u0833\n\u00ba")
        buf.write(u"\3\u00bb\3\u00bb\3\u00bb\3\u00bb\3\u00bb\7\u00bb\u083a")
        buf.write(u"\n\u00bb\f\u00bb\16\u00bb\u083d\13\u00bb\3\u00bc\3\u00bc")
        buf.write(u"\3\u00bc\3\u00bc\3\u00bc\5\u00bc\u0844\n\u00bc\3\u00bd")
        buf.write(u"\3\u00bd\3\u00be\3\u00be\3\u00be\3\u00bf\3\u00bf\3\u00bf")
        buf.write(u"\5\u00bf\u084e\n\u00bf\3\u00c0\3\u00c0\3\u00c0\5\u00c0")
        buf.write(u"\u0853\n\u00c0\3\u00c0\3\u00c0\3\u00c1\3\u00c1\3\u00c1")
        buf.write(u"\3\u00c1\3\u00c1\3\u00c1\7\u00c1\u085d\n\u00c1\f\u00c1")
        buf.write(u"\16\u00c1\u0860\13\u00c1\3\u00c2\3\u00c2\3\u00c2\3\u00c2")
        buf.write(u"\3\u00c3\3\u00c3\3\u00c3\3\u00c3\3\u00c4\3\u00c4\3\u00c4")
        buf.write(u"\5\u00c4\u086d\n\u00c4\3\u00c4\3\u00c4\3\u00c4\7\u00c4")
        buf.write(u"\u0872\n\u00c4\f\u00c4\16\u00c4\u0875\13\u00c4\3\u00c5")
        buf.write(u"\3\u00c5\3\u00c5\3\u00c5\3\u00c5\5\u00c5\u087c\n\u00c5")
        buf.write(u"\3\u00c6\3\u00c6\3\u00c6\2*\36\66JTXb\u0080\u0088\u008a")
        buf.write(u"\u008c\u0094\u0098\u00a6\u00b2\u00be\u00c0\u00c4\u00d4")
        buf.write(u"\u00da\u00e2\u00e4\u00e6\u00e8\u00ee\u00fe\u0100\u0108")
        buf.write(u"\u0126\u0132\u0140\u014a\u014c\u0150\u0158\u0164\u016a")
        buf.write(u"\u016c\u0174\u0180\u0186\u00c7\2\4\6\b\n\f\16\20\22\24")
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
        buf.write(u"\u0188\u018a\2\13\3\2QR\3\2\"#\4\2\u0087\u0087\u008f")
        buf.write(u"\u008f\4\2IIYY\4\2\'\'qq\b\2\64<\u0081\u0081\u008e\u008e")
        buf.write(u"\u0098\u0098\u009d\u009f\u00a1\u00a1\b\2\64<\u0081\u0081")
        buf.write(u"\u0087\u0087\u008e\u008f\u0098\u0098\u009d\u009f\7\2")
        buf.write(u"\64<\u0081\u0081\u008e\u008e\u0098\u0098\u009d\u00a1")
        buf.write(u"\7\2\64<\u0081\u0081\u008e\u008e\u0098\u0098\u009d\u009f")
        buf.write(u"\u08e8\2\u018c\3\2\2\2\4\u019d\3\2\2\2\6\u01a7\3\2\2")
        buf.write(u"\2\b\u01ab\3\2\2\2\n\u01b3\3\2\2\2\f\u01c3\3\2\2\2\16")
        buf.write(u"\u01d9\3\2\2\2\20\u01e6\3\2\2\2\22\u01e8\3\2\2\2\24\u01f7")
        buf.write(u"\3\2\2\2\26\u0201\3\2\2\2\30\u020c\3\2\2\2\32\u0220\3")
        buf.write(u"\2\2\2\34\u0232\3\2\2\2\36\u023a\3\2\2\2 \u0246\3\2\2")
        buf.write(u"\2\"\u0248\3\2\2\2$\u0254\3\2\2\2&\u0264\3\2\2\2(\u0275")
        buf.write(u"\3\2\2\2*\u0288\3\2\2\2,\u028a\3\2\2\2.\u02a8\3\2\2\2")
        buf.write(u"\60\u02be\3\2\2\2\62\u02c0\3\2\2\2\64\u02cc\3\2\2\2\66")
        buf.write(u"\u02ce\3\2\2\28\u02de\3\2\2\2:\u02e0\3\2\2\2<\u02e7\3")
        buf.write(u"\2\2\2>\u02ee\3\2\2\2@\u030e\3\2\2\2B\u0310\3\2\2\2D")
        buf.write(u"\u031d\3\2\2\2F\u0326\3\2\2\2H\u032d\3\2\2\2J\u0341\3")
        buf.write(u"\2\2\2L\u0359\3\2\2\2N\u035c\3\2\2\2P\u038d\3\2\2\2R")
        buf.write(u"\u038f\3\2\2\2T\u03a5\3\2\2\2V\u0410\3\2\2\2X\u0412\3")
        buf.write(u"\2\2\2Z\u0422\3\2\2\2\\\u0431\3\2\2\2^\u0433\3\2\2\2")
        buf.write(u"`\u0437\3\2\2\2b\u0443\3\2\2\2d\u044d\3\2\2\2f\u0451")
        buf.write(u"\3\2\2\2h\u0455\3\2\2\2j\u047f\3\2\2\2l\u0481\3\2\2\2")
        buf.write(u"n\u048d\3\2\2\2p\u0499\3\2\2\2r\u049b\3\2\2\2t\u04a2")
        buf.write(u"\3\2\2\2v\u04a6\3\2\2\2x\u04ab\3\2\2\2z\u04b4\3\2\2\2")
        buf.write(u"|\u04b9\3\2\2\2~\u04bc\3\2\2\2\u0080\u04c1\3\2\2\2\u0082")
        buf.write(u"\u04d2\3\2\2\2\u0084\u04dc\3\2\2\2\u0086\u04e0\3\2\2")
        buf.write(u"\2\u0088\u04e2\3\2\2\2\u008a\u04ee\3\2\2\2\u008c\u04fa")
        buf.write(u"\3\2\2\2\u008e\u050f\3\2\2\2\u0090\u0511\3\2\2\2\u0092")
        buf.write(u"\u0517\3\2\2\2\u0094\u051d\3\2\2\2\u0096\u0528\3\2\2")
        buf.write(u"\2\u0098\u052e\3\2\2\2\u009a\u0540\3\2\2\2\u009c\u0550")
        buf.write(u"\3\2\2\2\u009e\u0552\3\2\2\2\u00a0\u0555\3\2\2\2\u00a2")
        buf.write(u"\u0559\3\2\2\2\u00a4\u055e\3\2\2\2\u00a6\u0560\3\2\2")
        buf.write(u"\2\u00a8\u056d\3\2\2\2\u00aa\u0572\3\2\2\2\u00ac\u0574")
        buf.write(u"\3\2\2\2\u00ae\u0576\3\2\2\2\u00b0\u0578\3\2\2\2\u00b2")
        buf.write(u"\u057a\3\2\2\2\u00b4\u058a\3\2\2\2\u00b6\u058e\3\2\2")
        buf.write(u"\2\u00b8\u0590\3\2\2\2\u00ba\u0595\3\2\2\2\u00bc\u059a")
        buf.write(u"\3\2\2\2\u00be\u059c\3\2\2\2\u00c0\u05aa\3\2\2\2\u00c2")
        buf.write(u"\u05bb\3\2\2\2\u00c4\u05bd\3\2\2\2\u00c6\u05cb\3\2\2")
        buf.write(u"\2\u00c8\u05d7\3\2\2\2\u00ca\u05d9\3\2\2\2\u00cc\u05dd")
        buf.write(u"\3\2\2\2\u00ce\u05e8\3\2\2\2\u00d0\u05eb\3\2\2\2\u00d2")
        buf.write(u"\u05ef\3\2\2\2\u00d4\u0601\3\2\2\2\u00d6\u0610\3\2\2")
        buf.write(u"\2\u00d8\u0612\3\2\2\2\u00da\u0614\3\2\2\2\u00dc\u062a")
        buf.write(u"\3\2\2\2\u00de\u062c\3\2\2\2\u00e0\u0633\3\2\2\2\u00e2")
        buf.write(u"\u063a\3\2\2\2\u00e4\u0646\3\2\2\2\u00e6\u0652\3\2\2")
        buf.write(u"\2\u00e8\u065e\3\2\2\2\u00ea\u0678\3\2\2\2\u00ec\u0687")
        buf.write(u"\3\2\2\2\u00ee\u0689\3\2\2\2\u00f0\u0698\3\2\2\2\u00f2")
        buf.write(u"\u069a\3\2\2\2\u00f4\u069c\3\2\2\2\u00f6\u06a2\3\2\2")
        buf.write(u"\2\u00f8\u06a9\3\2\2\2\u00fa\u06ab\3\2\2\2\u00fc\u06b1")
        buf.write(u"\3\2\2\2\u00fe\u06b7\3\2\2\2\u0100\u06c2\3\2\2\2\u0102")
        buf.write(u"\u06cd\3\2\2\2\u0104\u06da\3\2\2\2\u0106\u06dc\3\2\2")
        buf.write(u"\2\u0108\u06e0\3\2\2\2\u010a\u06ee\3\2\2\2\u010c\u06f0")
        buf.write(u"\3\2\2\2\u010e\u06f8\3\2\2\2\u0110\u0709\3\2\2\2\u0112")
        buf.write(u"\u070b\3\2\2\2\u0114\u070e\3\2\2\2\u0116\u0711\3\2\2")
        buf.write(u"\2\u0118\u0714\3\2\2\2\u011a\u0717\3\2\2\2\u011c\u0719")
        buf.write(u"\3\2\2\2\u011e\u071b\3\2\2\2\u0120\u071d\3\2\2\2\u0122")
        buf.write(u"\u071f\3\2\2\2\u0124\u0728\3\2\2\2\u0126\u072a\3\2\2")
        buf.write(u"\2\u0128\u073b\3\2\2\2\u012a\u073d\3\2\2\2\u012c\u073f")
        buf.write(u"\3\2\2\2\u012e\u0747\3\2\2\2\u0130\u0749\3\2\2\2\u0132")
        buf.write(u"\u0750\3\2\2\2\u0134\u075b\3\2\2\2\u0136\u075f\3\2\2")
        buf.write(u"\2\u0138\u0763\3\2\2\2\u013a\u076a\3\2\2\2\u013c\u076c")
        buf.write(u"\3\2\2\2\u013e\u0771\3\2\2\2\u0140\u0773\3\2\2\2\u0142")
        buf.write(u"\u0781\3\2\2\2\u0144\u0789\3\2\2\2\u0146\u078b\3\2\2")
        buf.write(u"\2\u0148\u0798\3\2\2\2\u014a\u079a\3\2\2\2\u014c\u07a5")
        buf.write(u"\3\2\2\2\u014e\u07b5\3\2\2\2\u0150\u07bc\3\2\2\2\u0152")
        buf.write(u"\u07cb\3\2\2\2\u0154\u07cd\3\2\2\2\u0156\u07d6\3\2\2")
        buf.write(u"\2\u0158\u07d8\3\2\2\2\u015a\u07e7\3\2\2\2\u015c\u07e9")
        buf.write(u"\3\2\2\2\u015e\u07eb\3\2\2\2\u0160\u07f1\3\2\2\2\u0162")
        buf.write(u"\u07f3\3\2\2\2\u0164\u07fa\3\2\2\2\u0166\u0805\3\2\2")
        buf.write(u"\2\u0168\u0809\3\2\2\2\u016a\u080d\3\2\2\2\u016c\u0818")
        buf.write(u"\3\2\2\2\u016e\u0827\3\2\2\2\u0170\u0829\3\2\2\2\u0172")
        buf.write(u"\u0832\3\2\2\2\u0174\u0834\3\2\2\2\u0176\u0843\3\2\2")
        buf.write(u"\2\u0178\u0845\3\2\2\2\u017a\u0847\3\2\2\2\u017c\u084d")
        buf.write(u"\3\2\2\2\u017e\u084f\3\2\2\2\u0180\u0856\3\2\2\2\u0182")
        buf.write(u"\u0861\3\2\2\2\u0184\u0865\3\2\2\2\u0186\u086c\3\2\2")
        buf.write(u"\2\u0188\u087b\3\2\2\2\u018a\u087d\3\2\2\2\u018c\u018d")
        buf.write(u"\7^\2\2\u018d\u018e\5\u00aeX\2\u018e\u0195\7\26\2\2\u018f")
        buf.write(u"\u0192\5\u00aeX\2\u0190\u0191\7\23\2\2\u0191\u0193\5")
        buf.write(u" \21\2\u0192\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193")
        buf.write(u"\u0196\3\2\2\2\u0194\u0196\5 \21\2\u0195\u018f\3\2\2")
        buf.write(u"\2\u0195\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0198")
        buf.write(u"\7\27\2\2\u0198\u0199\7\21\2\2\u0199\u019a\5x=\2\u019a")
        buf.write(u"\u019b\5\u008aF\2\u019b\u019c\5z>\2\u019c\3\3\2\2\2\u019d")
        buf.write(u"\u019e\7^\2\2\u019e\u019f\5\u00aeX\2\u019f\u01a0\7\26")
        buf.write(u"\2\2\u01a0\u01a1\5\u009cO\2\u01a1\u01a2\7\27\2\2\u01a2")
        buf.write(u"\u01a3\7\21\2\2\u01a3\u01a4\5x=\2\u01a4\u01a5\5\u0088")
        buf.write(u"E\2\u01a5\u01a6\5z>\2\u01a6\5\3\2\2\2\u01a7\u01a8\5\u00b0")
        buf.write(u"Y\2\u01a8\u01a9\7-\2\2\u01a9\u01aa\5T+\2\u01aa\7\3\2")
        buf.write(u"\2\2\u01ab\u01ac\5\u00b0Y\2\u01ac\u01ae\7\26\2\2\u01ad")
        buf.write(u"\u01af\5b\62\2\u01ae\u01ad\3\2\2\2\u01ae\u01af\3\2\2")
        buf.write(u"\2\u01af\u01b0\3\2\2\2\u01b0\u01b1\7\27\2\2\u01b1\t\3")
        buf.write(u"\2\2\2\u01b2\u01b4\7\u008b\2\2\u01b3\u01b2\3\2\2\2\u01b3")
        buf.write(u"\u01b4\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b6\7J\2\2")
        buf.write(u"\u01b6\u01b7\5\u00acW\2\u01b7\u01b8\7\26\2\2\u01b8\u01b9")
        buf.write(u"\5\u0098M\2\u01b9\u01ba\7\27\2\2\u01ba\u01bb\7\21\2\2")
        buf.write(u"\u01bb\u01be\5x=\2\u01bc\u01bf\5\u008eH\2\u01bd\u01bf")
        buf.write(u"\7\177\2\2\u01be\u01bc\3\2\2\2\u01be\u01bd\3\2\2\2\u01bf")
        buf.write(u"\u01c0\3\2\2\2\u01c0\u01c1\5z>\2\u01c1\13\3\2\2\2\u01c2")
        buf.write(u"\u01c4\7\u008b\2\2\u01c3\u01c2\3\2\2\2\u01c3\u01c4\3")
        buf.write(u"\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c6\t\2\2\2\u01c6")
        buf.write(u"\u01c7\5\u00aeX\2\u01c7\u01ce\7\26\2\2\u01c8\u01cf\5")
        buf.write(u"\20\t\2\u01c9\u01cf\5 \21\2\u01ca\u01cb\5\20\t\2\u01cb")
        buf.write(u"\u01cc\7\23\2\2\u01cc\u01cd\5 \21\2\u01cd\u01cf\3\2\2")
        buf.write(u"\2\u01ce\u01c8\3\2\2\2\u01ce\u01c9\3\2\2\2\u01ce\u01ca")
        buf.write(u"\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d1\7\27\2\2\u01d1")
        buf.write(u"\u01d2\7\21\2\2\u01d2\u01d5\5x=\2\u01d3\u01d6\5\u00c0")
        buf.write(u"a\2\u01d4\u01d6\7\177\2\2\u01d5\u01d3\3\2\2\2\u01d5\u01d4")
        buf.write(u"\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d8\5z>\2\u01d8")
        buf.write(u"\r\3\2\2\2\u01d9\u01da\7\u0089\2\2\u01da\u01db\5\u00ae")
        buf.write(u"X\2\u01db\u01dc\7\26\2\2\u01dc\u01dd\5 \21\2\u01dd\u01de")
        buf.write(u"\7\27\2\2\u01de\u01df\7\21\2\2\u01df\u01e2\5x=\2\u01e0")
        buf.write(u"\u01e3\5\u00c0a\2\u01e1\u01e3\7\177\2\2\u01e2\u01e0\3")
        buf.write(u"\2\2\2\u01e2\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4")
        buf.write(u"\u01e5\5z>\2\u01e5\17\3\2\2\2\u01e6\u01e7\5\u00a6T\2")
        buf.write(u"\u01e7\21\3\2\2\2\u01e8\u01e9\7U\2\2\u01e9\u01ea\7{\2")
        buf.write(u"\2\u01ea\u01eb\5\u0110\u0089\2\u01eb\u01ec\7\26\2\2\u01ec")
        buf.write(u"\u01ed\5\u00b6\\\2\u01ed\u01f0\7\27\2\2\u01ee\u01ef\7")
        buf.write(u"\63\2\2\u01ef\u01f1\5\u0098M\2\u01f0\u01ee\3\2\2\2\u01f0")
        buf.write(u"\u01f1\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3\7\21\2")
        buf.write(u"\2\u01f3\u01f4\5x=\2\u01f4\u01f5\5\u00e2r\2\u01f5\u01f6")
        buf.write(u"\5z>\2\u01f6\23\3\2\2\2\u01f7\u01f8\7U\2\2\u01f8\u01f9")
        buf.write(u"\5\u00acW\2\u01f9\u01fa\7\u0088\2\2\u01fa\u01fb\7\26")
        buf.write(u"\2\2\u01fb\u01fc\7\27\2\2\u01fc\u01fd\7\21\2\2\u01fd")
        buf.write(u"\u01fe\5x=\2\u01fe\u01ff\5\u00e2r\2\u01ff\u0200\5z>\2")
        buf.write(u"\u0200\25\3\2\2\2\u0201\u0202\7U\2\2\u0202\u0203\5\u00ac")
        buf.write(u"W\2\u0203\u0204\7h\2\2\u0204\u0205\7\26\2\2\u0205\u0206")
        buf.write(u"\7\27\2\2\u0206\u0207\7\21\2\2\u0207\u0208\5x=\2\u0208")
        buf.write(u"\u0209\5\u00e2r\2\u0209\u020a\5z>\2\u020a\27\3\2\2\2")
        buf.write(u"\u020b\u020d\7\u008b\2\2\u020c\u020b\3\2\2\2\u020c\u020d")
        buf.write(u"\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u020f\7s\2\2\u020f")
        buf.write(u"\u0210\t\2\2\2\u0210\u0211\5\u00aeX\2\u0211\u0213\7\26")
        buf.write(u"\2\2\u0212\u0214\5 \21\2\u0213\u0212\3\2\2\2\u0213\u0214")
        buf.write(u"\3\2\2\2\u0214\u0215\3\2\2\2\u0215\u0216\7\27\2\2\u0216")
        buf.write(u"\u0217\7\21\2\2\u0217\u0218\5x=\2\u0218\u021c\5\34\17")
        buf.write(u"\2\u0219\u021a\5v<\2\u021a\u021b\5\u00c4c\2\u021b\u021d")
        buf.write(u"\3\2\2\2\u021c\u0219\3\2\2\2\u021c\u021d\3\2\2\2\u021d")
        buf.write(u"\u021e\3\2\2\2\u021e\u021f\5z>\2\u021f\31\3\2\2\2\u0220")
        buf.write(u"\u0221\7s\2\2\u0221\u0222\7\u0083\2\2\u0222\u0223\5\u00ae")
        buf.write(u"X\2\u0223\u0225\7\26\2\2\u0224\u0226\5 \21\2\u0225\u0224")
        buf.write(u"\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0227\3\2\2\2\u0227")
        buf.write(u"\u0228\7\27\2\2\u0228\u0229\7\21\2\2\u0229\u022a\5x=")
        buf.write(u"\2\u022a\u022e\5\34\17\2\u022b\u022c\5v<\2\u022c\u022d")
        buf.write(u"\5\u00c4c\2\u022d\u022f\3\2\2\2\u022e\u022b\3\2\2\2\u022e")
        buf.write(u"\u022f\3\2\2\2\u022f\u0230\3\2\2\2\u0230\u0231\5z>\2")
        buf.write(u"\u0231\33\3\2\2\2\u0232\u0233\7U\2\2\u0233\u0234\t\2")
        buf.write(u"\2\2\u0234\u0235\7M\2\2\u0235\u0236\7\21\2\2\u0236\u0237")
        buf.write(u"\5x=\2\u0237\u0238\5\36\20\2\u0238\u0239\5z>\2\u0239")
        buf.write(u"\35\3\2\2\2\u023a\u023b\b\20\1\2\u023b\u023c\5\u00c8")
        buf.write(u"e\2\u023c\u0243\3\2\2\2\u023d\u023e\f\3\2\2\u023e\u023f")
        buf.write(u"\5v<\2\u023f\u0240\5\u00c8e\2\u0240\u0242\3\2\2\2\u0241")
        buf.write(u"\u023d\3\2\2\2\u0242\u0245\3\2\2\2\u0243\u0241\3\2\2")
        buf.write(u"\2\u0243\u0244\3\2\2\2\u0244\37\3\2\2\2\u0245\u0243\3")
        buf.write(u"\2\2\2\u0246\u0247\5\u00d4k\2\u0247!\3\2\2\2\u0248\u0249")
        buf.write(u"\7C\2\2\u0249\u024a\7U\2\2\u024a\u024b\5\u00a8U\2\u024b")
        buf.write(u"\u024d\7\26\2\2\u024c\u024e\5\u00b2Z\2\u024d\u024c\3")
        buf.write(u"\2\2\2\u024d\u024e\3\2\2\2\u024e\u024f\3\2\2\2\u024f")
        buf.write(u"\u0252\7\27\2\2\u0250\u0251\7\63\2\2\u0251\u0253\5\u0098")
        buf.write(u"M\2\u0252\u0250\3\2\2\2\u0252\u0253\3\2\2\2\u0253#\3")
        buf.write(u"\2\2\2\u0254\u0255\7U\2\2\u0255\u0256\5\u00a8U\2\u0256")
        buf.write(u"\u0258\7\26\2\2\u0257\u0259\5\u00b2Z\2\u0258\u0257\3")
        buf.write(u"\2\2\2\u0258\u0259\3\2\2\2\u0259\u025a\3\2\2\2\u025a")
        buf.write(u"\u025d\7\27\2\2\u025b\u025c\7\63\2\2\u025c\u025e\5\u0098")
        buf.write(u"M\2\u025d\u025b\3\2\2\2\u025d\u025e\3\2\2\2\u025e\u025f")
        buf.write(u"\3\2\2\2\u025f\u0260\7\21\2\2\u0260\u0261\5x=\2\u0261")
        buf.write(u"\u0262\5\u00e2r\2\u0262\u0263\5z>\2\u0263%\3\2\2\2\u0264")
        buf.write(u"\u0265\7U\2\2\u0265\u0266\7s\2\2\u0266\u0267\5\u00a8")
        buf.write(u"U\2\u0267\u0269\7\26\2\2\u0268\u026a\5\u00b2Z\2\u0269")
        buf.write(u"\u0268\3\2\2\2\u0269\u026a\3\2\2\2\u026a\u026b\3\2\2")
        buf.write(u"\2\u026b\u026e\7\27\2\2\u026c\u026d\7\63\2\2\u026d\u026f")
        buf.write(u"\5\u00bc_\2\u026e\u026c\3\2\2\2\u026e\u026f\3\2\2\2\u026f")
        buf.write(u"\u0270\3\2\2\2\u0270\u0271\7\21\2\2\u0271\u0272\5x=\2")
        buf.write(u"\u0272\u0273\5\u00dan\2\u0273\u0274\5z>\2\u0274\'\3\2")
        buf.write(u"\2\2\u0275\u0276\7U\2\2\u0276\u0277\7\u008e\2\2\u0277")
        buf.write(u"\u0278\7\u00a2\2\2\u0278\u0279\7\26\2\2\u0279\u027a\7")
        buf.write(u"\27\2\2\u027a\u027b\7\21\2\2\u027b\u027c\5x=\2\u027c")
        buf.write(u"\u027d\5\u00e2r\2\u027d\u027e\5z>\2\u027e\u027f\5v<\2")
        buf.write(u"\u027f\u0280\7\u0093\2\2\u0280\u0286\7\21\2\2\u0281\u0282")
        buf.write(u"\5x=\2\u0282\u0283\5\u00e4s\2\u0283\u0284\5z>\2\u0284")
        buf.write(u"\u0287\3\2\2\2\u0285\u0287\5\u00b0Y\2\u0286\u0281\3\2")
        buf.write(u"\2\2\u0286\u0285\3\2\2\2\u0287)\3\2\2\2\u0288\u0289\5")
        buf.write(u"T+\2\u0289+\3\2\2\2\u028a\u028b\5\u00acW\2\u028b\u028c")
        buf.write(u"\7\21\2\2\u028c\u0291\5\u00bc_\2\u028d\u028e\7\26\2\2")
        buf.write(u"\u028e\u028f\5 \21\2\u028f\u0290\7\27\2\2\u0290\u0292")
        buf.write(u"\3\2\2\2\u0291\u028d\3\2\2\2\u0291\u0292\3\2\2\2\u0292")
        buf.write(u"\u0295\3\2\2\2\u0293\u0294\7-\2\2\u0294\u0296\5\u00f6")
        buf.write(u"|\2\u0295\u0293\3\2\2\2\u0295\u0296\3\2\2\2\u0296-\3")
        buf.write(u"\2\2\2\u0297\u02a9\5\62\32\2\u0298\u02a9\5n8\2\u0299")
        buf.write(u"\u02a9\5r:\2\u029a\u02a9\5\60\31\2\u029b\u02a9\5R*\2")
        buf.write(u"\u029c\u02a9\5H%\2\u029d\u02a9\5> \2\u029e\u02a9\5B\"")
        buf.write(u"\2\u029f\u02a9\5F$\2\u02a0\u02a9\5D#\2\u02a1\u02a9\5")
        buf.write(u"L\'\2\u02a2\u02a9\5N(\2\u02a3\u02a9\5h\65\2\u02a4\u02a9")
        buf.write(u"\5:\36\2\u02a5\u02a9\5<\37\2\u02a6\u02a9\5$\23\2\u02a7")
        buf.write(u"\u02a9\5\u00d8m\2\u02a8\u0297\3\2\2\2\u02a8\u0298\3\2")
        buf.write(u"\2\2\u02a8\u0299\3\2\2\2\u02a8\u029a\3\2\2\2\u02a8\u029b")
        buf.write(u"\3\2\2\2\u02a8\u029c\3\2\2\2\u02a8\u029d\3\2\2\2\u02a8")
        buf.write(u"\u029e\3\2\2\2\u02a8\u029f\3\2\2\2\u02a8\u02a0\3\2\2")
        buf.write(u"\2\u02a8\u02a1\3\2\2\2\u02a8\u02a2\3\2\2\2\u02a8\u02a3")
        buf.write(u"\3\2\2\2\u02a8\u02a4\3\2\2\2\u02a8\u02a5\3\2\2\2\u02a8")
        buf.write(u"\u02a6\3\2\2\2\u02a8\u02a7\3\2\2\2\u02a9/\3\2\2\2\u02aa")
        buf.write(u"\u02ab\7X\2\2\u02ab\u02ac\7\26\2\2\u02ac\u02ad\5\u0094")
        buf.write(u"K\2\u02ad\u02ae\7\27\2\2\u02ae\u02bf\3\2\2\2\u02af\u02b0")
        buf.write(u"\7\u008c\2\2\u02b0\u02b1\7\26\2\2\u02b1\u02b2\5\u0094")
        buf.write(u"K\2\u02b2\u02b3\7\27\2\2\u02b3\u02bf\3\2\2\2\u02b4\u02b5")
        buf.write(u"\7X\2\2\u02b5\u02b6\7\26\2\2\u02b6\u02b7\5\u0094K\2\u02b7")
        buf.write(u"\u02b8\7\27\2\2\u02b8\u02b9\7F\2\2\u02b9\u02ba\7\u008c")
        buf.write(u"\2\2\u02ba\u02bb\7\26\2\2\u02bb\u02bc\5\u0094K\2\u02bc")
        buf.write(u"\u02bd\7\27\2\2\u02bd\u02bf\3\2\2\2\u02be\u02aa\3\2\2")
        buf.write(u"\2\u02be\u02af\3\2\2\2\u02be\u02b4\3\2\2\2\u02bf\61\3")
        buf.write(u"\2\2\2\u02c0\u02c1\5\64\33\2\u02c1\u02c3\7\26\2\2\u02c2")
        buf.write(u"\u02c4\5b\62\2\u02c3\u02c2\3\2\2\2\u02c3\u02c4\3\2\2")
        buf.write(u"\2\u02c4\u02c5\3\2\2\2\u02c5\u02c6\7\27\2\2\u02c6\63")
        buf.write(u"\3\2\2\2\u02c7\u02cd\5\u00a8U\2\u02c8\u02c9\5\66\34\2")
        buf.write(u"\u02c9\u02ca\7\25\2\2\u02ca\u02cb\5\u00a8U\2\u02cb\u02cd")
        buf.write(u"\3\2\2\2\u02cc\u02c7\3\2\2\2\u02cc\u02c8\3\2\2\2\u02cd")
        buf.write(u"\65\3\2\2\2\u02ce\u02cf\b\34\1\2\u02cf\u02d0\5\u00aa")
        buf.write(u"V\2\u02d0\u02d5\3\2\2\2\u02d1\u02d2\f\3\2\2\u02d2\u02d4")
        buf.write(u"\58\35\2\u02d3\u02d1\3\2\2\2\u02d4\u02d7\3\2\2\2\u02d5")
        buf.write(u"\u02d3\3\2\2\2\u02d5\u02d6\3\2\2\2\u02d6\67\3\2\2\2\u02d7")
        buf.write(u"\u02d5\3\2\2\2\u02d8\u02d9\7\25\2\2\u02d9\u02df\5\u00ac")
        buf.write(u"W\2\u02da\u02db\7\30\2\2\u02db\u02dc\5T+\2\u02dc\u02dd")
        buf.write(u"\7\31\2\2\u02dd\u02df\3\2\2\2\u02de\u02d8\3\2\2\2\u02de")
        buf.write(u"\u02da\3\2\2\2\u02df9\3\2\2\2\u02e0\u02e1\7\u0094\2\2")
        buf.write(u"\u02e1\u02e2\5\u0106\u0084\2\u02e2\u02e3\7\21\2\2\u02e3")
        buf.write(u"\u02e4\5x=\2\u02e4\u02e5\5\u00e2r\2\u02e5\u02e6\5z>\2")
        buf.write(u"\u02e6;\3\2\2\2\u02e7\u02e8\7\u0094\2\2\u02e8\u02e9\5")
        buf.write(u"\u00aeX\2\u02e9\u02ea\7\21\2\2\u02ea\u02eb\5x=\2\u02eb")
        buf.write(u"\u02ec\5\u00e2r\2\u02ec\u02ed\5z>\2\u02ed=\3\2\2\2\u02ee")
        buf.write(u"\u02ef\7\u008d\2\2\u02ef\u02f0\7x\2\2\u02f0\u02f1\5T")
        buf.write(u"+\2\u02f1\u02f2\7\21\2\2\u02f2\u02f3\5x=\2\u02f3\u02fb")
        buf.write(u"\5\u00e6t\2\u02f4\u02f5\5v<\2\u02f5\u02f6\7~\2\2\u02f6")
        buf.write(u"\u02f7\7\21\2\2\u02f7\u02f8\5x=\2\u02f8\u02f9\5\u00e2")
        buf.write(u"r\2\u02f9\u02fa\5z>\2\u02fa\u02fc\3\2\2\2\u02fb\u02f4")
        buf.write(u"\3\2\2\2\u02fb\u02fc\3\2\2\2\u02fc\u02fd\3\2\2\2\u02fd")
        buf.write(u"\u02fe\5z>\2\u02fe?\3\2\2\2\u02ff\u0300\7\u0095\2\2\u0300")
        buf.write(u"\u0301\5\u00ecw\2\u0301\u0302\7\21\2\2\u0302\u0303\5")
        buf.write(u"x=\2\u0303\u0304\5\u00e2r\2\u0304\u0305\5z>\2\u0305\u030f")
        buf.write(u"\3\2\2\2\u0306\u0307\7\u0095\2\2\u0307\u0308\7j\2\2\u0308")
        buf.write(u"\u0309\5\u00eav\2\u0309\u030a\7\21\2\2\u030a\u030b\5")
        buf.write(u"x=\2\u030b\u030c\5\u00e2r\2\u030c\u030d\5z>\2\u030d\u030f")
        buf.write(u"\3\2\2\2\u030e\u02ff\3\2\2\2\u030e\u0306\3\2\2\2\u030f")
        buf.write(u"A\3\2\2\2\u0310\u0311\7f\2\2\u0311\u0314\5\u00acW\2\u0312")
        buf.write(u"\u0313\7\23\2\2\u0313\u0315\5\u00acW\2\u0314\u0312\3")
        buf.write(u"\2\2\2\u0314\u0315\3\2\2\2\u0315\u0316\3\2\2\2\u0316")
        buf.write(u"\u0317\7j\2\2\u0317\u0318\5T+\2\u0318\u0319\7\21\2\2")
        buf.write(u"\u0319\u031a\5x=\2\u031a\u031b\5\u00e2r\2\u031b\u031c")
        buf.write(u"\5z>\2\u031cC\3\2\2\2\u031d\u031e\7Z\2\2\u031e\u031f")
        buf.write(u"\7\21\2\2\u031f\u0320\5x=\2\u0320\u0321\5\u00e2r\2\u0321")
        buf.write(u"\u0322\5z>\2\u0322\u0323\5v<\2\u0323\u0324\7\u0097\2")
        buf.write(u"\2\u0324\u0325\5T+\2\u0325E\3\2\2\2\u0326\u0327\7\u0097")
        buf.write(u"\2\2\u0327\u0328\5T+\2\u0328\u0329\7\21\2\2\u0329\u032a")
        buf.write(u"\5x=\2\u032a\u032b\5\u00e2r\2\u032b\u032c\5z>\2\u032c")
        buf.write(u"G\3\2\2\2\u032d\u032e\7i\2\2\u032e\u032f\5T+\2\u032f")
        buf.write(u"\u0330\7\21\2\2\u0330\u0331\5x=\2\u0331\u0332\5\u00e2")
        buf.write(u"r\2\u0332\u0336\5z>\2\u0333\u0334\5v<\2\u0334\u0335\5")
        buf.write(u"J&\2\u0335\u0337\3\2\2\2\u0336\u0333\3\2\2\2\u0336\u0337")
        buf.write(u"\3\2\2\2\u0337\u033f\3\2\2\2\u0338\u0339\5v<\2\u0339")
        buf.write(u"\u033a\7]\2\2\u033a\u033b\7\21\2\2\u033b\u033c\5x=\2")
        buf.write(u"\u033c\u033d\5\u00e2r\2\u033d\u033e\5z>\2\u033e\u0340")
        buf.write(u"\3\2\2\2\u033f\u0338\3\2\2\2\u033f\u0340\3\2\2\2\u0340")
        buf.write(u"I\3\2\2\2\u0341\u0342\b&\1\2\u0342\u0343\7]\2\2\u0343")
        buf.write(u"\u0344\7i\2\2\u0344\u0345\5T+\2\u0345\u0346\7\21\2\2")
        buf.write(u"\u0346\u0347\5x=\2\u0347\u0348\5\u00e2r\2\u0348\u0349")
        buf.write(u"\5z>\2\u0349\u0356\3\2\2\2\u034a\u034b\f\3\2\2\u034b")
        buf.write(u"\u034c\5v<\2\u034c\u034d\7]\2\2\u034d\u034e\7i\2\2\u034e")
        buf.write(u"\u034f\5T+\2\u034f\u0350\7\21\2\2\u0350\u0351\5x=\2\u0351")
        buf.write(u"\u0352\5\u00e2r\2\u0352\u0353\5z>\2\u0353\u0355\3\2\2")
        buf.write(u"\2\u0354\u034a\3\2\2\2\u0355\u0358\3\2\2\2\u0356\u0354")
        buf.write(u"\3\2\2\2\u0356\u0357\3\2\2\2\u0357K\3\2\2\2\u0358\u0356")
        buf.write(u"\3\2\2\2\u0359\u035a\7\u0080\2\2\u035a\u035b\5T+\2\u035b")
        buf.write(u"M\3\2\2\2\u035c\u035d\7\u0092\2\2\u035d\u035e\5\u00ac")
        buf.write(u"W\2\u035e\u035f\7\21\2\2\u035f\u0360\5x=\2\u0360\u0361")
        buf.write(u"\5\u00e2r\2\u0361\u0362\5z>\2\u0362\u0364\5t;\2\u0363")
        buf.write(u"\u0365\5\u00e8u\2\u0364\u0363\3\2\2\2\u0364\u0365\3\2")
        buf.write(u"\2\2\u0365\u036d\3\2\2\2\u0366\u0367\7`\2\2\u0367\u0368")
        buf.write(u"\7\21\2\2\u0368\u0369\5x=\2\u0369\u036a\5\u00e2r\2\u036a")
        buf.write(u"\u036b\5z>\2\u036b\u036c\5t;\2\u036c\u036e\3\2\2\2\u036d")
        buf.write(u"\u0366\3\2\2\2\u036d\u036e\3\2\2\2\u036e\u0376\3\2\2")
        buf.write(u"\2\u036f\u0370\7e\2\2\u0370\u0371\7\21\2\2\u0371\u0372")
        buf.write(u"\5x=\2\u0372\u0373\5\u00e2r\2\u0373\u0374\5z>\2\u0374")
        buf.write(u"\u0375\5t;\2\u0375\u0377\3\2\2\2\u0376\u036f\3\2\2\2")
        buf.write(u"\u0376\u0377\3\2\2\2\u0377\u0378\3\2\2\2\u0378\u0379")
        buf.write(u"\5t;\2\u0379O\3\2\2\2\u037a\u037b\7`\2\2\u037b\u037c")
        buf.write(u"\5\u00b0Y\2\u037c\u037d\7\21\2\2\u037d\u037e\5x=\2\u037e")
        buf.write(u"\u037f\5\u00e2r\2\u037f\u0380\5z>\2\u0380\u0381\5t;\2")
        buf.write(u"\u0381\u038e\3\2\2\2\u0382\u0383\7`\2\2\u0383\u0384\7")
        buf.write(u"j\2\2\u0384\u0385\7\30\2\2\u0385\u0386\5\u008cG\2\u0386")
        buf.write(u"\u0387\7\31\2\2\u0387\u0388\7\21\2\2\u0388\u0389\5x=")
        buf.write(u"\2\u0389\u038a\5\u00e2r\2\u038a\u038b\5z>\2\u038b\u038c")
        buf.write(u"\5t;\2\u038c\u038e\3\2\2\2\u038d\u037a\3\2\2\2\u038d")
        buf.write(u"\u0382\3\2\2\2\u038eQ\3\2\2\2\u038f\u0391\7\u0084\2\2")
        buf.write(u"\u0390\u0392\5T+\2\u0391\u0390\3\2\2\2\u0391\u0392\3")
        buf.write(u"\2\2\2\u0392S\3\2\2\2\u0393\u0394\b+\1\2\u0394\u0395")
        buf.write(u"\7#\2\2\u0395\u03a6\5T+\"\u0396\u0397\7u\2\2\u0397\u03a6")
        buf.write(u"\5T+!\u0398\u03a6\5X-\2\u0399\u03a6\5Z.\2\u039a\u039b")
        buf.write(u"\7>\2\2\u039b\u039c\7\26\2\2\u039c\u039d\5T+\2\u039d")
        buf.write(u"\u039e\7\27\2\2\u039e\u03a6\3\2\2\2\u039f\u03a0\7a\2")
        buf.write(u"\2\u03a0\u03a1\7\26\2\2\u03a1\u03a2\5\u00acW\2\u03a2")
        buf.write(u"\u03a3\7\27\2\2\u03a3\u03a6\3\2\2\2\u03a4\u03a6\5V,\2")
        buf.write(u"\u03a5\u0393\3\2\2\2\u03a5\u0396\3\2\2\2\u03a5\u0398")
        buf.write(u"\3\2\2\2\u03a5\u0399\3\2\2\2\u03a5\u039a\3\2\2\2\u03a5")
        buf.write(u"\u039f\3\2\2\2\u03a5\u03a4\3\2\2\2\u03a6\u040d\3\2\2")
        buf.write(u"\2\u03a7\u03a8\f \2\2\u03a8\u03a9\5\u011c\u008f\2\u03a9")
        buf.write(u"\u03aa\5T+!\u03aa\u040c\3\2\2\2\u03ab\u03ac\f\37\2\2")
        buf.write(u"\u03ac\u03ad\5\u011e\u0090\2\u03ad\u03ae\5T+ \u03ae\u040c")
        buf.write(u"\3\2\2\2\u03af\u03b0\f\36\2\2\u03b0\u03b1\5\u0122\u0092")
        buf.write(u"\2\u03b1\u03b2\5T+\37\u03b2\u040c\3\2\2\2\u03b3\u03b4")
        buf.write(u"\f\35\2\2\u03b4\u03b5\5\u0120\u0091\2\u03b5\u03b6\5T")
        buf.write(u"+\36\u03b6\u040c\3\2\2\2\u03b7\u03b8\f\34\2\2\u03b8\u03b9")
        buf.write(u"\t\3\2\2\u03b9\u040c\5T+\35\u03ba\u03bb\f\33\2\2\u03bb")
        buf.write(u"\u03bc\7*\2\2\u03bc\u040c\5T+\34\u03bd\u03be\f\32\2\2")
        buf.write(u"\u03be\u03bf\7+\2\2\u03bf\u040c\5T+\33\u03c0\u03c1\f")
        buf.write(u"\31\2\2\u03c1\u03c2\7(\2\2\u03c2\u040c\5T+\32\u03c3\u03c4")
        buf.write(u"\f\30\2\2\u03c4\u03c5\7)\2\2\u03c5\u040c\5T+\31\u03c6")
        buf.write(u"\u03c7\f\25\2\2\u03c7\u03c8\7/\2\2\u03c8\u040c\5T+\26")
        buf.write(u"\u03c9\u03ca\f\24\2\2\u03ca\u03cb\7.\2\2\u03cb\u040c")
        buf.write(u"\5T+\25\u03cc\u03cd\f\23\2\2\u03cd\u03ce\7\60\2\2\u03ce")
        buf.write(u"\u040c\5T+\24\u03cf\u03d0\f\22\2\2\u03d0\u03d1\7|\2\2")
        buf.write(u"\u03d1\u040c\5T+\23\u03d2\u03d3\f\21\2\2\u03d3\u03d4")
        buf.write(u"\7F\2\2\u03d4\u040c\5T+\22\u03d5\u03d6\f\20\2\2\u03d6")
        buf.write(u"\u03d7\7i\2\2\u03d7\u03d8\5T+\2\u03d8\u03d9\7]\2\2\u03d9")
        buf.write(u"\u03da\5T+\21\u03da\u040c\3\2\2\2\u03db\u03dc\f\16\2")
        buf.write(u"\2\u03dc\u03dd\7j\2\2\u03dd\u040c\5T+\17\u03de\u03df")
        buf.write(u"\f\r\2\2\u03df\u03e0\7T\2\2\u03e0\u040c\5T+\16\u03e1")
        buf.write(u"\u03e2\f\f\2\2\u03e2\u03e3\7T\2\2\u03e3\u03e4\7D\2\2")
        buf.write(u"\u03e4\u040c\5T+\r\u03e5\u03e6\f\13\2\2\u03e6\u03e7\7")
        buf.write(u"T\2\2\u03e7\u03e8\7G\2\2\u03e8\u040c\5T+\f\u03e9\u03ea")
        buf.write(u"\f\n\2\2\u03ea\u03eb\7u\2\2\u03eb\u03ec\7j\2\2\u03ec")
        buf.write(u"\u040c\5T+\13\u03ed\u03ee\f\t\2\2\u03ee\u03ef\7u\2\2")
        buf.write(u"\u03ef\u03f0\7T\2\2\u03f0\u040c\5T+\n\u03f1\u03f2\f\b")
        buf.write(u"\2\2\u03f2\u03f3\7u\2\2\u03f3\u03f4\7T\2\2\u03f4\u03f5")
        buf.write(u"\7D\2\2\u03f5\u040c\5T+\t\u03f6\u03f7\f\7\2\2\u03f7\u03f8")
        buf.write(u"\7u\2\2\u03f8\u03f9\7T\2\2\u03f9\u03fa\7G\2\2\u03fa\u040c")
        buf.write(u"\5T+\b\u03fb\u03fc\f\3\2\2\u03fc\u03fd\7f\2\2\u03fd\u03fe")
        buf.write(u"\5\u00acW\2\u03fe\u03ff\7j\2\2\u03ff\u0400\5T+\4\u0400")
        buf.write(u"\u040c\3\2\2\2\u0401\u0402\f\27\2\2\u0402\u0403\7m\2")
        buf.write(u"\2\u0403\u0404\7u\2\2\u0404\u040c\5\u010a\u0086\2\u0405")
        buf.write(u"\u0406\f\26\2\2\u0406\u0407\7m\2\2\u0407\u040c\5\u010a")
        buf.write(u"\u0086\2\u0408\u0409\f\17\2\2\u0409\u040a\7H\2\2\u040a")
        buf.write(u"\u040c\5\u00bc_\2\u040b\u03a7\3\2\2\2\u040b\u03ab\3\2")
        buf.write(u"\2\2\u040b\u03af\3\2\2\2\u040b\u03b3\3\2\2\2\u040b\u03b7")
        buf.write(u"\3\2\2\2\u040b\u03ba\3\2\2\2\u040b\u03bd\3\2\2\2\u040b")
        buf.write(u"\u03c0\3\2\2\2\u040b\u03c3\3\2\2\2\u040b\u03c6\3\2\2")
        buf.write(u"\2\u040b\u03c9\3\2\2\2\u040b\u03cc\3\2\2\2\u040b\u03cf")
        buf.write(u"\3\2\2\2\u040b\u03d2\3\2\2\2\u040b\u03d5\3\2\2\2\u040b")
        buf.write(u"\u03db\3\2\2\2\u040b\u03de\3\2\2\2\u040b\u03e1\3\2\2")
        buf.write(u"\2\u040b\u03e5\3\2\2\2\u040b\u03e9\3\2\2\2\u040b\u03ed")
        buf.write(u"\3\2\2\2\u040b\u03f1\3\2\2\2\u040b\u03f6\3\2\2\2\u040b")
        buf.write(u"\u03fb\3\2\2\2\u040b\u0401\3\2\2\2\u040b\u0405\3\2\2")
        buf.write(u"\2\u040b\u0408\3\2\2\2\u040c\u040f\3\2\2\2\u040d\u040b")
        buf.write(u"\3\2\2\2\u040d\u040e\3\2\2\2\u040eU\3\2\2\2\u040f\u040d")
        buf.write(u"\3\2\2\2\u0410\u0411\5\u00aeX\2\u0411W\3\2\2\2\u0412")
        buf.write(u"\u0413\b-\1\2\u0413\u0414\5\u00f0y\2\u0414\u0419\3\2")
        buf.write(u"\2\2\u0415\u0416\f\3\2\2\u0416\u0418\5\\/\2\u0417\u0415")
        buf.write(u"\3\2\2\2\u0418\u041b\3\2\2\2\u0419\u0417\3\2\2\2\u0419")
        buf.write(u"\u041a\3\2\2\2\u041aY\3\2\2\2\u041b\u0419\3\2\2\2\u041c")
        buf.write(u"\u0423\5^\60\2\u041d\u0423\5j\66\2\u041e\u0423\5f\64")
        buf.write(u"\2\u041f\u0423\5l\67\2\u0420\u0423\5\62\32\2\u0421\u0423")
        buf.write(u"\5`\61\2\u0422\u041c\3\2\2\2\u0422\u041d\3\2\2\2\u0422")
        buf.write(u"\u041e\3\2\2\2\u0422\u041f\3\2\2\2\u0422\u0420\3\2\2")
        buf.write(u"\2\u0422\u0421\3\2\2\2\u0423[\3\2\2\2\u0424\u0425\6/")
        buf.write(u"!\3\u0425\u0426\7\25\2\2\u0426\u0432\5\u00acW\2\u0427")
        buf.write(u"\u0428\6/\"\3\u0428\u0429\7\30\2\2\u0429\u042a\5\u0104")
        buf.write(u"\u0083\2\u042a\u042b\7\31\2\2\u042b\u0432\3\2\2\2\u042c")
        buf.write(u"\u042d\6/#\3\u042d\u042e\7\30\2\2\u042e\u042f\5T+\2\u042f")
        buf.write(u"\u0430\7\31\2\2\u0430\u0432\3\2\2\2\u0431\u0424\3\2\2")
        buf.write(u"\2\u0431\u0427\3\2\2\2\u0431\u042c\3\2\2\2\u0432]\3\2")
        buf.write(u"\2\2\u0433\u0434\7?\2\2\u0434\u0435\7\26\2\2\u0435\u0436")
        buf.write(u"\7\27\2\2\u0436_\3\2\2\2\u0437\u0438\5\u00a0Q\2\u0438")
        buf.write(u"\u043a\7\26\2\2\u0439\u043b\5b\62\2\u043a\u0439\3\2\2")
        buf.write(u"\2\u043a\u043b\3\2\2\2\u043b\u043c\3\2\2\2\u043c\u043d")
        buf.write(u"\7\27\2\2\u043da\3\2\2\2\u043e\u043f\b\62\1\2\u043f\u0440")
        buf.write(u"\5T+\2\u0440\u0441\6\62$\3\u0441\u0444\3\2\2\2\u0442")
        buf.write(u"\u0444\5d\63\2\u0443\u043e\3\2\2\2\u0443\u0442\3\2\2")
        buf.write(u"\2\u0444\u044a\3\2\2\2\u0445\u0446\f\3\2\2\u0446\u0447")
        buf.write(u"\7\23\2\2\u0447\u0449\5d\63\2\u0448\u0445\3\2\2\2\u0449")
        buf.write(u"\u044c\3\2\2\2\u044a\u0448\3\2\2\2\u044a\u044b\3\2\2")
        buf.write(u"\2\u044bc\3\2\2\2\u044c\u044a\3\2\2\2\u044d\u044e\5\u00ac")
        buf.write(u"W\2\u044e\u044f\5\u011a\u008e\2\u044f\u0450\5T+\2\u0450")
        buf.write(u"e\3\2\2\2\u0451\u0452\7\u0081\2\2\u0452\u0453\7g\2\2")
        buf.write(u"\u0453\u0454\5T+\2\u0454g\3\2\2\2\u0455\u0456\7\u0098")
        buf.write(u"\2\2\u0456\u0457\5T+\2\u0457\u0458\7\u0091\2\2\u0458")
        buf.write(u"\u0459\5T+\2\u0459i\3\2\2\2\u045a\u045b\7d\2\2\u045b")
        buf.write(u"\u045c\5\u00acW\2\u045c\u045d\7g\2\2\u045d\u045e\5T+")
        buf.write(u"\2\u045e\u045f\7\u0096\2\2\u045f\u0460\5T+\2\u0460\u0480")
        buf.write(u"\3\2\2\2\u0461\u0462\7d\2\2\u0462\u0464\7y\2\2\u0463")
        buf.write(u"\u0465\5\u00a0Q\2\u0464\u0463\3\2\2\2\u0464\u0465\3\2")
        buf.write(u"\2\2\u0465\u0466\3\2\2\2\u0466\u0467\7\u0096\2\2\u0467")
        buf.write(u"\u0480\5T+\2\u0468\u046f\7d\2\2\u0469\u0470\7D\2\2\u046a")
        buf.write(u"\u046b\7\u0086\2\2\u046b\u046c\5T+\2\u046c\u046d\7\u0091")
        buf.write(u"\2\2\u046d\u046e\5T+\2\u046e\u0470\3\2\2\2\u046f\u0469")
        buf.write(u"\3\2\2\2\u046f\u046a\3\2\2\2\u0470\u0471\3\2\2\2\u0471")
        buf.write(u"\u0473\7\26\2\2\u0472\u0474\5\u00a0Q\2\u0473\u0472\3")
        buf.write(u"\2\2\2\u0473\u0474\3\2\2\2\u0474\u0475\3\2\2\2\u0475")
        buf.write(u"\u0478\7\27\2\2\u0476\u0477\7\u0096\2\2\u0477\u0479\5")
        buf.write(u"T+\2\u0478\u0476\3\2\2\2\u0478\u0479\3\2\2\2\u0479\u047d")
        buf.write(u"\3\2\2\2\u047a\u047b\7}\2\2\u047b\u047c\7N\2\2\u047c")
        buf.write(u"\u047e\5\u010c\u0087\2\u047d\u047a\3\2\2\2\u047d\u047e")
        buf.write(u"\3\2\2\2\u047e\u0480\3\2\2\2\u047f\u045a\3\2\2\2\u047f")
        buf.write(u"\u0461\3\2\2\2\u047f\u0468\3\2\2\2\u0480k\3\2\2\2\u0481")
        buf.write(u"\u0482\7\u008a\2\2\u0482\u0483\7\26\2\2\u0483\u0489\5")
        buf.write(u"X-\2\u0484\u0485\7\23\2\2\u0485\u0486\5\u0114\u008b\2")
        buf.write(u"\u0486\u0487\7-\2\2\u0487\u0488\5X-\2\u0488\u048a\3\2")
        buf.write(u"\2\2\u0489\u0484\3\2\2\2\u0489\u048a\3\2\2\2\u048a\u048b")
        buf.write(u"\3\2\2\2\u048b\u048c\7\27\2\2\u048cm\3\2\2\2\u048d\u048e")
        buf.write(u"\5\u0108\u0085\2\u048e\u048f\5\u011a\u008e\2\u048f\u0490")
        buf.write(u"\5T+\2\u0490o\3\2\2\2\u0491\u0492\69&\3\u0492\u0493\7")
        buf.write(u"\25\2\2\u0493\u049a\5\u00acW\2\u0494\u0495\69\'\3\u0495")
        buf.write(u"\u0496\7\30\2\2\u0496\u0497\5T+\2\u0497\u0498\7\31\2")
        buf.write(u"\2\u0498\u049a\3\2\2\2\u0499\u0491\3\2\2\2\u0499\u0494")
        buf.write(u"\3\2\2\2\u049aq\3\2\2\2\u049b\u049c\5\u00d4k\2\u049c")
        buf.write(u"\u049d\5\u011a\u008e\2\u049d\u049e\5T+\2\u049es\3\2\2")
        buf.write(u"\2\u049f\u04a1\7\7\2\2\u04a0\u049f\3\2\2\2\u04a1\u04a4")
        buf.write(u"\3\2\2\2\u04a2\u04a0\3\2\2\2\u04a2\u04a3\3\2\2\2\u04a3")
        buf.write(u"u\3\2\2\2\u04a4\u04a2\3\2\2\2\u04a5\u04a7\7\7\2\2\u04a6")
        buf.write(u"\u04a5\3\2\2\2\u04a7\u04a8\3\2\2\2\u04a8\u04a6\3\2\2")
        buf.write(u"\2\u04a8\u04a9\3\2\2\2\u04a9w\3\2\2\2\u04aa\u04ac\7\7")
        buf.write(u"\2\2\u04ab\u04aa\3\2\2\2\u04ac\u04ad\3\2\2\2\u04ad\u04ab")
        buf.write(u"\3\2\2\2\u04ad\u04ae\3\2\2\2\u04ae\u04af\3\2\2\2\u04af")
        buf.write(u"\u04b0\7\3\2\2\u04b0y\3\2\2\2\u04b1\u04b3\7\7\2\2\u04b2")
        buf.write(u"\u04b1\3\2\2\2\u04b3\u04b6\3\2\2\2\u04b4\u04b2\3\2\2")
        buf.write(u"\2\u04b4\u04b5\3\2\2\2\u04b5\u04b7\3\2\2\2\u04b6\u04b4")
        buf.write(u"\3\2\2\2\u04b7\u04b8\7\4\2\2\u04b8{\3\2\2\2\u04b9\u04ba")
        buf.write(u"\7t\2\2\u04ba}\3\2\2\2\u04bb\u04bd\5\u0080A\2\u04bc\u04bb")
        buf.write(u"\3\2\2\2\u04bc\u04bd\3\2\2\2\u04bd\u04be\3\2\2\2\u04be")
        buf.write(u"\u04bf\5t;\2\u04bf\u04c0\7\2\2\3\u04c0\177\3\2\2\2\u04c1")
        buf.write(u"\u04c2\bA\1\2\u04c2\u04c3\5\u0082B\2\u04c3\u04ca\3\2")
        buf.write(u"\2\2\u04c4\u04c5\f\3\2\2\u04c5\u04c6\5v<\2\u04c6\u04c7")
        buf.write(u"\5\u0082B\2\u04c7\u04c9\3\2\2\2\u04c8\u04c4\3\2\2\2\u04c9")
        buf.write(u"\u04cc\3\2\2\2\u04ca\u04c8\3\2\2\2\u04ca\u04cb\3\2\2")
        buf.write(u"\2\u04cb\u0081\3\2\2\2\u04cc\u04ca\3\2\2\2\u04cd\u04ce")
        buf.write(u"\5\u00d8m\2\u04ce\u04cf\5v<\2\u04cf\u04d1\3\2\2\2\u04d0")
        buf.write(u"\u04cd\3\2\2\2\u04d1\u04d4\3\2\2\2\u04d2\u04d0\3\2\2")
        buf.write(u"\2\u04d2\u04d3\3\2\2\2\u04d3\u04da\3\2\2\2\u04d4\u04d2")
        buf.write(u"\3\2\2\2\u04d5\u04db\5\n\6\2\u04d6\u04db\5\u00a4S\2\u04d7")
        buf.write(u"\u04db\5\u0084C\2\u04d8\u04db\5\u0086D\2\u04d9\u04db")
        buf.write(u"\5\u00d6l\2\u04da\u04d5\3\2\2\2\u04da\u04d6\3\2\2\2\u04da")
        buf.write(u"\u04d7\3\2\2\2\u04da\u04d8\3\2\2\2\u04da\u04d9\3\2\2")
        buf.write(u"\2\u04db\u0083\3\2\2\2\u04dc\u04dd\5\32\16\2\u04dd\u0085")
        buf.write(u"\3\2\2\2\u04de\u04e1\5\2\2\2\u04df\u04e1\5\4\3\2\u04e0")
        buf.write(u"\u04de\3\2\2\2\u04e0\u04df\3\2\2\2\u04e1\u0087\3\2\2")
        buf.write(u"\2\u04e2\u04e3\bE\1\2\u04e3\u04e4\5\6\4\2\u04e4\u04eb")
        buf.write(u"\3\2\2\2\u04e5\u04e6\f\3\2\2\u04e6\u04e7\5v<\2\u04e7")
        buf.write(u"\u04e8\5\6\4\2\u04e8\u04ea\3\2\2\2\u04e9\u04e5\3\2\2")
        buf.write(u"\2\u04ea\u04ed\3\2\2\2\u04eb\u04e9\3\2\2\2\u04eb\u04ec")
        buf.write(u"\3\2\2\2\u04ec\u0089\3\2\2\2\u04ed\u04eb\3\2\2\2\u04ee")
        buf.write(u"\u04ef\bF\1\2\u04ef\u04f0\5\b\5\2\u04f0\u04f7\3\2\2\2")
        buf.write(u"\u04f1\u04f2\f\3\2\2\u04f2\u04f3\5v<\2\u04f3\u04f4\5")
        buf.write(u"\b\5\2\u04f4\u04f6\3\2\2\2\u04f5\u04f1\3\2\2\2\u04f6")
        buf.write(u"\u04f9\3\2\2\2\u04f7\u04f5\3\2\2\2\u04f7\u04f8\3\2\2")
        buf.write(u"\2\u04f8\u008b\3\2\2\2\u04f9\u04f7\3\2\2\2\u04fa\u04fb")
        buf.write(u"\bG\1\2\u04fb\u04fc\5\u00b0Y\2\u04fc\u0502\3\2\2\2\u04fd")
        buf.write(u"\u04fe\f\3\2\2\u04fe\u04ff\7\23\2\2\u04ff\u0501\5\u00b0")
        buf.write(u"Y\2\u0500\u04fd\3\2\2\2\u0501\u0504\3\2\2\2\u0502\u0500")
        buf.write(u"\3\2\2\2\u0502\u0503\3\2\2\2\u0503\u008d\3\2\2\2\u0504")
        buf.write(u"\u0502\3\2\2\2\u0505\u0506\7j\2\2\u0506\u0510\5\u0090")
        buf.write(u"I\2\u0507\u0508\7j\2\2\u0508\u0510\5\u0092J\2\u0509\u050a")
        buf.write(u"\7j\2\2\u050a\u0510\5\u0096L\2\u050b\u050c\7n\2\2\u050c")
        buf.write(u"\u0510\7\u00a2\2\2\u050d\u050e\7n\2\2\u050e\u0510\5T")
        buf.write(u"+\2\u050f\u0505\3\2\2\2\u050f\u0507\3\2\2\2\u050f\u0509")
        buf.write(u"\3\2\2\2\u050f\u050b\3\2\2\2\u050f\u050d\3\2\2\2\u0510")
        buf.write(u"\u008f\3\2\2\2\u0511\u0513\7\30\2\2\u0512\u0514\5\u0094")
        buf.write(u"K\2\u0513\u0512\3\2\2\2\u0513\u0514\3\2\2\2\u0514\u0515")
        buf.write(u"\3\2\2\2\u0515\u0516\7\31\2\2\u0516\u0091\3\2\2\2\u0517")
        buf.write(u"\u0519\7*\2\2\u0518\u051a\5\u0094K\2\u0519\u0518\3\2")
        buf.write(u"\2\2\u0519\u051a\3\2\2\2\u051a\u051b\3\2\2\2\u051b\u051c")
        buf.write(u"\7(\2\2\u051c\u0093\3\2\2\2\u051d\u051e\bK\1\2\u051e")
        buf.write(u"\u051f\5T+\2\u051f\u0525\3\2\2\2\u0520\u0521\f\3\2\2")
        buf.write(u"\u0521\u0522\7\23\2\2\u0522\u0524\5T+\2\u0523\u0520\3")
        buf.write(u"\2\2\2\u0524\u0527\3\2\2\2\u0525\u0523\3\2\2\2\u0525")
        buf.write(u"\u0526\3\2\2\2\u0526\u0095\3\2\2\2\u0527\u0525\3\2\2")
        buf.write(u"\2\u0528\u0529\7\30\2\2\u0529\u052a\5T+\2\u052a\u052b")
        buf.write(u"\7\24\2\2\u052b\u052c\5T+\2\u052c\u052d\7\31\2\2\u052d")
        buf.write(u"\u0097\3\2\2\2\u052e\u052f\bM\1\2\u052f\u0530\5\u009a")
        buf.write(u"N\2\u0530\u053b\3\2\2\2\u0531\u0532\f\5\2\2\u0532\u053a")
        buf.write(u"\7,\2\2\u0533\u0534\f\4\2\2\u0534\u0535\7\30\2\2\u0535")
        buf.write(u"\u053a\7\31\2\2\u0536\u0537\f\3\2\2\u0537\u0538\7\32")
        buf.write(u"\2\2\u0538\u053a\7\33\2\2\u0539\u0531\3\2\2\2\u0539\u0533")
        buf.write(u"\3\2\2\2\u0539\u0536\3\2\2\2\u053a\u053d\3\2\2\2\u053b")
        buf.write(u"\u0539\3\2\2\2\u053b\u053c\3\2\2\2\u053c\u0099\3\2\2")
        buf.write(u"\2\u053d\u053b\3\2\2\2\u053e\u0541\5\u009cO\2\u053f\u0541")
        buf.write(u"\5\u009eP\2\u0540\u053e\3\2\2\2\u0540\u053f\3\2\2\2\u0541")
        buf.write(u"\u009b\3\2\2\2\u0542\u0551\7\64\2\2\u0543\u0551\7\65")
        buf.write(u"\2\2\u0544\u0551\7\66\2\2\u0545\u0551\7A\2\2\u0546\u0551")
        buf.write(u"\7\67\2\2\u0547\u0551\78\2\2\u0548\u0551\7?\2\2\u0549")
        buf.write(u"\u0551\79\2\2\u054a\u0551\7;\2\2\u054b\u0551\7:\2\2\u054c")
        buf.write(u"\u0551\7<\2\2\u054d\u0551\7>\2\2\u054e\u0551\7@\2\2\u054f")
        buf.write(u"\u0551\7B\2\2\u0550\u0542\3\2\2\2\u0550\u0543\3\2\2\2")
        buf.write(u"\u0550\u0544\3\2\2\2\u0550\u0545\3\2\2\2\u0550\u0546")
        buf.write(u"\3\2\2\2\u0550\u0547\3\2\2\2\u0550\u0548\3\2\2\2\u0550")
        buf.write(u"\u0549\3\2\2\2\u0550\u054a\3\2\2\2\u0550\u054b\3\2\2")
        buf.write(u"\2\u0550\u054c\3\2\2\2\u0550\u054d\3\2\2\2\u0550\u054e")
        buf.write(u"\3\2\2\2\u0550\u054f\3\2\2\2\u0551\u009d\3\2\2\2\u0552")
        buf.write(u"\u0553\7\u009e\2\2\u0553\u009f\3\2\2\2\u0554\u0556\7")
        buf.write(u"r\2\2\u0555\u0554\3\2\2\2\u0555\u0556\3\2\2\2\u0556\u0557")
        buf.write(u"\3\2\2\2\u0557\u0558\5\u009eP\2\u0558\u00a1\3\2\2\2\u0559")
        buf.write(u"\u055a\7>\2\2\u055a\u00a3\3\2\2\2\u055b\u055f\5\f\7\2")
        buf.write(u"\u055c\u055f\5\30\r\2\u055d\u055f\5\16\b\2\u055e\u055b")
        buf.write(u"\3\2\2\2\u055e\u055c\3\2\2\2\u055e\u055d\3\2\2\2\u055f")
        buf.write(u"\u00a5\3\2\2\2\u0560\u0561\bT\1\2\u0561\u0562\5\u00ae")
        buf.write(u"X\2\u0562\u0568\3\2\2\2\u0563\u0564\f\3\2\2\u0564\u0565")
        buf.write(u"\7\23\2\2\u0565\u0567\5\u00aeX\2\u0566\u0563\3\2\2\2")
        buf.write(u"\u0567\u056a\3\2\2\2\u0568\u0566\3\2\2\2\u0568\u0569")
        buf.write(u"\3\2\2\2\u0569\u00a7\3\2\2\2\u056a\u0568\3\2\2\2\u056b")
        buf.write(u"\u056e\5\u00acW\2\u056c\u056e\5\u00aeX\2\u056d\u056b")
        buf.write(u"\3\2\2\2\u056d\u056c\3\2\2\2\u056e\u00a9\3\2\2\2\u056f")
        buf.write(u"\u0573\5\u00acW\2\u0570\u0573\5\u00aeX\2\u0571\u0573")
        buf.write(u"\5\u00b0Y\2\u0572\u056f\3\2\2\2\u0572\u0570\3\2\2\2\u0572")
        buf.write(u"\u0571\3\2\2\2\u0573\u00ab\3\2\2\2\u0574\u0575\7\u009f")
        buf.write(u"\2\2\u0575\u00ad\3\2\2\2\u0576\u0577\7\u009e\2\2\u0577")
        buf.write(u"\u00af\3\2\2\2\u0578\u0579\7\u009d\2\2\u0579\u00b1\3")
        buf.write(u"\2\2\2\u057a\u057b\bZ\1\2\u057b\u057c\5\u00b4[\2\u057c")
        buf.write(u"\u0582\3\2\2\2\u057d\u057e\f\3\2\2\u057e\u057f\7\23\2")
        buf.write(u"\2\u057f\u0581\5\u00b4[\2\u0580\u057d\3\2\2\2\u0581\u0584")
        buf.write(u"\3\2\2\2\u0582\u0580\3\2\2\2\u0582\u0583\3\2\2\2\u0583")
        buf.write(u"\u00b3\3\2\2\2\u0584\u0582\3\2\2\2\u0585\u058b\5\u00ba")
        buf.write(u"^\2\u0586\u0588\7r\2\2\u0587\u0586\3\2\2\2\u0587\u0588")
        buf.write(u"\3\2\2\2\u0588\u0589\3\2\2\2\u0589\u058b\5\u00b6\\\2")
        buf.write(u"\u058a\u0585\3\2\2\2\u058a\u0587\3\2\2\2\u058b\u00b5")
        buf.write(u"\3\2\2\2\u058c\u058f\5\u00b8]\2\u058d\u058f\5,\27\2\u058e")
        buf.write(u"\u058c\3\2\2\2\u058e\u058d\3\2\2\2\u058f\u00b7\3\2\2")
        buf.write(u"\2\u0590\u0593\5\u00acW\2\u0591\u0592\7-\2\2\u0592\u0594")
        buf.write(u"\5\u00f6|\2\u0593\u0591\3\2\2\2\u0593\u0594\3\2\2\2\u0594")
        buf.write(u"\u00b9\3\2\2\2\u0595\u0596\5\u00a2R\2\u0596\u0597\5\u00ac")
        buf.write(u"W\2\u0597\u00bb\3\2\2\2\u0598\u059b\5\u0098M\2\u0599")
        buf.write(u"\u059b\5\u00be`\2\u059a\u0598\3\2\2\2\u059a\u0599\3\2")
        buf.write(u"\2\2\u059b\u00bd\3\2\2\2\u059c\u059d\b`\1\2\u059d\u059e")
        buf.write(u"\7G\2\2\u059e\u05a7\3\2\2\2\u059f\u05a0\f\4\2\2\u05a0")
        buf.write(u"\u05a1\7\30\2\2\u05a1\u05a6\7\31\2\2\u05a2\u05a3\f\3")
        buf.write(u"\2\2\u05a3\u05a4\7\32\2\2\u05a4\u05a6\7\33\2\2\u05a5")
        buf.write(u"\u059f\3\2\2\2\u05a5\u05a2\3\2\2\2\u05a6\u05a9\3\2\2")
        buf.write(u"\2\u05a7\u05a5\3\2\2\2\u05a7\u05a8\3\2\2\2\u05a8\u00bf")
        buf.write(u"\3\2\2\2\u05a9\u05a7\3\2\2\2\u05aa\u05ab\ba\1\2\u05ab")
        buf.write(u"\u05ac\5\u00c2b\2\u05ac\u05b3\3\2\2\2\u05ad\u05ae\f\3")
        buf.write(u"\2\2\u05ae\u05af\5v<\2\u05af\u05b0\5\u00c2b\2\u05b0\u05b2")
        buf.write(u"\3\2\2\2\u05b1\u05ad\3\2\2\2\u05b2\u05b5\3\2\2\2\u05b3")
        buf.write(u"\u05b1\3\2\2\2\u05b3\u05b4\3\2\2\2\u05b4\u00c1\3\2\2")
        buf.write(u"\2\u05b5\u05b3\3\2\2\2\u05b6\u05bc\5\24\13\2\u05b7\u05bc")
        buf.write(u"\5\26\f\2\u05b8\u05bc\5$\23\2\u05b9\u05bc\5\"\22\2\u05ba")
        buf.write(u"\u05bc\5\22\n\2\u05bb\u05b6\3\2\2\2\u05bb\u05b7\3\2\2")
        buf.write(u"\2\u05bb\u05b8\3\2\2\2\u05bb\u05b9\3\2\2\2\u05bb\u05ba")
        buf.write(u"\3\2\2\2\u05bc\u00c3\3\2\2\2\u05bd\u05be\bc\1\2\u05be")
        buf.write(u"\u05bf\5\u00c6d\2\u05bf\u05c6\3\2\2\2\u05c0\u05c1\f\3")
        buf.write(u"\2\2\u05c1\u05c2\5v<\2\u05c2\u05c3\5\u00c6d\2\u05c3\u05c5")
        buf.write(u"\3\2\2\2\u05c4\u05c0\3\2\2\2\u05c5\u05c8\3\2\2\2\u05c6")
        buf.write(u"\u05c4\3\2\2\2\u05c6\u05c7\3\2\2\2\u05c7\u00c5\3\2\2")
        buf.write(u"\2\u05c8\u05c6\3\2\2\2\u05c9\u05cc\5\u00c2b\2\u05ca\u05cc")
        buf.write(u"\5&\24\2\u05cb\u05c9\3\2\2\2\u05cb\u05ca\3\2\2\2\u05cc")
        buf.write(u"\u00c7\3\2\2\2\u05cd\u05ce\7\13\2\2\u05ce\u05d8\5\u016c")
        buf.write(u"\u00b7\2\u05cf\u05d0\7\f\2\2\u05d0\u05d8\5\u0186\u00c4")
        buf.write(u"\2\u05d1\u05d2\7\r\2\2\u05d2\u05d8\5\u00caf\2\u05d3\u05d4")
        buf.write(u"\7\16\2\2\u05d4\u05d8\5\u00caf\2\u05d5\u05d6\7\17\2\2")
        buf.write(u"\u05d6\u05d8\5\u00d0i\2\u05d7\u05cd\3\2\2\2\u05d7\u05cf")
        buf.write(u"\3\2\2\2\u05d7\u05d1\3\2\2\2\u05d7\u05d3\3\2\2\2\u05d7")
        buf.write(u"\u05d5\3\2\2\2\u05d8\u00c9\3\2\2\2\u05d9\u05db\5\u00aa")
        buf.write(u"V\2\u05da\u05dc\5\u00ccg\2\u05db\u05da\3\2\2\2\u05db")
        buf.write(u"\u05dc\3\2\2\2\u05dc\u00cb\3\2\2\2\u05dd\u05de\7g\2\2")
        buf.write(u"\u05de\u05df\5\u00ceh\2\u05df\u05e0\7\21\2\2\u05e0\u05e5")
        buf.write(u"\5\u00aaV\2\u05e1\u05e2\7\25\2\2\u05e2\u05e4\5\u00aa")
        buf.write(u"V\2\u05e3\u05e1\3\2\2\2\u05e4\u05e7\3\2\2\2\u05e5\u05e3")
        buf.write(u"\3\2\2\2\u05e5\u05e6\3\2\2\2\u05e6\u00cd\3\2\2\2\u05e7")
        buf.write(u"\u05e5\3\2\2\2\u05e8\u05e9\7\u009f\2\2\u05e9\u05ea\6")
        buf.write(u"h\66\3\u05ea\u00cf\3\2\2\2\u05eb\u05ed\5\u00aaV\2\u05ec")
        buf.write(u"\u05ee\5\u00d2j\2\u05ed\u05ec\3\2\2\2\u05ed\u05ee\3\2")
        buf.write(u"\2\2\u05ee\u00d1\3\2\2\2\u05ef\u05f0\7g\2\2\u05f0\u05f1")
        buf.write(u"\5\u00ceh\2\u05f1\u05f3\7\21\2\2\u05f2\u05f4\7%\2\2\u05f3")
        buf.write(u"\u05f2\3\2\2\2\u05f3\u05f4\3\2\2\2\u05f4\u05f5\3\2\2")
        buf.write(u"\2\u05f5\u05fa\5\u013c\u009f\2\u05f6\u05f7\7%\2\2\u05f7")
        buf.write(u"\u05f9\5\u013c\u009f\2\u05f8\u05f6\3\2\2\2\u05f9\u05fc")
        buf.write(u"\3\2\2\2\u05fa\u05f8\3\2\2\2\u05fa\u05fb\3\2\2\2\u05fb")
        buf.write(u"\u05ff\3\2\2\2\u05fc\u05fa\3\2\2\2\u05fd\u05fe\7\25\2")
        buf.write(u"\2\u05fe\u0600\5\u013c\u009f\2\u05ff\u05fd\3\2\2\2\u05ff")
        buf.write(u"\u0600\3\2\2\2\u0600\u00d3\3\2\2\2\u0601\u0602\bk\1\2")
        buf.write(u"\u0602\u0603\5\u00acW\2\u0603\u0609\3\2\2\2\u0604\u0605")
        buf.write(u"\f\3\2\2\u0605\u0606\7\23\2\2\u0606\u0608\5\u00acW\2")
        buf.write(u"\u0607\u0604\3\2\2\2\u0608\u060b\3\2\2\2\u0609\u0607")
        buf.write(u"\3\2\2\2\u0609\u060a\3\2\2\2\u060a\u00d5\3\2\2\2\u060b")
        buf.write(u"\u0609\3\2\2\2\u060c\u0611\5\"\22\2\u060d\u0611\5$\23")
        buf.write(u"\2\u060e\u0611\5&\24\2\u060f\u0611\5(\25\2\u0610\u060c")
        buf.write(u"\3\2\2\2\u0610\u060d\3\2\2\2\u0610\u060e\3\2\2\2\u0610")
        buf.write(u"\u060f\3\2\2\2\u0611\u00d7\3\2\2\2\u0612\u0613\7\n\2")
        buf.write(u"\2\u0613\u00d9\3\2\2\2\u0614\u0615\bn\1\2\u0615\u0616")
        buf.write(u"\5\u00dco\2\u0616\u061d\3\2\2\2\u0617\u0618\f\3\2\2\u0618")
        buf.write(u"\u0619\5v<\2\u0619\u061a\5\u00dco\2\u061a\u061c\3\2\2")
        buf.write(u"\2\u061b\u0617\3\2\2\2\u061c\u061f\3\2\2\2\u061d\u061b")
        buf.write(u"\3\2\2\2\u061d\u061e\3\2\2\2\u061e\u00db\3\2\2\2\u061f")
        buf.write(u"\u061d\3\2\2\2\u0620\u0621\7\13\2\2\u0621\u062b\5\u0156")
        buf.write(u"\u00ac\2\u0622\u0623\7\f\2\2\u0623\u062b\5\u0172\u00ba")
        buf.write(u"\2\u0624\u0625\7\r\2\2\u0625\u062b\5\u00dep\2\u0626\u0627")
        buf.write(u"\7\16\2\2\u0627\u062b\5\u00dep\2\u0628\u0629\7\17\2\2")
        buf.write(u"\u0629\u062b\5\u00e0q\2\u062a\u0620\3\2\2\2\u062a\u0622")
        buf.write(u"\3\2\2\2\u062a\u0624\3\2\2\2\u062a\u0626\3\2\2\2\u062a")
        buf.write(u"\u0628\3\2\2\2\u062b\u00dd\3\2\2\2\u062c\u062e\5\u013e")
        buf.write(u"\u00a0\2\u062d\u062f\7\22\2\2\u062e\u062d\3\2\2\2\u062e")
        buf.write(u"\u062f\3\2\2\2\u062f\u0631\3\2\2\2\u0630\u0632\5\u00cc")
        buf.write(u"g\2\u0631\u0630\3\2\2\2\u0631\u0632\3\2\2\2\u0632\u00df")
        buf.write(u"\3\2\2\2\u0633\u0635\5\u0124\u0093\2\u0634\u0636\7\22")
        buf.write(u"\2\2\u0635\u0634\3\2\2\2\u0635\u0636\3\2\2\2\u0636\u0638")
        buf.write(u"\3\2\2\2\u0637\u0639\5\u00d2j\2\u0638\u0637\3\2\2\2\u0638")
        buf.write(u"\u0639\3\2\2\2\u0639\u00e1\3\2\2\2\u063a\u063b\br\1\2")
        buf.write(u"\u063b\u063c\5.\30\2\u063c\u0643\3\2\2\2\u063d\u063e")
        buf.write(u"\f\3\2\2\u063e\u063f\5v<\2\u063f\u0640\5.\30\2\u0640")
        buf.write(u"\u0642\3\2\2\2\u0641\u063d\3\2\2\2\u0642\u0645\3\2\2")
        buf.write(u"\2\u0643\u0641\3\2\2\2\u0643\u0644\3\2\2\2\u0644\u00e3")
        buf.write(u"\3\2\2\2\u0645\u0643\3\2\2\2\u0646\u0647\bs\1\2\u0647")
        buf.write(u"\u0648\5*\26\2\u0648\u064f\3\2\2\2\u0649\u064a\f\3\2")
        buf.write(u"\2\u064a\u064b\5v<\2\u064b\u064c\5*\26\2\u064c\u064e")
        buf.write(u"\3\2\2\2\u064d\u0649\3\2\2\2\u064e\u0651\3\2\2\2\u064f")
        buf.write(u"\u064d\3\2\2\2\u064f\u0650\3\2\2\2\u0650\u00e5\3\2\2")
        buf.write(u"\2\u0651\u064f\3\2\2\2\u0652\u0653\bt\1\2\u0653\u0654")
        buf.write(u"\5@!\2\u0654\u065b\3\2\2\2\u0655\u0656\f\3\2\2\u0656")
        buf.write(u"\u0657\5v<\2\u0657\u0658\5@!\2\u0658\u065a\3\2\2\2\u0659")
        buf.write(u"\u0655\3\2\2\2\u065a\u065d\3\2\2\2\u065b\u0659\3\2\2")
        buf.write(u"\2\u065b\u065c\3\2\2\2\u065c\u00e7\3\2\2\2\u065d\u065b")
        buf.write(u"\3\2\2\2\u065e\u065f\bu\1\2\u065f\u0660\5P)\2\u0660\u0667")
        buf.write(u"\3\2\2\2\u0661\u0662\f\3\2\2\u0662\u0663\5v<\2\u0663")
        buf.write(u"\u0664\5P)\2\u0664\u0666\3\2\2\2\u0665\u0661\3\2\2\2")
        buf.write(u"\u0666\u0669\3\2\2\2\u0667\u0665\3\2\2\2\u0667\u0668")
        buf.write(u"\3\2\2\2\u0668\u00e9\3\2\2\2\u0669\u0667\3\2\2\2\u066a")
        buf.write(u"\u066b\7\30\2\2\u066b\u066c\5\u00ecw\2\u066c\u066d\7")
        buf.write(u"\24\2\2\u066d\u066e\5\u00ecw\2\u066e\u066f\7\31\2\2\u066f")
        buf.write(u"\u0679\3\2\2\2\u0670\u0671\7\30\2\2\u0671\u0672\5\u00ee")
        buf.write(u"x\2\u0672\u0673\7\31\2\2\u0673\u0679\3\2\2\2\u0674\u0675")
        buf.write(u"\7*\2\2\u0675\u0676\5\u00eex\2\u0676\u0677\7(\2\2\u0677")
        buf.write(u"\u0679\3\2\2\2\u0678\u066a\3\2\2\2\u0678\u0670\3\2\2")
        buf.write(u"\2\u0678\u0674\3\2\2\2\u0679\u00eb\3\2\2\2\u067a\u0688")
        buf.write(u"\7\u009b\2\2\u067b\u0688\7\u009c\2\2\u067c\u0688\7\u00a3")
        buf.write(u"\2\2\u067d\u0688\7\u00a4\2\2\u067e\u0688\7\u009a\2\2")
        buf.write(u"\u067f\u0688\7\u00a8\2\2\u0680\u0688\7\u00a7\2\2\u0681")
        buf.write(u"\u0688\7\u00a2\2\2\u0682\u0688\7\u00a5\2\2\u0683\u0688")
        buf.write(u"\7\u00a6\2\2\u0684\u0688\7\u0099\2\2\u0685\u0688\7\u00a9")
        buf.write(u"\2\2\u0686\u0688\5|?\2\u0687\u067a\3\2\2\2\u0687\u067b")
        buf.write(u"\3\2\2\2\u0687\u067c\3\2\2\2\u0687\u067d\3\2\2\2\u0687")
        buf.write(u"\u067e\3\2\2\2\u0687\u067f\3\2\2\2\u0687\u0680\3\2\2")
        buf.write(u"\2\u0687\u0681\3\2\2\2\u0687\u0682\3\2\2\2\u0687\u0683")
        buf.write(u"\3\2\2\2\u0687\u0684\3\2\2\2\u0687\u0685\3\2\2\2\u0687")
        buf.write(u"\u0686\3\2\2\2\u0688\u00ed\3\2\2\2\u0689\u068a\bx\1\2")
        buf.write(u"\u068a\u068b\5\u00ecw\2\u068b\u0691\3\2\2\2\u068c\u068d")
        buf.write(u"\f\3\2\2\u068d\u068e\7\23\2\2\u068e\u0690\5\u00ecw\2")
        buf.write(u"\u068f\u068c\3\2\2\2\u0690\u0693\3\2\2\2\u0691\u068f")
        buf.write(u"\3\2\2\2\u0691\u0692\3\2\2\2\u0692\u00ef\3\2\2\2\u0693")
        buf.write(u"\u0691\3\2\2\2\u0694\u0699\5\u00f4{\2\u0695\u0699\5\u00f6")
        buf.write(u"|\2\u0696\u0699\5\u00aaV\2\u0697\u0699\5\u00f2z\2\u0698")
        buf.write(u"\u0694\3\2\2\2\u0698\u0695\3\2\2\2\u0698\u0696\3\2\2")
        buf.write(u"\2\u0698\u0697\3\2\2\2\u0699\u00f1\3\2\2\2\u069a\u069b")
        buf.write(u"\t\4\2\2\u069b\u00f3\3\2\2\2\u069c\u069d\7\26\2\2\u069d")
        buf.write(u"\u069e\5T+\2\u069e\u069f\7\27\2\2\u069f\u00f5\3\2\2\2")
        buf.write(u"\u06a0\u06a3\5\u00ecw\2\u06a1\u06a3\5\u00f8}\2\u06a2")
        buf.write(u"\u06a0\3\2\2\2\u06a2\u06a1\3\2\2\2\u06a3\u00f7\3\2\2")
        buf.write(u"\2\u06a4\u06aa\5\u0096L\2\u06a5\u06aa\5\u0090I\2\u06a6")
        buf.write(u"\u06aa\5\u0092J\2\u06a7\u06aa\5\u00fc\177\2\u06a8\u06aa")
        buf.write(u"\5\u00fa~\2\u06a9\u06a4\3\2\2\2\u06a9\u06a5\3\2\2\2\u06a9")
        buf.write(u"\u06a6\3\2\2\2\u06a9\u06a7\3\2\2\2\u06a9\u06a8\3\2\2")
        buf.write(u"\2\u06aa\u00f9\3\2\2\2\u06ab\u06ad\7\26\2\2\u06ac\u06ae")
        buf.write(u"\5\u00fe\u0080\2\u06ad\u06ac\3\2\2\2\u06ad\u06ae\3\2")
        buf.write(u"\2\2\u06ae\u06af\3\2\2\2\u06af\u06b0\7\27\2\2\u06b0\u00fb")
        buf.write(u"\3\2\2\2\u06b1\u06b3\7\32\2\2\u06b2\u06b4\5\u0100\u0081")
        buf.write(u"\2\u06b3\u06b2\3\2\2\2\u06b3\u06b4\3\2\2\2\u06b4\u06b5")
        buf.write(u"\3\2\2\2\u06b5\u06b6\7\33\2\2\u06b6\u00fd\3\2\2\2\u06b7")
        buf.write(u"\u06b8\b\u0080\1\2\u06b8\u06b9\5T+\2\u06b9\u06bf\3\2")
        buf.write(u"\2\2\u06ba\u06bb\f\3\2\2\u06bb\u06bc\7\23\2\2\u06bc\u06be")
        buf.write(u"\5T+\2\u06bd\u06ba\3\2\2\2\u06be\u06c1\3\2\2\2\u06bf")
        buf.write(u"\u06bd\3\2\2\2\u06bf\u06c0\3\2\2\2\u06c0\u00ff\3\2\2")
        buf.write(u"\2\u06c1\u06bf\3\2\2\2\u06c2\u06c3\b\u0081\1\2\u06c3")
        buf.write(u"\u06c4\5\u0102\u0082\2\u06c4\u06ca\3\2\2\2\u06c5\u06c6")
        buf.write(u"\f\3\2\2\u06c6\u06c7\7\23\2\2\u06c7\u06c9\5\u0102\u0082")
        buf.write(u"\2\u06c8\u06c5\3\2\2\2\u06c9\u06cc\3\2\2\2\u06ca\u06c8")
        buf.write(u"\3\2\2\2\u06ca\u06cb\3\2\2\2\u06cb\u0101\3\2\2\2\u06cc")
        buf.write(u"\u06ca\3\2\2\2\u06cd\u06ce\5T+\2\u06ce\u06cf\7\21\2\2")
        buf.write(u"\u06cf\u06d0\5T+\2\u06d0\u0103\3\2\2\2\u06d1\u06d2\5")
        buf.write(u"T+\2\u06d2\u06d3\7\21\2\2\u06d3\u06d4\5T+\2\u06d4\u06db")
        buf.write(u"\3\2\2\2\u06d5\u06d6\5T+\2\u06d6\u06d7\7\21\2\2\u06d7")
        buf.write(u"\u06db\3\2\2\2\u06d8\u06d9\7\21\2\2\u06d9\u06db\5T+\2")
        buf.write(u"\u06da\u06d1\3\2\2\2\u06da\u06d5\3\2\2\2\u06da\u06d8")
        buf.write(u"\3\2\2\2\u06db\u0105\3\2\2\2\u06dc\u06dd\5\u00acW\2\u06dd")
        buf.write(u"\u06de\5\u011a\u008e\2\u06de\u06df\5T+\2\u06df\u0107")
        buf.write(u"\3\2\2\2\u06e0\u06e1\b\u0085\1\2\u06e1\u06e2\5\u00ac")
        buf.write(u"W\2\u06e2\u06e7\3\2\2\2\u06e3\u06e4\f\3\2\2\u06e4\u06e6")
        buf.write(u"\5p9\2\u06e5\u06e3\3\2\2\2\u06e6\u06e9\3\2\2\2\u06e7")
        buf.write(u"\u06e5\3\2\2\2\u06e7\u06e8\3\2\2\2\u06e8\u0109\3\2\2")
        buf.write(u"\2\u06e9\u06e7\3\2\2\2\u06ea\u06eb\6\u0086A\3\u06eb\u06ec")
        buf.write(u"\7\u009f\2\2\u06ec\u06ef\5\u00bc_\2\u06ed\u06ef\5T+\2")
        buf.write(u"\u06ee\u06ea\3\2\2\2\u06ee\u06ed\3\2\2\2\u06ef\u010b")
        buf.write(u"\3\2\2\2\u06f0\u06f5\5\u010e\u0088\2\u06f1\u06f2\7\23")
        buf.write(u"\2\2\u06f2\u06f4\5\u010e\u0088\2\u06f3\u06f1\3\2\2\2")
        buf.write(u"\u06f4\u06f7\3\2\2\2\u06f5\u06f3\3\2\2\2\u06f5\u06f6")
        buf.write(u"\3\2\2\2\u06f6\u010d\3\2\2\2\u06f7\u06f5\3\2\2\2\u06f8")
        buf.write(u"\u06fd\5\u00acW\2\u06f9\u06fa\7\25\2\2\u06fa\u06fc\5")
        buf.write(u"\u00acW\2\u06fb\u06f9\3\2\2\2\u06fc\u06ff\3\2\2\2\u06fd")
        buf.write(u"\u06fb\3\2\2\2\u06fd\u06fe\3\2\2\2\u06fe\u0701\3\2\2")
        buf.write(u"\2\u06ff\u06fd\3\2\2\2\u0700\u0702\t\5\2\2\u0701\u0700")
        buf.write(u"\3\2\2\2\u0701\u0702\3\2\2\2\u0702\u010f\3\2\2\2\u0703")
        buf.write(u"\u070a\7\"\2\2\u0704\u070a\7#\2\2\u0705\u070a\5\u011c")
        buf.write(u"\u008f\2\u0706\u070a\5\u011e\u0090\2\u0707\u070a\5\u0120")
        buf.write(u"\u0091\2\u0708\u070a\5\u0122\u0092\2\u0709\u0703\3\2")
        buf.write(u"\2\2\u0709\u0704\3\2\2\2\u0709\u0705\3\2\2\2\u0709\u0706")
        buf.write(u"\3\2\2\2\u0709\u0707\3\2\2\2\u0709\u0708\3\2\2\2\u070a")
        buf.write(u"\u0111\3\2\2\2\u070b\u070c\7\u009f\2\2\u070c\u070d\6")
        buf.write(u"\u008aB\3\u070d\u0113\3\2\2\2\u070e\u070f\7\u009f\2\2")
        buf.write(u"\u070f\u0710\6\u008bC\3\u0710\u0115\3\2\2\2\u0711\u0712")
        buf.write(u"\7\u009f\2\2\u0712\u0713\6\u008cD\3\u0713\u0117\3\2\2")
        buf.write(u"\2\u0714\u0715\7\u009f\2\2\u0715\u0716\6\u008dE\3\u0716")
        buf.write(u"\u0119\3\2\2\2\u0717\u0718\7-\2\2\u0718\u011b\3\2\2\2")
        buf.write(u"\u0719\u071a\7$\2\2\u071a\u011d\3\2\2\2\u071b\u071c\7")
        buf.write(u"%\2\2\u071c\u011f\3\2\2\2\u071d\u071e\7&\2\2\u071e\u0121")
        buf.write(u"\3\2\2\2\u071f\u0720\t\6\2\2\u0720\u0123\3\2\2\2\u0721")
        buf.write(u"\u0722\7\u0084\2\2\u0722\u0723\5\u0126\u0094\2\u0723")
        buf.write(u"\u0724\7\22\2\2\u0724\u0729\3\2\2\2\u0725\u0726\5\u0126")
        buf.write(u"\u0094\2\u0726\u0727\7\22\2\2\u0727\u0729\3\2\2\2\u0728")
        buf.write(u"\u0721\3\2\2\2\u0728\u0725\3\2\2\2\u0729\u0125\3\2\2")
        buf.write(u"\2\u072a\u072b\b\u0094\1\2\u072b\u072c\5\u0128\u0095")
        buf.write(u"\2\u072c\u0731\3\2\2\2\u072d\u072e\f\3\2\2\u072e\u0730")
        buf.write(u"\5\u012e\u0098\2\u072f\u072d\3\2\2\2\u0730\u0733\3\2")
        buf.write(u"\2\2\u0731\u072f\3\2\2\2\u0731\u0732\3\2\2\2\u0732\u0127")
        buf.write(u"\3\2\2\2\u0733\u0731\3\2\2\2\u0734\u073c\5\u012a\u0096")
        buf.write(u"\2\u0735\u073c\5\u012c\u0097\2\u0736\u073c\5\u0136\u009c")
        buf.write(u"\2\u0737\u073c\5\u0138\u009d\2\u0738\u073c\5\u013a\u009e")
        buf.write(u"\2\u0739\u073c\5\u0130\u0099\2\u073a\u073c\5\u0134\u009b")
        buf.write(u"\2\u073b\u0734\3\2\2\2\u073b\u0735\3\2\2\2\u073b\u0736")
        buf.write(u"\3\2\2\2\u073b\u0737\3\2\2\2\u073b\u0738\3\2\2\2\u073b")
        buf.write(u"\u0739\3\2\2\2\u073b\u073a\3\2\2\2\u073c\u0129\3\2\2")
        buf.write(u"\2\u073d\u073e\5\u00f2z\2\u073e\u012b\3\2\2\2\u073f\u0740")
        buf.write(u"\5\u0112\u008a\2\u0740\u0741\5\u0130\u0099\2\u0741\u012d")
        buf.write(u"\3\2\2\2\u0742\u0743\7\25\2\2\u0743\u0748\5\u0130\u0099")
        buf.write(u"\2\u0744\u0745\7\25\2\2\u0745\u0748\5\u013c\u009f\2\u0746")
        buf.write(u"\u0748\5\u0134\u009b\2\u0747\u0742\3\2\2\2\u0747\u0744")
        buf.write(u"\3\2\2\2\u0747\u0746\3\2\2\2\u0748\u012f\3\2\2\2\u0749")
        buf.write(u"\u074a\5\u013c\u009f\2\u074a\u074c\7\26\2\2\u074b\u074d")
        buf.write(u"\5\u0132\u009a\2\u074c\u074b\3\2\2\2\u074c\u074d\3\2")
        buf.write(u"\2\2\u074d\u074e\3\2\2\2\u074e\u074f\7\27\2\2\u074f\u0131")
        buf.write(u"\3\2\2\2\u0750\u0751\b\u009a\1\2\u0751\u0752\5\u0126")
        buf.write(u"\u0094\2\u0752\u0758\3\2\2\2\u0753\u0754\f\3\2\2\u0754")
        buf.write(u"\u0755\7\23\2\2\u0755\u0757\5\u0126\u0094\2\u0756\u0753")
        buf.write(u"\3\2\2\2\u0757\u075a\3\2\2\2\u0758\u0756\3\2\2\2\u0758")
        buf.write(u"\u0759\3\2\2\2\u0759\u0133\3\2\2\2\u075a\u0758\3\2\2")
        buf.write(u"\2\u075b\u075c\7\30\2\2\u075c\u075d\5\u0126\u0094\2\u075d")
        buf.write(u"\u075e\7\31\2\2\u075e\u0135\3\2\2\2\u075f\u0760\7\26")
        buf.write(u"\2\2\u0760\u0761\5\u0126\u0094\2\u0761\u0762\7\27\2\2")
        buf.write(u"\u0762\u0137\3\2\2\2\u0763\u0764\5\u013c\u009f\2\u0764")
        buf.write(u"\u0139\3\2\2\2\u0765\u076b\7\u00a3\2\2\u0766\u076b\7")
        buf.write(u"\u00a5\2\2\u0767\u076b\7\u00a2\2\2\u0768\u076b\7\u0099")
        buf.write(u"\2\2\u0769\u076b\7\u009a\2\2\u076a\u0765\3\2\2\2\u076a")
        buf.write(u"\u0766\3\2\2\2\u076a\u0767\3\2\2\2\u076a\u0768\3\2\2")
        buf.write(u"\2\u076a\u0769\3\2\2\2\u076b\u013b\3\2\2\2\u076c\u076d")
        buf.write(u"\t\7\2\2\u076d\u013d\3\2\2\2\u076e\u076f\7\u0084\2\2")
        buf.write(u"\u076f\u0772\5\u0140\u00a1\2\u0770\u0772\5\u0140\u00a1")
        buf.write(u"\2\u0771\u076e\3\2\2\2\u0771\u0770\3\2\2\2\u0772\u013f")
        buf.write(u"\3\2\2\2\u0773\u0774\b\u00a1\1\2\u0774\u0775\5\u0142")
        buf.write(u"\u00a2\2\u0775\u077a\3\2\2\2\u0776\u0777\f\3\2\2\u0777")
        buf.write(u"\u0779\5\u0144\u00a3\2\u0778\u0776\3\2\2\2\u0779\u077c")
        buf.write(u"\3\2\2\2\u077a\u0778\3\2\2\2\u077a\u077b\3\2\2\2\u077b")
        buf.write(u"\u0141\3\2\2\2\u077c\u077a\3\2\2\2\u077d\u0782\5\u014e")
        buf.write(u"\u00a8\2\u077e\u0782\5\u0150\u00a9\2\u077f\u0782\5\u0152")
        buf.write(u"\u00aa\2\u0780\u0782\5\u0146\u00a4\2\u0781\u077d\3\2")
        buf.write(u"\2\2\u0781\u077e\3\2\2\2\u0781\u077f\3\2\2\2\u0781\u0780")
        buf.write(u"\3\2\2\2\u0782\u0143\3\2\2\2\u0783\u0784\7\25\2\2\u0784")
        buf.write(u"\u078a\5\u0146\u00a4\2\u0785\u0786\7\30\2\2\u0786\u0787")
        buf.write(u"\5\u0140\u00a1\2\u0787\u0788\7\31\2\2\u0788\u078a\3\2")
        buf.write(u"\2\2\u0789\u0783\3\2\2\2\u0789\u0785\3\2\2\2\u078a\u0145")
        buf.write(u"\3\2\2\2\u078b\u078c\5\u0154\u00ab\2\u078c\u078e\7\26")
        buf.write(u"\2\2\u078d\u078f\5\u0148\u00a5\2\u078e\u078d\3\2\2\2")
        buf.write(u"\u078e\u078f\3\2\2\2\u078f\u0790\3\2\2\2\u0790\u0791")
        buf.write(u"\7\27\2\2\u0791\u0147\3\2\2\2\u0792\u0799\5\u014a\u00a6")
        buf.write(u"\2\u0793\u0799\5\u014c\u00a7\2\u0794\u0795\5\u014a\u00a6")
        buf.write(u"\2\u0795\u0796\7\23\2\2\u0796\u0797\5\u014c\u00a7\2\u0797")
        buf.write(u"\u0799\3\2\2\2\u0798\u0792\3\2\2\2\u0798\u0793\3\2\2")
        buf.write(u"\2\u0798\u0794\3\2\2\2\u0799\u0149\3\2\2\2\u079a\u079b")
        buf.write(u"\b\u00a6\1\2\u079b\u079c\5\u0140\u00a1\2\u079c\u07a2")
        buf.write(u"\3\2\2\2\u079d\u079e\f\3\2\2\u079e\u079f\7\23\2\2\u079f")
        buf.write(u"\u07a1\5\u0140\u00a1\2\u07a0\u079d\3\2\2\2\u07a1\u07a4")
        buf.write(u"\3\2\2\2\u07a2\u07a0\3\2\2\2\u07a2\u07a3\3\2\2\2\u07a3")
        buf.write(u"\u014b\3\2\2\2\u07a4\u07a2\3\2\2\2\u07a5\u07a6\b\u00a7")
        buf.write(u"\1\2\u07a6\u07a7\5\u0154\u00ab\2\u07a7\u07a8\7-\2\2\u07a8")
        buf.write(u"\u07a9\5\u0140\u00a1\2\u07a9\u07b2\3\2\2\2\u07aa\u07ab")
        buf.write(u"\f\3\2\2\u07ab\u07ac\7\23\2\2\u07ac\u07ad\5\u0154\u00ab")
        buf.write(u"\2\u07ad\u07ae\7-\2\2\u07ae\u07af\5\u0140\u00a1\2\u07af")
        buf.write(u"\u07b1\3\2\2\2\u07b0\u07aa\3\2\2\2\u07b1\u07b4\3\2\2")
        buf.write(u"\2\u07b2\u07b0\3\2\2\2\u07b2\u07b3\3\2\2\2\u07b3\u014d")
        buf.write(u"\3\2\2\2\u07b4\u07b2\3\2\2\2\u07b5\u07b6\7\26\2\2\u07b6")
        buf.write(u"\u07b7\5\u0140\u00a1\2\u07b7\u07b8\7\27\2\2\u07b8\u014f")
        buf.write(u"\3\2\2\2\u07b9\u07ba\b\u00a9\1\2\u07ba\u07bd\7\u00a1")
        buf.write(u"\2\2\u07bb\u07bd\5\u0154\u00ab\2\u07bc\u07b9\3\2\2\2")
        buf.write(u"\u07bc\u07bb\3\2\2\2\u07bd\u07c3\3\2\2\2\u07be\u07bf")
        buf.write(u"\f\3\2\2\u07bf\u07c0\7\25\2\2\u07c0\u07c2\5\u0154\u00ab")
        buf.write(u"\2\u07c1\u07be\3\2\2\2\u07c2\u07c5\3\2\2\2\u07c3\u07c1")
        buf.write(u"\3\2\2\2\u07c3\u07c4\3\2\2\2\u07c4\u0151\3\2\2\2\u07c5")
        buf.write(u"\u07c3\3\2\2\2\u07c6\u07cc\7\u00a3\2\2\u07c7\u07cc\7")
        buf.write(u"\u00a5\2\2\u07c8\u07cc\7\u00a2\2\2\u07c9\u07cc\7\u0099")
        buf.write(u"\2\2\u07ca\u07cc\7\u009a\2\2\u07cb\u07c6\3\2\2\2\u07cb")
        buf.write(u"\u07c7\3\2\2\2\u07cb\u07c8\3\2\2\2\u07cb\u07c9\3\2\2")
        buf.write(u"\2\u07cb\u07ca\3\2\2\2\u07cc\u0153\3\2\2\2\u07cd\u07ce")
        buf.write(u"\t\b\2\2\u07ce\u0155\3\2\2\2\u07cf\u07d0\7\u0084\2\2")
        buf.write(u"\u07d0\u07d1\5\u0158\u00ad\2\u07d1\u07d2\7\22\2\2\u07d2")
        buf.write(u"\u07d7\3\2\2\2\u07d3\u07d4\5\u0158\u00ad\2\u07d4\u07d5")
        buf.write(u"\7\22\2\2\u07d5\u07d7\3\2\2\2\u07d6\u07cf\3\2\2\2\u07d6")
        buf.write(u"\u07d3\3\2\2\2\u07d7\u0157\3\2\2\2\u07d8\u07d9\b\u00ad")
        buf.write(u"\1\2\u07d9\u07da\5\u015a\u00ae\2\u07da\u07df\3\2\2\2")
        buf.write(u"\u07db\u07dc\f\3\2\2\u07dc\u07de\5\u0160\u00b1\2\u07dd")
        buf.write(u"\u07db\3\2\2\2\u07de\u07e1\3\2\2\2\u07df\u07dd\3\2\2")
        buf.write(u"\2\u07df\u07e0\3\2\2\2\u07e0\u0159\3\2\2\2\u07e1\u07df")
        buf.write(u"\3\2\2\2\u07e2\u07e8\5\u015c\u00af\2\u07e3\u07e8\5\u015e")
        buf.write(u"\u00b0\2\u07e4\u07e8\5\u0168\u00b5\2\u07e5\u07e8\5\u016a")
        buf.write(u"\u00b6\2\u07e6\u07e8\5\u016e\u00b8\2\u07e7\u07e2\3\2")
        buf.write(u"\2\2\u07e7\u07e3\3\2\2\2\u07e7\u07e4\3\2\2\2\u07e7\u07e5")
        buf.write(u"\3\2\2\2\u07e7\u07e6\3\2\2\2\u07e8\u015b\3\2\2\2\u07e9")
        buf.write(u"\u07ea\5\u00f2z\2\u07ea\u015d\3\2\2\2\u07eb\u07ec\5\u0112")
        buf.write(u"\u008a\2\u07ec\u07ed\5\u0162\u00b2\2\u07ed\u015f\3\2")
        buf.write(u"\2\2\u07ee\u07ef\7\25\2\2\u07ef\u07f2\5\u0162\u00b2\2")
        buf.write(u"\u07f0\u07f2\5\u0166\u00b4\2\u07f1\u07ee\3\2\2\2\u07f1")
        buf.write(u"\u07f0\3\2\2\2\u07f2\u0161\3\2\2\2\u07f3\u07f4\5\u0170")
        buf.write(u"\u00b9\2\u07f4\u07f6\7\26\2\2\u07f5\u07f7\5\u0164\u00b3")
        buf.write(u"\2\u07f6\u07f5\3\2\2\2\u07f6\u07f7\3\2\2\2\u07f7\u07f8")
        buf.write(u"\3\2\2\2\u07f8\u07f9\7\27\2\2\u07f9\u0163\3\2\2\2\u07fa")
        buf.write(u"\u07fb\b\u00b3\1\2\u07fb\u07fc\5\u0158\u00ad\2\u07fc")
        buf.write(u"\u0802\3\2\2\2\u07fd\u07fe\f\3\2\2\u07fe\u07ff\7\23\2")
        buf.write(u"\2\u07ff\u0801\5\u0158\u00ad\2\u0800\u07fd\3\2\2\2\u0801")
        buf.write(u"\u0804\3\2\2\2\u0802\u0800\3\2\2\2\u0802\u0803\3\2\2")
        buf.write(u"\2\u0803\u0165\3\2\2\2\u0804\u0802\3\2\2\2\u0805\u0806")
        buf.write(u"\7\30\2\2\u0806\u0807\5\u0158\u00ad\2\u0807\u0808\7\31")
        buf.write(u"\2\2\u0808\u0167\3\2\2\2\u0809\u080a\7\26\2\2\u080a\u080b")
        buf.write(u"\5\u0158\u00ad\2\u080b\u080c\7\27\2\2\u080c\u0169\3\2")
        buf.write(u"\2\2\u080d\u080e\b\u00b6\1\2\u080e\u080f\5\u0170\u00b9")
        buf.write(u"\2\u080f\u0815\3\2\2\2\u0810\u0811\f\3\2\2\u0811\u0812")
        buf.write(u"\7\25\2\2\u0812\u0814\5\u0170\u00b9\2\u0813\u0810\3\2")
        buf.write(u"\2\2\u0814\u0817\3\2\2\2\u0815\u0813\3\2\2\2\u0815\u0816")
        buf.write(u"\3\2\2\2\u0816\u016b\3\2\2\2\u0817\u0815\3\2\2\2\u0818")
        buf.write(u"\u0819\b\u00b7\1\2\u0819\u081a\5\u016a\u00b6\2\u081a")
        buf.write(u"\u081f\3\2\2\2\u081b\u081c\f\3\2\2\u081c\u081e\7\u00a1")
        buf.write(u"\2\2\u081d\u081b\3\2\2\2\u081e\u0821\3\2\2\2\u081f\u081d")
        buf.write(u"\3\2\2\2\u081f\u0820\3\2\2\2\u0820\u016d\3\2\2\2\u0821")
        buf.write(u"\u081f\3\2\2\2\u0822\u0828\7\u00a3\2\2\u0823\u0828\7")
        buf.write(u"\u00a5\2\2\u0824\u0828\7\u00a2\2\2\u0825\u0828\7\u0099")
        buf.write(u"\2\2\u0826\u0828\7\u009a\2\2\u0827\u0822\3\2\2\2\u0827")
        buf.write(u"\u0823\3\2\2\2\u0827\u0824\3\2\2\2\u0827\u0825\3\2\2")
        buf.write(u"\2\u0827\u0826\3\2\2\2\u0828\u016f\3\2\2\2\u0829\u082a")
        buf.write(u"\t\t\2\2\u082a\u0171\3\2\2\2\u082b\u082c\7\u0084\2\2")
        buf.write(u"\u082c\u082d\5\u0174\u00bb\2\u082d\u082e\7\22\2\2\u082e")
        buf.write(u"\u0833\3\2\2\2\u082f\u0830\5\u0174\u00bb\2\u0830\u0831")
        buf.write(u"\7\22\2\2\u0831\u0833\3\2\2\2\u0832\u082b\3\2\2\2\u0832")
        buf.write(u"\u082f\3\2\2\2\u0833\u0173\3\2\2\2\u0834\u0835\b\u00bb")
        buf.write(u"\1\2\u0835\u0836\5\u0176\u00bc\2\u0836\u083b\3\2\2\2")
        buf.write(u"\u0837\u0838\f\3\2\2\u0838\u083a\5\u017c\u00bf\2\u0839")
        buf.write(u"\u0837\3\2\2\2\u083a\u083d\3\2\2\2\u083b\u0839\3\2\2")
        buf.write(u"\2\u083b\u083c\3\2\2\2\u083c\u0175\3\2\2\2\u083d\u083b")
        buf.write(u"\3\2\2\2\u083e\u0844\5\u0178\u00bd\2\u083f\u0844\5\u017a")
        buf.write(u"\u00be\2\u0840\u0844\5\u0184\u00c3\2\u0841\u0844\5\u0186")
        buf.write(u"\u00c4\2\u0842\u0844\5\u0188\u00c5\2\u0843\u083e\3\2")
        buf.write(u"\2\2\u0843\u083f\3\2\2\2\u0843\u0840\3\2\2\2\u0843\u0841")
        buf.write(u"\3\2\2\2\u0843\u0842\3\2\2\2\u0844\u0177\3\2\2\2\u0845")
        buf.write(u"\u0846\5\u00f2z\2\u0846\u0179\3\2\2\2\u0847\u0848\5\u0112")
        buf.write(u"\u008a\2\u0848\u0849\5\u017e\u00c0\2\u0849\u017b\3\2")
        buf.write(u"\2\2\u084a\u084b\7\25\2\2\u084b\u084e\5\u017e\u00c0\2")
        buf.write(u"\u084c\u084e\5\u0182\u00c2\2\u084d\u084a\3\2\2\2\u084d")
        buf.write(u"\u084c\3\2\2\2\u084e\u017d\3\2\2\2\u084f\u0850\5\u018a")
        buf.write(u"\u00c6\2\u0850\u0852\7\26\2\2\u0851\u0853\5\u0180\u00c1")
        buf.write(u"\2\u0852\u0851\3\2\2\2\u0852\u0853\3\2\2\2\u0853\u0854")
        buf.write(u"\3\2\2\2\u0854\u0855\7\27\2\2\u0855\u017f\3\2\2\2\u0856")
        buf.write(u"\u0857\b\u00c1\1\2\u0857\u0858\5\u0174\u00bb\2\u0858")
        buf.write(u"\u085e\3\2\2\2\u0859\u085a\f\3\2\2\u085a\u085b\7\23\2")
        buf.write(u"\2\u085b\u085d\5\u0174\u00bb\2\u085c\u0859\3\2\2\2\u085d")
        buf.write(u"\u0860\3\2\2\2\u085e\u085c\3\2\2\2\u085e\u085f\3\2\2")
        buf.write(u"\2\u085f\u0181\3\2\2\2\u0860\u085e\3\2\2\2\u0861\u0862")
        buf.write(u"\7\30\2\2\u0862\u0863\5\u0174\u00bb\2\u0863\u0864\7\31")
        buf.write(u"\2\2\u0864\u0183\3\2\2\2\u0865\u0866\7\26\2\2\u0866\u0867")
        buf.write(u"\5\u0174\u00bb\2\u0867\u0868\7\27\2\2\u0868\u0185\3\2")
        buf.write(u"\2\2\u0869\u086a\b\u00c4\1\2\u086a\u086d\7\u00a1\2\2")
        buf.write(u"\u086b\u086d\5\u018a\u00c6\2\u086c\u0869\3\2\2\2\u086c")
        buf.write(u"\u086b\3\2\2\2\u086d\u0873\3\2\2\2\u086e\u086f\f\3\2")
        buf.write(u"\2\u086f\u0870\7\25\2\2\u0870\u0872\5\u018a\u00c6\2\u0871")
        buf.write(u"\u086e\3\2\2\2\u0872\u0875\3\2\2\2\u0873\u0871\3\2\2")
        buf.write(u"\2\u0873\u0874\3\2\2\2\u0874\u0187\3\2\2\2\u0875\u0873")
        buf.write(u"\3\2\2\2\u0876\u087c\7\u00a3\2\2\u0877\u087c\7\u00a5")
        buf.write(u"\2\2\u0878\u087c\7\u00a2\2\2\u0879\u087c\7\u0099\2\2")
        buf.write(u"\u087a\u087c\7\u009a\2\2\u087b\u0876\3\2\2\2\u087b\u0877")
        buf.write(u"\3\2\2\2\u087b\u0878\3\2\2\2\u087b\u0879\3\2\2\2\u087b")
        buf.write(u"\u087a\3\2\2\2\u087c\u0189\3\2\2\2\u087d\u087e\t\n\2")
        buf.write(u"\2\u087e\u018b\3\2\2\2\u00aa\u0192\u0195\u01ae\u01b3")
        buf.write(u"\u01be\u01c3\u01ce\u01d5\u01e2\u01f0\u020c\u0213\u021c")
        buf.write(u"\u0225\u022e\u0243\u024d\u0252\u0258\u025d\u0269\u026e")
        buf.write(u"\u0286\u0291\u0295\u02a8\u02be\u02c3\u02cc\u02d5\u02de")
        buf.write(u"\u02fb\u030e\u0314\u0336\u033f\u0356\u0364\u036d\u0376")
        buf.write(u"\u038d\u0391\u03a5\u040b\u040d\u0419\u0422\u0431\u043a")
        buf.write(u"\u0443\u044a\u0464\u046f\u0473\u0478\u047d\u047f\u0489")
        buf.write(u"\u0499\u04a2\u04a8\u04ad\u04b4\u04bc\u04ca\u04d2\u04da")
        buf.write(u"\u04e0\u04eb\u04f7\u0502\u050f\u0513\u0519\u0525\u0539")
        buf.write(u"\u053b\u0540\u0550\u0555\u055e\u0568\u056d\u0572\u0582")
        buf.write(u"\u0587\u058a\u058e\u0593\u059a\u05a5\u05a7\u05b3\u05bb")
        buf.write(u"\u05c6\u05cb\u05d7\u05db\u05e5\u05ed\u05f3\u05fa\u05ff")
        buf.write(u"\u0609\u0610\u061d\u062a\u062e\u0631\u0635\u0638\u0643")
        buf.write(u"\u064f\u065b\u0667\u0678\u0687\u0691\u0698\u06a2\u06a9")
        buf.write(u"\u06ad\u06b3\u06bf\u06ca\u06da\u06e7\u06ee\u06f5\u06fd")
        buf.write(u"\u0701\u0709\u0728\u0731\u073b\u0747\u074c\u0758\u076a")
        buf.write(u"\u0771\u077a\u0781\u0789\u078e\u0798\u07a2\u07b2\u07bc")
        buf.write(u"\u07c3\u07cb\u07d6\u07df\u07e7\u07f1\u07f6\u0802\u0815")
        buf.write(u"\u081f\u0827\u0832\u083b\u0843\u084d\u0852\u085e\u086c")
        buf.write(u"\u0873\u087b")
        return buf.getvalue()
		

class SParser ( AbstractParser ):

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
                     u"'abstract'", u"'all'", u"'always'", u"'and'", u"'any'", 
                     u"'as'", u"<INVALID>", u"'attr'", u"'attribute'", u"'attributes'", 
                     u"'bindings'", u"'by'", u"'case'", u"'catch'", u"'category'", 
                     u"'class'", u"'close'", u"'contains'", u"'def'", u"'default'", 
                     u"'define'", u"'delete'", u"<INVALID>", u"'do'", u"'doing'", 
                     u"'each'", u"'else'", u"'enum'", u"'enumerated'", u"'except'", 
                     u"'execute'", u"'expecting'", u"'extends'", u"'fetch'", 
                     u"'finally'", u"'for'", u"'from'", u"'getter'", u"'if'", 
                     u"'in'", u"'index'", u"'invoke'", u"'is'", u"'matching'", 
                     u"'method'", u"'methods'", u"'modulo'", u"'mutable'", 
                     u"'native'", u"'None'", u"'not'", u"<INVALID>", u"'null'", 
                     u"'on'", u"'one'", u"'open'", u"'operator'", u"'or'", 
                     u"'order'", u"'otherwise'", u"'pass'", u"'raise'", 
                     u"'read'", u"'receiving'", u"'resource'", u"'return'", 
                     u"'returning'", u"'rows'", u"'self'", u"'setter'", 
                     u"'singleton'", u"'sorted'", u"'storable'", u"'store'", 
                     u"'switch'", u"'test'", u"'this'", u"'throw'", u"'to'", 
                     u"'try'", u"'verifying'", u"'with'", u"'when'", u"'where'", 
                     u"'while'", u"'write'", u"<INVALID>", u"<INVALID>", 
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
                      u"DOCUMENT", u"BLOB", u"IMAGE", u"UUID", u"ABSTRACT", 
                      u"ALL", u"ALWAYS", u"AND", u"ANY", u"AS", u"ASC", 
                      u"ATTR", u"ATTRIBUTE", u"ATTRIBUTES", u"BINDINGS", 
                      u"BY", u"CASE", u"CATCH", u"CATEGORY", u"CLASS", u"CLOSE", 
                      u"CONTAINS", u"DEF", u"DEFAULT", u"DEFINE", u"DELETE", 
                      u"DESC", u"DO", u"DOING", u"EACH", u"ELSE", u"ENUM", 
                      u"ENUMERATED", u"EXCEPT", u"EXECUTE", u"EXPECTING", 
                      u"EXTENDS", u"FETCH", u"FINALLY", u"FOR", u"FROM", 
                      u"GETTER", u"IF", u"IN", u"INDEX", u"INVOKE", u"IS", 
                      u"MATCHING", u"METHOD", u"METHODS", u"MODULO", u"MUTABLE", 
                      u"NATIVE", u"NONE", u"NOT", u"NOTHING", u"NULL", u"ON", 
                      u"ONE", u"OPEN", u"OPERATOR", u"OR", u"ORDER", u"OTHERWISE", 
                      u"PASS", u"RAISE", u"READ", u"RECEIVING", u"RESOURCE", 
                      u"RETURN", u"RETURNING", u"ROWS", u"SELF", u"SETTER", 
                      u"SINGLETON", u"SORTED", u"STORABLE", u"STORE", u"SWITCH", 
                      u"TEST", u"THIS", u"THROW", u"TO", u"TRY", u"VERIFYING", 
                      u"WITH", u"WHEN", u"WHERE", u"WHILE", u"WRITE", u"BOOLEAN_LITERAL", 
                      u"CHAR_LITERAL", u"MIN_INTEGER", u"MAX_INTEGER", u"SYMBOL_IDENTIFIER", 
                      u"TYPE_IDENTIFIER", u"VARIABLE_IDENTIFIER", u"NATIVE_IDENTIFIER", 
                      u"DOLLAR_IDENTIFIER", u"TEXT_LITERAL", u"INTEGER_LITERAL", 
                      u"HEXA_LITERAL", u"DECIMAL_LITERAL", u"DATETIME_LITERAL", 
                      u"TIME_LITERAL", u"DATE_LITERAL", u"PERIOD_LITERAL" ]

    RULE_enum_category_declaration = 0
    RULE_enum_native_declaration = 1
    RULE_native_symbol = 2
    RULE_category_symbol = 3
    RULE_attribute_declaration = 4
    RULE_concrete_category_declaration = 5
    RULE_singleton_category_declaration = 6
    RULE_derived_list = 7
    RULE_operator_method_declaration = 8
    RULE_setter_method_declaration = 9
    RULE_getter_method_declaration = 10
    RULE_native_category_declaration = 11
    RULE_native_resource_declaration = 12
    RULE_native_category_bindings = 13
    RULE_native_category_binding_list = 14
    RULE_attribute_list = 15
    RULE_abstract_method_declaration = 16
    RULE_concrete_method_declaration = 17
    RULE_native_method_declaration = 18
    RULE_test_method_declaration = 19
    RULE_assertion = 20
    RULE_typed_argument = 21
    RULE_statement = 22
    RULE_store_statement = 23
    RULE_method_call = 24
    RULE_method_selector = 25
    RULE_callable_parent = 26
    RULE_callable_selector = 27
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
    RULE_return_statement = 40
    RULE_expression = 41
    RULE_closure_expression = 42
    RULE_instance_expression = 43
    RULE_method_expression = 44
    RULE_instance_selector = 45
    RULE_document_expression = 46
    RULE_constructor_expression = 47
    RULE_argument_assignment_list = 48
    RULE_argument_assignment = 49
    RULE_read_expression = 50
    RULE_write_statement = 51
    RULE_fetch_expression = 52
    RULE_sorted_expression = 53
    RULE_assign_instance_statement = 54
    RULE_child_instance = 55
    RULE_assign_tuple_statement = 56
    RULE_lfs = 57
    RULE_lfp = 58
    RULE_indent = 59
    RULE_dedent = 60
    RULE_null_literal = 61
    RULE_declaration_list = 62
    RULE_declarations = 63
    RULE_declaration = 64
    RULE_resource_declaration = 65
    RULE_enum_declaration = 66
    RULE_native_symbol_list = 67
    RULE_category_symbol_list = 68
    RULE_symbol_list = 69
    RULE_attribute_constraint = 70
    RULE_list_literal = 71
    RULE_set_literal = 72
    RULE_expression_list = 73
    RULE_range_literal = 74
    RULE_typedef = 75
    RULE_primary_type = 76
    RULE_native_type = 77
    RULE_category_type = 78
    RULE_mutable_category_type = 79
    RULE_code_type = 80
    RULE_category_declaration = 81
    RULE_type_identifier_list = 82
    RULE_method_identifier = 83
    RULE_identifier = 84
    RULE_variable_identifier = 85
    RULE_type_identifier = 86
    RULE_symbol_identifier = 87
    RULE_argument_list = 88
    RULE_argument = 89
    RULE_operator_argument = 90
    RULE_named_argument = 91
    RULE_code_argument = 92
    RULE_category_or_any_type = 93
    RULE_any_type = 94
    RULE_member_method_declaration_list = 95
    RULE_member_method_declaration = 96
    RULE_native_member_method_declaration_list = 97
    RULE_native_member_method_declaration = 98
    RULE_native_category_binding = 99
    RULE_python_category_binding = 100
    RULE_python_module = 101
    RULE_module_token = 102
    RULE_javascript_category_binding = 103
    RULE_javascript_module = 104
    RULE_variable_identifier_list = 105
    RULE_method_declaration = 106
    RULE_comment_statement = 107
    RULE_native_statement_list = 108
    RULE_native_statement = 109
    RULE_python_native_statement = 110
    RULE_javascript_native_statement = 111
    RULE_statement_list = 112
    RULE_assertion_list = 113
    RULE_switch_case_statement_list = 114
    RULE_catch_statement_list = 115
    RULE_literal_collection = 116
    RULE_atomic_literal = 117
    RULE_literal_list_literal = 118
    RULE_selectable_expression = 119
    RULE_this_expression = 120
    RULE_parenthesis_expression = 121
    RULE_literal_expression = 122
    RULE_collection_literal = 123
    RULE_tuple_literal = 124
    RULE_dict_literal = 125
    RULE_expression_tuple = 126
    RULE_dict_entry_list = 127
    RULE_dict_entry = 128
    RULE_slice_arguments = 129
    RULE_assign_variable_statement = 130
    RULE_assignable_instance = 131
    RULE_is_expression = 132
    RULE_order_by_list = 133
    RULE_order_by = 134
    RULE_operator = 135
    RULE_new_token = 136
    RULE_key_token = 137
    RULE_value_token = 138
    RULE_symbols_token = 139
    RULE_assign = 140
    RULE_multiply = 141
    RULE_divide = 142
    RULE_idivide = 143
    RULE_modulo = 144
    RULE_javascript_statement = 145
    RULE_javascript_expression = 146
    RULE_javascript_primary_expression = 147
    RULE_javascript_this_expression = 148
    RULE_javascript_new_expression = 149
    RULE_javascript_selector_expression = 150
    RULE_javascript_method_expression = 151
    RULE_javascript_arguments = 152
    RULE_javascript_item_expression = 153
    RULE_javascript_parenthesis_expression = 154
    RULE_javascript_identifier_expression = 155
    RULE_javascript_literal_expression = 156
    RULE_javascript_identifier = 157
    RULE_python_statement = 158
    RULE_python_expression = 159
    RULE_python_primary_expression = 160
    RULE_python_selector_expression = 161
    RULE_python_method_expression = 162
    RULE_python_argument_list = 163
    RULE_python_ordinal_argument_list = 164
    RULE_python_named_argument_list = 165
    RULE_python_parenthesis_expression = 166
    RULE_python_identifier_expression = 167
    RULE_python_literal_expression = 168
    RULE_python_identifier = 169
    RULE_java_statement = 170
    RULE_java_expression = 171
    RULE_java_primary_expression = 172
    RULE_java_this_expression = 173
    RULE_java_new_expression = 174
    RULE_java_selector_expression = 175
    RULE_java_method_expression = 176
    RULE_java_arguments = 177
    RULE_java_item_expression = 178
    RULE_java_parenthesis_expression = 179
    RULE_java_identifier_expression = 180
    RULE_java_class_identifier_expression = 181
    RULE_java_literal_expression = 182
    RULE_java_identifier = 183
    RULE_csharp_statement = 184
    RULE_csharp_expression = 185
    RULE_csharp_primary_expression = 186
    RULE_csharp_this_expression = 187
    RULE_csharp_new_expression = 188
    RULE_csharp_selector_expression = 189
    RULE_csharp_method_expression = 190
    RULE_csharp_arguments = 191
    RULE_csharp_item_expression = 192
    RULE_csharp_parenthesis_expression = 193
    RULE_csharp_identifier_expression = 194
    RULE_csharp_literal_expression = 195
    RULE_csharp_identifier = 196

    ruleNames =  [ u"enum_category_declaration", u"enum_native_declaration", 
                   u"native_symbol", u"category_symbol", u"attribute_declaration", 
                   u"concrete_category_declaration", u"singleton_category_declaration", 
                   u"derived_list", u"operator_method_declaration", u"setter_method_declaration", 
                   u"getter_method_declaration", u"native_category_declaration", 
                   u"native_resource_declaration", u"native_category_bindings", 
                   u"native_category_binding_list", u"attribute_list", u"abstract_method_declaration", 
                   u"concrete_method_declaration", u"native_method_declaration", 
                   u"test_method_declaration", u"assertion", u"typed_argument", 
                   u"statement", u"store_statement", u"method_call", u"method_selector", 
                   u"callable_parent", u"callable_selector", u"with_resource_statement", 
                   u"with_singleton_statement", u"switch_statement", u"switch_case_statement", 
                   u"for_each_statement", u"do_while_statement", u"while_statement", 
                   u"if_statement", u"else_if_statement_list", u"raise_statement", 
                   u"try_statement", u"catch_statement", u"return_statement", 
                   u"expression", u"closure_expression", u"instance_expression", 
                   u"method_expression", u"instance_selector", u"document_expression", 
                   u"constructor_expression", u"argument_assignment_list", 
                   u"argument_assignment", u"read_expression", u"write_statement", 
                   u"fetch_expression", u"sorted_expression", u"assign_instance_statement", 
                   u"child_instance", u"assign_tuple_statement", u"lfs", 
                   u"lfp", u"indent", u"dedent", u"null_literal", u"declaration_list", 
                   u"declarations", u"declaration", u"resource_declaration", 
                   u"enum_declaration", u"native_symbol_list", u"category_symbol_list", 
                   u"symbol_list", u"attribute_constraint", u"list_literal", 
                   u"set_literal", u"expression_list", u"range_literal", 
                   u"typedef", u"primary_type", u"native_type", u"category_type", 
                   u"mutable_category_type", u"code_type", u"category_declaration", 
                   u"type_identifier_list", u"method_identifier", u"identifier", 
                   u"variable_identifier", u"type_identifier", u"symbol_identifier", 
                   u"argument_list", u"argument", u"operator_argument", 
                   u"named_argument", u"code_argument", u"category_or_any_type", 
                   u"any_type", u"member_method_declaration_list", u"member_method_declaration", 
                   u"native_member_method_declaration_list", u"native_member_method_declaration", 
                   u"native_category_binding", u"python_category_binding", 
                   u"python_module", u"module_token", u"javascript_category_binding", 
                   u"javascript_module", u"variable_identifier_list", u"method_declaration", 
                   u"comment_statement", u"native_statement_list", u"native_statement", 
                   u"python_native_statement", u"javascript_native_statement", 
                   u"statement_list", u"assertion_list", u"switch_case_statement_list", 
                   u"catch_statement_list", u"literal_collection", u"atomic_literal", 
                   u"literal_list_literal", u"selectable_expression", u"this_expression", 
                   u"parenthesis_expression", u"literal_expression", u"collection_literal", 
                   u"tuple_literal", u"dict_literal", u"expression_tuple", 
                   u"dict_entry_list", u"dict_entry", u"slice_arguments", 
                   u"assign_variable_statement", u"assignable_instance", 
                   u"is_expression", u"order_by_list", u"order_by", u"operator", 
                   u"new_token", u"key_token", u"value_token", u"symbols_token", 
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
    ABSTRACT=65
    ALL=66
    ALWAYS=67
    AND=68
    ANY=69
    AS=70
    ASC=71
    ATTR=72
    ATTRIBUTE=73
    ATTRIBUTES=74
    BINDINGS=75
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
    FINALLY=99
    FOR=100
    FROM=101
    GETTER=102
    IF=103
    IN=104
    INDEX=105
    INVOKE=106
    IS=107
    MATCHING=108
    METHOD=109
    METHODS=110
    MODULO=111
    MUTABLE=112
    NATIVE=113
    NONE=114
    NOT=115
    NOTHING=116
    NULL=117
    ON=118
    ONE=119
    OPEN=120
    OPERATOR=121
    OR=122
    ORDER=123
    OTHERWISE=124
    PASS=125
    RAISE=126
    READ=127
    RECEIVING=128
    RESOURCE=129
    RETURN=130
    RETURNING=131
    ROWS=132
    SELF=133
    SETTER=134
    SINGLETON=135
    SORTED=136
    STORABLE=137
    STORE=138
    SWITCH=139
    TEST=140
    THIS=141
    THROW=142
    TO=143
    TRY=144
    VERIFYING=145
    WITH=146
    WHEN=147
    WHERE=148
    WHILE=149
    WRITE=150
    BOOLEAN_LITERAL=151
    CHAR_LITERAL=152
    MIN_INTEGER=153
    MAX_INTEGER=154
    SYMBOL_IDENTIFIER=155
    TYPE_IDENTIFIER=156
    VARIABLE_IDENTIFIER=157
    NATIVE_IDENTIFIER=158
    DOLLAR_IDENTIFIER=159
    TEXT_LITERAL=160
    INTEGER_LITERAL=161
    HEXA_LITERAL=162
    DECIMAL_LITERAL=163
    DATETIME_LITERAL=164
    TIME_LITERAL=165
    DATE_LITERAL=166
    PERIOD_LITERAL=167

    def __init__(self, input):
        super(SParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Enum_category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Enum_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.derived = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.symbols = None # Category_symbol_listContext

        def ENUM(self):
            return self.getToken(SParser.ENUM, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def type_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Type_identifierContext)
            else:
                return self.getTypedRuleContext(SParser.Type_identifierContext,i)


        def category_symbol_list(self):
            return self.getTypedRuleContext(SParser.Category_symbol_listContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(SParser.Attribute_listContext,0)


        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)

        def getRuleIndex(self):
            return SParser.RULE_enum_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterEnum_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitEnum_category_declaration(self)




    def enum_category_declaration(self):

        localctx = SParser.Enum_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_enum_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(SParser.ENUM)
            self.state = 395 
            localctx.name = self.type_identifier()
            self.state = 396
            self.match(SParser.LPAR)
            self.state = 403
            token = self._input.LA(1)
            if token in [SParser.TYPE_IDENTIFIER]:
                self.state = 397 
                localctx.derived = self.type_identifier()
                self.state = 400
                _la = self._input.LA(1)
                if _la==SParser.COMMA:
                    self.state = 398
                    self.match(SParser.COMMA)
                    self.state = 399 
                    localctx.attrs = self.attribute_list()



            elif token in [SParser.VARIABLE_IDENTIFIER]:
                self.state = 402 
                localctx.attrs = self.attribute_list()

            else:
                raise NoViableAltException(self)

            self.state = 405
            self.match(SParser.RPAR)
            self.state = 406
            self.match(SParser.COLON)
            self.state = 407 
            self.indent()
            self.state = 408 
            localctx.symbols = self.category_symbol_list(0)
            self.state = 409 
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
            super(SParser.Enum_native_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.typ = None # Native_typeContext
            self.symbols = None # Native_symbol_listContext

        def ENUM(self):
            return self.getToken(SParser.ENUM, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(SParser.Type_identifierContext,0)


        def native_type(self):
            return self.getTypedRuleContext(SParser.Native_typeContext,0)


        def native_symbol_list(self):
            return self.getTypedRuleContext(SParser.Native_symbol_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_enum_native_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterEnum_native_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitEnum_native_declaration(self)




    def enum_native_declaration(self):

        localctx = SParser.Enum_native_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_enum_native_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(SParser.ENUM)
            self.state = 412 
            localctx.name = self.type_identifier()
            self.state = 413
            self.match(SParser.LPAR)
            self.state = 414 
            localctx.typ = self.native_type()
            self.state = 415
            self.match(SParser.RPAR)
            self.state = 416
            self.match(SParser.COLON)
            self.state = 417 
            self.indent()
            self.state = 418 
            localctx.symbols = self.native_symbol_list(0)
            self.state = 419 
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
            super(SParser.Native_symbolContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Symbol_identifierContext
            self.exp = None # ExpressionContext

        def EQ(self):
            return self.getToken(SParser.EQ, 0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(SParser.Symbol_identifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_native_symbol

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNative_symbol(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNative_symbol(self)




    def native_symbol(self):

        localctx = SParser.Native_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_native_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421 
            localctx.name = self.symbol_identifier()
            self.state = 422
            self.match(SParser.EQ)
            self.state = 423 
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
            super(SParser.Category_symbolContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Symbol_identifierContext
            self.args = None # Argument_assignment_listContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(SParser.Symbol_identifierContext,0)


        def argument_assignment_list(self):
            return self.getTypedRuleContext(SParser.Argument_assignment_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_category_symbol

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCategory_symbol(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCategory_symbol(self)




    def category_symbol(self):

        localctx = SParser.Category_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_category_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425 
            localctx.name = self.symbol_identifier()
            self.state = 426
            self.match(SParser.LPAR)
            self.state = 428
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (SParser.EXECUTE - 95)) | (1 << (SParser.FETCH - 95)) | (1 << (SParser.MUTABLE - 95)) | (1 << (SParser.NONE - 95)) | (1 << (SParser.NOT - 95)) | (1 << (SParser.READ - 95)) | (1 << (SParser.SELF - 95)) | (1 << (SParser.SORTED - 95)) | (1 << (SParser.THIS - 95)) | (1 << (SParser.BOOLEAN_LITERAL - 95)) | (1 << (SParser.CHAR_LITERAL - 95)) | (1 << (SParser.MIN_INTEGER - 95)) | (1 << (SParser.MAX_INTEGER - 95)) | (1 << (SParser.SYMBOL_IDENTIFIER - 95)) | (1 << (SParser.TYPE_IDENTIFIER - 95)) | (1 << (SParser.VARIABLE_IDENTIFIER - 95)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (SParser.TEXT_LITERAL - 160)) | (1 << (SParser.INTEGER_LITERAL - 160)) | (1 << (SParser.HEXA_LITERAL - 160)) | (1 << (SParser.DECIMAL_LITERAL - 160)) | (1 << (SParser.DATETIME_LITERAL - 160)) | (1 << (SParser.TIME_LITERAL - 160)) | (1 << (SParser.DATE_LITERAL - 160)) | (1 << (SParser.PERIOD_LITERAL - 160)))) != 0):
                self.state = 427 
                localctx.args = self.argument_assignment_list(0)


            self.state = 430
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Attribute_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.typ = None # TypedefContext
            self.match = None # Attribute_constraintContext

        def ATTR(self):
            return self.getToken(SParser.ATTR, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def typedef(self):
            return self.getTypedRuleContext(SParser.TypedefContext,0)


        def PASS(self):
            return self.getToken(SParser.PASS, 0)

        def STORABLE(self):
            return self.getToken(SParser.STORABLE, 0)

        def attribute_constraint(self):
            return self.getTypedRuleContext(SParser.Attribute_constraintContext,0)


        def getRuleIndex(self):
            return SParser.RULE_attribute_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAttribute_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAttribute_declaration(self)




    def attribute_declaration(self):

        localctx = SParser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            _la = self._input.LA(1)
            if _la==SParser.STORABLE:
                self.state = 432
                self.match(SParser.STORABLE)


            self.state = 435
            self.match(SParser.ATTR)
            self.state = 436 
            localctx.name = self.variable_identifier()
            self.state = 437
            self.match(SParser.LPAR)
            self.state = 438 
            localctx.typ = self.typedef(0)
            self.state = 439
            self.match(SParser.RPAR)
            self.state = 440
            self.match(SParser.COLON)
            self.state = 441 
            self.indent()
            self.state = 444
            token = self._input.LA(1)
            if token in [SParser.IN, SParser.MATCHING]:
                self.state = 442 
                localctx.match = self.attribute_constraint()

            elif token in [SParser.PASS]:
                self.state = 443
                self.match(SParser.PASS)

            else:
                raise NoViableAltException(self)

            self.state = 446 
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
            super(SParser.Concrete_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.derived = None # Derived_listContext
            self.attrs = None # Attribute_listContext
            self.methods = None # Member_method_declaration_listContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def CLASS(self):
            return self.getToken(SParser.CLASS, 0)

        def CATEGORY(self):
            return self.getToken(SParser.CATEGORY, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(SParser.Type_identifierContext,0)


        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)

        def PASS(self):
            return self.getToken(SParser.PASS, 0)

        def STORABLE(self):
            return self.getToken(SParser.STORABLE, 0)

        def derived_list(self):
            return self.getTypedRuleContext(SParser.Derived_listContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(SParser.Attribute_listContext,0)


        def member_method_declaration_list(self):
            return self.getTypedRuleContext(SParser.Member_method_declaration_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_concrete_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterConcrete_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitConcrete_category_declaration(self)




    def concrete_category_declaration(self):

        localctx = SParser.Concrete_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_concrete_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            _la = self._input.LA(1)
            if _la==SParser.STORABLE:
                self.state = 448
                self.match(SParser.STORABLE)


            self.state = 451
            _la = self._input.LA(1)
            if not(_la==SParser.CATEGORY or _la==SParser.CLASS):
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 452 
            localctx.name = self.type_identifier()
            self.state = 453
            self.match(SParser.LPAR)
            self.state = 460
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 454 
                localctx.derived = self.derived_list()
                pass

            elif la_ == 2:
                self.state = 455 
                localctx.attrs = self.attribute_list()
                pass

            elif la_ == 3:
                self.state = 456 
                localctx.derived = self.derived_list()
                self.state = 457
                self.match(SParser.COMMA)
                self.state = 458 
                localctx.attrs = self.attribute_list()
                pass


            self.state = 462
            self.match(SParser.RPAR)
            self.state = 463
            self.match(SParser.COLON)
            self.state = 464 
            self.indent()
            self.state = 467
            token = self._input.LA(1)
            if token in [SParser.ABSTRACT, SParser.DEF]:
                self.state = 465 
                localctx.methods = self.member_method_declaration_list(0)

            elif token in [SParser.PASS]:
                self.state = 466
                self.match(SParser.PASS)

            else:
                raise NoViableAltException(self)

            self.state = 469 
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
            super(SParser.Singleton_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.methods = None # Member_method_declaration_listContext

        def SINGLETON(self):
            return self.getToken(SParser.SINGLETON, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(SParser.Type_identifierContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(SParser.Attribute_listContext,0)


        def PASS(self):
            return self.getToken(SParser.PASS, 0)

        def member_method_declaration_list(self):
            return self.getTypedRuleContext(SParser.Member_method_declaration_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_singleton_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSingleton_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSingleton_category_declaration(self)




    def singleton_category_declaration(self):

        localctx = SParser.Singleton_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_singleton_category_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(SParser.SINGLETON)
            self.state = 472 
            localctx.name = self.type_identifier()
            self.state = 473
            self.match(SParser.LPAR)
            self.state = 474 
            localctx.attrs = self.attribute_list()
            self.state = 475
            self.match(SParser.RPAR)
            self.state = 476
            self.match(SParser.COLON)
            self.state = 477 
            self.indent()
            self.state = 480
            token = self._input.LA(1)
            if token in [SParser.ABSTRACT, SParser.DEF]:
                self.state = 478 
                localctx.methods = self.member_method_declaration_list(0)

            elif token in [SParser.PASS]:
                self.state = 479
                self.match(SParser.PASS)

            else:
                raise NoViableAltException(self)

            self.state = 482 
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
            super(SParser.Derived_listContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Type_identifier_listContext

        def type_identifier_list(self):
            return self.getTypedRuleContext(SParser.Type_identifier_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_derived_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDerived_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDerived_list(self)




    def derived_list(self):

        localctx = SParser.Derived_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_derived_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484 
            localctx.items = self.type_identifier_list(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Operator_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Operator_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.op = None # OperatorContext
            self.arg = None # Operator_argumentContext
            self.typ = None # TypedefContext
            self.stmts = None # Statement_listContext

        def DEF(self):
            return self.getToken(SParser.DEF, 0)

        def OPERATOR(self):
            return self.getToken(SParser.OPERATOR, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def operator(self):
            return self.getTypedRuleContext(SParser.OperatorContext,0)


        def operator_argument(self):
            return self.getTypedRuleContext(SParser.Operator_argumentContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def RARROW(self):
            return self.getToken(SParser.RARROW, 0)

        def typedef(self):
            return self.getTypedRuleContext(SParser.TypedefContext,0)


        def getRuleIndex(self):
            return SParser.RULE_operator_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterOperator_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitOperator_method_declaration(self)




    def operator_method_declaration(self):

        localctx = SParser.Operator_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_operator_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.match(SParser.DEF)
            self.state = 487
            self.match(SParser.OPERATOR)
            self.state = 488 
            localctx.op = self.operator()
            self.state = 489
            self.match(SParser.LPAR)
            self.state = 490 
            localctx.arg = self.operator_argument()
            self.state = 491
            self.match(SParser.RPAR)
            self.state = 494
            _la = self._input.LA(1)
            if _la==SParser.RARROW:
                self.state = 492
                self.match(SParser.RARROW)
                self.state = 493 
                localctx.typ = self.typedef(0)


            self.state = 496
            self.match(SParser.COLON)
            self.state = 497 
            self.indent()
            self.state = 498 
            localctx.stmts = self.statement_list(0)
            self.state = 499 
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
            super(SParser.Setter_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext

        def DEF(self):
            return self.getToken(SParser.DEF, 0)

        def SETTER(self):
            return self.getToken(SParser.SETTER, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_setter_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSetter_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSetter_method_declaration(self)




    def setter_method_declaration(self):

        localctx = SParser.Setter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_setter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.match(SParser.DEF)
            self.state = 502 
            localctx.name = self.variable_identifier()
            self.state = 503
            self.match(SParser.SETTER)
            self.state = 504
            self.match(SParser.LPAR)
            self.state = 505
            self.match(SParser.RPAR)
            self.state = 506
            self.match(SParser.COLON)
            self.state = 507 
            self.indent()
            self.state = 508 
            localctx.stmts = self.statement_list(0)
            self.state = 509 
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
            super(SParser.Getter_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext

        def DEF(self):
            return self.getToken(SParser.DEF, 0)

        def GETTER(self):
            return self.getToken(SParser.GETTER, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_getter_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterGetter_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitGetter_method_declaration(self)




    def getter_method_declaration(self):

        localctx = SParser.Getter_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_getter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.match(SParser.DEF)
            self.state = 512 
            localctx.name = self.variable_identifier()
            self.state = 513
            self.match(SParser.GETTER)
            self.state = 514
            self.match(SParser.LPAR)
            self.state = 515
            self.match(SParser.RPAR)
            self.state = 516
            self.match(SParser.COLON)
            self.state = 517 
            self.indent()
            self.state = 518 
            localctx.stmts = self.statement_list(0)
            self.state = 519 
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
            super(SParser.Native_category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.bindings = None # Native_category_bindingsContext
            self.methods = None # Native_member_method_declaration_listContext

        def NATIVE(self):
            return self.getToken(SParser.NATIVE, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def CLASS(self):
            return self.getToken(SParser.CLASS, 0)

        def CATEGORY(self):
            return self.getToken(SParser.CATEGORY, 0)

        def type_identifier(self):
            return self.getTypedRuleContext(SParser.Type_identifierContext,0)


        def native_category_bindings(self):
            return self.getTypedRuleContext(SParser.Native_category_bindingsContext,0)


        def STORABLE(self):
            return self.getToken(SParser.STORABLE, 0)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(SParser.Attribute_listContext,0)


        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(SParser.Native_member_method_declaration_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_native_category_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNative_category_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNative_category_declaration(self)




    def native_category_declaration(self):

        localctx = SParser.Native_category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_native_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            _la = self._input.LA(1)
            if _la==SParser.STORABLE:
                self.state = 521
                self.match(SParser.STORABLE)


            self.state = 524
            self.match(SParser.NATIVE)
            self.state = 525
            _la = self._input.LA(1)
            if not(_la==SParser.CATEGORY or _la==SParser.CLASS):
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 526 
            localctx.name = self.type_identifier()
            self.state = 527
            self.match(SParser.LPAR)
            self.state = 529
            _la = self._input.LA(1)
            if _la==SParser.VARIABLE_IDENTIFIER:
                self.state = 528 
                localctx.attrs = self.attribute_list()


            self.state = 531
            self.match(SParser.RPAR)
            self.state = 532
            self.match(SParser.COLON)
            self.state = 533 
            self.indent()
            self.state = 534 
            localctx.bindings = self.native_category_bindings()
            self.state = 538
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 535 
                self.lfp()
                self.state = 536 
                localctx.methods = self.native_member_method_declaration_list(0)


            self.state = 540 
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
            super(SParser.Native_resource_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext
            self.attrs = None # Attribute_listContext
            self.bindings = None # Native_category_bindingsContext
            self.methods = None # Native_member_method_declaration_listContext

        def NATIVE(self):
            return self.getToken(SParser.NATIVE, 0)

        def RESOURCE(self):
            return self.getToken(SParser.RESOURCE, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(SParser.Type_identifierContext,0)


        def native_category_bindings(self):
            return self.getTypedRuleContext(SParser.Native_category_bindingsContext,0)


        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(SParser.Attribute_listContext,0)


        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(SParser.Native_member_method_declaration_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_native_resource_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNative_resource_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNative_resource_declaration(self)




    def native_resource_declaration(self):

        localctx = SParser.Native_resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_native_resource_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.match(SParser.NATIVE)
            self.state = 543
            self.match(SParser.RESOURCE)
            self.state = 544 
            localctx.name = self.type_identifier()
            self.state = 545
            self.match(SParser.LPAR)
            self.state = 547
            _la = self._input.LA(1)
            if _la==SParser.VARIABLE_IDENTIFIER:
                self.state = 546 
                localctx.attrs = self.attribute_list()


            self.state = 549
            self.match(SParser.RPAR)
            self.state = 550
            self.match(SParser.COLON)
            self.state = 551 
            self.indent()
            self.state = 552 
            localctx.bindings = self.native_category_bindings()
            self.state = 556
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 553 
                self.lfp()
                self.state = 554 
                localctx.methods = self.native_member_method_declaration_list(0)


            self.state = 558 
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
            super(SParser.Native_category_bindingsContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Native_category_binding_listContext

        def DEF(self):
            return self.getToken(SParser.DEF, 0)

        def BINDINGS(self):
            return self.getToken(SParser.BINDINGS, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def CLASS(self):
            return self.getToken(SParser.CLASS, 0)

        def CATEGORY(self):
            return self.getToken(SParser.CATEGORY, 0)

        def native_category_binding_list(self):
            return self.getTypedRuleContext(SParser.Native_category_binding_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_native_category_bindings

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNative_category_bindings(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNative_category_bindings(self)




    def native_category_bindings(self):

        localctx = SParser.Native_category_bindingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_native_category_bindings)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            self.match(SParser.DEF)
            self.state = 561
            _la = self._input.LA(1)
            if not(_la==SParser.CATEGORY or _la==SParser.CLASS):
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 562
            self.match(SParser.BINDINGS)
            self.state = 563
            self.match(SParser.COLON)
            self.state = 564 
            self.indent()
            self.state = 565 
            localctx.items = self.native_category_binding_list(0)
            self.state = 566 
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
            super(SParser.Native_category_binding_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_native_category_binding_list

     
        def copyFrom(self, ctx):
            super(SParser.Native_category_binding_listContext, self).copyFrom(ctx)


    class NativeCategoryBindingListItemContext(Native_category_binding_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_category_binding_listContext)
            super(SParser.NativeCategoryBindingListItemContext, self).__init__(parser)
            self.items = None # Native_category_binding_listContext
            self.item = None # Native_category_bindingContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def native_category_binding_list(self):
            return self.getTypedRuleContext(SParser.Native_category_binding_listContext,0)

        def native_category_binding(self):
            return self.getTypedRuleContext(SParser.Native_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNativeCategoryBindingListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNativeCategoryBindingListItem(self)


    class NativeCategoryBindingListContext(Native_category_binding_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_category_binding_listContext)
            super(SParser.NativeCategoryBindingListContext, self).__init__(parser)
            self.item = None # Native_category_bindingContext
            self.copyFrom(ctx)

        def native_category_binding(self):
            return self.getTypedRuleContext(SParser.Native_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNativeCategoryBindingList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNativeCategoryBindingList(self)



    def native_category_binding_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Native_category_binding_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_native_category_binding_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.NativeCategoryBindingListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 569 
            localctx.item = self.native_category_binding()
            self._ctx.stop = self._input.LT(-1)
            self.state = 577
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.NativeCategoryBindingListItemContext(self, SParser.Native_category_binding_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_category_binding_list)
                    self.state = 571
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 572 
                    self.lfp()
                    self.state = 573 
                    localctx.item = self.native_category_binding() 
                self.state = 579
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Attribute_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Attribute_listContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Variable_identifier_listContext

        def variable_identifier_list(self):
            return self.getTypedRuleContext(SParser.Variable_identifier_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_attribute_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAttribute_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAttribute_list(self)




    def attribute_list(self):

        localctx = SParser.Attribute_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_attribute_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580 
            localctx.items = self.variable_identifier_list(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Abstract_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Abstract_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Argument_listContext
            self.typ = None # TypedefContext

        def ABSTRACT(self):
            return self.getToken(SParser.ABSTRACT, 0)

        def DEF(self):
            return self.getToken(SParser.DEF, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def method_identifier(self):
            return self.getTypedRuleContext(SParser.Method_identifierContext,0)


        def RARROW(self):
            return self.getToken(SParser.RARROW, 0)

        def argument_list(self):
            return self.getTypedRuleContext(SParser.Argument_listContext,0)


        def typedef(self):
            return self.getTypedRuleContext(SParser.TypedefContext,0)


        def getRuleIndex(self):
            return SParser.RULE_abstract_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAbstract_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAbstract_method_declaration(self)




    def abstract_method_declaration(self):

        localctx = SParser.Abstract_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_abstract_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 582
            self.match(SParser.ABSTRACT)
            self.state = 583
            self.match(SParser.DEF)
            self.state = 584 
            localctx.name = self.method_identifier()
            self.state = 585
            self.match(SParser.LPAR)
            self.state = 587
            _la = self._input.LA(1)
            if _la==SParser.CODE or _la==SParser.MUTABLE or _la==SParser.VARIABLE_IDENTIFIER:
                self.state = 586 
                localctx.args = self.argument_list(0)


            self.state = 589
            self.match(SParser.RPAR)
            self.state = 592
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 590
                self.match(SParser.RARROW)
                self.state = 591 
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
            super(SParser.Concrete_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Argument_listContext
            self.typ = None # TypedefContext
            self.stmts = None # Statement_listContext

        def DEF(self):
            return self.getToken(SParser.DEF, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def method_identifier(self):
            return self.getTypedRuleContext(SParser.Method_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def RARROW(self):
            return self.getToken(SParser.RARROW, 0)

        def argument_list(self):
            return self.getTypedRuleContext(SParser.Argument_listContext,0)


        def typedef(self):
            return self.getTypedRuleContext(SParser.TypedefContext,0)


        def getRuleIndex(self):
            return SParser.RULE_concrete_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterConcrete_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitConcrete_method_declaration(self)




    def concrete_method_declaration(self):

        localctx = SParser.Concrete_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_concrete_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self.match(SParser.DEF)
            self.state = 595 
            localctx.name = self.method_identifier()
            self.state = 596
            self.match(SParser.LPAR)
            self.state = 598
            _la = self._input.LA(1)
            if _la==SParser.CODE or _la==SParser.MUTABLE or _la==SParser.VARIABLE_IDENTIFIER:
                self.state = 597 
                localctx.args = self.argument_list(0)


            self.state = 600
            self.match(SParser.RPAR)
            self.state = 603
            _la = self._input.LA(1)
            if _la==SParser.RARROW:
                self.state = 601
                self.match(SParser.RARROW)
                self.state = 602 
                localctx.typ = self.typedef(0)


            self.state = 605
            self.match(SParser.COLON)
            self.state = 606 
            self.indent()
            self.state = 607 
            localctx.stmts = self.statement_list(0)
            self.state = 608 
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
            super(SParser.Native_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Method_identifierContext
            self.args = None # Argument_listContext
            self.typ = None # Category_or_any_typeContext
            self.stmts = None # Native_statement_listContext

        def DEF(self):
            return self.getToken(SParser.DEF, 0)

        def NATIVE(self):
            return self.getToken(SParser.NATIVE, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def method_identifier(self):
            return self.getTypedRuleContext(SParser.Method_identifierContext,0)


        def native_statement_list(self):
            return self.getTypedRuleContext(SParser.Native_statement_listContext,0)


        def RARROW(self):
            return self.getToken(SParser.RARROW, 0)

        def argument_list(self):
            return self.getTypedRuleContext(SParser.Argument_listContext,0)


        def category_or_any_type(self):
            return self.getTypedRuleContext(SParser.Category_or_any_typeContext,0)


        def getRuleIndex(self):
            return SParser.RULE_native_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNative_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNative_method_declaration(self)




    def native_method_declaration(self):

        localctx = SParser.Native_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_native_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 610
            self.match(SParser.DEF)
            self.state = 611
            self.match(SParser.NATIVE)
            self.state = 612 
            localctx.name = self.method_identifier()
            self.state = 613
            self.match(SParser.LPAR)
            self.state = 615
            _la = self._input.LA(1)
            if _la==SParser.CODE or _la==SParser.MUTABLE or _la==SParser.VARIABLE_IDENTIFIER:
                self.state = 614 
                localctx.args = self.argument_list(0)


            self.state = 617
            self.match(SParser.RPAR)
            self.state = 620
            _la = self._input.LA(1)
            if _la==SParser.RARROW:
                self.state = 618
                self.match(SParser.RARROW)
                self.state = 619 
                localctx.typ = self.category_or_any_type()


            self.state = 622
            self.match(SParser.COLON)
            self.state = 623 
            self.indent()
            self.state = 624 
            localctx.stmts = self.native_statement_list(0)
            self.state = 625 
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
            super(SParser.Test_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.stmts = None # Statement_listContext
            self.exps = None # Assertion_listContext
            self.error = None # Symbol_identifierContext

        def DEF(self):
            return self.getToken(SParser.DEF, 0)

        def TEST(self):
            return self.getToken(SParser.TEST, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(SParser.COLON)
            else:
                return self.getToken(SParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.IndentContext)
            else:
                return self.getTypedRuleContext(SParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.DedentContext)
            else:
                return self.getTypedRuleContext(SParser.DedentContext,i)


        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)


        def VERIFYING(self):
            return self.getToken(SParser.VERIFYING, 0)

        def TEXT_LITERAL(self):
            return self.getToken(SParser.TEXT_LITERAL, 0)

        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def assertion_list(self):
            return self.getTypedRuleContext(SParser.Assertion_listContext,0)


        def symbol_identifier(self):
            return self.getTypedRuleContext(SParser.Symbol_identifierContext,0)


        def getRuleIndex(self):
            return SParser.RULE_test_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTest_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTest_method_declaration(self)




    def test_method_declaration(self):

        localctx = SParser.Test_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_test_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 627
            self.match(SParser.DEF)
            self.state = 628
            self.match(SParser.TEST)
            self.state = 629
            localctx.name = self.match(SParser.TEXT_LITERAL)
            self.state = 630
            self.match(SParser.LPAR)
            self.state = 631
            self.match(SParser.RPAR)
            self.state = 632
            self.match(SParser.COLON)
            self.state = 633 
            self.indent()
            self.state = 634 
            localctx.stmts = self.statement_list(0)
            self.state = 635 
            self.dedent()
            self.state = 636 
            self.lfp()
            self.state = 637
            self.match(SParser.VERIFYING)
            self.state = 638
            self.match(SParser.COLON)
            self.state = 644
            token = self._input.LA(1)
            if token in [SParser.LF]:
                self.state = 639 
                self.indent()
                self.state = 640 
                localctx.exps = self.assertion_list(0)
                self.state = 641 
                self.dedent()

            elif token in [SParser.SYMBOL_IDENTIFIER]:
                self.state = 643 
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
            super(SParser.AssertionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_assertion

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAssertion(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAssertion(self)




    def assertion(self):

        localctx = SParser.AssertionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 646 
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
            super(SParser.Typed_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.typ = None # Category_or_any_typeContext
            self.attrs = None # Attribute_listContext
            self.value = None # Literal_expressionContext

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def category_or_any_type(self):
            return self.getTypedRuleContext(SParser.Category_or_any_typeContext,0)


        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def EQ(self):
            return self.getToken(SParser.EQ, 0)

        def attribute_list(self):
            return self.getTypedRuleContext(SParser.Attribute_listContext,0)


        def literal_expression(self):
            return self.getTypedRuleContext(SParser.Literal_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_typed_argument

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTyped_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTyped_argument(self)




    def typed_argument(self):

        localctx = SParser.Typed_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_typed_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 648 
            localctx.name = self.variable_identifier()
            self.state = 649
            self.match(SParser.COLON)
            self.state = 650 
            localctx.typ = self.category_or_any_type()
            self.state = 655
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 651
                self.match(SParser.LPAR)
                self.state = 652 
                localctx.attrs = self.attribute_list()
                self.state = 653
                self.match(SParser.RPAR)


            self.state = 659
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 657
                self.match(SParser.EQ)
                self.state = 658 
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
            super(SParser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_statement

     
        def copyFrom(self, ctx):
            super(SParser.StatementContext, self).copyFrom(ctx)



    class CommentStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.CommentStatementContext, self).__init__(parser)
            self.decl = None # Comment_statementContext
            self.copyFrom(ctx)

        def comment_statement(self):
            return self.getTypedRuleContext(SParser.Comment_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCommentStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCommentStatement(self)


    class StoreStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.StoreStatementContext, self).__init__(parser)
            self.stmt = None # Store_statementContext
            self.copyFrom(ctx)

        def store_statement(self):
            return self.getTypedRuleContext(SParser.Store_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterStoreStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitStoreStatement(self)


    class WithSingletonStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.WithSingletonStatementContext, self).__init__(parser)
            self.stmt = None # With_singleton_statementContext
            self.copyFrom(ctx)

        def with_singleton_statement(self):
            return self.getTypedRuleContext(SParser.With_singleton_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterWithSingletonStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitWithSingletonStatement(self)


    class WriteStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.WriteStatementContext, self).__init__(parser)
            self.stmt = None # Write_statementContext
            self.copyFrom(ctx)

        def write_statement(self):
            return self.getTypedRuleContext(SParser.Write_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterWriteStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitWriteStatement(self)


    class WhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.WhileStatementContext, self).__init__(parser)
            self.stmt = None # While_statementContext
            self.copyFrom(ctx)

        def while_statement(self):
            return self.getTypedRuleContext(SParser.While_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitWhileStatement(self)


    class WithResourceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.WithResourceStatementContext, self).__init__(parser)
            self.stmt = None # With_resource_statementContext
            self.copyFrom(ctx)

        def with_resource_statement(self):
            return self.getTypedRuleContext(SParser.With_resource_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterWithResourceStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitWithResourceStatement(self)


    class RaiseStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.RaiseStatementContext, self).__init__(parser)
            self.stmt = None # Raise_statementContext
            self.copyFrom(ctx)

        def raise_statement(self):
            return self.getTypedRuleContext(SParser.Raise_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterRaiseStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitRaiseStatement(self)


    class AssignInstanceStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.AssignInstanceStatementContext, self).__init__(parser)
            self.stmt = None # Assign_instance_statementContext
            self.copyFrom(ctx)

        def assign_instance_statement(self):
            return self.getTypedRuleContext(SParser.Assign_instance_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAssignInstanceStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAssignInstanceStatement(self)


    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.IfStatementContext, self).__init__(parser)
            self.stmt = None # If_statementContext
            self.copyFrom(ctx)

        def if_statement(self):
            return self.getTypedRuleContext(SParser.If_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIfStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIfStatement(self)


    class SwitchStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.SwitchStatementContext, self).__init__(parser)
            self.stmt = None # Switch_statementContext
            self.copyFrom(ctx)

        def switch_statement(self):
            return self.getTypedRuleContext(SParser.Switch_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSwitchStatement(self)


    class TryStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.TryStatementContext, self).__init__(parser)
            self.stmt = None # Try_statementContext
            self.copyFrom(ctx)

        def try_statement(self):
            return self.getTypedRuleContext(SParser.Try_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTryStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTryStatement(self)


    class MethodCallStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.MethodCallStatementContext, self).__init__(parser)
            self.stmt = None # Method_callContext
            self.copyFrom(ctx)

        def method_call(self):
            return self.getTypedRuleContext(SParser.Method_callContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMethodCallStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMethodCallStatement(self)


    class ReturnStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.ReturnStatementContext, self).__init__(parser)
            self.stmt = None # Return_statementContext
            self.copyFrom(ctx)

        def return_statement(self):
            return self.getTypedRuleContext(SParser.Return_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitReturnStatement(self)


    class AssignTupleStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.AssignTupleStatementContext, self).__init__(parser)
            self.stmt = None # Assign_tuple_statementContext
            self.copyFrom(ctx)

        def assign_tuple_statement(self):
            return self.getTypedRuleContext(SParser.Assign_tuple_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAssignTupleStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAssignTupleStatement(self)


    class ClosureStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.ClosureStatementContext, self).__init__(parser)
            self.decl = None # Concrete_method_declarationContext
            self.copyFrom(ctx)

        def concrete_method_declaration(self):
            return self.getTypedRuleContext(SParser.Concrete_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterClosureStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitClosureStatement(self)


    class DoWhileStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.DoWhileStatementContext, self).__init__(parser)
            self.stmt = None # Do_while_statementContext
            self.copyFrom(ctx)

        def do_while_statement(self):
            return self.getTypedRuleContext(SParser.Do_while_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDoWhileStatement(self)


    class ForEachStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.ForEachStatementContext, self).__init__(parser)
            self.stmt = None # For_each_statementContext
            self.copyFrom(ctx)

        def for_each_statement(self):
            return self.getTypedRuleContext(SParser.For_each_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterForEachStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitForEachStatement(self)



    def statement(self):

        localctx = SParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_statement)
        try:
            self.state = 678
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                localctx = SParser.MethodCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 661 
                localctx.stmt = self.method_call()
                pass

            elif la_ == 2:
                localctx = SParser.AssignInstanceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 662 
                localctx.stmt = self.assign_instance_statement()
                pass

            elif la_ == 3:
                localctx = SParser.AssignTupleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 663 
                localctx.stmt = self.assign_tuple_statement()
                pass

            elif la_ == 4:
                localctx = SParser.StoreStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 664 
                localctx.stmt = self.store_statement()
                pass

            elif la_ == 5:
                localctx = SParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 665 
                localctx.stmt = self.return_statement()
                pass

            elif la_ == 6:
                localctx = SParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 666 
                localctx.stmt = self.if_statement()
                pass

            elif la_ == 7:
                localctx = SParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 667 
                localctx.stmt = self.switch_statement()
                pass

            elif la_ == 8:
                localctx = SParser.ForEachStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 668 
                localctx.stmt = self.for_each_statement()
                pass

            elif la_ == 9:
                localctx = SParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 669 
                localctx.stmt = self.while_statement()
                pass

            elif la_ == 10:
                localctx = SParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 670 
                localctx.stmt = self.do_while_statement()
                pass

            elif la_ == 11:
                localctx = SParser.RaiseStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 671 
                localctx.stmt = self.raise_statement()
                pass

            elif la_ == 12:
                localctx = SParser.TryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 672 
                localctx.stmt = self.try_statement()
                pass

            elif la_ == 13:
                localctx = SParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 673 
                localctx.stmt = self.write_statement()
                pass

            elif la_ == 14:
                localctx = SParser.WithResourceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 674 
                localctx.stmt = self.with_resource_statement()
                pass

            elif la_ == 15:
                localctx = SParser.WithSingletonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 675 
                localctx.stmt = self.with_singleton_statement()
                pass

            elif la_ == 16:
                localctx = SParser.ClosureStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 676 
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 17:
                localctx = SParser.CommentStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 677 
                localctx.decl = self.comment_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Store_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Store_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.to_del = None # Expression_listContext
            self.to_add = None # Expression_listContext

        def DELETE(self):
            return self.getToken(SParser.DELETE, 0)

        def LPAR(self, i=None):
            if i is None:
                return self.getTokens(SParser.LPAR)
            else:
                return self.getToken(SParser.LPAR, i)

        def RPAR(self, i=None):
            if i is None:
                return self.getTokens(SParser.RPAR)
            else:
                return self.getToken(SParser.RPAR, i)

        def expression_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Expression_listContext)
            else:
                return self.getTypedRuleContext(SParser.Expression_listContext,i)


        def STORE(self):
            return self.getToken(SParser.STORE, 0)

        def AND(self):
            return self.getToken(SParser.AND, 0)

        def getRuleIndex(self):
            return SParser.RULE_store_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterStore_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitStore_statement(self)




    def store_statement(self):

        localctx = SParser.Store_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_store_statement)
        try:
            self.state = 700
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 680
                self.match(SParser.DELETE)
                self.state = 681
                self.match(SParser.LPAR)
                self.state = 682 
                localctx.to_del = self.expression_list(0)
                self.state = 683
                self.match(SParser.RPAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 685
                self.match(SParser.STORE)
                self.state = 686
                self.match(SParser.LPAR)
                self.state = 687 
                localctx.to_add = self.expression_list(0)
                self.state = 688
                self.match(SParser.RPAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 690
                self.match(SParser.DELETE)
                self.state = 691
                self.match(SParser.LPAR)
                self.state = 692 
                localctx.to_del = self.expression_list(0)
                self.state = 693
                self.match(SParser.RPAR)
                self.state = 694
                self.match(SParser.AND)
                self.state = 695
                self.match(SParser.STORE)
                self.state = 696
                self.match(SParser.LPAR)
                self.state = 697 
                localctx.to_add = self.expression_list(0)
                self.state = 698
                self.match(SParser.RPAR)
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
            super(SParser.Method_callContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.method = None # Method_selectorContext
            self.args = None # Argument_assignment_listContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def method_selector(self):
            return self.getTypedRuleContext(SParser.Method_selectorContext,0)


        def argument_assignment_list(self):
            return self.getTypedRuleContext(SParser.Argument_assignment_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_method_call

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMethod_call(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMethod_call(self)




    def method_call(self):

        localctx = SParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 702 
            localctx.method = self.method_selector()
            self.state = 703
            self.match(SParser.LPAR)
            self.state = 705
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (SParser.EXECUTE - 95)) | (1 << (SParser.FETCH - 95)) | (1 << (SParser.MUTABLE - 95)) | (1 << (SParser.NONE - 95)) | (1 << (SParser.NOT - 95)) | (1 << (SParser.READ - 95)) | (1 << (SParser.SELF - 95)) | (1 << (SParser.SORTED - 95)) | (1 << (SParser.THIS - 95)) | (1 << (SParser.BOOLEAN_LITERAL - 95)) | (1 << (SParser.CHAR_LITERAL - 95)) | (1 << (SParser.MIN_INTEGER - 95)) | (1 << (SParser.MAX_INTEGER - 95)) | (1 << (SParser.SYMBOL_IDENTIFIER - 95)) | (1 << (SParser.TYPE_IDENTIFIER - 95)) | (1 << (SParser.VARIABLE_IDENTIFIER - 95)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (SParser.TEXT_LITERAL - 160)) | (1 << (SParser.INTEGER_LITERAL - 160)) | (1 << (SParser.HEXA_LITERAL - 160)) | (1 << (SParser.DECIMAL_LITERAL - 160)) | (1 << (SParser.DATETIME_LITERAL - 160)) | (1 << (SParser.TIME_LITERAL - 160)) | (1 << (SParser.DATE_LITERAL - 160)) | (1 << (SParser.PERIOD_LITERAL - 160)))) != 0):
                self.state = 704 
                localctx.args = self.argument_assignment_list(0)


            self.state = 707
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Method_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_method_selector

     
        def copyFrom(self, ctx):
            super(SParser.Method_selectorContext, self).copyFrom(ctx)



    class MethodParentContext(Method_selectorContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_selectorContext)
            super(SParser.MethodParentContext, self).__init__(parser)
            self.parent = None # Callable_parentContext
            self.name = None # Method_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def callable_parent(self):
            return self.getTypedRuleContext(SParser.Callable_parentContext,0)

        def method_identifier(self):
            return self.getTypedRuleContext(SParser.Method_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMethodParent(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMethodParent(self)


    class MethodNameContext(Method_selectorContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_selectorContext)
            super(SParser.MethodNameContext, self).__init__(parser)
            self.name = None # Method_identifierContext
            self.copyFrom(ctx)

        def method_identifier(self):
            return self.getTypedRuleContext(SParser.Method_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMethodName(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMethodName(self)



    def method_selector(self):

        localctx = SParser.Method_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_method_selector)
        try:
            self.state = 714
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                localctx = SParser.MethodNameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 709 
                localctx.name = self.method_identifier()
                pass

            elif la_ == 2:
                localctx = SParser.MethodParentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 710 
                localctx.parent = self.callable_parent(0)
                self.state = 711
                self.match(SParser.DOT)
                self.state = 712 
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
            super(SParser.Callable_parentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_callable_parent

     
        def copyFrom(self, ctx):
            super(SParser.Callable_parentContext, self).copyFrom(ctx)


    class CallableSelectorContext(Callable_parentContext):

        def __init__(self, parser, ctx): # actually a SParser.Callable_parentContext)
            super(SParser.CallableSelectorContext, self).__init__(parser)
            self.parent = None # Callable_parentContext
            self.select = None # Callable_selectorContext
            self.copyFrom(ctx)

        def callable_parent(self):
            return self.getTypedRuleContext(SParser.Callable_parentContext,0)

        def callable_selector(self):
            return self.getTypedRuleContext(SParser.Callable_selectorContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCallableSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCallableSelector(self)


    class CallableRootContext(Callable_parentContext):

        def __init__(self, parser, ctx): # actually a SParser.Callable_parentContext)
            super(SParser.CallableRootContext, self).__init__(parser)
            self.name = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(SParser.IdentifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCallableRoot(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCallableRoot(self)



    def callable_parent(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Callable_parentContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_callable_parent, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.CallableRootContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 717 
            localctx.name = self.identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 723
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CallableSelectorContext(self, SParser.Callable_parentContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_callable_parent)
                    self.state = 719
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 720 
                    localctx.select = self.callable_selector() 
                self.state = 725
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Callable_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Callable_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_callable_selector

     
        def copyFrom(self, ctx):
            super(SParser.Callable_selectorContext, self).copyFrom(ctx)



    class CallableItemSelectorContext(Callable_selectorContext):

        def __init__(self, parser, ctx): # actually a SParser.Callable_selectorContext)
            super(SParser.CallableItemSelectorContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCallableItemSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCallableItemSelector(self)


    class CallableMemberSelectorContext(Callable_selectorContext):

        def __init__(self, parser, ctx): # actually a SParser.Callable_selectorContext)
            super(SParser.CallableMemberSelectorContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCallableMemberSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCallableMemberSelector(self)



    def callable_selector(self):

        localctx = SParser.Callable_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_callable_selector)
        try:
            self.state = 732
            token = self._input.LA(1)
            if token in [SParser.DOT]:
                localctx = SParser.CallableMemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 726
                self.match(SParser.DOT)
                self.state = 727 
                localctx.name = self.variable_identifier()

            elif token in [SParser.LBRAK]:
                localctx = SParser.CallableItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 728
                self.match(SParser.LBRAK)
                self.state = 729 
                localctx.exp = self.expression(0)
                self.state = 730
                self.match(SParser.RBRAK)

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
            super(SParser.With_resource_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmt = None # Assign_variable_statementContext
            self.stmts = None # Statement_listContext

        def WITH(self):
            return self.getToken(SParser.WITH, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def assign_variable_statement(self):
            return self.getTypedRuleContext(SParser.Assign_variable_statementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_with_resource_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterWith_resource_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitWith_resource_statement(self)




    def with_resource_statement(self):

        localctx = SParser.With_resource_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_with_resource_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 734
            self.match(SParser.WITH)
            self.state = 735 
            localctx.stmt = self.assign_variable_statement()
            self.state = 736
            self.match(SParser.COLON)
            self.state = 737 
            self.indent()
            self.state = 738 
            localctx.stmts = self.statement_list(0)
            self.state = 739 
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
            super(SParser.With_singleton_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # Type_identifierContext
            self.stmts = None # Statement_listContext

        def WITH(self):
            return self.getToken(SParser.WITH, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(SParser.Type_identifierContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_with_singleton_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterWith_singleton_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitWith_singleton_statement(self)




    def with_singleton_statement(self):

        localctx = SParser.With_singleton_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_with_singleton_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 741
            self.match(SParser.WITH)
            self.state = 742 
            localctx.typ = self.type_identifier()
            self.state = 743
            self.match(SParser.COLON)
            self.state = 744 
            self.indent()
            self.state = 745 
            localctx.stmts = self.statement_list(0)
            self.state = 746 
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
            super(SParser.Switch_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.cases = None # Switch_case_statement_listContext
            self.stmts = None # Statement_listContext

        def SWITCH(self):
            return self.getToken(SParser.SWITCH, 0)

        def ON(self):
            return self.getToken(SParser.ON, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(SParser.COLON)
            else:
                return self.getToken(SParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.IndentContext)
            else:
                return self.getTypedRuleContext(SParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.DedentContext)
            else:
                return self.getTypedRuleContext(SParser.DedentContext,i)


        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def switch_case_statement_list(self):
            return self.getTypedRuleContext(SParser.Switch_case_statement_listContext,0)


        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)


        def OTHERWISE(self):
            return self.getToken(SParser.OTHERWISE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_switch_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSwitch_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSwitch_statement(self)




    def switch_statement(self):

        localctx = SParser.Switch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_switch_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 748
            self.match(SParser.SWITCH)
            self.state = 749
            self.match(SParser.ON)
            self.state = 750 
            localctx.exp = self.expression(0)
            self.state = 751
            self.match(SParser.COLON)
            self.state = 752 
            self.indent()
            self.state = 753 
            localctx.cases = self.switch_case_statement_list(0)
            self.state = 761
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 754 
                self.lfp()
                self.state = 755
                self.match(SParser.OTHERWISE)
                self.state = 756
                self.match(SParser.COLON)
                self.state = 757 
                self.indent()
                self.state = 758 
                localctx.stmts = self.statement_list(0)
                self.state = 759 
                self.dedent()


            self.state = 763 
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
            super(SParser.Switch_case_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_switch_case_statement

     
        def copyFrom(self, ctx):
            super(SParser.Switch_case_statementContext, self).copyFrom(ctx)



    class AtomicSwitchCaseContext(Switch_case_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Switch_case_statementContext)
            super(SParser.AtomicSwitchCaseContext, self).__init__(parser)
            self.exp = None # Atomic_literalContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def WHEN(self):
            return self.getToken(SParser.WHEN, 0)
        def COLON(self):
            return self.getToken(SParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)

        def atomic_literal(self):
            return self.getTypedRuleContext(SParser.Atomic_literalContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAtomicSwitchCase(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAtomicSwitchCase(self)


    class CollectionSwitchCaseContext(Switch_case_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Switch_case_statementContext)
            super(SParser.CollectionSwitchCaseContext, self).__init__(parser)
            self.exp = None # Literal_collectionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def WHEN(self):
            return self.getToken(SParser.WHEN, 0)
        def IN(self):
            return self.getToken(SParser.IN, 0)
        def COLON(self):
            return self.getToken(SParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)

        def literal_collection(self):
            return self.getTypedRuleContext(SParser.Literal_collectionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCollectionSwitchCase(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCollectionSwitchCase(self)



    def switch_case_statement(self):

        localctx = SParser.Switch_case_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_switch_case_statement)
        try:
            self.state = 780
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                localctx = SParser.AtomicSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 765
                self.match(SParser.WHEN)
                self.state = 766 
                localctx.exp = self.atomic_literal()
                self.state = 767
                self.match(SParser.COLON)
                self.state = 768 
                self.indent()
                self.state = 769 
                localctx.stmts = self.statement_list(0)
                self.state = 770 
                self.dedent()
                pass

            elif la_ == 2:
                localctx = SParser.CollectionSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 772
                self.match(SParser.WHEN)
                self.state = 773
                self.match(SParser.IN)
                self.state = 774 
                localctx.exp = self.literal_collection()
                self.state = 775
                self.match(SParser.COLON)
                self.state = 776 
                self.indent()
                self.state = 777 
                localctx.stmts = self.statement_list(0)
                self.state = 778 
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
            super(SParser.For_each_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name1 = None # Variable_identifierContext
            self.name2 = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.stmts = None # Statement_listContext

        def FOR(self):
            return self.getToken(SParser.FOR, 0)

        def IN(self):
            return self.getToken(SParser.IN, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(SParser.Variable_identifierContext,i)


        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)

        def getRuleIndex(self):
            return SParser.RULE_for_each_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterFor_each_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitFor_each_statement(self)




    def for_each_statement(self):

        localctx = SParser.For_each_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_for_each_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 782
            self.match(SParser.FOR)
            self.state = 783 
            localctx.name1 = self.variable_identifier()
            self.state = 786
            _la = self._input.LA(1)
            if _la==SParser.COMMA:
                self.state = 784
                self.match(SParser.COMMA)
                self.state = 785 
                localctx.name2 = self.variable_identifier()


            self.state = 788
            self.match(SParser.IN)
            self.state = 789 
            localctx.source = self.expression(0)
            self.state = 790
            self.match(SParser.COLON)
            self.state = 791 
            self.indent()
            self.state = 792 
            localctx.stmts = self.statement_list(0)
            self.state = 793 
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
            super(SParser.Do_while_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmts = None # Statement_listContext
            self.exp = None # ExpressionContext

        def DO(self):
            return self.getToken(SParser.DO, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)


        def WHILE(self):
            return self.getToken(SParser.WHILE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_do_while_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDo_while_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDo_while_statement(self)




    def do_while_statement(self):

        localctx = SParser.Do_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_do_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 795
            self.match(SParser.DO)
            self.state = 796
            self.match(SParser.COLON)
            self.state = 797 
            self.indent()
            self.state = 798 
            localctx.stmts = self.statement_list(0)
            self.state = 799 
            self.dedent()
            self.state = 800 
            self.lfp()
            self.state = 801
            self.match(SParser.WHILE)
            self.state = 802 
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
            super(SParser.While_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext

        def WHILE(self):
            return self.getToken(SParser.WHILE, 0)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)


        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)


        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_while_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitWhile_statement(self)




    def while_statement(self):

        localctx = SParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 804
            self.match(SParser.WHILE)
            self.state = 805 
            localctx.exp = self.expression(0)
            self.state = 806
            self.match(SParser.COLON)
            self.state = 807 
            self.indent()
            self.state = 808 
            localctx.stmts = self.statement_list(0)
            self.state = 809 
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
            super(SParser.If_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.elseIfs = None # Else_if_statement_listContext
            self.elseStmts = None # Statement_listContext

        def IF(self):
            return self.getToken(SParser.IF, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(SParser.COLON)
            else:
                return self.getToken(SParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.IndentContext)
            else:
                return self.getTypedRuleContext(SParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.DedentContext)
            else:
                return self.getTypedRuleContext(SParser.DedentContext,i)


        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def statement_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(SParser.Statement_listContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.LfpContext)
            else:
                return self.getTypedRuleContext(SParser.LfpContext,i)


        def ELSE(self):
            return self.getToken(SParser.ELSE, 0)

        def else_if_statement_list(self):
            return self.getTypedRuleContext(SParser.Else_if_statement_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_if_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIf_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = SParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 811
            self.match(SParser.IF)
            self.state = 812 
            localctx.exp = self.expression(0)
            self.state = 813
            self.match(SParser.COLON)
            self.state = 814 
            self.indent()
            self.state = 815 
            localctx.stmts = self.statement_list(0)
            self.state = 816 
            self.dedent()
            self.state = 820
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 817 
                self.lfp()
                self.state = 818 
                localctx.elseIfs = self.else_if_statement_list(0)


            self.state = 829
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 822 
                self.lfp()
                self.state = 823
                self.match(SParser.ELSE)
                self.state = 824
                self.match(SParser.COLON)
                self.state = 825 
                self.indent()
                self.state = 826 
                localctx.elseStmts = self.statement_list(0)
                self.state = 827 
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
            super(SParser.Else_if_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_else_if_statement_list

     
        def copyFrom(self, ctx):
            super(SParser.Else_if_statement_listContext, self).copyFrom(ctx)


    class ElseIfStatementListContext(Else_if_statement_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Else_if_statement_listContext)
            super(SParser.ElseIfStatementListContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def ELSE(self):
            return self.getToken(SParser.ELSE, 0)
        def IF(self):
            return self.getToken(SParser.IF, 0)
        def COLON(self):
            return self.getToken(SParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterElseIfStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitElseIfStatementList(self)


    class ElseIfStatementListItemContext(Else_if_statement_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Else_if_statement_listContext)
            super(SParser.ElseIfStatementListItemContext, self).__init__(parser)
            self.items = None # Else_if_statement_listContext
            self.exp = None # ExpressionContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def ELSE(self):
            return self.getToken(SParser.ELSE, 0)
        def IF(self):
            return self.getToken(SParser.IF, 0)
        def COLON(self):
            return self.getToken(SParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)

        def else_if_statement_list(self):
            return self.getTypedRuleContext(SParser.Else_if_statement_listContext,0)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterElseIfStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitElseIfStatementListItem(self)



    def else_if_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Else_if_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_else_if_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.ElseIfStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 832
            self.match(SParser.ELSE)
            self.state = 833
            self.match(SParser.IF)
            self.state = 834 
            localctx.exp = self.expression(0)
            self.state = 835
            self.match(SParser.COLON)
            self.state = 836 
            self.indent()
            self.state = 837 
            localctx.stmts = self.statement_list(0)
            self.state = 838 
            self.dedent()
            self._ctx.stop = self._input.LT(-1)
            self.state = 852
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.ElseIfStatementListItemContext(self, SParser.Else_if_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_else_if_statement_list)
                    self.state = 840
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 841 
                    self.lfp()
                    self.state = 842
                    self.match(SParser.ELSE)
                    self.state = 843
                    self.match(SParser.IF)
                    self.state = 844 
                    localctx.exp = self.expression(0)
                    self.state = 845
                    self.match(SParser.COLON)
                    self.state = 846 
                    self.indent()
                    self.state = 847 
                    localctx.stmts = self.statement_list(0)
                    self.state = 848 
                    self.dedent() 
                self.state = 854
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Raise_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Raise_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def RAISE(self):
            return self.getToken(SParser.RAISE, 0)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_raise_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterRaise_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitRaise_statement(self)




    def raise_statement(self):

        localctx = SParser.Raise_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_raise_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 855
            self.match(SParser.RAISE)
            self.state = 856 
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
            super(SParser.Try_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Statement_listContext
            self.handlers = None # Catch_statement_listContext
            self.anyStmts = None # Statement_listContext
            self.finalStmts = None # Statement_listContext

        def TRY(self):
            return self.getToken(SParser.TRY, 0)

        def COLON(self, i=None):
            if i is None:
                return self.getTokens(SParser.COLON)
            else:
                return self.getToken(SParser.COLON, i)

        def indent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.IndentContext)
            else:
                return self.getTypedRuleContext(SParser.IndentContext,i)


        def dedent(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.DedentContext)
            else:
                return self.getTypedRuleContext(SParser.DedentContext,i)


        def lfs(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.LfsContext)
            else:
                return self.getTypedRuleContext(SParser.LfsContext,i)


        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def statement_list(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(SParser.Statement_listContext,i)


        def EXCEPT(self):
            return self.getToken(SParser.EXCEPT, 0)

        def FINALLY(self):
            return self.getToken(SParser.FINALLY, 0)

        def catch_statement_list(self):
            return self.getTypedRuleContext(SParser.Catch_statement_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_try_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTry_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTry_statement(self)




    def try_statement(self):

        localctx = SParser.Try_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_try_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 858
            self.match(SParser.TRY)
            self.state = 859 
            localctx.name = self.variable_identifier()
            self.state = 860
            self.match(SParser.COLON)
            self.state = 861 
            self.indent()
            self.state = 862 
            localctx.stmts = self.statement_list(0)
            self.state = 863 
            self.dedent()
            self.state = 864 
            self.lfs()
            self.state = 866
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 865 
                localctx.handlers = self.catch_statement_list(0)


            self.state = 875
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 868
                self.match(SParser.EXCEPT)
                self.state = 869
                self.match(SParser.COLON)
                self.state = 870 
                self.indent()
                self.state = 871 
                localctx.anyStmts = self.statement_list(0)
                self.state = 872 
                self.dedent()
                self.state = 873 
                self.lfs()


            self.state = 884
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 877
                self.match(SParser.FINALLY)
                self.state = 878
                self.match(SParser.COLON)
                self.state = 879 
                self.indent()
                self.state = 880 
                localctx.finalStmts = self.statement_list(0)
                self.state = 881 
                self.dedent()
                self.state = 882 
                self.lfs()


            self.state = 886 
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
            super(SParser.Catch_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_catch_statement

     
        def copyFrom(self, ctx):
            super(SParser.Catch_statementContext, self).copyFrom(ctx)



    class CatchAtomicStatementContext(Catch_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Catch_statementContext)
            super(SParser.CatchAtomicStatementContext, self).__init__(parser)
            self.name = None # Symbol_identifierContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def EXCEPT(self):
            return self.getToken(SParser.EXCEPT, 0)
        def COLON(self):
            return self.getToken(SParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)

        def lfs(self):
            return self.getTypedRuleContext(SParser.LfsContext,0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(SParser.Symbol_identifierContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCatchAtomicStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCatchAtomicStatement(self)


    class CatchCollectionStatementContext(Catch_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Catch_statementContext)
            super(SParser.CatchCollectionStatementContext, self).__init__(parser)
            self.exp = None # Symbol_listContext
            self.stmts = None # Statement_listContext
            self.copyFrom(ctx)

        def EXCEPT(self):
            return self.getToken(SParser.EXCEPT, 0)
        def IN(self):
            return self.getToken(SParser.IN, 0)
        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)
        def COLON(self):
            return self.getToken(SParser.COLON, 0)
        def indent(self):
            return self.getTypedRuleContext(SParser.IndentContext,0)

        def dedent(self):
            return self.getTypedRuleContext(SParser.DedentContext,0)

        def lfs(self):
            return self.getTypedRuleContext(SParser.LfsContext,0)

        def symbol_list(self):
            return self.getTypedRuleContext(SParser.Symbol_listContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCatchCollectionStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCatchCollectionStatement(self)



    def catch_statement(self):

        localctx = SParser.Catch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_catch_statement)
        try:
            self.state = 907
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                localctx = SParser.CatchAtomicStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 888
                self.match(SParser.EXCEPT)
                self.state = 889 
                localctx.name = self.symbol_identifier()
                self.state = 890
                self.match(SParser.COLON)
                self.state = 891 
                self.indent()
                self.state = 892 
                localctx.stmts = self.statement_list(0)
                self.state = 893 
                self.dedent()
                self.state = 894 
                self.lfs()
                pass

            elif la_ == 2:
                localctx = SParser.CatchCollectionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 896
                self.match(SParser.EXCEPT)
                self.state = 897
                self.match(SParser.IN)
                self.state = 898
                self.match(SParser.LBRAK)
                self.state = 899 
                localctx.exp = self.symbol_list(0)
                self.state = 900
                self.match(SParser.RBRAK)
                self.state = 901
                self.match(SParser.COLON)
                self.state = 902 
                self.indent()
                self.state = 903 
                localctx.stmts = self.statement_list(0)
                self.state = 904 
                self.dedent()
                self.state = 905 
                self.lfs()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Return_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def RETURN(self):
            return self.getToken(SParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_return_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitReturn_statement(self)




    def return_statement(self):

        localctx = SParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 909
            self.match(SParser.RETURN)
            self.state = 911
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 910 
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
            super(SParser.ExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_expression

     
        def copyFrom(self, ctx):
            super(SParser.ExpressionContext, self).copyFrom(ctx)


    class IntDivideExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.IntDivideExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def idivide(self):
            return self.getTypedRuleContext(SParser.IdivideContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIntDivideExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIntDivideExpression(self)


    class TernaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.TernaryExpressionContext, self).__init__(parser)
            self.ifTrue = None # ExpressionContext
            self.test = None # ExpressionContext
            self.ifFalse = None # ExpressionContext
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(SParser.IF, 0)
        def ELSE(self):
            return self.getToken(SParser.ELSE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTernaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTernaryExpression(self)


    class ContainsAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.ContainsAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(SParser.CONTAINS, 0)
        def ALL(self):
            return self.getToken(SParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterContainsAllExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitContainsAllExpression(self)


    class NotEqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.NotEqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def XEQ(self):
            return self.getToken(SParser.XEQ, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNotEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNotEqualsExpression(self)


    class InExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.InExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(SParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterInExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitInExpression(self)


    class NotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.NotExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(SParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNotExpression(self)


    class GreaterThanExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.GreaterThanExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def GT(self):
            return self.getToken(SParser.GT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterGreaterThanExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitGreaterThanExpression(self)


    class OrExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.OrExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def OR(self):
            return self.getToken(SParser.OR, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterOrExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitOrExpression(self)


    class CodeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.CodeExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(SParser.CODE, 0)
        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCodeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCodeExpression(self)


    class LessThanOrEqualExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.LessThanOrEqualExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LTE(self):
            return self.getToken(SParser.LTE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterLessThanOrEqualExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitLessThanOrEqualExpression(self)


    class AndExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.AndExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def AND(self):
            return self.getToken(SParser.AND, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAndExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAndExpression(self)


    class ClosureExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.ClosureExpressionContext, self).__init__(parser)
            self.exp = None # Closure_expressionContext
            self.copyFrom(ctx)

        def closure_expression(self):
            return self.getTypedRuleContext(SParser.Closure_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterClosureExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitClosureExpression(self)


    class NotContainsAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.NotContainsAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(SParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(SParser.CONTAINS, 0)
        def ANY(self):
            return self.getToken(SParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNotContainsAnyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNotContainsAnyExpression(self)


    class ContainsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.ContainsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(SParser.CONTAINS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterContainsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitContainsExpression(self)


    class NotContainsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.NotContainsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(SParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(SParser.CONTAINS, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNotContainsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNotContainsExpression(self)


    class MultiplyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.MultiplyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def multiply(self):
            return self.getTypedRuleContext(SParser.MultiplyContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMultiplyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMultiplyExpression(self)


    class RoughlyEqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.RoughlyEqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def TEQ(self):
            return self.getToken(SParser.TEQ, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterRoughlyEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitRoughlyEqualsExpression(self)


    class ExecuteExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.ExecuteExpressionContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def EXECUTE(self):
            return self.getToken(SParser.EXECUTE, 0)
        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterExecuteExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitExecuteExpression(self)


    class MethodExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.MethodExpressionContext, self).__init__(parser)
            self.exp = None # Method_expressionContext
            self.copyFrom(ctx)

        def method_expression(self):
            return self.getTypedRuleContext(SParser.Method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMethodExpression(self)


    class GreaterThanOrEqualExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.GreaterThanOrEqualExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def GTE(self):
            return self.getToken(SParser.GTE, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterGreaterThanOrEqualExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitGreaterThanOrEqualExpression(self)


    class NotInExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.NotInExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(SParser.NOT, 0)
        def IN(self):
            return self.getToken(SParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNotInExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNotInExpression(self)


    class IteratorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.IteratorExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.name = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(SParser.FOR, 0)
        def IN(self):
            return self.getToken(SParser.IN, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)

        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIteratorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIteratorExpression(self)


    class IsNotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.IsNotExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Is_expressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(SParser.IS, 0)
        def NOT(self):
            return self.getToken(SParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)

        def is_expression(self):
            return self.getTypedRuleContext(SParser.Is_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIsNotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIsNotExpression(self)


    class DivideExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.DivideExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def divide(self):
            return self.getTypedRuleContext(SParser.DivideContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDivideExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDivideExpression(self)


    class IsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.IsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Is_expressionContext
            self.copyFrom(ctx)

        def IS(self):
            return self.getToken(SParser.IS, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)

        def is_expression(self):
            return self.getTypedRuleContext(SParser.Is_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIsExpression(self)


    class MinusExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.MinusExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(SParser.MINUS, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMinusExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMinusExpression(self)


    class AddExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.AddExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.op = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(SParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(SParser.MINUS, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAddExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAddExpression(self)


    class NotContainsAllExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.NotContainsAllExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(SParser.NOT, 0)
        def CONTAINS(self):
            return self.getToken(SParser.CONTAINS, 0)
        def ALL(self):
            return self.getToken(SParser.ALL, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNotContainsAllExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNotContainsAllExpression(self)


    class InstanceExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.InstanceExpressionContext, self).__init__(parser)
            self.exp = None # Instance_expressionContext
            self.copyFrom(ctx)

        def instance_expression(self):
            return self.getTypedRuleContext(SParser.Instance_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterInstanceExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitInstanceExpression(self)


    class ContainsAnyExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.ContainsAnyExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def CONTAINS(self):
            return self.getToken(SParser.CONTAINS, 0)
        def ANY(self):
            return self.getToken(SParser.ANY, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterContainsAnyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitContainsAnyExpression(self)


    class CastExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.CastExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # Category_or_any_typeContext
            self.copyFrom(ctx)

        def AS(self):
            return self.getToken(SParser.AS, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)

        def category_or_any_type(self):
            return self.getTypedRuleContext(SParser.Category_or_any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCastExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCastExpression(self)


    class ModuloExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.ModuloExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def modulo(self):
            return self.getTypedRuleContext(SParser.ModuloContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterModuloExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitModuloExpression(self)


    class LessThanExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.LessThanExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(SParser.LT, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterLessThanExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitLessThanExpression(self)


    class EqualsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SParser.ExpressionContext)
            super(SParser.EqualsExpressionContext, self).__init__(parser)
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def EQ2(self):
            return self.getToken(SParser.EQ2, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitEqualsExpression(self)



    def expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 931
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                localctx = SParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 914
                self.match(SParser.MINUS)
                self.state = 915 
                localctx.exp = self.expression(32)
                pass

            elif la_ == 2:
                localctx = SParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 916
                self.match(SParser.NOT)
                self.state = 917 
                localctx.exp = self.expression(31)
                pass

            elif la_ == 3:
                localctx = SParser.InstanceExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 918 
                localctx.exp = self.instance_expression(0)
                pass

            elif la_ == 4:
                localctx = SParser.MethodExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 919 
                localctx.exp = self.method_expression()
                pass

            elif la_ == 5:
                localctx = SParser.CodeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 920
                self.match(SParser.CODE)
                self.state = 921
                self.match(SParser.LPAR)
                self.state = 922 
                localctx.exp = self.expression(0)
                self.state = 923
                self.match(SParser.RPAR)
                pass

            elif la_ == 6:
                localctx = SParser.ExecuteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 925
                self.match(SParser.EXECUTE)
                self.state = 926
                self.match(SParser.LPAR)
                self.state = 927 
                localctx.name = self.variable_identifier()
                self.state = 928
                self.match(SParser.RPAR)
                pass

            elif la_ == 7:
                localctx = SParser.ClosureExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 930 
                localctx.exp = self.closure_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1035
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1033
                    la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                    if la_ == 1:
                        localctx = SParser.MultiplyExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 933
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 934 
                        self.multiply()
                        self.state = 935 
                        localctx.right = self.expression(31)
                        pass

                    elif la_ == 2:
                        localctx = SParser.DivideExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 937
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 938 
                        self.divide()
                        self.state = 939 
                        localctx.right = self.expression(30)
                        pass

                    elif la_ == 3:
                        localctx = SParser.ModuloExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 941
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 942 
                        self.modulo()
                        self.state = 943 
                        localctx.right = self.expression(29)
                        pass

                    elif la_ == 4:
                        localctx = SParser.IntDivideExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 945
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 946 
                        self.idivide()
                        self.state = 947 
                        localctx.right = self.expression(28)
                        pass

                    elif la_ == 5:
                        localctx = SParser.AddExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 949
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 950
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SParser.PLUS or _la==SParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 951 
                        localctx.right = self.expression(27)
                        pass

                    elif la_ == 6:
                        localctx = SParser.LessThanExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 952
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 953
                        self.match(SParser.LT)
                        self.state = 954 
                        localctx.right = self.expression(26)
                        pass

                    elif la_ == 7:
                        localctx = SParser.LessThanOrEqualExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 955
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 956
                        self.match(SParser.LTE)
                        self.state = 957 
                        localctx.right = self.expression(25)
                        pass

                    elif la_ == 8:
                        localctx = SParser.GreaterThanExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 958
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 959
                        self.match(SParser.GT)
                        self.state = 960 
                        localctx.right = self.expression(24)
                        pass

                    elif la_ == 9:
                        localctx = SParser.GreaterThanOrEqualExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 961
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 962
                        self.match(SParser.GTE)
                        self.state = 963 
                        localctx.right = self.expression(23)
                        pass

                    elif la_ == 10:
                        localctx = SParser.EqualsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 964
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 965
                        self.match(SParser.EQ2)
                        self.state = 966 
                        localctx.right = self.expression(20)
                        pass

                    elif la_ == 11:
                        localctx = SParser.NotEqualsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 967
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 968
                        self.match(SParser.XEQ)
                        self.state = 969 
                        localctx.right = self.expression(19)
                        pass

                    elif la_ == 12:
                        localctx = SParser.RoughlyEqualsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 970
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 971
                        self.match(SParser.TEQ)
                        self.state = 972 
                        localctx.right = self.expression(18)
                        pass

                    elif la_ == 13:
                        localctx = SParser.OrExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 973
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 974
                        self.match(SParser.OR)
                        self.state = 975 
                        localctx.right = self.expression(17)
                        pass

                    elif la_ == 14:
                        localctx = SParser.AndExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 976
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 977
                        self.match(SParser.AND)
                        self.state = 978 
                        localctx.right = self.expression(16)
                        pass

                    elif la_ == 15:
                        localctx = SParser.TernaryExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.ifTrue = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 979
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 980
                        self.match(SParser.IF)
                        self.state = 981 
                        localctx.test = self.expression(0)
                        self.state = 982
                        self.match(SParser.ELSE)
                        self.state = 983 
                        localctx.ifFalse = self.expression(15)
                        pass

                    elif la_ == 16:
                        localctx = SParser.InExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 985
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 986
                        self.match(SParser.IN)
                        self.state = 987 
                        localctx.right = self.expression(13)
                        pass

                    elif la_ == 17:
                        localctx = SParser.ContainsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 988
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 989
                        self.match(SParser.CONTAINS)
                        self.state = 990 
                        localctx.right = self.expression(12)
                        pass

                    elif la_ == 18:
                        localctx = SParser.ContainsAllExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 991
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 992
                        self.match(SParser.CONTAINS)
                        self.state = 993
                        self.match(SParser.ALL)
                        self.state = 994 
                        localctx.right = self.expression(11)
                        pass

                    elif la_ == 19:
                        localctx = SParser.ContainsAnyExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 995
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 996
                        self.match(SParser.CONTAINS)
                        self.state = 997
                        self.match(SParser.ANY)
                        self.state = 998 
                        localctx.right = self.expression(10)
                        pass

                    elif la_ == 20:
                        localctx = SParser.NotInExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 999
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 1000
                        self.match(SParser.NOT)
                        self.state = 1001
                        self.match(SParser.IN)
                        self.state = 1002 
                        localctx.right = self.expression(9)
                        pass

                    elif la_ == 21:
                        localctx = SParser.NotContainsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1003
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 1004
                        self.match(SParser.NOT)
                        self.state = 1005
                        self.match(SParser.CONTAINS)
                        self.state = 1006 
                        localctx.right = self.expression(8)
                        pass

                    elif la_ == 22:
                        localctx = SParser.NotContainsAllExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1007
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 1008
                        self.match(SParser.NOT)
                        self.state = 1009
                        self.match(SParser.CONTAINS)
                        self.state = 1010
                        self.match(SParser.ALL)
                        self.state = 1011 
                        localctx.right = self.expression(7)
                        pass

                    elif la_ == 23:
                        localctx = SParser.NotContainsAnyExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1012
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 1013
                        self.match(SParser.NOT)
                        self.state = 1014
                        self.match(SParser.CONTAINS)
                        self.state = 1015
                        self.match(SParser.ANY)
                        self.state = 1016 
                        localctx.right = self.expression(6)
                        pass

                    elif la_ == 24:
                        localctx = SParser.IteratorExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.exp = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1017
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1018
                        self.match(SParser.FOR)
                        self.state = 1019 
                        localctx.name = self.variable_identifier()
                        self.state = 1020
                        self.match(SParser.IN)
                        self.state = 1021 
                        localctx.source = self.expression(2)
                        pass

                    elif la_ == 25:
                        localctx = SParser.IsNotExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1023
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 1024
                        self.match(SParser.IS)
                        self.state = 1025
                        self.match(SParser.NOT)
                        self.state = 1026 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 26:
                        localctx = SParser.IsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1027
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 1028
                        self.match(SParser.IS)
                        self.state = 1029 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 27:
                        localctx = SParser.CastExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1030
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 1031
                        self.match(SParser.AS)
                        self.state = 1032 
                        localctx.right = self.category_or_any_type()
                        pass

             
                self.state = 1037
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Closure_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Closure_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Type_identifierContext

        def type_identifier(self):
            return self.getTypedRuleContext(SParser.Type_identifierContext,0)


        def getRuleIndex(self):
            return SParser.RULE_closure_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterClosure_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitClosure_expression(self)




    def closure_expression(self):

        localctx = SParser.Closure_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_closure_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1038 
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
            super(SParser.Instance_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_instance_expression

     
        def copyFrom(self, ctx):
            super(SParser.Instance_expressionContext, self).copyFrom(ctx)


    class SelectorExpressionContext(Instance_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Instance_expressionContext)
            super(SParser.SelectorExpressionContext, self).__init__(parser)
            self.parent = None # Instance_expressionContext
            self.selector = None # Instance_selectorContext
            self.copyFrom(ctx)

        def instance_expression(self):
            return self.getTypedRuleContext(SParser.Instance_expressionContext,0)

        def instance_selector(self):
            return self.getTypedRuleContext(SParser.Instance_selectorContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSelectorExpression(self)


    class SelectableExpressionContext(Instance_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Instance_expressionContext)
            super(SParser.SelectableExpressionContext, self).__init__(parser)
            self.parent = None # Selectable_expressionContext
            self.copyFrom(ctx)

        def selectable_expression(self):
            return self.getTypedRuleContext(SParser.Selectable_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSelectableExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSelectableExpression(self)



    def instance_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Instance_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_instance_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.SelectableExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1041 
            localctx.parent = self.selectable_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1047
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.SelectorExpressionContext(self, SParser.Instance_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_expression)
                    self.state = 1043
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1044 
                    localctx.selector = self.instance_selector() 
                self.state = 1049
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Method_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_method_expression

     
        def copyFrom(self, ctx):
            super(SParser.Method_expressionContext, self).copyFrom(ctx)



    class ReadExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_expressionContext)
            super(SParser.ReadExpressionContext, self).__init__(parser)
            self.exp = None # Read_expressionContext
            self.copyFrom(ctx)

        def read_expression(self):
            return self.getTypedRuleContext(SParser.Read_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterReadExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitReadExpression(self)


    class MethodCallExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_expressionContext)
            super(SParser.MethodCallExpressionContext, self).__init__(parser)
            self.exp = None # Method_callContext
            self.copyFrom(ctx)

        def method_call(self):
            return self.getTypedRuleContext(SParser.Method_callContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMethodCallExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMethodCallExpression(self)


    class FetchExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_expressionContext)
            super(SParser.FetchExpressionContext, self).__init__(parser)
            self.exp = None # Fetch_expressionContext
            self.copyFrom(ctx)

        def fetch_expression(self):
            return self.getTypedRuleContext(SParser.Fetch_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterFetchExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitFetchExpression(self)


    class ConstructorExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_expressionContext)
            super(SParser.ConstructorExpressionContext, self).__init__(parser)
            self.exp = None # Constructor_expressionContext
            self.copyFrom(ctx)

        def constructor_expression(self):
            return self.getTypedRuleContext(SParser.Constructor_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterConstructorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitConstructorExpression(self)


    class DocumentExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_expressionContext)
            super(SParser.DocumentExpressionContext, self).__init__(parser)
            self.exp = None # Document_expressionContext
            self.copyFrom(ctx)

        def document_expression(self):
            return self.getTypedRuleContext(SParser.Document_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDocumentExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDocumentExpression(self)


    class SortedExpressionContext(Method_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_expressionContext)
            super(SParser.SortedExpressionContext, self).__init__(parser)
            self.exp = None # Sorted_expressionContext
            self.copyFrom(ctx)

        def sorted_expression(self):
            return self.getTypedRuleContext(SParser.Sorted_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSortedExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSortedExpression(self)



    def method_expression(self):

        localctx = SParser.Method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_method_expression)
        try:
            self.state = 1056
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                localctx = SParser.DocumentExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1050 
                localctx.exp = self.document_expression()
                pass

            elif la_ == 2:
                localctx = SParser.FetchExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1051 
                localctx.exp = self.fetch_expression()
                pass

            elif la_ == 3:
                localctx = SParser.ReadExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1052 
                localctx.exp = self.read_expression()
                pass

            elif la_ == 4:
                localctx = SParser.SortedExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1053 
                localctx.exp = self.sorted_expression()
                pass

            elif la_ == 5:
                localctx = SParser.MethodCallExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1054 
                localctx.exp = self.method_call()
                pass

            elif la_ == 6:
                localctx = SParser.ConstructorExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1055 
                localctx.exp = self.constructor_expression()
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
            super(SParser.Instance_selectorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_instance_selector

     
        def copyFrom(self, ctx):
            super(SParser.Instance_selectorContext, self).copyFrom(ctx)



    class SliceSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a SParser.Instance_selectorContext)
            super(SParser.SliceSelectorContext, self).__init__(parser)
            self.xslice = None # Slice_argumentsContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)
        def slice_arguments(self):
            return self.getTypedRuleContext(SParser.Slice_argumentsContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSliceSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSliceSelector(self)


    class MemberSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a SParser.Instance_selectorContext)
            super(SParser.MemberSelectorContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMemberSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMemberSelector(self)


    class ItemSelectorContext(Instance_selectorContext):

        def __init__(self, parser, ctx): # actually a SParser.Instance_selectorContext)
            super(SParser.ItemSelectorContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterItemSelector(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitItemSelector(self)



    def instance_selector(self):

        localctx = SParser.Instance_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_instance_selector)
        try:
            self.state = 1071
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                localctx = SParser.MemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1058
                if not self.wasNot(SParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(SParser.WS)")
                self.state = 1059
                self.match(SParser.DOT)
                self.state = 1060 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = SParser.SliceSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1061
                if not self.wasNot(SParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(SParser.WS)")
                self.state = 1062
                self.match(SParser.LBRAK)
                self.state = 1063 
                localctx.xslice = self.slice_arguments()
                self.state = 1064
                self.match(SParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = SParser.ItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1066
                if not self.wasNot(SParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(SParser.WS)")
                self.state = 1067
                self.match(SParser.LBRAK)
                self.state = 1068 
                localctx.exp = self.expression(0)
                self.state = 1069
                self.match(SParser.RBRAK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Document_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Document_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DOCUMENT(self):
            return self.getToken(SParser.DOCUMENT, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def getRuleIndex(self):
            return SParser.RULE_document_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDocument_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDocument_expression(self)




    def document_expression(self):

        localctx = SParser.Document_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_document_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1073
            self.match(SParser.DOCUMENT)
            self.state = 1074
            self.match(SParser.LPAR)
            self.state = 1075
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Constructor_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Constructor_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # Mutable_category_typeContext
            self.args = None # Argument_assignment_listContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def mutable_category_type(self):
            return self.getTypedRuleContext(SParser.Mutable_category_typeContext,0)


        def argument_assignment_list(self):
            return self.getTypedRuleContext(SParser.Argument_assignment_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_constructor_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterConstructor_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitConstructor_expression(self)




    def constructor_expression(self):

        localctx = SParser.Constructor_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_constructor_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1077 
            localctx.typ = self.mutable_category_type()
            self.state = 1078
            self.match(SParser.LPAR)
            self.state = 1080
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (SParser.EXECUTE - 95)) | (1 << (SParser.FETCH - 95)) | (1 << (SParser.MUTABLE - 95)) | (1 << (SParser.NONE - 95)) | (1 << (SParser.NOT - 95)) | (1 << (SParser.READ - 95)) | (1 << (SParser.SELF - 95)) | (1 << (SParser.SORTED - 95)) | (1 << (SParser.THIS - 95)) | (1 << (SParser.BOOLEAN_LITERAL - 95)) | (1 << (SParser.CHAR_LITERAL - 95)) | (1 << (SParser.MIN_INTEGER - 95)) | (1 << (SParser.MAX_INTEGER - 95)) | (1 << (SParser.SYMBOL_IDENTIFIER - 95)) | (1 << (SParser.TYPE_IDENTIFIER - 95)) | (1 << (SParser.VARIABLE_IDENTIFIER - 95)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (SParser.TEXT_LITERAL - 160)) | (1 << (SParser.INTEGER_LITERAL - 160)) | (1 << (SParser.HEXA_LITERAL - 160)) | (1 << (SParser.DECIMAL_LITERAL - 160)) | (1 << (SParser.DATETIME_LITERAL - 160)) | (1 << (SParser.TIME_LITERAL - 160)) | (1 << (SParser.DATE_LITERAL - 160)) | (1 << (SParser.PERIOD_LITERAL - 160)))) != 0):
                self.state = 1079 
                localctx.args = self.argument_assignment_list(0)


            self.state = 1082
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argument_assignment_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Argument_assignment_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_argument_assignment_list

     
        def copyFrom(self, ctx):
            super(SParser.Argument_assignment_listContext, self).copyFrom(ctx)


    class ExpressionAssignmentListContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Argument_assignment_listContext)
            super(SParser.ExpressionAssignmentListContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterExpressionAssignmentList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitExpressionAssignmentList(self)


    class ArgumentAssignmentListContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Argument_assignment_listContext)
            super(SParser.ArgumentAssignmentListContext, self).__init__(parser)
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def argument_assignment(self):
            return self.getTypedRuleContext(SParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterArgumentAssignmentList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitArgumentAssignmentList(self)


    class ArgumentAssignmentListItemContext(Argument_assignment_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Argument_assignment_listContext)
            super(SParser.ArgumentAssignmentListItemContext, self).__init__(parser)
            self.items = None # Argument_assignment_listContext
            self.item = None # Argument_assignmentContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def argument_assignment_list(self):
            return self.getTypedRuleContext(SParser.Argument_assignment_listContext,0)

        def argument_assignment(self):
            return self.getTypedRuleContext(SParser.Argument_assignmentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterArgumentAssignmentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitArgumentAssignmentListItem(self)



    def argument_assignment_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Argument_assignment_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_argument_assignment_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1089
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                localctx = SParser.ExpressionAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1085 
                localctx.exp = self.expression(0)
                self.state = 1086
                if not self.willNotBe(self.equalToken()):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willNotBe($parser.equalToken())")
                pass

            elif la_ == 2:
                localctx = SParser.ArgumentAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1088 
                localctx.item = self.argument_assignment()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1096
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.ArgumentAssignmentListItemContext(self, SParser.Argument_assignment_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_assignment_list)
                    self.state = 1091
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1092
                    self.match(SParser.COMMA)
                    self.state = 1093 
                    localctx.item = self.argument_assignment() 
                self.state = 1098
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Argument_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Argument_assignmentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(SParser.AssignContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_argument_assignment

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterArgument_assignment(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitArgument_assignment(self)




    def argument_assignment(self):

        localctx = SParser.Argument_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_argument_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1099 
            localctx.name = self.variable_identifier()
            self.state = 1100 
            self.assign()
            self.state = 1101 
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Read_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Read_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # ExpressionContext

        def READ(self):
            return self.getToken(SParser.READ, 0)

        def FROM(self):
            return self.getToken(SParser.FROM, 0)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_read_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterRead_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitRead_expression(self)




    def read_expression(self):

        localctx = SParser.Read_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_read_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1103
            self.match(SParser.READ)
            self.state = 1104
            self.match(SParser.FROM)
            self.state = 1105 
            localctx.source = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Write_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Write_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.what = None # ExpressionContext
            self.target = None # ExpressionContext

        def WRITE(self):
            return self.getToken(SParser.WRITE, 0)

        def TO(self):
            return self.getToken(SParser.TO, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SParser.RULE_write_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterWrite_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitWrite_statement(self)




    def write_statement(self):

        localctx = SParser.Write_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_write_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1107
            self.match(SParser.WRITE)
            self.state = 1108 
            localctx.what = self.expression(0)
            self.state = 1109
            self.match(SParser.TO)
            self.state = 1110 
            localctx.target = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fetch_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Fetch_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_fetch_expression

     
        def copyFrom(self, ctx):
            super(SParser.Fetch_expressionContext, self).copyFrom(ctx)



    class FetchOneContext(Fetch_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Fetch_expressionContext)
            super(SParser.FetchOneContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.xfilter = None # ExpressionContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(SParser.FETCH, 0)
        def ONE(self):
            return self.getToken(SParser.ONE, 0)
        def WHERE(self):
            return self.getToken(SParser.WHERE, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)

        def mutable_category_type(self):
            return self.getTypedRuleContext(SParser.Mutable_category_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterFetchOne(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitFetchOne(self)


    class FetchListContext(Fetch_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Fetch_expressionContext)
            super(SParser.FetchListContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.xfilter = None # ExpressionContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(SParser.FETCH, 0)
        def FROM(self):
            return self.getToken(SParser.FROM, 0)
        def WHERE(self):
            return self.getToken(SParser.WHERE, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterFetchList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitFetchList(self)


    class FetchAllContext(Fetch_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Fetch_expressionContext)
            super(SParser.FetchAllContext, self).__init__(parser)
            self.xstart = None # ExpressionContext
            self.xstop = None # ExpressionContext
            self.typ = None # Mutable_category_typeContext
            self.xfilter = None # ExpressionContext
            self.xorder = None # Order_by_listContext
            self.copyFrom(ctx)

        def FETCH(self):
            return self.getToken(SParser.FETCH, 0)
        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)
        def ALL(self):
            return self.getToken(SParser.ALL, 0)
        def ROWS(self):
            return self.getToken(SParser.ROWS, 0)
        def TO(self):
            return self.getToken(SParser.TO, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)

        def WHERE(self):
            return self.getToken(SParser.WHERE, 0)
        def ORDER(self):
            return self.getToken(SParser.ORDER, 0)
        def BY(self):
            return self.getToken(SParser.BY, 0)
        def mutable_category_type(self):
            return self.getTypedRuleContext(SParser.Mutable_category_typeContext,0)

        def order_by_list(self):
            return self.getTypedRuleContext(SParser.Order_by_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterFetchAll(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitFetchAll(self)



    def fetch_expression(self):

        localctx = SParser.Fetch_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_fetch_expression)
        self._la = 0 # Token type
        try:
            self.state = 1149
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                localctx = SParser.FetchListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1112
                self.match(SParser.FETCH)
                self.state = 1113 
                localctx.name = self.variable_identifier()
                self.state = 1114
                self.match(SParser.FROM)
                self.state = 1115 
                localctx.source = self.expression(0)
                self.state = 1116
                self.match(SParser.WHERE)
                self.state = 1117 
                localctx.xfilter = self.expression(0)
                pass

            elif la_ == 2:
                localctx = SParser.FetchOneContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1119
                self.match(SParser.FETCH)
                self.state = 1120
                self.match(SParser.ONE)
                self.state = 1122
                _la = self._input.LA(1)
                if _la==SParser.MUTABLE or _la==SParser.TYPE_IDENTIFIER:
                    self.state = 1121 
                    localctx.typ = self.mutable_category_type()


                self.state = 1124
                self.match(SParser.WHERE)
                self.state = 1125 
                localctx.xfilter = self.expression(0)
                pass

            elif la_ == 3:
                localctx = SParser.FetchAllContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1126
                self.match(SParser.FETCH)
                self.state = 1133
                token = self._input.LA(1)
                if token in [SParser.ALL]:
                    self.state = 1127
                    self.match(SParser.ALL)

                elif token in [SParser.ROWS]:
                    self.state = 1128
                    self.match(SParser.ROWS)
                    self.state = 1129 
                    localctx.xstart = self.expression(0)
                    self.state = 1130
                    self.match(SParser.TO)
                    self.state = 1131 
                    localctx.xstop = self.expression(0)

                else:
                    raise NoViableAltException(self)

                self.state = 1135
                self.match(SParser.LPAR)
                self.state = 1137
                _la = self._input.LA(1)
                if _la==SParser.MUTABLE or _la==SParser.TYPE_IDENTIFIER:
                    self.state = 1136 
                    localctx.typ = self.mutable_category_type()


                self.state = 1139
                self.match(SParser.RPAR)
                self.state = 1142
                la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
                if la_ == 1:
                    self.state = 1140
                    self.match(SParser.WHERE)
                    self.state = 1141 
                    localctx.xfilter = self.expression(0)


                self.state = 1147
                la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                if la_ == 1:
                    self.state = 1144
                    self.match(SParser.ORDER)
                    self.state = 1145
                    self.match(SParser.BY)
                    self.state = 1146 
                    localctx.xorder = self.order_by_list()


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
            super(SParser.Sorted_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.source = None # Instance_expressionContext
            self.key = None # Instance_expressionContext

        def SORTED(self):
            return self.getToken(SParser.SORTED, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def instance_expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Instance_expressionContext)
            else:
                return self.getTypedRuleContext(SParser.Instance_expressionContext,i)


        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)

        def key_token(self):
            return self.getTypedRuleContext(SParser.Key_tokenContext,0)


        def EQ(self):
            return self.getToken(SParser.EQ, 0)

        def getRuleIndex(self):
            return SParser.RULE_sorted_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSorted_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSorted_expression(self)




    def sorted_expression(self):

        localctx = SParser.Sorted_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_sorted_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1151
            self.match(SParser.SORTED)
            self.state = 1152
            self.match(SParser.LPAR)
            self.state = 1153 
            localctx.source = self.instance_expression(0)
            self.state = 1159
            _la = self._input.LA(1)
            if _la==SParser.COMMA:
                self.state = 1154
                self.match(SParser.COMMA)
                self.state = 1155 
                self.key_token()
                self.state = 1156
                self.match(SParser.EQ)
                self.state = 1157 
                localctx.key = self.instance_expression(0)


            self.state = 1161
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_instance_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Assign_instance_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.inst = None # Assignable_instanceContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(SParser.AssignContext,0)


        def assignable_instance(self):
            return self.getTypedRuleContext(SParser.Assignable_instanceContext,0)


        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_assign_instance_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAssign_instance_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAssign_instance_statement(self)




    def assign_instance_statement(self):

        localctx = SParser.Assign_instance_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_assign_instance_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1163 
            localctx.inst = self.assignable_instance(0)
            self.state = 1164 
            self.assign()
            self.state = 1165 
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
            super(SParser.Child_instanceContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_child_instance

     
        def copyFrom(self, ctx):
            super(SParser.Child_instanceContext, self).copyFrom(ctx)



    class MemberInstanceContext(Child_instanceContext):

        def __init__(self, parser, ctx): # actually a SParser.Child_instanceContext)
            super(SParser.MemberInstanceContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMemberInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMemberInstance(self)


    class ItemInstanceContext(Child_instanceContext):

        def __init__(self, parser, ctx): # actually a SParser.Child_instanceContext)
            super(SParser.ItemInstanceContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterItemInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitItemInstance(self)



    def child_instance(self):

        localctx = SParser.Child_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_child_instance)
        try:
            self.state = 1175
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                localctx = SParser.MemberInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1167
                if not self.wasNot(SParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(SParser.WS)")
                self.state = 1168
                self.match(SParser.DOT)
                self.state = 1169 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = SParser.ItemInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1170
                if not self.wasNot(SParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(SParser.WS)")
                self.state = 1171
                self.match(SParser.LBRAK)
                self.state = 1172 
                localctx.exp = self.expression(0)
                self.state = 1173
                self.match(SParser.RBRAK)
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
            super(SParser.Assign_tuple_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Variable_identifier_listContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(SParser.AssignContext,0)


        def variable_identifier_list(self):
            return self.getTypedRuleContext(SParser.Variable_identifier_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_assign_tuple_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAssign_tuple_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAssign_tuple_statement(self)




    def assign_tuple_statement(self):

        localctx = SParser.Assign_tuple_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_assign_tuple_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1177 
            localctx.items = self.variable_identifier_list(0)
            self.state = 1178 
            self.assign()
            self.state = 1179 
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
            super(SParser.LfsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LF(self, i=None):
            if i is None:
                return self.getTokens(SParser.LF)
            else:
                return self.getToken(SParser.LF, i)

        def getRuleIndex(self):
            return SParser.RULE_lfs

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterLfs(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitLfs(self)




    def lfs(self):

        localctx = SParser.LfsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_lfs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1184
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,59,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1181
                    self.match(SParser.LF) 
                self.state = 1186
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,59,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LfpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.LfpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LF(self, i=None):
            if i is None:
                return self.getTokens(SParser.LF)
            else:
                return self.getToken(SParser.LF, i)

        def getRuleIndex(self):
            return SParser.RULE_lfp

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterLfp(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitLfp(self)




    def lfp(self):

        localctx = SParser.LfpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_lfp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1188 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1187
                self.match(SParser.LF)
                self.state = 1190 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SParser.LF):
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
            super(SParser.IndentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(SParser.INDENT, 0)

        def LF(self, i=None):
            if i is None:
                return self.getTokens(SParser.LF)
            else:
                return self.getToken(SParser.LF, i)

        def getRuleIndex(self):
            return SParser.RULE_indent

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIndent(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIndent(self)




    def indent(self):

        localctx = SParser.IndentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_indent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1193 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1192
                self.match(SParser.LF)
                self.state = 1195 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SParser.LF):
                    break

            self.state = 1197
            self.match(SParser.INDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DedentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.DedentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DEDENT(self):
            return self.getToken(SParser.DEDENT, 0)

        def LF(self, i=None):
            if i is None:
                return self.getTokens(SParser.LF)
            else:
                return self.getToken(SParser.LF, i)

        def getRuleIndex(self):
            return SParser.RULE_dedent

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDedent(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDedent(self)




    def dedent(self):

        localctx = SParser.DedentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_dedent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SParser.LF:
                self.state = 1199
                self.match(SParser.LF)
                self.state = 1204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1205
            self.match(SParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Null_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Null_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NONE(self):
            return self.getToken(SParser.NONE, 0)

        def getRuleIndex(self):
            return SParser.RULE_null_literal

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNull_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNull_literal(self)




    def null_literal(self):

        localctx = SParser.Null_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1207
            self.match(SParser.NONE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_declaration_list

     
        def copyFrom(self, ctx):
            super(SParser.Declaration_listContext, self).copyFrom(ctx)



    class FullDeclarationListContext(Declaration_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Declaration_listContext)
            super(SParser.FullDeclarationListContext, self).__init__(parser)
            self.items = None # DeclarationsContext
            self.copyFrom(ctx)

        def lfs(self):
            return self.getTypedRuleContext(SParser.LfsContext,0)

        def EOF(self):
            return self.getToken(SParser.EOF, 0)
        def declarations(self):
            return self.getTypedRuleContext(SParser.DeclarationsContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterFullDeclarationList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitFullDeclarationList(self)



    def declaration_list(self):

        localctx = SParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            localctx = SParser.FullDeclarationListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 1210
            _la = self._input.LA(1)
            if _la==SParser.COMMENT or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (SParser.ABSTRACT - 65)) | (1 << (SParser.ATTR - 65)) | (1 << (SParser.CATEGORY - 65)) | (1 << (SParser.CLASS - 65)) | (1 << (SParser.DEF - 65)) | (1 << (SParser.ENUM - 65)) | (1 << (SParser.NATIVE - 65)))) != 0) or _la==SParser.SINGLETON or _la==SParser.STORABLE:
                self.state = 1209 
                localctx.items = self.declarations(0)


            self.state = 1212 
            self.lfs()
            self.state = 1213
            self.match(SParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.DeclarationsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_declarations

     
        def copyFrom(self, ctx):
            super(SParser.DeclarationsContext, self).copyFrom(ctx)


    class DeclarationListItemContext(DeclarationsContext):

        def __init__(self, parser, ctx): # actually a SParser.DeclarationsContext)
            super(SParser.DeclarationListItemContext, self).__init__(parser)
            self.items = None # DeclarationsContext
            self.item = None # DeclarationContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def declarations(self):
            return self.getTypedRuleContext(SParser.DeclarationsContext,0)

        def declaration(self):
            return self.getTypedRuleContext(SParser.DeclarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDeclarationListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDeclarationListItem(self)


    class DeclarationListContext(DeclarationsContext):

        def __init__(self, parser, ctx): # actually a SParser.DeclarationsContext)
            super(SParser.DeclarationListContext, self).__init__(parser)
            self.item = None # DeclarationContext
            self.copyFrom(ctx)

        def declaration(self):
            return self.getTypedRuleContext(SParser.DeclarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDeclarationList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDeclarationList(self)



    def declarations(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.DeclarationsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 126
        self.enterRecursionRule(localctx, 126, self.RULE_declarations, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.DeclarationListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1216 
            localctx.item = self.declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1224
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.DeclarationListItemContext(self, SParser.DeclarationsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declarations)
                    self.state = 1218
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1219 
                    self.lfp()
                    self.state = 1220 
                    localctx.item = self.declaration() 
                self.state = 1226
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.DeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def attribute_declaration(self):
            return self.getTypedRuleContext(SParser.Attribute_declarationContext,0)


        def category_declaration(self):
            return self.getTypedRuleContext(SParser.Category_declarationContext,0)


        def resource_declaration(self):
            return self.getTypedRuleContext(SParser.Resource_declarationContext,0)


        def enum_declaration(self):
            return self.getTypedRuleContext(SParser.Enum_declarationContext,0)


        def method_declaration(self):
            return self.getTypedRuleContext(SParser.Method_declarationContext,0)


        def comment_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Comment_statementContext)
            else:
                return self.getTypedRuleContext(SParser.Comment_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.LfpContext)
            else:
                return self.getTypedRuleContext(SParser.LfpContext,i)


        def getRuleIndex(self):
            return SParser.RULE_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = SParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SParser.COMMENT:
                self.state = 1227 
                self.comment_statement()
                self.state = 1228 
                self.lfp()
                self.state = 1234
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1240
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                self.state = 1235 
                self.attribute_declaration()
                pass

            elif la_ == 2:
                self.state = 1236 
                self.category_declaration()
                pass

            elif la_ == 3:
                self.state = 1237 
                self.resource_declaration()
                pass

            elif la_ == 4:
                self.state = 1238 
                self.enum_declaration()
                pass

            elif la_ == 5:
                self.state = 1239 
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
            super(SParser.Resource_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.decl = None # Native_resource_declarationContext

        def native_resource_declaration(self):
            return self.getTypedRuleContext(SParser.Native_resource_declarationContext,0)


        def getRuleIndex(self):
            return SParser.RULE_resource_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterResource_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitResource_declaration(self)




    def resource_declaration(self):

        localctx = SParser.Resource_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1242 
            localctx.decl = self.native_resource_declaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Enum_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Enum_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_enum_declaration

     
        def copyFrom(self, ctx):
            super(SParser.Enum_declarationContext, self).copyFrom(ctx)



    class EnumCategoryDeclarationContext(Enum_declarationContext):

        def __init__(self, parser, ctx): # actually a SParser.Enum_declarationContext)
            super(SParser.EnumCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Enum_category_declarationContext
            self.copyFrom(ctx)

        def enum_category_declaration(self):
            return self.getTypedRuleContext(SParser.Enum_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterEnumCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitEnumCategoryDeclaration(self)


    class EnumNativeDeclarationContext(Enum_declarationContext):

        def __init__(self, parser, ctx): # actually a SParser.Enum_declarationContext)
            super(SParser.EnumNativeDeclarationContext, self).__init__(parser)
            self.decl = None # Enum_native_declarationContext
            self.copyFrom(ctx)

        def enum_native_declaration(self):
            return self.getTypedRuleContext(SParser.Enum_native_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterEnumNativeDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitEnumNativeDeclaration(self)



    def enum_declaration(self):

        localctx = SParser.Enum_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_enum_declaration)
        try:
            self.state = 1246
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                localctx = SParser.EnumCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1244 
                localctx.decl = self.enum_category_declaration()
                pass

            elif la_ == 2:
                localctx = SParser.EnumNativeDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1245 
                localctx.decl = self.enum_native_declaration()
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
            super(SParser.Native_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_native_symbol_list

     
        def copyFrom(self, ctx):
            super(SParser.Native_symbol_listContext, self).copyFrom(ctx)


    class NativeSymbolListContext(Native_symbol_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_symbol_listContext)
            super(SParser.NativeSymbolListContext, self).__init__(parser)
            self.item = None # Native_symbolContext
            self.copyFrom(ctx)

        def native_symbol(self):
            return self.getTypedRuleContext(SParser.Native_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNativeSymbolList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNativeSymbolList(self)


    class NativeSymbolListItemContext(Native_symbol_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_symbol_listContext)
            super(SParser.NativeSymbolListItemContext, self).__init__(parser)
            self.items = None # Native_symbol_listContext
            self.item = None # Native_symbolContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def native_symbol_list(self):
            return self.getTypedRuleContext(SParser.Native_symbol_listContext,0)

        def native_symbol(self):
            return self.getTypedRuleContext(SParser.Native_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNativeSymbolListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNativeSymbolListItem(self)



    def native_symbol_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Native_symbol_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 134
        self.enterRecursionRule(localctx, 134, self.RULE_native_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.NativeSymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1249 
            localctx.item = self.native_symbol()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1257
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,68,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.NativeSymbolListItemContext(self, SParser.Native_symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_symbol_list)
                    self.state = 1251
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1252 
                    self.lfp()
                    self.state = 1253 
                    localctx.item = self.native_symbol() 
                self.state = 1259
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,68,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Category_symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Category_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_category_symbol_list

     
        def copyFrom(self, ctx):
            super(SParser.Category_symbol_listContext, self).copyFrom(ctx)


    class CategorySymbolListItemContext(Category_symbol_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Category_symbol_listContext)
            super(SParser.CategorySymbolListItemContext, self).__init__(parser)
            self.items = None # Category_symbol_listContext
            self.item = None # Category_symbolContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def category_symbol_list(self):
            return self.getTypedRuleContext(SParser.Category_symbol_listContext,0)

        def category_symbol(self):
            return self.getTypedRuleContext(SParser.Category_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCategorySymbolListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCategorySymbolListItem(self)


    class CategorySymbolListContext(Category_symbol_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Category_symbol_listContext)
            super(SParser.CategorySymbolListContext, self).__init__(parser)
            self.item = None # Category_symbolContext
            self.copyFrom(ctx)

        def category_symbol(self):
            return self.getTypedRuleContext(SParser.Category_symbolContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCategorySymbolList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCategorySymbolList(self)



    def category_symbol_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Category_symbol_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 136
        self.enterRecursionRule(localctx, 136, self.RULE_category_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.CategorySymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1261 
            localctx.item = self.category_symbol()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,69,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CategorySymbolListItemContext(self, SParser.Category_symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_category_symbol_list)
                    self.state = 1263
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1264 
                    self.lfp()
                    self.state = 1265 
                    localctx.item = self.category_symbol() 
                self.state = 1271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,69,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_symbol_list

     
        def copyFrom(self, ctx):
            super(SParser.Symbol_listContext, self).copyFrom(ctx)


    class SymbolListContext(Symbol_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Symbol_listContext)
            super(SParser.SymbolListContext, self).__init__(parser)
            self.item = None # Symbol_identifierContext
            self.copyFrom(ctx)

        def symbol_identifier(self):
            return self.getTypedRuleContext(SParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSymbolList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSymbolList(self)


    class SymbolListItemContext(Symbol_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Symbol_listContext)
            super(SParser.SymbolListItemContext, self).__init__(parser)
            self.items = None # Symbol_listContext
            self.item = None # Symbol_identifierContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def symbol_list(self):
            return self.getTypedRuleContext(SParser.Symbol_listContext,0)

        def symbol_identifier(self):
            return self.getTypedRuleContext(SParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSymbolListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSymbolListItem(self)



    def symbol_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Symbol_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 138
        self.enterRecursionRule(localctx, 138, self.RULE_symbol_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.SymbolListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1273 
            localctx.item = self.symbol_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1280
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,70,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.SymbolListItemContext(self, SParser.Symbol_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_symbol_list)
                    self.state = 1275
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1276
                    self.match(SParser.COMMA)
                    self.state = 1277 
                    localctx.item = self.symbol_identifier() 
                self.state = 1282
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,70,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Attribute_constraintContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Attribute_constraintContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_attribute_constraint

     
        def copyFrom(self, ctx):
            super(SParser.Attribute_constraintContext, self).copyFrom(ctx)



    class MatchingSetContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a SParser.Attribute_constraintContext)
            super(SParser.MatchingSetContext, self).__init__(parser)
            self.source = None # Set_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(SParser.IN, 0)
        def set_literal(self):
            return self.getTypedRuleContext(SParser.Set_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMatchingSet(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMatchingSet(self)


    class MatchingPatternContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a SParser.Attribute_constraintContext)
            super(SParser.MatchingPatternContext, self).__init__(parser)
            self.text = None # Token
            self.copyFrom(ctx)

        def MATCHING(self):
            return self.getToken(SParser.MATCHING, 0)
        def TEXT_LITERAL(self):
            return self.getToken(SParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMatchingPattern(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMatchingPattern(self)


    class MatchingListContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a SParser.Attribute_constraintContext)
            super(SParser.MatchingListContext, self).__init__(parser)
            self.source = None # List_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(SParser.IN, 0)
        def list_literal(self):
            return self.getTypedRuleContext(SParser.List_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMatchingList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMatchingList(self)


    class MatchingRangeContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a SParser.Attribute_constraintContext)
            super(SParser.MatchingRangeContext, self).__init__(parser)
            self.source = None # Range_literalContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(SParser.IN, 0)
        def range_literal(self):
            return self.getTypedRuleContext(SParser.Range_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMatchingRange(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMatchingRange(self)


    class MatchingExpressionContext(Attribute_constraintContext):

        def __init__(self, parser, ctx): # actually a SParser.Attribute_constraintContext)
            super(SParser.MatchingExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def MATCHING(self):
            return self.getToken(SParser.MATCHING, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMatchingExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMatchingExpression(self)



    def attribute_constraint(self):

        localctx = SParser.Attribute_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_attribute_constraint)
        try:
            self.state = 1293
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                localctx = SParser.MatchingListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1283
                self.match(SParser.IN)
                self.state = 1284 
                localctx.source = self.list_literal()
                pass

            elif la_ == 2:
                localctx = SParser.MatchingSetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1285
                self.match(SParser.IN)
                self.state = 1286 
                localctx.source = self.set_literal()
                pass

            elif la_ == 3:
                localctx = SParser.MatchingRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1287
                self.match(SParser.IN)
                self.state = 1288 
                localctx.source = self.range_literal()
                pass

            elif la_ == 4:
                localctx = SParser.MatchingPatternContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1289
                self.match(SParser.MATCHING)
                self.state = 1290
                localctx.text = self.match(SParser.TEXT_LITERAL)
                pass

            elif la_ == 5:
                localctx = SParser.MatchingExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1291
                self.match(SParser.MATCHING)
                self.state = 1292 
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
            super(SParser.List_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Expression_listContext

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)

        def expression_list(self):
            return self.getTypedRuleContext(SParser.Expression_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_list_literal

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterList_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitList_literal(self)




    def list_literal(self):

        localctx = SParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1295
            self.match(SParser.LBRAK)
            self.state = 1297
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (SParser.EXECUTE - 95)) | (1 << (SParser.FETCH - 95)) | (1 << (SParser.MUTABLE - 95)) | (1 << (SParser.NONE - 95)) | (1 << (SParser.NOT - 95)) | (1 << (SParser.READ - 95)) | (1 << (SParser.SELF - 95)) | (1 << (SParser.SORTED - 95)) | (1 << (SParser.THIS - 95)) | (1 << (SParser.BOOLEAN_LITERAL - 95)) | (1 << (SParser.CHAR_LITERAL - 95)) | (1 << (SParser.MIN_INTEGER - 95)) | (1 << (SParser.MAX_INTEGER - 95)) | (1 << (SParser.SYMBOL_IDENTIFIER - 95)) | (1 << (SParser.TYPE_IDENTIFIER - 95)) | (1 << (SParser.VARIABLE_IDENTIFIER - 95)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (SParser.TEXT_LITERAL - 160)) | (1 << (SParser.INTEGER_LITERAL - 160)) | (1 << (SParser.HEXA_LITERAL - 160)) | (1 << (SParser.DECIMAL_LITERAL - 160)) | (1 << (SParser.DATETIME_LITERAL - 160)) | (1 << (SParser.TIME_LITERAL - 160)) | (1 << (SParser.DATE_LITERAL - 160)) | (1 << (SParser.PERIOD_LITERAL - 160)))) != 0):
                self.state = 1296 
                localctx.items = self.expression_list(0)


            self.state = 1299
            self.match(SParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Set_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Set_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Expression_listContext

        def LT(self):
            return self.getToken(SParser.LT, 0)

        def GT(self):
            return self.getToken(SParser.GT, 0)

        def expression_list(self):
            return self.getTypedRuleContext(SParser.Expression_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_set_literal

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSet_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSet_literal(self)




    def set_literal(self):

        localctx = SParser.Set_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_set_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1301
            self.match(SParser.LT)
            self.state = 1303
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (SParser.EXECUTE - 95)) | (1 << (SParser.FETCH - 95)) | (1 << (SParser.MUTABLE - 95)) | (1 << (SParser.NONE - 95)) | (1 << (SParser.NOT - 95)) | (1 << (SParser.READ - 95)) | (1 << (SParser.SELF - 95)) | (1 << (SParser.SORTED - 95)) | (1 << (SParser.THIS - 95)) | (1 << (SParser.BOOLEAN_LITERAL - 95)) | (1 << (SParser.CHAR_LITERAL - 95)) | (1 << (SParser.MIN_INTEGER - 95)) | (1 << (SParser.MAX_INTEGER - 95)) | (1 << (SParser.SYMBOL_IDENTIFIER - 95)) | (1 << (SParser.TYPE_IDENTIFIER - 95)) | (1 << (SParser.VARIABLE_IDENTIFIER - 95)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (SParser.TEXT_LITERAL - 160)) | (1 << (SParser.INTEGER_LITERAL - 160)) | (1 << (SParser.HEXA_LITERAL - 160)) | (1 << (SParser.DECIMAL_LITERAL - 160)) | (1 << (SParser.DATETIME_LITERAL - 160)) | (1 << (SParser.TIME_LITERAL - 160)) | (1 << (SParser.DATE_LITERAL - 160)) | (1 << (SParser.PERIOD_LITERAL - 160)))) != 0):
                self.state = 1302 
                localctx.items = self.expression_list(0)


            self.state = 1305
            self.match(SParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Expression_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_expression_list

     
        def copyFrom(self, ctx):
            super(SParser.Expression_listContext, self).copyFrom(ctx)


    class ValueListContext(Expression_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Expression_listContext)
            super(SParser.ValueListContext, self).__init__(parser)
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterValueList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitValueList(self)


    class ValueListItemContext(Expression_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Expression_listContext)
            super(SParser.ValueListItemContext, self).__init__(parser)
            self.items = None # Expression_listContext
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def expression_list(self):
            return self.getTypedRuleContext(SParser.Expression_listContext,0)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterValueListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitValueListItem(self)



    def expression_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Expression_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 146
        self.enterRecursionRule(localctx, 146, self.RULE_expression_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.ValueListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1308 
            localctx.item = self.expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1315
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,74,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.ValueListItemContext(self, SParser.Expression_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_list)
                    self.state = 1310
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1311
                    self.match(SParser.COMMA)
                    self.state = 1312 
                    localctx.item = self.expression(0) 
                self.state = 1317
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,74,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Range_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Range_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.low = None # ExpressionContext
            self.high = None # ExpressionContext

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)

        def RANGE(self):
            return self.getToken(SParser.RANGE, 0)

        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SParser.RULE_range_literal

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterRange_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitRange_literal(self)




    def range_literal(self):

        localctx = SParser.Range_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_range_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1318
            self.match(SParser.LBRAK)
            self.state = 1319 
            localctx.low = self.expression(0)
            self.state = 1320
            self.match(SParser.RANGE)
            self.state = 1321 
            localctx.high = self.expression(0)
            self.state = 1322
            self.match(SParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypedefContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.TypedefContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_typedef

     
        def copyFrom(self, ctx):
            super(SParser.TypedefContext, self).copyFrom(ctx)


    class SetTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a SParser.TypedefContext)
            super(SParser.SetTypeContext, self).__init__(parser)
            self.s = None # TypedefContext
            self.copyFrom(ctx)

        def LTGT(self):
            return self.getToken(SParser.LTGT, 0)
        def typedef(self):
            return self.getTypedRuleContext(SParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSetType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSetType(self)


    class ListTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a SParser.TypedefContext)
            super(SParser.ListTypeContext, self).__init__(parser)
            self.l = None # TypedefContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)
        def typedef(self):
            return self.getTypedRuleContext(SParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterListType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitListType(self)


    class DictTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a SParser.TypedefContext)
            super(SParser.DictTypeContext, self).__init__(parser)
            self.d = None # TypedefContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(SParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(SParser.RCURL, 0)
        def typedef(self):
            return self.getTypedRuleContext(SParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDictType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDictType(self)


    class PrimaryTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a SParser.TypedefContext)
            super(SParser.PrimaryTypeContext, self).__init__(parser)
            self.p = None # Primary_typeContext
            self.copyFrom(ctx)

        def primary_type(self):
            return self.getTypedRuleContext(SParser.Primary_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPrimaryType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPrimaryType(self)



    def typedef(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.TypedefContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 150
        self.enterRecursionRule(localctx, 150, self.RULE_typedef, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.PrimaryTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1325 
            localctx.p = self.primary_type()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1337
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,76,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1335
                    la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
                    if la_ == 1:
                        localctx = SParser.SetTypeContext(self, SParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.s = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1327
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1328
                        self.match(SParser.LTGT)
                        pass

                    elif la_ == 2:
                        localctx = SParser.ListTypeContext(self, SParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1329
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1330
                        self.match(SParser.LBRAK)
                        self.state = 1331
                        self.match(SParser.RBRAK)
                        pass

                    elif la_ == 3:
                        localctx = SParser.DictTypeContext(self, SParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.d = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1332
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1333
                        self.match(SParser.LCURL)
                        self.state = 1334
                        self.match(SParser.RCURL)
                        pass

             
                self.state = 1339
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,76,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Primary_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Primary_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_primary_type

     
        def copyFrom(self, ctx):
            super(SParser.Primary_typeContext, self).copyFrom(ctx)



    class NativeTypeContext(Primary_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Primary_typeContext)
            super(SParser.NativeTypeContext, self).__init__(parser)
            self.n = None # Native_typeContext
            self.copyFrom(ctx)

        def native_type(self):
            return self.getTypedRuleContext(SParser.Native_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNativeType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNativeType(self)


    class CategoryTypeContext(Primary_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Primary_typeContext)
            super(SParser.CategoryTypeContext, self).__init__(parser)
            self.c = None # Category_typeContext
            self.copyFrom(ctx)

        def category_type(self):
            return self.getTypedRuleContext(SParser.Category_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCategoryType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCategoryType(self)



    def primary_type(self):

        localctx = SParser.Primary_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_primary_type)
        try:
            self.state = 1342
            token = self._input.LA(1)
            if token in [SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.CODE, SParser.DOCUMENT, SParser.BLOB, SParser.IMAGE, SParser.UUID]:
                localctx = SParser.NativeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1340 
                localctx.n = self.native_type()

            elif token in [SParser.TYPE_IDENTIFIER]:
                localctx = SParser.CategoryTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1341 
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
            super(SParser.Native_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_native_type

     
        def copyFrom(self, ctx):
            super(SParser.Native_typeContext, self).copyFrom(ctx)



    class PeriodTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.PeriodTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PERIOD(self):
            return self.getToken(SParser.PERIOD, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPeriodType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPeriodType(self)


    class BooleanTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.BooleanTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(SParser.BOOLEAN, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterBooleanType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitBooleanType(self)


    class DocumentTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.DocumentTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOCUMENT(self):
            return self.getToken(SParser.DOCUMENT, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDocumentType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDocumentType(self)


    class CharacterTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.CharacterTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHARACTER(self):
            return self.getToken(SParser.CHARACTER, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCharacterType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCharacterType(self)


    class TextTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.TextTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT(self):
            return self.getToken(SParser.TEXT, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTextType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTextType(self)


    class ImageTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.ImageTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def IMAGE(self):
            return self.getToken(SParser.IMAGE, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterImageType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitImageType(self)


    class TimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.TimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TIME(self):
            return self.getToken(SParser.TIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTimeType(self)


    class IntegerTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.IntegerTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(SParser.INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIntegerType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIntegerType(self)


    class DateTimeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.DateTimeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATETIME(self):
            return self.getToken(SParser.DATETIME, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDateTimeType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDateTimeType(self)


    class BlobTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.BlobTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BLOB(self):
            return self.getToken(SParser.BLOB, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterBlobType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitBlobType(self)


    class UUIDTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.UUIDTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def UUID(self):
            return self.getToken(SParser.UUID, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterUUIDType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitUUIDType(self)


    class DecimalTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.DecimalTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL(self):
            return self.getToken(SParser.DECIMAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDecimalType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDecimalType(self)


    class CodeTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.CodeTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CODE(self):
            return self.getToken(SParser.CODE, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCodeType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCodeType(self)


    class DateTypeContext(Native_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_typeContext)
            super(SParser.DateTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DATE(self):
            return self.getToken(SParser.DATE, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDateType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDateType(self)



    def native_type(self):

        localctx = SParser.Native_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_native_type)
        try:
            self.state = 1358
            token = self._input.LA(1)
            if token in [SParser.BOOLEAN]:
                localctx = SParser.BooleanTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1344
                self.match(SParser.BOOLEAN)

            elif token in [SParser.CHARACTER]:
                localctx = SParser.CharacterTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1345
                self.match(SParser.CHARACTER)

            elif token in [SParser.TEXT]:
                localctx = SParser.TextTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1346
                self.match(SParser.TEXT)

            elif token in [SParser.IMAGE]:
                localctx = SParser.ImageTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1347
                self.match(SParser.IMAGE)

            elif token in [SParser.INTEGER]:
                localctx = SParser.IntegerTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1348
                self.match(SParser.INTEGER)

            elif token in [SParser.DECIMAL]:
                localctx = SParser.DecimalTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1349
                self.match(SParser.DECIMAL)

            elif token in [SParser.DOCUMENT]:
                localctx = SParser.DocumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1350
                self.match(SParser.DOCUMENT)

            elif token in [SParser.DATE]:
                localctx = SParser.DateTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1351
                self.match(SParser.DATE)

            elif token in [SParser.DATETIME]:
                localctx = SParser.DateTimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1352
                self.match(SParser.DATETIME)

            elif token in [SParser.TIME]:
                localctx = SParser.TimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1353
                self.match(SParser.TIME)

            elif token in [SParser.PERIOD]:
                localctx = SParser.PeriodTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1354
                self.match(SParser.PERIOD)

            elif token in [SParser.CODE]:
                localctx = SParser.CodeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1355
                self.match(SParser.CODE)

            elif token in [SParser.BLOB]:
                localctx = SParser.BlobTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1356
                self.match(SParser.BLOB)

            elif token in [SParser.UUID]:
                localctx = SParser.UUIDTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1357
                self.match(SParser.UUID)

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
            super(SParser.Category_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def TYPE_IDENTIFIER(self):
            return self.getToken(SParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return SParser.RULE_category_type

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCategory_type(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCategory_type(self)




    def category_type(self):

        localctx = SParser.Category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_category_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1360
            localctx.t1 = self.match(SParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Mutable_category_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Mutable_category_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def category_type(self):
            return self.getTypedRuleContext(SParser.Category_typeContext,0)


        def MUTABLE(self):
            return self.getToken(SParser.MUTABLE, 0)

        def getRuleIndex(self):
            return SParser.RULE_mutable_category_type

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMutable_category_type(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMutable_category_type(self)




    def mutable_category_type(self):

        localctx = SParser.Mutable_category_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_mutable_category_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1363
            _la = self._input.LA(1)
            if _la==SParser.MUTABLE:
                self.state = 1362
                self.match(SParser.MUTABLE)


            self.state = 1365 
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
            super(SParser.Code_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t1 = None # Token

        def CODE(self):
            return self.getToken(SParser.CODE, 0)

        def getRuleIndex(self):
            return SParser.RULE_code_type

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCode_type(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCode_type(self)




    def code_type(self):

        localctx = SParser.Code_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_code_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1367
            localctx.t1 = self.match(SParser.CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Category_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_category_declaration

     
        def copyFrom(self, ctx):
            super(SParser.Category_declarationContext, self).copyFrom(ctx)



    class ConcreteCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a SParser.Category_declarationContext)
            super(SParser.ConcreteCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Concrete_category_declarationContext
            self.copyFrom(ctx)

        def concrete_category_declaration(self):
            return self.getTypedRuleContext(SParser.Concrete_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterConcreteCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitConcreteCategoryDeclaration(self)


    class NativeCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a SParser.Category_declarationContext)
            super(SParser.NativeCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Native_category_declarationContext
            self.copyFrom(ctx)

        def native_category_declaration(self):
            return self.getTypedRuleContext(SParser.Native_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNativeCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNativeCategoryDeclaration(self)


    class SingletonCategoryDeclarationContext(Category_declarationContext):

        def __init__(self, parser, ctx): # actually a SParser.Category_declarationContext)
            super(SParser.SingletonCategoryDeclarationContext, self).__init__(parser)
            self.decl = None # Singleton_category_declarationContext
            self.copyFrom(ctx)

        def singleton_category_declaration(self):
            return self.getTypedRuleContext(SParser.Singleton_category_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSingletonCategoryDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSingletonCategoryDeclaration(self)



    def category_declaration(self):

        localctx = SParser.Category_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_category_declaration)
        try:
            self.state = 1372
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                localctx = SParser.ConcreteCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1369 
                localctx.decl = self.concrete_category_declaration()
                pass

            elif la_ == 2:
                localctx = SParser.NativeCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1370 
                localctx.decl = self.native_category_declaration()
                pass

            elif la_ == 3:
                localctx = SParser.SingletonCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1371 
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
            super(SParser.Type_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_type_identifier_list

     
        def copyFrom(self, ctx):
            super(SParser.Type_identifier_listContext, self).copyFrom(ctx)


    class TypeIdentifierListContext(Type_identifier_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Type_identifier_listContext)
            super(SParser.TypeIdentifierListContext, self).__init__(parser)
            self.item = None # Type_identifierContext
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(SParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTypeIdentifierList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTypeIdentifierList(self)


    class TypeIdentifierListItemContext(Type_identifier_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Type_identifier_listContext)
            super(SParser.TypeIdentifierListItemContext, self).__init__(parser)
            self.items = None # Type_identifier_listContext
            self.item = None # Type_identifierContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def type_identifier_list(self):
            return self.getTypedRuleContext(SParser.Type_identifier_listContext,0)

        def type_identifier(self):
            return self.getTypedRuleContext(SParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTypeIdentifierListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTypeIdentifierListItem(self)



    def type_identifier_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Type_identifier_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 164
        self.enterRecursionRule(localctx, 164, self.RULE_type_identifier_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.TypeIdentifierListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1375 
            localctx.item = self.type_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1382
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,81,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.TypeIdentifierListItemContext(self, SParser.Type_identifier_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_type_identifier_list)
                    self.state = 1377
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1378
                    self.match(SParser.COMMA)
                    self.state = 1379 
                    localctx.item = self.type_identifier() 
                self.state = 1384
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,81,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Method_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Method_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_method_identifier

     
        def copyFrom(self, ctx):
            super(SParser.Method_identifierContext, self).copyFrom(ctx)



    class MethodVariableIdentifierContext(Method_identifierContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_identifierContext)
            super(SParser.MethodVariableIdentifierContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMethodVariableIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMethodVariableIdentifier(self)


    class MethodTypeIdentifierContext(Method_identifierContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_identifierContext)
            super(SParser.MethodTypeIdentifierContext, self).__init__(parser)
            self.name = None # Type_identifierContext
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(SParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMethodTypeIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMethodTypeIdentifier(self)



    def method_identifier(self):

        localctx = SParser.Method_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_method_identifier)
        try:
            self.state = 1387
            token = self._input.LA(1)
            if token in [SParser.VARIABLE_IDENTIFIER]:
                localctx = SParser.MethodVariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1385 
                localctx.name = self.variable_identifier()

            elif token in [SParser.TYPE_IDENTIFIER]:
                localctx = SParser.MethodTypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1386 
                localctx.name = self.type_identifier()

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
            super(SParser.IdentifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_identifier

     
        def copyFrom(self, ctx):
            super(SParser.IdentifierContext, self).copyFrom(ctx)



    class TypeIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a SParser.IdentifierContext)
            super(SParser.TypeIdentifierContext, self).__init__(parser)
            self.name = None # Type_identifierContext
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(SParser.Type_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTypeIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTypeIdentifier(self)


    class SymbolIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a SParser.IdentifierContext)
            super(SParser.SymbolIdentifierContext, self).__init__(parser)
            self.name = None # Symbol_identifierContext
            self.copyFrom(ctx)

        def symbol_identifier(self):
            return self.getTypedRuleContext(SParser.Symbol_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSymbolIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSymbolIdentifier(self)


    class VariableIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a SParser.IdentifierContext)
            super(SParser.VariableIdentifierContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterVariableIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitVariableIdentifier(self)



    def identifier(self):

        localctx = SParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_identifier)
        try:
            self.state = 1392
            token = self._input.LA(1)
            if token in [SParser.VARIABLE_IDENTIFIER]:
                localctx = SParser.VariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1389 
                localctx.name = self.variable_identifier()

            elif token in [SParser.TYPE_IDENTIFIER]:
                localctx = SParser.TypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1390 
                localctx.name = self.type_identifier()

            elif token in [SParser.SYMBOL_IDENTIFIER]:
                localctx = SParser.SymbolIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1391 
                localctx.name = self.symbol_identifier()

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
            super(SParser.Variable_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return SParser.RULE_variable_identifier

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterVariable_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitVariable_identifier(self)




    def variable_identifier(self):

        localctx = SParser.Variable_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_variable_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1394
            self.match(SParser.VARIABLE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Type_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TYPE_IDENTIFIER(self):
            return self.getToken(SParser.TYPE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return SParser.RULE_type_identifier

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterType_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitType_identifier(self)




    def type_identifier(self):

        localctx = SParser.Type_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_type_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1396
            self.match(SParser.TYPE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Symbol_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Symbol_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(SParser.SYMBOL_IDENTIFIER, 0)

        def getRuleIndex(self):
            return SParser.RULE_symbol_identifier

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSymbol_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSymbol_identifier(self)




    def symbol_identifier(self):

        localctx = SParser.Symbol_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_symbol_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1398
            self.match(SParser.SYMBOL_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_argument_list

     
        def copyFrom(self, ctx):
            super(SParser.Argument_listContext, self).copyFrom(ctx)


    class ArgumentListItemContext(Argument_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Argument_listContext)
            super(SParser.ArgumentListItemContext, self).__init__(parser)
            self.items = None # Argument_listContext
            self.item = None # ArgumentContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def argument_list(self):
            return self.getTypedRuleContext(SParser.Argument_listContext,0)

        def argument(self):
            return self.getTypedRuleContext(SParser.ArgumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitArgumentListItem(self)


    class ArgumentListContext(Argument_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Argument_listContext)
            super(SParser.ArgumentListContext, self).__init__(parser)
            self.item = None # ArgumentContext
            self.copyFrom(ctx)

        def argument(self):
            return self.getTypedRuleContext(SParser.ArgumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitArgumentList(self)



    def argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 176
        self.enterRecursionRule(localctx, 176, self.RULE_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.ArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1401 
            localctx.item = self.argument()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1408
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,84,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.ArgumentListItemContext(self, SParser.Argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_list)
                    self.state = 1403
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1404
                    self.match(SParser.COMMA)
                    self.state = 1405 
                    localctx.item = self.argument() 
                self.state = 1410
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,84,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.ArgumentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_argument

     
        def copyFrom(self, ctx):
            super(SParser.ArgumentContext, self).copyFrom(ctx)



    class OperatorArgumentContext(ArgumentContext):

        def __init__(self, parser, ctx): # actually a SParser.ArgumentContext)
            super(SParser.OperatorArgumentContext, self).__init__(parser)
            self.arg = None # Operator_argumentContext
            self.copyFrom(ctx)

        def operator_argument(self):
            return self.getTypedRuleContext(SParser.Operator_argumentContext,0)

        def MUTABLE(self):
            return self.getToken(SParser.MUTABLE, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterOperatorArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitOperatorArgument(self)


    class CodeArgumentContext(ArgumentContext):

        def __init__(self, parser, ctx): # actually a SParser.ArgumentContext)
            super(SParser.CodeArgumentContext, self).__init__(parser)
            self.arg = None # Code_argumentContext
            self.copyFrom(ctx)

        def code_argument(self):
            return self.getTypedRuleContext(SParser.Code_argumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCodeArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCodeArgument(self)



    def argument(self):

        localctx = SParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.state = 1416
            token = self._input.LA(1)
            if token in [SParser.CODE]:
                localctx = SParser.CodeArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1411 
                localctx.arg = self.code_argument()

            elif token in [SParser.MUTABLE, SParser.VARIABLE_IDENTIFIER]:
                localctx = SParser.OperatorArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1413
                _la = self._input.LA(1)
                if _la==SParser.MUTABLE:
                    self.state = 1412
                    self.match(SParser.MUTABLE)


                self.state = 1415 
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
            super(SParser.Operator_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_operator_argument

     
        def copyFrom(self, ctx):
            super(SParser.Operator_argumentContext, self).copyFrom(ctx)



    class TypedArgumentContext(Operator_argumentContext):

        def __init__(self, parser, ctx): # actually a SParser.Operator_argumentContext)
            super(SParser.TypedArgumentContext, self).__init__(parser)
            self.arg = None # Typed_argumentContext
            self.copyFrom(ctx)

        def typed_argument(self):
            return self.getTypedRuleContext(SParser.Typed_argumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTypedArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTypedArgument(self)


    class NamedArgumentContext(Operator_argumentContext):

        def __init__(self, parser, ctx): # actually a SParser.Operator_argumentContext)
            super(SParser.NamedArgumentContext, self).__init__(parser)
            self.arg = None # Named_argumentContext
            self.copyFrom(ctx)

        def named_argument(self):
            return self.getTypedRuleContext(SParser.Named_argumentContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNamedArgument(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNamedArgument(self)



    def operator_argument(self):

        localctx = SParser.Operator_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_operator_argument)
        try:
            self.state = 1420
            la_ = self._interp.adaptivePredict(self._input,87,self._ctx)
            if la_ == 1:
                localctx = SParser.NamedArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1418 
                localctx.arg = self.named_argument()
                pass

            elif la_ == 2:
                localctx = SParser.TypedArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1419 
                localctx.arg = self.typed_argument()
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
            super(SParser.Named_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.value = None # Literal_expressionContext

        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def EQ(self):
            return self.getToken(SParser.EQ, 0)

        def literal_expression(self):
            return self.getTypedRuleContext(SParser.Literal_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_named_argument

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNamed_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNamed_argument(self)




    def named_argument(self):

        localctx = SParser.Named_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_named_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1422 
            localctx.name = self.variable_identifier()
            self.state = 1425
            la_ = self._interp.adaptivePredict(self._input,88,self._ctx)
            if la_ == 1:
                self.state = 1423
                self.match(SParser.EQ)
                self.state = 1424 
                localctx.value = self.literal_expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Code_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Code_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext

        def code_type(self):
            return self.getTypedRuleContext(SParser.Code_typeContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def getRuleIndex(self):
            return SParser.RULE_code_argument

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCode_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCode_argument(self)




    def code_argument(self):

        localctx = SParser.Code_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_code_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1427 
            self.code_type()
            self.state = 1428 
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
            super(SParser.Category_or_any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_category_or_any_type

     
        def copyFrom(self, ctx):
            super(SParser.Category_or_any_typeContext, self).copyFrom(ctx)



    class AnyArgumentTypeContext(Category_or_any_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Category_or_any_typeContext)
            super(SParser.AnyArgumentTypeContext, self).__init__(parser)
            self.typ = None # Any_typeContext
            self.copyFrom(ctx)

        def any_type(self):
            return self.getTypedRuleContext(SParser.Any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAnyArgumentType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAnyArgumentType(self)


    class CategoryArgumentTypeContext(Category_or_any_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Category_or_any_typeContext)
            super(SParser.CategoryArgumentTypeContext, self).__init__(parser)
            self.typ = None # TypedefContext
            self.copyFrom(ctx)

        def typedef(self):
            return self.getTypedRuleContext(SParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCategoryArgumentType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCategoryArgumentType(self)



    def category_or_any_type(self):

        localctx = SParser.Category_or_any_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_category_or_any_type)
        try:
            self.state = 1432
            token = self._input.LA(1)
            if token in [SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.CODE, SParser.DOCUMENT, SParser.BLOB, SParser.IMAGE, SParser.UUID, SParser.TYPE_IDENTIFIER]:
                localctx = SParser.CategoryArgumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1430 
                localctx.typ = self.typedef(0)

            elif token in [SParser.ANY]:
                localctx = SParser.AnyArgumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1431 
                localctx.typ = self.any_type(0)

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
            super(SParser.Any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_any_type

     
        def copyFrom(self, ctx):
            super(SParser.Any_typeContext, self).copyFrom(ctx)


    class AnyListTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Any_typeContext)
            super(SParser.AnyListTypeContext, self).__init__(parser)
            self.typ = None # Any_typeContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)
        def any_type(self):
            return self.getTypedRuleContext(SParser.Any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAnyListType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAnyListType(self)


    class AnyTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Any_typeContext)
            super(SParser.AnyTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ANY(self):
            return self.getToken(SParser.ANY, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAnyType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAnyType(self)


    class AnyDictTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Any_typeContext)
            super(SParser.AnyDictTypeContext, self).__init__(parser)
            self.typ = None # Any_typeContext
            self.copyFrom(ctx)

        def LCURL(self):
            return self.getToken(SParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(SParser.RCURL, 0)
        def any_type(self):
            return self.getTypedRuleContext(SParser.Any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAnyDictType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAnyDictType(self)



    def any_type(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Any_typeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 188
        self.enterRecursionRule(localctx, 188, self.RULE_any_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.AnyTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1435
            self.match(SParser.ANY)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1445
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,91,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1443
                    la_ = self._interp.adaptivePredict(self._input,90,self._ctx)
                    if la_ == 1:
                        localctx = SParser.AnyListTypeContext(self, SParser.Any_typeContext(self, _parentctx, _parentState))
                        localctx.typ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1437
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1438
                        self.match(SParser.LBRAK)
                        self.state = 1439
                        self.match(SParser.RBRAK)
                        pass

                    elif la_ == 2:
                        localctx = SParser.AnyDictTypeContext(self, SParser.Any_typeContext(self, _parentctx, _parentState))
                        localctx.typ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1440
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1441
                        self.match(SParser.LCURL)
                        self.state = 1442
                        self.match(SParser.RCURL)
                        pass

             
                self.state = 1447
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,91,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Member_method_declaration_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Member_method_declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_member_method_declaration_list

     
        def copyFrom(self, ctx):
            super(SParser.Member_method_declaration_listContext, self).copyFrom(ctx)


    class CategoryMethodListItemContext(Member_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Member_method_declaration_listContext)
            super(SParser.CategoryMethodListItemContext, self).__init__(parser)
            self.items = None # Member_method_declaration_listContext
            self.item = None # Member_method_declarationContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def member_method_declaration_list(self):
            return self.getTypedRuleContext(SParser.Member_method_declaration_listContext,0)

        def member_method_declaration(self):
            return self.getTypedRuleContext(SParser.Member_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCategoryMethodListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCategoryMethodListItem(self)


    class CategoryMethodListContext(Member_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Member_method_declaration_listContext)
            super(SParser.CategoryMethodListContext, self).__init__(parser)
            self.item = None # Member_method_declarationContext
            self.copyFrom(ctx)

        def member_method_declaration(self):
            return self.getTypedRuleContext(SParser.Member_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCategoryMethodList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCategoryMethodList(self)



    def member_method_declaration_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Member_method_declaration_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 190
        self.enterRecursionRule(localctx, 190, self.RULE_member_method_declaration_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.CategoryMethodListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1449 
            localctx.item = self.member_method_declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1457
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,92,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CategoryMethodListItemContext(self, SParser.Member_method_declaration_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_member_method_declaration_list)
                    self.state = 1451
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1452 
                    self.lfp()
                    self.state = 1453 
                    localctx.item = self.member_method_declaration() 
                self.state = 1459
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,92,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def setter_method_declaration(self):
            return self.getTypedRuleContext(SParser.Setter_method_declarationContext,0)


        def getter_method_declaration(self):
            return self.getTypedRuleContext(SParser.Getter_method_declarationContext,0)


        def concrete_method_declaration(self):
            return self.getTypedRuleContext(SParser.Concrete_method_declarationContext,0)


        def abstract_method_declaration(self):
            return self.getTypedRuleContext(SParser.Abstract_method_declarationContext,0)


        def operator_method_declaration(self):
            return self.getTypedRuleContext(SParser.Operator_method_declarationContext,0)


        def getRuleIndex(self):
            return SParser.RULE_member_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMember_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMember_method_declaration(self)




    def member_method_declaration(self):

        localctx = SParser.Member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_member_method_declaration)
        try:
            self.state = 1465
            la_ = self._interp.adaptivePredict(self._input,93,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1460 
                self.setter_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1461 
                self.getter_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1462 
                self.concrete_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1463 
                self.abstract_method_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1464 
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
            super(SParser.Native_member_method_declaration_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_native_member_method_declaration_list

     
        def copyFrom(self, ctx):
            super(SParser.Native_member_method_declaration_listContext, self).copyFrom(ctx)


    class NativeCategoryMethodListContext(Native_member_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_member_method_declaration_listContext)
            super(SParser.NativeCategoryMethodListContext, self).__init__(parser)
            self.item = None # Native_member_method_declarationContext
            self.copyFrom(ctx)

        def native_member_method_declaration(self):
            return self.getTypedRuleContext(SParser.Native_member_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNativeCategoryMethodList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNativeCategoryMethodList(self)


    class NativeCategoryMethodListItemContext(Native_member_method_declaration_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_member_method_declaration_listContext)
            super(SParser.NativeCategoryMethodListItemContext, self).__init__(parser)
            self.items = None # Native_member_method_declaration_listContext
            self.item = None # Native_member_method_declarationContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def native_member_method_declaration_list(self):
            return self.getTypedRuleContext(SParser.Native_member_method_declaration_listContext,0)

        def native_member_method_declaration(self):
            return self.getTypedRuleContext(SParser.Native_member_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNativeCategoryMethodListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNativeCategoryMethodListItem(self)



    def native_member_method_declaration_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Native_member_method_declaration_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 194
        self.enterRecursionRule(localctx, 194, self.RULE_native_member_method_declaration_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.NativeCategoryMethodListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1468 
            localctx.item = self.native_member_method_declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1476
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,94,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.NativeCategoryMethodListItemContext(self, SParser.Native_member_method_declaration_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_member_method_declaration_list)
                    self.state = 1470
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1471 
                    self.lfp()
                    self.state = 1472 
                    localctx.item = self.native_member_method_declaration() 
                self.state = 1478
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,94,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Native_member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Native_member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def member_method_declaration(self):
            return self.getTypedRuleContext(SParser.Member_method_declarationContext,0)


        def native_method_declaration(self):
            return self.getTypedRuleContext(SParser.Native_method_declarationContext,0)


        def getRuleIndex(self):
            return SParser.RULE_native_member_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNative_member_method_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNative_member_method_declaration(self)




    def native_member_method_declaration(self):

        localctx = SParser.Native_member_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_native_member_method_declaration)
        try:
            self.state = 1481
            la_ = self._interp.adaptivePredict(self._input,95,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1479 
                self.member_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1480 
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
            super(SParser.Native_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_native_category_binding

     
        def copyFrom(self, ctx):
            super(SParser.Native_category_bindingContext, self).copyFrom(ctx)



    class Python2CategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_category_bindingContext)
            super(SParser.Python2CategoryBindingContext, self).__init__(parser)
            self.binding = None # Python_category_bindingContext
            self.copyFrom(ctx)

        def PYTHON2(self):
            return self.getToken(SParser.PYTHON2, 0)
        def python_category_binding(self):
            return self.getTypedRuleContext(SParser.Python_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPython2CategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPython2CategoryBinding(self)


    class Python3CategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_category_bindingContext)
            super(SParser.Python3CategoryBindingContext, self).__init__(parser)
            self.binding = None # Python_category_bindingContext
            self.copyFrom(ctx)

        def PYTHON3(self):
            return self.getToken(SParser.PYTHON3, 0)
        def python_category_binding(self):
            return self.getTypedRuleContext(SParser.Python_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPython3CategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPython3CategoryBinding(self)


    class JavaCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_category_bindingContext)
            super(SParser.JavaCategoryBindingContext, self).__init__(parser)
            self.binding = None # Java_class_identifier_expressionContext
            self.copyFrom(ctx)

        def JAVA(self):
            return self.getToken(SParser.JAVA, 0)
        def java_class_identifier_expression(self):
            return self.getTypedRuleContext(SParser.Java_class_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaCategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaCategoryBinding(self)


    class CSharpCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_category_bindingContext)
            super(SParser.CSharpCategoryBindingContext, self).__init__(parser)
            self.binding = None # Csharp_identifier_expressionContext
            self.copyFrom(ctx)

        def CSHARP(self):
            return self.getToken(SParser.CSHARP, 0)
        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpCategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpCategoryBinding(self)


    class JavaScriptCategoryBindingContext(Native_category_bindingContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_category_bindingContext)
            super(SParser.JavaScriptCategoryBindingContext, self).__init__(parser)
            self.binding = None # Javascript_category_bindingContext
            self.copyFrom(ctx)

        def JAVASCRIPT(self):
            return self.getToken(SParser.JAVASCRIPT, 0)
        def javascript_category_binding(self):
            return self.getTypedRuleContext(SParser.Javascript_category_bindingContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaScriptCategoryBinding(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaScriptCategoryBinding(self)



    def native_category_binding(self):

        localctx = SParser.Native_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_native_category_binding)
        try:
            self.state = 1493
            token = self._input.LA(1)
            if token in [SParser.JAVA]:
                localctx = SParser.JavaCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1483
                self.match(SParser.JAVA)
                self.state = 1484 
                localctx.binding = self.java_class_identifier_expression(0)

            elif token in [SParser.CSHARP]:
                localctx = SParser.CSharpCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1485
                self.match(SParser.CSHARP)
                self.state = 1486 
                localctx.binding = self.csharp_identifier_expression(0)

            elif token in [SParser.PYTHON2]:
                localctx = SParser.Python2CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1487
                self.match(SParser.PYTHON2)
                self.state = 1488 
                localctx.binding = self.python_category_binding()

            elif token in [SParser.PYTHON3]:
                localctx = SParser.Python3CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1489
                self.match(SParser.PYTHON3)
                self.state = 1490 
                localctx.binding = self.python_category_binding()

            elif token in [SParser.JAVASCRIPT]:
                localctx = SParser.JavaScriptCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1491
                self.match(SParser.JAVASCRIPT)
                self.state = 1492 
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
            super(SParser.Python_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.id_ = None # IdentifierContext
            self.module = None # Python_moduleContext

        def identifier(self):
            return self.getTypedRuleContext(SParser.IdentifierContext,0)


        def python_module(self):
            return self.getTypedRuleContext(SParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return SParser.RULE_python_category_binding

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPython_category_binding(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPython_category_binding(self)




    def python_category_binding(self):

        localctx = SParser.Python_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_python_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1495 
            localctx.id_ = self.identifier()
            self.state = 1497
            la_ = self._interp.adaptivePredict(self._input,97,self._ctx)
            if la_ == 1:
                self.state = 1496 
                localctx.module = self.python_module()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_moduleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Python_moduleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(SParser.FROM, 0)

        def module_token(self):
            return self.getTypedRuleContext(SParser.Module_tokenContext,0)


        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(SParser.IdentifierContext,i)


        def DOT(self, i=None):
            if i is None:
                return self.getTokens(SParser.DOT)
            else:
                return self.getToken(SParser.DOT, i)

        def getRuleIndex(self):
            return SParser.RULE_python_module

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPython_module(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPython_module(self)




    def python_module(self):

        localctx = SParser.Python_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_python_module)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1499
            self.match(SParser.FROM)
            self.state = 1500 
            self.module_token()
            self.state = 1501
            self.match(SParser.COLON)
            self.state = 1502 
            self.identifier()
            self.state = 1507
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,98,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1503
                    self.match(SParser.DOT)
                    self.state = 1504 
                    self.identifier() 
                self.state = 1509
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,98,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Module_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Module_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return SParser.RULE_module_token

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterModule_token(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitModule_token(self)




    def module_token(self):

        localctx = SParser.Module_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_module_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1510
            localctx.i1 = self.match(SParser.VARIABLE_IDENTIFIER)
            self.state = 1511
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

    class Javascript_category_bindingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Javascript_category_bindingContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.id_ = None # IdentifierContext
            self.module = None # Javascript_moduleContext

        def identifier(self):
            return self.getTypedRuleContext(SParser.IdentifierContext,0)


        def javascript_module(self):
            return self.getTypedRuleContext(SParser.Javascript_moduleContext,0)


        def getRuleIndex(self):
            return SParser.RULE_javascript_category_binding

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascript_category_binding(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascript_category_binding(self)




    def javascript_category_binding(self):

        localctx = SParser.Javascript_category_bindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 206, self.RULE_javascript_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1513 
            localctx.id_ = self.identifier()
            self.state = 1515
            la_ = self._interp.adaptivePredict(self._input,99,self._ctx)
            if la_ == 1:
                self.state = 1514 
                localctx.module = self.javascript_module()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_moduleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Javascript_moduleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(SParser.FROM, 0)

        def module_token(self):
            return self.getTypedRuleContext(SParser.Module_tokenContext,0)


        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def javascript_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Javascript_identifierContext)
            else:
                return self.getTypedRuleContext(SParser.Javascript_identifierContext,i)


        def SLASH(self, i=None):
            if i is None:
                return self.getTokens(SParser.SLASH)
            else:
                return self.getToken(SParser.SLASH, i)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)

        def getRuleIndex(self):
            return SParser.RULE_javascript_module

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascript_module(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascript_module(self)




    def javascript_module(self):

        localctx = SParser.Javascript_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_javascript_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1517
            self.match(SParser.FROM)
            self.state = 1518 
            self.module_token()
            self.state = 1519
            self.match(SParser.COLON)
            self.state = 1521
            _la = self._input.LA(1)
            if _la==SParser.SLASH:
                self.state = 1520
                self.match(SParser.SLASH)


            self.state = 1523 
            self.javascript_identifier()
            self.state = 1528
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,101,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1524
                    self.match(SParser.SLASH)
                    self.state = 1525 
                    self.javascript_identifier() 
                self.state = 1530
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,101,self._ctx)

            self.state = 1533
            la_ = self._interp.adaptivePredict(self._input,102,self._ctx)
            if la_ == 1:
                self.state = 1531
                self.match(SParser.DOT)
                self.state = 1532 
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
            super(SParser.Variable_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_variable_identifier_list

     
        def copyFrom(self, ctx):
            super(SParser.Variable_identifier_listContext, self).copyFrom(ctx)


    class VariableListContext(Variable_identifier_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Variable_identifier_listContext)
            super(SParser.VariableListContext, self).__init__(parser)
            self.item = None # Variable_identifierContext
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterVariableList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitVariableList(self)


    class VariableListItemContext(Variable_identifier_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Variable_identifier_listContext)
            super(SParser.VariableListItemContext, self).__init__(parser)
            self.items = None # Variable_identifier_listContext
            self.item = None # Variable_identifierContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def variable_identifier_list(self):
            return self.getTypedRuleContext(SParser.Variable_identifier_listContext,0)

        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterVariableListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitVariableListItem(self)



    def variable_identifier_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Variable_identifier_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 210
        self.enterRecursionRule(localctx, 210, self.RULE_variable_identifier_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.VariableListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1536 
            localctx.item = self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1543
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,103,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.VariableListItemContext(self, SParser.Variable_identifier_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_variable_identifier_list)
                    self.state = 1538
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1539
                    self.match(SParser.COMMA)
                    self.state = 1540 
                    localctx.item = self.variable_identifier() 
                self.state = 1545
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,103,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_method_declaration

     
        def copyFrom(self, ctx):
            super(SParser.Method_declarationContext, self).copyFrom(ctx)



    class NativeMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_declarationContext)
            super(SParser.NativeMethodContext, self).__init__(parser)
            self.decl = None # Native_method_declarationContext
            self.copyFrom(ctx)

        def native_method_declaration(self):
            return self.getTypedRuleContext(SParser.Native_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNativeMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNativeMethod(self)


    class AbstractMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_declarationContext)
            super(SParser.AbstractMethodContext, self).__init__(parser)
            self.decl = None # Abstract_method_declarationContext
            self.copyFrom(ctx)

        def abstract_method_declaration(self):
            return self.getTypedRuleContext(SParser.Abstract_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAbstractMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAbstractMethod(self)


    class ConcreteMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_declarationContext)
            super(SParser.ConcreteMethodContext, self).__init__(parser)
            self.decl = None # Concrete_method_declarationContext
            self.copyFrom(ctx)

        def concrete_method_declaration(self):
            return self.getTypedRuleContext(SParser.Concrete_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterConcreteMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitConcreteMethod(self)


    class TestMethodContext(Method_declarationContext):

        def __init__(self, parser, ctx): # actually a SParser.Method_declarationContext)
            super(SParser.TestMethodContext, self).__init__(parser)
            self.decl = None # Test_method_declarationContext
            self.copyFrom(ctx)

        def test_method_declaration(self):
            return self.getTypedRuleContext(SParser.Test_method_declarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTestMethod(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTestMethod(self)



    def method_declaration(self):

        localctx = SParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_method_declaration)
        try:
            self.state = 1550
            la_ = self._interp.adaptivePredict(self._input,104,self._ctx)
            if la_ == 1:
                localctx = SParser.AbstractMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1546 
                localctx.decl = self.abstract_method_declaration()
                pass

            elif la_ == 2:
                localctx = SParser.ConcreteMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1547 
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 3:
                localctx = SParser.NativeMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1548 
                localctx.decl = self.native_method_declaration()
                pass

            elif la_ == 4:
                localctx = SParser.TestMethodContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1549 
                localctx.decl = self.test_method_declaration()
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
            super(SParser.Comment_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(SParser.COMMENT, 0)

        def getRuleIndex(self):
            return SParser.RULE_comment_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterComment_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitComment_statement(self)




    def comment_statement(self):

        localctx = SParser.Comment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_comment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1552
            self.match(SParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Native_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_native_statement_list

     
        def copyFrom(self, ctx):
            super(SParser.Native_statement_listContext, self).copyFrom(ctx)


    class NativeStatementListItemContext(Native_statement_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_statement_listContext)
            super(SParser.NativeStatementListItemContext, self).__init__(parser)
            self.items = None # Native_statement_listContext
            self.item = None # Native_statementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def native_statement_list(self):
            return self.getTypedRuleContext(SParser.Native_statement_listContext,0)

        def native_statement(self):
            return self.getTypedRuleContext(SParser.Native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNativeStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNativeStatementListItem(self)


    class NativeStatementListContext(Native_statement_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_statement_listContext)
            super(SParser.NativeStatementListContext, self).__init__(parser)
            self.item = None # Native_statementContext
            self.copyFrom(ctx)

        def native_statement(self):
            return self.getTypedRuleContext(SParser.Native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNativeStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNativeStatementList(self)



    def native_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Native_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 216
        self.enterRecursionRule(localctx, 216, self.RULE_native_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.NativeStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1555 
            localctx.item = self.native_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1563
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,105,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.NativeStatementListItemContext(self, SParser.Native_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_statement_list)
                    self.state = 1557
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1558 
                    self.lfp()
                    self.state = 1559 
                    localctx.item = self.native_statement() 
                self.state = 1565
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,105,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Native_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_native_statement

     
        def copyFrom(self, ctx):
            super(SParser.Native_statementContext, self).copyFrom(ctx)



    class CSharpNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_statementContext)
            super(SParser.CSharpNativeStatementContext, self).__init__(parser)
            self.stmt = None # Csharp_statementContext
            self.copyFrom(ctx)

        def CSHARP(self):
            return self.getToken(SParser.CSHARP, 0)
        def csharp_statement(self):
            return self.getTypedRuleContext(SParser.Csharp_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpNativeStatement(self)


    class JavaNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_statementContext)
            super(SParser.JavaNativeStatementContext, self).__init__(parser)
            self.stmt = None # Java_statementContext
            self.copyFrom(ctx)

        def JAVA(self):
            return self.getToken(SParser.JAVA, 0)
        def java_statement(self):
            return self.getTypedRuleContext(SParser.Java_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaNativeStatement(self)


    class JavaScriptNativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_statementContext)
            super(SParser.JavaScriptNativeStatementContext, self).__init__(parser)
            self.stmt = None # Javascript_native_statementContext
            self.copyFrom(ctx)

        def JAVASCRIPT(self):
            return self.getToken(SParser.JAVASCRIPT, 0)
        def javascript_native_statement(self):
            return self.getTypedRuleContext(SParser.Javascript_native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaScriptNativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaScriptNativeStatement(self)


    class Python2NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_statementContext)
            super(SParser.Python2NativeStatementContext, self).__init__(parser)
            self.stmt = None # Python_native_statementContext
            self.copyFrom(ctx)

        def PYTHON2(self):
            return self.getToken(SParser.PYTHON2, 0)
        def python_native_statement(self):
            return self.getTypedRuleContext(SParser.Python_native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPython2NativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPython2NativeStatement(self)


    class Python3NativeStatementContext(Native_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Native_statementContext)
            super(SParser.Python3NativeStatementContext, self).__init__(parser)
            self.stmt = None # Python_native_statementContext
            self.copyFrom(ctx)

        def PYTHON3(self):
            return self.getToken(SParser.PYTHON3, 0)
        def python_native_statement(self):
            return self.getTypedRuleContext(SParser.Python_native_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPython3NativeStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPython3NativeStatement(self)



    def native_statement(self):

        localctx = SParser.Native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_native_statement)
        try:
            self.state = 1576
            token = self._input.LA(1)
            if token in [SParser.JAVA]:
                localctx = SParser.JavaNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1566
                self.match(SParser.JAVA)
                self.state = 1567 
                localctx.stmt = self.java_statement()

            elif token in [SParser.CSHARP]:
                localctx = SParser.CSharpNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1568
                self.match(SParser.CSHARP)
                self.state = 1569 
                localctx.stmt = self.csharp_statement()

            elif token in [SParser.PYTHON2]:
                localctx = SParser.Python2NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1570
                self.match(SParser.PYTHON2)
                self.state = 1571 
                localctx.stmt = self.python_native_statement()

            elif token in [SParser.PYTHON3]:
                localctx = SParser.Python3NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1572
                self.match(SParser.PYTHON3)
                self.state = 1573 
                localctx.stmt = self.python_native_statement()

            elif token in [SParser.JAVASCRIPT]:
                localctx = SParser.JavaScriptNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1574
                self.match(SParser.JAVASCRIPT)
                self.state = 1575 
                localctx.stmt = self.javascript_native_statement()

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
            super(SParser.Python_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmt = None # Python_statementContext
            self.module = None # Python_moduleContext

        def python_statement(self):
            return self.getTypedRuleContext(SParser.Python_statementContext,0)


        def SEMI(self):
            return self.getToken(SParser.SEMI, 0)

        def python_module(self):
            return self.getTypedRuleContext(SParser.Python_moduleContext,0)


        def getRuleIndex(self):
            return SParser.RULE_python_native_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPython_native_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPython_native_statement(self)




    def python_native_statement(self):

        localctx = SParser.Python_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 220, self.RULE_python_native_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1578 
            localctx.stmt = self.python_statement()
            self.state = 1580
            la_ = self._interp.adaptivePredict(self._input,107,self._ctx)
            if la_ == 1:
                self.state = 1579
                self.match(SParser.SEMI)


            self.state = 1583
            la_ = self._interp.adaptivePredict(self._input,108,self._ctx)
            if la_ == 1:
                self.state = 1582 
                localctx.module = self.python_module()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_native_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Javascript_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stmt = None # Javascript_statementContext
            self.module = None # Javascript_moduleContext

        def javascript_statement(self):
            return self.getTypedRuleContext(SParser.Javascript_statementContext,0)


        def SEMI(self):
            return self.getToken(SParser.SEMI, 0)

        def javascript_module(self):
            return self.getTypedRuleContext(SParser.Javascript_moduleContext,0)


        def getRuleIndex(self):
            return SParser.RULE_javascript_native_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascript_native_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascript_native_statement(self)




    def javascript_native_statement(self):

        localctx = SParser.Javascript_native_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 222, self.RULE_javascript_native_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1585 
            localctx.stmt = self.javascript_statement()
            self.state = 1587
            la_ = self._interp.adaptivePredict(self._input,109,self._ctx)
            if la_ == 1:
                self.state = 1586
                self.match(SParser.SEMI)


            self.state = 1590
            la_ = self._interp.adaptivePredict(self._input,110,self._ctx)
            if la_ == 1:
                self.state = 1589 
                localctx.module = self.javascript_module()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_statement_list

     
        def copyFrom(self, ctx):
            super(SParser.Statement_listContext, self).copyFrom(ctx)


    class StatementListContext(Statement_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Statement_listContext)
            super(SParser.StatementListContext, self).__init__(parser)
            self.item = None # StatementContext
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(SParser.StatementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitStatementList(self)


    class StatementListItemContext(Statement_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Statement_listContext)
            super(SParser.StatementListItemContext, self).__init__(parser)
            self.items = None # Statement_listContext
            self.item = None # StatementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(SParser.Statement_listContext,0)

        def statement(self):
            return self.getTypedRuleContext(SParser.StatementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitStatementListItem(self)



    def statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 224
        self.enterRecursionRule(localctx, 224, self.RULE_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.StatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1593 
            localctx.item = self.statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1601
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,111,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.StatementListItemContext(self, SParser.Statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_statement_list)
                    self.state = 1595
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1596 
                    self.lfp()
                    self.state = 1597 
                    localctx.item = self.statement() 
                self.state = 1603
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,111,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Assertion_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Assertion_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_assertion_list

     
        def copyFrom(self, ctx):
            super(SParser.Assertion_listContext, self).copyFrom(ctx)


    class AssertionListContext(Assertion_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Assertion_listContext)
            super(SParser.AssertionListContext, self).__init__(parser)
            self.item = None # AssertionContext
            self.copyFrom(ctx)

        def assertion(self):
            return self.getTypedRuleContext(SParser.AssertionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAssertionList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAssertionList(self)


    class AssertionListItemContext(Assertion_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Assertion_listContext)
            super(SParser.AssertionListItemContext, self).__init__(parser)
            self.items = None # Assertion_listContext
            self.item = None # AssertionContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def assertion_list(self):
            return self.getTypedRuleContext(SParser.Assertion_listContext,0)

        def assertion(self):
            return self.getTypedRuleContext(SParser.AssertionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAssertionListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAssertionListItem(self)



    def assertion_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Assertion_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 226
        self.enterRecursionRule(localctx, 226, self.RULE_assertion_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.AssertionListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1605 
            localctx.item = self.assertion()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1613
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,112,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.AssertionListItemContext(self, SParser.Assertion_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assertion_list)
                    self.state = 1607
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1608 
                    self.lfp()
                    self.state = 1609 
                    localctx.item = self.assertion() 
                self.state = 1615
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,112,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Switch_case_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Switch_case_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_switch_case_statement_list

     
        def copyFrom(self, ctx):
            super(SParser.Switch_case_statement_listContext, self).copyFrom(ctx)


    class SwitchCaseStatementListContext(Switch_case_statement_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Switch_case_statement_listContext)
            super(SParser.SwitchCaseStatementListContext, self).__init__(parser)
            self.item = None # Switch_case_statementContext
            self.copyFrom(ctx)

        def switch_case_statement(self):
            return self.getTypedRuleContext(SParser.Switch_case_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSwitchCaseStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSwitchCaseStatementList(self)


    class SwitchCaseStatementListItemContext(Switch_case_statement_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Switch_case_statement_listContext)
            super(SParser.SwitchCaseStatementListItemContext, self).__init__(parser)
            self.items = None # Switch_case_statement_listContext
            self.item = None # Switch_case_statementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def switch_case_statement_list(self):
            return self.getTypedRuleContext(SParser.Switch_case_statement_listContext,0)

        def switch_case_statement(self):
            return self.getTypedRuleContext(SParser.Switch_case_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSwitchCaseStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSwitchCaseStatementListItem(self)



    def switch_case_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Switch_case_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 228
        self.enterRecursionRule(localctx, 228, self.RULE_switch_case_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.SwitchCaseStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1617 
            localctx.item = self.switch_case_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1625
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,113,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.SwitchCaseStatementListItemContext(self, SParser.Switch_case_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_switch_case_statement_list)
                    self.state = 1619
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1620 
                    self.lfp()
                    self.state = 1621 
                    localctx.item = self.switch_case_statement() 
                self.state = 1627
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,113,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Catch_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Catch_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_catch_statement_list

     
        def copyFrom(self, ctx):
            super(SParser.Catch_statement_listContext, self).copyFrom(ctx)


    class CatchStatementListContext(Catch_statement_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Catch_statement_listContext)
            super(SParser.CatchStatementListContext, self).__init__(parser)
            self.item = None # Catch_statementContext
            self.copyFrom(ctx)

        def catch_statement(self):
            return self.getTypedRuleContext(SParser.Catch_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCatchStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCatchStatementList(self)


    class CatchStatementListItemContext(Catch_statement_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Catch_statement_listContext)
            super(SParser.CatchStatementListItemContext, self).__init__(parser)
            self.items = None # Catch_statement_listContext
            self.item = None # Catch_statementContext
            self.copyFrom(ctx)

        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)

        def catch_statement_list(self):
            return self.getTypedRuleContext(SParser.Catch_statement_listContext,0)

        def catch_statement(self):
            return self.getTypedRuleContext(SParser.Catch_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCatchStatementListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCatchStatementListItem(self)



    def catch_statement_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Catch_statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 230
        self.enterRecursionRule(localctx, 230, self.RULE_catch_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.CatchStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1629 
            localctx.item = self.catch_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1637
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,114,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CatchStatementListItemContext(self, SParser.Catch_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_catch_statement_list)
                    self.state = 1631
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1632 
                    self.lfp()
                    self.state = 1633 
                    localctx.item = self.catch_statement() 
                self.state = 1639
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,114,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Literal_collectionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Literal_collectionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_literal_collection

     
        def copyFrom(self, ctx):
            super(SParser.Literal_collectionContext, self).copyFrom(ctx)



    class LiteralListLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a SParser.Literal_collectionContext)
            super(SParser.LiteralListLiteralContext, self).__init__(parser)
            self.exp = None # Literal_list_literalContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(SParser.Literal_list_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterLiteralListLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitLiteralListLiteral(self)


    class LiteralRangeLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a SParser.Literal_collectionContext)
            super(SParser.LiteralRangeLiteralContext, self).__init__(parser)
            self.low = None # Atomic_literalContext
            self.high = None # Atomic_literalContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)
        def RANGE(self):
            return self.getToken(SParser.RANGE, 0)
        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)
        def atomic_literal(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Atomic_literalContext)
            else:
                return self.getTypedRuleContext(SParser.Atomic_literalContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterLiteralRangeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitLiteralRangeLiteral(self)


    class LiteralSetLiteralContext(Literal_collectionContext):

        def __init__(self, parser, ctx): # actually a SParser.Literal_collectionContext)
            super(SParser.LiteralSetLiteralContext, self).__init__(parser)
            self.exp = None # Literal_list_literalContext
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(SParser.LT, 0)
        def GT(self):
            return self.getToken(SParser.GT, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(SParser.Literal_list_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterLiteralSetLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitLiteralSetLiteral(self)



    def literal_collection(self):

        localctx = SParser.Literal_collectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_literal_collection)
        try:
            self.state = 1654
            la_ = self._interp.adaptivePredict(self._input,115,self._ctx)
            if la_ == 1:
                localctx = SParser.LiteralRangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1640
                self.match(SParser.LBRAK)
                self.state = 1641 
                localctx.low = self.atomic_literal()
                self.state = 1642
                self.match(SParser.RANGE)
                self.state = 1643 
                localctx.high = self.atomic_literal()
                self.state = 1644
                self.match(SParser.RBRAK)
                pass

            elif la_ == 2:
                localctx = SParser.LiteralListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1646
                self.match(SParser.LBRAK)
                self.state = 1647 
                localctx.exp = self.literal_list_literal(0)
                self.state = 1648
                self.match(SParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = SParser.LiteralSetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1650
                self.match(SParser.LT)
                self.state = 1651 
                localctx.exp = self.literal_list_literal(0)
                self.state = 1652
                self.match(SParser.GT)
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
            super(SParser.Atomic_literalContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_atomic_literal

     
        def copyFrom(self, ctx):
            super(SParser.Atomic_literalContext, self).copyFrom(ctx)



    class MinIntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.MinIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def MIN_INTEGER(self):
            return self.getToken(SParser.MIN_INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMinIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMinIntegerLiteral(self)


    class DateLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.DateLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATE_LITERAL(self):
            return self.getToken(SParser.DATE_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDateLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDateLiteral(self)


    class BooleanLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.BooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(SParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitBooleanLiteral(self)


    class HexadecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.HexadecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def HEXA_LITERAL(self):
            return self.getToken(SParser.HEXA_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterHexadecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitHexadecimalLiteral(self)


    class MaxIntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.MaxIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def MAX_INTEGER(self):
            return self.getToken(SParser.MAX_INTEGER, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMaxIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMaxIntegerLiteral(self)


    class DateTimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.DateTimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DATETIME_LITERAL(self):
            return self.getToken(SParser.DATETIME_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDateTimeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDateTimeLiteral(self)


    class PeriodLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.PeriodLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def PERIOD_LITERAL(self):
            return self.getToken(SParser.PERIOD_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPeriodLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPeriodLiteral(self)


    class DecimalLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.DecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(SParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDecimalLiteral(self)


    class TextLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.TextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(SParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTextLiteral(self)


    class NullLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.NullLiteralContext, self).__init__(parser)
            self.n = None # Null_literalContext
            self.copyFrom(ctx)

        def null_literal(self):
            return self.getTypedRuleContext(SParser.Null_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNullLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNullLiteral(self)


    class IntegerLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.IntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(SParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIntegerLiteral(self)


    class TimeLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.TimeLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TIME_LITERAL(self):
            return self.getToken(SParser.TIME_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTimeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTimeLiteral(self)


    class CharacterLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.CharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(SParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCharacterLiteral(self)



    def atomic_literal(self):

        localctx = SParser.Atomic_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_atomic_literal)
        try:
            self.state = 1669
            token = self._input.LA(1)
            if token in [SParser.MIN_INTEGER]:
                localctx = SParser.MinIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1656
                localctx.t = self.match(SParser.MIN_INTEGER)

            elif token in [SParser.MAX_INTEGER]:
                localctx = SParser.MaxIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1657
                localctx.t = self.match(SParser.MAX_INTEGER)

            elif token in [SParser.INTEGER_LITERAL]:
                localctx = SParser.IntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1658
                localctx.t = self.match(SParser.INTEGER_LITERAL)

            elif token in [SParser.HEXA_LITERAL]:
                localctx = SParser.HexadecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1659
                localctx.t = self.match(SParser.HEXA_LITERAL)

            elif token in [SParser.CHAR_LITERAL]:
                localctx = SParser.CharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1660
                localctx.t = self.match(SParser.CHAR_LITERAL)

            elif token in [SParser.DATE_LITERAL]:
                localctx = SParser.DateLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1661
                localctx.t = self.match(SParser.DATE_LITERAL)

            elif token in [SParser.TIME_LITERAL]:
                localctx = SParser.TimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1662
                localctx.t = self.match(SParser.TIME_LITERAL)

            elif token in [SParser.TEXT_LITERAL]:
                localctx = SParser.TextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1663
                localctx.t = self.match(SParser.TEXT_LITERAL)

            elif token in [SParser.DECIMAL_LITERAL]:
                localctx = SParser.DecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1664
                localctx.t = self.match(SParser.DECIMAL_LITERAL)

            elif token in [SParser.DATETIME_LITERAL]:
                localctx = SParser.DateTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1665
                localctx.t = self.match(SParser.DATETIME_LITERAL)

            elif token in [SParser.BOOLEAN_LITERAL]:
                localctx = SParser.BooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1666
                localctx.t = self.match(SParser.BOOLEAN_LITERAL)

            elif token in [SParser.PERIOD_LITERAL]:
                localctx = SParser.PeriodLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1667
                localctx.t = self.match(SParser.PERIOD_LITERAL)

            elif token in [SParser.NONE]:
                localctx = SParser.NullLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1668 
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
            super(SParser.Literal_list_literalContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_literal_list_literal

     
        def copyFrom(self, ctx):
            super(SParser.Literal_list_literalContext, self).copyFrom(ctx)


    class LiteralListContext(Literal_list_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Literal_list_literalContext)
            super(SParser.LiteralListContext, self).__init__(parser)
            self.item = None # Atomic_literalContext
            self.copyFrom(ctx)

        def atomic_literal(self):
            return self.getTypedRuleContext(SParser.Atomic_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterLiteralList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitLiteralList(self)


    class LiteralListItemContext(Literal_list_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Literal_list_literalContext)
            super(SParser.LiteralListItemContext, self).__init__(parser)
            self.items = None # Literal_list_literalContext
            self.item = None # Atomic_literalContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(SParser.Literal_list_literalContext,0)

        def atomic_literal(self):
            return self.getTypedRuleContext(SParser.Atomic_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterLiteralListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitLiteralListItem(self)



    def literal_list_literal(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Literal_list_literalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 236
        self.enterRecursionRule(localctx, 236, self.RULE_literal_list_literal, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.LiteralListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1672 
            localctx.item = self.atomic_literal()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1679
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,117,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.LiteralListItemContext(self, SParser.Literal_list_literalContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_literal_list_literal)
                    self.state = 1674
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1675
                    self.match(SParser.COMMA)
                    self.state = 1676 
                    localctx.item = self.atomic_literal() 
                self.state = 1681
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,117,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Selectable_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Selectable_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_selectable_expression

     
        def copyFrom(self, ctx):
            super(SParser.Selectable_expressionContext, self).copyFrom(ctx)



    class ThisExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Selectable_expressionContext)
            super(SParser.ThisExpressionContext, self).__init__(parser)
            self.exp = None # This_expressionContext
            self.copyFrom(ctx)

        def this_expression(self):
            return self.getTypedRuleContext(SParser.This_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterThisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitThisExpression(self)


    class ParenthesisExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Selectable_expressionContext)
            super(SParser.ParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Parenthesis_expressionContext
            self.copyFrom(ctx)

        def parenthesis_expression(self):
            return self.getTypedRuleContext(SParser.Parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterParenthesisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitParenthesisExpression(self)


    class LiteralExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Selectable_expressionContext)
            super(SParser.LiteralExpressionContext, self).__init__(parser)
            self.exp = None # Literal_expressionContext
            self.copyFrom(ctx)

        def literal_expression(self):
            return self.getTypedRuleContext(SParser.Literal_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitLiteralExpression(self)


    class IdentifierExpressionContext(Selectable_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Selectable_expressionContext)
            super(SParser.IdentifierExpressionContext, self).__init__(parser)
            self.exp = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(SParser.IdentifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIdentifierExpression(self)



    def selectable_expression(self):

        localctx = SParser.Selectable_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_selectable_expression)
        try:
            self.state = 1686
            la_ = self._interp.adaptivePredict(self._input,118,self._ctx)
            if la_ == 1:
                localctx = SParser.ParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1682 
                localctx.exp = self.parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = SParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1683 
                localctx.exp = self.literal_expression()
                pass

            elif la_ == 3:
                localctx = SParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1684 
                localctx.exp = self.identifier()
                pass

            elif la_ == 4:
                localctx = SParser.ThisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1685 
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
            super(SParser.This_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SELF(self):
            return self.getToken(SParser.SELF, 0)

        def THIS(self):
            return self.getToken(SParser.THIS, 0)

        def getRuleIndex(self):
            return SParser.RULE_this_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterThis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitThis_expression(self)




    def this_expression(self):

        localctx = SParser.This_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_this_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1688
            _la = self._input.LA(1)
            if not(_la==SParser.SELF or _la==SParser.THIS):
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
            super(SParser.Parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # ExpressionContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterParenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitParenthesis_expression(self)




    def parenthesis_expression(self):

        localctx = SParser.Parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1690
            self.match(SParser.LPAR)
            self.state = 1691 
            localctx.exp = self.expression(0)
            self.state = 1692
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_literal_expression

     
        def copyFrom(self, ctx):
            super(SParser.Literal_expressionContext, self).copyFrom(ctx)



    class CollectionLiteralContext(Literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Literal_expressionContext)
            super(SParser.CollectionLiteralContext, self).__init__(parser)
            self.exp = None # Collection_literalContext
            self.copyFrom(ctx)

        def collection_literal(self):
            return self.getTypedRuleContext(SParser.Collection_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCollectionLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCollectionLiteral(self)


    class AtomicLiteralContext(Literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Literal_expressionContext)
            super(SParser.AtomicLiteralContext, self).__init__(parser)
            self.exp = None # Atomic_literalContext
            self.copyFrom(ctx)

        def atomic_literal(self):
            return self.getTypedRuleContext(SParser.Atomic_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAtomicLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAtomicLiteral(self)



    def literal_expression(self):

        localctx = SParser.Literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_literal_expression)
        try:
            self.state = 1696
            token = self._input.LA(1)
            if token in [SParser.NONE, SParser.BOOLEAN_LITERAL, SParser.CHAR_LITERAL, SParser.MIN_INTEGER, SParser.MAX_INTEGER, SParser.TEXT_LITERAL, SParser.INTEGER_LITERAL, SParser.HEXA_LITERAL, SParser.DECIMAL_LITERAL, SParser.DATETIME_LITERAL, SParser.TIME_LITERAL, SParser.DATE_LITERAL, SParser.PERIOD_LITERAL]:
                localctx = SParser.AtomicLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1694 
                localctx.exp = self.atomic_literal()

            elif token in [SParser.LPAR, SParser.LBRAK, SParser.LCURL, SParser.LT]:
                localctx = SParser.CollectionLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1695 
                localctx.exp = self.collection_literal()

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
            super(SParser.Collection_literalContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_collection_literal

     
        def copyFrom(self, ctx):
            super(SParser.Collection_literalContext, self).copyFrom(ctx)



    class ListLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Collection_literalContext)
            super(SParser.ListLiteralContext, self).__init__(parser)
            self.exp = None # List_literalContext
            self.copyFrom(ctx)

        def list_literal(self):
            return self.getTypedRuleContext(SParser.List_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterListLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitListLiteral(self)


    class RangeLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Collection_literalContext)
            super(SParser.RangeLiteralContext, self).__init__(parser)
            self.exp = None # Range_literalContext
            self.copyFrom(ctx)

        def range_literal(self):
            return self.getTypedRuleContext(SParser.Range_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterRangeLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitRangeLiteral(self)


    class TupleLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Collection_literalContext)
            super(SParser.TupleLiteralContext, self).__init__(parser)
            self.exp = None # Tuple_literalContext
            self.copyFrom(ctx)

        def tuple_literal(self):
            return self.getTypedRuleContext(SParser.Tuple_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTupleLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTupleLiteral(self)


    class SetLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Collection_literalContext)
            super(SParser.SetLiteralContext, self).__init__(parser)
            self.exp = None # Set_literalContext
            self.copyFrom(ctx)

        def set_literal(self):
            return self.getTypedRuleContext(SParser.Set_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSetLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSetLiteral(self)


    class DictLiteralContext(Collection_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Collection_literalContext)
            super(SParser.DictLiteralContext, self).__init__(parser)
            self.exp = None # Dict_literalContext
            self.copyFrom(ctx)

        def dict_literal(self):
            return self.getTypedRuleContext(SParser.Dict_literalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDictLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDictLiteral(self)



    def collection_literal(self):

        localctx = SParser.Collection_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_collection_literal)
        try:
            self.state = 1703
            la_ = self._interp.adaptivePredict(self._input,120,self._ctx)
            if la_ == 1:
                localctx = SParser.RangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1698 
                localctx.exp = self.range_literal()
                pass

            elif la_ == 2:
                localctx = SParser.ListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1699 
                localctx.exp = self.list_literal()
                pass

            elif la_ == 3:
                localctx = SParser.SetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1700 
                localctx.exp = self.set_literal()
                pass

            elif la_ == 4:
                localctx = SParser.DictLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1701 
                localctx.exp = self.dict_literal()
                pass

            elif la_ == 5:
                localctx = SParser.TupleLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1702 
                localctx.exp = self.tuple_literal()
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
            super(SParser.Tuple_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Expression_tupleContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def expression_tuple(self):
            return self.getTypedRuleContext(SParser.Expression_tupleContext,0)


        def getRuleIndex(self):
            return SParser.RULE_tuple_literal

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterTuple_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitTuple_literal(self)




    def tuple_literal(self):

        localctx = SParser.Tuple_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_tuple_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1705
            self.match(SParser.LPAR)
            self.state = 1707
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (SParser.EXECUTE - 95)) | (1 << (SParser.FETCH - 95)) | (1 << (SParser.MUTABLE - 95)) | (1 << (SParser.NONE - 95)) | (1 << (SParser.NOT - 95)) | (1 << (SParser.READ - 95)) | (1 << (SParser.SELF - 95)) | (1 << (SParser.SORTED - 95)) | (1 << (SParser.THIS - 95)) | (1 << (SParser.BOOLEAN_LITERAL - 95)) | (1 << (SParser.CHAR_LITERAL - 95)) | (1 << (SParser.MIN_INTEGER - 95)) | (1 << (SParser.MAX_INTEGER - 95)) | (1 << (SParser.SYMBOL_IDENTIFIER - 95)) | (1 << (SParser.TYPE_IDENTIFIER - 95)) | (1 << (SParser.VARIABLE_IDENTIFIER - 95)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (SParser.TEXT_LITERAL - 160)) | (1 << (SParser.INTEGER_LITERAL - 160)) | (1 << (SParser.HEXA_LITERAL - 160)) | (1 << (SParser.DECIMAL_LITERAL - 160)) | (1 << (SParser.DATETIME_LITERAL - 160)) | (1 << (SParser.TIME_LITERAL - 160)) | (1 << (SParser.DATE_LITERAL - 160)) | (1 << (SParser.PERIOD_LITERAL - 160)))) != 0):
                self.state = 1706 
                localctx.items = self.expression_tuple(0)


            self.state = 1709
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dict_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Dict_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.items = None # Dict_entry_listContext

        def LCURL(self):
            return self.getToken(SParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(SParser.RCURL, 0)

        def dict_entry_list(self):
            return self.getTypedRuleContext(SParser.Dict_entry_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_dict_literal

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDict_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDict_literal(self)




    def dict_literal(self):

        localctx = SParser.Dict_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_dict_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1711
            self.match(SParser.LCURL)
            self.state = 1713
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT))) != 0) or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (SParser.EXECUTE - 95)) | (1 << (SParser.FETCH - 95)) | (1 << (SParser.MUTABLE - 95)) | (1 << (SParser.NONE - 95)) | (1 << (SParser.NOT - 95)) | (1 << (SParser.READ - 95)) | (1 << (SParser.SELF - 95)) | (1 << (SParser.SORTED - 95)) | (1 << (SParser.THIS - 95)) | (1 << (SParser.BOOLEAN_LITERAL - 95)) | (1 << (SParser.CHAR_LITERAL - 95)) | (1 << (SParser.MIN_INTEGER - 95)) | (1 << (SParser.MAX_INTEGER - 95)) | (1 << (SParser.SYMBOL_IDENTIFIER - 95)) | (1 << (SParser.TYPE_IDENTIFIER - 95)) | (1 << (SParser.VARIABLE_IDENTIFIER - 95)))) != 0) or ((((_la - 160)) & ~0x3f) == 0 and ((1 << (_la - 160)) & ((1 << (SParser.TEXT_LITERAL - 160)) | (1 << (SParser.INTEGER_LITERAL - 160)) | (1 << (SParser.HEXA_LITERAL - 160)) | (1 << (SParser.DECIMAL_LITERAL - 160)) | (1 << (SParser.DATETIME_LITERAL - 160)) | (1 << (SParser.TIME_LITERAL - 160)) | (1 << (SParser.DATE_LITERAL - 160)) | (1 << (SParser.PERIOD_LITERAL - 160)))) != 0):
                self.state = 1712 
                localctx.items = self.dict_entry_list(0)


            self.state = 1715
            self.match(SParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_tupleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Expression_tupleContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_expression_tuple

     
        def copyFrom(self, ctx):
            super(SParser.Expression_tupleContext, self).copyFrom(ctx)


    class ValueTupleContext(Expression_tupleContext):

        def __init__(self, parser, ctx): # actually a SParser.Expression_tupleContext)
            super(SParser.ValueTupleContext, self).__init__(parser)
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterValueTuple(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitValueTuple(self)


    class ValueTupleItemContext(Expression_tupleContext):

        def __init__(self, parser, ctx): # actually a SParser.Expression_tupleContext)
            super(SParser.ValueTupleItemContext, self).__init__(parser)
            self.items = None # Expression_tupleContext
            self.item = None # ExpressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def expression_tuple(self):
            return self.getTypedRuleContext(SParser.Expression_tupleContext,0)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterValueTupleItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitValueTupleItem(self)



    def expression_tuple(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Expression_tupleContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 252
        self.enterRecursionRule(localctx, 252, self.RULE_expression_tuple, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.ValueTupleContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1718 
            localctx.item = self.expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1725
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,123,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.ValueTupleItemContext(self, SParser.Expression_tupleContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_tuple)
                    self.state = 1720
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1721
                    self.match(SParser.COMMA)
                    self.state = 1722 
                    localctx.item = self.expression(0) 
                self.state = 1727
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,123,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Dict_entry_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Dict_entry_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_dict_entry_list

     
        def copyFrom(self, ctx):
            super(SParser.Dict_entry_listContext, self).copyFrom(ctx)


    class DictEntryListContext(Dict_entry_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Dict_entry_listContext)
            super(SParser.DictEntryListContext, self).__init__(parser)
            self.item = None # Dict_entryContext
            self.copyFrom(ctx)

        def dict_entry(self):
            return self.getTypedRuleContext(SParser.Dict_entryContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDictEntryList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDictEntryList(self)


    class DictEntryListItemContext(Dict_entry_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Dict_entry_listContext)
            super(SParser.DictEntryListItemContext, self).__init__(parser)
            self.items = None # Dict_entry_listContext
            self.item = None # Dict_entryContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def dict_entry_list(self):
            return self.getTypedRuleContext(SParser.Dict_entry_listContext,0)

        def dict_entry(self):
            return self.getTypedRuleContext(SParser.Dict_entryContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDictEntryListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDictEntryListItem(self)



    def dict_entry_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Dict_entry_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 254
        self.enterRecursionRule(localctx, 254, self.RULE_dict_entry_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.DictEntryListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1729 
            localctx.item = self.dict_entry()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1736
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,124,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.DictEntryListItemContext(self, SParser.Dict_entry_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_dict_entry_list)
                    self.state = 1731
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1732
                    self.match(SParser.COMMA)
                    self.state = 1733 
                    localctx.item = self.dict_entry() 
                self.state = 1738
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,124,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Dict_entryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Dict_entryContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.key = None # ExpressionContext
            self.value = None # ExpressionContext

        def COLON(self):
            return self.getToken(SParser.COLON, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SParser.RULE_dict_entry

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDict_entry(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDict_entry(self)




    def dict_entry(self):

        localctx = SParser.Dict_entryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_dict_entry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1739 
            localctx.key = self.expression(0)
            self.state = 1740
            self.match(SParser.COLON)
            self.state = 1741 
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
            super(SParser.Slice_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_slice_arguments

     
        def copyFrom(self, ctx):
            super(SParser.Slice_argumentsContext, self).copyFrom(ctx)



    class SliceFirstAndLastContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a SParser.Slice_argumentsContext)
            super(SParser.SliceFirstAndLastContext, self).__init__(parser)
            self.first = None # ExpressionContext
            self.last = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)
        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSliceFirstAndLast(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSliceFirstAndLast(self)


    class SliceLastOnlyContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a SParser.Slice_argumentsContext)
            super(SParser.SliceLastOnlyContext, self).__init__(parser)
            self.last = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSliceLastOnly(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSliceLastOnly(self)


    class SliceFirstOnlyContext(Slice_argumentsContext):

        def __init__(self, parser, ctx): # actually a SParser.Slice_argumentsContext)
            super(SParser.SliceFirstOnlyContext, self).__init__(parser)
            self.first = None # ExpressionContext
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(SParser.COLON, 0)
        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSliceFirstOnly(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSliceFirstOnly(self)



    def slice_arguments(self):

        localctx = SParser.Slice_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_slice_arguments)
        try:
            self.state = 1752
            la_ = self._interp.adaptivePredict(self._input,125,self._ctx)
            if la_ == 1:
                localctx = SParser.SliceFirstAndLastContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1743 
                localctx.first = self.expression(0)
                self.state = 1744
                self.match(SParser.COLON)
                self.state = 1745 
                localctx.last = self.expression(0)
                pass

            elif la_ == 2:
                localctx = SParser.SliceFirstOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1747 
                localctx.first = self.expression(0)
                self.state = 1748
                self.match(SParser.COLON)
                pass

            elif la_ == 3:
                localctx = SParser.SliceLastOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1750
                self.match(SParser.COLON)
                self.state = 1751 
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
            super(SParser.Assign_variable_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.exp = None # ExpressionContext

        def assign(self):
            return self.getTypedRuleContext(SParser.AssignContext,0)


        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_assign_variable_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAssign_variable_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAssign_variable_statement(self)




    def assign_variable_statement(self):

        localctx = SParser.Assign_variable_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_assign_variable_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1754 
            localctx.name = self.variable_identifier()
            self.state = 1755 
            self.assign()
            self.state = 1756 
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assignable_instanceContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Assignable_instanceContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_assignable_instance

     
        def copyFrom(self, ctx):
            super(SParser.Assignable_instanceContext, self).copyFrom(ctx)


    class ChildInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a SParser.Assignable_instanceContext)
            super(SParser.ChildInstanceContext, self).__init__(parser)
            self.parent = None # Assignable_instanceContext
            self.child = None # Child_instanceContext
            self.copyFrom(ctx)

        def assignable_instance(self):
            return self.getTypedRuleContext(SParser.Assignable_instanceContext,0)

        def child_instance(self):
            return self.getTypedRuleContext(SParser.Child_instanceContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterChildInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitChildInstance(self)


    class RootInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a SParser.Assignable_instanceContext)
            super(SParser.RootInstanceContext, self).__init__(parser)
            self.name = None # Variable_identifierContext
            self.copyFrom(ctx)

        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterRootInstance(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitRootInstance(self)



    def assignable_instance(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Assignable_instanceContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 262
        self.enterRecursionRule(localctx, 262, self.RULE_assignable_instance, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.RootInstanceContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1759 
            localctx.name = self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1765
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,126,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.ChildInstanceContext(self, SParser.Assignable_instanceContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignable_instance)
                    self.state = 1761
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1762 
                    localctx.child = self.child_instance() 
                self.state = 1767
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,126,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Is_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Is_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_is_expression

     
        def copyFrom(self, ctx):
            super(SParser.Is_expressionContext, self).copyFrom(ctx)



    class IsATypeExpressionContext(Is_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Is_expressionContext)
            super(SParser.IsATypeExpressionContext, self).__init__(parser)
            self.typ = None # Category_or_any_typeContext
            self.copyFrom(ctx)

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)
        def category_or_any_type(self):
            return self.getTypedRuleContext(SParser.Category_or_any_typeContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIsATypeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIsATypeExpression(self)


    class IsOtherExpressionContext(Is_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Is_expressionContext)
            super(SParser.IsOtherExpressionContext, self).__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIsOtherExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIsOtherExpression(self)



    def is_expression(self):

        localctx = SParser.Is_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_is_expression)
        try:
            self.state = 1772
            la_ = self._interp.adaptivePredict(self._input,127,self._ctx)
            if la_ == 1:
                localctx = SParser.IsATypeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1768
                if not self.willBeAOrAn():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willBeAOrAn()")
                self.state = 1769
                self.match(SParser.VARIABLE_IDENTIFIER)
                self.state = 1770 
                localctx.typ = self.category_or_any_type()
                pass

            elif la_ == 2:
                localctx = SParser.IsOtherExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1771 
                localctx.exp = self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Order_by_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Order_by_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def order_by(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Order_byContext)
            else:
                return self.getTypedRuleContext(SParser.Order_byContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SParser.COMMA)
            else:
                return self.getToken(SParser.COMMA, i)

        def getRuleIndex(self):
            return SParser.RULE_order_by_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterOrder_by_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitOrder_by_list(self)




    def order_by_list(self):

        localctx = SParser.Order_by_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_order_by_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1774 
            self.order_by()
            self.state = 1779
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,128,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1775
                    self.match(SParser.COMMA)
                    self.state = 1776 
                    self.order_by() 
                self.state = 1781
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,128,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Order_byContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Order_byContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(SParser.Variable_identifierContext,i)


        def DOT(self, i=None):
            if i is None:
                return self.getTokens(SParser.DOT)
            else:
                return self.getToken(SParser.DOT, i)

        def ASC(self):
            return self.getToken(SParser.ASC, 0)

        def DESC(self):
            return self.getToken(SParser.DESC, 0)

        def getRuleIndex(self):
            return SParser.RULE_order_by

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterOrder_by(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitOrder_by(self)




    def order_by(self):

        localctx = SParser.Order_byContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_order_by)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1782 
            self.variable_identifier()
            self.state = 1787
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,129,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1783
                    self.match(SParser.DOT)
                    self.state = 1784 
                    self.variable_identifier() 
                self.state = 1789
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,129,self._ctx)

            self.state = 1791
            la_ = self._interp.adaptivePredict(self._input,130,self._ctx)
            if la_ == 1:
                self.state = 1790
                _la = self._input.LA(1)
                if not(_la==SParser.ASC or _la==SParser.DESC):
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
            super(SParser.OperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_operator

     
        def copyFrom(self, ctx):
            super(SParser.OperatorContext, self).copyFrom(ctx)



    class OperatorPlusContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a SParser.OperatorContext)
            super(SParser.OperatorPlusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def PLUS(self):
            return self.getToken(SParser.PLUS, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterOperatorPlus(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitOperatorPlus(self)


    class OperatorDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a SParser.OperatorContext)
            super(SParser.OperatorDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def divide(self):
            return self.getTypedRuleContext(SParser.DivideContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterOperatorDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitOperatorDivide(self)


    class OperatorIDivideContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a SParser.OperatorContext)
            super(SParser.OperatorIDivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def idivide(self):
            return self.getTypedRuleContext(SParser.IdivideContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterOperatorIDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitOperatorIDivide(self)


    class OperatorMultiplyContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a SParser.OperatorContext)
            super(SParser.OperatorMultiplyContext, self).__init__(parser)
            self.copyFrom(ctx)

        def multiply(self):
            return self.getTypedRuleContext(SParser.MultiplyContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterOperatorMultiply(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitOperatorMultiply(self)


    class OperatorMinusContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a SParser.OperatorContext)
            super(SParser.OperatorMinusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(SParser.MINUS, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterOperatorMinus(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitOperatorMinus(self)


    class OperatorModuloContext(OperatorContext):

        def __init__(self, parser, ctx): # actually a SParser.OperatorContext)
            super(SParser.OperatorModuloContext, self).__init__(parser)
            self.copyFrom(ctx)

        def modulo(self):
            return self.getTypedRuleContext(SParser.ModuloContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterOperatorModulo(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitOperatorModulo(self)



    def operator(self):

        localctx = SParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_operator)
        try:
            self.state = 1799
            token = self._input.LA(1)
            if token in [SParser.PLUS]:
                localctx = SParser.OperatorPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1793
                self.match(SParser.PLUS)

            elif token in [SParser.MINUS]:
                localctx = SParser.OperatorMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1794
                self.match(SParser.MINUS)

            elif token in [SParser.STAR]:
                localctx = SParser.OperatorMultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1795 
                self.multiply()

            elif token in [SParser.SLASH]:
                localctx = SParser.OperatorDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1796 
                self.divide()

            elif token in [SParser.BSLASH]:
                localctx = SParser.OperatorIDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1797 
                self.idivide()

            elif token in [SParser.PERCENT, SParser.MODULO]:
                localctx = SParser.OperatorModuloContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1798 
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
            super(SParser.New_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return SParser.RULE_new_token

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNew_token(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNew_token(self)




    def new_token(self):

        localctx = SParser.New_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 272, self.RULE_new_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1801
            localctx.i1 = self.match(SParser.VARIABLE_IDENTIFIER)
            self.state = 1802
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
            super(SParser.Key_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return SParser.RULE_key_token

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterKey_token(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitKey_token(self)




    def key_token(self):

        localctx = SParser.Key_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 274, self.RULE_key_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1804
            localctx.i1 = self.match(SParser.VARIABLE_IDENTIFIER)
            self.state = 1805
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

    class Value_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Value_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return SParser.RULE_value_token

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterValue_token(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitValue_token(self)




    def value_token(self):

        localctx = SParser.Value_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_value_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1807
            localctx.i1 = self.match(SParser.VARIABLE_IDENTIFIER)
            self.state = 1808
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
            super(SParser.Symbols_tokenContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.i1 = None # Token

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return SParser.RULE_symbols_token

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSymbols_token(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSymbols_token(self)




    def symbols_token(self):

        localctx = SParser.Symbols_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 278, self.RULE_symbols_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1810
            localctx.i1 = self.match(SParser.VARIABLE_IDENTIFIER)
            self.state = 1811
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
            super(SParser.AssignContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(SParser.EQ, 0)

        def getRuleIndex(self):
            return SParser.RULE_assign

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAssign(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAssign(self)




    def assign(self):

        localctx = SParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1813
            self.match(SParser.EQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MultiplyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.MultiplyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(SParser.STAR, 0)

        def getRuleIndex(self):
            return SParser.RULE_multiply

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMultiply(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMultiply(self)




    def multiply(self):

        localctx = SParser.MultiplyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 282, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1815
            self.match(SParser.STAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DivideContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.DivideContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self):
            return self.getToken(SParser.SLASH, 0)

        def getRuleIndex(self):
            return SParser.RULE_divide

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDivide(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDivide(self)




    def divide(self):

        localctx = SParser.DivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_divide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1817
            self.match(SParser.SLASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdivideContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.IdivideContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BSLASH(self):
            return self.getToken(SParser.BSLASH, 0)

        def getRuleIndex(self):
            return SParser.RULE_idivide

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIdivide(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIdivide(self)




    def idivide(self):

        localctx = SParser.IdivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 286, self.RULE_idivide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1819
            self.match(SParser.BSLASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModuloContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.ModuloContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PERCENT(self):
            return self.getToken(SParser.PERCENT, 0)

        def MODULO(self):
            return self.getToken(SParser.MODULO, 0)

        def getRuleIndex(self):
            return SParser.RULE_modulo

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterModulo(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitModulo(self)




    def modulo(self):

        localctx = SParser.ModuloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 288, self.RULE_modulo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1821
            _la = self._input.LA(1)
            if not(_la==SParser.PERCENT or _la==SParser.MODULO):
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
            super(SParser.Javascript_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_javascript_statement

     
        def copyFrom(self, ctx):
            super(SParser.Javascript_statementContext, self).copyFrom(ctx)



    class JavascriptStatementContext(Javascript_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_statementContext)
            super(SParser.JavascriptStatementContext, self).__init__(parser)
            self.exp = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(SParser.SEMI, 0)
        def javascript_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascriptStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascriptStatement(self)


    class JavascriptReturnStatementContext(Javascript_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_statementContext)
            super(SParser.JavascriptReturnStatementContext, self).__init__(parser)
            self.exp = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(SParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(SParser.SEMI, 0)
        def javascript_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascriptReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascriptReturnStatement(self)



    def javascript_statement(self):

        localctx = SParser.Javascript_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_javascript_statement)
        try:
            self.state = 1830
            token = self._input.LA(1)
            if token in [SParser.RETURN]:
                localctx = SParser.JavascriptReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1823
                self.match(SParser.RETURN)
                self.state = 1824 
                localctx.exp = self.javascript_expression(0)
                self.state = 1825
                self.match(SParser.SEMI)

            elif token in [SParser.LPAR, SParser.LBRAK, SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.SELF, SParser.TEST, SParser.THIS, SParser.WRITE, SParser.BOOLEAN_LITERAL, SParser.CHAR_LITERAL, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER, SParser.DOLLAR_IDENTIFIER, SParser.TEXT_LITERAL, SParser.INTEGER_LITERAL, SParser.DECIMAL_LITERAL]:
                localctx = SParser.JavascriptStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1827 
                localctx.exp = self.javascript_expression(0)
                self.state = 1828
                self.match(SParser.SEMI)

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
            super(SParser.Javascript_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_javascript_expression

     
        def copyFrom(self, ctx):
            super(SParser.Javascript_expressionContext, self).copyFrom(ctx)


    class JavascriptSelectorExpressionContext(Javascript_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_expressionContext)
            super(SParser.JavascriptSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Javascript_expressionContext
            self.child = None # Javascript_selector_expressionContext
            self.copyFrom(ctx)

        def javascript_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_expressionContext,0)

        def javascript_selector_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascriptSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascriptSelectorExpression(self)


    class JavascriptPrimaryExpressionContext(Javascript_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_expressionContext)
            super(SParser.JavascriptPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_primary_expressionContext
            self.copyFrom(ctx)

        def javascript_primary_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascriptPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascriptPrimaryExpression(self)



    def javascript_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Javascript_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 292
        self.enterRecursionRule(localctx, 292, self.RULE_javascript_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavascriptPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1833 
            localctx.exp = self.javascript_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1839
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,133,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.JavascriptSelectorExpressionContext(self, SParser.Javascript_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_expression)
                    self.state = 1835
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1836 
                    localctx.child = self.javascript_selector_expression() 
                self.state = 1841
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,133,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Javascript_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Javascript_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def javascript_this_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_this_expressionContext,0)


        def javascript_new_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_new_expressionContext,0)


        def javascript_parenthesis_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_parenthesis_expressionContext,0)


        def javascript_identifier_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_identifier_expressionContext,0)


        def javascript_literal_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_literal_expressionContext,0)


        def javascript_method_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_method_expressionContext,0)


        def javascript_item_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_item_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_javascript_primary_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascript_primary_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascript_primary_expression(self)




    def javascript_primary_expression(self):

        localctx = SParser.Javascript_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_javascript_primary_expression)
        try:
            self.state = 1849
            la_ = self._interp.adaptivePredict(self._input,134,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1842 
                self.javascript_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1843 
                self.javascript_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1844 
                self.javascript_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1845 
                self.javascript_identifier_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1846 
                self.javascript_literal_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1847 
                self.javascript_method_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1848 
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
            super(SParser.Javascript_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(SParser.This_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_javascript_this_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascript_this_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascript_this_expression(self)




    def javascript_this_expression(self):

        localctx = SParser.Javascript_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 296, self.RULE_javascript_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1851 
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
            super(SParser.Javascript_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(SParser.New_tokenContext,0)


        def javascript_method_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_method_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_javascript_new_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascript_new_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascript_new_expression(self)




    def javascript_new_expression(self):

        localctx = SParser.Javascript_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_javascript_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1853 
            self.new_token()
            self.state = 1854 
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
            super(SParser.Javascript_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_javascript_selector_expression

     
        def copyFrom(self, ctx):
            super(SParser.Javascript_selector_expressionContext, self).copyFrom(ctx)



    class JavaScriptMemberExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_selector_expressionContext)
            super(SParser.JavaScriptMemberExpressionContext, self).__init__(parser)
            self.name = None # Javascript_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def javascript_identifier(self):
            return self.getTypedRuleContext(SParser.Javascript_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaScriptMemberExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaScriptMemberExpression(self)


    class JavaScriptItemExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_selector_expressionContext)
            super(SParser.JavaScriptItemExpressionContext, self).__init__(parser)
            self.exp = None # Javascript_item_expressionContext
            self.copyFrom(ctx)

        def javascript_item_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_item_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaScriptItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaScriptItemExpression(self)


    class JavaScriptMethodExpressionContext(Javascript_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_selector_expressionContext)
            super(SParser.JavaScriptMethodExpressionContext, self).__init__(parser)
            self.method = None # Javascript_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def javascript_method_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaScriptMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaScriptMethodExpression(self)



    def javascript_selector_expression(self):

        localctx = SParser.Javascript_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 300, self.RULE_javascript_selector_expression)
        try:
            self.state = 1861
            la_ = self._interp.adaptivePredict(self._input,135,self._ctx)
            if la_ == 1:
                localctx = SParser.JavaScriptMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1856
                self.match(SParser.DOT)
                self.state = 1857 
                localctx.method = self.javascript_method_expression()
                pass

            elif la_ == 2:
                localctx = SParser.JavaScriptMemberExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1858
                self.match(SParser.DOT)
                self.state = 1859 
                localctx.name = self.javascript_identifier()
                pass

            elif la_ == 3:
                localctx = SParser.JavaScriptItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1860 
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
            super(SParser.Javascript_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Javascript_identifierContext
            self.args = None # Javascript_argumentsContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def javascript_identifier(self):
            return self.getTypedRuleContext(SParser.Javascript_identifierContext,0)


        def javascript_arguments(self):
            return self.getTypedRuleContext(SParser.Javascript_argumentsContext,0)


        def getRuleIndex(self):
            return SParser.RULE_javascript_method_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascript_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascript_method_expression(self)




    def javascript_method_expression(self):

        localctx = SParser.Javascript_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_javascript_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1863 
            localctx.name = self.javascript_identifier()
            self.state = 1864
            self.match(SParser.LPAR)
            self.state = 1866
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 127)) & ~0x3f) == 0 and ((1 << (_la - 127)) & ((1 << (SParser.READ - 127)) | (1 << (SParser.SELF - 127)) | (1 << (SParser.TEST - 127)) | (1 << (SParser.THIS - 127)) | (1 << (SParser.WRITE - 127)) | (1 << (SParser.BOOLEAN_LITERAL - 127)) | (1 << (SParser.CHAR_LITERAL - 127)) | (1 << (SParser.SYMBOL_IDENTIFIER - 127)) | (1 << (SParser.TYPE_IDENTIFIER - 127)) | (1 << (SParser.VARIABLE_IDENTIFIER - 127)) | (1 << (SParser.DOLLAR_IDENTIFIER - 127)) | (1 << (SParser.TEXT_LITERAL - 127)) | (1 << (SParser.INTEGER_LITERAL - 127)) | (1 << (SParser.DECIMAL_LITERAL - 127)))) != 0):
                self.state = 1865 
                localctx.args = self.javascript_arguments(0)


            self.state = 1868
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Javascript_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_javascript_arguments

     
        def copyFrom(self, ctx):
            super(SParser.Javascript_argumentsContext, self).copyFrom(ctx)


    class JavascriptArgumentListContext(Javascript_argumentsContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_argumentsContext)
            super(SParser.JavascriptArgumentListContext, self).__init__(parser)
            self.item = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def javascript_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascriptArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascriptArgumentList(self)


    class JavascriptArgumentListItemContext(Javascript_argumentsContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_argumentsContext)
            super(SParser.JavascriptArgumentListItemContext, self).__init__(parser)
            self.items = None # Javascript_argumentsContext
            self.item = None # Javascript_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def javascript_arguments(self):
            return self.getTypedRuleContext(SParser.Javascript_argumentsContext,0)

        def javascript_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascriptArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascriptArgumentListItem(self)



    def javascript_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Javascript_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 304
        self.enterRecursionRule(localctx, 304, self.RULE_javascript_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavascriptArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1871 
            localctx.item = self.javascript_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1878
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,137,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.JavascriptArgumentListItemContext(self, SParser.Javascript_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_arguments)
                    self.state = 1873
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1874
                    self.match(SParser.COMMA)
                    self.state = 1875 
                    localctx.item = self.javascript_expression(0) 
                self.state = 1880
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,137,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Javascript_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Javascript_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Javascript_expressionContext

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)

        def javascript_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_javascript_item_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascript_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascript_item_expression(self)




    def javascript_item_expression(self):

        localctx = SParser.Javascript_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 306, self.RULE_javascript_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1881
            self.match(SParser.LBRAK)
            self.state = 1882 
            localctx.exp = self.javascript_expression(0)
            self.state = 1883
            self.match(SParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Javascript_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Javascript_expressionContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def javascript_expression(self):
            return self.getTypedRuleContext(SParser.Javascript_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_javascript_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascript_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascript_parenthesis_expression(self)




    def javascript_parenthesis_expression(self):

        localctx = SParser.Javascript_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 308, self.RULE_javascript_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1885
            self.match(SParser.LPAR)
            self.state = 1886 
            localctx.exp = self.javascript_expression(0)
            self.state = 1887
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Javascript_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Javascript_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Javascript_identifierContext

        def javascript_identifier(self):
            return self.getTypedRuleContext(SParser.Javascript_identifierContext,0)


        def getRuleIndex(self):
            return SParser.RULE_javascript_identifier_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascript_identifier_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascript_identifier_expression(self)




    def javascript_identifier_expression(self):

        localctx = SParser.Javascript_identifier_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 310, self.RULE_javascript_identifier_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1889 
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
            super(SParser.Javascript_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_javascript_literal_expression

     
        def copyFrom(self, ctx):
            super(SParser.Javascript_literal_expressionContext, self).copyFrom(ctx)



    class JavascriptIntegerLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_literal_expressionContext)
            super(SParser.JavascriptIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(SParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascriptIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascriptIntegerLiteral(self)


    class JavascriptBooleanLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_literal_expressionContext)
            super(SParser.JavascriptBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(SParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascriptBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascriptBooleanLiteral(self)


    class JavascriptCharacterLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_literal_expressionContext)
            super(SParser.JavascriptCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(SParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascriptCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascriptCharacterLiteral(self)


    class JavascriptTextLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_literal_expressionContext)
            super(SParser.JavascriptTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(SParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascriptTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascriptTextLiteral(self)


    class JavascriptDecimalLiteralContext(Javascript_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Javascript_literal_expressionContext)
            super(SParser.JavascriptDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(SParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascriptDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascriptDecimalLiteral(self)



    def javascript_literal_expression(self):

        localctx = SParser.Javascript_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 312, self.RULE_javascript_literal_expression)
        try:
            self.state = 1896
            token = self._input.LA(1)
            if token in [SParser.INTEGER_LITERAL]:
                localctx = SParser.JavascriptIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1891
                localctx.t = self.match(SParser.INTEGER_LITERAL)

            elif token in [SParser.DECIMAL_LITERAL]:
                localctx = SParser.JavascriptDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1892
                localctx.t = self.match(SParser.DECIMAL_LITERAL)

            elif token in [SParser.TEXT_LITERAL]:
                localctx = SParser.JavascriptTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1893
                localctx.t = self.match(SParser.TEXT_LITERAL)

            elif token in [SParser.BOOLEAN_LITERAL]:
                localctx = SParser.JavascriptBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1894
                localctx.t = self.match(SParser.BOOLEAN_LITERAL)

            elif token in [SParser.CHAR_LITERAL]:
                localctx = SParser.JavascriptCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1895
                localctx.t = self.match(SParser.CHAR_LITERAL)

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
            super(SParser.Javascript_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(SParser.SYMBOL_IDENTIFIER, 0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(SParser.DOLLAR_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(SParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(SParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(SParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(SParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(SParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(SParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(SParser.DATE, 0)

        def TIME(self):
            return self.getToken(SParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(SParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(SParser.PERIOD, 0)

        def READ(self):
            return self.getToken(SParser.READ, 0)

        def WRITE(self):
            return self.getToken(SParser.WRITE, 0)

        def TEST(self):
            return self.getToken(SParser.TEST, 0)

        def getRuleIndex(self):
            return SParser.RULE_javascript_identifier

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavascript_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavascript_identifier(self)




    def javascript_identifier(self):

        localctx = SParser.Javascript_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 314, self.RULE_javascript_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1898
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 127)) & ~0x3f) == 0 and ((1 << (_la - 127)) & ((1 << (SParser.READ - 127)) | (1 << (SParser.TEST - 127)) | (1 << (SParser.WRITE - 127)) | (1 << (SParser.SYMBOL_IDENTIFIER - 127)) | (1 << (SParser.TYPE_IDENTIFIER - 127)) | (1 << (SParser.VARIABLE_IDENTIFIER - 127)) | (1 << (SParser.DOLLAR_IDENTIFIER - 127)))) != 0)):
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
            super(SParser.Python_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_python_statement

     
        def copyFrom(self, ctx):
            super(SParser.Python_statementContext, self).copyFrom(ctx)



    class PythonStatementContext(Python_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_statementContext)
            super(SParser.PythonStatementContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(SParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonStatement(self)


    class PythonReturnStatementContext(Python_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_statementContext)
            super(SParser.PythonReturnStatementContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(SParser.RETURN, 0)
        def python_expression(self):
            return self.getTypedRuleContext(SParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonReturnStatement(self)



    def python_statement(self):

        localctx = SParser.Python_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 316, self.RULE_python_statement)
        try:
            self.state = 1903
            token = self._input.LA(1)
            if token in [SParser.RETURN]:
                localctx = SParser.PythonReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1900
                self.match(SParser.RETURN)
                self.state = 1901 
                localctx.exp = self.python_expression(0)

            elif token in [SParser.LPAR, SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.SELF, SParser.TEST, SParser.THIS, SParser.WRITE, SParser.BOOLEAN_LITERAL, SParser.CHAR_LITERAL, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER, SParser.DOLLAR_IDENTIFIER, SParser.TEXT_LITERAL, SParser.INTEGER_LITERAL, SParser.DECIMAL_LITERAL]:
                localctx = SParser.PythonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1902 
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
            super(SParser.Python_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_python_expression

     
        def copyFrom(self, ctx):
            super(SParser.Python_expressionContext, self).copyFrom(ctx)


    class PythonSelectorExpressionContext(Python_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_expressionContext)
            super(SParser.PythonSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Python_expressionContext
            self.child = None # Python_selector_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(SParser.Python_expressionContext,0)

        def python_selector_expression(self):
            return self.getTypedRuleContext(SParser.Python_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonSelectorExpression(self)


    class PythonPrimaryExpressionContext(Python_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_expressionContext)
            super(SParser.PythonPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Python_primary_expressionContext
            self.copyFrom(ctx)

        def python_primary_expression(self):
            return self.getTypedRuleContext(SParser.Python_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonPrimaryExpression(self)



    def python_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Python_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 318
        self.enterRecursionRule(localctx, 318, self.RULE_python_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.PythonPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1906 
            localctx.exp = self.python_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1912
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,140,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.PythonSelectorExpressionContext(self, SParser.Python_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_expression)
                    self.state = 1908
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1909 
                    localctx.child = self.python_selector_expression() 
                self.state = 1914
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,140,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Python_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_python_primary_expression

     
        def copyFrom(self, ctx):
            super(SParser.Python_primary_expressionContext, self).copyFrom(ctx)



    class PythonParenthesisExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_primary_expressionContext)
            super(SParser.PythonParenthesisExpressionContext, self).__init__(parser)
            self.exp = None # Python_parenthesis_expressionContext
            self.copyFrom(ctx)

        def python_parenthesis_expression(self):
            return self.getTypedRuleContext(SParser.Python_parenthesis_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonParenthesisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonParenthesisExpression(self)


    class PythonIdentifierExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_primary_expressionContext)
            super(SParser.PythonIdentifierExpressionContext, self).__init__(parser)
            self.exp = None # Python_identifier_expressionContext
            self.copyFrom(ctx)

        def python_identifier_expression(self):
            return self.getTypedRuleContext(SParser.Python_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonIdentifierExpression(self)


    class PythonLiteralExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_primary_expressionContext)
            super(SParser.PythonLiteralExpressionContext, self).__init__(parser)
            self.exp = None # Python_literal_expressionContext
            self.copyFrom(ctx)

        def python_literal_expression(self):
            return self.getTypedRuleContext(SParser.Python_literal_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonLiteralExpression(self)


    class PythonGlobalMethodExpressionContext(Python_primary_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_primary_expressionContext)
            super(SParser.PythonGlobalMethodExpressionContext, self).__init__(parser)
            self.exp = None # Python_method_expressionContext
            self.copyFrom(ctx)

        def python_method_expression(self):
            return self.getTypedRuleContext(SParser.Python_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonGlobalMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonGlobalMethodExpression(self)



    def python_primary_expression(self):

        localctx = SParser.Python_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 320, self.RULE_python_primary_expression)
        try:
            self.state = 1919
            la_ = self._interp.adaptivePredict(self._input,141,self._ctx)
            if la_ == 1:
                localctx = SParser.PythonParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1915 
                localctx.exp = self.python_parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = SParser.PythonIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1916 
                localctx.exp = self.python_identifier_expression(0)
                pass

            elif la_ == 3:
                localctx = SParser.PythonLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1917 
                localctx.exp = self.python_literal_expression()
                pass

            elif la_ == 4:
                localctx = SParser.PythonGlobalMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1918 
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
            super(SParser.Python_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_python_selector_expression

     
        def copyFrom(self, ctx):
            super(SParser.Python_selector_expressionContext, self).copyFrom(ctx)



    class PythonMethodExpressionContext(Python_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_selector_expressionContext)
            super(SParser.PythonMethodExpressionContext, self).__init__(parser)
            self.exp = None # Python_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def python_method_expression(self):
            return self.getTypedRuleContext(SParser.Python_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonMethodExpression(self)


    class PythonItemExpressionContext(Python_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_selector_expressionContext)
            super(SParser.PythonItemExpressionContext, self).__init__(parser)
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)
        def python_expression(self):
            return self.getTypedRuleContext(SParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonItemExpression(self)



    def python_selector_expression(self):

        localctx = SParser.Python_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 322, self.RULE_python_selector_expression)
        try:
            self.state = 1927
            token = self._input.LA(1)
            if token in [SParser.DOT]:
                localctx = SParser.PythonMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1921
                self.match(SParser.DOT)
                self.state = 1922 
                localctx.exp = self.python_method_expression()

            elif token in [SParser.LBRAK]:
                localctx = SParser.PythonItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1923
                self.match(SParser.LBRAK)
                self.state = 1924 
                localctx.exp = self.python_expression(0)
                self.state = 1925
                self.match(SParser.RBRAK)

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
            super(SParser.Python_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Python_identifierContext
            self.args = None # Python_argument_listContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def python_identifier(self):
            return self.getTypedRuleContext(SParser.Python_identifierContext,0)


        def python_argument_list(self):
            return self.getTypedRuleContext(SParser.Python_argument_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_python_method_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPython_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPython_method_expression(self)




    def python_method_expression(self):

        localctx = SParser.Python_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 324, self.RULE_python_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1929 
            localctx.name = self.python_identifier()
            self.state = 1930
            self.match(SParser.LPAR)
            self.state = 1932
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 127)) & ~0x3f) == 0 and ((1 << (_la - 127)) & ((1 << (SParser.READ - 127)) | (1 << (SParser.SELF - 127)) | (1 << (SParser.TEST - 127)) | (1 << (SParser.THIS - 127)) | (1 << (SParser.WRITE - 127)) | (1 << (SParser.BOOLEAN_LITERAL - 127)) | (1 << (SParser.CHAR_LITERAL - 127)) | (1 << (SParser.SYMBOL_IDENTIFIER - 127)) | (1 << (SParser.TYPE_IDENTIFIER - 127)) | (1 << (SParser.VARIABLE_IDENTIFIER - 127)) | (1 << (SParser.DOLLAR_IDENTIFIER - 127)) | (1 << (SParser.TEXT_LITERAL - 127)) | (1 << (SParser.INTEGER_LITERAL - 127)) | (1 << (SParser.DECIMAL_LITERAL - 127)))) != 0):
                self.state = 1931 
                localctx.args = self.python_argument_list()


            self.state = 1934
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Python_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_python_argument_list

     
        def copyFrom(self, ctx):
            super(SParser.Python_argument_listContext, self).copyFrom(ctx)



    class PythonOrdinalOnlyArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_argument_listContext)
            super(SParser.PythonOrdinalOnlyArgumentListContext, self).__init__(parser)
            self.ordinal = None # Python_ordinal_argument_listContext
            self.copyFrom(ctx)

        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(SParser.Python_ordinal_argument_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonOrdinalOnlyArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonOrdinalOnlyArgumentList(self)


    class PythonNamedOnlyArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_argument_listContext)
            super(SParser.PythonNamedOnlyArgumentListContext, self).__init__(parser)
            self.named = None # Python_named_argument_listContext
            self.copyFrom(ctx)

        def python_named_argument_list(self):
            return self.getTypedRuleContext(SParser.Python_named_argument_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonNamedOnlyArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonNamedOnlyArgumentList(self)


    class PythonArgumentListContext(Python_argument_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_argument_listContext)
            super(SParser.PythonArgumentListContext, self).__init__(parser)
            self.ordinal = None # Python_ordinal_argument_listContext
            self.named = None # Python_named_argument_listContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(SParser.Python_ordinal_argument_listContext,0)

        def python_named_argument_list(self):
            return self.getTypedRuleContext(SParser.Python_named_argument_listContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonArgumentList(self)



    def python_argument_list(self):

        localctx = SParser.Python_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 326, self.RULE_python_argument_list)
        try:
            self.state = 1942
            la_ = self._interp.adaptivePredict(self._input,144,self._ctx)
            if la_ == 1:
                localctx = SParser.PythonOrdinalOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1936 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                pass

            elif la_ == 2:
                localctx = SParser.PythonNamedOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1937 
                localctx.named = self.python_named_argument_list(0)
                pass

            elif la_ == 3:
                localctx = SParser.PythonArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1938 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                self.state = 1939
                self.match(SParser.COMMA)
                self.state = 1940 
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
            super(SParser.Python_ordinal_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_python_ordinal_argument_list

     
        def copyFrom(self, ctx):
            super(SParser.Python_ordinal_argument_listContext, self).copyFrom(ctx)


    class PythonOrdinalArgumentListContext(Python_ordinal_argument_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_ordinal_argument_listContext)
            super(SParser.PythonOrdinalArgumentListContext, self).__init__(parser)
            self.item = None # Python_expressionContext
            self.copyFrom(ctx)

        def python_expression(self):
            return self.getTypedRuleContext(SParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonOrdinalArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonOrdinalArgumentList(self)


    class PythonOrdinalArgumentListItemContext(Python_ordinal_argument_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_ordinal_argument_listContext)
            super(SParser.PythonOrdinalArgumentListItemContext, self).__init__(parser)
            self.items = None # Python_ordinal_argument_listContext
            self.item = None # Python_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def python_ordinal_argument_list(self):
            return self.getTypedRuleContext(SParser.Python_ordinal_argument_listContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(SParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonOrdinalArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonOrdinalArgumentListItem(self)



    def python_ordinal_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Python_ordinal_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 328
        self.enterRecursionRule(localctx, 328, self.RULE_python_ordinal_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.PythonOrdinalArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1945 
            localctx.item = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1952
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,145,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.PythonOrdinalArgumentListItemContext(self, SParser.Python_ordinal_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_ordinal_argument_list)
                    self.state = 1947
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1948
                    self.match(SParser.COMMA)
                    self.state = 1949 
                    localctx.item = self.python_expression(0) 
                self.state = 1954
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,145,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_named_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Python_named_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_python_named_argument_list

     
        def copyFrom(self, ctx):
            super(SParser.Python_named_argument_listContext, self).copyFrom(ctx)


    class PythonNamedArgumentListContext(Python_named_argument_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_named_argument_listContext)
            super(SParser.PythonNamedArgumentListContext, self).__init__(parser)
            self.name = None # Python_identifierContext
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def EQ(self):
            return self.getToken(SParser.EQ, 0)
        def python_identifier(self):
            return self.getTypedRuleContext(SParser.Python_identifierContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(SParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonNamedArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonNamedArgumentList(self)


    class PythonNamedArgumentListItemContext(Python_named_argument_listContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_named_argument_listContext)
            super(SParser.PythonNamedArgumentListItemContext, self).__init__(parser)
            self.items = None # Python_named_argument_listContext
            self.name = None # Python_identifierContext
            self.exp = None # Python_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def EQ(self):
            return self.getToken(SParser.EQ, 0)
        def python_named_argument_list(self):
            return self.getTypedRuleContext(SParser.Python_named_argument_listContext,0)

        def python_identifier(self):
            return self.getTypedRuleContext(SParser.Python_identifierContext,0)

        def python_expression(self):
            return self.getTypedRuleContext(SParser.Python_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonNamedArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonNamedArgumentListItem(self)



    def python_named_argument_list(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Python_named_argument_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 330
        self.enterRecursionRule(localctx, 330, self.RULE_python_named_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.PythonNamedArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1956 
            localctx.name = self.python_identifier()
            self.state = 1957
            self.match(SParser.EQ)
            self.state = 1958 
            localctx.exp = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1968
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,146,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.PythonNamedArgumentListItemContext(self, SParser.Python_named_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_named_argument_list)
                    self.state = 1960
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1961
                    self.match(SParser.COMMA)
                    self.state = 1962 
                    localctx.name = self.python_identifier()
                    self.state = 1963
                    self.match(SParser.EQ)
                    self.state = 1964 
                    localctx.exp = self.python_expression(0) 
                self.state = 1970
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,146,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Python_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Python_expressionContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def python_expression(self):
            return self.getTypedRuleContext(SParser.Python_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_python_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPython_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPython_parenthesis_expression(self)




    def python_parenthesis_expression(self):

        localctx = SParser.Python_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 332, self.RULE_python_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1971
            self.match(SParser.LPAR)
            self.state = 1972 
            localctx.exp = self.python_expression(0)
            self.state = 1973
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Python_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Python_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_python_identifier_expression

     
        def copyFrom(self, ctx):
            super(SParser.Python_identifier_expressionContext, self).copyFrom(ctx)


    class PythonChildIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_identifier_expressionContext)
            super(SParser.PythonChildIdentifierContext, self).__init__(parser)
            self.parent = None # Python_identifier_expressionContext
            self.name = None # Python_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def python_identifier_expression(self):
            return self.getTypedRuleContext(SParser.Python_identifier_expressionContext,0)

        def python_identifier(self):
            return self.getTypedRuleContext(SParser.Python_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonChildIdentifier(self)


    class PythonPromptoIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_identifier_expressionContext)
            super(SParser.PythonPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(SParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonPromptoIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonPromptoIdentifier(self)


    class PythonIdentifierContext(Python_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_identifier_expressionContext)
            super(SParser.PythonIdentifierContext, self).__init__(parser)
            self.name = None # Python_identifierContext
            self.copyFrom(ctx)

        def python_identifier(self):
            return self.getTypedRuleContext(SParser.Python_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonIdentifier(self)



    def python_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Python_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 334
        self.enterRecursionRule(localctx, 334, self.RULE_python_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1978
            token = self._input.LA(1)
            if token in [SParser.DOLLAR_IDENTIFIER]:
                localctx = SParser.PythonPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1976
                self.match(SParser.DOLLAR_IDENTIFIER)

            elif token in [SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.SELF, SParser.TEST, SParser.THIS, SParser.WRITE, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER]:
                localctx = SParser.PythonIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1977 
                localctx.name = self.python_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 1985
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,148,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.PythonChildIdentifierContext(self, SParser.Python_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_identifier_expression)
                    self.state = 1980
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1981
                    self.match(SParser.DOT)
                    self.state = 1982 
                    localctx.name = self.python_identifier() 
                self.state = 1987
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,148,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Python_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Python_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_python_literal_expression

     
        def copyFrom(self, ctx):
            super(SParser.Python_literal_expressionContext, self).copyFrom(ctx)



    class PythonIntegerLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_literal_expressionContext)
            super(SParser.PythonIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(SParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonIntegerLiteral(self)


    class PythonBooleanLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_literal_expressionContext)
            super(SParser.PythonBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(SParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonBooleanLiteral(self)


    class PythonCharacterLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_literal_expressionContext)
            super(SParser.PythonCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(SParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonCharacterLiteral(self)


    class PythonTextLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_literal_expressionContext)
            super(SParser.PythonTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(SParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonTextLiteral(self)


    class PythonDecimalLiteralContext(Python_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Python_literal_expressionContext)
            super(SParser.PythonDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(SParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPythonDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPythonDecimalLiteral(self)



    def python_literal_expression(self):

        localctx = SParser.Python_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 336, self.RULE_python_literal_expression)
        try:
            self.state = 1993
            token = self._input.LA(1)
            if token in [SParser.INTEGER_LITERAL]:
                localctx = SParser.PythonIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1988
                localctx.t = self.match(SParser.INTEGER_LITERAL)

            elif token in [SParser.DECIMAL_LITERAL]:
                localctx = SParser.PythonDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1989
                localctx.t = self.match(SParser.DECIMAL_LITERAL)

            elif token in [SParser.TEXT_LITERAL]:
                localctx = SParser.PythonTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1990
                localctx.t = self.match(SParser.TEXT_LITERAL)

            elif token in [SParser.BOOLEAN_LITERAL]:
                localctx = SParser.PythonBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1991
                localctx.t = self.match(SParser.BOOLEAN_LITERAL)

            elif token in [SParser.CHAR_LITERAL]:
                localctx = SParser.PythonCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1992
                localctx.t = self.match(SParser.CHAR_LITERAL)

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
            super(SParser.Python_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(SParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(SParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(SParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(SParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(SParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(SParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(SParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(SParser.DATE, 0)

        def TIME(self):
            return self.getToken(SParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(SParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(SParser.PERIOD, 0)

        def READ(self):
            return self.getToken(SParser.READ, 0)

        def WRITE(self):
            return self.getToken(SParser.WRITE, 0)

        def TEST(self):
            return self.getToken(SParser.TEST, 0)

        def SELF(self):
            return self.getToken(SParser.SELF, 0)

        def THIS(self):
            return self.getToken(SParser.THIS, 0)

        def getRuleIndex(self):
            return SParser.RULE_python_identifier

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterPython_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitPython_identifier(self)




    def python_identifier(self):

        localctx = SParser.Python_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 338, self.RULE_python_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1995
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 127)) & ~0x3f) == 0 and ((1 << (_la - 127)) & ((1 << (SParser.READ - 127)) | (1 << (SParser.SELF - 127)) | (1 << (SParser.TEST - 127)) | (1 << (SParser.THIS - 127)) | (1 << (SParser.WRITE - 127)) | (1 << (SParser.SYMBOL_IDENTIFIER - 127)) | (1 << (SParser.TYPE_IDENTIFIER - 127)) | (1 << (SParser.VARIABLE_IDENTIFIER - 127)))) != 0)):
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
            super(SParser.Java_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_java_statement

     
        def copyFrom(self, ctx):
            super(SParser.Java_statementContext, self).copyFrom(ctx)



    class JavaReturnStatementContext(Java_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_statementContext)
            super(SParser.JavaReturnStatementContext, self).__init__(parser)
            self.exp = None # Java_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(SParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(SParser.SEMI, 0)
        def java_expression(self):
            return self.getTypedRuleContext(SParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaReturnStatement(self)


    class JavaStatementContext(Java_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_statementContext)
            super(SParser.JavaStatementContext, self).__init__(parser)
            self.exp = None # Java_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(SParser.SEMI, 0)
        def java_expression(self):
            return self.getTypedRuleContext(SParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaStatement(self)



    def java_statement(self):

        localctx = SParser.Java_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 340, self.RULE_java_statement)
        try:
            self.state = 2004
            token = self._input.LA(1)
            if token in [SParser.RETURN]:
                localctx = SParser.JavaReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1997
                self.match(SParser.RETURN)
                self.state = 1998 
                localctx.exp = self.java_expression(0)
                self.state = 1999
                self.match(SParser.SEMI)

            elif token in [SParser.LPAR, SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.SELF, SParser.TEST, SParser.THIS, SParser.WRITE, SParser.BOOLEAN_LITERAL, SParser.CHAR_LITERAL, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER, SParser.NATIVE_IDENTIFIER, SParser.DOLLAR_IDENTIFIER, SParser.TEXT_LITERAL, SParser.INTEGER_LITERAL, SParser.DECIMAL_LITERAL]:
                localctx = SParser.JavaStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2001 
                localctx.exp = self.java_expression(0)
                self.state = 2002
                self.match(SParser.SEMI)

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
            super(SParser.Java_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_java_expression

     
        def copyFrom(self, ctx):
            super(SParser.Java_expressionContext, self).copyFrom(ctx)


    class JavaSelectorExpressionContext(Java_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_expressionContext)
            super(SParser.JavaSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Java_expressionContext
            self.child = None # Java_selector_expressionContext
            self.copyFrom(ctx)

        def java_expression(self):
            return self.getTypedRuleContext(SParser.Java_expressionContext,0)

        def java_selector_expression(self):
            return self.getTypedRuleContext(SParser.Java_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaSelectorExpression(self)


    class JavaPrimaryExpressionContext(Java_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_expressionContext)
            super(SParser.JavaPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Java_primary_expressionContext
            self.copyFrom(ctx)

        def java_primary_expression(self):
            return self.getTypedRuleContext(SParser.Java_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaPrimaryExpression(self)



    def java_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Java_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 342
        self.enterRecursionRule(localctx, 342, self.RULE_java_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavaPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2007 
            localctx.exp = self.java_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2013
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,151,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.JavaSelectorExpressionContext(self, SParser.Java_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_expression)
                    self.state = 2009
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2010 
                    localctx.child = self.java_selector_expression() 
                self.state = 2015
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,151,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Java_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def java_this_expression(self):
            return self.getTypedRuleContext(SParser.Java_this_expressionContext,0)


        def java_new_expression(self):
            return self.getTypedRuleContext(SParser.Java_new_expressionContext,0)


        def java_parenthesis_expression(self):
            return self.getTypedRuleContext(SParser.Java_parenthesis_expressionContext,0)


        def java_identifier_expression(self):
            return self.getTypedRuleContext(SParser.Java_identifier_expressionContext,0)


        def java_literal_expression(self):
            return self.getTypedRuleContext(SParser.Java_literal_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_java_primary_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJava_primary_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJava_primary_expression(self)




    def java_primary_expression(self):

        localctx = SParser.Java_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 344, self.RULE_java_primary_expression)
        try:
            self.state = 2021
            la_ = self._interp.adaptivePredict(self._input,152,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2016 
                self.java_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2017 
                self.java_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2018 
                self.java_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2019 
                self.java_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2020 
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
            super(SParser.Java_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(SParser.This_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_java_this_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJava_this_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJava_this_expression(self)




    def java_this_expression(self):

        localctx = SParser.Java_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 346, self.RULE_java_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2023 
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
            super(SParser.Java_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(SParser.New_tokenContext,0)


        def java_method_expression(self):
            return self.getTypedRuleContext(SParser.Java_method_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_java_new_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJava_new_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJava_new_expression(self)




    def java_new_expression(self):

        localctx = SParser.Java_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 348, self.RULE_java_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2025 
            self.new_token()
            self.state = 2026 
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
            super(SParser.Java_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_java_selector_expression

     
        def copyFrom(self, ctx):
            super(SParser.Java_selector_expressionContext, self).copyFrom(ctx)



    class JavaItemExpressionContext(Java_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_selector_expressionContext)
            super(SParser.JavaItemExpressionContext, self).__init__(parser)
            self.exp = None # Java_item_expressionContext
            self.copyFrom(ctx)

        def java_item_expression(self):
            return self.getTypedRuleContext(SParser.Java_item_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaItemExpression(self)


    class JavaMethodExpressionContext(Java_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_selector_expressionContext)
            super(SParser.JavaMethodExpressionContext, self).__init__(parser)
            self.exp = None # Java_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def java_method_expression(self):
            return self.getTypedRuleContext(SParser.Java_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaMethodExpression(self)



    def java_selector_expression(self):

        localctx = SParser.Java_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 350, self.RULE_java_selector_expression)
        try:
            self.state = 2031
            token = self._input.LA(1)
            if token in [SParser.DOT]:
                localctx = SParser.JavaMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2028
                self.match(SParser.DOT)
                self.state = 2029 
                localctx.exp = self.java_method_expression()

            elif token in [SParser.LBRAK]:
                localctx = SParser.JavaItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2030 
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
            super(SParser.Java_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Java_identifierContext
            self.args = None # Java_argumentsContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def java_identifier(self):
            return self.getTypedRuleContext(SParser.Java_identifierContext,0)


        def java_arguments(self):
            return self.getTypedRuleContext(SParser.Java_argumentsContext,0)


        def getRuleIndex(self):
            return SParser.RULE_java_method_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJava_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJava_method_expression(self)




    def java_method_expression(self):

        localctx = SParser.Java_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 352, self.RULE_java_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2033 
            localctx.name = self.java_identifier()
            self.state = 2034
            self.match(SParser.LPAR)
            self.state = 2036
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 127)) & ~0x3f) == 0 and ((1 << (_la - 127)) & ((1 << (SParser.READ - 127)) | (1 << (SParser.SELF - 127)) | (1 << (SParser.TEST - 127)) | (1 << (SParser.THIS - 127)) | (1 << (SParser.WRITE - 127)) | (1 << (SParser.BOOLEAN_LITERAL - 127)) | (1 << (SParser.CHAR_LITERAL - 127)) | (1 << (SParser.SYMBOL_IDENTIFIER - 127)) | (1 << (SParser.TYPE_IDENTIFIER - 127)) | (1 << (SParser.VARIABLE_IDENTIFIER - 127)) | (1 << (SParser.NATIVE_IDENTIFIER - 127)) | (1 << (SParser.DOLLAR_IDENTIFIER - 127)) | (1 << (SParser.TEXT_LITERAL - 127)) | (1 << (SParser.INTEGER_LITERAL - 127)) | (1 << (SParser.DECIMAL_LITERAL - 127)))) != 0):
                self.state = 2035 
                localctx.args = self.java_arguments(0)


            self.state = 2038
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Java_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_java_arguments

     
        def copyFrom(self, ctx):
            super(SParser.Java_argumentsContext, self).copyFrom(ctx)


    class JavaArgumentListItemContext(Java_argumentsContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_argumentsContext)
            super(SParser.JavaArgumentListItemContext, self).__init__(parser)
            self.items = None # Java_argumentsContext
            self.item = None # Java_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def java_arguments(self):
            return self.getTypedRuleContext(SParser.Java_argumentsContext,0)

        def java_expression(self):
            return self.getTypedRuleContext(SParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaArgumentListItem(self)


    class JavaArgumentListContext(Java_argumentsContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_argumentsContext)
            super(SParser.JavaArgumentListContext, self).__init__(parser)
            self.item = None # Java_expressionContext
            self.copyFrom(ctx)

        def java_expression(self):
            return self.getTypedRuleContext(SParser.Java_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaArgumentList(self)



    def java_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Java_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 354
        self.enterRecursionRule(localctx, 354, self.RULE_java_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavaArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2041 
            localctx.item = self.java_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2048
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,155,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.JavaArgumentListItemContext(self, SParser.Java_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_arguments)
                    self.state = 2043
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2044
                    self.match(SParser.COMMA)
                    self.state = 2045 
                    localctx.item = self.java_expression(0) 
                self.state = 2050
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,155,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Java_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Java_expressionContext

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)

        def java_expression(self):
            return self.getTypedRuleContext(SParser.Java_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_java_item_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJava_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJava_item_expression(self)




    def java_item_expression(self):

        localctx = SParser.Java_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 356, self.RULE_java_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2051
            self.match(SParser.LBRAK)
            self.state = 2052 
            localctx.exp = self.java_expression(0)
            self.state = 2053
            self.match(SParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Java_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Java_expressionContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def java_expression(self):
            return self.getTypedRuleContext(SParser.Java_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_java_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJava_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJava_parenthesis_expression(self)




    def java_parenthesis_expression(self):

        localctx = SParser.Java_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 358, self.RULE_java_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2055
            self.match(SParser.LPAR)
            self.state = 2056 
            localctx.exp = self.java_expression(0)
            self.state = 2057
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Java_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Java_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_java_identifier_expression

     
        def copyFrom(self, ctx):
            super(SParser.Java_identifier_expressionContext, self).copyFrom(ctx)


    class JavaIdentifierContext(Java_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_identifier_expressionContext)
            super(SParser.JavaIdentifierContext, self).__init__(parser)
            self.name = None # Java_identifierContext
            self.copyFrom(ctx)

        def java_identifier(self):
            return self.getTypedRuleContext(SParser.Java_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaIdentifier(self)


    class JavaChildIdentifierContext(Java_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_identifier_expressionContext)
            super(SParser.JavaChildIdentifierContext, self).__init__(parser)
            self.parent = None # Java_identifier_expressionContext
            self.name = None # Java_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def java_identifier_expression(self):
            return self.getTypedRuleContext(SParser.Java_identifier_expressionContext,0)

        def java_identifier(self):
            return self.getTypedRuleContext(SParser.Java_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaChildIdentifier(self)



    def java_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Java_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 360
        self.enterRecursionRule(localctx, 360, self.RULE_java_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavaIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2060 
            localctx.name = self.java_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2067
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,156,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.JavaChildIdentifierContext(self, SParser.Java_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_identifier_expression)
                    self.state = 2062
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2063
                    self.match(SParser.DOT)
                    self.state = 2064 
                    localctx.name = self.java_identifier() 
                self.state = 2069
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,156,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_class_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Java_class_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_java_class_identifier_expression

     
        def copyFrom(self, ctx):
            super(SParser.Java_class_identifier_expressionContext, self).copyFrom(ctx)


    class JavaClassIdentifierContext(Java_class_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_class_identifier_expressionContext)
            super(SParser.JavaClassIdentifierContext, self).__init__(parser)
            self.klass = None # Java_identifier_expressionContext
            self.copyFrom(ctx)

        def java_identifier_expression(self):
            return self.getTypedRuleContext(SParser.Java_identifier_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaClassIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaClassIdentifier(self)


    class JavaChildClassIdentifierContext(Java_class_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_class_identifier_expressionContext)
            super(SParser.JavaChildClassIdentifierContext, self).__init__(parser)
            self.parent = None # Java_class_identifier_expressionContext
            self.name = None # Token
            self.copyFrom(ctx)

        def java_class_identifier_expression(self):
            return self.getTypedRuleContext(SParser.Java_class_identifier_expressionContext,0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(SParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaChildClassIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaChildClassIdentifier(self)



    def java_class_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Java_class_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 362
        self.enterRecursionRule(localctx, 362, self.RULE_java_class_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavaClassIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2071 
            localctx.klass = self.java_identifier_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2077
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,157,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.JavaChildClassIdentifierContext(self, SParser.Java_class_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_class_identifier_expression)
                    self.state = 2073
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2074
                    localctx.name = self.match(SParser.DOLLAR_IDENTIFIER) 
                self.state = 2079
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,157,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Java_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Java_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_java_literal_expression

     
        def copyFrom(self, ctx):
            super(SParser.Java_literal_expressionContext, self).copyFrom(ctx)



    class JavaBooleanLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_literal_expressionContext)
            super(SParser.JavaBooleanLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(SParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaBooleanLiteral(self)


    class JavaCharacterLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_literal_expressionContext)
            super(SParser.JavaCharacterLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(SParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaCharacterLiteral(self)


    class JavaIntegerLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_literal_expressionContext)
            super(SParser.JavaIntegerLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(SParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaIntegerLiteral(self)


    class JavaTextLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_literal_expressionContext)
            super(SParser.JavaTextLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(SParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaTextLiteral(self)


    class JavaDecimalLiteralContext(Java_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Java_literal_expressionContext)
            super(SParser.JavaDecimalLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(SParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJavaDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJavaDecimalLiteral(self)



    def java_literal_expression(self):

        localctx = SParser.Java_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 364, self.RULE_java_literal_expression)
        try:
            self.state = 2085
            token = self._input.LA(1)
            if token in [SParser.INTEGER_LITERAL]:
                localctx = SParser.JavaIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2080
                localctx.t = self.match(SParser.INTEGER_LITERAL)

            elif token in [SParser.DECIMAL_LITERAL]:
                localctx = SParser.JavaDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2081
                localctx.t = self.match(SParser.DECIMAL_LITERAL)

            elif token in [SParser.TEXT_LITERAL]:
                localctx = SParser.JavaTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2082
                localctx.t = self.match(SParser.TEXT_LITERAL)

            elif token in [SParser.BOOLEAN_LITERAL]:
                localctx = SParser.JavaBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2083
                localctx.t = self.match(SParser.BOOLEAN_LITERAL)

            elif token in [SParser.CHAR_LITERAL]:
                localctx = SParser.JavaCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2084
                localctx.t = self.match(SParser.CHAR_LITERAL)

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
            super(SParser.Java_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(SParser.SYMBOL_IDENTIFIER, 0)

        def NATIVE_IDENTIFIER(self):
            return self.getToken(SParser.NATIVE_IDENTIFIER, 0)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(SParser.DOLLAR_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(SParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(SParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(SParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(SParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(SParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(SParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(SParser.DATE, 0)

        def TIME(self):
            return self.getToken(SParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(SParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(SParser.PERIOD, 0)

        def READ(self):
            return self.getToken(SParser.READ, 0)

        def WRITE(self):
            return self.getToken(SParser.WRITE, 0)

        def TEST(self):
            return self.getToken(SParser.TEST, 0)

        def getRuleIndex(self):
            return SParser.RULE_java_identifier

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterJava_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitJava_identifier(self)




    def java_identifier(self):

        localctx = SParser.Java_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 366, self.RULE_java_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2087
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 127)) & ~0x3f) == 0 and ((1 << (_la - 127)) & ((1 << (SParser.READ - 127)) | (1 << (SParser.TEST - 127)) | (1 << (SParser.WRITE - 127)) | (1 << (SParser.SYMBOL_IDENTIFIER - 127)) | (1 << (SParser.TYPE_IDENTIFIER - 127)) | (1 << (SParser.VARIABLE_IDENTIFIER - 127)) | (1 << (SParser.NATIVE_IDENTIFIER - 127)) | (1 << (SParser.DOLLAR_IDENTIFIER - 127)))) != 0)):
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
            super(SParser.Csharp_statementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_csharp_statement

     
        def copyFrom(self, ctx):
            super(SParser.Csharp_statementContext, self).copyFrom(ctx)



    class CSharpReturnStatementContext(Csharp_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_statementContext)
            super(SParser.CSharpReturnStatementContext, self).__init__(parser)
            self.exp = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(SParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(SParser.SEMI, 0)
        def csharp_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpReturnStatement(self)


    class CSharpStatementContext(Csharp_statementContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_statementContext)
            super(SParser.CSharpStatementContext, self).__init__(parser)
            self.exp = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(SParser.SEMI, 0)
        def csharp_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpStatement(self)



    def csharp_statement(self):

        localctx = SParser.Csharp_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 368, self.RULE_csharp_statement)
        try:
            self.state = 2096
            token = self._input.LA(1)
            if token in [SParser.RETURN]:
                localctx = SParser.CSharpReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2089
                self.match(SParser.RETURN)
                self.state = 2090 
                localctx.exp = self.csharp_expression(0)
                self.state = 2091
                self.match(SParser.SEMI)

            elif token in [SParser.LPAR, SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.SELF, SParser.TEST, SParser.THIS, SParser.WRITE, SParser.BOOLEAN_LITERAL, SParser.CHAR_LITERAL, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER, SParser.DOLLAR_IDENTIFIER, SParser.TEXT_LITERAL, SParser.INTEGER_LITERAL, SParser.DECIMAL_LITERAL]:
                localctx = SParser.CSharpStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2093 
                localctx.exp = self.csharp_expression(0)
                self.state = 2094
                self.match(SParser.SEMI)

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
            super(SParser.Csharp_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_csharp_expression

     
        def copyFrom(self, ctx):
            super(SParser.Csharp_expressionContext, self).copyFrom(ctx)


    class CSharpSelectorExpressionContext(Csharp_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_expressionContext)
            super(SParser.CSharpSelectorExpressionContext, self).__init__(parser)
            self.parent = None # Csharp_expressionContext
            self.child = None # Csharp_selector_expressionContext
            self.copyFrom(ctx)

        def csharp_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_expressionContext,0)

        def csharp_selector_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_selector_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpSelectorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpSelectorExpression(self)


    class CSharpPrimaryExpressionContext(Csharp_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_expressionContext)
            super(SParser.CSharpPrimaryExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_primary_expressionContext
            self.copyFrom(ctx)

        def csharp_primary_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_primary_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpPrimaryExpression(self)



    def csharp_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Csharp_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 370
        self.enterRecursionRule(localctx, 370, self.RULE_csharp_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.CSharpPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2099 
            localctx.exp = self.csharp_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2105
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,160,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CSharpSelectorExpressionContext(self, SParser.Csharp_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_expression)
                    self.state = 2101
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2102 
                    localctx.child = self.csharp_selector_expression() 
                self.state = 2107
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,160,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Csharp_primary_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def csharp_this_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_this_expressionContext,0)


        def csharp_new_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_new_expressionContext,0)


        def csharp_parenthesis_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_parenthesis_expressionContext,0)


        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_identifier_expressionContext,0)


        def csharp_literal_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_literal_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_csharp_primary_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCsharp_primary_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCsharp_primary_expression(self)




    def csharp_primary_expression(self):

        localctx = SParser.Csharp_primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 372, self.RULE_csharp_primary_expression)
        try:
            self.state = 2113
            la_ = self._interp.adaptivePredict(self._input,161,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2108 
                self.csharp_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2109 
                self.csharp_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2110 
                self.csharp_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2111 
                self.csharp_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2112 
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
            super(SParser.Csharp_this_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def this_expression(self):
            return self.getTypedRuleContext(SParser.This_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_csharp_this_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCsharp_this_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCsharp_this_expression(self)




    def csharp_this_expression(self):

        localctx = SParser.Csharp_this_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 374, self.RULE_csharp_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2115 
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
            super(SParser.Csharp_new_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def new_token(self):
            return self.getTypedRuleContext(SParser.New_tokenContext,0)


        def csharp_method_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_method_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_csharp_new_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCsharp_new_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCsharp_new_expression(self)




    def csharp_new_expression(self):

        localctx = SParser.Csharp_new_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 376, self.RULE_csharp_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2117 
            self.new_token()
            self.state = 2118 
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
            super(SParser.Csharp_selector_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_csharp_selector_expression

     
        def copyFrom(self, ctx):
            super(SParser.Csharp_selector_expressionContext, self).copyFrom(ctx)



    class CSharpMethodExpressionContext(Csharp_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_selector_expressionContext)
            super(SParser.CSharpMethodExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_method_expressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def csharp_method_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_method_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpMethodExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpMethodExpression(self)


    class CSharpItemExpressionContext(Csharp_selector_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_selector_expressionContext)
            super(SParser.CSharpItemExpressionContext, self).__init__(parser)
            self.exp = None # Csharp_item_expressionContext
            self.copyFrom(ctx)

        def csharp_item_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_item_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpItemExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpItemExpression(self)



    def csharp_selector_expression(self):

        localctx = SParser.Csharp_selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 378, self.RULE_csharp_selector_expression)
        try:
            self.state = 2123
            token = self._input.LA(1)
            if token in [SParser.DOT]:
                localctx = SParser.CSharpMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2120
                self.match(SParser.DOT)
                self.state = 2121 
                localctx.exp = self.csharp_method_expression()

            elif token in [SParser.LBRAK]:
                localctx = SParser.CSharpItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2122 
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
            super(SParser.Csharp_method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Csharp_identifierContext
            self.args = None # Csharp_argumentsContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def csharp_identifier(self):
            return self.getTypedRuleContext(SParser.Csharp_identifierContext,0)


        def csharp_arguments(self):
            return self.getTypedRuleContext(SParser.Csharp_argumentsContext,0)


        def getRuleIndex(self):
            return SParser.RULE_csharp_method_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCsharp_method_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCsharp_method_expression(self)




    def csharp_method_expression(self):

        localctx = SParser.Csharp_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 380, self.RULE_csharp_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2125 
            localctx.name = self.csharp_identifier()
            self.state = 2126
            self.match(SParser.LPAR)
            self.state = 2128
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 127)) & ~0x3f) == 0 and ((1 << (_la - 127)) & ((1 << (SParser.READ - 127)) | (1 << (SParser.SELF - 127)) | (1 << (SParser.TEST - 127)) | (1 << (SParser.THIS - 127)) | (1 << (SParser.WRITE - 127)) | (1 << (SParser.BOOLEAN_LITERAL - 127)) | (1 << (SParser.CHAR_LITERAL - 127)) | (1 << (SParser.SYMBOL_IDENTIFIER - 127)) | (1 << (SParser.TYPE_IDENTIFIER - 127)) | (1 << (SParser.VARIABLE_IDENTIFIER - 127)) | (1 << (SParser.DOLLAR_IDENTIFIER - 127)) | (1 << (SParser.TEXT_LITERAL - 127)) | (1 << (SParser.INTEGER_LITERAL - 127)) | (1 << (SParser.DECIMAL_LITERAL - 127)))) != 0):
                self.state = 2127 
                localctx.args = self.csharp_arguments(0)


            self.state = 2130
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Csharp_argumentsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_csharp_arguments

     
        def copyFrom(self, ctx):
            super(SParser.Csharp_argumentsContext, self).copyFrom(ctx)


    class CSharpArgumentListContext(Csharp_argumentsContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_argumentsContext)
            super(SParser.CSharpArgumentListContext, self).__init__(parser)
            self.item = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def csharp_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpArgumentList(self)


    class CSharpArgumentListItemContext(Csharp_argumentsContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_argumentsContext)
            super(SParser.CSharpArgumentListItemContext, self).__init__(parser)
            self.items = None # Csharp_argumentsContext
            self.item = None # Csharp_expressionContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(SParser.COMMA, 0)
        def csharp_arguments(self):
            return self.getTypedRuleContext(SParser.Csharp_argumentsContext,0)

        def csharp_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_expressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpArgumentListItem(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpArgumentListItem(self)



    def csharp_arguments(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Csharp_argumentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 382
        self.enterRecursionRule(localctx, 382, self.RULE_csharp_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.CSharpArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2133 
            localctx.item = self.csharp_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2140
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,164,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CSharpArgumentListItemContext(self, SParser.Csharp_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_arguments)
                    self.state = 2135
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2136
                    self.match(SParser.COMMA)
                    self.state = 2137 
                    localctx.item = self.csharp_expression(0) 
                self.state = 2142
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,164,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_item_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Csharp_item_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Csharp_expressionContext

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)

        def csharp_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_csharp_item_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCsharp_item_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCsharp_item_expression(self)




    def csharp_item_expression(self):

        localctx = SParser.Csharp_item_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 384, self.RULE_csharp_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2143
            self.match(SParser.LBRAK)
            self.state = 2144 
            localctx.exp = self.csharp_expression(0)
            self.state = 2145
            self.match(SParser.RBRAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_parenthesis_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Csharp_parenthesis_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.exp = None # Csharp_expressionContext

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def csharp_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_csharp_parenthesis_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCsharp_parenthesis_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCsharp_parenthesis_expression(self)




    def csharp_parenthesis_expression(self):

        localctx = SParser.Csharp_parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 386, self.RULE_csharp_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2147
            self.match(SParser.LPAR)
            self.state = 2148 
            localctx.exp = self.csharp_expression(0)
            self.state = 2149
            self.match(SParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Csharp_identifier_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Csharp_identifier_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_csharp_identifier_expression

     
        def copyFrom(self, ctx):
            super(SParser.Csharp_identifier_expressionContext, self).copyFrom(ctx)


    class CSharpIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_identifier_expressionContext)
            super(SParser.CSharpIdentifierContext, self).__init__(parser)
            self.name = None # Csharp_identifierContext
            self.copyFrom(ctx)

        def csharp_identifier(self):
            return self.getTypedRuleContext(SParser.Csharp_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpIdentifier(self)


    class CSharpChildIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_identifier_expressionContext)
            super(SParser.CSharpChildIdentifierContext, self).__init__(parser)
            self.parent = None # Csharp_identifier_expressionContext
            self.name = None # Csharp_identifierContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(SParser.DOT, 0)
        def csharp_identifier_expression(self):
            return self.getTypedRuleContext(SParser.Csharp_identifier_expressionContext,0)

        def csharp_identifier(self):
            return self.getTypedRuleContext(SParser.Csharp_identifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpChildIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpChildIdentifier(self)


    class CSharpPromptoIdentifierContext(Csharp_identifier_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_identifier_expressionContext)
            super(SParser.CSharpPromptoIdentifierContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DOLLAR_IDENTIFIER(self):
            return self.getToken(SParser.DOLLAR_IDENTIFIER, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpPromptoIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpPromptoIdentifier(self)



    def csharp_identifier_expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SParser.Csharp_identifier_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 388
        self.enterRecursionRule(localctx, 388, self.RULE_csharp_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2154
            token = self._input.LA(1)
            if token in [SParser.DOLLAR_IDENTIFIER]:
                localctx = SParser.CSharpPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2152
                self.match(SParser.DOLLAR_IDENTIFIER)

            elif token in [SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.TEST, SParser.WRITE, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER]:
                localctx = SParser.CSharpIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2153 
                localctx.name = self.csharp_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2161
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,166,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CSharpChildIdentifierContext(self, SParser.Csharp_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_identifier_expression)
                    self.state = 2156
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2157
                    self.match(SParser.DOT)
                    self.state = 2158 
                    localctx.name = self.csharp_identifier() 
                self.state = 2163
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,166,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Csharp_literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Csharp_literal_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_csharp_literal_expression

     
        def copyFrom(self, ctx):
            super(SParser.Csharp_literal_expressionContext, self).copyFrom(ctx)



    class CSharpBooleanLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_literal_expressionContext)
            super(SParser.CSharpBooleanLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN_LITERAL(self):
            return self.getToken(SParser.BOOLEAN_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpBooleanLiteral(self)


    class CSharpIntegerLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_literal_expressionContext)
            super(SParser.CSharpIntegerLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(SParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpIntegerLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpIntegerLiteral(self)


    class CSharpDecimalLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_literal_expressionContext)
            super(SParser.CSharpDecimalLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(SParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpDecimalLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpDecimalLiteral(self)


    class CSharpCharacterLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_literal_expressionContext)
            super(SParser.CSharpCharacterLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(SParser.CHAR_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpCharacterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpCharacterLiteral(self)


    class CSharpTextLiteralContext(Csharp_literal_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Csharp_literal_expressionContext)
            super(SParser.CSharpTextLiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TEXT_LITERAL(self):
            return self.getToken(SParser.TEXT_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCSharpTextLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCSharpTextLiteral(self)



    def csharp_literal_expression(self):

        localctx = SParser.Csharp_literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 390, self.RULE_csharp_literal_expression)
        try:
            self.state = 2169
            token = self._input.LA(1)
            if token in [SParser.INTEGER_LITERAL]:
                localctx = SParser.CSharpIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2164
                self.match(SParser.INTEGER_LITERAL)

            elif token in [SParser.DECIMAL_LITERAL]:
                localctx = SParser.CSharpDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2165
                self.match(SParser.DECIMAL_LITERAL)

            elif token in [SParser.TEXT_LITERAL]:
                localctx = SParser.CSharpTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2166
                self.match(SParser.TEXT_LITERAL)

            elif token in [SParser.BOOLEAN_LITERAL]:
                localctx = SParser.CSharpBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2167
                self.match(SParser.BOOLEAN_LITERAL)

            elif token in [SParser.CHAR_LITERAL]:
                localctx = SParser.CSharpCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2168
                self.match(SParser.CHAR_LITERAL)

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
            super(SParser.Csharp_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)

        def SYMBOL_IDENTIFIER(self):
            return self.getToken(SParser.SYMBOL_IDENTIFIER, 0)

        def TYPE_IDENTIFIER(self):
            return self.getToken(SParser.TYPE_IDENTIFIER, 0)

        def BOOLEAN(self):
            return self.getToken(SParser.BOOLEAN, 0)

        def CHARACTER(self):
            return self.getToken(SParser.CHARACTER, 0)

        def TEXT(self):
            return self.getToken(SParser.TEXT, 0)

        def INTEGER(self):
            return self.getToken(SParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(SParser.DECIMAL, 0)

        def DATE(self):
            return self.getToken(SParser.DATE, 0)

        def TIME(self):
            return self.getToken(SParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(SParser.DATETIME, 0)

        def PERIOD(self):
            return self.getToken(SParser.PERIOD, 0)

        def READ(self):
            return self.getToken(SParser.READ, 0)

        def WRITE(self):
            return self.getToken(SParser.WRITE, 0)

        def TEST(self):
            return self.getToken(SParser.TEST, 0)

        def getRuleIndex(self):
            return SParser.RULE_csharp_identifier

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCsharp_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCsharp_identifier(self)




    def csharp_identifier(self):

        localctx = SParser.Csharp_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 392, self.RULE_csharp_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2171
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 127)) & ~0x3f) == 0 and ((1 << (_la - 127)) & ((1 << (SParser.READ - 127)) | (1 << (SParser.TEST - 127)) | (1 << (SParser.WRITE - 127)) | (1 << (SParser.SYMBOL_IDENTIFIER - 127)) | (1 << (SParser.TYPE_IDENTIFIER - 127)) | (1 << (SParser.VARIABLE_IDENTIFIER - 127)))) != 0)):
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
        self._predicates[14] = self.native_category_binding_list_sempred
        self._predicates[26] = self.callable_parent_sempred
        self._predicates[36] = self.else_if_statement_list_sempred
        self._predicates[41] = self.expression_sempred
        self._predicates[43] = self.instance_expression_sempred
        self._predicates[45] = self.instance_selector_sempred
        self._predicates[48] = self.argument_assignment_list_sempred
        self._predicates[55] = self.child_instance_sempred
        self._predicates[63] = self.declarations_sempred
        self._predicates[67] = self.native_symbol_list_sempred
        self._predicates[68] = self.category_symbol_list_sempred
        self._predicates[69] = self.symbol_list_sempred
        self._predicates[73] = self.expression_list_sempred
        self._predicates[75] = self.typedef_sempred
        self._predicates[82] = self.type_identifier_list_sempred
        self._predicates[88] = self.argument_list_sempred
        self._predicates[94] = self.any_type_sempred
        self._predicates[95] = self.member_method_declaration_list_sempred
        self._predicates[97] = self.native_member_method_declaration_list_sempred
        self._predicates[102] = self.module_token_sempred
        self._predicates[105] = self.variable_identifier_list_sempred
        self._predicates[108] = self.native_statement_list_sempred
        self._predicates[112] = self.statement_list_sempred
        self._predicates[113] = self.assertion_list_sempred
        self._predicates[114] = self.switch_case_statement_list_sempred
        self._predicates[115] = self.catch_statement_list_sempred
        self._predicates[118] = self.literal_list_literal_sempred
        self._predicates[126] = self.expression_tuple_sempred
        self._predicates[127] = self.dict_entry_list_sempred
        self._predicates[131] = self.assignable_instance_sempred
        self._predicates[132] = self.is_expression_sempred
        self._predicates[136] = self.new_token_sempred
        self._predicates[137] = self.key_token_sempred
        self._predicates[138] = self.value_token_sempred
        self._predicates[139] = self.symbols_token_sempred
        self._predicates[146] = self.javascript_expression_sempred
        self._predicates[152] = self.javascript_arguments_sempred
        self._predicates[159] = self.python_expression_sempred
        self._predicates[164] = self.python_ordinal_argument_list_sempred
        self._predicates[165] = self.python_named_argument_list_sempred
        self._predicates[167] = self.python_identifier_expression_sempred
        self._predicates[171] = self.java_expression_sempred
        self._predicates[177] = self.java_arguments_sempred
        self._predicates[180] = self.java_identifier_expression_sempred
        self._predicates[181] = self.java_class_identifier_expression_sempred
        self._predicates[185] = self.csharp_expression_sempred
        self._predicates[191] = self.csharp_arguments_sempred
        self._predicates[194] = self.csharp_identifier_expression_sempred
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
                return self.precpred(self._ctx, 21)
         

            if predIndex == 28:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 29:
                return self.precpred(self._ctx, 13)
         

    def instance_expression_sempred(self, localctx, predIndex):
            if predIndex == 30:
                return self.precpred(self._ctx, 1)
         

    def instance_selector_sempred(self, localctx, predIndex):
            if predIndex == 31:
                return self.wasNot(SParser.WS)
         

            if predIndex == 32:
                return self.wasNot(SParser.WS)
         

            if predIndex == 33:
                return self.wasNot(SParser.WS)
         

    def argument_assignment_list_sempred(self, localctx, predIndex):
            if predIndex == 34:
                return self.willNotBe(self.equalToken())
         

            if predIndex == 35:
                return self.precpred(self._ctx, 1)
         

    def child_instance_sempred(self, localctx, predIndex):
            if predIndex == 36:
                return self.wasNot(SParser.WS)
         

            if predIndex == 37:
                return self.wasNot(SParser.WS)
         

    def declarations_sempred(self, localctx, predIndex):
            if predIndex == 38:
                return self.precpred(self._ctx, 1)
         

    def native_symbol_list_sempred(self, localctx, predIndex):
            if predIndex == 39:
                return self.precpred(self._ctx, 1)
         

    def category_symbol_list_sempred(self, localctx, predIndex):
            if predIndex == 40:
                return self.precpred(self._ctx, 1)
         

    def symbol_list_sempred(self, localctx, predIndex):
            if predIndex == 41:
                return self.precpred(self._ctx, 1)
         

    def expression_list_sempred(self, localctx, predIndex):
            if predIndex == 42:
                return self.precpred(self._ctx, 1)
         

    def typedef_sempred(self, localctx, predIndex):
            if predIndex == 43:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 44:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 45:
                return self.precpred(self._ctx, 1)
         

    def type_identifier_list_sempred(self, localctx, predIndex):
            if predIndex == 46:
                return self.precpred(self._ctx, 1)
         

    def argument_list_sempred(self, localctx, predIndex):
            if predIndex == 47:
                return self.precpred(self._ctx, 1)
         

    def any_type_sempred(self, localctx, predIndex):
            if predIndex == 48:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 49:
                return self.precpred(self._ctx, 1)
         

    def member_method_declaration_list_sempred(self, localctx, predIndex):
            if predIndex == 50:
                return self.precpred(self._ctx, 1)
         

    def native_member_method_declaration_list_sempred(self, localctx, predIndex):
            if predIndex == 51:
                return self.precpred(self._ctx, 1)
         

    def module_token_sempred(self, localctx, predIndex):
            if predIndex == 52:
                return self.isText(localctx.i1,"module")
         

    def variable_identifier_list_sempred(self, localctx, predIndex):
            if predIndex == 53:
                return self.precpred(self._ctx, 1)
         

    def native_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 54:
                return self.precpred(self._ctx, 1)
         

    def statement_list_sempred(self, localctx, predIndex):
            if predIndex == 55:
                return self.precpred(self._ctx, 1)
         

    def assertion_list_sempred(self, localctx, predIndex):
            if predIndex == 56:
                return self.precpred(self._ctx, 1)
         

    def switch_case_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 57:
                return self.precpred(self._ctx, 1)
         

    def catch_statement_list_sempred(self, localctx, predIndex):
            if predIndex == 58:
                return self.precpred(self._ctx, 1)
         

    def literal_list_literal_sempred(self, localctx, predIndex):
            if predIndex == 59:
                return self.precpred(self._ctx, 1)
         

    def expression_tuple_sempred(self, localctx, predIndex):
            if predIndex == 60:
                return self.precpred(self._ctx, 1)
         

    def dict_entry_list_sempred(self, localctx, predIndex):
            if predIndex == 61:
                return self.precpred(self._ctx, 1)
         

    def assignable_instance_sempred(self, localctx, predIndex):
            if predIndex == 62:
                return self.precpred(self._ctx, 1)
         

    def is_expression_sempred(self, localctx, predIndex):
            if predIndex == 63:
                return self.willBeAOrAn()
         

    def new_token_sempred(self, localctx, predIndex):
            if predIndex == 64:
                return self.isText(localctx.i1,"new")
         

    def key_token_sempred(self, localctx, predIndex):
            if predIndex == 65:
                return self.isText(localctx.i1,"key")
         

    def value_token_sempred(self, localctx, predIndex):
            if predIndex == 66:
                return self.isText(localctx.i1,"value")
         

    def symbols_token_sempred(self, localctx, predIndex):
            if predIndex == 67:
                return self.isText(localctx.i1,"symbols")
         

    def javascript_expression_sempred(self, localctx, predIndex):
            if predIndex == 68:
                return self.precpred(self._ctx, 1)
         

    def javascript_arguments_sempred(self, localctx, predIndex):
            if predIndex == 69:
                return self.precpred(self._ctx, 1)
         

    def python_expression_sempred(self, localctx, predIndex):
            if predIndex == 70:
                return self.precpred(self._ctx, 1)
         

    def python_ordinal_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 71:
                return self.precpred(self._ctx, 1)
         

    def python_named_argument_list_sempred(self, localctx, predIndex):
            if predIndex == 72:
                return self.precpred(self._ctx, 1)
         

    def python_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 73:
                return self.precpred(self._ctx, 1)
         

    def java_expression_sempred(self, localctx, predIndex):
            if predIndex == 74:
                return self.precpred(self._ctx, 1)
         

    def java_arguments_sempred(self, localctx, predIndex):
            if predIndex == 75:
                return self.precpred(self._ctx, 1)
         

    def java_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 76:
                return self.precpred(self._ctx, 1)
         

    def java_class_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 77:
                return self.precpred(self._ctx, 1)
         

    def csharp_expression_sempred(self, localctx, predIndex):
            if predIndex == 78:
                return self.precpred(self._ctx, 1)
         

    def csharp_arguments_sempred(self, localctx, predIndex):
            if predIndex == 79:
                return self.precpred(self._ctx, 1)
         

    def csharp_identifier_expression_sempred(self, localctx, predIndex):
            if predIndex == 80:
                return self.precpred(self._ctx, 1)
         


