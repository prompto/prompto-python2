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
        buf.write(u"\u00ae\u08c3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
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
        buf.write(u"\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u01a3\n\2\3\2\5\2\u01a6")
        buf.write(u"\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\5\5\u01bf")
        buf.write(u"\n\5\3\5\3\5\3\6\5\6\u01c4\n\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write(u"\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u01d2\n\6\3\6\3\6\3\6")
        buf.write(u"\3\6\5\6\u01d8\n\6\5\6\u01da\n\6\5\6\u01dc\n\6\3\6\3")
        buf.write(u"\6\3\7\3\7\3\7\5\7\u01e3\n\7\3\7\3\7\3\b\5\b\u01e8\n")
        buf.write(u"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u01f3\n\b")
        buf.write(u"\3\b\3\b\3\b\3\b\3\b\5\b\u01fa\n\b\3\b\3\b\3\t\3\t\3")
        buf.write(u"\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u0207\n\t\3\t\3\t\3\n")
        buf.write(u"\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u0215")
        buf.write(u"\n\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write(u"\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\5\r\u0229\n\r\3\r\3\r")
        buf.write(u"\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write(u"\3\16\3\16\3\16\3\16\3\17\3\17\3\17\5\17\u0240\n\17\3")
        buf.write(u"\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\5\20\u024b")
        buf.write(u"\n\20\3\20\3\20\3\20\3\20\3\20\5\20\u0252\n\20\3\20\3")
        buf.write(u"\20\3\20\3\20\3\20\3\20\3\20\5\20\u025b\n\20\3\20\3\20")
        buf.write(u"\3\21\3\21\3\21\3\21\3\21\5\21\u0264\n\21\3\21\3\21\3")
        buf.write(u"\21\3\21\3\21\3\21\3\21\5\21\u026d\n\21\3\21\3\21\3\22")
        buf.write(u"\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3")
        buf.write(u"\23\3\23\3\23\3\23\7\23\u0280\n\23\f\23\16\23\u0283\13")
        buf.write(u"\23\3\24\3\24\3\24\3\24\3\24\5\24\u028a\n\24\3\24\3\24")
        buf.write(u"\3\24\5\24\u028f\n\24\3\25\3\25\3\25\3\25\5\25\u0295")
        buf.write(u"\n\25\3\25\3\25\3\25\5\25\u029a\n\25\3\25\3\25\3\25\3")
        buf.write(u"\25\3\25\3\26\3\26\5\26\u02a3\n\26\3\26\3\26\3\26\5\26")
        buf.write(u"\u02a8\n\26\3\26\3\26\3\26\5\26\u02ad\n\26\3\26\3\26")
        buf.write(u"\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write(u"\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27")
        buf.write(u"\u02c5\n\27\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write(u"\31\5\31\u02d0\n\31\3\31\3\31\5\31\u02d4\n\31\3\32\3")
        buf.write(u"\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write(u"\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u02e9\n\32\3")
        buf.write(u"\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write(u"\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write(u"\34\3\34\3\34\5\34\u0303\n\34\3\35\3\35\3\35\5\35\u0308")
        buf.write(u"\n\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\5\36\u0311\n")
        buf.write(u"\36\3\37\3\37\3\37\3\37\3\37\7\37\u0318\n\37\f\37\16")
        buf.write(u"\37\u031b\13\37\3 \3 \3 \3 \3 \3 \5 \u0323\n \3!\3!\3")
        buf.write(u"!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write(u"#\3#\3#\3#\3#\3#\3#\3#\3#\3#\5#\u0340\n#\3#\3#\3$\3$")
        buf.write(u"\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u0353\n$\3")
        buf.write(u"%\3%\3%\3%\5%\u0359\n%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&")
        buf.write(u"\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(")
        buf.write(u"\3(\3(\3(\3(\3(\3(\3(\5(\u037b\n(\3(\3(\3(\3(\3(\3(\3")
        buf.write(u"(\5(\u0384\n(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)")
        buf.write(u"\3)\3)\3)\3)\3)\3)\7)\u0399\n)\f)\16)\u039c\13)\3*\3")
        buf.write(u"*\3*\3+\3+\3+\3+\3+\3+\3+\3+\5+\u03a9\n+\3+\3+\3+\3+")
        buf.write(u"\3+\3+\3+\5+\u03b2\n+\3+\3+\3+\3+\3+\3+\3+\5+\u03bb\n")
        buf.write(u"+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,")
        buf.write(u"\3,\3,\3,\3,\5,\u03d2\n,\3-\3-\3.\3.\5.\u03d8\n.\3/\3")
        buf.write(u"/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\5/")
        buf.write(u"\u03ec\n/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3")
        buf.write(u"/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/")
        buf.write(u"\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3")
        buf.write(u"/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/")
        buf.write(u"\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3")
        buf.write(u"/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\7/\u0452")
        buf.write(u"\n/\f/\16/\u0455\13/\3\60\3\60\3\61\3\61\3\61\3\61\3")
        buf.write(u"\61\7\61\u045e\n\61\f\61\16\61\u0461\13\61\3\62\3\62")
        buf.write(u"\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u046b\n\62\3\63\3")
        buf.write(u"\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write(u"\3\63\5\63\u047a\n\63\3\64\3\64\3\64\5\64\u047f\n\64")
        buf.write(u"\3\64\3\64\3\65\3\65\3\65\5\65\u0486\n\65\3\65\3\65\3")
        buf.write(u"\66\3\66\3\66\5\66\u048d\n\66\3\66\3\66\3\67\3\67\3\67")
        buf.write(u"\3\67\3\67\5\67\u0496\n\67\3\67\3\67\3\67\7\67\u049b")
        buf.write(u"\n\67\f\67\16\67\u049e\13\67\38\38\38\38\39\39\39\39")
        buf.write(u"\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\3<\3<\3<\5<\u04b7")
        buf.write(u"\n<\3<\3<\3<\3<\3<\3<\3<\3<\3<\5<\u04c2\n<\3<\3<\5<\u04c6")
        buf.write(u"\n<\3<\3<\3<\5<\u04cb\n<\3<\3<\3<\5<\u04d0\n<\5<\u04d2")
        buf.write(u"\n<\3=\3=\3=\3=\3=\3=\3=\3=\5=\u04dc\n=\3=\3=\3>\3>\3")
        buf.write(u">\3>\3?\3?\3?\3?\3?\3?\3?\3?\5?\u04ec\n?\3@\3@\3@\3@")
        buf.write(u"\3A\7A\u04f3\nA\fA\16A\u04f6\13A\3B\6B\u04f9\nB\rB\16")
        buf.write(u"B\u04fa\3C\6C\u04fe\nC\rC\16C\u04ff\3C\3C\3D\7D\u0505")
        buf.write(u"\nD\fD\16D\u0508\13D\3D\3D\3E\3E\3F\5F\u050f\nF\3F\3")
        buf.write(u"F\3F\3G\3G\3G\3G\7G\u0518\nG\fG\16G\u051b\13G\3H\3H\3")
        buf.write(u"H\7H\u0520\nH\fH\16H\u0523\13H\3H\3H\3H\3H\3H\5H\u052a")
        buf.write(u"\nH\3I\3I\3J\3J\5J\u0530\nJ\3K\3K\3K\3K\7K\u0536\nK\f")
        buf.write(u"K\16K\u0539\13K\3L\3L\3L\3L\7L\u053f\nL\fL\16L\u0542")
        buf.write(u"\13L\3M\3M\3M\7M\u0547\nM\fM\16M\u054a\13M\3N\3N\3N\3")
        buf.write(u"N\3N\3N\3N\3N\3N\3N\5N\u0556\nN\3O\5O\u0559\nO\3O\3O")
        buf.write(u"\5O\u055d\nO\3O\3O\3P\5P\u0562\nP\3P\3P\5P\u0566\nP\3")
        buf.write(u"P\3P\3Q\3Q\3Q\7Q\u056d\nQ\fQ\16Q\u0570\13Q\3R\3R\3R\3")
        buf.write(u"R\3R\3R\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\5S\u0584")
        buf.write(u"\nS\3S\3S\3S\3S\3S\3S\3S\3S\7S\u058e\nS\fS\16S\u0591")
        buf.write(u"\13S\3T\3T\5T\u0595\nT\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U")
        buf.write(u"\3U\3U\3U\3U\5U\u05a5\nU\3V\3V\3W\5W\u05aa\nW\3W\3W\3")
        buf.write(u"X\3X\3Y\3Y\3Y\5Y\u05b3\nY\3Z\3Z\3Z\7Z\u05b8\nZ\fZ\16")
        buf.write(u"Z\u05bb\13Z\3[\3[\5[\u05bf\n[\3\\\3\\\3\\\5\\\u05c4\n")
        buf.write(u"\\\3]\3]\3^\3^\3_\3_\3`\3`\3a\3a\3a\7a\u05d1\na\fa\16")
        buf.write(u"a\u05d4\13a\3b\3b\5b\u05d8\nb\3b\5b\u05db\nb\3c\3c\5")
        buf.write(u"c\u05df\nc\3d\3d\3d\5d\u05e4\nd\3e\3e\3e\3f\3f\5f\u05eb")
        buf.write(u"\nf\3g\3g\3g\3g\3g\3g\3g\3g\3g\7g\u05f6\ng\fg\16g\u05f9")
        buf.write(u"\13g\3h\3h\3h\3h\7h\u05ff\nh\fh\16h\u0602\13h\3i\3i\3")
        buf.write(u"i\3i\3i\5i\u0609\ni\3j\3j\3j\3j\7j\u060f\nj\fj\16j\u0612")
        buf.write(u"\13j\3k\3k\3k\5k\u0617\nk\3l\3l\3l\3l\3l\3l\3l\3l\3l")
        buf.write(u"\3l\5l\u0623\nl\3m\3m\5m\u0627\nm\3n\3n\3n\3n\3n\3n\7")
        buf.write(u"n\u062f\nn\fn\16n\u0632\13n\3o\3o\5o\u0636\no\3p\3p\3")
        buf.write(u"p\3p\5p\u063c\np\3p\3p\3p\7p\u0641\np\fp\16p\u0644\13")
        buf.write(u"p\3p\3p\5p\u0648\np\3q\3q\3q\7q\u064d\nq\fq\16q\u0650")
        buf.write(u"\13q\3r\3r\3r\7r\u0655\nr\fr\16r\u0658\13r\3s\3s\3s\3")
        buf.write(u"s\5s\u065e\ns\3t\3t\3u\3u\3u\3u\7u\u0666\nu\fu\16u\u0669")
        buf.write(u"\13u\3v\3v\3v\3v\3v\3v\3v\3v\3v\3v\5v\u0675\nv\3w\3w")
        buf.write(u"\5w\u0679\nw\3w\5w\u067c\nw\3x\3x\5x\u0680\nx\3x\5x\u0683")
        buf.write(u"\nx\3y\3y\3y\3y\7y\u0689\ny\fy\16y\u068c\13y\3z\3z\3")
        buf.write(u"z\3z\7z\u0692\nz\fz\16z\u0695\13z\3{\3{\3{\3{\7{\u069b")
        buf.write(u"\n{\f{\16{\u069e\13{\3|\3|\3|\3|\7|\u06a4\n|\f|\16|\u06a7")
        buf.write(u"\13|\3}\3}\3}\3}\3}\3}\3}\3}\3}\3}\3}\3}\3}\3}\5}\u06b7")
        buf.write(u"\n}\3~\3~\3~\3~\3~\3~\3~\3~\3~\3~\3~\3~\3~\3~\5~\u06c7")
        buf.write(u"\n~\3\177\3\177\3\177\7\177\u06cc\n\177\f\177\16\177")
        buf.write(u"\u06cf\13\177\3\u0080\3\u0080\3\u0080\3\u0080\5\u0080")
        buf.write(u"\u06d5\n\u0080\3\u0081\3\u0081\3\u0082\3\u0082\3\u0082")
        buf.write(u"\3\u0082\3\u0083\3\u0083\5\u0083\u06df\n\u0083\3\u0084")
        buf.write(u"\3\u0084\3\u0084\3\u0084\3\u0084\5\u0084\u06e6\n\u0084")
        buf.write(u"\3\u0085\5\u0085\u06e9\n\u0085\3\u0085\3\u0085\5\u0085")
        buf.write(u"\u06ed\n\u0085\3\u0085\3\u0085\3\u0086\5\u0086\u06f2")
        buf.write(u"\n\u0086\3\u0086\3\u0086\5\u0086\u06f6\n\u0086\3\u0086")
        buf.write(u"\3\u0086\3\u0087\3\u0087\3\u0087\3\u0087\3\u0087\7\u0087")
        buf.write(u"\u06ff\n\u0087\f\u0087\16\u0087\u0702\13\u0087\5\u0087")
        buf.write(u"\u0704\n\u0087\3\u0088\3\u0088\3\u0088\7\u0088\u0709")
        buf.write(u"\n\u0088\f\u0088\16\u0088\u070c\13\u0088\3\u0089\3\u0089")
        buf.write(u"\3\u0089\3\u0089\3\u008a\3\u008a\3\u008a\3\u008a\3\u008a")
        buf.write(u"\3\u008a\3\u008a\3\u008a\3\u008a\5\u008a\u071b\n\u008a")
        buf.write(u"\3\u008b\3\u008b\3\u008b\3\u008b\3\u008c\3\u008c\3\u008c")
        buf.write(u"\3\u008c\3\u008c\7\u008c\u0726\n\u008c\f\u008c\16\u008c")
        buf.write(u"\u0729\13\u008c\3\u008d\3\u008d\3\u008d\3\u008d\5\u008d")
        buf.write(u"\u072f\n\u008d\3\u008e\3\u008e\3\u008e\7\u008e\u0734")
        buf.write(u"\n\u008e\f\u008e\16\u008e\u0737\13\u008e\3\u008f\3\u008f")
        buf.write(u"\3\u008f\7\u008f\u073c\n\u008f\f\u008f\16\u008f\u073f")
        buf.write(u"\13\u008f\3\u008f\5\u008f\u0742\n\u008f\3\u0090\3\u0090")
        buf.write(u"\3\u0090\3\u0090\3\u0090\3\u0090\5\u0090\u074a\n\u0090")
        buf.write(u"\3\u0091\3\u0091\3\u0091\3\u0092\3\u0092\3\u0092\3\u0093")
        buf.write(u"\3\u0093\3\u0093\3\u0094\3\u0094\3\u0094\3\u0095\3\u0095")
        buf.write(u"\3\u0095\3\u0096\3\u0096\3\u0097\3\u0097\3\u0098\3\u0098")
        buf.write(u"\3\u0099\3\u0099\3\u009a\3\u009a\3\u009b\3\u009b\3\u009b")
        buf.write(u"\3\u009b\3\u009b\3\u009b\3\u009b\5\u009b\u076c\n\u009b")
        buf.write(u"\3\u009c\3\u009c\3\u009c\3\u009c\3\u009c\7\u009c\u0773")
        buf.write(u"\n\u009c\f\u009c\16\u009c\u0776\13\u009c\3\u009d\3\u009d")
        buf.write(u"\3\u009d\3\u009d\3\u009d\3\u009d\3\u009d\5\u009d\u077f")
        buf.write(u"\n\u009d\3\u009e\3\u009e\3\u009f\3\u009f\3\u009f\3\u00a0")
        buf.write(u"\3\u00a0\3\u00a0\3\u00a0\3\u00a0\5\u00a0\u078b\n\u00a0")
        buf.write(u"\3\u00a1\3\u00a1\3\u00a1\5\u00a1\u0790\n\u00a1\3\u00a1")
        buf.write(u"\3\u00a1\3\u00a2\3\u00a2\3\u00a2\3\u00a2\3\u00a2\3\u00a2")
        buf.write(u"\7\u00a2\u079a\n\u00a2\f\u00a2\16\u00a2\u079d\13\u00a2")
        buf.write(u"\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a4\3\u00a4\3\u00a4")
        buf.write(u"\3\u00a4\3\u00a5\3\u00a5\3\u00a6\3\u00a6\3\u00a6\3\u00a6")
        buf.write(u"\3\u00a6\5\u00a6\u07ae\n\u00a6\3\u00a7\3\u00a7\3\u00a8")
        buf.write(u"\3\u00a8\3\u00a8\5\u00a8\u07b5\n\u00a8\3\u00a9\3\u00a9")
        buf.write(u"\3\u00a9\3\u00a9\3\u00a9\7\u00a9\u07bc\n\u00a9\f\u00a9")
        buf.write(u"\16\u00a9\u07bf\13\u00a9\3\u00aa\3\u00aa\3\u00aa\3\u00aa")
        buf.write(u"\5\u00aa\u07c5\n\u00aa\3\u00ab\3\u00ab\3\u00ab\3\u00ab")
        buf.write(u"\3\u00ab\3\u00ab\5\u00ab\u07cd\n\u00ab\3\u00ac\3\u00ac")
        buf.write(u"\3\u00ac\5\u00ac\u07d2\n\u00ac\3\u00ac\3\u00ac\3\u00ad")
        buf.write(u"\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad\5\u00ad\u07dc")
        buf.write(u"\n\u00ad\3\u00ae\3\u00ae\3\u00ae\3\u00ae\3\u00ae\3\u00ae")
        buf.write(u"\7\u00ae\u07e4\n\u00ae\f\u00ae\16\u00ae\u07e7\13\u00ae")
        buf.write(u"\3\u00af\3\u00af\3\u00af\3\u00af\3\u00af\3\u00af\3\u00af")
        buf.write(u"\3\u00af\3\u00af\3\u00af\3\u00af\7\u00af\u07f4\n\u00af")
        buf.write(u"\f\u00af\16\u00af\u07f7\13\u00af\3\u00b0\3\u00b0\3\u00b0")
        buf.write(u"\3\u00b0\3\u00b1\3\u00b1\3\u00b1\5\u00b1\u0800\n\u00b1")
        buf.write(u"\3\u00b1\3\u00b1\3\u00b1\7\u00b1\u0805\n\u00b1\f\u00b1")
        buf.write(u"\16\u00b1\u0808\13\u00b1\3\u00b2\3\u00b2\3\u00b2\3\u00b2")
        buf.write(u"\3\u00b2\5\u00b2\u080f\n\u00b2\3\u00b3\3\u00b3\3\u00b4")
        buf.write(u"\3\u00b4\3\u00b4\3\u00b4\3\u00b4\3\u00b4\3\u00b4\5\u00b4")
        buf.write(u"\u081a\n\u00b4\3\u00b5\3\u00b5\3\u00b5\3\u00b5\3\u00b5")
        buf.write(u"\7\u00b5\u0821\n\u00b5\f\u00b5\16\u00b5\u0824\13\u00b5")
        buf.write(u"\3\u00b6\3\u00b6\3\u00b6\3\u00b6\3\u00b6\5\u00b6\u082b")
        buf.write(u"\n\u00b6\3\u00b7\3\u00b7\3\u00b8\3\u00b8\3\u00b8\3\u00b9")
        buf.write(u"\3\u00b9\3\u00b9\5\u00b9\u0835\n\u00b9\3\u00ba\3\u00ba")
        buf.write(u"\3\u00ba\5\u00ba\u083a\n\u00ba\3\u00ba\3\u00ba\3\u00bb")
        buf.write(u"\3\u00bb\3\u00bb\3\u00bb\3\u00bb\3\u00bb\7\u00bb\u0844")
        buf.write(u"\n\u00bb\f\u00bb\16\u00bb\u0847\13\u00bb\3\u00bc\3\u00bc")
        buf.write(u"\3\u00bc\3\u00bc\3\u00bd\3\u00bd\3\u00bd\3\u00bd\3\u00be")
        buf.write(u"\3\u00be\3\u00be\3\u00be\3\u00be\3\u00be\7\u00be\u0857")
        buf.write(u"\n\u00be\f\u00be\16\u00be\u085a\13\u00be\3\u00bf\3\u00bf")
        buf.write(u"\3\u00bf\3\u00bf\3\u00bf\7\u00bf\u0861\n\u00bf\f\u00bf")
        buf.write(u"\16\u00bf\u0864\13\u00bf\3\u00c0\3\u00c0\3\u00c0\3\u00c0")
        buf.write(u"\3\u00c0\5\u00c0\u086b\n\u00c0\3\u00c1\3\u00c1\3\u00c2")
        buf.write(u"\3\u00c2\3\u00c2\3\u00c2\3\u00c2\3\u00c2\3\u00c2\5\u00c2")
        buf.write(u"\u0876\n\u00c2\3\u00c3\3\u00c3\3\u00c3\3\u00c3\3\u00c3")
        buf.write(u"\7\u00c3\u087d\n\u00c3\f\u00c3\16\u00c3\u0880\13\u00c3")
        buf.write(u"\3\u00c4\3\u00c4\3\u00c4\3\u00c4\3\u00c4\5\u00c4\u0887")
        buf.write(u"\n\u00c4\3\u00c5\3\u00c5\3\u00c6\3\u00c6\3\u00c6\3\u00c7")
        buf.write(u"\3\u00c7\3\u00c7\5\u00c7\u0891\n\u00c7\3\u00c8\3\u00c8")
        buf.write(u"\3\u00c8\5\u00c8\u0896\n\u00c8\3\u00c8\3\u00c8\3\u00c9")
        buf.write(u"\3\u00c9\3\u00c9\3\u00c9\3\u00c9\3\u00c9\7\u00c9\u08a0")
        buf.write(u"\n\u00c9\f\u00c9\16\u00c9\u08a3\13\u00c9\3\u00ca\3\u00ca")
        buf.write(u"\3\u00ca\3\u00ca\3\u00cb\3\u00cb\3\u00cb\3\u00cb\3\u00cc")
        buf.write(u"\3\u00cc\3\u00cc\5\u00cc\u08b0\n\u00cc\3\u00cc\3\u00cc")
        buf.write(u"\3\u00cc\7\u00cc\u08b5\n\u00cc\f\u00cc\16\u00cc\u08b8")
        buf.write(u"\13\u00cc\3\u00cd\3\u00cd\3\u00cd\3\u00cd\3\u00cd\5\u00cd")
        buf.write(u"\u08bf\n\u00cd\3\u00ce\3\u00ce\3\u00ce\2\30$<P\\`l\u00a4")
        buf.write(u"\u00cc\u0116\u0136\u0142\u0150\u015a\u015c\u0160\u0168")
        buf.write(u"\u0174\u017a\u017c\u0184\u0190\u0196\u00cf\2\4\6\b\n")
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
        buf.write(u"\u0194\u0196\u0198\u019a\2\f\3\2TU\3\2\"#\4\2\u008f\u008f")
        buf.write(u"\u00a3\u00a3\4\2\u008b\u008b\u0093\u0093\4\2KK\\\\\4")
        buf.write(u"\2\'\'uu\b\2\64<\u0085\u0085\u0092\u0092\u009c\u009c")
        buf.write(u"\u00a1\u00a3\u00a5\u00a5\b\2\64<\u0085\u0085\u008b\u008b")
        buf.write(u"\u0092\u0093\u009c\u009c\u00a1\u00a3\7\2\64<\u0085\u0085")
        buf.write(u"\u0092\u0092\u009c\u009c\u00a1\u00a5\7\2\64<\u0085\u0085")
        buf.write(u"\u0092\u0092\u009c\u009c\u00a1\u00a3\u0939\2\u019c\3")
        buf.write(u"\2\2\2\4\u01ad\3\2\2\2\6\u01b7\3\2\2\2\b\u01bb\3\2\2")
        buf.write(u"\2\n\u01c3\3\2\2\2\f\u01df\3\2\2\2\16\u01e7\3\2\2\2\20")
        buf.write(u"\u01fd\3\2\2\2\22\u020a\3\2\2\2\24\u020c\3\2\2\2\26\u021b")
        buf.write(u"\3\2\2\2\30\u0225\3\2\2\2\32\u0232\3\2\2\2\34\u023c\3")
        buf.write(u"\2\2\2\36\u024a\3\2\2\2 \u025e\3\2\2\2\"\u0270\3\2\2")
        buf.write(u"\2$\u0278\3\2\2\2&\u0284\3\2\2\2(\u0290\3\2\2\2*\u02a0")
        buf.write(u"\3\2\2\2,\u02b3\3\2\2\2.\u02c6\3\2\2\2\60\u02c8\3\2\2")
        buf.write(u"\2\62\u02e8\3\2\2\2\64\u02ea\3\2\2\2\66\u0302\3\2\2\2")
        buf.write(u"8\u0304\3\2\2\2:\u0310\3\2\2\2<\u0312\3\2\2\2>\u0322")
        buf.write(u"\3\2\2\2@\u0324\3\2\2\2B\u032b\3\2\2\2D\u0332\3\2\2\2")
        buf.write(u"F\u0352\3\2\2\2H\u0354\3\2\2\2J\u0361\3\2\2\2L\u036a")
        buf.write(u"\3\2\2\2N\u0371\3\2\2\2P\u0385\3\2\2\2R\u039d\3\2\2\2")
        buf.write(u"T\u03a0\3\2\2\2V\u03d1\3\2\2\2X\u03d3\3\2\2\2Z\u03d5")
        buf.write(u"\3\2\2\2\\\u03eb\3\2\2\2^\u0456\3\2\2\2`\u0458\3\2\2")
        buf.write(u"\2b\u046a\3\2\2\2d\u0479\3\2\2\2f\u047b\3\2\2\2h\u0482")
        buf.write(u"\3\2\2\2j\u0489\3\2\2\2l\u0495\3\2\2\2n\u049f\3\2\2\2")
        buf.write(u"p\u04a3\3\2\2\2r\u04a7\3\2\2\2t\u04ac\3\2\2\2v\u04d1")
        buf.write(u"\3\2\2\2x\u04d3\3\2\2\2z\u04df\3\2\2\2|\u04eb\3\2\2\2")
        buf.write(u"~\u04ed\3\2\2\2\u0080\u04f4\3\2\2\2\u0082\u04f8\3\2\2")
        buf.write(u"\2\u0084\u04fd\3\2\2\2\u0086\u0506\3\2\2\2\u0088\u050b")
        buf.write(u"\3\2\2\2\u008a\u050e\3\2\2\2\u008c\u0513\3\2\2\2\u008e")
        buf.write(u"\u0521\3\2\2\2\u0090\u052b\3\2\2\2\u0092\u052f\3\2\2")
        buf.write(u"\2\u0094\u0531\3\2\2\2\u0096\u053a\3\2\2\2\u0098\u0543")
        buf.write(u"\3\2\2\2\u009a\u0555\3\2\2\2\u009c\u0558\3\2\2\2\u009e")
        buf.write(u"\u0561\3\2\2\2\u00a0\u0569\3\2\2\2\u00a2\u0571\3\2\2")
        buf.write(u"\2\u00a4\u0583\3\2\2\2\u00a6\u0594\3\2\2\2\u00a8\u05a4")
        buf.write(u"\3\2\2\2\u00aa\u05a6\3\2\2\2\u00ac\u05a9\3\2\2\2\u00ae")
        buf.write(u"\u05ad\3\2\2\2\u00b0\u05b2\3\2\2\2\u00b2\u05b4\3\2\2")
        buf.write(u"\2\u00b4\u05be\3\2\2\2\u00b6\u05c3\3\2\2\2\u00b8\u05c5")
        buf.write(u"\3\2\2\2\u00ba\u05c7\3\2\2\2\u00bc\u05c9\3\2\2\2\u00be")
        buf.write(u"\u05cb\3\2\2\2\u00c0\u05cd\3\2\2\2\u00c2\u05da\3\2\2")
        buf.write(u"\2\u00c4\u05de\3\2\2\2\u00c6\u05e0\3\2\2\2\u00c8\u05e5")
        buf.write(u"\3\2\2\2\u00ca\u05ea\3\2\2\2\u00cc\u05ec\3\2\2\2\u00ce")
        buf.write(u"\u05fa\3\2\2\2\u00d0\u0608\3\2\2\2\u00d2\u060a\3\2\2")
        buf.write(u"\2\u00d4\u0616\3\2\2\2\u00d6\u0622\3\2\2\2\u00d8\u0624")
        buf.write(u"\3\2\2\2\u00da\u0628\3\2\2\2\u00dc\u0633\3\2\2\2\u00de")
        buf.write(u"\u0637\3\2\2\2\u00e0\u0649\3\2\2\2\u00e2\u0651\3\2\2")
        buf.write(u"\2\u00e4\u065d\3\2\2\2\u00e6\u065f\3\2\2\2\u00e8\u0661")
        buf.write(u"\3\2\2\2\u00ea\u0674\3\2\2\2\u00ec\u0676\3\2\2\2\u00ee")
        buf.write(u"\u067d\3\2\2\2\u00f0\u0684\3\2\2\2\u00f2\u068d\3\2\2")
        buf.write(u"\2\u00f4\u0696\3\2\2\2\u00f6\u069f\3\2\2\2\u00f8\u06b6")
        buf.write(u"\3\2\2\2\u00fa\u06c6\3\2\2\2\u00fc\u06c8\3\2\2\2\u00fe")
        buf.write(u"\u06d4\3\2\2\2\u0100\u06d6\3\2\2\2\u0102\u06d8\3\2\2")
        buf.write(u"\2\u0104\u06de\3\2\2\2\u0106\u06e5\3\2\2\2\u0108\u06e8")
        buf.write(u"\3\2\2\2\u010a\u06f1\3\2\2\2\u010c\u06f9\3\2\2\2\u010e")
        buf.write(u"\u0705\3\2\2\2\u0110\u070d\3\2\2\2\u0112\u071a\3\2\2")
        buf.write(u"\2\u0114\u071c\3\2\2\2\u0116\u0720\3\2\2\2\u0118\u072e")
        buf.write(u"\3\2\2\2\u011a\u0730\3\2\2\2\u011c\u0738\3\2\2\2\u011e")
        buf.write(u"\u0749\3\2\2\2\u0120\u074b\3\2\2\2\u0122\u074e\3\2\2")
        buf.write(u"\2\u0124\u0751\3\2\2\2\u0126\u0754\3\2\2\2\u0128\u0757")
        buf.write(u"\3\2\2\2\u012a\u075a\3\2\2\2\u012c\u075c\3\2\2\2\u012e")
        buf.write(u"\u075e\3\2\2\2\u0130\u0760\3\2\2\2\u0132\u0762\3\2\2")
        buf.write(u"\2\u0134\u076b\3\2\2\2\u0136\u076d\3\2\2\2\u0138\u077e")
        buf.write(u"\3\2\2\2\u013a\u0780\3\2\2\2\u013c\u0782\3\2\2\2\u013e")
        buf.write(u"\u078a\3\2\2\2\u0140\u078c\3\2\2\2\u0142\u0793\3\2\2")
        buf.write(u"\2\u0144\u079e\3\2\2\2\u0146\u07a2\3\2\2\2\u0148\u07a6")
        buf.write(u"\3\2\2\2\u014a\u07ad\3\2\2\2\u014c\u07af\3\2\2\2\u014e")
        buf.write(u"\u07b4\3\2\2\2\u0150\u07b6\3\2\2\2\u0152\u07c4\3\2\2")
        buf.write(u"\2\u0154\u07cc\3\2\2\2\u0156\u07ce\3\2\2\2\u0158\u07db")
        buf.write(u"\3\2\2\2\u015a\u07dd\3\2\2\2\u015c\u07e8\3\2\2\2\u015e")
        buf.write(u"\u07f8\3\2\2\2\u0160\u07ff\3\2\2\2\u0162\u080e\3\2\2")
        buf.write(u"\2\u0164\u0810\3\2\2\2\u0166\u0819\3\2\2\2\u0168\u081b")
        buf.write(u"\3\2\2\2\u016a\u082a\3\2\2\2\u016c\u082c\3\2\2\2\u016e")
        buf.write(u"\u082e\3\2\2\2\u0170\u0834\3\2\2\2\u0172\u0836\3\2\2")
        buf.write(u"\2\u0174\u083d\3\2\2\2\u0176\u0848\3\2\2\2\u0178\u084c")
        buf.write(u"\3\2\2\2\u017a\u0850\3\2\2\2\u017c\u085b\3\2\2\2\u017e")
        buf.write(u"\u086a\3\2\2\2\u0180\u086c\3\2\2\2\u0182\u0875\3\2\2")
        buf.write(u"\2\u0184\u0877\3\2\2\2\u0186\u0886\3\2\2\2\u0188\u0888")
        buf.write(u"\3\2\2\2\u018a\u088a\3\2\2\2\u018c\u0890\3\2\2\2\u018e")
        buf.write(u"\u0892\3\2\2\2\u0190\u0899\3\2\2\2\u0192\u08a4\3\2\2")
        buf.write(u"\2\u0194\u08a8\3\2\2\2\u0196\u08af\3\2\2\2\u0198\u08be")
        buf.write(u"\3\2\2\2\u019a\u08c0\3\2\2\2\u019c\u019d\7a\2\2\u019d")
        buf.write(u"\u019e\5\u00bc_\2\u019e\u01a5\7\26\2\2\u019f\u01a2\5")
        buf.write(u"\u00bc_\2\u01a0\u01a1\7\23\2\2\u01a1\u01a3\5\u00e2r\2")
        buf.write(u"\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a6")
        buf.write(u"\3\2\2\2\u01a4\u01a6\5\u00e2r\2\u01a5\u019f\3\2\2\2\u01a5")
        buf.write(u"\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a8\7\27\2")
        buf.write(u"\2\u01a8\u01a9\7\21\2\2\u01a9\u01aa\5\u0084C\2\u01aa")
        buf.write(u"\u01ab\5\u0096L\2\u01ab\u01ac\5\u0086D\2\u01ac\3\3\2")
        buf.write(u"\2\2\u01ad\u01ae\7a\2\2\u01ae\u01af\5\u00bc_\2\u01af")
        buf.write(u"\u01b0\7\26\2\2\u01b0\u01b1\5\u00a8U\2\u01b1\u01b2\7")
        buf.write(u"\27\2\2\u01b2\u01b3\7\21\2\2\u01b3\u01b4\5\u0084C\2\u01b4")
        buf.write(u"\u01b5\5\u0094K\2\u01b5\u01b6\5\u0086D\2\u01b6\5\3\2")
        buf.write(u"\2\2\u01b7\u01b8\5\u00be`\2\u01b8\u01b9\7-\2\2\u01b9")
        buf.write(u"\u01ba\5\\/\2\u01ba\7\3\2\2\2\u01bb\u01bc\5\u00be`\2")
        buf.write(u"\u01bc\u01be\7\26\2\2\u01bd\u01bf\5l\67\2\u01be\u01bd")
        buf.write(u"\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0")
        buf.write(u"\u01c1\7\27\2\2\u01c1\t\3\2\2\2\u01c2\u01c4\7\u008f\2")
        buf.write(u"\2\u01c3\u01c2\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c5")
        buf.write(u"\3\2\2\2\u01c5\u01c6\7L\2\2\u01c6\u01c7\5\u00ba^\2\u01c7")
        buf.write(u"\u01c8\7\26\2\2\u01c8\u01c9\5\u00a4S\2\u01c9\u01ca\7")
        buf.write(u"\27\2\2\u01ca\u01cb\7\21\2\2\u01cb\u01db\5\u0084C\2\u01cc")
        buf.write(u"\u01dc\7\u0083\2\2\u01cd\u01d1\5\u009aN\2\u01ce\u01cf")
        buf.write(u"\5\u0082B\2\u01cf\u01d0\5\f\7\2\u01d0\u01d2\3\2\2\2\u01d1")
        buf.write(u"\u01ce\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01da\3\2\2")
        buf.write(u"\2\u01d3\u01d7\5\f\7\2\u01d4\u01d5\5\u0082B\2\u01d5\u01d6")
        buf.write(u"\5\u009aN\2\u01d6\u01d8\3\2\2\2\u01d7\u01d4\3\2\2\2\u01d7")
        buf.write(u"\u01d8\3\2\2\2\u01d8\u01da\3\2\2\2\u01d9\u01cd\3\2\2")
        buf.write(u"\2\u01d9\u01d3\3\2\2\2\u01da\u01dc\3\2\2\2\u01db\u01cc")
        buf.write(u"\3\2\2\2\u01db\u01d9\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd")
        buf.write(u"\u01de\5\u0086D\2\u01de\13\3\2\2\2\u01df\u01e0\7o\2\2")
        buf.write(u"\u01e0\u01e2\7\26\2\2\u01e1\u01e3\5\u00e0q\2\u01e2\u01e1")
        buf.write(u"\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4")
        buf.write(u"\u01e5\7\27\2\2\u01e5\r\3\2\2\2\u01e6\u01e8\7\u008f\2")
        buf.write(u"\2\u01e7\u01e6\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01e9")
        buf.write(u"\3\2\2\2\u01e9\u01ea\t\2\2\2\u01ea\u01eb\5\u00bc_\2\u01eb")
        buf.write(u"\u01f2\7\26\2\2\u01ec\u01f3\5\22\n\2\u01ed\u01f3\5\u00e2")
        buf.write(u"r\2\u01ee\u01ef\5\22\n\2\u01ef\u01f0\7\23\2\2\u01f0\u01f1")
        buf.write(u"\5\u00e2r\2\u01f1\u01f3\3\2\2\2\u01f2\u01ec\3\2\2\2\u01f2")
        buf.write(u"\u01ed\3\2\2\2\u01f2\u01ee\3\2\2\2\u01f3\u01f4\3\2\2")
        buf.write(u"\2\u01f4\u01f5\7\27\2\2\u01f5\u01f6\7\21\2\2\u01f6\u01f9")
        buf.write(u"\5\u0084C\2\u01f7\u01fa\5\u00ceh\2\u01f8\u01fa\7\u0083")
        buf.write(u"\2\2\u01f9\u01f7\3\2\2\2\u01f9\u01f8\3\2\2\2\u01fa\u01fb")
        buf.write(u"\3\2\2\2\u01fb\u01fc\5\u0086D\2\u01fc\17\3\2\2\2\u01fd")
        buf.write(u"\u01fe\7\u008d\2\2\u01fe\u01ff\5\u00bc_\2\u01ff\u0200")
        buf.write(u"\7\26\2\2\u0200\u0201\5\u00e2r\2\u0201\u0202\7\27\2\2")
        buf.write(u"\u0202\u0203\7\21\2\2\u0203\u0206\5\u0084C\2\u0204\u0207")
        buf.write(u"\5\u00ceh\2\u0205\u0207\7\u0083\2\2\u0206\u0204\3\2\2")
        buf.write(u"\2\u0206\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208\u0209")
        buf.write(u"\5\u0086D\2\u0209\21\3\2\2\2\u020a\u020b\5\u00b2Z\2\u020b")
        buf.write(u"\23\3\2\2\2\u020c\u020d\7X\2\2\u020d\u020e\7\177\2\2")
        buf.write(u"\u020e\u020f\5\u011e\u0090\2\u020f\u0210\7\26\2\2\u0210")
        buf.write(u"\u0211\5\u00c4c\2\u0211\u0214\7\27\2\2\u0212\u0213\7")
        buf.write(u"\63\2\2\u0213\u0215\5\u00a4S\2\u0214\u0212\3\2\2\2\u0214")
        buf.write(u"\u0215\3\2\2\2\u0215\u0216\3\2\2\2\u0216\u0217\7\21\2")
        buf.write(u"\2\u0217\u0218\5\u0084C\2\u0218\u0219\5\u00f0y\2\u0219")
        buf.write(u"\u021a\5\u0086D\2\u021a\25\3\2\2\2\u021b\u021c\7X\2\2")
        buf.write(u"\u021c\u021d\5\u00b8]\2\u021d\u021e\7\u008c\2\2\u021e")
        buf.write(u"\u021f\7\26\2\2\u021f\u0220\7\27\2\2\u0220\u0221\7\21")
        buf.write(u"\2\2\u0221\u0222\5\u0084C\2\u0222\u0223\5\u00f0y\2\u0223")
        buf.write(u"\u0224\5\u0086D\2\u0224\27\3\2\2\2\u0225\u0226\7X\2\2")
        buf.write(u"\u0226\u0228\5\u00b8]\2\u0227\u0229\7w\2\2\u0228\u0227")
        buf.write(u"\3\2\2\2\u0228\u0229\3\2\2\2\u0229\u022a\3\2\2\2\u022a")
        buf.write(u"\u022b\7\u008c\2\2\u022b\u022c\7\26\2\2\u022c\u022d\7")
        buf.write(u"\27\2\2\u022d\u022e\7\21\2\2\u022e\u022f\5\u0084C\2\u022f")
        buf.write(u"\u0230\5\u00e8u\2\u0230\u0231\5\u0086D\2\u0231\31\3\2")
        buf.write(u"\2\2\u0232\u0233\7X\2\2\u0233\u0234\5\u00b8]\2\u0234")
        buf.write(u"\u0235\7l\2\2\u0235\u0236\7\26\2\2\u0236\u0237\7\27\2")
        buf.write(u"\2\u0237\u0238\7\21\2\2\u0238\u0239\5\u0084C\2\u0239")
        buf.write(u"\u023a\5\u00f0y\2\u023a\u023b\5\u0086D\2\u023b\33\3\2")
        buf.write(u"\2\2\u023c\u023d\7X\2\2\u023d\u023f\5\u00b8]\2\u023e")
        buf.write(u"\u0240\7w\2\2\u023f\u023e\3\2\2\2\u023f\u0240\3\2\2\2")
        buf.write(u"\u0240\u0241\3\2\2\2\u0241\u0242\7l\2\2\u0242\u0243\7")
        buf.write(u"\26\2\2\u0243\u0244\7\27\2\2\u0244\u0245\7\21\2\2\u0245")
        buf.write(u"\u0246\5\u0084C\2\u0246\u0247\5\u00e8u\2\u0247\u0248")
        buf.write(u"\5\u0086D\2\u0248\35\3\2\2\2\u0249\u024b\7\u008f\2\2")
        buf.write(u"\u024a\u0249\3\2\2\2\u024a\u024b\3\2\2\2\u024b\u024c")
        buf.write(u"\3\2\2\2\u024c\u024d\7w\2\2\u024d\u024e\t\2\2\2\u024e")
        buf.write(u"\u024f\5\u00bc_\2\u024f\u0251\7\26\2\2\u0250\u0252\5")
        buf.write(u"\u00e2r\2\u0251\u0250\3\2\2\2\u0251\u0252\3\2\2\2\u0252")
        buf.write(u"\u0253\3\2\2\2\u0253\u0254\7\27\2\2\u0254\u0255\7\21")
        buf.write(u"\2\2\u0255\u0256\5\u0084C\2\u0256\u025a\5\"\22\2\u0257")
        buf.write(u"\u0258\5\u0082B\2\u0258\u0259\5\u00d2j\2\u0259\u025b")
        buf.write(u"\3\2\2\2\u025a\u0257\3\2\2\2\u025a\u025b\3\2\2\2\u025b")
        buf.write(u"\u025c\3\2\2\2\u025c\u025d\5\u0086D\2\u025d\37\3\2\2")
        buf.write(u"\2\u025e\u025f\7w\2\2\u025f\u0260\7\u0087\2\2\u0260\u0261")
        buf.write(u"\5\u00bc_\2\u0261\u0263\7\26\2\2\u0262\u0264\5\u00e2")
        buf.write(u"r\2\u0263\u0262\3\2\2\2\u0263\u0264\3\2\2\2\u0264\u0265")
        buf.write(u"\3\2\2\2\u0265\u0266\7\27\2\2\u0266\u0267\7\21\2\2\u0267")
        buf.write(u"\u0268\5\u0084C\2\u0268\u026c\5\"\22\2\u0269\u026a\5")
        buf.write(u"\u0082B\2\u026a\u026b\5\u00d2j\2\u026b\u026d\3\2\2\2")
        buf.write(u"\u026c\u0269\3\2\2\2\u026c\u026d\3\2\2\2\u026d\u026e")
        buf.write(u"\3\2\2\2\u026e\u026f\5\u0086D\2\u026f!\3\2\2\2\u0270")
        buf.write(u"\u0271\7X\2\2\u0271\u0272\t\2\2\2\u0272\u0273\7O\2\2")
        buf.write(u"\u0273\u0274\7\21\2\2\u0274\u0275\5\u0084C\2\u0275\u0276")
        buf.write(u"\5$\23\2\u0276\u0277\5\u0086D\2\u0277#\3\2\2\2\u0278")
        buf.write(u"\u0279\b\23\1\2\u0279\u027a\5\u00d6l\2\u027a\u0281\3")
        buf.write(u"\2\2\2\u027b\u027c\f\3\2\2\u027c\u027d\5\u0082B\2\u027d")
        buf.write(u"\u027e\5\u00d6l\2\u027e\u0280\3\2\2\2\u027f\u027b\3\2")
        buf.write(u"\2\2\u0280\u0283\3\2\2\2\u0281\u027f\3\2\2\2\u0281\u0282")
        buf.write(u"\3\2\2\2\u0282%\3\2\2\2\u0283\u0281\3\2\2\2\u0284\u0285")
        buf.write(u"\7E\2\2\u0285\u0286\7X\2\2\u0286\u0287\5\u00b4[\2\u0287")
        buf.write(u"\u0289\7\26\2\2\u0288\u028a\5\u00c0a\2\u0289\u0288\3")
        buf.write(u"\2\2\2\u0289\u028a\3\2\2\2\u028a\u028b\3\2\2\2\u028b")
        buf.write(u"\u028e\7\27\2\2\u028c\u028d\7\63\2\2\u028d\u028f\5\u00a4")
        buf.write(u"S\2\u028e\u028c\3\2\2\2\u028e\u028f\3\2\2\2\u028f\'\3")
        buf.write(u"\2\2\2\u0290\u0291\7X\2\2\u0291\u0292\5\u00b4[\2\u0292")
        buf.write(u"\u0294\7\26\2\2\u0293\u0295\5\u00c0a\2\u0294\u0293\3")
        buf.write(u"\2\2\2\u0294\u0295\3\2\2\2\u0295\u0296\3\2\2\2\u0296")
        buf.write(u"\u0299\7\27\2\2\u0297\u0298\7\63\2\2\u0298\u029a\5\u00a4")
        buf.write(u"S\2\u0299\u0297\3\2\2\2\u0299\u029a\3\2\2\2\u029a\u029b")
        buf.write(u"\3\2\2\2\u029b\u029c\7\21\2\2\u029c\u029d\5\u0084C\2")
        buf.write(u"\u029d\u029e\5\u00f0y\2\u029e\u029f\5\u0086D\2\u029f")
        buf.write(u")\3\2\2\2\u02a0\u02a2\7X\2\2\u02a1\u02a3\7w\2\2\u02a2")
        buf.write(u"\u02a1\3\2\2\2\u02a2\u02a3\3\2\2\2\u02a3\u02a4\3\2\2")
        buf.write(u"\2\u02a4\u02a5\5\u00b4[\2\u02a5\u02a7\7\26\2\2\u02a6")
        buf.write(u"\u02a8\5\u00c0a\2\u02a7\u02a6\3\2\2\2\u02a7\u02a8\3\2")
        buf.write(u"\2\2\u02a8\u02a9\3\2\2\2\u02a9\u02ac\7\27\2\2\u02aa\u02ab")
        buf.write(u"\7\63\2\2\u02ab\u02ad\5\u00caf\2\u02ac\u02aa\3\2\2\2")
        buf.write(u"\u02ac\u02ad\3\2\2\2\u02ad\u02ae\3\2\2\2\u02ae\u02af")
        buf.write(u"\7\21\2\2\u02af\u02b0\5\u0084C\2\u02b0\u02b1\5\u00e8")
        buf.write(u"u\2\u02b1\u02b2\5\u0086D\2\u02b2+\3\2\2\2\u02b3\u02b4")
        buf.write(u"\7X\2\2\u02b4\u02b5\7\u0092\2\2\u02b5\u02b6\7\u00a6\2")
        buf.write(u"\2\u02b6\u02b7\7\26\2\2\u02b7\u02b8\7\27\2\2\u02b8\u02b9")
        buf.write(u"\7\21\2\2\u02b9\u02ba\5\u0084C\2\u02ba\u02bb\5\u00f0")
        buf.write(u"y\2\u02bb\u02bc\5\u0086D\2\u02bc\u02bd\5\u0082B\2\u02bd")
        buf.write(u"\u02be\7\u0097\2\2\u02be\u02c4\7\21\2\2\u02bf\u02c0\5")
        buf.write(u"\u0084C\2\u02c0\u02c1\5\u00f2z\2\u02c1\u02c2\5\u0086")
        buf.write(u"D\2\u02c2\u02c5\3\2\2\2\u02c3\u02c5\5\u00be`\2\u02c4")
        buf.write(u"\u02bf\3\2\2\2\u02c4\u02c3\3\2\2\2\u02c5-\3\2\2\2\u02c6")
        buf.write(u"\u02c7\5\\/\2\u02c7/\3\2\2\2\u02c8\u02c9\5\u00b8]\2\u02c9")
        buf.write(u"\u02ca\7\21\2\2\u02ca\u02cf\5\u00caf\2\u02cb\u02cc\7")
        buf.write(u"\26\2\2\u02cc\u02cd\5\u00e2r\2\u02cd\u02ce\7\27\2\2\u02ce")
        buf.write(u"\u02d0\3\2\2\2\u02cf\u02cb\3\2\2\2\u02cf\u02d0\3\2\2")
        buf.write(u"\2\u02d0\u02d3\3\2\2\2\u02d1\u02d2\7-\2\2\u02d2\u02d4")
        buf.write(u"\5\u0104\u0083\2\u02d3\u02d1\3\2\2\2\u02d3\u02d4\3\2")
        buf.write(u"\2\2\u02d4\61\3\2\2\2\u02d5\u02e9\58\35\2\u02d6\u02e9")
        buf.write(u"\5z>\2\u02d7\u02e9\5~@\2\u02d8\u02e9\5\66\34\2\u02d9")
        buf.write(u"\u02e9\5\64\33\2\u02da\u02e9\5X-\2\u02db\u02e9\5Z.\2")
        buf.write(u"\u02dc\u02e9\5N(\2\u02dd\u02e9\5D#\2\u02de\u02e9\5H%")
        buf.write(u"\2\u02df\u02e9\5L\'\2\u02e0\u02e9\5J&\2\u02e1\u02e9\5")
        buf.write(u"R*\2\u02e2\u02e9\5T+\2\u02e3\u02e9\5r:\2\u02e4\u02e9")
        buf.write(u"\5@!\2\u02e5\u02e9\5B\"\2\u02e6\u02e9\5(\25\2\u02e7\u02e9")
        buf.write(u"\5\u00e6t\2\u02e8\u02d5\3\2\2\2\u02e8\u02d6\3\2\2\2\u02e8")
        buf.write(u"\u02d7\3\2\2\2\u02e8\u02d8\3\2\2\2\u02e8\u02d9\3\2\2")
        buf.write(u"\2\u02e8\u02da\3\2\2\2\u02e8\u02db\3\2\2\2\u02e8\u02dc")
        buf.write(u"\3\2\2\2\u02e8\u02dd\3\2\2\2\u02e8\u02de\3\2\2\2\u02e8")
        buf.write(u"\u02df\3\2\2\2\u02e8\u02e0\3\2\2\2\u02e8\u02e1\3\2\2")
        buf.write(u"\2\u02e8\u02e2\3\2\2\2\u02e8\u02e3\3\2\2\2\u02e8\u02e4")
        buf.write(u"\3\2\2\2\u02e8\u02e5\3\2\2\2\u02e8\u02e6\3\2\2\2\u02e8")
        buf.write(u"\u02e7\3\2\2\2\u02e9\63\3\2\2\2\u02ea\u02eb\7i\2\2\u02eb")
        buf.write(u"\u02ec\7\26\2\2\u02ec\u02ed\7\27\2\2\u02ed\65\3\2\2\2")
        buf.write(u"\u02ee\u02ef\7[\2\2\u02ef\u02f0\7\26\2\2\u02f0\u02f1")
        buf.write(u"\5\u00a0Q\2\u02f1\u02f2\7\27\2\2\u02f2\u0303\3\2\2\2")
        buf.write(u"\u02f3\u02f4\7\u0090\2\2\u02f4\u02f5\7\26\2\2\u02f5\u02f6")
        buf.write(u"\5\u00a0Q\2\u02f6\u02f7\7\27\2\2\u02f7\u0303\3\2\2\2")
        buf.write(u"\u02f8\u02f9\7[\2\2\u02f9\u02fa\7\26\2\2\u02fa\u02fb")
        buf.write(u"\5\u00a0Q\2\u02fb\u02fc\7\27\2\2\u02fc\u02fd\7H\2\2\u02fd")
        buf.write(u"\u02fe\7\u0090\2\2\u02fe\u02ff\7\26\2\2\u02ff\u0300\5")
        buf.write(u"\u00a0Q\2\u0300\u0301\7\27\2\2\u0301\u0303\3\2\2\2\u0302")
        buf.write(u"\u02ee\3\2\2\2\u0302\u02f3\3\2\2\2\u0302\u02f8\3\2\2")
        buf.write(u"\2\u0303\67\3\2\2\2\u0304\u0305\5:\36\2\u0305\u0307\7")
        buf.write(u"\26\2\2\u0306\u0308\5l\67\2\u0307\u0306\3\2\2\2\u0307")
        buf.write(u"\u0308\3\2\2\2\u0308\u0309\3\2\2\2\u0309\u030a\7\27\2")
        buf.write(u"\2\u030a9\3\2\2\2\u030b\u0311\5\u00b4[\2\u030c\u030d")
        buf.write(u"\5<\37\2\u030d\u030e\7\25\2\2\u030e\u030f\5\u00b4[\2")
        buf.write(u"\u030f\u0311\3\2\2\2\u0310\u030b\3\2\2\2\u0310\u030c")
        buf.write(u"\3\2\2\2\u0311;\3\2\2\2\u0312\u0313\b\37\1\2\u0313\u0314")
        buf.write(u"\5\u00b6\\\2\u0314\u0319\3\2\2\2\u0315\u0316\f\3\2\2")
        buf.write(u"\u0316\u0318\5> \2\u0317\u0315\3\2\2\2\u0318\u031b\3")
        buf.write(u"\2\2\2\u0319\u0317\3\2\2\2\u0319\u031a\3\2\2\2\u031a")
        buf.write(u"=\3\2\2\2\u031b\u0319\3\2\2\2\u031c\u031d\7\25\2\2\u031d")
        buf.write(u"\u0323\5\u00b8]\2\u031e\u031f\7\30\2\2\u031f\u0320\5")
        buf.write(u"\\/\2\u0320\u0321\7\31\2\2\u0321\u0323\3\2\2\2\u0322")
        buf.write(u"\u031c\3\2\2\2\u0322\u031e\3\2\2\2\u0323?\3\2\2\2\u0324")
        buf.write(u"\u0325\7\u0098\2\2\u0325\u0326\5\u0114\u008b\2\u0326")
        buf.write(u"\u0327\7\21\2\2\u0327\u0328\5\u0084C\2\u0328\u0329\5")
        buf.write(u"\u00f0y\2\u0329\u032a\5\u0086D\2\u032aA\3\2\2\2\u032b")
        buf.write(u"\u032c\7\u0098\2\2\u032c\u032d\5\u00bc_\2\u032d\u032e")
        buf.write(u"\7\21\2\2\u032e\u032f\5\u0084C\2\u032f\u0330\5\u00f0")
        buf.write(u"y\2\u0330\u0331\5\u0086D\2\u0331C\3\2\2\2\u0332\u0333")
        buf.write(u"\7\u0091\2\2\u0333\u0334\7|\2\2\u0334\u0335\5\\/\2\u0335")
        buf.write(u"\u0336\7\21\2\2\u0336\u0337\5\u0084C\2\u0337\u033f\5")
        buf.write(u"\u00f4{\2\u0338\u0339\5\u0082B\2\u0339\u033a\7\u0082")
        buf.write(u"\2\2\u033a\u033b\7\21\2\2\u033b\u033c\5\u0084C\2\u033c")
        buf.write(u"\u033d\5\u00f0y\2\u033d\u033e\5\u0086D\2\u033e\u0340")
        buf.write(u"\3\2\2\2\u033f\u0338\3\2\2\2\u033f\u0340\3\2\2\2\u0340")
        buf.write(u"\u0341\3\2\2\2\u0341\u0342\5\u0086D\2\u0342E\3\2\2\2")
        buf.write(u"\u0343\u0344\7\u0099\2\2\u0344\u0345\5\u00fa~\2\u0345")
        buf.write(u"\u0346\7\21\2\2\u0346\u0347\5\u0084C\2\u0347\u0348\5")
        buf.write(u"\u00f0y\2\u0348\u0349\5\u0086D\2\u0349\u0353\3\2\2\2")
        buf.write(u"\u034a\u034b\7\u0099\2\2\u034b\u034c\7n\2\2\u034c\u034d")
        buf.write(u"\5\u00f8}\2\u034d\u034e\7\21\2\2\u034e\u034f\5\u0084")
        buf.write(u"C\2\u034f\u0350\5\u00f0y\2\u0350\u0351\5\u0086D\2\u0351")
        buf.write(u"\u0353\3\2\2\2\u0352\u0343\3\2\2\2\u0352\u034a\3\2\2")
        buf.write(u"\2\u0353G\3\2\2\2\u0354\u0355\7j\2\2\u0355\u0358\5\u00b8")
        buf.write(u"]\2\u0356\u0357\7\23\2\2\u0357\u0359\5\u00b8]\2\u0358")
        buf.write(u"\u0356\3\2\2\2\u0358\u0359\3\2\2\2\u0359\u035a\3\2\2")
        buf.write(u"\2\u035a\u035b\7n\2\2\u035b\u035c\5\\/\2\u035c\u035d")
        buf.write(u"\7\21\2\2\u035d\u035e\5\u0084C\2\u035e\u035f\5\u00f0")
        buf.write(u"y\2\u035f\u0360\5\u0086D\2\u0360I\3\2\2\2\u0361\u0362")
        buf.write(u"\7]\2\2\u0362\u0363\7\21\2\2\u0363\u0364\5\u0084C\2\u0364")
        buf.write(u"\u0365\5\u00f0y\2\u0365\u0366\5\u0086D\2\u0366\u0367")
        buf.write(u"\5\u0082B\2\u0367\u0368\7\u009b\2\2\u0368\u0369\5\\/")
        buf.write(u"\2\u0369K\3\2\2\2\u036a\u036b\7\u009b\2\2\u036b\u036c")
        buf.write(u"\5\\/\2\u036c\u036d\7\21\2\2\u036d\u036e\5\u0084C\2\u036e")
        buf.write(u"\u036f\5\u00f0y\2\u036f\u0370\5\u0086D\2\u0370M\3\2\2")
        buf.write(u"\2\u0371\u0372\7m\2\2\u0372\u0373\5\\/\2\u0373\u0374")
        buf.write(u"\7\21\2\2\u0374\u0375\5\u0084C\2\u0375\u0376\5\u00f0")
        buf.write(u"y\2\u0376\u037a\5\u0086D\2\u0377\u0378\5\u0082B\2\u0378")
        buf.write(u"\u0379\5P)\2\u0379\u037b\3\2\2\2\u037a\u0377\3\2\2\2")
        buf.write(u"\u037a\u037b\3\2\2\2\u037b\u0383\3\2\2\2\u037c\u037d")
        buf.write(u"\5\u0082B\2\u037d\u037e\7`\2\2\u037e\u037f\7\21\2\2\u037f")
        buf.write(u"\u0380\5\u0084C\2\u0380\u0381\5\u00f0y\2\u0381\u0382")
        buf.write(u"\5\u0086D\2\u0382\u0384\3\2\2\2\u0383\u037c\3\2\2\2\u0383")
        buf.write(u"\u0384\3\2\2\2\u0384O\3\2\2\2\u0385\u0386\b)\1\2\u0386")
        buf.write(u"\u0387\7`\2\2\u0387\u0388\7m\2\2\u0388\u0389\5\\/\2\u0389")
        buf.write(u"\u038a\7\21\2\2\u038a\u038b\5\u0084C\2\u038b\u038c\5")
        buf.write(u"\u00f0y\2\u038c\u038d\5\u0086D\2\u038d\u039a\3\2\2\2")
        buf.write(u"\u038e\u038f\f\3\2\2\u038f\u0390\5\u0082B\2\u0390\u0391")
        buf.write(u"\7`\2\2\u0391\u0392\7m\2\2\u0392\u0393\5\\/\2\u0393\u0394")
        buf.write(u"\7\21\2\2\u0394\u0395\5\u0084C\2\u0395\u0396\5\u00f0")
        buf.write(u"y\2\u0396\u0397\5\u0086D\2\u0397\u0399\3\2\2\2\u0398")
        buf.write(u"\u038e\3\2\2\2\u0399\u039c\3\2\2\2\u039a\u0398\3\2\2")
        buf.write(u"\2\u039a\u039b\3\2\2\2\u039bQ\3\2\2\2\u039c\u039a\3\2")
        buf.write(u"\2\2\u039d\u039e\7\u0084\2\2\u039e\u039f\5\\/\2\u039f")
        buf.write(u"S\3\2\2\2\u03a0\u03a1\7\u0096\2\2\u03a1\u03a2\5\u00b8")
        buf.write(u"]\2\u03a2\u03a3\7\21\2\2\u03a3\u03a4\5\u0084C\2\u03a4")
        buf.write(u"\u03a5\5\u00f0y\2\u03a5\u03a6\5\u0086D\2\u03a6\u03a8")
        buf.write(u"\5\u0080A\2\u03a7\u03a9\5\u00f6|\2\u03a8\u03a7\3\2\2")
        buf.write(u"\2\u03a8\u03a9\3\2\2\2\u03a9\u03b1\3\2\2\2\u03aa\u03ab")
        buf.write(u"\7c\2\2\u03ab\u03ac\7\21\2\2\u03ac\u03ad\5\u0084C\2\u03ad")
        buf.write(u"\u03ae\5\u00f0y\2\u03ae\u03af\5\u0086D\2\u03af\u03b0")
        buf.write(u"\5\u0080A\2\u03b0\u03b2\3\2\2\2\u03b1\u03aa\3\2\2\2\u03b1")
        buf.write(u"\u03b2\3\2\2\2\u03b2\u03ba\3\2\2\2\u03b3\u03b4\7h\2\2")
        buf.write(u"\u03b4\u03b5\7\21\2\2\u03b5\u03b6\5\u0084C\2\u03b6\u03b7")
        buf.write(u"\5\u00f0y\2\u03b7\u03b8\5\u0086D\2\u03b8\u03b9\5\u0080")
        buf.write(u"A\2\u03b9\u03bb\3\2\2\2\u03ba\u03b3\3\2\2\2\u03ba\u03bb")
        buf.write(u"\3\2\2\2\u03bb\u03bc\3\2\2\2\u03bc\u03bd\5\u0080A\2\u03bd")
        buf.write(u"U\3\2\2\2\u03be\u03bf\7c\2\2\u03bf\u03c0\5\u00be`\2\u03c0")
        buf.write(u"\u03c1\7\21\2\2\u03c1\u03c2\5\u0084C\2\u03c2\u03c3\5")
        buf.write(u"\u00f0y\2\u03c3\u03c4\5\u0086D\2\u03c4\u03c5\5\u0080")
        buf.write(u"A\2\u03c5\u03d2\3\2\2\2\u03c6\u03c7\7c\2\2\u03c7\u03c8")
        buf.write(u"\7n\2\2\u03c8\u03c9\7\30\2\2\u03c9\u03ca\5\u0098M\2\u03ca")
        buf.write(u"\u03cb\7\31\2\2\u03cb\u03cc\7\21\2\2\u03cc\u03cd\5\u0084")
        buf.write(u"C\2\u03cd\u03ce\5\u00f0y\2\u03ce\u03cf\5\u0086D\2\u03cf")
        buf.write(u"\u03d0\5\u0080A\2\u03d0\u03d2\3\2\2\2\u03d1\u03be\3\2")
        buf.write(u"\2\2\u03d1\u03c6\3\2\2\2\u03d2W\3\2\2\2\u03d3\u03d4\7")
        buf.write(u"P\2\2\u03d4Y\3\2\2\2\u03d5\u03d7\7\u0088\2\2\u03d6\u03d8")
        buf.write(u"\5\\/\2\u03d7\u03d6\3\2\2\2\u03d7\u03d8\3\2\2\2\u03d8")
        buf.write(u"[\3\2\2\2\u03d9\u03da\b/\1\2\u03da\u03db\7#\2\2\u03db")
        buf.write(u"\u03ec\5\\/\"\u03dc\u03dd\7y\2\2\u03dd\u03ec\5\\/!\u03de")
        buf.write(u"\u03ec\5`\61\2\u03df\u03ec\5b\62\2\u03e0\u03e1\7>\2\2")
        buf.write(u"\u03e1\u03e2\7\26\2\2\u03e2\u03e3\5\\/\2\u03e3\u03e4")
        buf.write(u"\7\27\2\2\u03e4\u03ec\3\2\2\2\u03e5\u03e6\7d\2\2\u03e6")
        buf.write(u"\u03e7\7\26\2\2\u03e7\u03e8\5\u00b8]\2\u03e8\u03e9\7")
        buf.write(u"\27\2\2\u03e9\u03ec\3\2\2\2\u03ea\u03ec\5^\60\2\u03eb")
        buf.write(u"\u03d9\3\2\2\2\u03eb\u03dc\3\2\2\2\u03eb\u03de\3\2\2")
        buf.write(u"\2\u03eb\u03df\3\2\2\2\u03eb\u03e0\3\2\2\2\u03eb\u03e5")
        buf.write(u"\3\2\2\2\u03eb\u03ea\3\2\2\2\u03ec\u0453\3\2\2\2\u03ed")
        buf.write(u"\u03ee\f \2\2\u03ee\u03ef\5\u012c\u0097\2\u03ef\u03f0")
        buf.write(u"\5\\/!\u03f0\u0452\3\2\2\2\u03f1\u03f2\f\37\2\2\u03f2")
        buf.write(u"\u03f3\5\u012e\u0098\2\u03f3\u03f4\5\\/ \u03f4\u0452")
        buf.write(u"\3\2\2\2\u03f5\u03f6\f\36\2\2\u03f6\u03f7\5\u0132\u009a")
        buf.write(u"\2\u03f7\u03f8\5\\/\37\u03f8\u0452\3\2\2\2\u03f9\u03fa")
        buf.write(u"\f\35\2\2\u03fa\u03fb\5\u0130\u0099\2\u03fb\u03fc\5\\")
        buf.write(u"/\36\u03fc\u0452\3\2\2\2\u03fd\u03fe\f\34\2\2\u03fe\u03ff")
        buf.write(u"\t\3\2\2\u03ff\u0452\5\\/\35\u0400\u0401\f\33\2\2\u0401")
        buf.write(u"\u0402\7*\2\2\u0402\u0452\5\\/\34\u0403\u0404\f\32\2")
        buf.write(u"\2\u0404\u0405\7+\2\2\u0405\u0452\5\\/\33\u0406\u0407")
        buf.write(u"\f\31\2\2\u0407\u0408\7(\2\2\u0408\u0452\5\\/\32\u0409")
        buf.write(u"\u040a\f\30\2\2\u040a\u040b\7)\2\2\u040b\u0452\5\\/\31")
        buf.write(u"\u040c\u040d\f\25\2\2\u040d\u040e\7/\2\2\u040e\u0452")
        buf.write(u"\5\\/\26\u040f\u0410\f\24\2\2\u0410\u0411\7.\2\2\u0411")
        buf.write(u"\u0452\5\\/\25\u0412\u0413\f\23\2\2\u0413\u0414\7\60")
        buf.write(u"\2\2\u0414\u0452\5\\/\24\u0415\u0416\f\22\2\2\u0416\u0417")
        buf.write(u"\7\u0080\2\2\u0417\u0452\5\\/\23\u0418\u0419\f\21\2\2")
        buf.write(u"\u0419\u041a\7H\2\2\u041a\u0452\5\\/\22\u041b\u041c\f")
        buf.write(u"\20\2\2\u041c\u041d\7m\2\2\u041d\u041e\5\\/\2\u041e\u041f")
        buf.write(u"\7`\2\2\u041f\u0420\5\\/\21\u0420\u0452\3\2\2\2\u0421")
        buf.write(u"\u0422\f\16\2\2\u0422\u0423\7n\2\2\u0423\u0452\5\\/\17")
        buf.write(u"\u0424\u0425\f\r\2\2\u0425\u0426\7W\2\2\u0426\u0452\5")
        buf.write(u"\\/\16\u0427\u0428\f\f\2\2\u0428\u0429\7W\2\2\u0429\u042a")
        buf.write(u"\7F\2\2\u042a\u0452\5\\/\r\u042b\u042c\f\13\2\2\u042c")
        buf.write(u"\u042d\7W\2\2\u042d\u042e\7I\2\2\u042e\u0452\5\\/\f\u042f")
        buf.write(u"\u0430\f\n\2\2\u0430\u0431\7y\2\2\u0431\u0432\7n\2\2")
        buf.write(u"\u0432\u0452\5\\/\13\u0433\u0434\f\t\2\2\u0434\u0435")
        buf.write(u"\7y\2\2\u0435\u0436\7W\2\2\u0436\u0452\5\\/\n\u0437\u0438")
        buf.write(u"\f\b\2\2\u0438\u0439\7y\2\2\u0439\u043a\7W\2\2\u043a")
        buf.write(u"\u043b\7F\2\2\u043b\u0452\5\\/\t\u043c\u043d\f\7\2\2")
        buf.write(u"\u043d\u043e\7y\2\2\u043e\u043f\7W\2\2\u043f\u0440\7")
        buf.write(u"I\2\2\u0440\u0452\5\\/\b\u0441\u0442\f\3\2\2\u0442\u0443")
        buf.write(u"\7j\2\2\u0443\u0444\5\u00b8]\2\u0444\u0445\7n\2\2\u0445")
        buf.write(u"\u0446\5\\/\4\u0446\u0452\3\2\2\2\u0447\u0448\f\27\2")
        buf.write(u"\2\u0448\u0449\7q\2\2\u0449\u044a\7y\2\2\u044a\u0452")
        buf.write(u"\5\u0118\u008d\2\u044b\u044c\f\26\2\2\u044c\u044d\7q")
        buf.write(u"\2\2\u044d\u0452\5\u0118\u008d\2\u044e\u044f\f\17\2\2")
        buf.write(u"\u044f\u0450\7J\2\2\u0450\u0452\5\u00caf\2\u0451\u03ed")
        buf.write(u"\3\2\2\2\u0451\u03f1\3\2\2\2\u0451\u03f5\3\2\2\2\u0451")
        buf.write(u"\u03f9\3\2\2\2\u0451\u03fd\3\2\2\2\u0451\u0400\3\2\2")
        buf.write(u"\2\u0451\u0403\3\2\2\2\u0451\u0406\3\2\2\2\u0451\u0409")
        buf.write(u"\3\2\2\2\u0451\u040c\3\2\2\2\u0451\u040f\3\2\2\2\u0451")
        buf.write(u"\u0412\3\2\2\2\u0451\u0415\3\2\2\2\u0451\u0418\3\2\2")
        buf.write(u"\2\u0451\u041b\3\2\2\2\u0451\u0421\3\2\2\2\u0451\u0424")
        buf.write(u"\3\2\2\2\u0451\u0427\3\2\2\2\u0451\u042b\3\2\2\2\u0451")
        buf.write(u"\u042f\3\2\2\2\u0451\u0433\3\2\2\2\u0451\u0437\3\2\2")
        buf.write(u"\2\u0451\u043c\3\2\2\2\u0451\u0441\3\2\2\2\u0451\u0447")
        buf.write(u"\3\2\2\2\u0451\u044b\3\2\2\2\u0451\u044e\3\2\2\2\u0452")
        buf.write(u"\u0455\3\2\2\2\u0453\u0451\3\2\2\2\u0453\u0454\3\2\2")
        buf.write(u"\2\u0454]\3\2\2\2\u0455\u0453\3\2\2\2\u0456\u0457\5\u00bc")
        buf.write(u"_\2\u0457_\3\2\2\2\u0458\u0459\b\61\1\2\u0459\u045a\5")
        buf.write(u"\u00fe\u0080\2\u045a\u045f\3\2\2\2\u045b\u045c\f\3\2")
        buf.write(u"\2\u045c\u045e\5d\63\2\u045d\u045b\3\2\2\2\u045e\u0461")
        buf.write(u"\3\2\2\2\u045f\u045d\3\2\2\2\u045f\u0460\3\2\2\2\u0460")
        buf.write(u"a\3\2\2\2\u0461\u045f\3\2\2\2\u0462\u046b\5f\64\2\u0463")
        buf.write(u"\u046b\5h\65\2\u0464\u046b\5t;\2\u0465\u046b\5v<\2\u0466")
        buf.write(u"\u046b\5p9\2\u0467\u046b\5x=\2\u0468\u046b\58\35\2\u0469")
        buf.write(u"\u046b\5j\66\2\u046a\u0462\3\2\2\2\u046a\u0463\3\2\2")
        buf.write(u"\2\u046a\u0464\3\2\2\2\u046a\u0465\3\2\2\2\u046a\u0466")
        buf.write(u"\3\2\2\2\u046a\u0467\3\2\2\2\u046a\u0468\3\2\2\2\u046a")
        buf.write(u"\u0469\3\2\2\2\u046bc\3\2\2\2\u046c\u046d\6\63!\3\u046d")
        buf.write(u"\u046e\7\25\2\2\u046e\u047a\5\u00b8]\2\u046f\u0470\6")
        buf.write(u"\63\"\3\u0470\u0471\7\30\2\2\u0471\u0472\5\u0112\u008a")
        buf.write(u"\2\u0472\u0473\7\31\2\2\u0473\u047a\3\2\2\2\u0474\u0475")
        buf.write(u"\6\63#\3\u0475\u0476\7\30\2\2\u0476\u0477\5\\/\2\u0477")
        buf.write(u"\u0478\7\31\2\2\u0478\u047a\3\2\2\2\u0479\u046c\3\2\2")
        buf.write(u"\2\u0479\u046f\3\2\2\2\u0479\u0474\3\2\2\2\u047ae\3\2")
        buf.write(u"\2\2\u047b\u047c\7@\2\2\u047c\u047e\7\26\2\2\u047d\u047f")
        buf.write(u"\5\\/\2\u047e\u047d\3\2\2\2\u047e\u047f\3\2\2\2\u047f")
        buf.write(u"\u0480\3\2\2\2\u0480\u0481\7\27\2\2\u0481g\3\2\2\2\u0482")
        buf.write(u"\u0483\7?\2\2\u0483\u0485\7\26\2\2\u0484\u0486\5\\/\2")
        buf.write(u"\u0485\u0484\3\2\2\2\u0485\u0486\3\2\2\2\u0486\u0487")
        buf.write(u"\3\2\2\2\u0487\u0488\7\27\2\2\u0488i\3\2\2\2\u0489\u048a")
        buf.write(u"\5\u00acW\2\u048a\u048c\7\26\2\2\u048b\u048d\5l\67\2")
        buf.write(u"\u048c\u048b\3\2\2\2\u048c\u048d\3\2\2\2\u048d\u048e")
        buf.write(u"\3\2\2\2\u048e\u048f\7\27\2\2\u048fk\3\2\2\2\u0490\u0491")
        buf.write(u"\b\67\1\2\u0491\u0492\5\\/\2\u0492\u0493\6\67$\3\u0493")
        buf.write(u"\u0496\3\2\2\2\u0494\u0496\5n8\2\u0495\u0490\3\2\2\2")
        buf.write(u"\u0495\u0494\3\2\2\2\u0496\u049c\3\2\2\2\u0497\u0498")
        buf.write(u"\f\3\2\2\u0498\u0499\7\23\2\2\u0499\u049b\5n8\2\u049a")
        buf.write(u"\u0497\3\2\2\2\u049b\u049e\3\2\2\2\u049c\u049a\3\2\2")
        buf.write(u"\2\u049c\u049d\3\2\2\2\u049dm\3\2\2\2\u049e\u049c\3\2")
        buf.write(u"\2\2\u049f\u04a0\5\u00b8]\2\u04a0\u04a1\5\u012a\u0096")
        buf.write(u"\2\u04a1\u04a2\5\\/\2\u04a2o\3\2\2\2\u04a3\u04a4\7\u0085")
        buf.write(u"\2\2\u04a4\u04a5\7k\2\2\u04a5\u04a6\5\\/\2\u04a6q\3\2")
        buf.write(u"\2\2\u04a7\u04a8\7\u009c\2\2\u04a8\u04a9\5\\/\2\u04a9")
        buf.write(u"\u04aa\7\u0095\2\2\u04aa\u04ab\5\\/\2\u04abs\3\2\2\2")
        buf.write(u"\u04ac\u04ad\7g\2\2\u04ad\u04ae\5\u00b8]\2\u04ae\u04af")
        buf.write(u"\7k\2\2\u04af\u04b0\5\\/\2\u04b0\u04b1\7\u009a\2\2\u04b1")
        buf.write(u"\u04b2\5\\/\2\u04b2u\3\2\2\2\u04b3\u04b4\7g\2\2\u04b4")
        buf.write(u"\u04b6\7}\2\2\u04b5\u04b7\5\u00acW\2\u04b6\u04b5\3\2")
        buf.write(u"\2\2\u04b6\u04b7\3\2\2\2\u04b7\u04b8\3\2\2\2\u04b8\u04b9")
        buf.write(u"\7\u009a\2\2\u04b9\u04d2\5\\/\2\u04ba\u04c1\7g\2\2\u04bb")
        buf.write(u"\u04c2\7F\2\2\u04bc\u04bd\7\u008a\2\2\u04bd\u04be\5\\")
        buf.write(u"/\2\u04be\u04bf\7\u0095\2\2\u04bf\u04c0\5\\/\2\u04c0")
        buf.write(u"\u04c2\3\2\2\2\u04c1\u04bb\3\2\2\2\u04c1\u04bc\3\2\2")
        buf.write(u"\2\u04c2\u04c3\3\2\2\2\u04c3\u04c5\7\26\2\2\u04c4\u04c6")
        buf.write(u"\5\u00acW\2\u04c5\u04c4\3\2\2\2\u04c5\u04c6\3\2\2\2\u04c6")
        buf.write(u"\u04c7\3\2\2\2\u04c7\u04ca\7\27\2\2\u04c8\u04c9\7\u009a")
        buf.write(u"\2\2\u04c9\u04cb\5\\/\2\u04ca\u04c8\3\2\2\2\u04ca\u04cb")
        buf.write(u"\3\2\2\2\u04cb\u04cf\3\2\2\2\u04cc\u04cd\7\u0081\2\2")
        buf.write(u"\u04cd\u04ce\7Q\2\2\u04ce\u04d0\5\u011a\u008e\2\u04cf")
        buf.write(u"\u04cc\3\2\2\2\u04cf\u04d0\3\2\2\2\u04d0\u04d2\3\2\2")
        buf.write(u"\2\u04d1\u04b3\3\2\2\2\u04d1\u04ba\3\2\2\2\u04d2w\3\2")
        buf.write(u"\2\2\u04d3\u04d4\7\u008e\2\2\u04d4\u04d5\7\26\2\2\u04d5")
        buf.write(u"\u04db\5`\61\2\u04d6\u04d7\7\23\2\2\u04d7\u04d8\5\u0122")
        buf.write(u"\u0092\2\u04d8\u04d9\7-\2\2\u04d9\u04da\5`\61\2\u04da")
        buf.write(u"\u04dc\3\2\2\2\u04db\u04d6\3\2\2\2\u04db\u04dc\3\2\2")
        buf.write(u"\2\u04dc\u04dd\3\2\2\2\u04dd\u04de\7\27\2\2\u04dey\3")
        buf.write(u"\2\2\2\u04df\u04e0\5\u0116\u008c\2\u04e0\u04e1\5\u012a")
        buf.write(u"\u0096\2\u04e1\u04e2\5\\/\2\u04e2{\3\2\2\2\u04e3\u04e4")
        buf.write(u"\6?&\3\u04e4\u04e5\7\25\2\2\u04e5\u04ec\5\u00b8]\2\u04e6")
        buf.write(u"\u04e7\6?\'\3\u04e7\u04e8\7\30\2\2\u04e8\u04e9\5\\/\2")
        buf.write(u"\u04e9\u04ea\7\31\2\2\u04ea\u04ec\3\2\2\2\u04eb\u04e3")
        buf.write(u"\3\2\2\2\u04eb\u04e6\3\2\2\2\u04ec}\3\2\2\2\u04ed\u04ee")
        buf.write(u"\5\u00e0q\2\u04ee\u04ef\5\u012a\u0096\2\u04ef\u04f0\5")
        buf.write(u"\\/\2\u04f0\177\3\2\2\2\u04f1\u04f3\7\7\2\2\u04f2\u04f1")
        buf.write(u"\3\2\2\2\u04f3\u04f6\3\2\2\2\u04f4\u04f2\3\2\2\2\u04f4")
        buf.write(u"\u04f5\3\2\2\2\u04f5\u0081\3\2\2\2\u04f6\u04f4\3\2\2")
        buf.write(u"\2\u04f7\u04f9\7\7\2\2\u04f8\u04f7\3\2\2\2\u04f9\u04fa")
        buf.write(u"\3\2\2\2\u04fa\u04f8\3\2\2\2\u04fa\u04fb\3\2\2\2\u04fb")
        buf.write(u"\u0083\3\2\2\2\u04fc\u04fe\7\7\2\2\u04fd\u04fc\3\2\2")
        buf.write(u"\2\u04fe\u04ff\3\2\2\2\u04ff\u04fd\3\2\2\2\u04ff\u0500")
        buf.write(u"\3\2\2\2\u0500\u0501\3\2\2\2\u0501\u0502\7\3\2\2\u0502")
        buf.write(u"\u0085\3\2\2\2\u0503\u0505\7\7\2\2\u0504\u0503\3\2\2")
        buf.write(u"\2\u0505\u0508\3\2\2\2\u0506\u0504\3\2\2\2\u0506\u0507")
        buf.write(u"\3\2\2\2\u0507\u0509\3\2\2\2\u0508\u0506\3\2\2\2\u0509")
        buf.write(u"\u050a\7\4\2\2\u050a\u0087\3\2\2\2\u050b\u050c\7x\2\2")
        buf.write(u"\u050c\u0089\3\2\2\2\u050d\u050f\5\u008cG\2\u050e\u050d")
        buf.write(u"\3\2\2\2\u050e\u050f\3\2\2\2\u050f\u0510\3\2\2\2\u0510")
        buf.write(u"\u0511\5\u0080A\2\u0511\u0512\7\2\2\3\u0512\u008b\3\2")
        buf.write(u"\2\2\u0513\u0519\5\u008eH\2\u0514\u0515\5\u0082B\2\u0515")
        buf.write(u"\u0516\5\u008eH\2\u0516\u0518\3\2\2\2\u0517\u0514\3\2")
        buf.write(u"\2\2\u0518\u051b\3\2\2\2\u0519\u0517\3\2\2\2\u0519\u051a")
        buf.write(u"\3\2\2\2\u051a\u008d\3\2\2\2\u051b\u0519\3\2\2\2\u051c")
        buf.write(u"\u051d\5\u00e6t\2\u051d\u051e\5\u0082B\2\u051e\u0520")
        buf.write(u"\3\2\2\2\u051f\u051c\3\2\2\2\u0520\u0523\3\2\2\2\u0521")
        buf.write(u"\u051f\3\2\2\2\u0521\u0522\3\2\2\2\u0522\u0529\3\2\2")
        buf.write(u"\2\u0523\u0521\3\2\2\2\u0524\u052a\5\n\6\2\u0525\u052a")
        buf.write(u"\5\u00b0Y\2\u0526\u052a\5\u0090I\2\u0527\u052a\5\u0092")
        buf.write(u"J\2\u0528\u052a\5\u00e4s\2\u0529\u0524\3\2\2\2\u0529")
        buf.write(u"\u0525\3\2\2\2\u0529\u0526\3\2\2\2\u0529\u0527\3\2\2")
        buf.write(u"\2\u0529\u0528\3\2\2\2\u052a\u008f\3\2\2\2\u052b\u052c")
        buf.write(u"\5 \21\2\u052c\u0091\3\2\2\2\u052d\u0530\5\2\2\2\u052e")
        buf.write(u"\u0530\5\4\3\2\u052f\u052d\3\2\2\2\u052f\u052e\3\2\2")
        buf.write(u"\2\u0530\u0093\3\2\2\2\u0531\u0537\5\6\4\2\u0532\u0533")
        buf.write(u"\5\u0082B\2\u0533\u0534\5\6\4\2\u0534\u0536\3\2\2\2\u0535")
        buf.write(u"\u0532\3\2\2\2\u0536\u0539\3\2\2\2\u0537\u0535\3\2\2")
        buf.write(u"\2\u0537\u0538\3\2\2\2\u0538\u0095\3\2\2\2\u0539\u0537")
        buf.write(u"\3\2\2\2\u053a\u0540\5\b\5\2\u053b\u053c\5\u0082B\2\u053c")
        buf.write(u"\u053d\5\b\5\2\u053d\u053f\3\2\2\2\u053e\u053b\3\2\2")
        buf.write(u"\2\u053f\u0542\3\2\2\2\u0540\u053e\3\2\2\2\u0540\u0541")
        buf.write(u"\3\2\2\2\u0541\u0097\3\2\2\2\u0542\u0540\3\2\2\2\u0543")
        buf.write(u"\u0548\5\u00be`\2\u0544\u0545\7\23\2\2\u0545\u0547\5")
        buf.write(u"\u00be`\2\u0546\u0544\3\2\2\2\u0547\u054a\3\2\2\2\u0548")
        buf.write(u"\u0546\3\2\2\2\u0548\u0549\3\2\2\2\u0549\u0099\3\2\2")
        buf.write(u"\2\u054a\u0548\3\2\2\2\u054b\u054c\7n\2\2\u054c\u0556")
        buf.write(u"\5\u009cO\2\u054d\u054e\7n\2\2\u054e\u0556\5\u009eP\2")
        buf.write(u"\u054f\u0550\7n\2\2\u0550\u0556\5\u00a2R\2\u0551\u0552")
        buf.write(u"\7r\2\2\u0552\u0556\7\u00a6\2\2\u0553\u0554\7r\2\2\u0554")
        buf.write(u"\u0556\5\\/\2\u0555\u054b\3\2\2\2\u0555\u054d\3\2\2\2")
        buf.write(u"\u0555\u054f\3\2\2\2\u0555\u0551\3\2\2\2\u0555\u0553")
        buf.write(u"\3\2\2\2\u0556\u009b\3\2\2\2\u0557\u0559\7v\2\2\u0558")
        buf.write(u"\u0557\3\2\2\2\u0558\u0559\3\2\2\2\u0559\u055a\3\2\2")
        buf.write(u"\2\u055a\u055c\7\30\2\2\u055b\u055d\5\u00a0Q\2\u055c")
        buf.write(u"\u055b\3\2\2\2\u055c\u055d\3\2\2\2\u055d\u055e\3\2\2")
        buf.write(u"\2\u055e\u055f\7\31\2\2\u055f\u009d\3\2\2\2\u0560\u0562")
        buf.write(u"\7v\2\2\u0561\u0560\3\2\2\2\u0561\u0562\3\2\2\2\u0562")
        buf.write(u"\u0563\3\2\2\2\u0563\u0565\7*\2\2\u0564\u0566\5\u00a0")
        buf.write(u"Q\2\u0565\u0564\3\2\2\2\u0565\u0566\3\2\2\2\u0566\u0567")
        buf.write(u"\3\2\2\2\u0567\u0568\7(\2\2\u0568\u009f\3\2\2\2\u0569")
        buf.write(u"\u056e\5\\/\2\u056a\u056b\7\23\2\2\u056b\u056d\5\\/\2")
        buf.write(u"\u056c\u056a\3\2\2\2\u056d\u0570\3\2\2\2\u056e\u056c")
        buf.write(u"\3\2\2\2\u056e\u056f\3\2\2\2\u056f\u00a1\3\2\2\2\u0570")
        buf.write(u"\u056e\3\2\2\2\u0571\u0572\7\30\2\2\u0572\u0573\5\\/")
        buf.write(u"\2\u0573\u0574\7\24\2\2\u0574\u0575\5\\/\2\u0575\u0576")
        buf.write(u"\7\31\2\2\u0576\u00a3\3\2\2\2\u0577\u0578\bS\1\2\u0578")
        buf.write(u"\u0584\5\u00a6T\2\u0579\u057a\7D\2\2\u057a\u057b\7*\2")
        buf.write(u"\2\u057b\u057c\5\u00a4S\2\u057c\u057d\7(\2\2\u057d\u0584")
        buf.write(u"\3\2\2\2\u057e\u057f\7C\2\2\u057f\u0580\7*\2\2\u0580")
        buf.write(u"\u0581\5\u00a4S\2\u0581\u0582\7(\2\2\u0582\u0584\3\2")
        buf.write(u"\2\2\u0583\u0577\3\2\2\2\u0583\u0579\3\2\2\2\u0583\u057e")
        buf.write(u"\3\2\2\2\u0584\u058f\3\2\2\2\u0585\u0586\f\7\2\2\u0586")
        buf.write(u"\u058e\7,\2\2\u0587\u0588\f\6\2\2\u0588\u0589\7\30\2")
        buf.write(u"\2\u0589\u058e\7\31\2\2\u058a\u058b\f\5\2\2\u058b\u058c")
        buf.write(u"\7\32\2\2\u058c\u058e\7\33\2\2\u058d\u0585\3\2\2\2\u058d")
        buf.write(u"\u0587\3\2\2\2\u058d\u058a\3\2\2\2\u058e\u0591\3\2\2")
        buf.write(u"\2\u058f\u058d\3\2\2\2\u058f\u0590\3\2\2\2\u0590\u00a5")
        buf.write(u"\3\2\2\2\u0591\u058f\3\2\2\2\u0592\u0595\5\u00a8U\2\u0593")
        buf.write(u"\u0595\5\u00aaV\2\u0594\u0592\3\2\2\2\u0594\u0593\3\2")
        buf.write(u"\2\2\u0595\u00a7\3\2\2\2\u0596\u05a5\7\64\2\2\u0597\u05a5")
        buf.write(u"\7\65\2\2\u0598\u05a5\7\66\2\2\u0599\u05a5\7A\2\2\u059a")
        buf.write(u"\u05a5\7\67\2\2\u059b\u05a5\78\2\2\u059c\u05a5\7?\2\2")
        buf.write(u"\u059d\u05a5\79\2\2\u059e\u05a5\7;\2\2\u059f\u05a5\7")
        buf.write(u":\2\2\u05a0\u05a5\7<\2\2\u05a1\u05a5\7>\2\2\u05a2\u05a5")
        buf.write(u"\7@\2\2\u05a3\u05a5\7B\2\2\u05a4\u0596\3\2\2\2\u05a4")
        buf.write(u"\u0597\3\2\2\2\u05a4\u0598\3\2\2\2\u05a4\u0599\3\2\2")
        buf.write(u"\2\u05a4\u059a\3\2\2\2\u05a4\u059b\3\2\2\2\u05a4\u059c")
        buf.write(u"\3\2\2\2\u05a4\u059d\3\2\2\2\u05a4\u059e\3\2\2\2\u05a4")
        buf.write(u"\u059f\3\2\2\2\u05a4\u05a0\3\2\2\2\u05a4\u05a1\3\2\2")
        buf.write(u"\2\u05a4\u05a2\3\2\2\2\u05a4\u05a3\3\2\2\2\u05a5\u00a9")
        buf.write(u"\3\2\2\2\u05a6\u05a7\7\u00a2\2\2\u05a7\u00ab\3\2\2\2")
        buf.write(u"\u05a8\u05aa\7v\2\2\u05a9\u05a8\3\2\2\2\u05a9\u05aa\3")
        buf.write(u"\2\2\2\u05aa\u05ab\3\2\2\2\u05ab\u05ac\5\u00aaV\2\u05ac")
        buf.write(u"\u00ad\3\2\2\2\u05ad\u05ae\7>\2\2\u05ae\u00af\3\2\2\2")
        buf.write(u"\u05af\u05b3\5\16\b\2\u05b0\u05b3\5\36\20\2\u05b1\u05b3")
        buf.write(u"\5\20\t\2\u05b2\u05af\3\2\2\2\u05b2\u05b0\3\2\2\2\u05b2")
        buf.write(u"\u05b1\3\2\2\2\u05b3\u00b1\3\2\2\2\u05b4\u05b9\5\u00bc")
        buf.write(u"_\2\u05b5\u05b6\7\23\2\2\u05b6\u05b8\5\u00bc_\2\u05b7")
        buf.write(u"\u05b5\3\2\2\2\u05b8\u05bb\3\2\2\2\u05b9\u05b7\3\2\2")
        buf.write(u"\2\u05b9\u05ba\3\2\2\2\u05ba\u00b3\3\2\2\2\u05bb\u05b9")
        buf.write(u"\3\2\2\2\u05bc\u05bf\5\u00b8]\2\u05bd\u05bf\5\u00bc_")
        buf.write(u"\2\u05be\u05bc\3\2\2\2\u05be\u05bd\3\2\2\2\u05bf\u00b5")
        buf.write(u"\3\2\2\2\u05c0\u05c4\5\u00b8]\2\u05c1\u05c4\5\u00bc_")
        buf.write(u"\2\u05c2\u05c4\5\u00be`\2\u05c3\u05c0\3\2\2\2\u05c3\u05c1")
        buf.write(u"\3\2\2\2\u05c3\u05c2\3\2\2\2\u05c4\u00b7\3\2\2\2\u05c5")
        buf.write(u"\u05c6\7\u00a3\2\2\u05c6\u00b9\3\2\2\2\u05c7\u05c8\t")
        buf.write(u"\4\2\2\u05c8\u00bb\3\2\2\2\u05c9\u05ca\7\u00a2\2\2\u05ca")
        buf.write(u"\u00bd\3\2\2\2\u05cb\u05cc\7\u00a1\2\2\u05cc\u00bf\3")
        buf.write(u"\2\2\2\u05cd\u05d2\5\u00c2b\2\u05ce\u05cf\7\23\2\2\u05cf")
        buf.write(u"\u05d1\5\u00c2b\2\u05d0\u05ce\3\2\2\2\u05d1\u05d4\3\2")
        buf.write(u"\2\2\u05d2\u05d0\3\2\2\2\u05d2\u05d3\3\2\2\2\u05d3\u00c1")
        buf.write(u"\3\2\2\2\u05d4\u05d2\3\2\2\2\u05d5\u05db\5\u00c8e\2\u05d6")
        buf.write(u"\u05d8\7v\2\2\u05d7\u05d6\3\2\2\2\u05d7\u05d8\3\2\2\2")
        buf.write(u"\u05d8\u05d9\3\2\2\2\u05d9\u05db\5\u00c4c\2\u05da\u05d5")
        buf.write(u"\3\2\2\2\u05da\u05d7\3\2\2\2\u05db\u00c3\3\2\2\2\u05dc")
        buf.write(u"\u05df\5\u00c6d\2\u05dd\u05df\5\60\31\2\u05de\u05dc\3")
        buf.write(u"\2\2\2\u05de\u05dd\3\2\2\2\u05df\u00c5\3\2\2\2\u05e0")
        buf.write(u"\u05e3\5\u00b8]\2\u05e1\u05e2\7-\2\2\u05e2\u05e4\5\u0104")
        buf.write(u"\u0083\2\u05e3\u05e1\3\2\2\2\u05e3\u05e4\3\2\2\2\u05e4")
        buf.write(u"\u00c7\3\2\2\2\u05e5\u05e6\5\u00aeX\2\u05e6\u05e7\5\u00b8")
        buf.write(u"]\2\u05e7\u00c9\3\2\2\2\u05e8\u05eb\5\u00a4S\2\u05e9")
        buf.write(u"\u05eb\5\u00ccg\2\u05ea\u05e8\3\2\2\2\u05ea\u05e9\3\2")
        buf.write(u"\2\2\u05eb\u00cb\3\2\2\2\u05ec\u05ed\bg\1\2\u05ed\u05ee")
        buf.write(u"\7I\2\2\u05ee\u05f7\3\2\2\2\u05ef\u05f0\f\4\2\2\u05f0")
        buf.write(u"\u05f1\7\30\2\2\u05f1\u05f6\7\31\2\2\u05f2\u05f3\f\3")
        buf.write(u"\2\2\u05f3\u05f4\7\32\2\2\u05f4\u05f6\7\33\2\2\u05f5")
        buf.write(u"\u05ef\3\2\2\2\u05f5\u05f2\3\2\2\2\u05f6\u05f9\3\2\2")
        buf.write(u"\2\u05f7\u05f5\3\2\2\2\u05f7\u05f8\3\2\2\2\u05f8\u00cd")
        buf.write(u"\3\2\2\2\u05f9\u05f7\3\2\2\2\u05fa\u0600\5\u00d0i\2\u05fb")
        buf.write(u"\u05fc\5\u0082B\2\u05fc\u05fd\5\u00d0i\2\u05fd\u05ff")
        buf.write(u"\3\2\2\2\u05fe\u05fb\3\2\2\2\u05ff\u0602\3\2\2\2\u0600")
        buf.write(u"\u05fe\3\2\2\2\u0600\u0601\3\2\2\2\u0601\u00cf\3\2\2")
        buf.write(u"\2\u0602\u0600\3\2\2\2\u0603\u0609\5\26\f\2\u0604\u0609")
        buf.write(u"\5\32\16\2\u0605\u0609\5(\25\2\u0606\u0609\5&\24\2\u0607")
        buf.write(u"\u0609\5\24\13\2\u0608\u0603\3\2\2\2\u0608\u0604\3\2")
        buf.write(u"\2\2\u0608\u0605\3\2\2\2\u0608\u0606\3\2\2\2\u0608\u0607")
        buf.write(u"\3\2\2\2\u0609\u00d1\3\2\2\2\u060a\u0610\5\u00d4k\2\u060b")
        buf.write(u"\u060c\5\u0082B\2\u060c\u060d\5\u00d4k\2\u060d\u060f")
        buf.write(u"\3\2\2\2\u060e\u060b\3\2\2\2\u060f\u0612\3\2\2\2\u0610")
        buf.write(u"\u060e\3\2\2\2\u0610\u0611\3\2\2\2\u0611\u00d3\3\2\2")
        buf.write(u"\2\u0612\u0610\3\2\2\2\u0613\u0617\5\34\17\2\u0614\u0617")
        buf.write(u"\5\30\r\2\u0615\u0617\5*\26\2\u0616\u0613\3\2\2\2\u0616")
        buf.write(u"\u0614\3\2\2\2\u0616\u0615\3\2\2\2\u0617\u00d5\3\2\2")
        buf.write(u"\2\u0618\u0619\7\13\2\2\u0619\u0623\5\u017c\u00bf\2\u061a")
        buf.write(u"\u061b\7\f\2\2\u061b\u0623\5\u0196\u00cc\2\u061c\u061d")
        buf.write(u"\7\r\2\2\u061d\u0623\5\u00d8m\2\u061e\u061f\7\16\2\2")
        buf.write(u"\u061f\u0623\5\u00d8m\2\u0620\u0621\7\17\2\2\u0621\u0623")
        buf.write(u"\5\u00dco\2\u0622\u0618\3\2\2\2\u0622\u061a\3\2\2\2\u0622")
        buf.write(u"\u061c\3\2\2\2\u0622\u061e\3\2\2\2\u0622\u0620\3\2\2")
        buf.write(u"\2\u0623\u00d7\3\2\2\2\u0624\u0626\5\u00b6\\\2\u0625")
        buf.write(u"\u0627\5\u00dan\2\u0626\u0625\3\2\2\2\u0626\u0627\3\2")
        buf.write(u"\2\2\u0627\u00d9\3\2\2\2\u0628\u0629\7k\2\2\u0629\u062a")
        buf.write(u"\5\u0124\u0093\2\u062a\u062b\7\21\2\2\u062b\u0630\5\u00b6")
        buf.write(u"\\\2\u062c\u062d\7\25\2\2\u062d\u062f\5\u00b6\\\2\u062e")
        buf.write(u"\u062c\3\2\2\2\u062f\u0632\3\2\2\2\u0630\u062e\3\2\2")
        buf.write(u"\2\u0630\u0631\3\2\2\2\u0631\u00db\3\2\2\2\u0632\u0630")
        buf.write(u"\3\2\2\2\u0633\u0635\5\u00b6\\\2\u0634\u0636\5\u00de")
        buf.write(u"p\2\u0635\u0634\3\2\2\2\u0635\u0636\3\2\2\2\u0636\u00dd")
        buf.write(u"\3\2\2\2\u0637\u0638\7k\2\2\u0638\u0639\5\u0124\u0093")
        buf.write(u"\2\u0639\u063b\7\21\2\2\u063a\u063c\7%\2\2\u063b\u063a")
        buf.write(u"\3\2\2\2\u063b\u063c\3\2\2\2\u063c\u063d\3\2\2\2\u063d")
        buf.write(u"\u0642\5\u014c\u00a7\2\u063e\u063f\7%\2\2\u063f\u0641")
        buf.write(u"\5\u014c\u00a7\2\u0640\u063e\3\2\2\2\u0641\u0644\3\2")
        buf.write(u"\2\2\u0642\u0640\3\2\2\2\u0642\u0643\3\2\2\2\u0643\u0647")
        buf.write(u"\3\2\2\2\u0644\u0642\3\2\2\2\u0645\u0646\7\25\2\2\u0646")
        buf.write(u"\u0648\5\u014c\u00a7\2\u0647\u0645\3\2\2\2\u0647\u0648")
        buf.write(u"\3\2\2\2\u0648\u00df\3\2\2\2\u0649\u064e\5\u00b8]\2\u064a")
        buf.write(u"\u064b\7\23\2\2\u064b\u064d\5\u00b8]\2\u064c\u064a\3")
        buf.write(u"\2\2\2\u064d\u0650\3\2\2\2\u064e\u064c\3\2\2\2\u064e")
        buf.write(u"\u064f\3\2\2\2\u064f\u00e1\3\2\2\2\u0650\u064e\3\2\2")
        buf.write(u"\2\u0651\u0656\5\u00ba^\2\u0652\u0653\7\23\2\2\u0653")
        buf.write(u"\u0655\5\u00ba^\2\u0654\u0652\3\2\2\2\u0655\u0658\3\2")
        buf.write(u"\2\2\u0656\u0654\3\2\2\2\u0656\u0657\3\2\2\2\u0657\u00e3")
        buf.write(u"\3\2\2\2\u0658\u0656\3\2\2\2\u0659\u065e\5&\24\2\u065a")
        buf.write(u"\u065e\5(\25\2\u065b\u065e\5*\26\2\u065c\u065e\5,\27")
        buf.write(u"\2\u065d\u0659\3\2\2\2\u065d\u065a\3\2\2\2\u065d\u065b")
        buf.write(u"\3\2\2\2\u065d\u065c\3\2\2\2\u065e\u00e5\3\2\2\2\u065f")
        buf.write(u"\u0660\7\n\2\2\u0660\u00e7\3\2\2\2\u0661\u0667\5\u00ea")
        buf.write(u"v\2\u0662\u0663\5\u0082B\2\u0663\u0664\5\u00eav\2\u0664")
        buf.write(u"\u0666\3\2\2\2\u0665\u0662\3\2\2\2\u0666\u0669\3\2\2")
        buf.write(u"\2\u0667\u0665\3\2\2\2\u0667\u0668\3\2\2\2\u0668\u00e9")
        buf.write(u"\3\2\2\2\u0669\u0667\3\2\2\2\u066a\u066b\7\13\2\2\u066b")
        buf.write(u"\u0675\5\u0166\u00b4\2\u066c\u066d\7\f\2\2\u066d\u0675")
        buf.write(u"\5\u0182\u00c2\2\u066e\u066f\7\r\2\2\u066f\u0675\5\u00ec")
        buf.write(u"w\2\u0670\u0671\7\16\2\2\u0671\u0675\5\u00ecw\2\u0672")
        buf.write(u"\u0673\7\17\2\2\u0673\u0675\5\u00eex\2\u0674\u066a\3")
        buf.write(u"\2\2\2\u0674\u066c\3\2\2\2\u0674\u066e\3\2\2\2\u0674")
        buf.write(u"\u0670\3\2\2\2\u0674\u0672\3\2\2\2\u0675\u00eb\3\2\2")
        buf.write(u"\2\u0676\u0678\5\u014e\u00a8\2\u0677\u0679\7\22\2\2\u0678")
        buf.write(u"\u0677\3\2\2\2\u0678\u0679\3\2\2\2\u0679\u067b\3\2\2")
        buf.write(u"\2\u067a\u067c\5\u00dan\2\u067b\u067a\3\2\2\2\u067b\u067c")
        buf.write(u"\3\2\2\2\u067c\u00ed\3\2\2\2\u067d\u067f\5\u0134\u009b")
        buf.write(u"\2\u067e\u0680\7\22\2\2\u067f\u067e\3\2\2\2\u067f\u0680")
        buf.write(u"\3\2\2\2\u0680\u0682\3\2\2\2\u0681\u0683\5\u00dep\2\u0682")
        buf.write(u"\u0681\3\2\2\2\u0682\u0683\3\2\2\2\u0683\u00ef\3\2\2")
        buf.write(u"\2\u0684\u068a\5\62\32\2\u0685\u0686\5\u0082B\2\u0686")
        buf.write(u"\u0687\5\62\32\2\u0687\u0689\3\2\2\2\u0688\u0685\3\2")
        buf.write(u"\2\2\u0689\u068c\3\2\2\2\u068a\u0688\3\2\2\2\u068a\u068b")
        buf.write(u"\3\2\2\2\u068b\u00f1\3\2\2\2\u068c\u068a\3\2\2\2\u068d")
        buf.write(u"\u0693\5.\30\2\u068e\u068f\5\u0082B\2\u068f\u0690\5.")
        buf.write(u"\30\2\u0690\u0692\3\2\2\2\u0691\u068e\3\2\2\2\u0692\u0695")
        buf.write(u"\3\2\2\2\u0693\u0691\3\2\2\2\u0693\u0694\3\2\2\2\u0694")
        buf.write(u"\u00f3\3\2\2\2\u0695\u0693\3\2\2\2\u0696\u069c\5F$\2")
        buf.write(u"\u0697\u0698\5\u0082B\2\u0698\u0699\5F$\2\u0699\u069b")
        buf.write(u"\3\2\2\2\u069a\u0697\3\2\2\2\u069b\u069e\3\2\2\2\u069c")
        buf.write(u"\u069a\3\2\2\2\u069c\u069d\3\2\2\2\u069d\u00f5\3\2\2")
        buf.write(u"\2\u069e\u069c\3\2\2\2\u069f\u06a5\5V,\2\u06a0\u06a1")
        buf.write(u"\5\u0082B\2\u06a1\u06a2\5V,\2\u06a2\u06a4\3\2\2\2\u06a3")
        buf.write(u"\u06a0\3\2\2\2\u06a4\u06a7\3\2\2\2\u06a5\u06a3\3\2\2")
        buf.write(u"\2\u06a5\u06a6\3\2\2\2\u06a6\u00f7\3\2\2\2\u06a7\u06a5")
        buf.write(u"\3\2\2\2\u06a8\u06a9\7\30\2\2\u06a9\u06aa\5\u00fa~\2")
        buf.write(u"\u06aa\u06ab\7\24\2\2\u06ab\u06ac\5\u00fa~\2\u06ac\u06ad")
        buf.write(u"\7\31\2\2\u06ad\u06b7\3\2\2\2\u06ae\u06af\7\30\2\2\u06af")
        buf.write(u"\u06b0\5\u00fc\177\2\u06b0\u06b1\7\31\2\2\u06b1\u06b7")
        buf.write(u"\3\2\2\2\u06b2\u06b3\7*\2\2\u06b3\u06b4\5\u00fc\177\2")
        buf.write(u"\u06b4\u06b5\7(\2\2\u06b5\u06b7\3\2\2\2\u06b6\u06a8\3")
        buf.write(u"\2\2\2\u06b6\u06ae\3\2\2\2\u06b6\u06b2\3\2\2\2\u06b7")
        buf.write(u"\u00f9\3\2\2\2\u06b8\u06c7\7\u009f\2\2\u06b9\u06c7\7")
        buf.write(u"\u00a0\2\2\u06ba\u06c7\7\u00a8\2\2\u06bb\u06c7\7\u00a9")
        buf.write(u"\2\2\u06bc\u06c7\7\u009e\2\2\u06bd\u06c7\7\u00ad\2\2")
        buf.write(u"\u06be\u06c7\7\u00ac\2\2\u06bf\u06c7\7\u00a6\2\2\u06c0")
        buf.write(u"\u06c7\7\u00aa\2\2\u06c1\u06c7\7\u00ab\2\2\u06c2\u06c7")
        buf.write(u"\7\u009d\2\2\u06c3\u06c7\7\u00ae\2\2\u06c4\u06c7\7\u00a7")
        buf.write(u"\2\2\u06c5\u06c7\5\u0088E\2\u06c6\u06b8\3\2\2\2\u06c6")
        buf.write(u"\u06b9\3\2\2\2\u06c6\u06ba\3\2\2\2\u06c6\u06bb\3\2\2")
        buf.write(u"\2\u06c6\u06bc\3\2\2\2\u06c6\u06bd\3\2\2\2\u06c6\u06be")
        buf.write(u"\3\2\2\2\u06c6\u06bf\3\2\2\2\u06c6\u06c0\3\2\2\2\u06c6")
        buf.write(u"\u06c1\3\2\2\2\u06c6\u06c2\3\2\2\2\u06c6\u06c3\3\2\2")
        buf.write(u"\2\u06c6\u06c4\3\2\2\2\u06c6\u06c5\3\2\2\2\u06c7\u00fb")
        buf.write(u"\3\2\2\2\u06c8\u06cd\5\u00fa~\2\u06c9\u06ca\7\23\2\2")
        buf.write(u"\u06ca\u06cc\5\u00fa~\2\u06cb\u06c9\3\2\2\2\u06cc\u06cf")
        buf.write(u"\3\2\2\2\u06cd\u06cb\3\2\2\2\u06cd\u06ce\3\2\2\2\u06ce")
        buf.write(u"\u00fd\3\2\2\2\u06cf\u06cd\3\2\2\2\u06d0\u06d5\5\u0102")
        buf.write(u"\u0082\2\u06d1\u06d5\5\u0104\u0083\2\u06d2\u06d5\5\u00b6")
        buf.write(u"\\\2\u06d3\u06d5\5\u0100\u0081\2\u06d4\u06d0\3\2\2\2")
        buf.write(u"\u06d4\u06d1\3\2\2\2\u06d4\u06d2\3\2\2\2\u06d4\u06d3")
        buf.write(u"\3\2\2\2\u06d5\u00ff\3\2\2\2\u06d6\u06d7\t\5\2\2\u06d7")
        buf.write(u"\u0101\3\2\2\2\u06d8\u06d9\7\26\2\2\u06d9\u06da\5\\/")
        buf.write(u"\2\u06da\u06db\7\27\2\2\u06db\u0103\3\2\2\2\u06dc\u06df")
        buf.write(u"\5\u00fa~\2\u06dd\u06df\5\u0106\u0084\2\u06de\u06dc\3")
        buf.write(u"\2\2\2\u06de\u06dd\3\2\2\2\u06df\u0105\3\2\2\2\u06e0")
        buf.write(u"\u06e6\5\u00a2R\2\u06e1\u06e6\5\u009cO\2\u06e2\u06e6")
        buf.write(u"\5\u009eP\2\u06e3\u06e6\5\u010a\u0086\2\u06e4\u06e6\5")
        buf.write(u"\u0108\u0085\2\u06e5\u06e0\3\2\2\2\u06e5\u06e1\3\2\2")
        buf.write(u"\2\u06e5\u06e2\3\2\2\2\u06e5\u06e3\3\2\2\2\u06e5\u06e4")
        buf.write(u"\3\2\2\2\u06e6\u0107\3\2\2\2\u06e7\u06e9\7v\2\2\u06e8")
        buf.write(u"\u06e7\3\2\2\2\u06e8\u06e9\3\2\2\2\u06e9\u06ea\3\2\2")
        buf.write(u"\2\u06ea\u06ec\7\26\2\2\u06eb\u06ed\5\u010c\u0087\2\u06ec")
        buf.write(u"\u06eb\3\2\2\2\u06ec\u06ed\3\2\2\2\u06ed\u06ee\3\2\2")
        buf.write(u"\2\u06ee\u06ef\7\27\2\2\u06ef\u0109\3\2\2\2\u06f0\u06f2")
        buf.write(u"\7v\2\2\u06f1\u06f0\3\2\2\2\u06f1\u06f2\3\2\2\2\u06f2")
        buf.write(u"\u06f3\3\2\2\2\u06f3\u06f5\7\32\2\2\u06f4\u06f6\5\u010e")
        buf.write(u"\u0088\2\u06f5\u06f4\3\2\2\2\u06f5\u06f6\3\2\2\2\u06f6")
        buf.write(u"\u06f7\3\2\2\2\u06f7\u06f8\7\33\2\2\u06f8\u010b\3\2\2")
        buf.write(u"\2\u06f9\u06fa\5\\/\2\u06fa\u0703\7\23\2\2\u06fb\u0700")
        buf.write(u"\5\\/\2\u06fc\u06fd\7\23\2\2\u06fd\u06ff\5\\/\2\u06fe")
        buf.write(u"\u06fc\3\2\2\2\u06ff\u0702\3\2\2\2\u0700\u06fe\3\2\2")
        buf.write(u"\2\u0700\u0701\3\2\2\2\u0701\u0704\3\2\2\2\u0702\u0700")
        buf.write(u"\3\2\2\2\u0703\u06fb\3\2\2\2\u0703\u0704\3\2\2\2\u0704")
        buf.write(u"\u010d\3\2\2\2\u0705\u070a\5\u0110\u0089\2\u0706\u0707")
        buf.write(u"\7\23\2\2\u0707\u0709\5\u0110\u0089\2\u0708\u0706\3\2")
        buf.write(u"\2\2\u0709\u070c\3\2\2\2\u070a\u0708\3\2\2\2\u070a\u070b")
        buf.write(u"\3\2\2\2\u070b\u010f\3\2\2\2\u070c\u070a\3\2\2\2\u070d")
        buf.write(u"\u070e\5\\/\2\u070e\u070f\7\21\2\2\u070f\u0710\5\\/\2")
        buf.write(u"\u0710\u0111\3\2\2\2\u0711\u0712\5\\/\2\u0712\u0713\7")
        buf.write(u"\21\2\2\u0713\u0714\5\\/\2\u0714\u071b\3\2\2\2\u0715")
        buf.write(u"\u0716\5\\/\2\u0716\u0717\7\21\2\2\u0717\u071b\3\2\2")
        buf.write(u"\2\u0718\u0719\7\21\2\2\u0719\u071b\5\\/\2\u071a\u0711")
        buf.write(u"\3\2\2\2\u071a\u0715\3\2\2\2\u071a\u0718\3\2\2\2\u071b")
        buf.write(u"\u0113\3\2\2\2\u071c\u071d\5\u00b8]\2\u071d\u071e\5\u012a")
        buf.write(u"\u0096\2\u071e\u071f\5\\/\2\u071f\u0115\3\2\2\2\u0720")
        buf.write(u"\u0721\b\u008c\1\2\u0721\u0722\5\u00b8]\2\u0722\u0727")
        buf.write(u"\3\2\2\2\u0723\u0724\f\3\2\2\u0724\u0726\5|?\2\u0725")
        buf.write(u"\u0723\3\2\2\2\u0726\u0729\3\2\2\2\u0727\u0725\3\2\2")
        buf.write(u"\2\u0727\u0728\3\2\2\2\u0728\u0117\3\2\2\2\u0729\u0727")
        buf.write(u"\3\2\2\2\u072a\u072b\6\u008d.\3\u072b\u072c\7\u00a3\2")
        buf.write(u"\2\u072c\u072f\5\u00caf\2\u072d\u072f\5\\/\2\u072e\u072a")
        buf.write(u"\3\2\2\2\u072e\u072d\3\2\2\2\u072f\u0119\3\2\2\2\u0730")
        buf.write(u"\u0735\5\u011c\u008f\2\u0731\u0732\7\23\2\2\u0732\u0734")
        buf.write(u"\5\u011c\u008f\2\u0733\u0731\3\2\2\2\u0734\u0737\3\2")
        buf.write(u"\2\2\u0735\u0733\3\2\2\2\u0735\u0736\3\2\2\2\u0736\u011b")
        buf.write(u"\3\2\2\2\u0737\u0735\3\2\2\2\u0738\u073d\5\u00b8]\2\u0739")
        buf.write(u"\u073a\7\25\2\2\u073a\u073c\5\u00b8]\2\u073b\u0739\3")
        buf.write(u"\2\2\2\u073c\u073f\3\2\2\2\u073d\u073b\3\2\2\2\u073d")
        buf.write(u"\u073e\3\2\2\2\u073e\u0741\3\2\2\2\u073f\u073d\3\2\2")
        buf.write(u"\2\u0740\u0742\t\6\2\2\u0741\u0740\3\2\2\2\u0741\u0742")
        buf.write(u"\3\2\2\2\u0742\u011d\3\2\2\2\u0743\u074a\7\"\2\2\u0744")
        buf.write(u"\u074a\7#\2\2\u0745\u074a\5\u012c\u0097\2\u0746\u074a")
        buf.write(u"\5\u012e\u0098\2\u0747\u074a\5\u0130\u0099\2\u0748\u074a")
        buf.write(u"\5\u0132\u009a\2\u0749\u0743\3\2\2\2\u0749\u0744\3\2")
        buf.write(u"\2\2\u0749\u0745\3\2\2\2\u0749\u0746\3\2\2\2\u0749\u0747")
        buf.write(u"\3\2\2\2\u0749\u0748\3\2\2\2\u074a\u011f\3\2\2\2\u074b")
        buf.write(u"\u074c\7\u00a3\2\2\u074c\u074d\6\u0091/\3\u074d\u0121")
        buf.write(u"\3\2\2\2\u074e\u074f\7\u00a3\2\2\u074f\u0750\6\u0092")
        buf.write(u"\60\3\u0750\u0123\3\2\2\2\u0751\u0752\7\u00a3\2\2\u0752")
        buf.write(u"\u0753\6\u0093\61\3\u0753\u0125\3\2\2\2\u0754\u0755\7")
        buf.write(u"\u00a3\2\2\u0755\u0756\6\u0094\62\3\u0756\u0127\3\2\2")
        buf.write(u"\2\u0757\u0758\7\u00a3\2\2\u0758\u0759\6\u0095\63\3\u0759")
        buf.write(u"\u0129\3\2\2\2\u075a\u075b\7-\2\2\u075b\u012b\3\2\2\2")
        buf.write(u"\u075c\u075d\7$\2\2\u075d\u012d\3\2\2\2\u075e\u075f\7")
        buf.write(u"%\2\2\u075f\u012f\3\2\2\2\u0760\u0761\7&\2\2\u0761\u0131")
        buf.write(u"\3\2\2\2\u0762\u0763\t\7\2\2\u0763\u0133\3\2\2\2\u0764")
        buf.write(u"\u0765\7\u0088\2\2\u0765\u0766\5\u0136\u009c\2\u0766")
        buf.write(u"\u0767\7\22\2\2\u0767\u076c\3\2\2\2\u0768\u0769\5\u0136")
        buf.write(u"\u009c\2\u0769\u076a\7\22\2\2\u076a\u076c\3\2\2\2\u076b")
        buf.write(u"\u0764\3\2\2\2\u076b\u0768\3\2\2\2\u076c\u0135\3\2\2")
        buf.write(u"\2\u076d\u076e\b\u009c\1\2\u076e\u076f\5\u0138\u009d")
        buf.write(u"\2\u076f\u0774\3\2\2\2\u0770\u0771\f\3\2\2\u0771\u0773")
        buf.write(u"\5\u013e\u00a0\2\u0772\u0770\3\2\2\2\u0773\u0776\3\2")
        buf.write(u"\2\2\u0774\u0772\3\2\2\2\u0774\u0775\3\2\2\2\u0775\u0137")
        buf.write(u"\3\2\2\2\u0776\u0774\3\2\2\2\u0777\u077f\5\u013a\u009e")
        buf.write(u"\2\u0778\u077f\5\u013c\u009f\2\u0779\u077f\5\u0146\u00a4")
        buf.write(u"\2\u077a\u077f\5\u0148\u00a5\2\u077b\u077f\5\u014a\u00a6")
        buf.write(u"\2\u077c\u077f\5\u0140\u00a1\2\u077d\u077f\5\u0144\u00a3")
        buf.write(u"\2\u077e\u0777\3\2\2\2\u077e\u0778\3\2\2\2\u077e\u0779")
        buf.write(u"\3\2\2\2\u077e\u077a\3\2\2\2\u077e\u077b\3\2\2\2\u077e")
        buf.write(u"\u077c\3\2\2\2\u077e\u077d\3\2\2\2\u077f\u0139\3\2\2")
        buf.write(u"\2\u0780\u0781\5\u0100\u0081\2\u0781\u013b\3\2\2\2\u0782")
        buf.write(u"\u0783\5\u0120\u0091\2\u0783\u0784\5\u0140\u00a1\2\u0784")
        buf.write(u"\u013d\3\2\2\2\u0785\u0786\7\25\2\2\u0786\u078b\5\u0140")
        buf.write(u"\u00a1\2\u0787\u0788\7\25\2\2\u0788\u078b\5\u014c\u00a7")
        buf.write(u"\2\u0789\u078b\5\u0144\u00a3\2\u078a\u0785\3\2\2\2\u078a")
        buf.write(u"\u0787\3\2\2\2\u078a\u0789\3\2\2\2\u078b\u013f\3\2\2")
        buf.write(u"\2\u078c\u078d\5\u014c\u00a7\2\u078d\u078f\7\26\2\2\u078e")
        buf.write(u"\u0790\5\u0142\u00a2\2\u078f\u078e\3\2\2\2\u078f\u0790")
        buf.write(u"\3\2\2\2\u0790\u0791\3\2\2\2\u0791\u0792\7\27\2\2\u0792")
        buf.write(u"\u0141\3\2\2\2\u0793\u0794\b\u00a2\1\2\u0794\u0795\5")
        buf.write(u"\u0136\u009c\2\u0795\u079b\3\2\2\2\u0796\u0797\f\3\2")
        buf.write(u"\2\u0797\u0798\7\23\2\2\u0798\u079a\5\u0136\u009c\2\u0799")
        buf.write(u"\u0796\3\2\2\2\u079a\u079d\3\2\2\2\u079b\u0799\3\2\2")
        buf.write(u"\2\u079b\u079c\3\2\2\2\u079c\u0143\3\2\2\2\u079d\u079b")
        buf.write(u"\3\2\2\2\u079e\u079f\7\30\2\2\u079f\u07a0\5\u0136\u009c")
        buf.write(u"\2\u07a0\u07a1\7\31\2\2\u07a1\u0145\3\2\2\2\u07a2\u07a3")
        buf.write(u"\7\26\2\2\u07a3\u07a4\5\u0136\u009c\2\u07a4\u07a5\7\27")
        buf.write(u"\2\2\u07a5\u0147\3\2\2\2\u07a6\u07a7\5\u014c\u00a7\2")
        buf.write(u"\u07a7\u0149\3\2\2\2\u07a8\u07ae\7\u00a8\2\2\u07a9\u07ae")
        buf.write(u"\7\u00aa\2\2\u07aa\u07ae\7\u00a6\2\2\u07ab\u07ae\7\u009d")
        buf.write(u"\2\2\u07ac\u07ae\7\u009e\2\2\u07ad\u07a8\3\2\2\2\u07ad")
        buf.write(u"\u07a9\3\2\2\2\u07ad\u07aa\3\2\2\2\u07ad\u07ab\3\2\2")
        buf.write(u"\2\u07ad\u07ac\3\2\2\2\u07ae\u014b\3\2\2\2\u07af\u07b0")
        buf.write(u"\t\b\2\2\u07b0\u014d\3\2\2\2\u07b1\u07b2\7\u0088\2\2")
        buf.write(u"\u07b2\u07b5\5\u0150\u00a9\2\u07b3\u07b5\5\u0150\u00a9")
        buf.write(u"\2\u07b4\u07b1\3\2\2\2\u07b4\u07b3\3\2\2\2\u07b5\u014f")
        buf.write(u"\3\2\2\2\u07b6\u07b7\b\u00a9\1\2\u07b7\u07b8\5\u0152")
        buf.write(u"\u00aa\2\u07b8\u07bd\3\2\2\2\u07b9\u07ba\f\3\2\2\u07ba")
        buf.write(u"\u07bc\5\u0154\u00ab\2\u07bb\u07b9\3\2\2\2\u07bc\u07bf")
        buf.write(u"\3\2\2\2\u07bd\u07bb\3\2\2\2\u07bd\u07be\3\2\2\2\u07be")
        buf.write(u"\u0151\3\2\2\2\u07bf\u07bd\3\2\2\2\u07c0\u07c5\5\u015e")
        buf.write(u"\u00b0\2\u07c1\u07c5\5\u0160\u00b1\2\u07c2\u07c5\5\u0162")
        buf.write(u"\u00b2\2\u07c3\u07c5\5\u0156\u00ac\2\u07c4\u07c0\3\2")
        buf.write(u"\2\2\u07c4\u07c1\3\2\2\2\u07c4\u07c2\3\2\2\2\u07c4\u07c3")
        buf.write(u"\3\2\2\2\u07c5\u0153\3\2\2\2\u07c6\u07c7\7\25\2\2\u07c7")
        buf.write(u"\u07cd\5\u0156\u00ac\2\u07c8\u07c9\7\30\2\2\u07c9\u07ca")
        buf.write(u"\5\u0150\u00a9\2\u07ca\u07cb\7\31\2\2\u07cb\u07cd\3\2")
        buf.write(u"\2\2\u07cc\u07c6\3\2\2\2\u07cc\u07c8\3\2\2\2\u07cd\u0155")
        buf.write(u"\3\2\2\2\u07ce\u07cf\5\u0164\u00b3\2\u07cf\u07d1\7\26")
        buf.write(u"\2\2\u07d0\u07d2\5\u0158\u00ad\2\u07d1\u07d0\3\2\2\2")
        buf.write(u"\u07d1\u07d2\3\2\2\2\u07d2\u07d3\3\2\2\2\u07d3\u07d4")
        buf.write(u"\7\27\2\2\u07d4\u0157\3\2\2\2\u07d5\u07dc\5\u015a\u00ae")
        buf.write(u"\2\u07d6\u07dc\5\u015c\u00af\2\u07d7\u07d8\5\u015a\u00ae")
        buf.write(u"\2\u07d8\u07d9\7\23\2\2\u07d9\u07da\5\u015c\u00af\2\u07da")
        buf.write(u"\u07dc\3\2\2\2\u07db\u07d5\3\2\2\2\u07db\u07d6\3\2\2")
        buf.write(u"\2\u07db\u07d7\3\2\2\2\u07dc\u0159\3\2\2\2\u07dd\u07de")
        buf.write(u"\b\u00ae\1\2\u07de\u07df\5\u0150\u00a9\2\u07df\u07e5")
        buf.write(u"\3\2\2\2\u07e0\u07e1\f\3\2\2\u07e1\u07e2\7\23\2\2\u07e2")
        buf.write(u"\u07e4\5\u0150\u00a9\2\u07e3\u07e0\3\2\2\2\u07e4\u07e7")
        buf.write(u"\3\2\2\2\u07e5\u07e3\3\2\2\2\u07e5\u07e6\3\2\2\2\u07e6")
        buf.write(u"\u015b\3\2\2\2\u07e7\u07e5\3\2\2\2\u07e8\u07e9\b\u00af")
        buf.write(u"\1\2\u07e9\u07ea\5\u0164\u00b3\2\u07ea\u07eb\7-\2\2\u07eb")
        buf.write(u"\u07ec\5\u0150\u00a9\2\u07ec\u07f5\3\2\2\2\u07ed\u07ee")
        buf.write(u"\f\3\2\2\u07ee\u07ef\7\23\2\2\u07ef\u07f0\5\u0164\u00b3")
        buf.write(u"\2\u07f0\u07f1\7-\2\2\u07f1\u07f2\5\u0150\u00a9\2\u07f2")
        buf.write(u"\u07f4\3\2\2\2\u07f3\u07ed\3\2\2\2\u07f4\u07f7\3\2\2")
        buf.write(u"\2\u07f5\u07f3\3\2\2\2\u07f5\u07f6\3\2\2\2\u07f6\u015d")
        buf.write(u"\3\2\2\2\u07f7\u07f5\3\2\2\2\u07f8\u07f9\7\26\2\2\u07f9")
        buf.write(u"\u07fa\5\u0150\u00a9\2\u07fa\u07fb\7\27\2\2\u07fb\u015f")
        buf.write(u"\3\2\2\2\u07fc\u07fd\b\u00b1\1\2\u07fd\u0800\7\u00a5")
        buf.write(u"\2\2\u07fe\u0800\5\u0164\u00b3\2\u07ff\u07fc\3\2\2\2")
        buf.write(u"\u07ff\u07fe\3\2\2\2\u0800\u0806\3\2\2\2\u0801\u0802")
        buf.write(u"\f\3\2\2\u0802\u0803\7\25\2\2\u0803\u0805\5\u0164\u00b3")
        buf.write(u"\2\u0804\u0801\3\2\2\2\u0805\u0808\3\2\2\2\u0806\u0804")
        buf.write(u"\3\2\2\2\u0806\u0807\3\2\2\2\u0807\u0161\3\2\2\2\u0808")
        buf.write(u"\u0806\3\2\2\2\u0809\u080f\7\u00a8\2\2\u080a\u080f\7")
        buf.write(u"\u00aa\2\2\u080b\u080f\7\u00a6\2\2\u080c\u080f\7\u009d")
        buf.write(u"\2\2\u080d\u080f\7\u009e\2\2\u080e\u0809\3\2\2\2\u080e")
        buf.write(u"\u080a\3\2\2\2\u080e\u080b\3\2\2\2\u080e\u080c\3\2\2")
        buf.write(u"\2\u080e\u080d\3\2\2\2\u080f\u0163\3\2\2\2\u0810\u0811")
        buf.write(u"\t\t\2\2\u0811\u0165\3\2\2\2\u0812\u0813\7\u0088\2\2")
        buf.write(u"\u0813\u0814\5\u0168\u00b5\2\u0814\u0815\7\22\2\2\u0815")
        buf.write(u"\u081a\3\2\2\2\u0816\u0817\5\u0168\u00b5\2\u0817\u0818")
        buf.write(u"\7\22\2\2\u0818\u081a\3\2\2\2\u0819\u0812\3\2\2\2\u0819")
        buf.write(u"\u0816\3\2\2\2\u081a\u0167\3\2\2\2\u081b\u081c\b\u00b5")
        buf.write(u"\1\2\u081c\u081d\5\u016a\u00b6\2\u081d\u0822\3\2\2\2")
        buf.write(u"\u081e\u081f\f\3\2\2\u081f\u0821\5\u0170\u00b9\2\u0820")
        buf.write(u"\u081e\3\2\2\2\u0821\u0824\3\2\2\2\u0822\u0820\3\2\2")
        buf.write(u"\2\u0822\u0823\3\2\2\2\u0823\u0169\3\2\2\2\u0824\u0822")
        buf.write(u"\3\2\2\2\u0825\u082b\5\u016c\u00b7\2\u0826\u082b\5\u016e")
        buf.write(u"\u00b8\2\u0827\u082b\5\u0178\u00bd\2\u0828\u082b\5\u017a")
        buf.write(u"\u00be\2\u0829\u082b\5\u017e\u00c0\2\u082a\u0825\3\2")
        buf.write(u"\2\2\u082a\u0826\3\2\2\2\u082a\u0827\3\2\2\2\u082a\u0828")
        buf.write(u"\3\2\2\2\u082a\u0829\3\2\2\2\u082b\u016b\3\2\2\2\u082c")
        buf.write(u"\u082d\5\u0100\u0081\2\u082d\u016d\3\2\2\2\u082e\u082f")
        buf.write(u"\5\u0120\u0091\2\u082f\u0830\5\u0172\u00ba\2\u0830\u016f")
        buf.write(u"\3\2\2\2\u0831\u0832\7\25\2\2\u0832\u0835\5\u0172\u00ba")
        buf.write(u"\2\u0833\u0835\5\u0176\u00bc\2\u0834\u0831\3\2\2\2\u0834")
        buf.write(u"\u0833\3\2\2\2\u0835\u0171\3\2\2\2\u0836\u0837\5\u0180")
        buf.write(u"\u00c1\2\u0837\u0839\7\26\2\2\u0838\u083a\5\u0174\u00bb")
        buf.write(u"\2\u0839\u0838\3\2\2\2\u0839\u083a\3\2\2\2\u083a\u083b")
        buf.write(u"\3\2\2\2\u083b\u083c\7\27\2\2\u083c\u0173\3\2\2\2\u083d")
        buf.write(u"\u083e\b\u00bb\1\2\u083e\u083f\5\u0168\u00b5\2\u083f")
        buf.write(u"\u0845\3\2\2\2\u0840\u0841\f\3\2\2\u0841\u0842\7\23\2")
        buf.write(u"\2\u0842\u0844\5\u0168\u00b5\2\u0843\u0840\3\2\2\2\u0844")
        buf.write(u"\u0847\3\2\2\2\u0845\u0843\3\2\2\2\u0845\u0846\3\2\2")
        buf.write(u"\2\u0846\u0175\3\2\2\2\u0847\u0845\3\2\2\2\u0848\u0849")
        buf.write(u"\7\30\2\2\u0849\u084a\5\u0168\u00b5\2\u084a\u084b\7\31")
        buf.write(u"\2\2\u084b\u0177\3\2\2\2\u084c\u084d\7\26\2\2\u084d\u084e")
        buf.write(u"\5\u0168\u00b5\2\u084e\u084f\7\27\2\2\u084f\u0179\3\2")
        buf.write(u"\2\2\u0850\u0851\b\u00be\1\2\u0851\u0852\5\u0180\u00c1")
        buf.write(u"\2\u0852\u0858\3\2\2\2\u0853\u0854\f\3\2\2\u0854\u0855")
        buf.write(u"\7\25\2\2\u0855\u0857\5\u0180\u00c1\2\u0856\u0853\3\2")
        buf.write(u"\2\2\u0857\u085a\3\2\2\2\u0858\u0856\3\2\2\2\u0858\u0859")
        buf.write(u"\3\2\2\2\u0859\u017b\3\2\2\2\u085a\u0858\3\2\2\2\u085b")
        buf.write(u"\u085c\b\u00bf\1\2\u085c\u085d\5\u017a\u00be\2\u085d")
        buf.write(u"\u0862\3\2\2\2\u085e\u085f\f\3\2\2\u085f\u0861\7\u00a5")
        buf.write(u"\2\2\u0860\u085e\3\2\2\2\u0861\u0864\3\2\2\2\u0862\u0860")
        buf.write(u"\3\2\2\2\u0862\u0863\3\2\2\2\u0863\u017d\3\2\2\2\u0864")
        buf.write(u"\u0862\3\2\2\2\u0865\u086b\7\u00a8\2\2\u0866\u086b\7")
        buf.write(u"\u00aa\2\2\u0867\u086b\7\u00a6\2\2\u0868\u086b\7\u009d")
        buf.write(u"\2\2\u0869\u086b\7\u009e\2\2\u086a\u0865\3\2\2\2\u086a")
        buf.write(u"\u0866\3\2\2\2\u086a\u0867\3\2\2\2\u086a\u0868\3\2\2")
        buf.write(u"\2\u086a\u0869\3\2\2\2\u086b\u017f\3\2\2\2\u086c\u086d")
        buf.write(u"\t\n\2\2\u086d\u0181\3\2\2\2\u086e\u086f\7\u0088\2\2")
        buf.write(u"\u086f\u0870\5\u0184\u00c3\2\u0870\u0871\7\22\2\2\u0871")
        buf.write(u"\u0876\3\2\2\2\u0872\u0873\5\u0184\u00c3\2\u0873\u0874")
        buf.write(u"\7\22\2\2\u0874\u0876\3\2\2\2\u0875\u086e\3\2\2\2\u0875")
        buf.write(u"\u0872\3\2\2\2\u0876\u0183\3\2\2\2\u0877\u0878\b\u00c3")
        buf.write(u"\1\2\u0878\u0879\5\u0186\u00c4\2\u0879\u087e\3\2\2\2")
        buf.write(u"\u087a\u087b\f\3\2\2\u087b\u087d\5\u018c\u00c7\2\u087c")
        buf.write(u"\u087a\3\2\2\2\u087d\u0880\3\2\2\2\u087e\u087c\3\2\2")
        buf.write(u"\2\u087e\u087f\3\2\2\2\u087f\u0185\3\2\2\2\u0880\u087e")
        buf.write(u"\3\2\2\2\u0881\u0887\5\u0188\u00c5\2\u0882\u0887\5\u018a")
        buf.write(u"\u00c6\2\u0883\u0887\5\u0194\u00cb\2\u0884\u0887\5\u0196")
        buf.write(u"\u00cc\2\u0885\u0887\5\u0198\u00cd\2\u0886\u0881\3\2")
        buf.write(u"\2\2\u0886\u0882\3\2\2\2\u0886\u0883\3\2\2\2\u0886\u0884")
        buf.write(u"\3\2\2\2\u0886\u0885\3\2\2\2\u0887\u0187\3\2\2\2\u0888")
        buf.write(u"\u0889\5\u0100\u0081\2\u0889\u0189\3\2\2\2\u088a\u088b")
        buf.write(u"\5\u0120\u0091\2\u088b\u088c\5\u018e\u00c8\2\u088c\u018b")
        buf.write(u"\3\2\2\2\u088d\u088e\7\25\2\2\u088e\u0891\5\u018e\u00c8")
        buf.write(u"\2\u088f\u0891\5\u0192\u00ca\2\u0890\u088d\3\2\2\2\u0890")
        buf.write(u"\u088f\3\2\2\2\u0891\u018d\3\2\2\2\u0892\u0893\5\u019a")
        buf.write(u"\u00ce\2\u0893\u0895\7\26\2\2\u0894\u0896\5\u0190\u00c9")
        buf.write(u"\2\u0895\u0894\3\2\2\2\u0895\u0896\3\2\2\2\u0896\u0897")
        buf.write(u"\3\2\2\2\u0897\u0898\7\27\2\2\u0898\u018f\3\2\2\2\u0899")
        buf.write(u"\u089a\b\u00c9\1\2\u089a\u089b\5\u0184\u00c3\2\u089b")
        buf.write(u"\u08a1\3\2\2\2\u089c\u089d\f\3\2\2\u089d\u089e\7\23\2")
        buf.write(u"\2\u089e\u08a0\5\u0184\u00c3\2\u089f\u089c\3\2\2\2\u08a0")
        buf.write(u"\u08a3\3\2\2\2\u08a1\u089f\3\2\2\2\u08a1\u08a2\3\2\2")
        buf.write(u"\2\u08a2\u0191\3\2\2\2\u08a3\u08a1\3\2\2\2\u08a4\u08a5")
        buf.write(u"\7\30\2\2\u08a5\u08a6\5\u0184\u00c3\2\u08a6\u08a7\7\31")
        buf.write(u"\2\2\u08a7\u0193\3\2\2\2\u08a8\u08a9\7\26\2\2\u08a9\u08aa")
        buf.write(u"\5\u0184\u00c3\2\u08aa\u08ab\7\27\2\2\u08ab\u0195\3\2")
        buf.write(u"\2\2\u08ac\u08ad\b\u00cc\1\2\u08ad\u08b0\7\u00a5\2\2")
        buf.write(u"\u08ae\u08b0\5\u019a\u00ce\2\u08af\u08ac\3\2\2\2\u08af")
        buf.write(u"\u08ae\3\2\2\2\u08b0\u08b6\3\2\2\2\u08b1\u08b2\f\3\2")
        buf.write(u"\2\u08b2\u08b3\7\25\2\2\u08b3\u08b5\5\u019a\u00ce\2\u08b4")
        buf.write(u"\u08b1\3\2\2\2\u08b5\u08b8\3\2\2\2\u08b6\u08b4\3\2\2")
        buf.write(u"\2\u08b6\u08b7\3\2\2\2\u08b7\u0197\3\2\2\2\u08b8\u08b6")
        buf.write(u"\3\2\2\2\u08b9\u08bf\7\u00a8\2\2\u08ba\u08bf\7\u00aa")
        buf.write(u"\2\2\u08bb\u08bf\7\u00a6\2\2\u08bc\u08bf\7\u009d\2\2")
        buf.write(u"\u08bd\u08bf\7\u009e\2\2\u08be\u08b9\3\2\2\2\u08be\u08ba")
        buf.write(u"\3\2\2\2\u08be\u08bb\3\2\2\2\u08be\u08bc\3\2\2\2\u08be")
        buf.write(u"\u08bd\3\2\2\2\u08bf\u0199\3\2\2\2\u08c0\u08c1\t\13\2")
        buf.write(u"\2\u08c1\u019b\3\2\2\2\u00ba\u01a2\u01a5\u01be\u01c3")
        buf.write(u"\u01d1\u01d7\u01d9\u01db\u01e2\u01e7\u01f2\u01f9\u0206")
        buf.write(u"\u0214\u0228\u023f\u024a\u0251\u025a\u0263\u026c\u0281")
        buf.write(u"\u0289\u028e\u0294\u0299\u02a2\u02a7\u02ac\u02c4\u02cf")
        buf.write(u"\u02d3\u02e8\u0302\u0307\u0310\u0319\u0322\u033f\u0352")
        buf.write(u"\u0358\u037a\u0383\u039a\u03a8\u03b1\u03ba\u03d1\u03d7")
        buf.write(u"\u03eb\u0451\u0453\u045f\u046a\u0479\u047e\u0485\u048c")
        buf.write(u"\u0495\u049c\u04b6\u04c1\u04c5\u04ca\u04cf\u04d1\u04db")
        buf.write(u"\u04eb\u04f4\u04fa\u04ff\u0506\u050e\u0519\u0521\u0529")
        buf.write(u"\u052f\u0537\u0540\u0548\u0555\u0558\u055c\u0561\u0565")
        buf.write(u"\u056e\u0583\u058d\u058f\u0594\u05a4\u05a9\u05b2\u05b9")
        buf.write(u"\u05be\u05c3\u05d2\u05d7\u05da\u05de\u05e3\u05ea\u05f5")
        buf.write(u"\u05f7\u0600\u0608\u0610\u0616\u0622\u0626\u0630\u0635")
        buf.write(u"\u063b\u0642\u0647\u064e\u0656\u065d\u0667\u0674\u0678")
        buf.write(u"\u067b\u067f\u0682\u068a\u0693\u069c\u06a5\u06b6\u06c6")
        buf.write(u"\u06cd\u06d4\u06de\u06e5\u06e8\u06ec\u06f1\u06f5\u0700")
        buf.write(u"\u0703\u070a\u071a\u0727\u072e\u0735\u073d\u0741\u0749")
        buf.write(u"\u076b\u0774\u077e\u078a\u078f\u079b\u07ad\u07b4\u07bd")
        buf.write(u"\u07c4\u07cc\u07d1\u07db\u07e5\u07f5\u07ff\u0806\u080e")
        buf.write(u"\u0819\u0822\u082a\u0834\u0839\u0845\u0858\u0862\u086a")
        buf.write(u"\u0875\u087e\u0886\u0890\u0895\u08a1\u08af\u08b6\u08be")
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
                     u"'Iterator'", u"'Cursor'", u"'abstract'", u"'all'", 
                     u"'always'", u"'and'", u"'any'", u"'as'", u"<INVALID>", 
                     u"'attr'", u"'attribute'", u"'attributes'", u"'bindings'", 
                     u"'break'", u"'by'", u"'case'", u"'catch'", u"'category'", 
                     u"'class'", u"'close'", u"'contains'", u"'def'", u"'default'", 
                     u"'define'", u"'delete'", u"<INVALID>", u"'do'", u"'doing'", 
                     u"'each'", u"'else'", u"'enum'", u"'enumerated'", u"'except'", 
                     u"'execute'", u"'expecting'", u"'extends'", u"'fetch'", 
                     u"'finally'", u"'flush'", u"'for'", u"'from'", u"'getter'", 
                     u"'if'", u"'in'", u"'index'", u"'invoke'", u"'is'", 
                     u"'matching'", u"'method'", u"'methods'", u"'modulo'", 
                     u"'mutable'", u"'native'", u"'None'", u"'not'", u"<INVALID>", 
                     u"'null'", u"'on'", u"'one'", u"'open'", u"'operator'", 
                     u"'or'", u"'order'", u"'otherwise'", u"'pass'", u"'raise'", 
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
                      u"DOCUMENT", u"BLOB", u"IMAGE", u"UUID", u"ITERATOR", 
                      u"CURSOR", u"ABSTRACT", u"ALL", u"ALWAYS", u"AND", 
                      u"ANY", u"AS", u"ASC", u"ATTR", u"ATTRIBUTE", u"ATTRIBUTES", 
                      u"BINDINGS", u"BREAK", u"BY", u"CASE", u"CATCH", u"CATEGORY", 
                      u"CLASS", u"CLOSE", u"CONTAINS", u"DEF", u"DEFAULT", 
                      u"DEFINE", u"DELETE", u"DESC", u"DO", u"DOING", u"EACH", 
                      u"ELSE", u"ENUM", u"ENUMERATED", u"EXCEPT", u"EXECUTE", 
                      u"EXPECTING", u"EXTENDS", u"FETCH", u"FINALLY", u"FLUSH", 
                      u"FOR", u"FROM", u"GETTER", u"IF", u"IN", u"INDEX", 
                      u"INVOKE", u"IS", u"MATCHING", u"METHOD", u"METHODS", 
                      u"MODULO", u"MUTABLE", u"NATIVE", u"NONE", u"NOT", 
                      u"NOTHING", u"NULL", u"ON", u"ONE", u"OPEN", u"OPERATOR", 
                      u"OR", u"ORDER", u"OTHERWISE", u"PASS", u"RAISE", 
                      u"READ", u"RECEIVING", u"RESOURCE", u"RETURN", u"RETURNING", 
                      u"ROWS", u"SELF", u"SETTER", u"SINGLETON", u"SORTED", 
                      u"STORABLE", u"STORE", u"SWITCH", u"TEST", u"THIS", 
                      u"THROW", u"TO", u"TRY", u"VERIFYING", u"WITH", u"WHEN", 
                      u"WHERE", u"WHILE", u"WRITE", u"BOOLEAN_LITERAL", 
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
    RULE_read_expression = 55
    RULE_write_statement = 56
    RULE_fetch_list_expression = 57
    RULE_fetch_store_expression = 58
    RULE_sorted_expression = 59
    RULE_assign_instance_statement = 60
    RULE_child_instance = 61
    RULE_assign_tuple_statement = 62
    RULE_lfs = 63
    RULE_lfp = 64
    RULE_indent = 65
    RULE_dedent = 66
    RULE_null_literal = 67
    RULE_declaration_list = 68
    RULE_declarations = 69
    RULE_declaration = 70
    RULE_resource_declaration = 71
    RULE_enum_declaration = 72
    RULE_native_symbol_list = 73
    RULE_category_symbol_list = 74
    RULE_symbol_list = 75
    RULE_attribute_constraint = 76
    RULE_list_literal = 77
    RULE_set_literal = 78
    RULE_expression_list = 79
    RULE_range_literal = 80
    RULE_typedef = 81
    RULE_primary_type = 82
    RULE_native_type = 83
    RULE_category_type = 84
    RULE_mutable_category_type = 85
    RULE_code_type = 86
    RULE_category_declaration = 87
    RULE_type_identifier_list = 88
    RULE_method_identifier = 89
    RULE_identifier = 90
    RULE_variable_identifier = 91
    RULE_attribute_identifier = 92
    RULE_type_identifier = 93
    RULE_symbol_identifier = 94
    RULE_argument_list = 95
    RULE_argument = 96
    RULE_operator_argument = 97
    RULE_named_argument = 98
    RULE_code_argument = 99
    RULE_category_or_any_type = 100
    RULE_any_type = 101
    RULE_member_method_declaration_list = 102
    RULE_member_method_declaration = 103
    RULE_native_member_method_declaration_list = 104
    RULE_native_member_method_declaration = 105
    RULE_native_category_binding = 106
    RULE_python_category_binding = 107
    RULE_python_module = 108
    RULE_javascript_category_binding = 109
    RULE_javascript_module = 110
    RULE_variable_identifier_list = 111
    RULE_attribute_identifier_list = 112
    RULE_method_declaration = 113
    RULE_comment_statement = 114
    RULE_native_statement_list = 115
    RULE_native_statement = 116
    RULE_python_native_statement = 117
    RULE_javascript_native_statement = 118
    RULE_statement_list = 119
    RULE_assertion_list = 120
    RULE_switch_case_statement_list = 121
    RULE_catch_statement_list = 122
    RULE_literal_collection = 123
    RULE_atomic_literal = 124
    RULE_literal_list_literal = 125
    RULE_selectable_expression = 126
    RULE_this_expression = 127
    RULE_parenthesis_expression = 128
    RULE_literal_expression = 129
    RULE_collection_literal = 130
    RULE_tuple_literal = 131
    RULE_dict_literal = 132
    RULE_expression_tuple = 133
    RULE_dict_entry_list = 134
    RULE_dict_entry = 135
    RULE_slice_arguments = 136
    RULE_assign_variable_statement = 137
    RULE_assignable_instance = 138
    RULE_is_expression = 139
    RULE_order_by_list = 140
    RULE_order_by = 141
    RULE_operator = 142
    RULE_new_token = 143
    RULE_key_token = 144
    RULE_module_token = 145
    RULE_value_token = 146
    RULE_symbols_token = 147
    RULE_assign = 148
    RULE_multiply = 149
    RULE_divide = 150
    RULE_idivide = 151
    RULE_modulo = 152
    RULE_javascript_statement = 153
    RULE_javascript_expression = 154
    RULE_javascript_primary_expression = 155
    RULE_javascript_this_expression = 156
    RULE_javascript_new_expression = 157
    RULE_javascript_selector_expression = 158
    RULE_javascript_method_expression = 159
    RULE_javascript_arguments = 160
    RULE_javascript_item_expression = 161
    RULE_javascript_parenthesis_expression = 162
    RULE_javascript_identifier_expression = 163
    RULE_javascript_literal_expression = 164
    RULE_javascript_identifier = 165
    RULE_python_statement = 166
    RULE_python_expression = 167
    RULE_python_primary_expression = 168
    RULE_python_selector_expression = 169
    RULE_python_method_expression = 170
    RULE_python_argument_list = 171
    RULE_python_ordinal_argument_list = 172
    RULE_python_named_argument_list = 173
    RULE_python_parenthesis_expression = 174
    RULE_python_identifier_expression = 175
    RULE_python_literal_expression = 176
    RULE_python_identifier = 177
    RULE_java_statement = 178
    RULE_java_expression = 179
    RULE_java_primary_expression = 180
    RULE_java_this_expression = 181
    RULE_java_new_expression = 182
    RULE_java_selector_expression = 183
    RULE_java_method_expression = 184
    RULE_java_arguments = 185
    RULE_java_item_expression = 186
    RULE_java_parenthesis_expression = 187
    RULE_java_identifier_expression = 188
    RULE_java_class_identifier_expression = 189
    RULE_java_literal_expression = 190
    RULE_java_identifier = 191
    RULE_csharp_statement = 192
    RULE_csharp_expression = 193
    RULE_csharp_primary_expression = 194
    RULE_csharp_this_expression = 195
    RULE_csharp_new_expression = 196
    RULE_csharp_selector_expression = 197
    RULE_csharp_method_expression = 198
    RULE_csharp_arguments = 199
    RULE_csharp_item_expression = 200
    RULE_csharp_parenthesis_expression = 201
    RULE_csharp_identifier_expression = 202
    RULE_csharp_literal_expression = 203
    RULE_csharp_identifier = 204

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
                   u"argument_assignment", u"read_expression", u"write_statement", 
                   u"fetch_list_expression", u"fetch_store_expression", 
                   u"sorted_expression", u"assign_instance_statement", u"child_instance", 
                   u"assign_tuple_statement", u"lfs", u"lfp", u"indent", 
                   u"dedent", u"null_literal", u"declaration_list", u"declarations", 
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
                   u"is_expression", u"order_by_list", u"order_by", u"operator", 
                   u"new_token", u"key_token", u"module_token", u"value_token", 
                   u"symbols_token", u"assign", u"multiply", u"divide", 
                   u"idivide", u"modulo", u"javascript_statement", u"javascript_expression", 
                   u"javascript_primary_expression", u"javascript_this_expression", 
                   u"javascript_new_expression", u"javascript_selector_expression", 
                   u"javascript_method_expression", u"javascript_arguments", 
                   u"javascript_item_expression", u"javascript_parenthesis_expression", 
                   u"javascript_identifier_expression", u"javascript_literal_expression", 
                   u"javascript_identifier", u"python_statement", u"python_expression", 
                   u"python_primary_expression", u"python_selector_expression", 
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
    FINALLY=102
    FLUSH=103
    FOR=104
    FROM=105
    GETTER=106
    IF=107
    IN=108
    INDEX=109
    INVOKE=110
    IS=111
    MATCHING=112
    METHOD=113
    METHODS=114
    MODULO=115
    MUTABLE=116
    NATIVE=117
    NONE=118
    NOT=119
    NOTHING=120
    NULL=121
    ON=122
    ONE=123
    OPEN=124
    OPERATOR=125
    OR=126
    ORDER=127
    OTHERWISE=128
    PASS=129
    RAISE=130
    READ=131
    RECEIVING=132
    RESOURCE=133
    RETURN=134
    RETURNING=135
    ROWS=136
    SELF=137
    SETTER=138
    SINGLETON=139
    SORTED=140
    STORABLE=141
    STORE=142
    SWITCH=143
    TEST=144
    THIS=145
    THROW=146
    TO=147
    TRY=148
    VERIFYING=149
    WITH=150
    WHEN=151
    WHERE=152
    WHILE=153
    WRITE=154
    BOOLEAN_LITERAL=155
    CHAR_LITERAL=156
    MIN_INTEGER=157
    MAX_INTEGER=158
    SYMBOL_IDENTIFIER=159
    TYPE_IDENTIFIER=160
    VARIABLE_IDENTIFIER=161
    NATIVE_IDENTIFIER=162
    DOLLAR_IDENTIFIER=163
    TEXT_LITERAL=164
    UUID_LITERAL=165
    INTEGER_LITERAL=166
    HEXA_LITERAL=167
    DECIMAL_LITERAL=168
    DATETIME_LITERAL=169
    TIME_LITERAL=170
    DATE_LITERAL=171
    PERIOD_LITERAL=172

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
            self.attrs = None # Attribute_identifier_listContext
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


        def attribute_identifier_list(self):
            return self.getTypedRuleContext(SParser.Attribute_identifier_listContext,0)


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
            self.state = 410
            self.match(SParser.ENUM)
            self.state = 411 
            localctx.name = self.type_identifier()
            self.state = 412
            self.match(SParser.LPAR)
            self.state = 419
            token = self._input.LA(1)
            if token in [SParser.TYPE_IDENTIFIER]:
                self.state = 413 
                localctx.derived = self.type_identifier()
                self.state = 416
                _la = self._input.LA(1)
                if _la==SParser.COMMA:
                    self.state = 414
                    self.match(SParser.COMMA)
                    self.state = 415 
                    localctx.attrs = self.attribute_identifier_list()



            elif token in [SParser.STORABLE, SParser.VARIABLE_IDENTIFIER]:
                self.state = 418 
                localctx.attrs = self.attribute_identifier_list()

            else:
                raise NoViableAltException(self)

            self.state = 421
            self.match(SParser.RPAR)
            self.state = 422
            self.match(SParser.COLON)
            self.state = 423 
            self.indent()
            self.state = 424 
            localctx.symbols = self.category_symbol_list()
            self.state = 425 
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
            self.state = 427
            self.match(SParser.ENUM)
            self.state = 428 
            localctx.name = self.type_identifier()
            self.state = 429
            self.match(SParser.LPAR)
            self.state = 430 
            localctx.typ = self.native_type()
            self.state = 431
            self.match(SParser.RPAR)
            self.state = 432
            self.match(SParser.COLON)
            self.state = 433 
            self.indent()
            self.state = 434 
            localctx.symbols = self.native_symbol_list()
            self.state = 435 
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
            self.state = 437 
            localctx.name = self.symbol_identifier()
            self.state = 438
            self.match(SParser.EQ)
            self.state = 439 
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
            self.state = 441 
            localctx.name = self.symbol_identifier()
            self.state = 442
            self.match(SParser.LPAR)
            self.state = 444
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT) | (1 << SParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (SParser.EXECUTE - 98)) | (1 << (SParser.FETCH - 98)) | (1 << (SParser.MUTABLE - 98)) | (1 << (SParser.NONE - 98)) | (1 << (SParser.NOT - 98)) | (1 << (SParser.READ - 98)) | (1 << (SParser.SELF - 98)) | (1 << (SParser.SORTED - 98)) | (1 << (SParser.THIS - 98)) | (1 << (SParser.BOOLEAN_LITERAL - 98)) | (1 << (SParser.CHAR_LITERAL - 98)) | (1 << (SParser.MIN_INTEGER - 98)) | (1 << (SParser.MAX_INTEGER - 98)) | (1 << (SParser.SYMBOL_IDENTIFIER - 98)) | (1 << (SParser.TYPE_IDENTIFIER - 98)) | (1 << (SParser.VARIABLE_IDENTIFIER - 98)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (SParser.TEXT_LITERAL - 164)) | (1 << (SParser.UUID_LITERAL - 164)) | (1 << (SParser.INTEGER_LITERAL - 164)) | (1 << (SParser.HEXA_LITERAL - 164)) | (1 << (SParser.DECIMAL_LITERAL - 164)) | (1 << (SParser.DATETIME_LITERAL - 164)) | (1 << (SParser.TIME_LITERAL - 164)) | (1 << (SParser.DATE_LITERAL - 164)) | (1 << (SParser.PERIOD_LITERAL - 164)))) != 0):
                self.state = 443 
                localctx.args = self.argument_assignment_list(0)


            self.state = 446
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
            self.name = None # Attribute_identifierContext
            self.typ = None # TypedefContext
            self.match = None # Attribute_constraintContext
            self.indices = None # Index_clauseContext

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


        def attribute_identifier(self):
            return self.getTypedRuleContext(SParser.Attribute_identifierContext,0)


        def typedef(self):
            return self.getTypedRuleContext(SParser.TypedefContext,0)


        def PASS(self):
            return self.getToken(SParser.PASS, 0)

        def STORABLE(self):
            return self.getToken(SParser.STORABLE, 0)

        def attribute_constraint(self):
            return self.getTypedRuleContext(SParser.Attribute_constraintContext,0)


        def index_clause(self):
            return self.getTypedRuleContext(SParser.Index_clauseContext,0)


        def lfp(self):
            return self.getTypedRuleContext(SParser.LfpContext,0)


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
            self.state = 449
            _la = self._input.LA(1)
            if _la==SParser.STORABLE:
                self.state = 448
                self.match(SParser.STORABLE)


            self.state = 451
            self.match(SParser.ATTR)
            self.state = 452 
            localctx.name = self.attribute_identifier()
            self.state = 453
            self.match(SParser.LPAR)
            self.state = 454 
            localctx.typ = self.typedef(0)
            self.state = 455
            self.match(SParser.RPAR)
            self.state = 456
            self.match(SParser.COLON)
            self.state = 457 
            self.indent()
            self.state = 473
            token = self._input.LA(1)
            if token in [SParser.PASS]:
                self.state = 458
                self.match(SParser.PASS)

            elif token in [SParser.IN, SParser.INDEX, SParser.MATCHING]:
                self.state = 471
                token = self._input.LA(1)
                if token in [SParser.IN, SParser.MATCHING]:
                    self.state = 459 
                    localctx.match = self.attribute_constraint()
                    self.state = 463
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        self.state = 460 
                        self.lfp()
                        self.state = 461 
                        localctx.indices = self.index_clause()



                elif token in [SParser.INDEX]:
                    self.state = 465 
                    localctx.indices = self.index_clause()
                    self.state = 469
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        self.state = 466 
                        self.lfp()
                        self.state = 467 
                        localctx.match = self.attribute_constraint()



                else:
                    raise NoViableAltException(self)


            else:
                raise NoViableAltException(self)

            self.state = 475 
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
            super(SParser.Index_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.indices = None # Variable_identifier_listContext

        def INDEX(self):
            return self.getToken(SParser.INDEX, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def variable_identifier_list(self):
            return self.getTypedRuleContext(SParser.Variable_identifier_listContext,0)


        def getRuleIndex(self):
            return SParser.RULE_index_clause

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIndex_clause(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIndex_clause(self)




    def index_clause(self):

        localctx = SParser.Index_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_index_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.match(SParser.INDEX)
            self.state = 478
            self.match(SParser.LPAR)
            self.state = 480
            _la = self._input.LA(1)
            if _la==SParser.VARIABLE_IDENTIFIER:
                self.state = 479 
                localctx.indices = self.variable_identifier_list()


            self.state = 482
            self.match(SParser.RPAR)
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
            self.attrs = None # Attribute_identifier_listContext
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


        def attribute_identifier_list(self):
            return self.getTypedRuleContext(SParser.Attribute_identifier_listContext,0)


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
        self.enterRule(localctx, 12, self.RULE_concrete_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            _la = self._input.LA(1)
            if _la==SParser.STORABLE:
                self.state = 484
                self.match(SParser.STORABLE)


            self.state = 487
            _la = self._input.LA(1)
            if not(_la==SParser.CATEGORY or _la==SParser.CLASS):
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 488 
            localctx.name = self.type_identifier()
            self.state = 489
            self.match(SParser.LPAR)
            self.state = 496
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 490 
                localctx.derived = self.derived_list()
                pass

            elif la_ == 2:
                self.state = 491 
                localctx.attrs = self.attribute_identifier_list()
                pass

            elif la_ == 3:
                self.state = 492 
                localctx.derived = self.derived_list()
                self.state = 493
                self.match(SParser.COMMA)
                self.state = 494 
                localctx.attrs = self.attribute_identifier_list()
                pass


            self.state = 498
            self.match(SParser.RPAR)
            self.state = 499
            self.match(SParser.COLON)
            self.state = 500 
            self.indent()
            self.state = 503
            token = self._input.LA(1)
            if token in [SParser.ABSTRACT, SParser.DEF]:
                self.state = 501 
                localctx.methods = self.member_method_declaration_list()

            elif token in [SParser.PASS]:
                self.state = 502
                self.match(SParser.PASS)

            else:
                raise NoViableAltException(self)

            self.state = 505 
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
            self.attrs = None # Attribute_identifier_listContext
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


        def attribute_identifier_list(self):
            return self.getTypedRuleContext(SParser.Attribute_identifier_listContext,0)


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
        self.enterRule(localctx, 14, self.RULE_singleton_category_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(SParser.SINGLETON)
            self.state = 508 
            localctx.name = self.type_identifier()
            self.state = 509
            self.match(SParser.LPAR)
            self.state = 510 
            localctx.attrs = self.attribute_identifier_list()
            self.state = 511
            self.match(SParser.RPAR)
            self.state = 512
            self.match(SParser.COLON)
            self.state = 513 
            self.indent()
            self.state = 516
            token = self._input.LA(1)
            if token in [SParser.ABSTRACT, SParser.DEF]:
                self.state = 514 
                localctx.methods = self.member_method_declaration_list()

            elif token in [SParser.PASS]:
                self.state = 515
                self.match(SParser.PASS)

            else:
                raise NoViableAltException(self)

            self.state = 518 
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
        self.enterRule(localctx, 16, self.RULE_derived_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520 
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
        self.enterRule(localctx, 18, self.RULE_operator_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            self.match(SParser.DEF)
            self.state = 523
            self.match(SParser.OPERATOR)
            self.state = 524 
            localctx.op = self.operator()
            self.state = 525
            self.match(SParser.LPAR)
            self.state = 526 
            localctx.arg = self.operator_argument()
            self.state = 527
            self.match(SParser.RPAR)
            self.state = 530
            _la = self._input.LA(1)
            if _la==SParser.RARROW:
                self.state = 528
                self.match(SParser.RARROW)
                self.state = 529 
                localctx.typ = self.typedef(0)


            self.state = 532
            self.match(SParser.COLON)
            self.state = 533 
            self.indent()
            self.state = 534 
            localctx.stmts = self.statement_list()
            self.state = 535 
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
        self.enterRule(localctx, 20, self.RULE_setter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            self.match(SParser.DEF)
            self.state = 538 
            localctx.name = self.variable_identifier()
            self.state = 539
            self.match(SParser.SETTER)
            self.state = 540
            self.match(SParser.LPAR)
            self.state = 541
            self.match(SParser.RPAR)
            self.state = 542
            self.match(SParser.COLON)
            self.state = 543 
            self.indent()
            self.state = 544 
            localctx.stmts = self.statement_list()
            self.state = 545 
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
            super(SParser.Native_setter_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Native_statement_listContext

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


        def native_statement_list(self):
            return self.getTypedRuleContext(SParser.Native_statement_listContext,0)


        def NATIVE(self):
            return self.getToken(SParser.NATIVE, 0)

        def getRuleIndex(self):
            return SParser.RULE_native_setter_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNative_setter_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNative_setter_declaration(self)




    def native_setter_declaration(self):

        localctx = SParser.Native_setter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_native_setter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.match(SParser.DEF)
            self.state = 548 
            localctx.name = self.variable_identifier()
            self.state = 550
            _la = self._input.LA(1)
            if _la==SParser.NATIVE:
                self.state = 549
                self.match(SParser.NATIVE)


            self.state = 552
            self.match(SParser.SETTER)
            self.state = 553
            self.match(SParser.LPAR)
            self.state = 554
            self.match(SParser.RPAR)
            self.state = 555
            self.match(SParser.COLON)
            self.state = 556 
            self.indent()
            self.state = 557 
            localctx.stmts = self.native_statement_list()
            self.state = 558 
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
        self.enterRule(localctx, 24, self.RULE_getter_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            self.match(SParser.DEF)
            self.state = 561 
            localctx.name = self.variable_identifier()
            self.state = 562
            self.match(SParser.GETTER)
            self.state = 563
            self.match(SParser.LPAR)
            self.state = 564
            self.match(SParser.RPAR)
            self.state = 565
            self.match(SParser.COLON)
            self.state = 566 
            self.indent()
            self.state = 567 
            localctx.stmts = self.statement_list()
            self.state = 568 
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
            super(SParser.Native_getter_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.stmts = None # Native_statement_listContext

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


        def native_statement_list(self):
            return self.getTypedRuleContext(SParser.Native_statement_listContext,0)


        def NATIVE(self):
            return self.getToken(SParser.NATIVE, 0)

        def getRuleIndex(self):
            return SParser.RULE_native_getter_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNative_getter_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNative_getter_declaration(self)




    def native_getter_declaration(self):

        localctx = SParser.Native_getter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_native_getter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            self.match(SParser.DEF)
            self.state = 571 
            localctx.name = self.variable_identifier()
            self.state = 573
            _la = self._input.LA(1)
            if _la==SParser.NATIVE:
                self.state = 572
                self.match(SParser.NATIVE)


            self.state = 575
            self.match(SParser.GETTER)
            self.state = 576
            self.match(SParser.LPAR)
            self.state = 577
            self.match(SParser.RPAR)
            self.state = 578
            self.match(SParser.COLON)
            self.state = 579 
            self.indent()
            self.state = 580 
            localctx.stmts = self.native_statement_list()
            self.state = 581 
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
            self.attrs = None # Attribute_identifier_listContext
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


        def attribute_identifier_list(self):
            return self.getTypedRuleContext(SParser.Attribute_identifier_listContext,0)


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
        self.enterRule(localctx, 28, self.RULE_native_category_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 584
            _la = self._input.LA(1)
            if _la==SParser.STORABLE:
                self.state = 583
                self.match(SParser.STORABLE)


            self.state = 586
            self.match(SParser.NATIVE)
            self.state = 587
            _la = self._input.LA(1)
            if not(_la==SParser.CATEGORY or _la==SParser.CLASS):
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 588 
            localctx.name = self.type_identifier()
            self.state = 589
            self.match(SParser.LPAR)
            self.state = 591
            _la = self._input.LA(1)
            if _la==SParser.STORABLE or _la==SParser.VARIABLE_IDENTIFIER:
                self.state = 590 
                localctx.attrs = self.attribute_identifier_list()


            self.state = 593
            self.match(SParser.RPAR)
            self.state = 594
            self.match(SParser.COLON)
            self.state = 595 
            self.indent()
            self.state = 596 
            localctx.bindings = self.native_category_bindings()
            self.state = 600
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 597 
                self.lfp()
                self.state = 598 
                localctx.methods = self.native_member_method_declaration_list()


            self.state = 602 
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
            self.attrs = None # Attribute_identifier_listContext
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


        def attribute_identifier_list(self):
            return self.getTypedRuleContext(SParser.Attribute_identifier_listContext,0)


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
        self.enterRule(localctx, 30, self.RULE_native_resource_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.match(SParser.NATIVE)
            self.state = 605
            self.match(SParser.RESOURCE)
            self.state = 606 
            localctx.name = self.type_identifier()
            self.state = 607
            self.match(SParser.LPAR)
            self.state = 609
            _la = self._input.LA(1)
            if _la==SParser.STORABLE or _la==SParser.VARIABLE_IDENTIFIER:
                self.state = 608 
                localctx.attrs = self.attribute_identifier_list()


            self.state = 611
            self.match(SParser.RPAR)
            self.state = 612
            self.match(SParser.COLON)
            self.state = 613 
            self.indent()
            self.state = 614 
            localctx.bindings = self.native_category_bindings()
            self.state = 618
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 615 
                self.lfp()
                self.state = 616 
                localctx.methods = self.native_member_method_declaration_list()


            self.state = 620 
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
        self.enterRule(localctx, 32, self.RULE_native_category_bindings)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 622
            self.match(SParser.DEF)
            self.state = 623
            _la = self._input.LA(1)
            if not(_la==SParser.CATEGORY or _la==SParser.CLASS):
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 624
            self.match(SParser.BINDINGS)
            self.state = 625
            self.match(SParser.COLON)
            self.state = 626 
            self.indent()
            self.state = 627 
            localctx.items = self.native_category_binding_list(0)
            self.state = 628 
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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_native_category_binding_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.NativeCategoryBindingListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 631 
            localctx.item = self.native_category_binding()
            self._ctx.stop = self._input.LT(-1)
            self.state = 639
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.NativeCategoryBindingListItemContext(self, SParser.Native_category_binding_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_native_category_binding_list)
                    self.state = 633
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 634 
                    self.lfp()
                    self.state = 635 
                    localctx.item = self.native_category_binding() 
                self.state = 641
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
        self.enterRule(localctx, 36, self.RULE_abstract_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 642
            self.match(SParser.ABSTRACT)
            self.state = 643
            self.match(SParser.DEF)
            self.state = 644 
            localctx.name = self.method_identifier()
            self.state = 645
            self.match(SParser.LPAR)
            self.state = 647
            _la = self._input.LA(1)
            if _la==SParser.CODE or _la==SParser.MUTABLE or _la==SParser.VARIABLE_IDENTIFIER:
                self.state = 646 
                localctx.args = self.argument_list()


            self.state = 649
            self.match(SParser.RPAR)
            self.state = 652
            _la = self._input.LA(1)
            if _la==SParser.RARROW:
                self.state = 650
                self.match(SParser.RARROW)
                self.state = 651 
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
        self.enterRule(localctx, 38, self.RULE_concrete_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 654
            self.match(SParser.DEF)
            self.state = 655 
            localctx.name = self.method_identifier()
            self.state = 656
            self.match(SParser.LPAR)
            self.state = 658
            _la = self._input.LA(1)
            if _la==SParser.CODE or _la==SParser.MUTABLE or _la==SParser.VARIABLE_IDENTIFIER:
                self.state = 657 
                localctx.args = self.argument_list()


            self.state = 660
            self.match(SParser.RPAR)
            self.state = 663
            _la = self._input.LA(1)
            if _la==SParser.RARROW:
                self.state = 661
                self.match(SParser.RARROW)
                self.state = 662 
                localctx.typ = self.typedef(0)


            self.state = 665
            self.match(SParser.COLON)
            self.state = 666 
            self.indent()
            self.state = 667 
            localctx.stmts = self.statement_list()
            self.state = 668 
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


        def NATIVE(self):
            return self.getToken(SParser.NATIVE, 0)

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
        self.enterRule(localctx, 40, self.RULE_native_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 670
            self.match(SParser.DEF)
            self.state = 672
            _la = self._input.LA(1)
            if _la==SParser.NATIVE:
                self.state = 671
                self.match(SParser.NATIVE)


            self.state = 674 
            localctx.name = self.method_identifier()
            self.state = 675
            self.match(SParser.LPAR)
            self.state = 677
            _la = self._input.LA(1)
            if _la==SParser.CODE or _la==SParser.MUTABLE or _la==SParser.VARIABLE_IDENTIFIER:
                self.state = 676 
                localctx.args = self.argument_list()


            self.state = 679
            self.match(SParser.RPAR)
            self.state = 682
            _la = self._input.LA(1)
            if _la==SParser.RARROW:
                self.state = 680
                self.match(SParser.RARROW)
                self.state = 681 
                localctx.typ = self.category_or_any_type()


            self.state = 684
            self.match(SParser.COLON)
            self.state = 685 
            self.indent()
            self.state = 686 
            localctx.stmts = self.native_statement_list()
            self.state = 687 
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
        self.enterRule(localctx, 42, self.RULE_test_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 689
            self.match(SParser.DEF)
            self.state = 690
            self.match(SParser.TEST)
            self.state = 691
            localctx.name = self.match(SParser.TEXT_LITERAL)
            self.state = 692
            self.match(SParser.LPAR)
            self.state = 693
            self.match(SParser.RPAR)
            self.state = 694
            self.match(SParser.COLON)
            self.state = 695 
            self.indent()
            self.state = 696 
            localctx.stmts = self.statement_list()
            self.state = 697 
            self.dedent()
            self.state = 698 
            self.lfp()
            self.state = 699
            self.match(SParser.VERIFYING)
            self.state = 700
            self.match(SParser.COLON)
            self.state = 706
            token = self._input.LA(1)
            if token in [SParser.LF]:
                self.state = 701 
                self.indent()
                self.state = 702 
                localctx.exps = self.assertion_list()
                self.state = 703 
                self.dedent()

            elif token in [SParser.SYMBOL_IDENTIFIER]:
                self.state = 705 
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
        self.enterRule(localctx, 44, self.RULE_assertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 708 
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
            self.attrs = None # Attribute_identifier_listContext
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

        def attribute_identifier_list(self):
            return self.getTypedRuleContext(SParser.Attribute_identifier_listContext,0)


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
        self.enterRule(localctx, 46, self.RULE_typed_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 710 
            localctx.name = self.variable_identifier()
            self.state = 711
            self.match(SParser.COLON)
            self.state = 712 
            localctx.typ = self.category_or_any_type()
            self.state = 717
            _la = self._input.LA(1)
            if _la==SParser.LPAR:
                self.state = 713
                self.match(SParser.LPAR)
                self.state = 714 
                localctx.attrs = self.attribute_identifier_list()
                self.state = 715
                self.match(SParser.RPAR)


            self.state = 721
            _la = self._input.LA(1)
            if _la==SParser.EQ:
                self.state = 719
                self.match(SParser.EQ)
                self.state = 720 
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


    class BreakStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.BreakStatementContext, self).__init__(parser)
            self.stmt = None # Break_statementContext
            self.copyFrom(ctx)

        def break_statement(self):
            return self.getTypedRuleContext(SParser.Break_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitBreakStatement(self)


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


    class FlushStatementContext(StatementContext):

        def __init__(self, parser, ctx): # actually a SParser.StatementContext)
            super(SParser.FlushStatementContext, self).__init__(parser)
            self.stmt = None # Flush_statementContext
            self.copyFrom(ctx)

        def flush_statement(self):
            return self.getTypedRuleContext(SParser.Flush_statementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterFlushStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitFlushStatement(self)


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
        self.enterRule(localctx, 48, self.RULE_statement)
        try:
            self.state = 742
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                localctx = SParser.MethodCallStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 723 
                localctx.stmt = self.method_call()
                pass

            elif la_ == 2:
                localctx = SParser.AssignInstanceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 724 
                localctx.stmt = self.assign_instance_statement()
                pass

            elif la_ == 3:
                localctx = SParser.AssignTupleStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 725 
                localctx.stmt = self.assign_tuple_statement()
                pass

            elif la_ == 4:
                localctx = SParser.StoreStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 726 
                localctx.stmt = self.store_statement()
                pass

            elif la_ == 5:
                localctx = SParser.FlushStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 727 
                localctx.stmt = self.flush_statement()
                pass

            elif la_ == 6:
                localctx = SParser.BreakStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 728 
                localctx.stmt = self.break_statement()
                pass

            elif la_ == 7:
                localctx = SParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 729 
                localctx.stmt = self.return_statement()
                pass

            elif la_ == 8:
                localctx = SParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 730 
                localctx.stmt = self.if_statement()
                pass

            elif la_ == 9:
                localctx = SParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 731 
                localctx.stmt = self.switch_statement()
                pass

            elif la_ == 10:
                localctx = SParser.ForEachStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 732 
                localctx.stmt = self.for_each_statement()
                pass

            elif la_ == 11:
                localctx = SParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 733 
                localctx.stmt = self.while_statement()
                pass

            elif la_ == 12:
                localctx = SParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 734 
                localctx.stmt = self.do_while_statement()
                pass

            elif la_ == 13:
                localctx = SParser.RaiseStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 735 
                localctx.stmt = self.raise_statement()
                pass

            elif la_ == 14:
                localctx = SParser.TryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 736 
                localctx.stmt = self.try_statement()
                pass

            elif la_ == 15:
                localctx = SParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 737 
                localctx.stmt = self.write_statement()
                pass

            elif la_ == 16:
                localctx = SParser.WithResourceStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 738 
                localctx.stmt = self.with_resource_statement()
                pass

            elif la_ == 17:
                localctx = SParser.WithSingletonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 739 
                localctx.stmt = self.with_singleton_statement()
                pass

            elif la_ == 18:
                localctx = SParser.ClosureStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 740 
                localctx.decl = self.concrete_method_declaration()
                pass

            elif la_ == 19:
                localctx = SParser.CommentStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 19)
                self.state = 741 
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
            super(SParser.Flush_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FLUSH(self):
            return self.getToken(SParser.FLUSH, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def getRuleIndex(self):
            return SParser.RULE_flush_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterFlush_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitFlush_statement(self)




    def flush_statement(self):

        localctx = SParser.Flush_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_flush_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 744
            self.match(SParser.FLUSH)
            self.state = 745
            self.match(SParser.LPAR)
            self.state = 746
            self.match(SParser.RPAR)
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
        self.enterRule(localctx, 52, self.RULE_store_statement)
        try:
            self.state = 768
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 748
                self.match(SParser.DELETE)
                self.state = 749
                self.match(SParser.LPAR)
                self.state = 750 
                localctx.to_del = self.expression_list()
                self.state = 751
                self.match(SParser.RPAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 753
                self.match(SParser.STORE)
                self.state = 754
                self.match(SParser.LPAR)
                self.state = 755 
                localctx.to_add = self.expression_list()
                self.state = 756
                self.match(SParser.RPAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 758
                self.match(SParser.DELETE)
                self.state = 759
                self.match(SParser.LPAR)
                self.state = 760 
                localctx.to_del = self.expression_list()
                self.state = 761
                self.match(SParser.RPAR)
                self.state = 762
                self.match(SParser.AND)
                self.state = 763
                self.match(SParser.STORE)
                self.state = 764
                self.match(SParser.LPAR)
                self.state = 765 
                localctx.to_add = self.expression_list()
                self.state = 766
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
        self.enterRule(localctx, 54, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 770 
            localctx.method = self.method_selector()
            self.state = 771
            self.match(SParser.LPAR)
            self.state = 773
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT) | (1 << SParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (SParser.EXECUTE - 98)) | (1 << (SParser.FETCH - 98)) | (1 << (SParser.MUTABLE - 98)) | (1 << (SParser.NONE - 98)) | (1 << (SParser.NOT - 98)) | (1 << (SParser.READ - 98)) | (1 << (SParser.SELF - 98)) | (1 << (SParser.SORTED - 98)) | (1 << (SParser.THIS - 98)) | (1 << (SParser.BOOLEAN_LITERAL - 98)) | (1 << (SParser.CHAR_LITERAL - 98)) | (1 << (SParser.MIN_INTEGER - 98)) | (1 << (SParser.MAX_INTEGER - 98)) | (1 << (SParser.SYMBOL_IDENTIFIER - 98)) | (1 << (SParser.TYPE_IDENTIFIER - 98)) | (1 << (SParser.VARIABLE_IDENTIFIER - 98)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (SParser.TEXT_LITERAL - 164)) | (1 << (SParser.UUID_LITERAL - 164)) | (1 << (SParser.INTEGER_LITERAL - 164)) | (1 << (SParser.HEXA_LITERAL - 164)) | (1 << (SParser.DECIMAL_LITERAL - 164)) | (1 << (SParser.DATETIME_LITERAL - 164)) | (1 << (SParser.TIME_LITERAL - 164)) | (1 << (SParser.DATE_LITERAL - 164)) | (1 << (SParser.PERIOD_LITERAL - 164)))) != 0):
                self.state = 772 
                localctx.args = self.argument_assignment_list(0)


            self.state = 775
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
        self.enterRule(localctx, 56, self.RULE_method_selector)
        try:
            self.state = 782
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                localctx = SParser.MethodNameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 777 
                localctx.name = self.method_identifier()
                pass

            elif la_ == 2:
                localctx = SParser.MethodParentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 778 
                localctx.parent = self.callable_parent(0)
                self.state = 779
                self.match(SParser.DOT)
                self.state = 780 
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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_callable_parent, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.CallableRootContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 785 
            localctx.name = self.identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 791
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CallableSelectorContext(self, SParser.Callable_parentContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_callable_parent)
                    self.state = 787
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 788 
                    localctx.select = self.callable_selector() 
                self.state = 793
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
        self.enterRule(localctx, 60, self.RULE_callable_selector)
        try:
            self.state = 800
            token = self._input.LA(1)
            if token in [SParser.DOT]:
                localctx = SParser.CallableMemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 794
                self.match(SParser.DOT)
                self.state = 795 
                localctx.name = self.variable_identifier()

            elif token in [SParser.LBRAK]:
                localctx = SParser.CallableItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 796
                self.match(SParser.LBRAK)
                self.state = 797 
                localctx.exp = self.expression(0)
                self.state = 798
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
        self.enterRule(localctx, 62, self.RULE_with_resource_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 802
            self.match(SParser.WITH)
            self.state = 803 
            localctx.stmt = self.assign_variable_statement()
            self.state = 804
            self.match(SParser.COLON)
            self.state = 805 
            self.indent()
            self.state = 806 
            localctx.stmts = self.statement_list()
            self.state = 807 
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
        self.enterRule(localctx, 64, self.RULE_with_singleton_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 809
            self.match(SParser.WITH)
            self.state = 810 
            localctx.typ = self.type_identifier()
            self.state = 811
            self.match(SParser.COLON)
            self.state = 812 
            self.indent()
            self.state = 813 
            localctx.stmts = self.statement_list()
            self.state = 814 
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
        self.enterRule(localctx, 66, self.RULE_switch_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 816
            self.match(SParser.SWITCH)
            self.state = 817
            self.match(SParser.ON)
            self.state = 818 
            localctx.exp = self.expression(0)
            self.state = 819
            self.match(SParser.COLON)
            self.state = 820 
            self.indent()
            self.state = 821 
            localctx.cases = self.switch_case_statement_list()
            self.state = 829
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 822 
                self.lfp()
                self.state = 823
                self.match(SParser.OTHERWISE)
                self.state = 824
                self.match(SParser.COLON)
                self.state = 825 
                self.indent()
                self.state = 826 
                localctx.stmts = self.statement_list()
                self.state = 827 
                self.dedent()


            self.state = 831 
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
        self.enterRule(localctx, 68, self.RULE_switch_case_statement)
        try:
            self.state = 848
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                localctx = SParser.AtomicSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 833
                self.match(SParser.WHEN)
                self.state = 834 
                localctx.exp = self.atomic_literal()
                self.state = 835
                self.match(SParser.COLON)
                self.state = 836 
                self.indent()
                self.state = 837 
                localctx.stmts = self.statement_list()
                self.state = 838 
                self.dedent()
                pass

            elif la_ == 2:
                localctx = SParser.CollectionSwitchCaseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 840
                self.match(SParser.WHEN)
                self.state = 841
                self.match(SParser.IN)
                self.state = 842 
                localctx.exp = self.literal_collection()
                self.state = 843
                self.match(SParser.COLON)
                self.state = 844 
                self.indent()
                self.state = 845 
                localctx.stmts = self.statement_list()
                self.state = 846 
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
        self.enterRule(localctx, 70, self.RULE_for_each_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 850
            self.match(SParser.FOR)
            self.state = 851 
            localctx.name1 = self.variable_identifier()
            self.state = 854
            _la = self._input.LA(1)
            if _la==SParser.COMMA:
                self.state = 852
                self.match(SParser.COMMA)
                self.state = 853 
                localctx.name2 = self.variable_identifier()


            self.state = 856
            self.match(SParser.IN)
            self.state = 857 
            localctx.source = self.expression(0)
            self.state = 858
            self.match(SParser.COLON)
            self.state = 859 
            self.indent()
            self.state = 860 
            localctx.stmts = self.statement_list()
            self.state = 861 
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
        self.enterRule(localctx, 72, self.RULE_do_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 863
            self.match(SParser.DO)
            self.state = 864
            self.match(SParser.COLON)
            self.state = 865 
            self.indent()
            self.state = 866 
            localctx.stmts = self.statement_list()
            self.state = 867 
            self.dedent()
            self.state = 868 
            self.lfp()
            self.state = 869
            self.match(SParser.WHILE)
            self.state = 870 
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
        self.enterRule(localctx, 74, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 872
            self.match(SParser.WHILE)
            self.state = 873 
            localctx.exp = self.expression(0)
            self.state = 874
            self.match(SParser.COLON)
            self.state = 875 
            self.indent()
            self.state = 876 
            localctx.stmts = self.statement_list()
            self.state = 877 
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
        self.enterRule(localctx, 76, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 879
            self.match(SParser.IF)
            self.state = 880 
            localctx.exp = self.expression(0)
            self.state = 881
            self.match(SParser.COLON)
            self.state = 882 
            self.indent()
            self.state = 883 
            localctx.stmts = self.statement_list()
            self.state = 884 
            self.dedent()
            self.state = 888
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 885 
                self.lfp()
                self.state = 886 
                localctx.elseIfs = self.else_if_statement_list(0)


            self.state = 897
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 890 
                self.lfp()
                self.state = 891
                self.match(SParser.ELSE)
                self.state = 892
                self.match(SParser.COLON)
                self.state = 893 
                self.indent()
                self.state = 894 
                localctx.elseStmts = self.statement_list()
                self.state = 895 
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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_else_if_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.ElseIfStatementListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 900
            self.match(SParser.ELSE)
            self.state = 901
            self.match(SParser.IF)
            self.state = 902 
            localctx.exp = self.expression(0)
            self.state = 903
            self.match(SParser.COLON)
            self.state = 904 
            self.indent()
            self.state = 905 
            localctx.stmts = self.statement_list()
            self.state = 906 
            self.dedent()
            self._ctx.stop = self._input.LT(-1)
            self.state = 920
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.ElseIfStatementListItemContext(self, SParser.Else_if_statement_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_else_if_statement_list)
                    self.state = 908
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 909 
                    self.lfp()
                    self.state = 910
                    self.match(SParser.ELSE)
                    self.state = 911
                    self.match(SParser.IF)
                    self.state = 912 
                    localctx.exp = self.expression(0)
                    self.state = 913
                    self.match(SParser.COLON)
                    self.state = 914 
                    self.indent()
                    self.state = 915 
                    localctx.stmts = self.statement_list()
                    self.state = 916 
                    self.dedent() 
                self.state = 922
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
        self.enterRule(localctx, 80, self.RULE_raise_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 923
            self.match(SParser.RAISE)
            self.state = 924 
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
        self.enterRule(localctx, 82, self.RULE_try_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 926
            self.match(SParser.TRY)
            self.state = 927 
            localctx.name = self.variable_identifier()
            self.state = 928
            self.match(SParser.COLON)
            self.state = 929 
            self.indent()
            self.state = 930 
            localctx.stmts = self.statement_list()
            self.state = 931 
            self.dedent()
            self.state = 932 
            self.lfs()
            self.state = 934
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 933 
                localctx.handlers = self.catch_statement_list()


            self.state = 943
            _la = self._input.LA(1)
            if _la==SParser.EXCEPT:
                self.state = 936
                self.match(SParser.EXCEPT)
                self.state = 937
                self.match(SParser.COLON)
                self.state = 938 
                self.indent()
                self.state = 939 
                localctx.anyStmts = self.statement_list()
                self.state = 940 
                self.dedent()
                self.state = 941 
                self.lfs()


            self.state = 952
            _la = self._input.LA(1)
            if _la==SParser.FINALLY:
                self.state = 945
                self.match(SParser.FINALLY)
                self.state = 946
                self.match(SParser.COLON)
                self.state = 947 
                self.indent()
                self.state = 948 
                localctx.finalStmts = self.statement_list()
                self.state = 949 
                self.dedent()
                self.state = 950 
                self.lfs()


            self.state = 954 
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
        self.enterRule(localctx, 84, self.RULE_catch_statement)
        try:
            self.state = 975
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                localctx = SParser.CatchAtomicStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 956
                self.match(SParser.EXCEPT)
                self.state = 957 
                localctx.name = self.symbol_identifier()
                self.state = 958
                self.match(SParser.COLON)
                self.state = 959 
                self.indent()
                self.state = 960 
                localctx.stmts = self.statement_list()
                self.state = 961 
                self.dedent()
                self.state = 962 
                self.lfs()
                pass

            elif la_ == 2:
                localctx = SParser.CatchCollectionStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 964
                self.match(SParser.EXCEPT)
                self.state = 965
                self.match(SParser.IN)
                self.state = 966
                self.match(SParser.LBRAK)
                self.state = 967 
                localctx.exp = self.symbol_list()
                self.state = 968
                self.match(SParser.RBRAK)
                self.state = 969
                self.match(SParser.COLON)
                self.state = 970 
                self.indent()
                self.state = 971 
                localctx.stmts = self.statement_list()
                self.state = 972 
                self.dedent()
                self.state = 973 
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
            super(SParser.Break_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(SParser.BREAK, 0)

        def getRuleIndex(self):
            return SParser.RULE_break_statement

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterBreak_statement(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitBreak_statement(self)




    def break_statement(self):

        localctx = SParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 977
            self.match(SParser.BREAK)
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
        self.enterRule(localctx, 88, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 979
            self.match(SParser.RETURN)
            self.state = 981
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT) | (1 << SParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (SParser.EXECUTE - 98)) | (1 << (SParser.FETCH - 98)) | (1 << (SParser.MUTABLE - 98)) | (1 << (SParser.NONE - 98)) | (1 << (SParser.NOT - 98)) | (1 << (SParser.READ - 98)) | (1 << (SParser.SELF - 98)) | (1 << (SParser.SORTED - 98)) | (1 << (SParser.THIS - 98)) | (1 << (SParser.BOOLEAN_LITERAL - 98)) | (1 << (SParser.CHAR_LITERAL - 98)) | (1 << (SParser.MIN_INTEGER - 98)) | (1 << (SParser.MAX_INTEGER - 98)) | (1 << (SParser.SYMBOL_IDENTIFIER - 98)) | (1 << (SParser.TYPE_IDENTIFIER - 98)) | (1 << (SParser.VARIABLE_IDENTIFIER - 98)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (SParser.TEXT_LITERAL - 164)) | (1 << (SParser.UUID_LITERAL - 164)) | (1 << (SParser.INTEGER_LITERAL - 164)) | (1 << (SParser.HEXA_LITERAL - 164)) | (1 << (SParser.DECIMAL_LITERAL - 164)) | (1 << (SParser.DATETIME_LITERAL - 164)) | (1 << (SParser.TIME_LITERAL - 164)) | (1 << (SParser.DATE_LITERAL - 164)) | (1 << (SParser.PERIOD_LITERAL - 164)))) != 0):
                self.state = 980 
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
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1001
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                localctx = SParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 984
                self.match(SParser.MINUS)
                self.state = 985 
                localctx.exp = self.expression(32)
                pass

            elif la_ == 2:
                localctx = SParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 986
                self.match(SParser.NOT)
                self.state = 987 
                localctx.exp = self.expression(31)
                pass

            elif la_ == 3:
                localctx = SParser.InstanceExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 988 
                localctx.exp = self.instance_expression(0)
                pass

            elif la_ == 4:
                localctx = SParser.MethodExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 989 
                localctx.exp = self.method_expression()
                pass

            elif la_ == 5:
                localctx = SParser.CodeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 990
                self.match(SParser.CODE)
                self.state = 991
                self.match(SParser.LPAR)
                self.state = 992 
                localctx.exp = self.expression(0)
                self.state = 993
                self.match(SParser.RPAR)
                pass

            elif la_ == 6:
                localctx = SParser.ExecuteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 995
                self.match(SParser.EXECUTE)
                self.state = 996
                self.match(SParser.LPAR)
                self.state = 997 
                localctx.name = self.variable_identifier()
                self.state = 998
                self.match(SParser.RPAR)
                pass

            elif la_ == 7:
                localctx = SParser.ClosureExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1000 
                localctx.exp = self.closure_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1105
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1103
                    la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                    if la_ == 1:
                        localctx = SParser.MultiplyExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1003
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 1004 
                        self.multiply()
                        self.state = 1005 
                        localctx.right = self.expression(31)
                        pass

                    elif la_ == 2:
                        localctx = SParser.DivideExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1007
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 1008 
                        self.divide()
                        self.state = 1009 
                        localctx.right = self.expression(30)
                        pass

                    elif la_ == 3:
                        localctx = SParser.ModuloExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1011
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 1012 
                        self.modulo()
                        self.state = 1013 
                        localctx.right = self.expression(29)
                        pass

                    elif la_ == 4:
                        localctx = SParser.IntDivideExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1015
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 1016 
                        self.idivide()
                        self.state = 1017 
                        localctx.right = self.expression(28)
                        pass

                    elif la_ == 5:
                        localctx = SParser.AddExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1019
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 1020
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SParser.PLUS or _la==SParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 1021 
                        localctx.right = self.expression(27)
                        pass

                    elif la_ == 6:
                        localctx = SParser.LessThanExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1022
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 1023
                        self.match(SParser.LT)
                        self.state = 1024 
                        localctx.right = self.expression(26)
                        pass

                    elif la_ == 7:
                        localctx = SParser.LessThanOrEqualExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1025
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 1026
                        self.match(SParser.LTE)
                        self.state = 1027 
                        localctx.right = self.expression(25)
                        pass

                    elif la_ == 8:
                        localctx = SParser.GreaterThanExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1028
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 1029
                        self.match(SParser.GT)
                        self.state = 1030 
                        localctx.right = self.expression(24)
                        pass

                    elif la_ == 9:
                        localctx = SParser.GreaterThanOrEqualExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1031
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 1032
                        self.match(SParser.GTE)
                        self.state = 1033 
                        localctx.right = self.expression(23)
                        pass

                    elif la_ == 10:
                        localctx = SParser.EqualsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1034
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 1035
                        self.match(SParser.EQ2)
                        self.state = 1036 
                        localctx.right = self.expression(20)
                        pass

                    elif la_ == 11:
                        localctx = SParser.NotEqualsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1037
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 1038
                        self.match(SParser.XEQ)
                        self.state = 1039 
                        localctx.right = self.expression(19)
                        pass

                    elif la_ == 12:
                        localctx = SParser.RoughlyEqualsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1040
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 1041
                        self.match(SParser.TEQ)
                        self.state = 1042 
                        localctx.right = self.expression(18)
                        pass

                    elif la_ == 13:
                        localctx = SParser.OrExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1043
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 1044
                        self.match(SParser.OR)
                        self.state = 1045 
                        localctx.right = self.expression(17)
                        pass

                    elif la_ == 14:
                        localctx = SParser.AndExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1046
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 1047
                        self.match(SParser.AND)
                        self.state = 1048 
                        localctx.right = self.expression(16)
                        pass

                    elif la_ == 15:
                        localctx = SParser.TernaryExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.ifTrue = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1049
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 1050
                        self.match(SParser.IF)
                        self.state = 1051 
                        localctx.test = self.expression(0)
                        self.state = 1052
                        self.match(SParser.ELSE)
                        self.state = 1053 
                        localctx.ifFalse = self.expression(15)
                        pass

                    elif la_ == 16:
                        localctx = SParser.InExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1055
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 1056
                        self.match(SParser.IN)
                        self.state = 1057 
                        localctx.right = self.expression(13)
                        pass

                    elif la_ == 17:
                        localctx = SParser.ContainsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1058
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 1059
                        self.match(SParser.CONTAINS)
                        self.state = 1060 
                        localctx.right = self.expression(12)
                        pass

                    elif la_ == 18:
                        localctx = SParser.ContainsAllExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1061
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 1062
                        self.match(SParser.CONTAINS)
                        self.state = 1063
                        self.match(SParser.ALL)
                        self.state = 1064 
                        localctx.right = self.expression(11)
                        pass

                    elif la_ == 19:
                        localctx = SParser.ContainsAnyExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1065
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 1066
                        self.match(SParser.CONTAINS)
                        self.state = 1067
                        self.match(SParser.ANY)
                        self.state = 1068 
                        localctx.right = self.expression(10)
                        pass

                    elif la_ == 20:
                        localctx = SParser.NotInExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1069
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 1070
                        self.match(SParser.NOT)
                        self.state = 1071
                        self.match(SParser.IN)
                        self.state = 1072 
                        localctx.right = self.expression(9)
                        pass

                    elif la_ == 21:
                        localctx = SParser.NotContainsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1073
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 1074
                        self.match(SParser.NOT)
                        self.state = 1075
                        self.match(SParser.CONTAINS)
                        self.state = 1076 
                        localctx.right = self.expression(8)
                        pass

                    elif la_ == 22:
                        localctx = SParser.NotContainsAllExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1077
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 1078
                        self.match(SParser.NOT)
                        self.state = 1079
                        self.match(SParser.CONTAINS)
                        self.state = 1080
                        self.match(SParser.ALL)
                        self.state = 1081 
                        localctx.right = self.expression(7)
                        pass

                    elif la_ == 23:
                        localctx = SParser.NotContainsAnyExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1082
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 1083
                        self.match(SParser.NOT)
                        self.state = 1084
                        self.match(SParser.CONTAINS)
                        self.state = 1085
                        self.match(SParser.ANY)
                        self.state = 1086 
                        localctx.right = self.expression(6)
                        pass

                    elif la_ == 24:
                        localctx = SParser.IteratorExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.exp = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1087
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1088
                        self.match(SParser.FOR)
                        self.state = 1089 
                        localctx.name = self.variable_identifier()
                        self.state = 1090
                        self.match(SParser.IN)
                        self.state = 1091 
                        localctx.source = self.expression(2)
                        pass

                    elif la_ == 25:
                        localctx = SParser.IsNotExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1093
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 1094
                        self.match(SParser.IS)
                        self.state = 1095
                        self.match(SParser.NOT)
                        self.state = 1096 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 26:
                        localctx = SParser.IsExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1097
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 1098
                        self.match(SParser.IS)
                        self.state = 1099 
                        localctx.right = self.is_expression()
                        pass

                    elif la_ == 27:
                        localctx = SParser.CastExpressionContext(self, SParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1100
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 1101
                        self.match(SParser.AS)
                        self.state = 1102 
                        localctx.right = self.category_or_any_type()
                        pass

             
                self.state = 1107
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
        self.enterRule(localctx, 92, self.RULE_closure_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1108 
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
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_instance_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.SelectableExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1111 
            localctx.parent = self.selectable_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1117
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.SelectorExpressionContext(self, SParser.Instance_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_instance_expression)
                    self.state = 1113
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1114 
                    localctx.selector = self.instance_selector() 
                self.state = 1119
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
            super(SParser.Method_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def blob_expression(self):
            return self.getTypedRuleContext(SParser.Blob_expressionContext,0)


        def document_expression(self):
            return self.getTypedRuleContext(SParser.Document_expressionContext,0)


        def fetch_list_expression(self):
            return self.getTypedRuleContext(SParser.Fetch_list_expressionContext,0)


        def fetch_store_expression(self):
            return self.getTypedRuleContext(SParser.Fetch_store_expressionContext,0)


        def read_expression(self):
            return self.getTypedRuleContext(SParser.Read_expressionContext,0)


        def sorted_expression(self):
            return self.getTypedRuleContext(SParser.Sorted_expressionContext,0)


        def method_call(self):
            return self.getTypedRuleContext(SParser.Method_callContext,0)


        def constructor_expression(self):
            return self.getTypedRuleContext(SParser.Constructor_expressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_method_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMethod_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMethod_expression(self)




    def method_expression(self):

        localctx = SParser.Method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_method_expression)
        try:
            self.state = 1128
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1120 
                self.blob_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1121 
                self.document_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1122 
                self.fetch_list_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1123 
                self.fetch_store_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1124 
                self.read_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1125 
                self.sorted_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1126 
                self.method_call()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1127 
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
        self.enterRule(localctx, 98, self.RULE_instance_selector)
        try:
            self.state = 1143
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                localctx = SParser.MemberSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1130
                if not self.wasNot(SParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(SParser.WS)")
                self.state = 1131
                self.match(SParser.DOT)
                self.state = 1132 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = SParser.SliceSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1133
                if not self.wasNot(SParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(SParser.WS)")
                self.state = 1134
                self.match(SParser.LBRAK)
                self.state = 1135 
                localctx.xslice = self.slice_arguments()
                self.state = 1136
                self.match(SParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = SParser.ItemSelectorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1138
                if not self.wasNot(SParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(SParser.WS)")
                self.state = 1139
                self.match(SParser.LBRAK)
                self.state = 1140 
                localctx.exp = self.expression(0)
                self.state = 1141
                self.match(SParser.RBRAK)
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
            super(SParser.Blob_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BLOB(self):
            return self.getToken(SParser.BLOB, 0)

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SParser.RULE_blob_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterBlob_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitBlob_expression(self)




    def blob_expression(self):

        localctx = SParser.Blob_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_blob_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1145
            self.match(SParser.BLOB)
            self.state = 1146
            self.match(SParser.LPAR)
            self.state = 1148
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT) | (1 << SParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (SParser.EXECUTE - 98)) | (1 << (SParser.FETCH - 98)) | (1 << (SParser.MUTABLE - 98)) | (1 << (SParser.NONE - 98)) | (1 << (SParser.NOT - 98)) | (1 << (SParser.READ - 98)) | (1 << (SParser.SELF - 98)) | (1 << (SParser.SORTED - 98)) | (1 << (SParser.THIS - 98)) | (1 << (SParser.BOOLEAN_LITERAL - 98)) | (1 << (SParser.CHAR_LITERAL - 98)) | (1 << (SParser.MIN_INTEGER - 98)) | (1 << (SParser.MAX_INTEGER - 98)) | (1 << (SParser.SYMBOL_IDENTIFIER - 98)) | (1 << (SParser.TYPE_IDENTIFIER - 98)) | (1 << (SParser.VARIABLE_IDENTIFIER - 98)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (SParser.TEXT_LITERAL - 164)) | (1 << (SParser.UUID_LITERAL - 164)) | (1 << (SParser.INTEGER_LITERAL - 164)) | (1 << (SParser.HEXA_LITERAL - 164)) | (1 << (SParser.DECIMAL_LITERAL - 164)) | (1 << (SParser.DATETIME_LITERAL - 164)) | (1 << (SParser.TIME_LITERAL - 164)) | (1 << (SParser.DATE_LITERAL - 164)) | (1 << (SParser.PERIOD_LITERAL - 164)))) != 0):
                self.state = 1147 
                self.expression(0)


            self.state = 1150
            self.match(SParser.RPAR)
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

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


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
        self.enterRule(localctx, 102, self.RULE_document_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1152
            self.match(SParser.DOCUMENT)
            self.state = 1153
            self.match(SParser.LPAR)
            self.state = 1155
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT) | (1 << SParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (SParser.EXECUTE - 98)) | (1 << (SParser.FETCH - 98)) | (1 << (SParser.MUTABLE - 98)) | (1 << (SParser.NONE - 98)) | (1 << (SParser.NOT - 98)) | (1 << (SParser.READ - 98)) | (1 << (SParser.SELF - 98)) | (1 << (SParser.SORTED - 98)) | (1 << (SParser.THIS - 98)) | (1 << (SParser.BOOLEAN_LITERAL - 98)) | (1 << (SParser.CHAR_LITERAL - 98)) | (1 << (SParser.MIN_INTEGER - 98)) | (1 << (SParser.MAX_INTEGER - 98)) | (1 << (SParser.SYMBOL_IDENTIFIER - 98)) | (1 << (SParser.TYPE_IDENTIFIER - 98)) | (1 << (SParser.VARIABLE_IDENTIFIER - 98)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (SParser.TEXT_LITERAL - 164)) | (1 << (SParser.UUID_LITERAL - 164)) | (1 << (SParser.INTEGER_LITERAL - 164)) | (1 << (SParser.HEXA_LITERAL - 164)) | (1 << (SParser.DECIMAL_LITERAL - 164)) | (1 << (SParser.DATETIME_LITERAL - 164)) | (1 << (SParser.TIME_LITERAL - 164)) | (1 << (SParser.DATE_LITERAL - 164)) | (1 << (SParser.PERIOD_LITERAL - 164)))) != 0):
                self.state = 1154 
                self.expression(0)


            self.state = 1157
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
        self.enterRule(localctx, 104, self.RULE_constructor_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1159 
            localctx.typ = self.mutable_category_type()
            self.state = 1160
            self.match(SParser.LPAR)
            self.state = 1162
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT) | (1 << SParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (SParser.EXECUTE - 98)) | (1 << (SParser.FETCH - 98)) | (1 << (SParser.MUTABLE - 98)) | (1 << (SParser.NONE - 98)) | (1 << (SParser.NOT - 98)) | (1 << (SParser.READ - 98)) | (1 << (SParser.SELF - 98)) | (1 << (SParser.SORTED - 98)) | (1 << (SParser.THIS - 98)) | (1 << (SParser.BOOLEAN_LITERAL - 98)) | (1 << (SParser.CHAR_LITERAL - 98)) | (1 << (SParser.MIN_INTEGER - 98)) | (1 << (SParser.MAX_INTEGER - 98)) | (1 << (SParser.SYMBOL_IDENTIFIER - 98)) | (1 << (SParser.TYPE_IDENTIFIER - 98)) | (1 << (SParser.VARIABLE_IDENTIFIER - 98)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (SParser.TEXT_LITERAL - 164)) | (1 << (SParser.UUID_LITERAL - 164)) | (1 << (SParser.INTEGER_LITERAL - 164)) | (1 << (SParser.HEXA_LITERAL - 164)) | (1 << (SParser.DECIMAL_LITERAL - 164)) | (1 << (SParser.DATETIME_LITERAL - 164)) | (1 << (SParser.TIME_LITERAL - 164)) | (1 << (SParser.DATE_LITERAL - 164)) | (1 << (SParser.PERIOD_LITERAL - 164)))) != 0):
                self.state = 1161 
                localctx.args = self.argument_assignment_list(0)


            self.state = 1164
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
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_argument_assignment_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1171
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                localctx = SParser.ExpressionAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1167 
                localctx.exp = self.expression(0)
                self.state = 1168
                if not self.willNotBe(self.equalToken()):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willNotBe($parser.equalToken())")
                pass

            elif la_ == 2:
                localctx = SParser.ArgumentAssignmentListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1170 
                localctx.item = self.argument_assignment()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1178
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,59,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.ArgumentAssignmentListItemContext(self, SParser.Argument_assignment_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argument_assignment_list)
                    self.state = 1173
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1174
                    self.match(SParser.COMMA)
                    self.state = 1175 
                    localctx.item = self.argument_assignment() 
                self.state = 1180
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
        self.enterRule(localctx, 108, self.RULE_argument_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1181 
            localctx.name = self.variable_identifier()
            self.state = 1182 
            self.assign()
            self.state = 1183 
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
        self.enterRule(localctx, 110, self.RULE_read_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1185
            self.match(SParser.READ)
            self.state = 1186
            self.match(SParser.FROM)
            self.state = 1187 
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
        self.enterRule(localctx, 112, self.RULE_write_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1189
            self.match(SParser.WRITE)
            self.state = 1190 
            localctx.what = self.expression(0)
            self.state = 1191
            self.match(SParser.TO)
            self.state = 1192 
            localctx.target = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fetch_list_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Fetch_list_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Variable_identifierContext
            self.source = None # ExpressionContext
            self.predicate = None # ExpressionContext

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


        def getRuleIndex(self):
            return SParser.RULE_fetch_list_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterFetch_list_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitFetch_list_expression(self)




    def fetch_list_expression(self):

        localctx = SParser.Fetch_list_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_fetch_list_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1194
            self.match(SParser.FETCH)
            self.state = 1195 
            localctx.name = self.variable_identifier()
            self.state = 1196
            self.match(SParser.FROM)
            self.state = 1197 
            localctx.source = self.expression(0)
            self.state = 1198
            self.match(SParser.WHERE)
            self.state = 1199 
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
            super(SParser.Fetch_store_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_fetch_store_expression

     
        def copyFrom(self, ctx):
            super(SParser.Fetch_store_expressionContext, self).copyFrom(ctx)



    class FetchOneContext(Fetch_store_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Fetch_store_expressionContext)
            super(SParser.FetchOneContext, self).__init__(parser)
            self.typ = None # Mutable_category_typeContext
            self.predicate = None # ExpressionContext
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


    class FetchManyContext(Fetch_store_expressionContext):

        def __init__(self, parser, ctx): # actually a SParser.Fetch_store_expressionContext)
            super(SParser.FetchManyContext, self).__init__(parser)
            self.xstart = None # ExpressionContext
            self.xstop = None # ExpressionContext
            self.typ = None # Mutable_category_typeContext
            self.predicate = None # ExpressionContext
            self.orderby = None # Order_by_listContext
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
                listener.enterFetchMany(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitFetchMany(self)



    def fetch_store_expression(self):

        localctx = SParser.Fetch_store_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_fetch_store_expression)
        self._la = 0 # Token type
        try:
            self.state = 1231
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                localctx = SParser.FetchOneContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1201
                self.match(SParser.FETCH)
                self.state = 1202
                self.match(SParser.ONE)
                self.state = 1204
                _la = self._input.LA(1)
                if _la==SParser.MUTABLE or _la==SParser.TYPE_IDENTIFIER:
                    self.state = 1203 
                    localctx.typ = self.mutable_category_type()


                self.state = 1206
                self.match(SParser.WHERE)
                self.state = 1207 
                localctx.predicate = self.expression(0)
                pass

            elif la_ == 2:
                localctx = SParser.FetchManyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1208
                self.match(SParser.FETCH)
                self.state = 1215
                token = self._input.LA(1)
                if token in [SParser.ALL]:
                    self.state = 1209
                    self.match(SParser.ALL)

                elif token in [SParser.ROWS]:
                    self.state = 1210
                    self.match(SParser.ROWS)
                    self.state = 1211 
                    localctx.xstart = self.expression(0)
                    self.state = 1212
                    self.match(SParser.TO)
                    self.state = 1213 
                    localctx.xstop = self.expression(0)

                else:
                    raise NoViableAltException(self)

                self.state = 1217
                self.match(SParser.LPAR)
                self.state = 1219
                _la = self._input.LA(1)
                if _la==SParser.MUTABLE or _la==SParser.TYPE_IDENTIFIER:
                    self.state = 1218 
                    localctx.typ = self.mutable_category_type()


                self.state = 1221
                self.match(SParser.RPAR)
                self.state = 1224
                la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                if la_ == 1:
                    self.state = 1222
                    self.match(SParser.WHERE)
                    self.state = 1223 
                    localctx.predicate = self.expression(0)


                self.state = 1229
                la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
                if la_ == 1:
                    self.state = 1226
                    self.match(SParser.ORDER)
                    self.state = 1227
                    self.match(SParser.BY)
                    self.state = 1228 
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
        self.enterRule(localctx, 118, self.RULE_sorted_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1233
            self.match(SParser.SORTED)
            self.state = 1234
            self.match(SParser.LPAR)
            self.state = 1235 
            localctx.source = self.instance_expression(0)
            self.state = 1241
            _la = self._input.LA(1)
            if _la==SParser.COMMA:
                self.state = 1236
                self.match(SParser.COMMA)
                self.state = 1237 
                self.key_token()
                self.state = 1238
                self.match(SParser.EQ)
                self.state = 1239 
                localctx.key = self.instance_expression(0)


            self.state = 1243
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
        self.enterRule(localctx, 120, self.RULE_assign_instance_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1245 
            localctx.inst = self.assignable_instance(0)
            self.state = 1246 
            self.assign()
            self.state = 1247 
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
        self.enterRule(localctx, 122, self.RULE_child_instance)
        try:
            self.state = 1257
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                localctx = SParser.MemberInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1249
                if not self.wasNot(SParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(SParser.WS)")
                self.state = 1250
                self.match(SParser.DOT)
                self.state = 1251 
                localctx.name = self.variable_identifier()
                pass

            elif la_ == 2:
                localctx = SParser.ItemInstanceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1252
                if not self.wasNot(SParser.WS):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.wasNot(SParser.WS)")
                self.state = 1253
                self.match(SParser.LBRAK)
                self.state = 1254 
                localctx.exp = self.expression(0)
                self.state = 1255
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
        self.enterRule(localctx, 124, self.RULE_assign_tuple_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1259 
            localctx.items = self.variable_identifier_list()
            self.state = 1260 
            self.assign()
            self.state = 1261 
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
        self.enterRule(localctx, 126, self.RULE_lfs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,68,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1263
                    self.match(SParser.LF) 
                self.state = 1268
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,68,self._ctx)

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
        self.enterRule(localctx, 128, self.RULE_lfp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1270 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1269
                self.match(SParser.LF)
                self.state = 1272 
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
        self.enterRule(localctx, 130, self.RULE_indent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1275 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1274
                self.match(SParser.LF)
                self.state = 1277 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SParser.LF):
                    break

            self.state = 1279
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
        self.enterRule(localctx, 132, self.RULE_dedent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SParser.LF:
                self.state = 1281
                self.match(SParser.LF)
                self.state = 1286
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1287
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
        self.enterRule(localctx, 134, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1289
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
        self.enterRule(localctx, 136, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            localctx = SParser.FullDeclarationListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 1292
            _la = self._input.LA(1)
            if _la==SParser.COMMENT or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (SParser.ABSTRACT - 67)) | (1 << (SParser.ATTR - 67)) | (1 << (SParser.CATEGORY - 67)) | (1 << (SParser.CLASS - 67)) | (1 << (SParser.DEF - 67)) | (1 << (SParser.ENUM - 67)) | (1 << (SParser.NATIVE - 67)))) != 0) or _la==SParser.SINGLETON or _la==SParser.STORABLE:
                self.state = 1291 
                self.declarations()


            self.state = 1294 
            self.lfs()
            self.state = 1295
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

        def declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(SParser.DeclarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.LfpContext)
            else:
                return self.getTypedRuleContext(SParser.LfpContext,i)


        def getRuleIndex(self):
            return SParser.RULE_declarations

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDeclarations(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDeclarations(self)




    def declarations(self):

        localctx = SParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_declarations)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1297 
            self.declaration()
            self.state = 1303
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,73,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1298 
                    self.lfp()
                    self.state = 1299 
                    self.declaration() 
                self.state = 1305
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,73,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 140, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SParser.COMMENT:
                self.state = 1306 
                self.comment_statement()
                self.state = 1307 
                self.lfp()
                self.state = 1313
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1319
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                self.state = 1314 
                self.attribute_declaration()
                pass

            elif la_ == 2:
                self.state = 1315 
                self.category_declaration()
                pass

            elif la_ == 3:
                self.state = 1316 
                self.resource_declaration()
                pass

            elif la_ == 4:
                self.state = 1317 
                self.enum_declaration()
                pass

            elif la_ == 5:
                self.state = 1318 
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
        self.enterRule(localctx, 142, self.RULE_resource_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1321 
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
            super(SParser.Enum_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def enum_category_declaration(self):
            return self.getTypedRuleContext(SParser.Enum_category_declarationContext,0)


        def enum_native_declaration(self):
            return self.getTypedRuleContext(SParser.Enum_native_declarationContext,0)


        def getRuleIndex(self):
            return SParser.RULE_enum_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterEnum_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitEnum_declaration(self)




    def enum_declaration(self):

        localctx = SParser.Enum_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_enum_declaration)
        try:
            self.state = 1325
            la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1323 
                self.enum_category_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1324 
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
            super(SParser.Native_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_symbol(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Native_symbolContext)
            else:
                return self.getTypedRuleContext(SParser.Native_symbolContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.LfpContext)
            else:
                return self.getTypedRuleContext(SParser.LfpContext,i)


        def getRuleIndex(self):
            return SParser.RULE_native_symbol_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNative_symbol_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNative_symbol_list(self)




    def native_symbol_list(self):

        localctx = SParser.Native_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_native_symbol_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1327 
            self.native_symbol()
            self.state = 1333
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,77,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1328 
                    self.lfp()
                    self.state = 1329 
                    self.native_symbol() 
                self.state = 1335
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,77,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Category_symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Category_symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def category_symbol(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Category_symbolContext)
            else:
                return self.getTypedRuleContext(SParser.Category_symbolContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.LfpContext)
            else:
                return self.getTypedRuleContext(SParser.LfpContext,i)


        def getRuleIndex(self):
            return SParser.RULE_category_symbol_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCategory_symbol_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCategory_symbol_list(self)




    def category_symbol_list(self):

        localctx = SParser.Category_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_category_symbol_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1336 
            self.category_symbol()
            self.state = 1342
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,78,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1337 
                    self.lfp()
                    self.state = 1338 
                    self.category_symbol() 
                self.state = 1344
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,78,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Symbol_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Symbol_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def symbol_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Symbol_identifierContext)
            else:
                return self.getTypedRuleContext(SParser.Symbol_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SParser.COMMA)
            else:
                return self.getToken(SParser.COMMA, i)

        def getRuleIndex(self):
            return SParser.RULE_symbol_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSymbol_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSymbol_list(self)




    def symbol_list(self):

        localctx = SParser.Symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_symbol_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1345 
            self.symbol_identifier()
            self.state = 1350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SParser.COMMA:
                self.state = 1346
                self.match(SParser.COMMA)
                self.state = 1347 
                self.symbol_identifier()
                self.state = 1352
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
        self.enterRule(localctx, 152, self.RULE_attribute_constraint)
        try:
            self.state = 1363
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                localctx = SParser.MatchingListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1353
                self.match(SParser.IN)
                self.state = 1354 
                localctx.source = self.list_literal()
                pass

            elif la_ == 2:
                localctx = SParser.MatchingSetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1355
                self.match(SParser.IN)
                self.state = 1356 
                localctx.source = self.set_literal()
                pass

            elif la_ == 3:
                localctx = SParser.MatchingRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1357
                self.match(SParser.IN)
                self.state = 1358 
                localctx.source = self.range_literal()
                pass

            elif la_ == 4:
                localctx = SParser.MatchingPatternContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1359
                self.match(SParser.MATCHING)
                self.state = 1360
                localctx.text = self.match(SParser.TEXT_LITERAL)
                pass

            elif la_ == 5:
                localctx = SParser.MatchingExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1361
                self.match(SParser.MATCHING)
                self.state = 1362 
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

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)

        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)

        def MUTABLE(self):
            return self.getToken(SParser.MUTABLE, 0)

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
        self.enterRule(localctx, 154, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1366
            _la = self._input.LA(1)
            if _la==SParser.MUTABLE:
                self.state = 1365
                self.match(SParser.MUTABLE)


            self.state = 1368
            self.match(SParser.LBRAK)
            self.state = 1370
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT) | (1 << SParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (SParser.EXECUTE - 98)) | (1 << (SParser.FETCH - 98)) | (1 << (SParser.MUTABLE - 98)) | (1 << (SParser.NONE - 98)) | (1 << (SParser.NOT - 98)) | (1 << (SParser.READ - 98)) | (1 << (SParser.SELF - 98)) | (1 << (SParser.SORTED - 98)) | (1 << (SParser.THIS - 98)) | (1 << (SParser.BOOLEAN_LITERAL - 98)) | (1 << (SParser.CHAR_LITERAL - 98)) | (1 << (SParser.MIN_INTEGER - 98)) | (1 << (SParser.MAX_INTEGER - 98)) | (1 << (SParser.SYMBOL_IDENTIFIER - 98)) | (1 << (SParser.TYPE_IDENTIFIER - 98)) | (1 << (SParser.VARIABLE_IDENTIFIER - 98)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (SParser.TEXT_LITERAL - 164)) | (1 << (SParser.UUID_LITERAL - 164)) | (1 << (SParser.INTEGER_LITERAL - 164)) | (1 << (SParser.HEXA_LITERAL - 164)) | (1 << (SParser.DECIMAL_LITERAL - 164)) | (1 << (SParser.DATETIME_LITERAL - 164)) | (1 << (SParser.TIME_LITERAL - 164)) | (1 << (SParser.DATE_LITERAL - 164)) | (1 << (SParser.PERIOD_LITERAL - 164)))) != 0):
                self.state = 1369 
                self.expression_list()


            self.state = 1372
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

        def LT(self):
            return self.getToken(SParser.LT, 0)

        def GT(self):
            return self.getToken(SParser.GT, 0)

        def MUTABLE(self):
            return self.getToken(SParser.MUTABLE, 0)

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
        self.enterRule(localctx, 156, self.RULE_set_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1375
            _la = self._input.LA(1)
            if _la==SParser.MUTABLE:
                self.state = 1374
                self.match(SParser.MUTABLE)


            self.state = 1377
            self.match(SParser.LT)
            self.state = 1379
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT) | (1 << SParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (SParser.EXECUTE - 98)) | (1 << (SParser.FETCH - 98)) | (1 << (SParser.MUTABLE - 98)) | (1 << (SParser.NONE - 98)) | (1 << (SParser.NOT - 98)) | (1 << (SParser.READ - 98)) | (1 << (SParser.SELF - 98)) | (1 << (SParser.SORTED - 98)) | (1 << (SParser.THIS - 98)) | (1 << (SParser.BOOLEAN_LITERAL - 98)) | (1 << (SParser.CHAR_LITERAL - 98)) | (1 << (SParser.MIN_INTEGER - 98)) | (1 << (SParser.MAX_INTEGER - 98)) | (1 << (SParser.SYMBOL_IDENTIFIER - 98)) | (1 << (SParser.TYPE_IDENTIFIER - 98)) | (1 << (SParser.VARIABLE_IDENTIFIER - 98)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (SParser.TEXT_LITERAL - 164)) | (1 << (SParser.UUID_LITERAL - 164)) | (1 << (SParser.INTEGER_LITERAL - 164)) | (1 << (SParser.HEXA_LITERAL - 164)) | (1 << (SParser.DECIMAL_LITERAL - 164)) | (1 << (SParser.DATETIME_LITERAL - 164)) | (1 << (SParser.TIME_LITERAL - 164)) | (1 << (SParser.DATE_LITERAL - 164)) | (1 << (SParser.PERIOD_LITERAL - 164)))) != 0):
                self.state = 1378 
                self.expression_list()


            self.state = 1381
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

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SParser.COMMA)
            else:
                return self.getToken(SParser.COMMA, i)

        def getRuleIndex(self):
            return SParser.RULE_expression_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterExpression_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitExpression_list(self)




    def expression_list(self):

        localctx = SParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1383 
            self.expression(0)
            self.state = 1388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SParser.COMMA:
                self.state = 1384
                self.match(SParser.COMMA)
                self.state = 1385 
                self.expression(0)
                self.state = 1390
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
        self.enterRule(localctx, 160, self.RULE_range_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1391
            self.match(SParser.LBRAK)
            self.state = 1392 
            localctx.low = self.expression(0)
            self.state = 1393
            self.match(SParser.RANGE)
            self.state = 1394 
            localctx.high = self.expression(0)
            self.state = 1395
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


    class IteratorTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a SParser.TypedefContext)
            super(SParser.IteratorTypeContext, self).__init__(parser)
            self.i = None # TypedefContext
            self.copyFrom(ctx)

        def ITERATOR(self):
            return self.getToken(SParser.ITERATOR, 0)
        def LT(self):
            return self.getToken(SParser.LT, 0)
        def GT(self):
            return self.getToken(SParser.GT, 0)
        def typedef(self):
            return self.getTypedRuleContext(SParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterIteratorType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitIteratorType(self)


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


    class CursorTypeContext(TypedefContext):

        def __init__(self, parser, ctx): # actually a SParser.TypedefContext)
            super(SParser.CursorTypeContext, self).__init__(parser)
            self.c = None # TypedefContext
            self.copyFrom(ctx)

        def CURSOR(self):
            return self.getToken(SParser.CURSOR, 0)
        def LT(self):
            return self.getToken(SParser.LT, 0)
        def GT(self):
            return self.getToken(SParser.GT, 0)
        def typedef(self):
            return self.getTypedRuleContext(SParser.TypedefContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCursorType(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCursorType(self)


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
        _startState = 162
        self.enterRecursionRule(localctx, 162, self.RULE_typedef, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1409
            token = self._input.LA(1)
            if token in [SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.CODE, SParser.DOCUMENT, SParser.BLOB, SParser.IMAGE, SParser.UUID, SParser.TYPE_IDENTIFIER]:
                localctx = SParser.PrimaryTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1398 
                localctx.p = self.primary_type()

            elif token in [SParser.CURSOR]:
                localctx = SParser.CursorTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1399
                self.match(SParser.CURSOR)
                self.state = 1400
                self.match(SParser.LT)
                self.state = 1401 
                localctx.c = self.typedef(0)
                self.state = 1402
                self.match(SParser.GT)

            elif token in [SParser.ITERATOR]:
                localctx = SParser.IteratorTypeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1404
                self.match(SParser.ITERATOR)
                self.state = 1405
                self.match(SParser.LT)
                self.state = 1406 
                localctx.i = self.typedef(0)
                self.state = 1407
                self.match(SParser.GT)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 1421
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,88,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1419
                    la_ = self._interp.adaptivePredict(self._input,87,self._ctx)
                    if la_ == 1:
                        localctx = SParser.SetTypeContext(self, SParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.s = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1411
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 1412
                        self.match(SParser.LTGT)
                        pass

                    elif la_ == 2:
                        localctx = SParser.ListTypeContext(self, SParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1413
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 1414
                        self.match(SParser.LBRAK)
                        self.state = 1415
                        self.match(SParser.RBRAK)
                        pass

                    elif la_ == 3:
                        localctx = SParser.DictTypeContext(self, SParser.TypedefContext(self, _parentctx, _parentState))
                        localctx.d = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_typedef)
                        self.state = 1416
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1417
                        self.match(SParser.LCURL)
                        self.state = 1418
                        self.match(SParser.RCURL)
                        pass

             
                self.state = 1423
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,88,self._ctx)

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
        self.enterRule(localctx, 164, self.RULE_primary_type)
        try:
            self.state = 1426
            token = self._input.LA(1)
            if token in [SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.CODE, SParser.DOCUMENT, SParser.BLOB, SParser.IMAGE, SParser.UUID]:
                localctx = SParser.NativeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1424 
                localctx.n = self.native_type()

            elif token in [SParser.TYPE_IDENTIFIER]:
                localctx = SParser.CategoryTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1425 
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
        self.enterRule(localctx, 166, self.RULE_native_type)
        try:
            self.state = 1442
            token = self._input.LA(1)
            if token in [SParser.BOOLEAN]:
                localctx = SParser.BooleanTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1428
                self.match(SParser.BOOLEAN)

            elif token in [SParser.CHARACTER]:
                localctx = SParser.CharacterTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1429
                self.match(SParser.CHARACTER)

            elif token in [SParser.TEXT]:
                localctx = SParser.TextTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1430
                self.match(SParser.TEXT)

            elif token in [SParser.IMAGE]:
                localctx = SParser.ImageTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1431
                self.match(SParser.IMAGE)

            elif token in [SParser.INTEGER]:
                localctx = SParser.IntegerTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1432
                self.match(SParser.INTEGER)

            elif token in [SParser.DECIMAL]:
                localctx = SParser.DecimalTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1433
                self.match(SParser.DECIMAL)

            elif token in [SParser.DOCUMENT]:
                localctx = SParser.DocumentTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1434
                self.match(SParser.DOCUMENT)

            elif token in [SParser.DATE]:
                localctx = SParser.DateTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1435
                self.match(SParser.DATE)

            elif token in [SParser.DATETIME]:
                localctx = SParser.DateTimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1436
                self.match(SParser.DATETIME)

            elif token in [SParser.TIME]:
                localctx = SParser.TimeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1437
                self.match(SParser.TIME)

            elif token in [SParser.PERIOD]:
                localctx = SParser.PeriodTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1438
                self.match(SParser.PERIOD)

            elif token in [SParser.CODE]:
                localctx = SParser.CodeTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1439
                self.match(SParser.CODE)

            elif token in [SParser.BLOB]:
                localctx = SParser.BlobTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1440
                self.match(SParser.BLOB)

            elif token in [SParser.UUID]:
                localctx = SParser.UUIDTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1441
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
        self.enterRule(localctx, 168, self.RULE_category_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1444
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
        self.enterRule(localctx, 170, self.RULE_mutable_category_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1447
            _la = self._input.LA(1)
            if _la==SParser.MUTABLE:
                self.state = 1446
                self.match(SParser.MUTABLE)


            self.state = 1449 
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
        self.enterRule(localctx, 172, self.RULE_code_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1451
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
        self.enterRule(localctx, 174, self.RULE_category_declaration)
        try:
            self.state = 1456
            la_ = self._interp.adaptivePredict(self._input,92,self._ctx)
            if la_ == 1:
                localctx = SParser.ConcreteCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1453 
                localctx.decl = self.concrete_category_declaration()
                pass

            elif la_ == 2:
                localctx = SParser.NativeCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1454 
                localctx.decl = self.native_category_declaration()
                pass

            elif la_ == 3:
                localctx = SParser.SingletonCategoryDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1455 
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

        def type_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Type_identifierContext)
            else:
                return self.getTypedRuleContext(SParser.Type_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SParser.COMMA)
            else:
                return self.getToken(SParser.COMMA, i)

        def getRuleIndex(self):
            return SParser.RULE_type_identifier_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterType_identifier_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitType_identifier_list(self)




    def type_identifier_list(self):

        localctx = SParser.Type_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_type_identifier_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1458 
            self.type_identifier()
            self.state = 1463
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,93,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1459
                    self.match(SParser.COMMA)
                    self.state = 1460 
                    self.type_identifier() 
                self.state = 1465
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,93,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Method_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(SParser.Type_identifierContext,0)


        def getRuleIndex(self):
            return SParser.RULE_method_identifier

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMethod_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMethod_identifier(self)




    def method_identifier(self):

        localctx = SParser.Method_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_method_identifier)
        try:
            self.state = 1468
            token = self._input.LA(1)
            if token in [SParser.VARIABLE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1466 
                self.variable_identifier()

            elif token in [SParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1467 
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
            super(SParser.IdentifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_identifier

     
        def copyFrom(self, ctx):
            super(SParser.IdentifierContext, self).copyFrom(ctx)



    class TypeIdentifierContext(IdentifierContext):

        def __init__(self, parser, ctx): # actually a SParser.IdentifierContext)
            super(SParser.TypeIdentifierContext, self).__init__(parser)
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
        self.enterRule(localctx, 180, self.RULE_identifier)
        try:
            self.state = 1473
            token = self._input.LA(1)
            if token in [SParser.VARIABLE_IDENTIFIER]:
                localctx = SParser.VariableIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1470 
                self.variable_identifier()

            elif token in [SParser.TYPE_IDENTIFIER]:
                localctx = SParser.TypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1471 
                self.type_identifier()

            elif token in [SParser.SYMBOL_IDENTIFIER]:
                localctx = SParser.SymbolIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1472 
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
        self.enterRule(localctx, 182, self.RULE_variable_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1475
            self.match(SParser.VARIABLE_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Attribute_identifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIER(self):
            return self.getToken(SParser.VARIABLE_IDENTIFIER, 0)

        def STORABLE(self):
            return self.getToken(SParser.STORABLE, 0)

        def getRuleIndex(self):
            return SParser.RULE_attribute_identifier

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAttribute_identifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAttribute_identifier(self)




    def attribute_identifier(self):

        localctx = SParser.Attribute_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_attribute_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1477
            _la = self._input.LA(1)
            if not(_la==SParser.STORABLE or _la==SParser.VARIABLE_IDENTIFIER):
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
        self.enterRule(localctx, 186, self.RULE_type_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1479
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
        self.enterRule(localctx, 188, self.RULE_symbol_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1481
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

        def argument(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(SParser.ArgumentContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SParser.COMMA)
            else:
                return self.getToken(SParser.COMMA, i)

        def getRuleIndex(self):
            return SParser.RULE_argument_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterArgument_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitArgument_list(self)




    def argument_list(self):

        localctx = SParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1483 
            self.argument()
            self.state = 1488
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SParser.COMMA:
                self.state = 1484
                self.match(SParser.COMMA)
                self.state = 1485 
                self.argument()
                self.state = 1490
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
        self.enterRule(localctx, 192, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.state = 1496
            token = self._input.LA(1)
            if token in [SParser.CODE]:
                localctx = SParser.CodeArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1491 
                localctx.arg = self.code_argument()

            elif token in [SParser.MUTABLE, SParser.VARIABLE_IDENTIFIER]:
                localctx = SParser.OperatorArgumentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1493
                _la = self._input.LA(1)
                if _la==SParser.MUTABLE:
                    self.state = 1492
                    self.match(SParser.MUTABLE)


                self.state = 1495 
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

        def named_argument(self):
            return self.getTypedRuleContext(SParser.Named_argumentContext,0)


        def typed_argument(self):
            return self.getTypedRuleContext(SParser.Typed_argumentContext,0)


        def getRuleIndex(self):
            return SParser.RULE_operator_argument

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterOperator_argument(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitOperator_argument(self)




    def operator_argument(self):

        localctx = SParser.Operator_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_operator_argument)
        try:
            self.state = 1500
            la_ = self._interp.adaptivePredict(self._input,99,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1498 
                self.named_argument()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1499 
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
            super(SParser.Named_argumentContext, self).__init__(parent, invokingState)
            self.parser = parser

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
        self.enterRule(localctx, 196, self.RULE_named_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1502 
            self.variable_identifier()
            self.state = 1505
            _la = self._input.LA(1)
            if _la==SParser.EQ:
                self.state = 1503
                self.match(SParser.EQ)
                self.state = 1504 
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
        self.enterRule(localctx, 198, self.RULE_code_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1507 
            self.code_type()
            self.state = 1508 
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

        def typedef(self):
            return self.getTypedRuleContext(SParser.TypedefContext,0)


        def any_type(self):
            return self.getTypedRuleContext(SParser.Any_typeContext,0)


        def getRuleIndex(self):
            return SParser.RULE_category_or_any_type

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCategory_or_any_type(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCategory_or_any_type(self)




    def category_or_any_type(self):

        localctx = SParser.Category_or_any_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_category_or_any_type)
        try:
            self.state = 1512
            token = self._input.LA(1)
            if token in [SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.CODE, SParser.DOCUMENT, SParser.BLOB, SParser.IMAGE, SParser.UUID, SParser.ITERATOR, SParser.CURSOR, SParser.TYPE_IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1510 
                self.typedef(0)

            elif token in [SParser.ANY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1511 
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
            super(SParser.Any_typeContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_any_type

     
        def copyFrom(self, ctx):
            super(SParser.Any_typeContext, self).copyFrom(ctx)


    class AnyListTypeContext(Any_typeContext):

        def __init__(self, parser, ctx): # actually a SParser.Any_typeContext)
            super(SParser.AnyListTypeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def any_type(self):
            return self.getTypedRuleContext(SParser.Any_typeContext,0)

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)
        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)

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
            self.copyFrom(ctx)

        def any_type(self):
            return self.getTypedRuleContext(SParser.Any_typeContext,0)

        def LCURL(self):
            return self.getToken(SParser.LCURL, 0)
        def RCURL(self):
            return self.getToken(SParser.RCURL, 0)

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
        _startState = 202
        self.enterRecursionRule(localctx, 202, self.RULE_any_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.AnyTypeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1515
            self.match(SParser.ANY)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1525
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,103,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1523
                    la_ = self._interp.adaptivePredict(self._input,102,self._ctx)
                    if la_ == 1:
                        localctx = SParser.AnyListTypeContext(self, SParser.Any_typeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1517
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1518
                        self.match(SParser.LBRAK)
                        self.state = 1519
                        self.match(SParser.RBRAK)
                        pass

                    elif la_ == 2:
                        localctx = SParser.AnyDictTypeContext(self, SParser.Any_typeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_any_type)
                        self.state = 1520
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1521
                        self.match(SParser.LCURL)
                        self.state = 1522
                        self.match(SParser.RCURL)
                        pass

             
                self.state = 1527
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,103,self._ctx)

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

        def member_method_declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Member_method_declarationContext)
            else:
                return self.getTypedRuleContext(SParser.Member_method_declarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.LfpContext)
            else:
                return self.getTypedRuleContext(SParser.LfpContext,i)


        def getRuleIndex(self):
            return SParser.RULE_member_method_declaration_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMember_method_declaration_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMember_method_declaration_list(self)




    def member_method_declaration_list(self):

        localctx = SParser.Member_method_declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_member_method_declaration_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1528 
            self.member_method_declaration()
            self.state = 1534
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,104,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1529 
                    self.lfp()
                    self.state = 1530 
                    self.member_method_declaration() 
                self.state = 1536
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,104,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 206, self.RULE_member_method_declaration)
        try:
            self.state = 1542
            la_ = self._interp.adaptivePredict(self._input,105,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1537 
                self.setter_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1538 
                self.getter_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1539 
                self.concrete_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1540 
                self.abstract_method_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1541 
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

        def native_member_method_declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Native_member_method_declarationContext)
            else:
                return self.getTypedRuleContext(SParser.Native_member_method_declarationContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.LfpContext)
            else:
                return self.getTypedRuleContext(SParser.LfpContext,i)


        def getRuleIndex(self):
            return SParser.RULE_native_member_method_declaration_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNative_member_method_declaration_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNative_member_method_declaration_list(self)




    def native_member_method_declaration_list(self):

        localctx = SParser.Native_member_method_declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_native_member_method_declaration_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1544 
            self.native_member_method_declaration()
            self.state = 1550
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,106,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1545 
                    self.lfp()
                    self.state = 1546 
                    self.native_member_method_declaration() 
                self.state = 1552
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,106,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Native_member_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Native_member_method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def native_getter_declaration(self):
            return self.getTypedRuleContext(SParser.Native_getter_declarationContext,0)


        def native_setter_declaration(self):
            return self.getTypedRuleContext(SParser.Native_setter_declarationContext,0)


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
        self.enterRule(localctx, 210, self.RULE_native_member_method_declaration)
        try:
            self.state = 1556
            la_ = self._interp.adaptivePredict(self._input,107,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1553 
                self.native_getter_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1554 
                self.native_setter_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1555 
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
        self.enterRule(localctx, 212, self.RULE_native_category_binding)
        try:
            self.state = 1568
            token = self._input.LA(1)
            if token in [SParser.JAVA]:
                localctx = SParser.JavaCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1558
                self.match(SParser.JAVA)
                self.state = 1559 
                localctx.binding = self.java_class_identifier_expression(0)

            elif token in [SParser.CSHARP]:
                localctx = SParser.CSharpCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1560
                self.match(SParser.CSHARP)
                self.state = 1561 
                localctx.binding = self.csharp_identifier_expression(0)

            elif token in [SParser.PYTHON2]:
                localctx = SParser.Python2CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1562
                self.match(SParser.PYTHON2)
                self.state = 1563 
                localctx.binding = self.python_category_binding()

            elif token in [SParser.PYTHON3]:
                localctx = SParser.Python3CategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1564
                self.match(SParser.PYTHON3)
                self.state = 1565 
                localctx.binding = self.python_category_binding()

            elif token in [SParser.JAVASCRIPT]:
                localctx = SParser.JavaScriptCategoryBindingContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1566
                self.match(SParser.JAVASCRIPT)
                self.state = 1567 
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
        self.enterRule(localctx, 214, self.RULE_python_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1570 
            self.identifier()
            self.state = 1572
            la_ = self._interp.adaptivePredict(self._input,109,self._ctx)
            if la_ == 1:
                self.state = 1571 
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
        self.enterRule(localctx, 216, self.RULE_python_module)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1574
            self.match(SParser.FROM)
            self.state = 1575 
            self.module_token()
            self.state = 1576
            self.match(SParser.COLON)
            self.state = 1577 
            self.identifier()
            self.state = 1582
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,110,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1578
                    self.match(SParser.DOT)
                    self.state = 1579 
                    self.identifier() 
                self.state = 1584
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,110,self._ctx)

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
        self.enterRule(localctx, 218, self.RULE_javascript_category_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1585 
            self.identifier()
            self.state = 1587
            la_ = self._interp.adaptivePredict(self._input,111,self._ctx)
            if la_ == 1:
                self.state = 1586 
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
        self.enterRule(localctx, 220, self.RULE_javascript_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1589
            self.match(SParser.FROM)
            self.state = 1590 
            self.module_token()
            self.state = 1591
            self.match(SParser.COLON)
            self.state = 1593
            _la = self._input.LA(1)
            if _la==SParser.SLASH:
                self.state = 1592
                self.match(SParser.SLASH)


            self.state = 1595 
            self.javascript_identifier()
            self.state = 1600
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,113,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1596
                    self.match(SParser.SLASH)
                    self.state = 1597 
                    self.javascript_identifier() 
                self.state = 1602
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,113,self._ctx)

            self.state = 1605
            la_ = self._interp.adaptivePredict(self._input,114,self._ctx)
            if la_ == 1:
                self.state = 1603
                self.match(SParser.DOT)
                self.state = 1604 
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

        def variable_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Variable_identifierContext)
            else:
                return self.getTypedRuleContext(SParser.Variable_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SParser.COMMA)
            else:
                return self.getToken(SParser.COMMA, i)

        def getRuleIndex(self):
            return SParser.RULE_variable_identifier_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterVariable_identifier_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitVariable_identifier_list(self)




    def variable_identifier_list(self):

        localctx = SParser.Variable_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 222, self.RULE_variable_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1607 
            self.variable_identifier()
            self.state = 1612
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SParser.COMMA:
                self.state = 1608
                self.match(SParser.COMMA)
                self.state = 1609 
                self.variable_identifier()
                self.state = 1614
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
            super(SParser.Attribute_identifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def attribute_identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Attribute_identifierContext)
            else:
                return self.getTypedRuleContext(SParser.Attribute_identifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SParser.COMMA)
            else:
                return self.getToken(SParser.COMMA, i)

        def getRuleIndex(self):
            return SParser.RULE_attribute_identifier_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAttribute_identifier_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAttribute_identifier_list(self)




    def attribute_identifier_list(self):

        localctx = SParser.Attribute_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 224, self.RULE_attribute_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1615 
            self.attribute_identifier()
            self.state = 1620
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SParser.COMMA:
                self.state = 1616
                self.match(SParser.COMMA)
                self.state = 1617 
                self.attribute_identifier()
                self.state = 1622
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
            super(SParser.Method_declarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def abstract_method_declaration(self):
            return self.getTypedRuleContext(SParser.Abstract_method_declarationContext,0)


        def concrete_method_declaration(self):
            return self.getTypedRuleContext(SParser.Concrete_method_declarationContext,0)


        def native_method_declaration(self):
            return self.getTypedRuleContext(SParser.Native_method_declarationContext,0)


        def test_method_declaration(self):
            return self.getTypedRuleContext(SParser.Test_method_declarationContext,0)


        def getRuleIndex(self):
            return SParser.RULE_method_declaration

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterMethod_declaration(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitMethod_declaration(self)




    def method_declaration(self):

        localctx = SParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 226, self.RULE_method_declaration)
        try:
            self.state = 1627
            la_ = self._interp.adaptivePredict(self._input,117,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1623 
                self.abstract_method_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1624 
                self.concrete_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1625 
                self.native_method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1626 
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
        self.enterRule(localctx, 228, self.RULE_comment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1629
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

        def native_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Native_statementContext)
            else:
                return self.getTypedRuleContext(SParser.Native_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.LfpContext)
            else:
                return self.getTypedRuleContext(SParser.LfpContext,i)


        def getRuleIndex(self):
            return SParser.RULE_native_statement_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterNative_statement_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitNative_statement_list(self)




    def native_statement_list(self):

        localctx = SParser.Native_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 230, self.RULE_native_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1631 
            self.native_statement()
            self.state = 1637
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,118,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1632 
                    self.lfp()
                    self.state = 1633 
                    self.native_statement() 
                self.state = 1639
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,118,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 232, self.RULE_native_statement)
        try:
            self.state = 1650
            token = self._input.LA(1)
            if token in [SParser.JAVA]:
                localctx = SParser.JavaNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1640
                self.match(SParser.JAVA)
                self.state = 1641 
                self.java_statement()

            elif token in [SParser.CSHARP]:
                localctx = SParser.CSharpNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1642
                self.match(SParser.CSHARP)
                self.state = 1643 
                self.csharp_statement()

            elif token in [SParser.PYTHON2]:
                localctx = SParser.Python2NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1644
                self.match(SParser.PYTHON2)
                self.state = 1645 
                self.python_native_statement()

            elif token in [SParser.PYTHON3]:
                localctx = SParser.Python3NativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1646
                self.match(SParser.PYTHON3)
                self.state = 1647 
                self.python_native_statement()

            elif token in [SParser.JAVASCRIPT]:
                localctx = SParser.JavaScriptNativeStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1648
                self.match(SParser.JAVASCRIPT)
                self.state = 1649 
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
            super(SParser.Python_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

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
        self.enterRule(localctx, 234, self.RULE_python_native_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1652 
            self.python_statement()
            self.state = 1654
            _la = self._input.LA(1)
            if _la==SParser.SEMI:
                self.state = 1653
                self.match(SParser.SEMI)


            self.state = 1657
            _la = self._input.LA(1)
            if _la==SParser.FROM:
                self.state = 1656 
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
            super(SParser.Javascript_native_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

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
        self.enterRule(localctx, 236, self.RULE_javascript_native_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1659 
            self.javascript_statement()
            self.state = 1661
            _la = self._input.LA(1)
            if _la==SParser.SEMI:
                self.state = 1660
                self.match(SParser.SEMI)


            self.state = 1664
            _la = self._input.LA(1)
            if _la==SParser.FROM:
                self.state = 1663 
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
            super(SParser.Statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.StatementContext)
            else:
                return self.getTypedRuleContext(SParser.StatementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.LfpContext)
            else:
                return self.getTypedRuleContext(SParser.LfpContext,i)


        def getRuleIndex(self):
            return SParser.RULE_statement_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterStatement_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitStatement_list(self)




    def statement_list(self):

        localctx = SParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1666 
            self.statement()
            self.state = 1672
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,124,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1667 
                    self.lfp()
                    self.state = 1668 
                    self.statement() 
                self.state = 1674
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,124,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assertion_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Assertion_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assertion(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.AssertionContext)
            else:
                return self.getTypedRuleContext(SParser.AssertionContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.LfpContext)
            else:
                return self.getTypedRuleContext(SParser.LfpContext,i)


        def getRuleIndex(self):
            return SParser.RULE_assertion_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterAssertion_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitAssertion_list(self)




    def assertion_list(self):

        localctx = SParser.Assertion_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_assertion_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1675 
            self.assertion()
            self.state = 1681
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,125,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1676 
                    self.lfp()
                    self.state = 1677 
                    self.assertion() 
                self.state = 1683
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,125,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Switch_case_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Switch_case_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def switch_case_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Switch_case_statementContext)
            else:
                return self.getTypedRuleContext(SParser.Switch_case_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.LfpContext)
            else:
                return self.getTypedRuleContext(SParser.LfpContext,i)


        def getRuleIndex(self):
            return SParser.RULE_switch_case_statement_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterSwitch_case_statement_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitSwitch_case_statement_list(self)




    def switch_case_statement_list(self):

        localctx = SParser.Switch_case_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_switch_case_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1684 
            self.switch_case_statement()
            self.state = 1690
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,126,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1685 
                    self.lfp()
                    self.state = 1686 
                    self.switch_case_statement() 
                self.state = 1692
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,126,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Catch_statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SParser.Catch_statement_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def catch_statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Catch_statementContext)
            else:
                return self.getTypedRuleContext(SParser.Catch_statementContext,i)


        def lfp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.LfpContext)
            else:
                return self.getTypedRuleContext(SParser.LfpContext,i)


        def getRuleIndex(self):
            return SParser.RULE_catch_statement_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCatch_statement_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCatch_statement_list(self)




    def catch_statement_list(self):

        localctx = SParser.Catch_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_catch_statement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1693 
            self.catch_statement()
            self.state = 1699
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,127,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1694 
                    self.lfp()
                    self.state = 1695 
                    self.catch_statement() 
                self.state = 1701
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,127,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
            self.copyFrom(ctx)

        def LBRAK(self):
            return self.getToken(SParser.LBRAK, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(SParser.Literal_list_literalContext,0)

        def RBRAK(self):
            return self.getToken(SParser.RBRAK, 0)

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
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(SParser.LT, 0)
        def literal_list_literal(self):
            return self.getTypedRuleContext(SParser.Literal_list_literalContext,0)

        def GT(self):
            return self.getToken(SParser.GT, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterLiteralSetLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitLiteralSetLiteral(self)



    def literal_collection(self):

        localctx = SParser.Literal_collectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_literal_collection)
        try:
            self.state = 1716
            la_ = self._interp.adaptivePredict(self._input,128,self._ctx)
            if la_ == 1:
                localctx = SParser.LiteralRangeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1702
                self.match(SParser.LBRAK)
                self.state = 1703 
                localctx.low = self.atomic_literal()
                self.state = 1704
                self.match(SParser.RANGE)
                self.state = 1705 
                localctx.high = self.atomic_literal()
                self.state = 1706
                self.match(SParser.RBRAK)
                pass

            elif la_ == 2:
                localctx = SParser.LiteralListLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1708
                self.match(SParser.LBRAK)
                self.state = 1709 
                self.literal_list_literal()
                self.state = 1710
                self.match(SParser.RBRAK)
                pass

            elif la_ == 3:
                localctx = SParser.LiteralSetLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1712
                self.match(SParser.LT)
                self.state = 1713 
                self.literal_list_literal()
                self.state = 1714
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


    class UUIDLiteralContext(Atomic_literalContext):

        def __init__(self, parser, ctx): # actually a SParser.Atomic_literalContext)
            super(SParser.UUIDLiteralContext, self).__init__(parser)
            self.t = None # Token
            self.copyFrom(ctx)

        def UUID_LITERAL(self):
            return self.getToken(SParser.UUID_LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterUUIDLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitUUIDLiteral(self)


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
        self.enterRule(localctx, 248, self.RULE_atomic_literal)
        try:
            self.state = 1732
            token = self._input.LA(1)
            if token in [SParser.MIN_INTEGER]:
                localctx = SParser.MinIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1718
                localctx.t = self.match(SParser.MIN_INTEGER)

            elif token in [SParser.MAX_INTEGER]:
                localctx = SParser.MaxIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1719
                localctx.t = self.match(SParser.MAX_INTEGER)

            elif token in [SParser.INTEGER_LITERAL]:
                localctx = SParser.IntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1720
                localctx.t = self.match(SParser.INTEGER_LITERAL)

            elif token in [SParser.HEXA_LITERAL]:
                localctx = SParser.HexadecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1721
                localctx.t = self.match(SParser.HEXA_LITERAL)

            elif token in [SParser.CHAR_LITERAL]:
                localctx = SParser.CharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1722
                localctx.t = self.match(SParser.CHAR_LITERAL)

            elif token in [SParser.DATE_LITERAL]:
                localctx = SParser.DateLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1723
                localctx.t = self.match(SParser.DATE_LITERAL)

            elif token in [SParser.TIME_LITERAL]:
                localctx = SParser.TimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 1724
                localctx.t = self.match(SParser.TIME_LITERAL)

            elif token in [SParser.TEXT_LITERAL]:
                localctx = SParser.TextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 1725
                localctx.t = self.match(SParser.TEXT_LITERAL)

            elif token in [SParser.DECIMAL_LITERAL]:
                localctx = SParser.DecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 1726
                localctx.t = self.match(SParser.DECIMAL_LITERAL)

            elif token in [SParser.DATETIME_LITERAL]:
                localctx = SParser.DateTimeLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 1727
                localctx.t = self.match(SParser.DATETIME_LITERAL)

            elif token in [SParser.BOOLEAN_LITERAL]:
                localctx = SParser.BooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 1728
                localctx.t = self.match(SParser.BOOLEAN_LITERAL)

            elif token in [SParser.PERIOD_LITERAL]:
                localctx = SParser.PeriodLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 1729
                localctx.t = self.match(SParser.PERIOD_LITERAL)

            elif token in [SParser.UUID_LITERAL]:
                localctx = SParser.UUIDLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 1730
                localctx.t = self.match(SParser.UUID_LITERAL)

            elif token in [SParser.NONE]:
                localctx = SParser.NullLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 1731 
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

        def atomic_literal(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Atomic_literalContext)
            else:
                return self.getTypedRuleContext(SParser.Atomic_literalContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SParser.COMMA)
            else:
                return self.getToken(SParser.COMMA, i)

        def getRuleIndex(self):
            return SParser.RULE_literal_list_literal

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterLiteral_list_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitLiteral_list_literal(self)




    def literal_list_literal(self):

        localctx = SParser.Literal_list_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_literal_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1734 
            self.atomic_literal()
            self.state = 1739
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SParser.COMMA:
                self.state = 1735
                self.match(SParser.COMMA)
                self.state = 1736 
                self.atomic_literal()
                self.state = 1741
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
        self.enterRule(localctx, 252, self.RULE_selectable_expression)
        try:
            self.state = 1746
            la_ = self._interp.adaptivePredict(self._input,131,self._ctx)
            if la_ == 1:
                localctx = SParser.ParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1742 
                localctx.exp = self.parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = SParser.LiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1743 
                localctx.exp = self.literal_expression()
                pass

            elif la_ == 3:
                localctx = SParser.IdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1744 
                localctx.exp = self.identifier()
                pass

            elif la_ == 4:
                localctx = SParser.ThisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1745 
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
        self.enterRule(localctx, 254, self.RULE_this_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1748
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

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(SParser.ExpressionContext,0)


        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

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
        self.enterRule(localctx, 256, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1750
            self.match(SParser.LPAR)
            self.state = 1751 
            self.expression(0)
            self.state = 1752
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

        def atomic_literal(self):
            return self.getTypedRuleContext(SParser.Atomic_literalContext,0)


        def collection_literal(self):
            return self.getTypedRuleContext(SParser.Collection_literalContext,0)


        def getRuleIndex(self):
            return SParser.RULE_literal_expression

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterLiteral_expression(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitLiteral_expression(self)




    def literal_expression(self):

        localctx = SParser.Literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_literal_expression)
        try:
            self.state = 1756
            token = self._input.LA(1)
            if token in [SParser.NONE, SParser.BOOLEAN_LITERAL, SParser.CHAR_LITERAL, SParser.MIN_INTEGER, SParser.MAX_INTEGER, SParser.TEXT_LITERAL, SParser.UUID_LITERAL, SParser.INTEGER_LITERAL, SParser.HEXA_LITERAL, SParser.DECIMAL_LITERAL, SParser.DATETIME_LITERAL, SParser.TIME_LITERAL, SParser.DATE_LITERAL, SParser.PERIOD_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1754 
                self.atomic_literal()

            elif token in [SParser.LPAR, SParser.LBRAK, SParser.LCURL, SParser.LT, SParser.MUTABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1755 
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
            super(SParser.Collection_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def range_literal(self):
            return self.getTypedRuleContext(SParser.Range_literalContext,0)


        def list_literal(self):
            return self.getTypedRuleContext(SParser.List_literalContext,0)


        def set_literal(self):
            return self.getTypedRuleContext(SParser.Set_literalContext,0)


        def dict_literal(self):
            return self.getTypedRuleContext(SParser.Dict_literalContext,0)


        def tuple_literal(self):
            return self.getTypedRuleContext(SParser.Tuple_literalContext,0)


        def getRuleIndex(self):
            return SParser.RULE_collection_literal

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterCollection_literal(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitCollection_literal(self)




    def collection_literal(self):

        localctx = SParser.Collection_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_collection_literal)
        try:
            self.state = 1763
            la_ = self._interp.adaptivePredict(self._input,133,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1758 
                self.range_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1759 
                self.list_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1760 
                self.set_literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1761 
                self.dict_literal()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1762 
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
            super(SParser.Tuple_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(SParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SParser.RPAR, 0)

        def MUTABLE(self):
            return self.getToken(SParser.MUTABLE, 0)

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
        self.enterRule(localctx, 262, self.RULE_tuple_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1766
            _la = self._input.LA(1)
            if _la==SParser.MUTABLE:
                self.state = 1765
                self.match(SParser.MUTABLE)


            self.state = 1768
            self.match(SParser.LPAR)
            self.state = 1770
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT) | (1 << SParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (SParser.EXECUTE - 98)) | (1 << (SParser.FETCH - 98)) | (1 << (SParser.MUTABLE - 98)) | (1 << (SParser.NONE - 98)) | (1 << (SParser.NOT - 98)) | (1 << (SParser.READ - 98)) | (1 << (SParser.SELF - 98)) | (1 << (SParser.SORTED - 98)) | (1 << (SParser.THIS - 98)) | (1 << (SParser.BOOLEAN_LITERAL - 98)) | (1 << (SParser.CHAR_LITERAL - 98)) | (1 << (SParser.MIN_INTEGER - 98)) | (1 << (SParser.MAX_INTEGER - 98)) | (1 << (SParser.SYMBOL_IDENTIFIER - 98)) | (1 << (SParser.TYPE_IDENTIFIER - 98)) | (1 << (SParser.VARIABLE_IDENTIFIER - 98)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (SParser.TEXT_LITERAL - 164)) | (1 << (SParser.UUID_LITERAL - 164)) | (1 << (SParser.INTEGER_LITERAL - 164)) | (1 << (SParser.HEXA_LITERAL - 164)) | (1 << (SParser.DECIMAL_LITERAL - 164)) | (1 << (SParser.DATETIME_LITERAL - 164)) | (1 << (SParser.TIME_LITERAL - 164)) | (1 << (SParser.DATE_LITERAL - 164)) | (1 << (SParser.PERIOD_LITERAL - 164)))) != 0):
                self.state = 1769 
                self.expression_tuple()


            self.state = 1772
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

        def LCURL(self):
            return self.getToken(SParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(SParser.RCURL, 0)

        def MUTABLE(self):
            return self.getToken(SParser.MUTABLE, 0)

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
        self.enterRule(localctx, 264, self.RULE_dict_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1775
            _la = self._input.LA(1)
            if _la==SParser.MUTABLE:
                self.state = 1774
                self.match(SParser.MUTABLE)


            self.state = 1777
            self.match(SParser.LCURL)
            self.state = 1779
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT) | (1 << SParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (SParser.EXECUTE - 98)) | (1 << (SParser.FETCH - 98)) | (1 << (SParser.MUTABLE - 98)) | (1 << (SParser.NONE - 98)) | (1 << (SParser.NOT - 98)) | (1 << (SParser.READ - 98)) | (1 << (SParser.SELF - 98)) | (1 << (SParser.SORTED - 98)) | (1 << (SParser.THIS - 98)) | (1 << (SParser.BOOLEAN_LITERAL - 98)) | (1 << (SParser.CHAR_LITERAL - 98)) | (1 << (SParser.MIN_INTEGER - 98)) | (1 << (SParser.MAX_INTEGER - 98)) | (1 << (SParser.SYMBOL_IDENTIFIER - 98)) | (1 << (SParser.TYPE_IDENTIFIER - 98)) | (1 << (SParser.VARIABLE_IDENTIFIER - 98)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (SParser.TEXT_LITERAL - 164)) | (1 << (SParser.UUID_LITERAL - 164)) | (1 << (SParser.INTEGER_LITERAL - 164)) | (1 << (SParser.HEXA_LITERAL - 164)) | (1 << (SParser.DECIMAL_LITERAL - 164)) | (1 << (SParser.DATETIME_LITERAL - 164)) | (1 << (SParser.TIME_LITERAL - 164)) | (1 << (SParser.DATE_LITERAL - 164)) | (1 << (SParser.PERIOD_LITERAL - 164)))) != 0):
                self.state = 1778 
                self.dict_entry_list()


            self.state = 1781
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

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SParser.ExpressionContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SParser.COMMA)
            else:
                return self.getToken(SParser.COMMA, i)

        def getRuleIndex(self):
            return SParser.RULE_expression_tuple

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterExpression_tuple(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitExpression_tuple(self)




    def expression_tuple(self):

        localctx = SParser.Expression_tupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_expression_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1783 
            self.expression(0)
            self.state = 1784
            self.match(SParser.COMMA)
            self.state = 1793
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.LCURL) | (1 << SParser.MINUS) | (1 << SParser.LT) | (1 << SParser.CODE) | (1 << SParser.DOCUMENT) | (1 << SParser.BLOB))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (SParser.EXECUTE - 98)) | (1 << (SParser.FETCH - 98)) | (1 << (SParser.MUTABLE - 98)) | (1 << (SParser.NONE - 98)) | (1 << (SParser.NOT - 98)) | (1 << (SParser.READ - 98)) | (1 << (SParser.SELF - 98)) | (1 << (SParser.SORTED - 98)) | (1 << (SParser.THIS - 98)) | (1 << (SParser.BOOLEAN_LITERAL - 98)) | (1 << (SParser.CHAR_LITERAL - 98)) | (1 << (SParser.MIN_INTEGER - 98)) | (1 << (SParser.MAX_INTEGER - 98)) | (1 << (SParser.SYMBOL_IDENTIFIER - 98)) | (1 << (SParser.TYPE_IDENTIFIER - 98)) | (1 << (SParser.VARIABLE_IDENTIFIER - 98)))) != 0) or ((((_la - 164)) & ~0x3f) == 0 and ((1 << (_la - 164)) & ((1 << (SParser.TEXT_LITERAL - 164)) | (1 << (SParser.UUID_LITERAL - 164)) | (1 << (SParser.INTEGER_LITERAL - 164)) | (1 << (SParser.HEXA_LITERAL - 164)) | (1 << (SParser.DECIMAL_LITERAL - 164)) | (1 << (SParser.DATETIME_LITERAL - 164)) | (1 << (SParser.TIME_LITERAL - 164)) | (1 << (SParser.DATE_LITERAL - 164)) | (1 << (SParser.PERIOD_LITERAL - 164)))) != 0):
                self.state = 1785 
                self.expression(0)
                self.state = 1790
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SParser.COMMA:
                    self.state = 1786
                    self.match(SParser.COMMA)
                    self.state = 1787 
                    self.expression(0)
                    self.state = 1792
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
            super(SParser.Dict_entry_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def dict_entry(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SParser.Dict_entryContext)
            else:
                return self.getTypedRuleContext(SParser.Dict_entryContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SParser.COMMA)
            else:
                return self.getToken(SParser.COMMA, i)

        def getRuleIndex(self):
            return SParser.RULE_dict_entry_list

        def enterRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.enterDict_entry_list(self)

        def exitRule(self, listener):
            if isinstance( listener, SParserListener ):
                listener.exitDict_entry_list(self)




    def dict_entry_list(self):

        localctx = SParser.Dict_entry_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_dict_entry_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1795 
            self.dict_entry()
            self.state = 1800
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SParser.COMMA:
                self.state = 1796
                self.match(SParser.COMMA)
                self.state = 1797 
                self.dict_entry()
                self.state = 1802
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
        self.enterRule(localctx, 270, self.RULE_dict_entry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1803 
            localctx.key = self.expression(0)
            self.state = 1804
            self.match(SParser.COLON)
            self.state = 1805 
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
        self.enterRule(localctx, 272, self.RULE_slice_arguments)
        try:
            self.state = 1816
            la_ = self._interp.adaptivePredict(self._input,141,self._ctx)
            if la_ == 1:
                localctx = SParser.SliceFirstAndLastContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1807 
                localctx.first = self.expression(0)
                self.state = 1808
                self.match(SParser.COLON)
                self.state = 1809 
                localctx.last = self.expression(0)
                pass

            elif la_ == 2:
                localctx = SParser.SliceFirstOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1811 
                localctx.first = self.expression(0)
                self.state = 1812
                self.match(SParser.COLON)
                pass

            elif la_ == 3:
                localctx = SParser.SliceLastOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1814
                self.match(SParser.COLON)
                self.state = 1815 
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

        def variable_identifier(self):
            return self.getTypedRuleContext(SParser.Variable_identifierContext,0)


        def assign(self):
            return self.getTypedRuleContext(SParser.AssignContext,0)


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
        self.enterRule(localctx, 274, self.RULE_assign_variable_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1818 
            self.variable_identifier()
            self.state = 1819 
            self.assign()
            self.state = 1820 
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
            super(SParser.Assignable_instanceContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SParser.RULE_assignable_instance

     
        def copyFrom(self, ctx):
            super(SParser.Assignable_instanceContext, self).copyFrom(ctx)


    class ChildInstanceContext(Assignable_instanceContext):

        def __init__(self, parser, ctx): # actually a SParser.Assignable_instanceContext)
            super(SParser.ChildInstanceContext, self).__init__(parser)
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
        _startState = 276
        self.enterRecursionRule(localctx, 276, self.RULE_assignable_instance, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.RootInstanceContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1823 
            self.variable_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1829
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,142,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.ChildInstanceContext(self, SParser.Assignable_instanceContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignable_instance)
                    self.state = 1825
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1826 
                    self.child_instance() 
                self.state = 1831
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,142,self._ctx)

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
        self.enterRule(localctx, 278, self.RULE_is_expression)
        try:
            self.state = 1836
            la_ = self._interp.adaptivePredict(self._input,143,self._ctx)
            if la_ == 1:
                localctx = SParser.IsATypeExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1832
                if not self.willBeAOrAn():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$parser.willBeAOrAn()")
                self.state = 1833
                self.match(SParser.VARIABLE_IDENTIFIER)
                self.state = 1834 
                self.category_or_any_type()
                pass

            elif la_ == 2:
                localctx = SParser.IsOtherExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1835 
                self.expression(0)
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
        self.enterRule(localctx, 280, self.RULE_order_by_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1838 
            self.order_by()
            self.state = 1843
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,144,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1839
                    self.match(SParser.COMMA)
                    self.state = 1840 
                    self.order_by() 
                self.state = 1845
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,144,self._ctx)

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
        self.enterRule(localctx, 282, self.RULE_order_by)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1846 
            self.variable_identifier()
            self.state = 1851
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,145,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1847
                    self.match(SParser.DOT)
                    self.state = 1848 
                    self.variable_identifier() 
                self.state = 1853
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,145,self._ctx)

            self.state = 1855
            la_ = self._interp.adaptivePredict(self._input,146,self._ctx)
            if la_ == 1:
                self.state = 1854
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
        self.enterRule(localctx, 284, self.RULE_operator)
        try:
            self.state = 1863
            token = self._input.LA(1)
            if token in [SParser.PLUS]:
                localctx = SParser.OperatorPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1857
                self.match(SParser.PLUS)

            elif token in [SParser.MINUS]:
                localctx = SParser.OperatorMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1858
                self.match(SParser.MINUS)

            elif token in [SParser.STAR]:
                localctx = SParser.OperatorMultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1859 
                self.multiply()

            elif token in [SParser.SLASH]:
                localctx = SParser.OperatorDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1860 
                self.divide()

            elif token in [SParser.BSLASH]:
                localctx = SParser.OperatorIDivideContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1861 
                self.idivide()

            elif token in [SParser.PERCENT, SParser.MODULO]:
                localctx = SParser.OperatorModuloContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 1862 
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
        self.enterRule(localctx, 286, self.RULE_new_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1865
            localctx.i1 = self.match(SParser.VARIABLE_IDENTIFIER)
            self.state = 1866
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
        self.enterRule(localctx, 288, self.RULE_key_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1868
            localctx.i1 = self.match(SParser.VARIABLE_IDENTIFIER)
            self.state = 1869
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
        self.enterRule(localctx, 290, self.RULE_module_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1871
            localctx.i1 = self.match(SParser.VARIABLE_IDENTIFIER)
            self.state = 1872
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
        self.enterRule(localctx, 292, self.RULE_value_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1874
            localctx.i1 = self.match(SParser.VARIABLE_IDENTIFIER)
            self.state = 1875
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
        self.enterRule(localctx, 294, self.RULE_symbols_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1877
            localctx.i1 = self.match(SParser.VARIABLE_IDENTIFIER)
            self.state = 1878
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
        self.enterRule(localctx, 296, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1880
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
        self.enterRule(localctx, 298, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1882
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
        self.enterRule(localctx, 300, self.RULE_divide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1884
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
        self.enterRule(localctx, 302, self.RULE_idivide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1886
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
        self.enterRule(localctx, 304, self.RULE_modulo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1888
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
        self.enterRule(localctx, 306, self.RULE_javascript_statement)
        try:
            self.state = 1897
            token = self._input.LA(1)
            if token in [SParser.RETURN]:
                localctx = SParser.JavascriptReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1890
                self.match(SParser.RETURN)
                self.state = 1891 
                localctx.exp = self.javascript_expression(0)
                self.state = 1892
                self.match(SParser.SEMI)

            elif token in [SParser.LPAR, SParser.LBRAK, SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.SELF, SParser.TEST, SParser.THIS, SParser.WRITE, SParser.BOOLEAN_LITERAL, SParser.CHAR_LITERAL, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER, SParser.DOLLAR_IDENTIFIER, SParser.TEXT_LITERAL, SParser.INTEGER_LITERAL, SParser.DECIMAL_LITERAL]:
                localctx = SParser.JavascriptStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1894 
                localctx.exp = self.javascript_expression(0)
                self.state = 1895
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
        _startState = 308
        self.enterRecursionRule(localctx, 308, self.RULE_javascript_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavascriptPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1900 
            localctx.exp = self.javascript_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1906
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,149,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.JavascriptSelectorExpressionContext(self, SParser.Javascript_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_expression)
                    self.state = 1902
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1903 
                    localctx.child = self.javascript_selector_expression() 
                self.state = 1908
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,149,self._ctx)

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
        self.enterRule(localctx, 310, self.RULE_javascript_primary_expression)
        try:
            self.state = 1916
            la_ = self._interp.adaptivePredict(self._input,150,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1909 
                self.javascript_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1910 
                self.javascript_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1911 
                self.javascript_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1912 
                self.javascript_identifier_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1913 
                self.javascript_literal_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1914 
                self.javascript_method_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1915 
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
        self.enterRule(localctx, 312, self.RULE_javascript_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1918 
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
        self.enterRule(localctx, 314, self.RULE_javascript_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1920 
            self.new_token()
            self.state = 1921 
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
        self.enterRule(localctx, 316, self.RULE_javascript_selector_expression)
        try:
            self.state = 1928
            la_ = self._interp.adaptivePredict(self._input,151,self._ctx)
            if la_ == 1:
                localctx = SParser.JavaScriptMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1923
                self.match(SParser.DOT)
                self.state = 1924 
                localctx.method = self.javascript_method_expression()
                pass

            elif la_ == 2:
                localctx = SParser.JavaScriptMemberExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1925
                self.match(SParser.DOT)
                self.state = 1926 
                localctx.name = self.javascript_identifier()
                pass

            elif la_ == 3:
                localctx = SParser.JavaScriptItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1927 
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
        self.enterRule(localctx, 318, self.RULE_javascript_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1930 
            localctx.name = self.javascript_identifier()
            self.state = 1931
            self.match(SParser.LPAR)
            self.state = 1933
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.LBRAK) | (1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 131)) & ~0x3f) == 0 and ((1 << (_la - 131)) & ((1 << (SParser.READ - 131)) | (1 << (SParser.SELF - 131)) | (1 << (SParser.TEST - 131)) | (1 << (SParser.THIS - 131)) | (1 << (SParser.WRITE - 131)) | (1 << (SParser.BOOLEAN_LITERAL - 131)) | (1 << (SParser.CHAR_LITERAL - 131)) | (1 << (SParser.SYMBOL_IDENTIFIER - 131)) | (1 << (SParser.TYPE_IDENTIFIER - 131)) | (1 << (SParser.VARIABLE_IDENTIFIER - 131)) | (1 << (SParser.DOLLAR_IDENTIFIER - 131)) | (1 << (SParser.TEXT_LITERAL - 131)) | (1 << (SParser.INTEGER_LITERAL - 131)) | (1 << (SParser.DECIMAL_LITERAL - 131)))) != 0):
                self.state = 1932 
                localctx.args = self.javascript_arguments(0)


            self.state = 1935
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
        _startState = 320
        self.enterRecursionRule(localctx, 320, self.RULE_javascript_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavascriptArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1938 
            localctx.item = self.javascript_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1945
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,153,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.JavascriptArgumentListItemContext(self, SParser.Javascript_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_javascript_arguments)
                    self.state = 1940
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1941
                    self.match(SParser.COMMA)
                    self.state = 1942 
                    localctx.item = self.javascript_expression(0) 
                self.state = 1947
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,153,self._ctx)

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
        self.enterRule(localctx, 322, self.RULE_javascript_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1948
            self.match(SParser.LBRAK)
            self.state = 1949 
            localctx.exp = self.javascript_expression(0)
            self.state = 1950
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
        self.enterRule(localctx, 324, self.RULE_javascript_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1952
            self.match(SParser.LPAR)
            self.state = 1953 
            localctx.exp = self.javascript_expression(0)
            self.state = 1954
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
        self.enterRule(localctx, 326, self.RULE_javascript_identifier_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1956 
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
        self.enterRule(localctx, 328, self.RULE_javascript_literal_expression)
        try:
            self.state = 1963
            token = self._input.LA(1)
            if token in [SParser.INTEGER_LITERAL]:
                localctx = SParser.JavascriptIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1958
                localctx.t = self.match(SParser.INTEGER_LITERAL)

            elif token in [SParser.DECIMAL_LITERAL]:
                localctx = SParser.JavascriptDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1959
                localctx.t = self.match(SParser.DECIMAL_LITERAL)

            elif token in [SParser.TEXT_LITERAL]:
                localctx = SParser.JavascriptTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1960
                localctx.t = self.match(SParser.TEXT_LITERAL)

            elif token in [SParser.BOOLEAN_LITERAL]:
                localctx = SParser.JavascriptBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1961
                localctx.t = self.match(SParser.BOOLEAN_LITERAL)

            elif token in [SParser.CHAR_LITERAL]:
                localctx = SParser.JavascriptCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 1962
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
        self.enterRule(localctx, 330, self.RULE_javascript_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1965
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 131)) & ~0x3f) == 0 and ((1 << (_la - 131)) & ((1 << (SParser.READ - 131)) | (1 << (SParser.TEST - 131)) | (1 << (SParser.WRITE - 131)) | (1 << (SParser.SYMBOL_IDENTIFIER - 131)) | (1 << (SParser.TYPE_IDENTIFIER - 131)) | (1 << (SParser.VARIABLE_IDENTIFIER - 131)) | (1 << (SParser.DOLLAR_IDENTIFIER - 131)))) != 0)):
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
        self.enterRule(localctx, 332, self.RULE_python_statement)
        try:
            self.state = 1970
            token = self._input.LA(1)
            if token in [SParser.RETURN]:
                localctx = SParser.PythonReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1967
                self.match(SParser.RETURN)
                self.state = 1968 
                localctx.exp = self.python_expression(0)

            elif token in [SParser.LPAR, SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.SELF, SParser.TEST, SParser.THIS, SParser.WRITE, SParser.BOOLEAN_LITERAL, SParser.CHAR_LITERAL, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER, SParser.DOLLAR_IDENTIFIER, SParser.TEXT_LITERAL, SParser.INTEGER_LITERAL, SParser.DECIMAL_LITERAL]:
                localctx = SParser.PythonStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1969 
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
        _startState = 334
        self.enterRecursionRule(localctx, 334, self.RULE_python_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.PythonPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 1973 
            localctx.exp = self.python_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1979
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,156,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.PythonSelectorExpressionContext(self, SParser.Python_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_expression)
                    self.state = 1975
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1976 
                    localctx.child = self.python_selector_expression() 
                self.state = 1981
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,156,self._ctx)

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
        self.enterRule(localctx, 336, self.RULE_python_primary_expression)
        try:
            self.state = 1986
            la_ = self._interp.adaptivePredict(self._input,157,self._ctx)
            if la_ == 1:
                localctx = SParser.PythonParenthesisExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1982 
                localctx.exp = self.python_parenthesis_expression()
                pass

            elif la_ == 2:
                localctx = SParser.PythonIdentifierExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1983 
                localctx.exp = self.python_identifier_expression(0)
                pass

            elif la_ == 3:
                localctx = SParser.PythonLiteralExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 1984 
                localctx.exp = self.python_literal_expression()
                pass

            elif la_ == 4:
                localctx = SParser.PythonGlobalMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 1985 
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
        self.enterRule(localctx, 338, self.RULE_python_selector_expression)
        try:
            self.state = 1994
            token = self._input.LA(1)
            if token in [SParser.DOT]:
                localctx = SParser.PythonMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 1988
                self.match(SParser.DOT)
                self.state = 1989 
                localctx.exp = self.python_method_expression()

            elif token in [SParser.LBRAK]:
                localctx = SParser.PythonItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 1990
                self.match(SParser.LBRAK)
                self.state = 1991 
                localctx.exp = self.python_expression(0)
                self.state = 1992
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
        self.enterRule(localctx, 340, self.RULE_python_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1996 
            localctx.name = self.python_identifier()
            self.state = 1997
            self.match(SParser.LPAR)
            self.state = 1999
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 131)) & ~0x3f) == 0 and ((1 << (_la - 131)) & ((1 << (SParser.READ - 131)) | (1 << (SParser.SELF - 131)) | (1 << (SParser.TEST - 131)) | (1 << (SParser.THIS - 131)) | (1 << (SParser.WRITE - 131)) | (1 << (SParser.BOOLEAN_LITERAL - 131)) | (1 << (SParser.CHAR_LITERAL - 131)) | (1 << (SParser.SYMBOL_IDENTIFIER - 131)) | (1 << (SParser.TYPE_IDENTIFIER - 131)) | (1 << (SParser.VARIABLE_IDENTIFIER - 131)) | (1 << (SParser.DOLLAR_IDENTIFIER - 131)) | (1 << (SParser.TEXT_LITERAL - 131)) | (1 << (SParser.INTEGER_LITERAL - 131)) | (1 << (SParser.DECIMAL_LITERAL - 131)))) != 0):
                self.state = 1998 
                localctx.args = self.python_argument_list()


            self.state = 2001
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
        self.enterRule(localctx, 342, self.RULE_python_argument_list)
        try:
            self.state = 2009
            la_ = self._interp.adaptivePredict(self._input,160,self._ctx)
            if la_ == 1:
                localctx = SParser.PythonOrdinalOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2003 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                pass

            elif la_ == 2:
                localctx = SParser.PythonNamedOnlyArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2004 
                localctx.named = self.python_named_argument_list(0)
                pass

            elif la_ == 3:
                localctx = SParser.PythonArgumentListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2005 
                localctx.ordinal = self.python_ordinal_argument_list(0)
                self.state = 2006
                self.match(SParser.COMMA)
                self.state = 2007 
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
        _startState = 344
        self.enterRecursionRule(localctx, 344, self.RULE_python_ordinal_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.PythonOrdinalArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2012 
            localctx.item = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2019
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,161,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.PythonOrdinalArgumentListItemContext(self, SParser.Python_ordinal_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_ordinal_argument_list)
                    self.state = 2014
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2015
                    self.match(SParser.COMMA)
                    self.state = 2016 
                    localctx.item = self.python_expression(0) 
                self.state = 2021
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,161,self._ctx)

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
        _startState = 346
        self.enterRecursionRule(localctx, 346, self.RULE_python_named_argument_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.PythonNamedArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2023 
            localctx.name = self.python_identifier()
            self.state = 2024
            self.match(SParser.EQ)
            self.state = 2025 
            localctx.exp = self.python_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2035
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,162,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.PythonNamedArgumentListItemContext(self, SParser.Python_named_argument_listContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_named_argument_list)
                    self.state = 2027
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2028
                    self.match(SParser.COMMA)
                    self.state = 2029 
                    localctx.name = self.python_identifier()
                    self.state = 2030
                    self.match(SParser.EQ)
                    self.state = 2031 
                    localctx.exp = self.python_expression(0) 
                self.state = 2037
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,162,self._ctx)

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
        self.enterRule(localctx, 348, self.RULE_python_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2038
            self.match(SParser.LPAR)
            self.state = 2039 
            localctx.exp = self.python_expression(0)
            self.state = 2040
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
        _startState = 350
        self.enterRecursionRule(localctx, 350, self.RULE_python_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2045
            token = self._input.LA(1)
            if token in [SParser.DOLLAR_IDENTIFIER]:
                localctx = SParser.PythonPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2043
                self.match(SParser.DOLLAR_IDENTIFIER)

            elif token in [SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.SELF, SParser.TEST, SParser.THIS, SParser.WRITE, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER]:
                localctx = SParser.PythonIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2044 
                localctx.name = self.python_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2052
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,164,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.PythonChildIdentifierContext(self, SParser.Python_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_python_identifier_expression)
                    self.state = 2047
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2048
                    self.match(SParser.DOT)
                    self.state = 2049 
                    localctx.name = self.python_identifier() 
                self.state = 2054
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,164,self._ctx)

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
        self.enterRule(localctx, 352, self.RULE_python_literal_expression)
        try:
            self.state = 2060
            token = self._input.LA(1)
            if token in [SParser.INTEGER_LITERAL]:
                localctx = SParser.PythonIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2055
                localctx.t = self.match(SParser.INTEGER_LITERAL)

            elif token in [SParser.DECIMAL_LITERAL]:
                localctx = SParser.PythonDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2056
                localctx.t = self.match(SParser.DECIMAL_LITERAL)

            elif token in [SParser.TEXT_LITERAL]:
                localctx = SParser.PythonTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2057
                localctx.t = self.match(SParser.TEXT_LITERAL)

            elif token in [SParser.BOOLEAN_LITERAL]:
                localctx = SParser.PythonBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2058
                localctx.t = self.match(SParser.BOOLEAN_LITERAL)

            elif token in [SParser.CHAR_LITERAL]:
                localctx = SParser.PythonCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2059
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
        self.enterRule(localctx, 354, self.RULE_python_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2062
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 131)) & ~0x3f) == 0 and ((1 << (_la - 131)) & ((1 << (SParser.READ - 131)) | (1 << (SParser.SELF - 131)) | (1 << (SParser.TEST - 131)) | (1 << (SParser.THIS - 131)) | (1 << (SParser.WRITE - 131)) | (1 << (SParser.SYMBOL_IDENTIFIER - 131)) | (1 << (SParser.TYPE_IDENTIFIER - 131)) | (1 << (SParser.VARIABLE_IDENTIFIER - 131)))) != 0)):
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
        self.enterRule(localctx, 356, self.RULE_java_statement)
        try:
            self.state = 2071
            token = self._input.LA(1)
            if token in [SParser.RETURN]:
                localctx = SParser.JavaReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2064
                self.match(SParser.RETURN)
                self.state = 2065 
                localctx.exp = self.java_expression(0)
                self.state = 2066
                self.match(SParser.SEMI)

            elif token in [SParser.LPAR, SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.SELF, SParser.TEST, SParser.THIS, SParser.WRITE, SParser.BOOLEAN_LITERAL, SParser.CHAR_LITERAL, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER, SParser.NATIVE_IDENTIFIER, SParser.DOLLAR_IDENTIFIER, SParser.TEXT_LITERAL, SParser.INTEGER_LITERAL, SParser.DECIMAL_LITERAL]:
                localctx = SParser.JavaStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2068 
                localctx.exp = self.java_expression(0)
                self.state = 2069
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
        _startState = 358
        self.enterRecursionRule(localctx, 358, self.RULE_java_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavaPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2074 
            localctx.exp = self.java_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2080
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,167,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.JavaSelectorExpressionContext(self, SParser.Java_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_expression)
                    self.state = 2076
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2077 
                    localctx.child = self.java_selector_expression() 
                self.state = 2082
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,167,self._ctx)

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
        self.enterRule(localctx, 360, self.RULE_java_primary_expression)
        try:
            self.state = 2088
            la_ = self._interp.adaptivePredict(self._input,168,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2083 
                self.java_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2084 
                self.java_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2085 
                self.java_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2086 
                self.java_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2087 
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
        self.enterRule(localctx, 362, self.RULE_java_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2090 
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
        self.enterRule(localctx, 364, self.RULE_java_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2092 
            self.new_token()
            self.state = 2093 
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
        self.enterRule(localctx, 366, self.RULE_java_selector_expression)
        try:
            self.state = 2098
            token = self._input.LA(1)
            if token in [SParser.DOT]:
                localctx = SParser.JavaMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2095
                self.match(SParser.DOT)
                self.state = 2096 
                localctx.exp = self.java_method_expression()

            elif token in [SParser.LBRAK]:
                localctx = SParser.JavaItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2097 
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
        self.enterRule(localctx, 368, self.RULE_java_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2100 
            localctx.name = self.java_identifier()
            self.state = 2101
            self.match(SParser.LPAR)
            self.state = 2103
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 131)) & ~0x3f) == 0 and ((1 << (_la - 131)) & ((1 << (SParser.READ - 131)) | (1 << (SParser.SELF - 131)) | (1 << (SParser.TEST - 131)) | (1 << (SParser.THIS - 131)) | (1 << (SParser.WRITE - 131)) | (1 << (SParser.BOOLEAN_LITERAL - 131)) | (1 << (SParser.CHAR_LITERAL - 131)) | (1 << (SParser.SYMBOL_IDENTIFIER - 131)) | (1 << (SParser.TYPE_IDENTIFIER - 131)) | (1 << (SParser.VARIABLE_IDENTIFIER - 131)) | (1 << (SParser.NATIVE_IDENTIFIER - 131)) | (1 << (SParser.DOLLAR_IDENTIFIER - 131)) | (1 << (SParser.TEXT_LITERAL - 131)) | (1 << (SParser.INTEGER_LITERAL - 131)) | (1 << (SParser.DECIMAL_LITERAL - 131)))) != 0):
                self.state = 2102 
                localctx.args = self.java_arguments(0)


            self.state = 2105
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
        _startState = 370
        self.enterRecursionRule(localctx, 370, self.RULE_java_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavaArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2108 
            localctx.item = self.java_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2115
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,171,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.JavaArgumentListItemContext(self, SParser.Java_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_arguments)
                    self.state = 2110
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2111
                    self.match(SParser.COMMA)
                    self.state = 2112 
                    localctx.item = self.java_expression(0) 
                self.state = 2117
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,171,self._ctx)

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
        self.enterRule(localctx, 372, self.RULE_java_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2118
            self.match(SParser.LBRAK)
            self.state = 2119 
            localctx.exp = self.java_expression(0)
            self.state = 2120
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
        self.enterRule(localctx, 374, self.RULE_java_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2122
            self.match(SParser.LPAR)
            self.state = 2123 
            localctx.exp = self.java_expression(0)
            self.state = 2124
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
        _startState = 376
        self.enterRecursionRule(localctx, 376, self.RULE_java_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavaIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2127 
            localctx.name = self.java_identifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2134
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,172,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.JavaChildIdentifierContext(self, SParser.Java_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_identifier_expression)
                    self.state = 2129
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2130
                    self.match(SParser.DOT)
                    self.state = 2131 
                    localctx.name = self.java_identifier() 
                self.state = 2136
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,172,self._ctx)

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
        _startState = 378
        self.enterRecursionRule(localctx, 378, self.RULE_java_class_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.JavaClassIdentifierContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2138 
            localctx.klass = self.java_identifier_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2144
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,173,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.JavaChildClassIdentifierContext(self, SParser.Java_class_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_java_class_identifier_expression)
                    self.state = 2140
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2141
                    localctx.name = self.match(SParser.DOLLAR_IDENTIFIER) 
                self.state = 2146
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,173,self._ctx)

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
        self.enterRule(localctx, 380, self.RULE_java_literal_expression)
        try:
            self.state = 2152
            token = self._input.LA(1)
            if token in [SParser.INTEGER_LITERAL]:
                localctx = SParser.JavaIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2147
                localctx.t = self.match(SParser.INTEGER_LITERAL)

            elif token in [SParser.DECIMAL_LITERAL]:
                localctx = SParser.JavaDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2148
                localctx.t = self.match(SParser.DECIMAL_LITERAL)

            elif token in [SParser.TEXT_LITERAL]:
                localctx = SParser.JavaTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2149
                localctx.t = self.match(SParser.TEXT_LITERAL)

            elif token in [SParser.BOOLEAN_LITERAL]:
                localctx = SParser.JavaBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2150
                localctx.t = self.match(SParser.BOOLEAN_LITERAL)

            elif token in [SParser.CHAR_LITERAL]:
                localctx = SParser.JavaCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2151
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
        self.enterRule(localctx, 382, self.RULE_java_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2154
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 131)) & ~0x3f) == 0 and ((1 << (_la - 131)) & ((1 << (SParser.READ - 131)) | (1 << (SParser.TEST - 131)) | (1 << (SParser.WRITE - 131)) | (1 << (SParser.SYMBOL_IDENTIFIER - 131)) | (1 << (SParser.TYPE_IDENTIFIER - 131)) | (1 << (SParser.VARIABLE_IDENTIFIER - 131)) | (1 << (SParser.NATIVE_IDENTIFIER - 131)) | (1 << (SParser.DOLLAR_IDENTIFIER - 131)))) != 0)):
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
        self.enterRule(localctx, 384, self.RULE_csharp_statement)
        try:
            self.state = 2163
            token = self._input.LA(1)
            if token in [SParser.RETURN]:
                localctx = SParser.CSharpReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2156
                self.match(SParser.RETURN)
                self.state = 2157 
                localctx.exp = self.csharp_expression(0)
                self.state = 2158
                self.match(SParser.SEMI)

            elif token in [SParser.LPAR, SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.SELF, SParser.TEST, SParser.THIS, SParser.WRITE, SParser.BOOLEAN_LITERAL, SParser.CHAR_LITERAL, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER, SParser.DOLLAR_IDENTIFIER, SParser.TEXT_LITERAL, SParser.INTEGER_LITERAL, SParser.DECIMAL_LITERAL]:
                localctx = SParser.CSharpStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2160 
                localctx.exp = self.csharp_expression(0)
                self.state = 2161
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
        _startState = 386
        self.enterRecursionRule(localctx, 386, self.RULE_csharp_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.CSharpPrimaryExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2166 
            localctx.exp = self.csharp_primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2172
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,176,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CSharpSelectorExpressionContext(self, SParser.Csharp_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_expression)
                    self.state = 2168
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2169 
                    localctx.child = self.csharp_selector_expression() 
                self.state = 2174
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,176,self._ctx)

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
        self.enterRule(localctx, 388, self.RULE_csharp_primary_expression)
        try:
            self.state = 2180
            la_ = self._interp.adaptivePredict(self._input,177,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2175 
                self.csharp_this_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2176 
                self.csharp_new_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2177 
                self.csharp_parenthesis_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2178 
                self.csharp_identifier_expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2179 
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
        self.enterRule(localctx, 390, self.RULE_csharp_this_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2182 
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
        self.enterRule(localctx, 392, self.RULE_csharp_new_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2184 
            self.new_token()
            self.state = 2185 
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
        self.enterRule(localctx, 394, self.RULE_csharp_selector_expression)
        try:
            self.state = 2190
            token = self._input.LA(1)
            if token in [SParser.DOT]:
                localctx = SParser.CSharpMethodExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2187
                self.match(SParser.DOT)
                self.state = 2188 
                localctx.exp = self.csharp_method_expression()

            elif token in [SParser.LBRAK]:
                localctx = SParser.CSharpItemExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2189 
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
        self.enterRule(localctx, 396, self.RULE_csharp_method_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2192 
            localctx.name = self.csharp_identifier()
            self.state = 2193
            self.match(SParser.LPAR)
            self.state = 2195
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.LPAR) | (1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 131)) & ~0x3f) == 0 and ((1 << (_la - 131)) & ((1 << (SParser.READ - 131)) | (1 << (SParser.SELF - 131)) | (1 << (SParser.TEST - 131)) | (1 << (SParser.THIS - 131)) | (1 << (SParser.WRITE - 131)) | (1 << (SParser.BOOLEAN_LITERAL - 131)) | (1 << (SParser.CHAR_LITERAL - 131)) | (1 << (SParser.SYMBOL_IDENTIFIER - 131)) | (1 << (SParser.TYPE_IDENTIFIER - 131)) | (1 << (SParser.VARIABLE_IDENTIFIER - 131)) | (1 << (SParser.DOLLAR_IDENTIFIER - 131)) | (1 << (SParser.TEXT_LITERAL - 131)) | (1 << (SParser.INTEGER_LITERAL - 131)) | (1 << (SParser.DECIMAL_LITERAL - 131)))) != 0):
                self.state = 2194 
                localctx.args = self.csharp_arguments(0)


            self.state = 2197
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
        _startState = 398
        self.enterRecursionRule(localctx, 398, self.RULE_csharp_arguments, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SParser.CSharpArgumentListContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 2200 
            localctx.item = self.csharp_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2207
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,180,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CSharpArgumentListItemContext(self, SParser.Csharp_argumentsContext(self, _parentctx, _parentState))
                    localctx.items = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_arguments)
                    self.state = 2202
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2203
                    self.match(SParser.COMMA)
                    self.state = 2204 
                    localctx.item = self.csharp_expression(0) 
                self.state = 2209
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,180,self._ctx)

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
        self.enterRule(localctx, 400, self.RULE_csharp_item_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2210
            self.match(SParser.LBRAK)
            self.state = 2211 
            localctx.exp = self.csharp_expression(0)
            self.state = 2212
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
        self.enterRule(localctx, 402, self.RULE_csharp_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2214
            self.match(SParser.LPAR)
            self.state = 2215 
            localctx.exp = self.csharp_expression(0)
            self.state = 2216
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
        _startState = 404
        self.enterRecursionRule(localctx, 404, self.RULE_csharp_identifier_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2221
            token = self._input.LA(1)
            if token in [SParser.DOLLAR_IDENTIFIER]:
                localctx = SParser.CSharpPromptoIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2219
                self.match(SParser.DOLLAR_IDENTIFIER)

            elif token in [SParser.BOOLEAN, SParser.CHARACTER, SParser.TEXT, SParser.INTEGER, SParser.DECIMAL, SParser.DATE, SParser.TIME, SParser.DATETIME, SParser.PERIOD, SParser.READ, SParser.TEST, SParser.WRITE, SParser.SYMBOL_IDENTIFIER, SParser.TYPE_IDENTIFIER, SParser.VARIABLE_IDENTIFIER]:
                localctx = SParser.CSharpIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2220 
                localctx.name = self.csharp_identifier()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 2228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,182,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SParser.CSharpChildIdentifierContext(self, SParser.Csharp_identifier_expressionContext(self, _parentctx, _parentState))
                    localctx.parent = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_csharp_identifier_expression)
                    self.state = 2223
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2224
                    self.match(SParser.DOT)
                    self.state = 2225 
                    localctx.name = self.csharp_identifier() 
                self.state = 2230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,182,self._ctx)

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
        self.enterRule(localctx, 406, self.RULE_csharp_literal_expression)
        try:
            self.state = 2236
            token = self._input.LA(1)
            if token in [SParser.INTEGER_LITERAL]:
                localctx = SParser.CSharpIntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2231
                self.match(SParser.INTEGER_LITERAL)

            elif token in [SParser.DECIMAL_LITERAL]:
                localctx = SParser.CSharpDecimalLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 2232
                self.match(SParser.DECIMAL_LITERAL)

            elif token in [SParser.TEXT_LITERAL]:
                localctx = SParser.CSharpTextLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 2233
                self.match(SParser.TEXT_LITERAL)

            elif token in [SParser.BOOLEAN_LITERAL]:
                localctx = SParser.CSharpBooleanLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 2234
                self.match(SParser.BOOLEAN_LITERAL)

            elif token in [SParser.CHAR_LITERAL]:
                localctx = SParser.CSharpCharacterLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 2235
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
        self.enterRule(localctx, 408, self.RULE_csharp_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2238
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SParser.BOOLEAN) | (1 << SParser.CHARACTER) | (1 << SParser.TEXT) | (1 << SParser.INTEGER) | (1 << SParser.DECIMAL) | (1 << SParser.DATE) | (1 << SParser.TIME) | (1 << SParser.DATETIME) | (1 << SParser.PERIOD))) != 0) or ((((_la - 131)) & ~0x3f) == 0 and ((1 << (_la - 131)) & ((1 << (SParser.READ - 131)) | (1 << (SParser.TEST - 131)) | (1 << (SParser.WRITE - 131)) | (1 << (SParser.SYMBOL_IDENTIFIER - 131)) | (1 << (SParser.TYPE_IDENTIFIER - 131)) | (1 << (SParser.VARIABLE_IDENTIFIER - 131)))) != 0)):
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
        self._predicates[61] = self.child_instance_sempred
        self._predicates[81] = self.typedef_sempred
        self._predicates[101] = self.any_type_sempred
        self._predicates[138] = self.assignable_instance_sempred
        self._predicates[139] = self.is_expression_sempred
        self._predicates[143] = self.new_token_sempred
        self._predicates[144] = self.key_token_sempred
        self._predicates[145] = self.module_token_sempred
        self._predicates[146] = self.value_token_sempred
        self._predicates[147] = self.symbols_token_sempred
        self._predicates[154] = self.javascript_expression_sempred
        self._predicates[160] = self.javascript_arguments_sempred
        self._predicates[167] = self.python_expression_sempred
        self._predicates[172] = self.python_ordinal_argument_list_sempred
        self._predicates[173] = self.python_named_argument_list_sempred
        self._predicates[175] = self.python_identifier_expression_sempred
        self._predicates[179] = self.java_expression_sempred
        self._predicates[185] = self.java_arguments_sempred
        self._predicates[188] = self.java_identifier_expression_sempred
        self._predicates[189] = self.java_class_identifier_expression_sempred
        self._predicates[193] = self.csharp_expression_sempred
        self._predicates[199] = self.csharp_arguments_sempred
        self._predicates[202] = self.csharp_identifier_expression_sempred
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
         



